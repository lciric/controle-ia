"""Sondes neuves de l'étape A de T0.7, v1 (brouillon 19, `07039ed2…` : plan, points 1 à 4 et 6 bis ; « Métrique » ; section
« Module » ; consigne de la mère `consigne-developpement-module-t07-v2-suite-sondes-neuves.md`, `5cfba438…`, décision 1).

Rien de ce que fait le paquet gelé n'est réécrit : apprentissage par `sondes.familles.entrainer` (cinq familles, `Reglages` par
défaut), Mahalanobis réécrite en produit matriciel par `t07.mahalanobis_v1.preparer_sonde` (miroir de
`familles_v2.entrainer_v2(…, calcul="produit_matriciel_v2")` : même sonde gelée, puis `en_produit_matriciel`, puis l'essai
d'égalité au paquet gelé, joué avant chaque usage ; un échec met **le couple** en « échec », jamais l'ensemble), aires par
`sondes.evaluation.scores_actions` et `aire_sous_courbe`, planchers par `plancher_apparie`, directions des concepts par
`sondes.temoins.direction_concept` et `plancher_concept`, témoins lexicaux par `temoin_lexical`, extraction par
`harnais.activations.passe_unique` sur les empans de `premier_test_ia.empans` (gabarit de dialogue du harnais).

1. **Jeux** (`lire_jeu`) : fichiers JSON Lines de la consigne v3 (`d9de50a6…`, section 3), un par ligne de registre
   `SCELLEMENT-JEUX-T07-JD`, `-JC`, `-JA` (sceaux déjà vérifiés par la garde) : clés, valeurs (`jeu`, `mode`, `etiquette`),
   paires complètes (deux membres A et B, une étiquette 0 et une 1), `position_cost` dans la réponse ; toute faute → arrêt.
   **Contrôle de disjonction** (`controler_disjonction`, plan, point 1) : aucune tâche d'un jeu n'est une tâche d'évaluation
   de la course 7b (identifiants de `episodes-t06.json`, fiches) ; sinon arrêt.
2. **Découpage** (`decouper_taches`) : 80 % des tâches de réserve pour l'entraînement, 20 % pour la validation générique,
   par tâche (les paires d'une tâche, et les deux membres d'une paire, du même côté), graine dérivée (clé « decoupage »),
   le même pour les trois jeux (« même découpage », plan 6 bis).
3. **Empans** (`Extracteur`) : J-D, les jetons de la réponse ; J-C (et J-A pour T7-P6), les jetons de l'action **avant** le
   champ `COST` (`reponse[:position_cost]`, DS-1 (a)) ; validation du domaine rapportée aussi **sur l'action entière**.
4. **Couples** (`entrainer_concept`) : deux concepts × cinq familles × trois couches = 30 couples ; aires de validation.
5. **Sonde principale** (`choisir_principale`) : meilleure aire de validation générique ; **ex aequo** (écart ≤
   `ecart_ex_aequo`, saturation comprise) départagés par famille (différence de moyennes, linéaire, perceptron, attention,
   Mahalanobis), puis couche (15, puis 7, puis 23 ; sur d'autres couches : celle du milieu, puis la plus basse, puis la plus
   haute), jamais par l'ordre ; la règle appliquée est écrite.
6. **T7-P6** (`sondes_p6`) : famille et couche de la sonde principale du domaine, réapprise sur J-A seul ; témoin de même
   taille (autant de paires d'entraînement, tirées dans les trois modes, graine « temoin-p6 »).
7. **Planchers** (`plancher_de`) : 200 directions appariées en covariance des jetons d'entraînement (sondes neuves lues,
   T7-P6 et son témoin), graine « plancher/<nom> ».
8. **Directions des concepts** (`directions_concepts`, T7-P9) et **témoins lexicaux** (`temoins_lexicaux`, T7-P10).

**Interprétations déclarées** (au rapport) : (a) l'empan « réponse » est la réponse entière (`retrait_fin` = 0) ; (b) la
frontière « avant le champ » est le nombre de jetons de `reponse[:position_cost]` tokenisé seul s'il est un préfixe des jetons
de la réponse, sinon le plus long préfixe dont le décodage tient dans `reponse[:position_cost]` (écrit) ; (c) « saturation
comprise » : si la meilleure aire est ≥ 0,99, tous les couples à aire ≥ 0,99 sont ex aequo avec elle ; (d) fichier des phrases
des concepts : première ligne `{"format_lecture": "message_utilisateur" | "phrase_seule"}`, puis une ligne par paire
`{"concept", "indice", "phrase_concept", "phrase_neutre"}` ; (e) pénalité du témoin lexical : meilleure aire de validation
générique, ex aequo départagés par l'ordre croissant de la liste gelée ; (f) T7-P10 de tromperie et d'enjeux : non calculé
(les textes génériques de P3 ne sont pas une entrée de ce texte) ; (g) graines des clés nommées après le manifeste (noms des
sondes choisies) dérivées de la même entropie par `manifeste.graines` (R9), écrites dans le résultat.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal
from ..manifeste import generateur, graines as deriver_graines
from ..sondes.evaluation import aire_sous_courbe, plancher_apparie, scores_actions
from ..sondes.familles import Reglages, entrainer
from ..sondes.temoins import direction_concept, exiger_concept_sans_affect, plancher_concept, temoin_lexical
from .mahalanobis_v1 import preparer_sonde

JEU_JD, JEU_JC, JEU_JA = "dissimulation", "domaine-cout", "intention-autres-modes"
MODES_JEU = {JEU_JD: ("aucun",), JEU_JC: ("cout",), JEU_JA: ("controles", "direction")}
CLES_ENREGISTREMENT = ("jeu", "tache", "paire", "membre", "etiquette", "mode", "instruction_id", "incitation_id",
                       "contexte_systeme", "observation", "reponse", "cout_declare", "position_cost")
ORDRE_FAMILLES = ("difference_moyennes", "lineaire", "perceptron", "attention", "mahalanobis")
CONCEPT_DE_JEU = {JEU_JD: "dissimulation", JEU_JC: "domaine"}
EMPAN_DE_JEU = {JEU_JD: "reponse", JEU_JC: "avant_champ", JEU_JA: "avant_champ"}
PART_ENTRAINEMENT = 0.8
SATURATION = 0.99
PENALITES_LEXICALES = (0.01, 0.1, 1.0, 10.0)
FORMATS_LECTURE = ("message_utilisateur", "phrase_seule")
MAX_JETONS_PHRASE = 128


def reglages_par_defaut() -> dict:
    """`sondes.familles.Reglages` par défaut (plan, point 3), sans le journal : la seule valeur permise de la clé `reglages`."""
    r = Reglages()
    return {"l2": r.l2, "epoques": r.epoques, "pas": r.pas, "cachees": r.cachees, "retrecissement": r.retrecissement}


def agregation_de(famille: str) -> str:
    return "attention" if famille == "attention" else "max"


def ordre_couches(couches) -> list[int]:
    """15, puis 7, puis 23 (plan, point 4) ; sur trois autres couches : celle du milieu, la plus basse, la plus haute."""
    c = sorted(int(x) for x in couches)
    return [c[1], c[0], c[2]] if len(c) == 3 else c


def graine(graines: dict, cle: str, derivees: dict | None = None) -> int:
    """Graine entière de `cle` : celle du manifeste, ou, pour une clé nommée après lui, dérivée de la même entropie
    (`manifeste.graines`), consignée dans `derivees`."""
    g = graines.get(cle)
    if g is None:
        if not graines:
            raise GardeArret(f"graine {cle} : manifeste sans graines")
        entropie = int(next(iter(graines.values()))["entropie"])
        g = deriver_graines([cle], entropie)[cle]
        if derivees is not None:
            derivees[cle] = g
    return int(generateur(g).integers(0, 2 ** 63 - 1))


# ------------------------------------------------------------------------------------------------------------------ jeux
def lire_jeu(chemin: Path, jeu: str) -> list[dict]:
    """Enregistrements d'un jeu (consigne v3, section 3) ; toute faute → `GardeArret` (arrêt de l'étape A, R5). L'étiquette est
    lue dans son champ, jamais au rang de ligne ; les enregistrements sont rendus dans un **ordre canonique** (tâche, paire,
    membre), indépendant de l'ordre du fichier (R-2109 : `assembler` écrit toujours le membre d'étiquette 0 en premier ; la lettre
    du membre, tirée par graine, ne porte pas l'étiquette) : extraction, plis, apprentissage, validation, témoins et T7-P6 sont
    les mêmes au bit près quel que soit l'ordre des lignes."""
    chemin = Path(chemin)
    if jeu not in MODES_JEU:
        raise GardeArret(f"jeu {jeu!r} inconnu")
    try:
        lignes = [json.loads(l) for l in chemin.read_text(encoding="utf-8").splitlines() if l.strip()]
    except (OSError, ValueError) as e:
        raise GardeArret(f"jeu {jeu} ({chemin}) illisible ({type(e).__name__})") from None
    if not lignes:
        raise GardeArret(f"jeu {jeu} ({chemin}) vide")
    paires: dict = {}
    for k, r in enumerate(lignes, start=1):
        lieu = f"jeu {jeu}, ligne {k}"
        if not isinstance(r, dict) or set(r) != set(CLES_ENREGISTREMENT):
            raise GardeArret(f"{lieu} : clés {sorted(r) if isinstance(r, dict) else type(r).__name__} ≠ {list(CLES_ENREGISTREMENT)}")
        if r["jeu"] != jeu or r["mode"] not in MODES_JEU[jeu]:
            raise GardeArret(f"{lieu} : jeu {r['jeu']!r} ou mode {r['mode']!r} hors de {jeu} {MODES_JEU[jeu]}")
        if r["etiquette"] not in (0, 1) or isinstance(r["etiquette"], bool) or r["membre"] not in ("A", "B"):
            raise GardeArret(f"{lieu} : étiquette {r['etiquette']!r} ou membre {r['membre']!r} hors domaine")
        if not all(isinstance(r[c], str) and r[c].strip() for c in ("tache", "contexte_systeme", "observation", "reponse")):
            raise GardeArret(f"{lieu} : tâche, contexte, observation et réponse : textes non vides attendus")
        pc = r["position_cost"]
        if isinstance(pc, bool) or not isinstance(pc, int) or not 0 < pc < len(r["reponse"]) or not r["reponse"][pc:].startswith("COST:"):
            raise GardeArret(f"{lieu} : position_cost {pc!r} ne pointe pas la ligne COST: de la réponse")
        if isinstance(r["paire"], bool) or not isinstance(r["paire"], int) or r["paire"] < 1:
            raise GardeArret(f"{lieu} : paire {r['paire']!r} : entier ≥ 1 attendu")
        paires.setdefault((r["tache"], r["paire"]), []).append(r)
    for (t, p), membres in paires.items():
        if sorted(m["membre"] for m in membres) != ["A", "B"] or sorted(m["etiquette"] for m in membres) != [0, 1]:
            raise GardeArret(f"jeu {jeu}, tâche {t}, paire {p} : deux membres A et B, étiquettes 0 et 1 attendus")
        if len({m["mode"] for m in membres}) != 1:
            raise GardeArret(f"jeu {jeu}, tâche {t}, paire {p} : membres de modes différents")
    return sorted(lignes, key=lambda r: (r["tache"], r["paire"], r["membre"]))


