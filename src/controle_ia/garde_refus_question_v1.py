"""Garde refus-question v1 — sonde de pré-vol pour les questions ouvertes de l'organisme.

R-514 (conv-audit) : avant de lancer une course d'idéation sur une question, sonder chaque
modèle avec un extrait de la question. Un modèle qui refuse (stop_reason=refusal, catégorie de
sécurité, ou contenu vide) est consigné et retiré de la course. Si tous les modèles refusent,
la garde renvoie code 2 (arrêt propre).

R5 : testée sur un cas sain et sur un artefact ; aucun repli silencieux.

Utilisation (sans réseau, avec un simulateur) :
    from controle_ia.garde_refus_question_v1 import sonder_modeles, ACCEPTE, REFUSE

Utilisation (en réel, par un lanceur) :
    python -I -m controle_ia.garde_refus_question_v1 --question FICHIER --modeles m1,m2 \\
        [--extrait-max 500] [--sortie FICHIER.json]
    Code de sortie : 0 = au moins un modèle accepte ; 2 = tous refusent.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass, field
from typing import Protocol, Sequence

VERSION = "garde-refus-question-v1"

ACCEPTE = "accepte"
REFUSE = "refuse"
ERREUR = "erreur"

EXTRAIT_MAX_DEFAUT = 500

CATEGORIES_REFUS_GEMINI = frozenset({
    "SAFETY", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII", "RECITATION",
    "IMAGE_SAFETY", "BLOCAGE_PROMPT",
})


@dataclass
class ResultatSonde:
    modele: str
    statut: str  # ACCEPTE, REFUSE, ERREUR
    motif: str = ""
    categorie: str = ""
    duree_s: float = 0.0
    extrait_reponse: str = ""


@dataclass
class BilanGarde:
    question_sha256: str
    extrait_caracteres: int
    modeles_sondes: list[ResultatSonde] = field(default_factory=list)
    modeles_acceptes: list[str] = field(default_factory=list)
    modeles_refuses: list[str] = field(default_factory=list)
    modeles_en_erreur: list[str] = field(default_factory=list)
    tous_refuses: bool = False
    version: str = VERSION

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "question_sha256": self.question_sha256,
            "extrait_caracteres": self.extrait_caracteres,
            "tous_refuses": self.tous_refuses,
            "modeles_acceptes": self.modeles_acceptes,
            "modeles_refuses": self.modeles_refuses,
            "modeles_en_erreur": self.modeles_en_erreur,
            "sondes": [
                {"modele": s.modele, "statut": s.statut, "motif": s.motif,
                 "categorie": s.categorie, "duree_s": round(s.duree_s, 3),
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
        "si tu peux t'engager sur le sujet, ou explique brièvement pourquoi tu ne peux pas.\n\n"
        f"--- Extrait ---\n{extrait}\n--- Fin de l'extrait ---"
    )


def classifier_reponse(stop_reason: str, categorie: str | None, texte: str) -> tuple[str, str]:
    if stop_reason == "refusal":
        return REFUSE, f"stop_reason=refusal"
    if categorie and categorie.upper() in CATEGORIES_REFUS_GEMINI:
        return REFUSE, f"categorie_gemini={categorie}"
    if not texte or not texte.strip():
        return REFUSE, "reponse_vide"
    mots_refus = ("i cannot", "je ne peux pas", "i'm unable", "je refuse", "not able to",
                  "i can't", "cannot assist", "ne suis pas en mesure",
                  "i'm not able", "cannot help with", "cannot engage")
    texte_bas = texte.lower()
    for mot in mots_refus:
        if mot in texte_bas:
            return REFUSE, f"refus_textuel={mot!r}"
    return ACCEPTE, ""


def sonder_un_modele(appelant: Appelant, modele: str, prompt: str) -> ResultatSonde:
    t0 = time.monotonic()
    try:
        rep = appelant.appeler(modele, prompt, max_tokens=256)
    except Exception as e:
        return ResultatSonde(
            modele=modele, statut=ERREUR,
            motif=f"exception: {type(e).__name__}: {str(e)[:200]}",
            duree_s=time.monotonic() - t0)
    duree = time.monotonic() - t0
    texte = rep.get("texte", "")
    stop = rep.get("stop_reason", "")
    cat = rep.get("categorie") or ""
    statut, motif = classifier_reponse(stop, cat, texte)
    return ResultatSonde(
        modele=modele, statut=statut, motif=motif,
        categorie=cat, duree_s=duree,
        extrait_reponse=texte[:200] if texte else "")


def sonder_modeles(
    appelant: Appelant,
    question: str,
    modeles: Sequence[str],
    extrait_max: int = EXTRAIT_MAX_DEFAUT,
) -> BilanGarde:
    sha = hashlib.sha256(question.encode("utf-8")).hexdigest()
    extrait = extraire_question(question, extrait_max)
    prompt = construire_prompt_sonde(extrait)
    bilan = BilanGarde(question_sha256=sha, extrait_caracteres=len(extrait))
    for modele in modeles:
        r = sonder_un_modele(appelant, modele, prompt)
        bilan.modeles_sondes.append(r)
        if r.statut == ACCEPTE:
            bilan.modeles_acceptes.append(modele)
        elif r.statut == REFUSE:
            bilan.modeles_refuses.append(modele)
        else:
            bilan.modeles_en_erreur.append(modele)
    bilan.tous_refuses = len(bilan.modeles_acceptes) == 0
    return bilan


class AppelantSimule:
    """Pour les essais R5 : simule des réponses de modèles, avec ou sans refus."""

    def __init__(self, reponses: dict[str, dict] | None = None):
        self._reponses = reponses or {}

    def appeler(self, modele: str, prompt: str, max_tokens: int) -> dict:
        if modele in self._reponses:
            return self._reponses[modele]
        return {"texte": "Compris, je suis prêt à répondre à cette question.",
                "stop_reason": "end_turn", "categorie": None}


def main():
    import argparse
    p = argparse.ArgumentParser(description="Garde refus-question v1 (R-514)")
    p.add_argument("--question", required=True, help="Fichier contenant la question")
    p.add_argument("--modeles", required=True, help="Modèles séparés par des virgules")
    p.add_argument("--extrait-max", type=int, default=EXTRAIT_MAX_DEFAUT)
    p.add_argument("--sortie", help="Fichier JSON de sortie")
    p.add_argument("--simuler", action="store_true", help="Mode simulé (tous acceptent)")
    args = p.parse_args()

    with open(args.question, encoding="utf-8") as f:
        question = f.read()
    modeles = [m.strip() for m in args.modeles.split(",") if m.strip()]

    if args.simuler:
        appelant = AppelantSimule()
    else:
        raise SystemExit("Mode réel non implémenté dans cette version ; utiliser --simuler ou appeler sonder_modeles().")

    bilan = sonder_modeles(appelant, question, modeles, args.extrait_max)

    sortie = bilan.to_dict()
    texte_json = json.dumps(sortie, indent=2, ensure_ascii=False)

    if args.sortie:
        with open(args.sortie, "w", encoding="utf-8") as f:
            f.write(texte_json + "\n")
        print(f"Bilan écrit dans {args.sortie}", file=sys.stderr)

    print(texte_json)

    if bilan.tous_refuses:
        print(f"\nTous les modèles ont refusé ({len(bilan.modeles_refuses)}/{len(modeles)}).", file=sys.stderr)
        sys.exit(2)
    else:
        print(f"\n{len(bilan.modeles_acceptes)}/{len(modeles)} modèle(s) accepte(nt).", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
