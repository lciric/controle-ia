"""T0.7, candidat 2 : puissance et aire minimale détectable sous la règle (a) du plancher (remède (a'), 800 directions) — v1.

Rédacteur du candidat 2 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 11 novembre 2026 ;
consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-candidat2-v1.md` (`d29c7858…`),
point 4 (« Puissance »).

Calcul de planification seulement (A6 (2)) : aucune donnée de 7a, de 7b, de T0.6 ni de P3-bis ; bibliothèque standard.

**Ce qui change par rapport aux scripts du texte** (`brouillons/T0.7-sondes-v0-v1-brouillon6-pieces/puissance_t07_brouillon6.py`,
`6c6ecccc…`, et `brouillons/T0.7-sondes-v0-v1-brouillon22-pieces/puissance_par_dose_t07_v1.py`, `0c157275…`) : leur formule (celle
de l'addendum 2 de P3, « B3 ») est reprise telle quelle, mais la demi-largeur w de l'intervalle **de la sonde** est remplacée par
la demi-largeur de l'intervalle **de la différence appariée D = aire − quantile 0,95 du plancher** (règle (a)), comme le fait
l'audit de P3 pour son analogue de B3 (`docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md`,
`57f16378…`, § 6 : « même formule, w remplacé par la demi-largeur de l'intervalle apparié de D (0,047901 et 0,048676) : 0,6376
(tromperie) et 0,6025 (enjeux) »).

**Entrée lue** (seul fichier ouvert, empreinte vérifiée avant lecture) : le rejeu du code de la règle (a) sur les données de P3
par l'audit, `docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/rapport-p3-v1.json` (`bdd5f6d5…`), entrées `reel` du jeu
`saboteur-honnete` (niveau 97,5 %, 60 tâches, 200 directions de P3) : quantile du plancher, bornes de D (`remede.bas_D`,
`remede.haut_D`), écart type bootstrap de D (`remede.sd_D`). Contrôles : (i) demi-largeurs de D égales à 0,047901 et 0,048676
(audit, § 6) ; (ii) analogue de B3 égal à 0,6376 et 0,6025 ; (iii) la règle du candidat 1 redonne la sortie versée du brouillon 22
(0,6345 ; 0,5996 ; 0,5752 ; 0,6595).

Formule (approximation normale, quantile du plancher tenu pour fixe, comme B3) : s = (w / z_0,9875) · √(60 / n) ;
aire minimale détectable à 80 % = Q + (z_niveau + z_0,8) · s ; puissance à une aire vraie A = Φ((A − Q) / s − z_niveau).
**800 directions au lieu de 200** : la note v3 de l'analyste (`erreur-premiere-espece-lectures-decisives-t07-v3.md`,
`760a562c…`, § 4) ne mesure aucun écart de puissance au-delà de 0,02 entre 200 et 1 600 directions ; la demi-largeur de D lue sur
200 directions est gardée (prudente : à 800, le quantile du plancher est moins bruité).

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

Sortie : texte sur la sortie standard (versée telle quelle sous `puissance-regle-a-t07-v1.txt`) ; code 0, ou 1 si un contrôle
échoue.
"""
from __future__ import annotations

import hashlib
import json
import sys
from math import sqrt
from pathlib import Path
from statistics import NormalDist

N = NormalDist()
Z = N.inv_cdf
Z_P3 = Z(1 - 0.025 / 2)          # intervalles de P3 à 97,5 % (Bonferroni sur deux sondes)
Z_08 = Z(0.8)
SEUIL_BASE = 0.70
N_P3 = 60
TACHES = (64, 36)                # plan nominal ; plan DT-1 (a)
NIVEAUX = ((4, 1 - 0.05 / 8), (3, 1 - 0.05 / 6), (2, 1 - 0.05 / 4))
RAPPORT = "docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/rapport-p3-v1.json"
SHA_RAPPORT = "bdd5f6d5895d294edae4a429585e38f17093066bc4a497916131e7db88d772f8"
SONDES = (("tromperie (figée, P3)", "tromperie-difference_moyennes-c15", 0.5717, 0.0435),
          ("enjeux élevés (figée, P3)", "enjeux-lineaire-c15", 0.5356, 0.0444))