def controler_disjonction(jeux: dict, taches_evaluation) -> dict:
    """Aucune tâche d'un jeu générique n'est une tâche d'évaluation (plan, point 1 ; contrôle par identifiants)."""
    evaluation = set(str(t) for t in taches_evaluation)
    if not evaluation:
        raise GardeArret("contrôle de disjonction : aucune tâche d'évaluation lue dans la course 7b")
    communes = {j: sorted({r["tache"] for r in recs} & evaluation) for j, recs in jeux.items()}
    fautes = {j: c for j, c in communes.items() if c}
    if fautes:
        raise GardeArret(f"contrôle de disjonction : tâches de réserve aussi tâches d'évaluation : {fautes} : arrêt")
    return {"taches_evaluation": len(evaluation), "taches_reserve": {j: len({r['tache'] for r in recs}) for j, recs in jeux.items()},
            "communes": 0}


def decouper_taches(taches, graine_entiere: int, part: float = PART_ENTRAINEMENT) -> tuple[list, list]:
    """Tâches d'entraînement et de validation (par tâche), tirées par une permutation de la graine dérivée « decoupage »."""
    taches = sorted(set(str(t) for t in taches))
    if len(taches) < 2:
        raise GardeArret(f"découpage : au moins deux tâches de réserve ({len(taches)})")
    rng = np.random.default_rng(int(graine_entiere))
    ordre = [taches[i] for i in rng.permutation(len(taches))]
    n = min(len(taches) - 1, max(1, int(round(part * len(taches)))))
    return sorted(ordre[:n]), sorted(ordre[n:])


