"""Grille des lignes L du critère 3 de T0.7 (brouillon 12 : script du brouillon 11 + deux sources de la dérivation (3) :
écart « aire » et liste `doses_qualifiees` écrite dans un autre ordre ; rapport du développeur v2, section 5).

Trois vérifications, toutes par énumération complète :

(1) Agrégation par dose (`agreger_doses`) : pour tout ensemble non vide de doses jugées parmi S25, S50, S75, S100 et tout
    état de sonde par dose (U, N, Z, E) : 4 × 4 + 6 × 16 + 4 × 64 + 1 × 256 = 624 cas, un état agrégé chacun.

(2) Grille par classes : G × P × A × Q × (i) × (ii) × F = 3 × 6 × 8 × 6 × 4 × 4 × 4 = 55 296 cas ; Q est la CLASSE de
    l'issue « mots et coût » DÉRIVÉE par le module (absente, non_calculable, incoherent, vide, partiel, complet) ; (ii)
    est l'état agrégé sur les doses jugées. Exactement une ligne par cas, 0 chevauchement hors L6 (L6, fuite nommée, est
    vraie en même temps qu'une ligne L4 à L3 par construction et passe avant elles par l'ordre). Sous-phrases de L1b
    énumérées : exactement une chacune (celles de L7 le sont dans la grille (3)).

(3) Grille par états par dose (CLT7C-08 ; CLT7D-01, CLT7D-02, CLT7D-06) : G = ok, P = vu, A = A4 (A5 suit le même chemin
    du code) ; écart INTERNE du fichier de T0.6, énuméré source par source (aucun ; dose hors de S25 à S100 présente ;
    état recalculé différent sur une dose « réussit » ou « échoue » ; base décisive différente de l'argmax sur une telle
    dose ; brouillon 12 : `aire` différente de l'aire de la base décisive écrite sur une telle dose) × liste
    `doses_qualifiees` ÉCRITE dans le fichier (égale aux doses « échoue » ; vide ; doses « échoue » plus les doses non
    calculables ; brouillon 12 : doses « échoue » dans l'ordre inverse, comparée en liste ordonnée) × étiquette M du fichier (M1 à M4) × état de la base par dose (réussit, échoue, non
    calculable)^4 × effet du coût par dose (établi, non établi, non calculable : `effet_cout` = null)^4 × règle P-064
    (appliquée ou non) × état de (i) × F × états des sondes par dose jugée (4^k). Les écarts « état », « argmax », « aire » ne
    sont possibles que s'il existe une dose « réussit » ou « échoue » : les configurations impossibles sont comptées et
    sautées. Le module DÉRIVE la classe Q et l'état agrégé de (ii), puis la ligne.

Portée des preuves, déclarée (CLT7D-06) : (a) la grille (3) applique la même fonction de lignes `regles` que la grille (2) ;
son contrôle propre est que L7, L7b et L7c ne dépendent ni de (i), ni de (ii), ni de F, plus la couverture ; (b) le contrôle
de priorité de L7b (toute configuration sans écart interne et avec une dose non calculable donne L7b, quelles que soient
la liste écrite et l'étiquette) est écrit À PART de `deriver`, à partir du texte ; (c) les contrôles de sous-phrases prouvent
l'exclusivité, pas la fidélité au texte, qui vient de la lecture ; (d) la lecture du fichier (champs `null` permis sur une
dose non calculable et sur `effet_cout` ; `null` ailleurs = fichier illisible = Q absente = L1) n'est pas modélisée ici :
elle est couverte par les essais R5 du module.

    python3 -I -B grille_l_t07_brouillon12.py

Bibliothèque standard seule ; aucune donnée lue ; code de sortie 0 si tout est complet et sans chevauchement, 2 sinon.
"""
from __future__ import annotations

import itertools
import sys

G = ("ok", "garde-echec", "7a")
P = ("absente", "non lu", "échec", "non vu", "non tranché", "vu")
A = ("absent", "arret", "A1", "A1b", "A2", "A3", "A4", "A5")
Q = ("absente", "non_calculable", "incoherent", "vide", "partiel", "complet")
ETATS = ("U", "N", "Z", "E")
F = ("aucune", "(i)", "(ii)", "les deux")
DOSES = ("S25", "S50", "S75", "S100")
BASE = ("reussit", "echoue", "non_calculable")
EFFET = ("etabli", "non_etabli", "non_calculable")          # non_calculable : `effet_cout` = null (CLT7D-02)
ETIQUETTES = ("M1", "M2", "M3", "M4")
ECART_INTERNE = ("aucun", "dose_hors", "etat", "argmax", "aire")    # CLT7D-01, CLT7D-06 ; « aire » : brouillon 12
LISTE_ECRITE = ("echoue", "vide", "echoue_et_nc", "echoue_inverse")   # CLT7D-01 ; « echoue_inverse » : brouillon 12