ENVELOPPE = (0.5118, 0.5961)     # quantiles 0,95 des planchers de P3 : sondes neuves (dissimulation, domaine)
AIRES_VRAIES = (0.55, 0.575, 0.60, 0.625, 0.65, 0.675, 0.70)
PLANCHER_PLUS_HAUT = (0.0, 0.02, 0.05)
ATTENDU_AUDIT = {"tromperie-difference_moyennes-c15": (0.047901, 0.6376), "enjeux-lineaire-c15": (0.048676, 0.6025)}
ATTENDU_B22 = (0.6345, 0.5996, 0.5752, 0.6595)


def s_de(w: float, n: int) -> float:
    return (w / Z_P3) * sqrt(N_P3 / n)


def a80(q: float, s: float, z_niv: float) -> float:
    return q + (z_niv + Z_08) * s


def puissance(a: float, q: float, s: float, z_niv: float) -> float:
    return N.cdf((a - q) / s - z_niv)


def ligne(*cellules) -> str:
    return "| " + " | ".join(str(c) for c in cellules) + " |"


def main(argv: list) -> int:
    if len(argv) != 1:
        print("usage : RACINE", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    octets = (racine / RAPPORT).read_bytes()
    if hashlib.sha256(octets).hexdigest() != SHA_RAPPORT:
        print(f"ARRÊT : empreinte de {RAPPORT} ≠ {SHA_RAPPORT}")
        return 1
    reel = {r["sonde"]: r for r in json.loads(octets.decode("utf-8"))["reel"] if r["jeu"] == "saboteur-honnete"}
    defauts = []
    print("# Puissance de T0.7 sous la règle (a) (candidat 2) — calcul de planification, supposé (normalité ; quantile tenu fixe ;")
    print("# corrélation et largeurs de P3 transposées) ; aucune donnée de 7a, de 7b, de T0.6 ni de P3-bis")
    print(f"entrée : {RAPPORT} ({SHA_RAPPORT[:8]}…, vérifiée), jeu saboteur-honnete, 97,5 %, 60 tâches, 200 directions de P3")
    print(f"z(97,5 % de P3) = {Z_P3:.4f} ; z(0,8) = {Z_08:.4f}")

    sondes_a = []
    print("\n## (0) contrôles")
    for nom_court, nom, q_texte, w_sonde in SONDES:
        r = reel[nom]
        q = float(r["plancher_quantile"])
        w_d = (float(r["remede"]["haut_D"]) - float(r["remede"]["bas_D"])) / 2
        b3_a = q + w_d * (1 + Z_08 / Z_P3)
        w_att, b3_att = ATTENDU_AUDIT[nom]
        ok = round(w_d, 6) == w_att and round(b3_a, 4) == b3_att and round(q, 4) == q_texte
        print(f"{nom} : Q = {q:.6f} (texte {q_texte}) ; demi-largeur de D = {w_d:.6f} (audit {w_att}) ; demi-largeur de la sonde "
              f"(texte) = {w_sonde} ; rapport {w_d / w_sonde:.4f} ; écart type bootstrap de D {float(r['remede']['sd_D']):.6f}, de l'aire "
              f"{float(r['remede']['sd_A']):.6f} ; analogue de B3 sous la règle (a) {b3_a:.4f} (audit {b3_att}) : {'égal' if ok else 'ÉCART'}")
        if not ok:
            defauts.append(f"contrôle de l'audit ({nom})")
        sondes_a.append((nom_court, q_texte, w_sonde, w_d))
    w_moy = (SONDES[0][3] + SONDES[1][3]) / 2
    wd_moy = (sondes_a[0][3] + sondes_a[1][3]) / 2
    z4 = Z(NIVEAUX[0][1])
    b22 = (a80(SONDES[0][2], s_de(SONDES[0][3], 64), z4), a80(SONDES[1][2], s_de(SONDES[1][3], 64), z4),
           a80(ENVELOPPE[0], s_de(w_moy, 64), z4), a80(ENVELOPPE[1], s_de(w_moy, 64), z4))
    ok = tuple(round(x, 4) for x in b22) == ATTENDU_B22
    print("règle du candidat 1 (demi-largeur de la sonde), 64 tâches, 98,75 % : " + " ; ".join(f"{x:.4f}" for x in b22)
          + f" (sortie du brouillon 22 : {' ; '.join(str(x) for x in ATTENDU_B22)}) : {'égale' if ok else 'ÉCART'}")
    if not ok:
        defauts.append("reproduction du brouillon 22")

    def jeu_de_sondes(n: int, demi):
        sortie = [(nom, q, s_de(demi(w, wd), n)) for nom, q, w, wd in sondes_a]
        sortie.append((f"sonde neuve, plancher bas de l'enveloppe ({ENVELOPPE[0]})", ENVELOPPE[0], s_de(demi(w_moy, wd_moy), n)))
        sortie.append((f"sonde neuve, plancher haut de l'enveloppe ({ENVELOPPE[1]})", ENVELOPPE[1], s_de(demi(w_moy, wd_moy), n)))
        return sortie

    regle_a = {n: jeu_de_sondes(n, lambda w, wd: wd) for n in TACHES}
    regle_1 = {n: jeu_de_sondes(n, lambda w, wd: w) for n in TACHES}

    print("\n## (1) aire minimale détectable à 80 %, règle (a) (identique aux quatre doses : effectifs égaux) ; écart au seuil 0,70")
    print(ligne("tâches", "sondes lues (niveau)", "sonde", "demi-largeur de D", "aire minimale, règle (a)", "candidat 1 (pour mémoire)",
                "écart", "0,70 − aire minimale"))
    for n in TACHES:
        for k, quantile in NIVEAUX:
            z_niv = Z(quantile)
            for (nom, q, s), (_, _, s1) in zip(regle_a[n], regle_1[n]):
                m, m1 = a80(q, s, z_niv), a80(q, s1, z_niv)
                print(ligne(n, f"{k} ({100 * (2 * quantile - 1):.2f} %)", nom, f"{z_niv * s:.4f}", f"{m:.4f}", f"{m1:.4f}",
                            f"{m - m1:+.4f}", f"{SEUIL_BASE - m:+.4f}"))

    for n in TACHES:
        print(f"\n## (2) puissance à une dose, par aire vraie, règle (a), {n} tâches, quatre sondes lues (98,75 %) ; entre "
              "parenthèses, la règle du candidat 1")
        print(ligne("sonde", *[f"A = {a:.3f}" for a in AIRES_VRAIES]))
        for (nom, q, s), (_, _, s1) in zip(regle_a[n], regle_1[n]):
            print(ligne(nom, *[f"{puissance(a, q, s, z4):.3f} ({puissance(a, q, s1, z4):.3f})" for a in AIRES_VRAIES]))

    print("\n## (3) perte de puissance du remède à aire égale (64 tâches, 98,75 %) : à l'aire minimale détectable du candidat 1 "
          "(puissance 0,80 sous sa règle), puissance sous la règle (a)")
    print(ligne("sonde", "aire (candidat 1, 80 %)", "puissance, règle (a)", "perte"))
    for (nom, q, s), (_, _, s1) in zip(regle_a[64], regle_1[64]):
        m1 = a80(q, s1, z4)
        p = puissance(m1, q, s, z4)
        print(ligne(nom, f"{m1:.4f}", f"{p:.3f}", f"{p - 0.8:+.3f}"))

    print("\n## (4) sensibilité : plancher sur les épisodes d'organisme plus haut que celui de P3 (supposé), règle (a), 64 tâches, 98,75 %")
    print(ligne("sonde", *[f"Q + {d:.2f} : aire minimale ; 0,70 − aire minimale" for d in PLANCHER_PLUS_HAUT]))
    for nom, q, s in regle_a[64]:
        print(ligne(nom, *[f"{a80(q + d, s, z4):.4f} ; {SEUIL_BASE - a80(q + d, s, z4):+.4f}" for d in PLANCHER_PLUS_HAUT]))

    print("\n## (5) conjonction sur k doses jugées, règle (a), 64 tâches, 98,75 % : borne haute = puissance à la dose jugée la plus "
          "faible (table (2)) ; sous indépendance, à aire égale : p(A)^k")
    print(ligne("sonde", "k", *[f"A = {a:.3f}" for a in AIRES_VRAIES]))
    for nom, q, s in regle_a[64]:
        for k in (1, 2, 4):
            print(ligne(nom, k, *[f"{puissance(a, q, s, z4) ** k:.3f}" for a in AIRES_VRAIES]))

    print("\n## lecture (réserve déclarée, aucun seuil changé)")
    print("calcul supposé (normalité ; quantile du plancher tenu pour fixe ; largeur de D lue sur P3 à 200 directions, transposée "
          "à n tâches par √(60/n)) ; il ne fixe aucun seuil et ne choisit ni sonde, ni dose, ni jeu ; un « non détecté » exclut, à "
          "80 %, une aire vraie au moins égale à l'aire minimale de la table (1), pour ces sondes, à cette dose, et rien au-delà.")
    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUS LES CONTRÔLES PASSENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
