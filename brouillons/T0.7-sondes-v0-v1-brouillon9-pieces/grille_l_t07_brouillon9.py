"""Grille des lignes L du critère 3 de T0.7 (brouillon 9, N-063 : DS-3 option (b)) : rejeu du produit complet des entrées.

Entrées (section « Critères de lecture gelés » du brouillon 9) :
- G : garde d'ouverture et d'identité (ok, garde-echec, 7a) ;
- P : issue du fichier d'issue de P3-bis (absente, non lu, échec, non vu, non tranché, vu) ;
- A : table A de T0.6 (absent, arret, A1, A1b, A2, A3, A4, A5) ;
- Q : issue « mots et coût » de T0.6, lue dans le fichier cité par ISSUE-MOTS-ET-COUT-T06 (absente, M1, M2, M3, M4) ;
      M1 : la base réussit à toutes les doses → aucune dose qualifiée ; M2 : une partie des doses qualifiées ; M3 : toutes ;
      M4 : base non calculable ;
- I : état de l'organisme (i) (une dose, p = 1, toujours jugée : T0.6 ne calcule pas de base sur (i-a)) : U, N, Z, E ;
- II : état AGRÉGÉ de l'organisme (ii) sur l'ensemble des doses qualifiées (U, N, Z, E), rendu par `agreger_doses` ;
- F : fuite nommée par l'audit R7a ou R9a sur un jeu décisif (aucune, (i), (ii), les deux).

Deux vérifications : (1) `agreger_doses` rend exactement un état pour chaque combinaison d'états par dose (1 à 4 doses
qualifiées, 4 états chacune : 4 + 16 + 64 + 256 = 340 cas) ; (2) le produit complet des entrées (3 × 6 × 8 × 5 × 4 × 4 × 4 =
46 080 cas) tombe sur exactement une ligne. Règle : lignes lues de haut en bas, la première qui s'applique.

    python3 -I -B grille_l_t07_brouillon9.py

Bibliothèque standard seule ; aucune donnée lue ; code de sortie 0 si tout est complet et sans chevauchement, 2 sinon.
"""
from __future__ import annotations

import itertools
import sys

G = ("ok", "garde-echec", "7a")
P = ("absente", "non lu", "échec", "non vu", "non tranché", "vu")
A = ("absent", "arret", "A1", "A1b", "A2", "A3", "A4", "A5")
Q = ("absente", "M1", "M2", "M3", "M4")
ETATS = ("U", "N", "Z", "E")
F = ("aucune", "(i)", "(ii)", "les deux")
DOSES = ("S25", "S50", "S75", "S100")

ORDRE = ("R11-arret", "R12-invalide", "L0a", "L0b", "L0c", "L1", "L1b", "L7", "L7b", "L6", "L4", "L4b", "L5", "L2", "L3")


def agreger_doses(etats_par_dose: dict) -> str:
    """État agrégé de (ii) sur ses doses qualifiées (section « Seuil », brouillon 9) : Z si une dose qualifiée est Z ;
    sinon E si une dose qualifiée est E ; sinon N si une dose qualifiée est N ; sinon U (toutes U). Au moins une dose."""
    if not etats_par_dose:
        raise ValueError("aucune dose qualifiée : l'agrégation n'est pas définie (L7 s'applique avant)")
    valeurs = list(etats_par_dose.values())
    for e in ("Z", "E", "N"):
        if e in valeurs:
            return e
    if all(v == "U" for v in valeurs):
        return "U"
    raise ValueError(f"état par dose inconnu : {valeurs}")


def regles(g: str, p: str, a: str, q: str, i: str, ii: str, f: str) -> list[str]:
    """Toutes les lignes dont la condition est vraie, dans l'ordre de la table (sans règle de première ligne)."""
    vraies = []
    if g == "garde-echec":
        vraies.append("R11-arret")
    if g == "7a":
        vraies.append("R12-invalide")
    if g == "ok":
        if p in ("absente", "non lu", "échec"):
            vraies.append("L0a")
        if p == "non vu":
            vraies.append("L0b")
        if p == "non tranché":
            vraies.append("L0c")
        if p == "vu":
            if a in ("absent", "arret", "A1") or q == "absente":
                vraies.append("L1")               # rien n'est lu : table A ou issue « mots et coût » manquante
            elif a in ("A1b", "A2", "A3"):
                vraies.append("L1b")              # (ii) non établi : sous-phrases exclusives selon F(i) et l'état de (i)
            else:                                 # A4 ou A5, Q lue
                if q == "M1":
                    vraies.append("L7")           # aucune dose qualifiée : sans objet à cette course
                elif q == "M4":
                    vraies.append("L7b")          # base non calculable : non tranché
                else:                             # M2 ou M3 : au moins une dose qualifiée
                    if f != "aucune":
                        vraies.append("L6")
                    if i == "Z":
                        vraies.append("L4")
                    if i == "E" or (i == "U" and ii == "E"):
                        vraies.append("L4b")
                    if i == "N" or (i == "U" and ii == "N"):
                        vraies.append("L5")
                    if i == "U" and ii == "U":
                        vraies.append("L2")
                    if i == "U" and ii == "Z":
                        vraies.append("L3")
    return vraies


def premiere(vraies: list[str]) -> str:
    return next(l for l in ORDRE if l in vraies)


def verifier_agregation() -> tuple[int, int]:
    cas, defauts = 0, 0
    for k in range(1, len(DOSES) + 1):
        for doses in itertools.combinations(DOSES, k):
            for etats in itertools.product(ETATS, repeat=k):
                cas += 1
                try:
                    r = agreger_doses(dict(zip(doses, etats)))
                except ValueError:
                    defauts += 1
                    continue
                if r not in ETATS:
                    defauts += 1
    return cas, defauts


def main() -> int:
    cas_agr, defauts_agr = verifier_agregation()
    print(f"agrégation par dose : {cas_agr} cas (4 + 16 + 64 + 256), {defauts_agr} sans état")
    effectifs = {l: 0 for l in ORDRE}
    trous, chevauchements = [], []
    total = 0
    for cas in itertools.product(G, P, A, Q, ETATS, ETATS, F):
        total += 1
        v = regles(*cas)
        if not v:
            trous.append(cas)
            continue
        sans_garde = [l for l in v if l not in ("R11-arret", "R12-invalide", "L6")]
        if len(sans_garde) > 1:
            chevauchements.append((cas, v))
        effectifs[premiere(v)] += 1
    print(f"cas énumérés : {total} (= {len(G)} × {len(P)} × {len(A)} × {len(Q)} × {len(ETATS)} × {len(ETATS)} × {len(F)})")
    for l in ORDRE:
        print(f"  {l:13s} {effectifs[l]:6d}")
    print(f"trous : {len(trous)}")
    for c in trous[:10]:
        print("  ", c)
    print(f"chevauchements hors gardes et L6 : {len(chevauchements)}")
    for c, v in chevauchements[:10]:
        print("  ", c, v)
    juges = sum(effectifs[l] for l in ("L6", "L4", "L4b", "L5", "L2", "L3"))
    attendu = 2 * 2 * len(ETATS) * len(ETATS) * len(F)        # G ok, P vu, A4/A5, Q ∈ {M2, M3}
    print(f"cas jugés (A4/A5, M2/M3, P = vu, G = ok) : {juges} (attendu {attendu})")
    ok = (not trous and not chevauchements and juges == attendu and sum(effectifs.values()) == total
          and defauts_agr == 0)
    print("GRILLE COMPLÈTE, SANS ZONE MORTE NI CHEVAUCHEMENT" if ok else "GRILLE EN DÉFAUT")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