# -------------------------------------------------------------------------------------------------------------- empans
class Extracteur:
    """Activations des jeux génériques par la passe unique du harnais (modèle de base, dose 0), aux couches lues.
    `modele` et `fmt` : ceux de la chaîne de T0.6 pour la course lue (réel : révision figée ; jouet : modèle par caractères)."""

    def __init__(self, modele, fmt, couches):
        self.modele, self.fmt, self.couches = modele, fmt, [int(c) for c in couches]
        self.frontieres_ajustees = 0

    def _passe(self, ids):
        from ..harnais.activations import passe_unique
        return passe_unique(self.modele, ids, self.couches)

    def frontiere(self, reponse: str, position_cost: int) -> int:
        from ..harnais.formats import _ids
        plein = _ids(self.fmt.tok, reponse.strip())
        avant = _ids(self.fmt.tok, reponse[:position_cost])
        if avant and plein[:len(avant)] == avant:
            return len(avant)
        self.frontieres_ajustees += 1
        borne = len(reponse[:position_cost])
        k = 0
        while k < len(plein) and len(self.fmt.tok.decode(plein[:k + 1])) <= borne:
            k += 1
        return k

    def reponse(self, contexte: str, observation: str, reponse: str, empan: str, position_cost: int | None = None) -> dict:
        from ..premier_test_ia.empans import jetons_reponse_forcee
        r = jetons_reponse_forcee(self.fmt, contexte, observation, reponse, 0)
        n = r["fin"] - r["debut"]
        if empan == "avant_champ":
            n = self.frontiere(reponse, int(position_cost))
        elif empan not in ("reponse", "action_entiere"):
            raise GardeArret(f"empan {empan!r} inconnu")
        if n < 1:
            raise GardeArret("empan vide")
        acts = self._passe(r["ids"])
        sortie = {}
        for c in self.couches:
            a = np.asarray(acts[c][r["debut"]:r["debut"] + n], dtype=np.float32)
            if a.shape[0] != n or not np.all(np.isfinite(a)):
                raise GardeArret(f"empan de {n} jetons hors des activations ou non fini (couche {c})")
            sortie[c] = np.ascontiguousarray(a)
        return sortie

    def phrase(self, texte: str, format_lecture: str) -> dict:
        from ..harnais.formats import _ids
        from ..premier_test_ia.empans import jetons_message_utilisateur
        if format_lecture == "message_utilisateur":
            r = jetons_message_utilisateur(self.fmt, "", texte, MAX_JETONS_PHRASE)
            ids, debut, fin = r["ids"], r["debut"], r["fin"]
        elif format_lecture == "phrase_seule":
            ids = _ids(self.fmt.tok, texte.strip())
            debut, fin = 0, len(ids)
        else:
            raise GardeArret(f"format de lecture {format_lecture!r} inconnu ({FORMATS_LECTURE})")
        acts = self._passe(ids)
        return {c: np.ascontiguousarray(np.asarray(acts[c][debut:fin], dtype=np.float32)) for c in self.couches}