ORDRE = ("R11-arret", "R12-invalide", "L0a", "L0b", "L0c", "L1", "L1b", "L7", "L7b", "L7c", "L6", "L4", "L4b", "L5",
         "L2", "L3")
SOUS_L1B = ("F(i)", "N", "U", "Z", "E")


def agreger_doses(etats_par_dose: dict) -> str:
    """État agrégé de (ii) sur les doses JUGÉES : Z si une est Z ; sinon E si une est E ; sinon N si une est N ; sinon U."""
    if not etats_par_dose:
        raise ValueError("aucune dose jugée : l'agrégation n'est pas définie (L7 s'applique avant)")
    valeurs = list(etats_par_dose.values())
    for e in ("Z", "E", "N"):
        if e in valeurs:
            return e
    if all(v == "U" for v in valeurs):
        return "U"
    raise ValueError(f"état par dose inconnu : {valeurs}")


def etiquette_recalculee(base: dict) -> str:
    """Étiquette M recalculée sur S25 à S100 seules, appelée seulement sans dose non calculable (l'étape 2 passe avant ;
    la branche « M4 » du brouillon 10 était inatteignable et est retirée, CLT7D-08) : M1, M3, sinon M2."""
    v = [base[d] for d in DOSES]
    if "non_calculable" in v:
        raise ValueError("étiquette recalculée demandée avec une dose non calculable : l'étape 2 passe avant")
    if all(x == "reussit" for x in v):
        return "M1"
    if all(x == "echoue" for x in v):
        return "M3"
    return "M2"


def liste_ecrite(forme: str, base: dict) -> list:
    if forme == "echoue":
        return [d for d in DOSES if base[d] == "echoue"]
    if forme == "vide":
        return []
    if forme == "echoue_inverse":
        return [d for d in reversed(DOSES) if base[d] == "echoue"]   # comparée en liste ordonnée
    return [d for d in DOSES if base[d] in ("echoue", "non_calculable")]


def deriver(ecart: str, liste: list, etiquette: str, base: dict, effet: dict, p064: bool) -> tuple[str, list, list]:
    """Dérivation du module (CLT7C-01, CLT7C-05, CLT7D-01, CLT7D-02, P-064) : classe Q, doses qualifiées, doses jugées.
    1. écart interne (dose hors de S25 à S100, état recalculé, argmax ou `aire` sur une dose réussit/échoue) → incoherent ;
    2. une dose non calculable → non_calculable (quelles que soient la liste écrite et l'étiquette) ;
    3. étiquette du fichier ≠ recalculée, OU `doses_qualifiees` écrite ≠ doses « échoue » (liste ordonnée) → incoherent ;
    4. doses jugées = qualifiées à effet « établi » (si p064 ; « non établi » et « non calculable » ne le sont pas) ;
       vide / partiel / complet. L'étiquette M du fichier n'aiguille jamais."""
    qualifiees = [d for d in DOSES if base[d] == "echoue"]
    if ecart != "aucun":
        return "incoherent", qualifiees, []
    if any(base[d] == "non_calculable" for d in DOSES):
        return "non_calculable", qualifiees, []
    if etiquette != etiquette_recalculee(base) or liste != qualifiees:
        return "incoherent", qualifiees, []
    jugees = [d for d in qualifiees if (effet[d] == "etabli" or not p064)]
    if not jugees:
        return "vide", qualifiees, jugees
    return ("complet" if len(jugees) == len(DOSES) else "partiel"), qualifiees, jugees


