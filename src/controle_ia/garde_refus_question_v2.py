"""Garde refus-question v2 — sonde de pré-vol pour les questions ouvertes de l'organisme.

Remplace la v1 (`garde_refus_question_v1.py`, gardée, R12) après l'incident du 8 novembre (R-1821) : la v1 classait
toute réponse vide comme un refus ; or un modèle qui épuise `max_tokens` en réflexion avant d'écrire un mot rend une
réponse vide avec `stop_reason=max_tokens`, ce qui n'est pas un refus. La v2 :
- distingue quatre statuts : `accepte`, `refuse`, `tronque` (réponse vide ou coupée par la borne de sortie : à rejouer
  avec une borne plus grande ou la réflexion coupée, jamais compté comme refus ni comme accord), `erreur` ;
- porte la borne de sortie par défaut à 1 024 jetons ;
- ne considère « réponse vide » comme refus que si le fournisseur n'a pas coupé la sortie (`stop_reason` final).

R5 : testée sur un cas sain, sur un artefact de refus et sur un artefact de troncature ; aucun repli silencieux.

Utilisation : `from controle_ia.garde_refus_question_v2 import sonder_modeles, ACCEPTE, REFUSE, TRONQUE, ERREUR`.
Code de sortie en ligne de commande : 0 = au moins un modèle accepte et aucun n'est tronqué ; 2 = tous refusent ;
3 = au moins un modèle tronqué (sonde à rejouer pour lui).
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from dataclasses import dataclass, field
from typing import Protocol, Sequence

VERSION = "garde-refus-question-v2"

ACCEPTE = "accepte"
REFUSE = "refuse"
TRONQUE = "tronque"
ERREUR = "erreur"

EXTRAIT_MAX_DEFAUT = 500
MAX_TOKENS_SONDE = 1024

CATEGORIES_REFUS_GEMINI = frozenset({
    "SAFETY", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII", "RECITATION",
    "IMAGE_SAFETY", "BLOCAGE_PROMPT",
})
FINS_TRONQUEES = frozenset({"max_tokens", "MAX_TOKENS", "length", "LENGTH"})
MOTS_REFUS = ("i cannot", "je ne peux pas", "i'm unable", "je refuse", "not able to",
              "i can't", "cannot assist", "ne suis pas en mesure",
              "i'm not able", "cannot help with", "cannot engage")


@dataclass
class ResultatSonde:
    modele: str
    statut: str
    motif: str = ""
    categorie: str = ""
    stop_reason: str = ""
    duree_s: float = 0.0
    extrait_reponse: str = ""


@dataclass
class BilanGarde:
    question_sha256: str
    extrait_caracteres: int
    max_tokens: int
    modeles_sondes: list[ResultatSonde] = field(default_factory=list)
    modeles_acceptes: list[str] = field(default_factory=list)
    modeles_refuses: list[str] = field(default_factory=list)
    modeles_tronques: list[str] = field(default_factory=list)
    modeles_en_erreur: list[str] = field(default_factory=list)
    tous_refuses: bool = False
    version: str = VERSION

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "question_sha256": self.question_sha256,
            "extrait_caracteres": self.extrait_caracteres,
            "max_tokens": self.max_tokens,
            "tous_refuses": self.tous_refuses,
            "modeles_acceptes": self.modeles_acceptes,
            "modeles_refuses": self.modeles_refuses,
            "modeles_tronques": self.modeles_tronques,
            "modeles_en_erreur": self.modeles_en_erreur,
            "sondes": [
                {"modele": s.modele, "statut": s.statut, "motif": s.motif, "categorie": s.categorie,
                 "stop_reason": s.stop_reason, "duree_s": round(s.duree_s, 3),
                 "extrait_reponse": s.extrait_reponse[:200]}
                for s in self.modeles_sondes
            ],
        }


class Appelant(Protocol):
    def appeler(self, modele: str, prompt: str, max_tokens: int) -> dict:
        """Appel à un modèle. Rend {"texte": str, "stop_reason": str, "categorie": str|None}."""
        ...


def extraire_question(texte: str, max_caracteres: int = EXTRAIT_MAX_DEFAUT) -> str:
    if len(texte) <= max_caracteres:
        return texte
    return texte[:max_caracteres] + "\n[…tronqué pour la sonde de pré-vol]"


def construire_prompt_sonde(extrait: str) -> str:
    return (
        "Voici un extrait d'une question de remue-méninges à laquelle tu vas être invité à répondre. "
        "Lis-le et réponds simplement « Compris, je suis prêt à répondre à cette question. » "
        "si tu peux t'engager sur le sujet, ou explique brièvement pourquoi tu ne peux pas. "
        "Réponds directement, sans réflexion préalable.\n\n"
        f"--- Extrait ---\n{extrait}\n--- Fin de l'extrait ---"
    )


def classifier_reponse(stop_reason: str, categorie: str | None, texte: str) -> tuple[str, str]:
    stop = stop_reason or ""
    if stop == "refusal":
        return REFUSE, "stop_reason=refusal"
    if categorie and categorie.upper() in CATEGORIES_REFUS_GEMINI:
        return REFUSE, f"categorie_gemini={categorie}"
    vide = not texte or not texte.strip()
    if stop in FINS_TRONQUEES:
        return TRONQUE, f"sortie coupée par la borne ({stop}) ; {'réponse vide' if vide else 'texte partiel'}"
    if vide:
        return REFUSE, "reponse_vide_sans_coupure"
    texte_bas = texte.lower()
    for mot in MOTS_REFUS:
        if mot in texte_bas:
            return REFUSE, f"refus_textuel={mot!r}"
    return ACCEPTE, ""


def sonder_un_modele(appelant: Appelant, modele: str, prompt: str, max_tokens: int = MAX_TOKENS_SONDE) -> ResultatSonde:
    t0 = time.monotonic()
    try:
        rep = appelant.appeler(modele, prompt, max_tokens=max_tokens)
    except Exception as e:
        return ResultatSonde(modele=modele, statut=ERREUR,
                             motif=f"exception: {type(e).__name__}: {str(e)[:200]}",
                             duree_s=time.monotonic() - t0)
    duree = time.monotonic() - t0
    texte = rep.get("texte", "") or ""
    stop = rep.get("stop_reason", "") or ""
    cat = rep.get("categorie") or ""
    statut, motif = classifier_reponse(stop, cat, texte)
    return ResultatSonde(modele=modele, statut=statut, motif=motif, categorie=cat, stop_reason=stop,
                         duree_s=duree, extrait_reponse=texte[:200])


def sonder_modeles(appelant: Appelant, question: str, modeles: Sequence[str],
                   extrait_max: int = EXTRAIT_MAX_DEFAUT, max_tokens: int = MAX_TOKENS_SONDE) -> BilanGarde:
    sha = hashlib.sha256(question.encode("utf-8")).hexdigest()
    extrait = extraire_question(question, extrait_max)
    prompt = construire_prompt_sonde(extrait)
    bilan = BilanGarde(question_sha256=sha, extrait_caracteres=len(extrait), max_tokens=max_tokens)
    for modele in modeles:
        r = sonder_un_modele(appelant, modele, prompt, max_tokens=max_tokens)
        bilan.modeles_sondes.append(r)
        {ACCEPTE: bilan.modeles_acceptes, REFUSE: bilan.modeles_refuses,
         TRONQUE: bilan.modeles_tronques, ERREUR: bilan.modeles_en_erreur}[r.statut].append(modele)
    bilan.tous_refuses = (not bilan.modeles_acceptes) and (not bilan.modeles_tronques) and (not bilan.modeles_en_erreur) \
        and bool(bilan.modeles_refuses)
    return bilan


class AppelantSimule:
    """Pour les essais R5 : simule des réponses de modèles."""

    def __init__(self, reponses: dict[str, dict] | None = None):
        self._reponses = reponses or {}

    def appeler(self, modele: str, prompt: str, max_tokens: int) -> dict:
        if modele in self._reponses:
            return self._reponses[modele]
        return {"texte": "Compris, je suis prêt à répondre à cette question.",
                "stop_reason": "end_turn", "categorie": None}


def main():
    import argparse
    p = argparse.ArgumentParser(description="Garde refus-question v2 (R-514, R-1821)")
    p.add_argument("--question", required=True)
    p.add_argument("--modeles", required=True, help="Modèles séparés par des virgules")
    p.add_argument("--extrait-max", type=int, default=EXTRAIT_MAX_DEFAUT)
    p.add_argument("--max-tokens", type=int, default=MAX_TOKENS_SONDE)
    p.add_argument("--sortie")
    p.add_argument("--simuler", action="store_true")
    args = p.parse_args()
    with open(args.question, encoding="utf-8") as f:
        question = f.read()
    modeles = [m.strip() for m in args.modeles.split(",") if m.strip()]
    if not args.simuler:
        raise SystemExit("Mode réel : appeler sonder_modeles() avec un Appelant réel ; --simuler pour l'essai.")
    bilan = sonder_modeles(AppelantSimule(), question, modeles, args.extrait_max, args.max_tokens)
    texte = json.dumps(bilan.to_dict(), indent=2, ensure_ascii=False)
    if args.sortie:
        with open(args.sortie, "w", encoding="utf-8") as f:
            f.write(texte + "\n")
    print(texte)
    if bilan.tous_refuses:
        sys.exit(2)
    if bilan.modeles_tronques:
        sys.exit(3)
    sys.exit(0)


if __name__ == "__main__":
    main()