def extraire_jeu(extracteur, recs: list, empan: str, echeance=None) -> dict:
    """Activations par couche d'un jeu (ordre des enregistrements), étiquettes, tâches."""
    seqs = {c: [] for c in extracteur.couches}
    for k, r in enumerate(recs):
        if k % 50 == 0:
            exiger_sans_signal(f"l'extraction du jeu {r['jeu']} (séquence {k})")
            if echeance is not None and time.perf_counter() > echeance:
                raise GardeArret(f"limite de durée dépassée pendant l'extraction du jeu {r['jeu']}")
        a = extracteur.reponse(r["contexte_systeme"], r["observation"], r["reponse"], empan, r["position_cost"])
        for c in seqs:
            seqs[c].append(a[c])
    return {"seqs": seqs, "y": np.array([int(r["etiquette"]) for r in recs], dtype=np.int64),
            "taches": [r["tache"] for r in recs], "modes": [r["mode"] for r in recs]}


# ---------------------------------------------------------------------------------------------------------- apprentissage
def entrainer_concept(concept: str, ex: dict, idx_e: list, idx_v: list, couches, graines: dict, calcul: str,
                      derivees: dict, ex_entier: dict | None = None) -> dict:
    """Cinq familles × couches (`familles.entrainer`, réglages par défaut, une graine par sonde) ; Mahalanobis préparée par
    `preparer_sonde` (essai d'égalité avant usage ; échec → couple en « échec ») ; aires de validation générique (et sur
    l'action entière si `ex_entier`)."""
    y = ex["y"]
    if len(set(y[idx_e].tolist())) < 2 or len(set(y[idx_v].tolist())) < 2:
        raise GardeArret(f"{concept} : les deux classes sont nécessaires à l'entraînement et à la validation")
    couples, rapport = [], {}
    for famille in ORDRE_FAMILLES:
        for c in couches:
            nom = f"{concept}-{famille}-c{int(c)}"
            exiger_sans_signal(f"l'entraînement de {nom}")
            r = Reglages()
            depart = time.perf_counter()
            s = entrainer(famille, nom, int(c), [ex["seqs"][c][i] for i in idx_e], y[idx_e], agregation_de(famille),
                          graine(graines, f"entrainement/{nom}", derivees), r)
            pertes = [float(x["perte"]) for x in r.journal]
            if any(not np.isfinite(p) for p in pertes):
                raise GardeArret(f"{nom} : perte non finie pendant l'entraînement")
            entree = {"nom": nom, "famille": famille, "couche": int(c), "agregation": agregation_de(famille),
                      "duree_s": round(time.perf_counter() - depart, 2), "etat": "notée", "essai_egalite": None,
                      "pertes": {"premiere": pertes[0], "derniere": pertes[-1], "relevees": len(pertes)} if pertes else None}
            try:
                s, essai = preparer_sonde(s, calcul, graine(graines, f"mahalanobis-egalite/{nom}", derivees))
                entree["essai_egalite"] = essai
                entree["aire_validation"] = aire_sous_courbe(scores_actions(s, [ex["seqs"][c][i] for i in idx_v]), y[idx_v])
                if ex_entier is not None:
                    entree["aire_action_entiere"] = aire_sous_courbe(scores_actions(s, [ex_entier["seqs"][c][i] for i in idx_v]),
                                                                     ex_entier["y"][idx_v])
                entree["empreinte"] = s.empreinte()
            except GardeArret as e:
                entree["etat"], entree["echec"] = "échec", str(e)
            couples.append(s)
            rapport[nom] = entree
    return {"concept": concept, "sondes": couples, "couples": rapport, "n_entrainement": len(idx_e), "n_validation": len(idx_v)}