def regles(g: str, p: str, a: str, q: str, i: str, ii: str, f: str) -> list[str]:
    """Toutes les lignes dont la condition est vraie (sans règle de première ligne)."""
    vraies = []
    if g == "garde-echec":
        vraies.append("R11-arret")
    if g == "7a":
        vraies.append("R12-invalide")
    if g != "ok":
        return vraies
    if p in ("absente", "non lu", "échec"):
        vraies.append("L0a")
    if p == "non vu":
        vraies.append("L0b")
    if p == "non tranché":
        vraies.append("L0c")
    if p != "vu":
        return vraies
    if a in ("absent", "arret", "A1") or q == "absente":
        vraies.append("L1")
        return vraies
    if a in ("A1b", "A2", "A3"):
        vraies.append("L1b")
        return vraies
    if q == "vide":
        vraies.append("L7")
    if q == "non_calculable":
        vraies.append("L7b")
    if q == "incoherent":
        vraies.append("L7c")
    if q in ("partiel", "complet"):
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


def sous_phrases_l1b(i: str, f: str) -> list[str]:
    """Phrases de L1b vraies (la première qui s'applique est écrite) ; une fuite sur (ii) seul ne change pas la phrase."""
    v = []
    if f in ("(i)", "les deux"):
        v.append("F(i)")
    v.append(i)                                   # exactement un de N, U, Z, E
    return v


def sous_phrases_l7(qualifiees: list, jugees: list) -> list[str]:
    """Phrases de L7 : « aucune dose qualifiée » ou « doses qualifiées sans effet du coût établi » (exclusives)."""
    if jugees:
        return []
    return ["aucune qualifiee"] if not qualifiees else ["qualifiees sans effet"]


def verifier_agregation() -> tuple[int, int]:
    cas, defauts = 0, 0
    for k in range(1, len(DOSES) + 1):
        for doses in itertools.combinations(DOSES, k):
            for etats in itertools.product(ETATS, repeat=k):
                cas += 1
                try:
                    if agreger_doses(dict(zip(doses, etats))) not in ETATS:
                        defauts += 1
                except ValueError:
                    defauts += 1
    return cas, defauts


def grille_classes() -> dict:
    effectifs = {l: 0 for l in ORDRE}
    trous, chev, l1b_defauts = 0, 0, 0
    total = 0
    for cas in itertools.product(G, P, A, Q, ETATS, ETATS, F):
        total += 1
        v = regles(*cas)
        if not v:
            trous += 1
            continue
        if len([l for l in v if l not in ("R11-arret", "R12-invalide", "L6")]) > 1:
            chev += 1
        l = premiere(v)
        effectifs[l] += 1
        if l == "L1b":
            s = sous_phrases_l1b(cas[4], cas[6])
            if not s or s[0] not in SOUS_L1B or len([x for x in s if x in ETATS]) != 1:
                l1b_defauts += 1
    juges = sum(effectifs[l] for l in ("L6", "L4", "L4b", "L5", "L2", "L3"))
    return {"total": total, "effectifs": effectifs, "trous": trous, "chevauchements": chev, "juges": juges,
            "juges_attendus": 2 * 2 * len(ETATS) * len(ETATS) * len(F), "l1b_defauts": l1b_defauts}


