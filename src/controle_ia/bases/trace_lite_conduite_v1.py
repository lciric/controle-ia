"""TRACE-lite en conduite réelle (lot L7, v1) : les deux fonctions que `trace_lite.executer` attend de l'appelant,
`generer(invite, rôle, graine_appel)` et `lire_score(invite, réponse imposée, valeurs)`, servies par un modèle de
`transformers`, avec un chronométrage par appel.

Conventions reprises du harnais, sans rien réécrire :
- chargement : `harnais.modeles.charger_modele` (liste blanche, révision figée en commit complet, bfloat16 vérifié),
  format `harnais.formats.FormatChat` à variables de gabarit figées (date d'en-tête), jetons d'arrêt
  `fins_du_modele` plus le premier jeton de clôture du tour (comme `lancer_pilote_a.charger_modele_et_format`) ;
  modèle jouet : `modele_jouet` et `tokeniseur_caracteres_chat`, fins « <|im_end|> » et fin de séquence ;
- génération : `harnais.episode.generer_lot` (remplissage à gauche, positions explicites, un générateur par appel
  semé par la graine que `executer` dérive par `SeedSequence`, R9) ;
- verdict : lecture forcée de `bases.scores_jetons` (`contexte_impose`, espérance sur les jetons « 1 » à « 5 » après
  `{"score": `, masse consignée), jamais un nombre généré puis relu.

**Le modèle observateur n'est pas fixé** (décision à venir) : son nom est un paramètre obligatoire, refusé hors de
`MODELES_AUTORISES` (révision figée exigée) ; le seul autre nom admis est `NOM_JOUET`, pour les essais sur
processeur, consigné « jouet » et sans valeur de mesure. Un modèle réel annoncé sous un autre nom que celui de ses
poids est refusé.

**Chronométrage** : chaque appel au modèle est consigné (rang, rôle, graine, jetons d'entrée, jetons de sortie,
secondes d'horloge murale, troncature ; masse pour le verdict). Les secondes comprennent le préremplissage et, sur
carte, une synchronisation avant chaque lecture d'horloge. Les appels d'un épisode se font un à un, dans l'ordre du
calendrier (chacun dépend des constats précédents) ; aucun lot entre épisodes en v1.

**Score manquant** : un épisode dont un appel ne peut pas aboutir — contexte plus long que ce que le modèle admet,
probabilité nulle ou non finie sur toutes les valeurs du verdict — n'a pas de score. La règle est un paramètre
obligatoire, sans défaut (R5) :
- `"arret"` : arrêt du run (`GardeArret`), cause citée ;
- `"exclure"` : l'épisode est rendu sans score (`score` à None, `exclu` vrai, cause, chronométrage des appels faits),
  pour qu'une règle d'exclusion déclarée d'avance le compte ; aucune valeur n'est jamais imputée.
Toute autre garde d'arrêt (journal invalide, sortie hors forme, score hors de [1, 5]) arrête dans les deux cas.
"""
from __future__ import annotations

import hashlib
import math
import time

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.episode import generer_lot
from ..harnais.modeles import MODELES_AUTORISES, exiger_modele_autorise
from . import trace_lite as tl
from .scores_jetons import contexte_impose, esperance, jetons_des_valeurs

VERSION = "trace-lite-conduite-v1"
NOM_JOUET = "jouet-caracteres"
REGLES_SCORE_MANQUANT = ("arret", "exclure")
ROLES_GENERATION = ("triage",) + tuple(tl.GABARIT_DE_L_ACTION)       # triage, InspectStep, CompareSteps, …


class ScoreManquant(Exception):
    """Interne : un appel ne peut pas aboutir ; traité par la règle écrite de l'observateur, jamais ailleurs."""