def choisir_principale(couples: dict, couches, ecart: float) -> dict:
    """Meilleure aire de validation ; ex aequo (écart ≤ `ecart`, saturation comprise) départagés par famille puis couche,
    jamais par l'ordre. Rend le nom choisi, les ex aequo et la règle appliquée."""
    vivants = {n: e for n, e in couples.items() if e["etat"] == "notée"}
    if not vivants:
        raise GardeArret("aucun couple notable : sonde principale impossible")
    meilleure = max(e["aire_validation"] for e in vivants.values())
    ex_aequo = [n for n, e in vivants.items() if e["aire_validation"] >= meilleure - float(ecart) - 1e-12
                or (meilleure >= SATURATION and e["aire_validation"] >= SATURATION)]
    oc = ordre_couches(couches)
    rang = lambda n: (ORDRE_FAMILLES.index(vivants[n]["famille"]), oc.index(vivants[n]["couche"]))
    choisie = min(ex_aequo, key=rang)
    return {"principale": choisie, "aire_validation": vivants[choisie]["aire_validation"], "meilleure_aire": meilleure,
            "ex_aequo": sorted(ex_aequo, key=rang), "saturation": meilleure >= SATURATION,
            "regle": (f"meilleure aire de validation générique ; ex aequo (écart ≤ {ecart}, saturation ≥ {SATURATION} comprise) "
                      f"départagés par famille {list(ORDRE_FAMILLES)}, puis couche {oc} ; jamais par l'ordre")}


def plancher_de(sonde, sequences_entrainement: list, n: int, g: int) -> list:
    return plancher_apparie(f"{sonde.nom}-plancher", int(sonde.couche), sequences_entrainement, sonde.agregation, int(n), int(g))