def grille_doses() -> dict:
    total, trous, chev, ecarts, l7_defauts, priorite_l7b, impossibles, configs = 0, 0, 0, 0, 0, 0, 0, 0
    controles_b12 = 0   # brouillon 12 : écart « aire » → incoherent ; liste à l'envers (≥ 2 doses « échoue », aucune non calculable) → incoherent
    effectifs = {l: 0 for l in ORDRE}
    classes = {q: 0 for q in Q}
    for ecart, forme, etiquette, p064 in itertools.product(ECART_INTERNE, LISTE_ECRITE, ETIQUETTES, (True, False)):
        for base_v in itertools.product(BASE, repeat=4):
            base = dict(zip(DOSES, base_v))
            if ecart in ("etat", "argmax", "aire") and all(b == "non_calculable" for b in base_v):
                impossibles += 3 ** 4          # aucune dose réussit/échoue où l'écart pourrait se trouver
                continue
            liste = liste_ecrite(forme, base)
            for effet_v in itertools.product(EFFET, repeat=4):
                effet = dict(zip(DOSES, effet_v))
                configs += 1
                q, qualifiees, jugees = deriver(ecart, liste, etiquette, base, effet, p064)
                classes[q] += 1
                # contrôle de priorité de L7b, écrit à part de `deriver` (CLT7D-01, CLT7D-06 (b))
                if ecart == "aucun" and "non_calculable" in base_v and q != "non_calculable":
                    priorite_l7b += 1
                # contrôles du brouillon 12, écrits à part de `deriver`
                if ecart == "aire" and q != "incoherent":
                    controles_b12 += 1
                if (ecart == "aucun" and forme == "echoue_inverse" and "non_calculable" not in base_v
                        and base_v.count("echoue") >= 2 and q != "incoherent"):
                    controles_b12 += 1
                if q == "vide" and len(sous_phrases_l7(qualifiees, jugees)) != 1:
                    l7_defauts += 1
                etats_sondes = itertools.product(ETATS, repeat=len(jugees)) if jugees else [()]
                for es in etats_sondes:
                    ii = agreger_doses(dict(zip(jugees, es))) if jugees else "U"   # sans effet hors partiel/complet
                    for i, f in itertools.product(ETATS, F):
                        total += 1
                        v = regles("ok", "vu", "A4", q, i, ii, f)
                        if not v:
                            trous += 1
                            continue
                        if len([l for l in v if l not in ("R11-arret", "R12-invalide", "L6")]) > 1:
                            chev += 1
                        l = premiere(v)
                        effectifs[l] += 1
                        if q in ("vide", "non_calculable", "incoherent"):
                            # la ligne ne doit dépendre ni de (i), ni de (ii), ni de F
                            if l != {"vide": "L7", "non_calculable": "L7b", "incoherent": "L7c"}[q]:
                                ecarts += 1
    return {"total": total, "effectifs": effectifs, "classes": classes, "trous": trous, "chevauchements": chev,
            "ecarts_L7": ecarts, "l7_defauts": l7_defauts, "priorite_l7b": priorite_l7b,
            "impossibles": impossibles, "configs": configs, "controles_b12": controles_b12}


def main() -> int:
    cas_agr, defauts_agr = verifier_agregation()
    print(f"(1) agrégation par dose : {cas_agr} cas (4 × 4 + 6 × 16 + 4 × 64 + 1 × 256 = 624), {defauts_agr} sans état")
    c = grille_classes()
    print(f"(2) grille par classes : {c['total']} cas (= 3 × 6 × 8 × 6 × 4 × 4 × 4)")
    for l in ORDRE:
        print(f"      {l:13s} {c['effectifs'][l]:7d}")
    print(f"    trous : {c['trous']} ; chevauchements hors L6 : {c['chevauchements']} ; "
          f"cas jugés : {c['juges']} (attendu {c['juges_attendus']}) ; sous-phrases de L1b en défaut : {c['l1b_defauts']}")
    d = grille_doses()
    print(f"(3) grille par états par dose : {d['total']} cas (G = ok, P = vu, A = A4 ; écart interne 5 × liste écrite 4 × "
          f"étiquette 4 × P-064 2 × base 3^4 × effet 3^4 × (i) 4 × F 4 × sondes 4^k par dose jugée)")
    print(f"    configurations de dose : {d['configs']} (impossibles sautées : {d['impossibles']})")
    print("    classes dérivées : " + ", ".join(f"{q} {n}" for q, n in d["classes"].items()))
    for l in ORDRE:
        if d["effectifs"][l]:
            print(f"      {l:13s} {d['effectifs'][l]:9d}")
    print(f"    trous : {d['trous']} ; chevauchements hors L6 : {d['chevauchements']} ; L7, L7b, L7c dépendant de (i), "
          f"(ii) ou F : {d['ecarts_L7']} ; sous-phrases de L7 en défaut : {d['l7_defauts']} ; "
          f"dose non calculable sans écart interne hors L7b : {d['priorite_l7b']} ; "
          f"écart « aire » ou liste à l'envers hors incoherent : {d['controles_b12']}")
    ok = (defauts_agr == 0 and cas_agr == 624 and c["trous"] == 0 and c["chevauchements"] == 0
          and c["juges"] == c["juges_attendus"] and c["l1b_defauts"] == 0 and sum(c["effectifs"].values()) == c["total"]
          and d["trous"] == 0 and d["chevauchements"] == 0 and d["ecarts_L7"] == 0 and d["l7_defauts"] == 0
          and d["priorite_l7b"] == 0 and d["controles_b12"] == 0 and sum(d["effectifs"].values()) == d["total"])
    print("GRILLE COMPLÈTE, SANS ZONE MORTE NI CHEVAUCHEMENT HORS L6" if ok else "GRILLE EN DÉFAUT")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