def _sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def _reel(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _entier(x) -> bool:
    return isinstance(x, (int, np.integer)) and not isinstance(x, bool)


def graines_episodes(graine_racine: int, n: int) -> list[int]:
    """Une graine par épisode, dérivée de la graine racine par `SeedSequence` (R9) ; l'épisode k reçoit toujours la même,
    quel que soit n. `executer` en dérive ensuite une par appel."""
    if not (_entier(graine_racine) and graine_racine >= 0) or not (_entier(n) and n >= 1):
        raise GardeArret(f"graine racine {graine_racine!r} ou nombre d'épisodes {n!r} invalide")
    return [int(e.generate_state(1)[0]) for e in np.random.SeedSequence(int(graine_racine)).spawn(int(n))]


class ObservateurTraceLite:
    """Modèle observateur de TRACE-lite, chargé par l'appelant (`charger_observateur` ou `observateur_jouet`).

    Paramètres tous obligatoires (le préenregistrement les fixe) : `nom` et `revision` du modèle, `systeme` (message
    système, éventuellement vide, consigné par son empreinte), `temperature` (≥ 0 ; 0 = choix du plus probable),
    `max_nouveaux` (un plafond par rôle de génération, `ROLES_GENERATION`), `regle_score_manquant`
    (`REGLES_SCORE_MANQUANT`)."""

    def __init__(self, modele, fmt, *, nom: str, revision: str | None, systeme: str, temperature: float,
                 max_nouveaux: dict[str, int], regle_score_manquant: str):
        self.jouet = _verifier_identite(modele, nom, revision)
        if not isinstance(systeme, str):
            raise GardeArret(f"message système de type {type(systeme).__name__} : texte attendu (vide permis)")
        if not (_reel(temperature) and temperature >= 0):
            raise GardeArret(f"température {temperature!r} : réel fini ≥ 0 attendu")
        if not isinstance(max_nouveaux, dict) or set(max_nouveaux) != set(ROLES_GENERATION):
            raise GardeArret(f"max_nouveaux : un plafond pour chacun de {list(ROLES_GENERATION)} attendu, "
                             f"pas {sorted(max_nouveaux) if isinstance(max_nouveaux, dict) else max_nouveaux!r}")
        if not all(_entier(v) and v >= 1 for v in max_nouveaux.values()):
            raise GardeArret(f"max_nouveaux {max_nouveaux} : entiers ≥ 1 attendus")
        if regle_score_manquant not in REGLES_SCORE_MANQUANT:
            raise GardeArret(f"règle de score manquant {regle_score_manquant!r} : une de {REGLES_SCORE_MANQUANT} "
                             "attendue (aucun défaut)")
        if not getattr(fmt, "fins", None):
            raise GardeArret("format sans jeton d'arrêt")
        self.modele, self.fmt, self.nom, self.revision = modele, fmt, nom, revision
        self.systeme, self.temperature = systeme, float(temperature)
        self.max_nouveaux = {k: int(v) for k, v in max_nouveaux.items()}
        self.regle = regle_score_manquant
        self.pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
        self.limite_contexte = int(getattr(modele.config, "max_position_embeddings", 0) or 0)
        if self.limite_contexte < 1:
            raise GardeArret("modèle sans longueur de contexte déclarée (max_position_embeddings)")
        self.appareil = next(modele.parameters()).device
        self._jetons = {tl.VALEURS_VERDICT: jetons_des_valeurs(fmt.tok, tl.VALEURS_VERDICT)}   # garde dès le départ
        self.chrono: list[dict] = []

    # --- description consignée ---------------------------------------------------------------------------------
    def description(self) -> dict:
        return {"version": VERSION, "nom": self.nom, "revision": self.revision, "jouet": self.jouet,
                "systeme_sha256": _sha(self.systeme), "temperature": self.temperature,
                "max_nouveaux": dict(self.max_nouveaux), "regle_score_manquant": self.regle,
                "fins": sorted(int(f) for f in self.fmt.fins), "pad": int(self.pad),
                "limite_contexte": self.limite_contexte, "appareil": str(self.appareil),
                "type_poids": str(next(self.modele.parameters()).dtype).replace("torch.", ""),
                "jetons_verdict": {str(k): v for k, v in self._jetons[tl.VALEURS_VERDICT].items()},
                "torch": torch.__version__}

    # --- chronométrage --------------------------------------------------------------------------------------------
    def _horloge(self) -> float:
        if self.appareil.type == "cuda":
            torch.cuda.synchronize(self.appareil)
        return time.perf_counter()

    def _consigner(self, **ligne) -> None:
        self.chrono.append({"rang": len(self.chrono) + 1, **ligne})

    def _contexte(self, invite: str, reponse_imposee: str = "") -> list[int]:
        if not isinstance(invite, str):
            raise GardeArret(f"invite de type {type(invite).__name__} : texte attendu")
        return contexte_impose(self.fmt, self.systeme, invite, reponse_imposee)

    # --- les deux fonctions attendues par `trace_lite.executer` ---------------------------------------------------
    def generer(self, invite: str, role: str, graine: int) -> tuple[str, bool]:
        """(texte, tronqué) ; tronqué = plafond du rôle atteint sans jeton d'arrêt."""
        if role not in self.max_nouveaux:
            raise GardeArret(f"rôle {role!r} inconnu : un de {list(ROLES_GENERATION)} attendu")
        if not (_entier(graine) and graine >= 0):
            raise GardeArret(f"graine d'appel {graine!r} : entier ≥ 0 attendu")
        plafond = self.max_nouveaux[role]
        depart = self._horloge()
        ctx = self._contexte(invite)
        if len(ctx) + plafond > self.limite_contexte:
            self._consigner(role=role, graine=int(graine), jetons_entree=len(ctx), jetons_sortie=0,
                            secondes=self._horloge() - depart, tronque=None, echec="contexte trop long")
            raise ScoreManquant(f"{role} : contexte de {len(ctx)} jetons + {plafond} à générer > limite du modèle "
                                f"({self.limite_contexte})")
        nouveaux, _ = generer_lot(self.modele, [ctx], plafond, self.temperature, [int(graine)], self.fmt.fins,
                                  self.pad)
        sortie = nouveaux[0]
        fini = bool(sortie) and sortie[-1] in self.fmt.fins
        texte = self.fmt.tok.decode(sortie[:-1] if fini else sortie, skip_special_tokens=True)
        self._consigner(role=role, graine=int(graine), jetons_entree=len(ctx), jetons_sortie=len(sortie),
                        secondes=self._horloge() - depart, tronque=not fini)
        return texte, not fini

    def lire_score(self, invite: str, reponse_imposee: str, valeurs: tuple) -> tuple[float, float]:
        """(espérance sur `valeurs` après la réponse imposée, masse de leurs jetons) par une passe unique."""
        valeurs = tuple(valeurs)
        if valeurs not in self._jetons:
            self._jetons[valeurs] = jetons_des_valeurs(self.fmt.tok, valeurs)
        depart = self._horloge()
        ctx = self._contexte(invite, reponse_imposee)
        if len(ctx) > self.limite_contexte:
            self._consigner(role="verdict", graine=None, jetons_entree=len(ctx), jetons_sortie=0,
                            secondes=self._horloge() - depart, masse=None, echec="contexte trop long")
            raise ScoreManquant(f"verdict : contexte de {len(ctx)} jetons > limite du modèle ({self.limite_contexte})")
        lp = _logits_derniere_position(self.modele, [ctx], self.pad)[0]
        try:
            score, masse = esperance(lp, self._jetons[valeurs])
        except GardeArret as e:
            self._consigner(role="verdict", graine=None, jetons_entree=len(ctx), jetons_sortie=0,
                            secondes=self._horloge() - depart, masse=None, echec=str(e))
            raise ScoreManquant(f"verdict : lecture forcée impossible ({e})") from e
        self._consigner(role="verdict", graine=None, jetons_entree=len(ctx), jetons_sortie=0,
                        secondes=self._horloge() - depart, masse=masse)
        return score, masse

    # --- un épisode -----------------------------------------------------------------------------------------------
    def juger(self, env, journal, graine: int, masse_min: float, gabarits: dict[str, str] | None = None) -> dict:
        """Un épisode jugé par TRACE-lite avec ce modèle. Rend la trace de `executer`, augmentée de `chronometrage`
        (une ligne par appel), de son résumé et de la description de l'observateur ; ou, si un score manque et que la
        règle est « exclure », un épisode sans score (`score` None, `exclu` vrai, cause)."""
        self.chrono = []
        try:
            trace = tl.executer(env, journal, self.generer, self.lire_score, graine=graine, masse_min=masse_min,
                                gabarits=gabarits)
        except ScoreManquant as e:
            if self.regle == "arret":
                raise GardeArret(f"score manquant ({e}) : règle « arret »") from e
            return {"graine": graine, "masse_min": float(masse_min), "score": None, "exclu": True, "cause": str(e),
                    "regle_score_manquant": self.regle, "chronometrage": list(self.chrono),
                    "resume_chronometrage": resume_chronometrage(self.chrono), "observateur": self.description()}
        if len(self.chrono) != trace["nombre_appels"]:
            raise GardeArret(f"{len(self.chrono)} appels chronométrés pour {trace['nombre_appels']} appels de "
                             "l'épisode")
        attendus = [trace["triage"]["graine"]] + [a["graine"] for a in trace["appels"]] + [None]
        if [c["graine"] for c in self.chrono] != attendus:
            raise GardeArret("graines chronométrées ≠ graines de la trace")
        return {**trace, "score": trace["verdict"]["score"], "exclu": False, "regle_score_manquant": self.regle,
                "chronometrage": list(self.chrono), "resume_chronometrage": resume_chronometrage(self.chrono),
                "observateur": self.description()}


def _logits_derniere_position(modele, contextes, pad):
    """Passe unique du harnais (`pilote_a.logits_derniere_position`), importée ici pour être remplaçable en essai."""
    from ..environnements.pilote_a import logits_derniere_position
    return logits_derniere_position(modele, contextes, pad)


def resume_chronometrage(chrono: list[dict]) -> dict:
    """Totaux d'un épisode : appels, jetons d'entrée et de sortie, secondes ; secondes et appels par rôle."""
    par_role: dict[str, dict] = {}
    for c in chrono:
        r = par_role.setdefault(c["role"], {"appels": 0, "secondes": 0.0, "jetons_entree": 0, "jetons_sortie": 0})
        r["appels"] += 1
        r["secondes"] += c["secondes"]
        r["jetons_entree"] += c["jetons_entree"]
        r["jetons_sortie"] += c["jetons_sortie"]
    return {"appels": len(chrono), "secondes": sum(c["secondes"] for c in chrono),
            "jetons_entree": sum(c["jetons_entree"] for c in chrono),
            "jetons_sortie": sum(c["jetons_sortie"] for c in chrono), "par_role": par_role}


def _verifier_identite(modele, nom: str, revision: str | None) -> bool:
    """Vrai pour le modèle jouet. Nom réel : liste blanche et révision figée (`exiger_modele_autorise`), poids chargés
    sous ce nom. Nom jouet : aucune révision, poids non chargés d'un dépôt."""
    if not isinstance(nom, str) or not nom:
        raise GardeArret(f"modèle observateur {nom!r} : nom obligatoire (le choix de l'observateur est une décision)")
    chargeur = getattr(getattr(modele, "config", None), "_name_or_path", None) or ""
    if nom == NOM_JOUET:
        if revision is not None:
            raise GardeArret("modèle jouet : aucune révision attendue")
        if chargeur:
            raise GardeArret(f"modèle jouet annoncé, mais poids chargés de {chargeur!r}")
        return True
    exiger_modele_autorise(nom, revision)
    if chargeur != nom:
        raise GardeArret(f"modèle annoncé {nom!r}, poids chargés de {chargeur or 'nulle part'!r}")
    return False


def charger_observateur(nom: str, revision: str, *, variables_gabarit: dict, systeme: str, temperature: float,
                        max_nouveaux: dict[str, int], regle_score_manquant: str, dtype: str = "bfloat16",
                        appareil: str = "cuda", attention: str = "sdpa", hors_ligne: bool = True,
                        cache_dir: str | None = None) -> ObservateurTraceLite:
    """Observateur réel (machines de calcul) : liste blanche et révision vérifiées avant tout chargement ; lecture du
    cache local seulement par défaut (`precharger_modele` avant). `variables_gabarit` (date d'en-tête figée, par
    exemple) : obligatoire, comme pour les juges du pilote."""
    exiger_modele_autorise(nom, revision)
    if not isinstance(variables_gabarit, dict):
        raise GardeArret("variables du gabarit de conversation : dictionnaire attendu (vide permis)")
    from ..harnais.formats import FormatChat
    from ..harnais.modeles import charger_modele, fins_du_modele

    modele, tok = charger_modele(nom, revision, dtype, appareil, attention, hors_ligne=hors_ligne,
                                 cache_dir=cache_dir)
    fmt = FormatChat(tok, variables=variables_gabarit)
    fmt.fins = fins_du_modele(modele, tok) | {fmt._pieces(("x", "y"))["cloture"][0]}
    return ObservateurTraceLite(modele, fmt, nom=nom, revision=revision, systeme=systeme, temperature=temperature,
                                max_nouveaux=max_nouveaux, regle_score_manquant=regle_score_manquant)


def observateur_jouet(graine: int, *, systeme: str, temperature: float, max_nouveaux: dict[str, int],
                      regle_score_manquant: str) -> ObservateurTraceLite:
    """Observateur jouet (processeur, hors ligne) : `modele_jouet` à poids aléatoires et tokeniseur par caractères à
    gabarit de conversation. Pour les essais seulement : aucune mesure."""
    from ..harnais.formats import FormatChat
    from ..harnais.modeles import modele_jouet, tokeniseur_caracteres_chat

    tok = tokeniseur_caracteres_chat()
    modele = modele_jouet(graine, len(tok), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    fmt = FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    return ObservateurTraceLite(modele, fmt, nom=NOM_JOUET, revision=None, systeme=systeme, temperature=temperature,
                                max_nouveaux=max_nouveaux, regle_score_manquant=regle_score_manquant)


__all__ = ["VERSION", "NOM_JOUET", "REGLES_SCORE_MANQUANT", "ROLES_GENERATION", "ObservateurTraceLite",
           "charger_observateur", "observateur_jouet", "graines_episodes", "resume_chronometrage", "MODELES_AUTORISES"]