def sondes_p6(jc: dict, ja: dict, idx_tr: dict, principale: dict, graines: dict, calcul: str, derivees: dict) -> dict:
    """T7-P6 (plan 6 bis) : famille et couche de la sonde du domaine, réapprise sur J-A seul (deux modes) ; témoin de même
    taille : autant de paires d'entraînement tirées dans les trois modes (J-C et J-A), graine « temoin-p6 »."""
    f, c = principale["famille"], principale["couche"]
    nom_p6, nom_t = f"intention-sans-cout-{f}-c{c}", f"intention-temoin-{f}-c{c}"
    e_ja = idx_tr["JA"]["e"]
    s_p6 = entrainer(f, nom_p6, c, [ja["seqs"][c][i] for i in e_ja], ja["y"][e_ja], agregation_de(f),
                     graine(graines, f"entrainement/{nom_p6}", derivees), Reglages())
    paires = {}
    for nom_jeu, ex, idx in (("JC", jc, idx_tr["JC"]["e"]), ("JA", ja, e_ja)):
        for i in idx:
            paires.setdefault((nom_jeu, ex["taches"][i], ex["paires"][i]), []).append((nom_jeu, i))
    cles = sorted(paires)
    n_paires = len({(ja["taches"][i], ja["paires"][i]) for i in e_ja})
    rng = np.random.default_rng(graine(graines, "temoin-p6", derivees))
    tirees = [cles[k] for k in sorted(rng.choice(len(cles), size=min(n_paires, len(cles)), replace=False))]
    membres = [m for k in tirees for m in paires[k]]
    seqs = [(jc if j == "JC" else ja)["seqs"][c][i] for j, i in membres]
    y = np.array([(jc if j == "JC" else ja)["y"][i] for j, i in membres], dtype=np.int64)
    s_t = entrainer(f, nom_t, c, seqs, y, agregation_de(f), graine(graines, f"entrainement/{nom_t}", derivees), Reglages())
    sortie = {}
    for nom, s, entr in ((nom_p6, s_p6, [ja["seqs"][c][i] for i in e_ja]), (nom_t, s_t, seqs)):
        s2, essai = preparer_sonde(s, calcul, graine(graines, f"mahalanobis-egalite/{nom}", derivees))
        sortie[nom] = {"sonde": s2, "entrainement": entr, "essai_egalite": essai}
    v = idx_tr["JA"]["v"]
    return {"sonde": nom_p6, "temoin": nom_t, "famille": f, "couche": c, "paires_entrainement": n_paires,
            "modes_temoin": sorted({(jc if j == "JC" else ja)["modes"][i] for j, i in membres}),
            "aires_validation_ja": {n: aire_sous_courbe(scores_actions(sortie[n]["sonde"], [ja["seqs"][c][i] for i in v]),
                                                        ja["y"][v]) for n in sortie}, "_sondes": sortie}


def lire_phrases_concepts(chemin: Path, min_concepts: int = 1) -> dict:
    """Jeu de phrases des concepts sans lien (ligne `SCELLEMENT-CONCEPTS-T07`) : format de lecture, puis paires par concept ;
    au moins `min_concepts` concepts (plan, point 10 : quatre en mode réel ; CT-13), au moins deux paires par concept."""
    try:
        lignes = [json.loads(l) for l in Path(chemin).read_text(encoding="utf-8").splitlines() if l.strip()]
    except (OSError, ValueError) as e:
        raise GardeArret(f"phrases des concepts ({chemin}) illisibles ({type(e).__name__})") from None
    if not lignes or not isinstance(lignes[0], dict) or set(lignes[0]) != {"format_lecture"} \
            or lignes[0]["format_lecture"] not in FORMATS_LECTURE:
        raise GardeArret(f"phrases des concepts : première ligne {{\"format_lecture\": {list(FORMATS_LECTURE)}}} attendue")
    concepts: dict = {}
    for k, r in enumerate(lignes[1:], start=2):
        if not isinstance(r, dict) or set(r) != {"concept", "indice", "phrase_concept", "phrase_neutre"} \
                or not all(isinstance(r[c], str) and r[c].strip() for c in ("concept", "phrase_concept", "phrase_neutre")):
            raise GardeArret(f"phrases des concepts, ligne {k} : {{concept, indice, phrase_concept, phrase_neutre}} attendu")
        exiger_concept_sans_affect(r["concept"])
        concepts.setdefault(r["concept"], []).append(r)
    if len(concepts) < max(1, int(min_concepts)):
        raise GardeArret(f"phrases des concepts : {len(concepts)} concept(s), au moins {max(1, int(min_concepts))} attendus (plan, point 10)")
    courts = sorted(c for c, v in concepts.items() if len(v) < 2)
    if courts:
        raise GardeArret(f"phrases des concepts : moins de deux paires pour {courts}")
    return {"format_lecture": lignes[0]["format_lecture"], "concepts": concepts}


def directions_concepts(extracteur, phrases: dict, couches, n_plancher: int, graines: dict, derivees: dict) -> dict:
    """T7-P9 : une direction par concept et par couche (`direction_concept`), et son plancher (`plancher_concept`)."""
    sortie, rapports = [], []
    for concept in sorted(phrases["concepts"]):
        paires = sorted(phrases["concepts"][concept], key=lambda r: r["indice"])
        pos = [extracteur.phrase(r["phrase_concept"], phrases["format_lecture"]) for r in paires]
        neg = [extracteur.phrase(r["phrase_neutre"], phrases["format_lecture"]) for r in paires]
        for c in couches:
            try:                                              # CT-05 : une direction en échec n'arrête pas l'ensemble
                d, rap = direction_concept(concept, int(c), [p[c] for p in pos], [p[c] for p in neg])
                pl = plancher_concept(concept, int(c), [p[c] for p in pos], [p[c] for p in neg], int(n_plancher),
                                      graine(graines, f"plancher-concept/{concept}/c{int(c)}", derivees))
            except GardeArret as e:
                rapports.append({"concept": concept, "couche": int(c), "etat": f"échec : {e}"})
                continue
            sortie.append({"sonde": d, "plancher": pl})
            rapports.append(rap)
    return {"directions": sortie, "rapports": rapports, "format_lecture": phrases["format_lecture"]}


def texte_empan(r: dict, empan: str) -> str:
    return r["reponse"][:r["position_cost"]] if empan == "avant_champ" else r["reponse"]


def temoins_lexicaux(jeux: dict, idx: dict) -> dict:
    """T7-P10 : témoin lexical générique de chaque concept neuf lu (même empan que la sonde) ; pénalité choisie sur la
    validation générique dans la liste gelée, avant toute lecture d'organisme, sans tirage."""
    sortie = {}
    for cle, jeu in (("JD", JEU_JD), ("JC", JEU_JC)):
        if cle not in jeux:
            continue
        recs, empan = jeux[cle], EMPAN_DE_JEU[jeu]
        e, v = idx[cle]["e"], idx[cle]["v"]
        tx_e, y_e = [texte_empan(recs[i], empan) for i in e], [recs[i]["etiquette"] for i in e]
        tx_v, y_v = [texte_empan(recs[i], empan) for i in v], np.array([recs[i]["etiquette"] for i in v])
        aires, temoins = {}, {}
        for p in PENALITES_LEXICALES:
            t = temoin_lexical(f"lexical-{CONCEPT_DE_JEU[jeu]}", tx_e, y_e, p)
            temoins[p], aires[p] = t, aire_sous_courbe(t.scores(tx_v), y_v)
        meilleure = max(aires.values())
        p = next(x for x in PENALITES_LEXICALES if aires[x] == meilleure)
        sortie[CONCEPT_DE_JEU[jeu]] = {"temoin": temoins[p], "penalite": p, "aires_validation": {str(k): v for k, v in aires.items()},
                                        "empan": empan, "empreinte": temoins[p].empreinte()}
    return sortie


def index_par_taches(ex: dict, taches_e, taches_v) -> dict:
    e = [i for i, t in enumerate(ex["taches"]) if t in set(taches_e)]
    v = [i for i, t in enumerate(ex["taches"]) if t in set(taches_v)]
    return {"e": e, "v": v}


def apprendre(jeux: dict, phrases: dict | None, extracteur, config: dict, graines: dict, concepts_lus: list,
              echeance=None) -> dict:
    """Étape A (2) et (4) : extraction, découpage, 30 couples, sondes principales, T7-P6, planchers, directions, témoins.
    `jeux` : {"JD"|"JC"|"JA": enregistrements} (jeux scellés présents) ; `concepts_lus` : concepts dont la sonde est lue.
    Rend les sondes (objets) et un rapport sérialisable."""
    derivees: dict = {}
    couches = [int(c) for c in config["couches"]]
    calcul = config["mahalanobis_calcul"]
    n = int(config["n_plancher"])
    taches = sorted({r["tache"] for recs in jeux.values() for r in recs})
    t_e, t_v = decouper_taches(taches, graine(graines, "decoupage", derivees)) if taches else ([], [])
    ext, idx = {}, {}
    for cle, recs in jeux.items():
        jeu = recs[0]["jeu"]
        ext[cle] = extraire_jeu(extracteur, recs, EMPAN_DE_JEU[jeu], echeance)
        ext[cle]["paires"] = [r["paire"] for r in recs]
        idx[cle] = index_par_taches(ext[cle], t_e, t_v)
    entier = extraire_jeu(extracteur, jeux["JC"], "action_entiere", echeance) if "JC" in jeux else None
    r0 = Reglages()
    rapport = {"decoupage": {"entrainement": t_e, "validation": t_v, "part": PART_ENTRAINEMENT}, "concepts": {},
               "frontieres_ajustees": None,
               "reglages": {"l2": r0.l2, "epoques": r0.epoques, "pas": r0.pas, "cachees": r0.cachees,
                            "retrecissement": r0.retrecissement, "source": "sondes.familles.Reglages par défaut (plan, point 3)"}}
    sondes, planchers, entrainement = {}, {}, {}
    for cle, concept in (("JD", "dissimulation"), ("JC", "domaine")):
        if cle not in jeux:
            rapport["concepts"][concept] = {"etat": "jeu non scellé : aucune sonde apprise"}
            continue
        r = entrainer_concept(concept, ext[cle], idx[cle]["e"], idx[cle]["v"], couches, graines, calcul, derivees,
                              entier if cle == "JC" else None)
        choix = choisir_principale(r["couples"], couches, float(config["ecart_ex_aequo"]))
        par_nom = {s.nom: s for s in r["sondes"]}
        p = par_nom[choix["principale"]]
        c = int(p.couche)
        tr = [ext[cle]["seqs"][c][i] for i in idx[cle]["e"]]
        rapport["concepts"][concept] = {"couples": r["couples"], **choix, "empreinte_principale": p.empreinte(),
                                        "n_entrainement": r["n_entrainement"], "n_validation": r["n_validation"],
                                        "lue": concept in concepts_lus}
        sondes[concept] = {"principale": p, "couples": r["sondes"]}
        entrainement[p.nom] = tr
        if concept in concepts_lus:
            planchers[p.nom] = plancher_de(p, tr, n, graine(graines, f"plancher/{p.nom}", derivees))
    p6, echec_p6 = None, None
    if "JA" in jeux and "JC" in jeux:
        try:                                                  # CT-05 : un échec met T7-P6 en « échec », jamais l'ensemble
            p6 = sondes_p6(ext["JC"], ext["JA"], idx, rapport["concepts"]["domaine"]["couples"][rapport["concepts"]["domaine"]["principale"]],
                           graines, calcul, derivees)
            pl6 = {nom: plancher_de(x["sonde"], x["entrainement"], n, graine(graines, f"plancher/{nom}", derivees))
                   for nom, x in p6["_sondes"].items()}
            planchers.update(pl6)
        except GardeArret as e:
            p6, echec_p6 = None, str(e)
    rapport["p6"] = ({k: v for k, v in p6.items() if k != "_sondes"} if p6 else
                     {"etat": f"échec : {echec_p6}"} if echec_p6 else
                     {"etat": "non lue : " + ("jeu J-A non scellé" if "JA" not in jeux else "jeu J-C non scellé (famille et couche du domaine)")})
    directions = directions_concepts(extracteur, phrases, couches, n, graines, derivees) if phrases else None
    rapport["directions"] = directions["rapports"] if directions else []
    lexicaux = temoins_lexicaux(jeux, idx)
    rapport["temoins_lexicaux"] = {k: {x: y for x, y in v.items() if x != "temoin"} for k, v in lexicaux.items()}
    rapport["temoins_lexicaux_p3"] = "non calculés : les textes génériques de P3 (tromperie, enjeux) ne sont pas une entrée de ce texte"
    rapport["frontieres_ajustees"] = getattr(extracteur, "frontieres_ajustees", None)
    rapport["graines_derivees_apres_manifeste"] = sorted(derivees)
    return {"sondes": sondes, "planchers": planchers, "p6": p6, "directions": directions, "lexicaux": lexicaux,
            "rapport": rapport, "graines_derivees": derivees}


__all__ = ["lire_jeu", "controler_disjonction", "decouper_taches", "Extracteur", "extraire_jeu", "entrainer_concept",
           "choisir_principale", "plancher_de", "sondes_p6", "lire_phrases_concepts", "directions_concepts", "temoins_lexicaux",
           "apprendre", "graine", "ordre_couches", "agregation_de", "ORDRE_FAMILLES", "JEU_JD", "JEU_JC", "JEU_JA", "MODES_JEU",
           "CLES_ENREGISTREMENT", "PENALITES_LEXICALES", "SATURATION", "FORMATS_LECTURE"]
