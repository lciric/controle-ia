"""Vérifications mécaniques du brouillon 15 de T0.7 (sondes v0) — v1.

Écrit le 2026-11-09 par le rédacteur du brouillon 15 (Claude Opus 5.5, sous-agent neuf). Bibliothèque standard et numpy
seulement ; aucune écriture sur disque ; n'imprime que des comptes, des booléens et des noms de marqueurs (jamais un
poids, un score, une aire ni un champ de `meta`).

Usage : cd /tmp && <python avec numpy> -I -B <chemin absolu de ce script> <racine absolue du dépôt> [partie]
        partie ∈ {couples, brouillon, garde, tout} (défaut : tout). Code 0 si tout passe, 1 sinon.

(1) couples : compte, dans `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` (empreinte exigée `701f73bd…`,
    égale à son compagnon), les sondes, les planchers et les couples (famille, concept, couche) hors planchers ; lit
    l'index JSON du fichier sans `pickle` (`allow_pickle=False`), sans reconstruire aucune sonde.
(2) brouillon : marqueurs `<<…>>` du brouillon 15 comptés par le motif de `controle_ia.prereg.GABARIT` (même motif que le
    `grep -o '<<[A-Z0-9_]\\+>>'` du texte), comparés à ceux du brouillon 14 ; balises de la proposition « garde adaptée »
    (une ouverture, une fermeture, dans cet ordre, le marqueur `MOT_LAZAR_DS2_GARDE` entre elles) ; ligne DS-2 du
    brouillon 14 présente à l'identique (texte en vigueur gardé) ; aucune occurrence restante de « 30 couples figés » ni
    de « 30 figées de P3 » ; `controle_ia.prereg.problemes` ne rend que la ligne des marqueurs.
(3) garde : énumération de la garde PROPOSÉE (non en vigueur) de l'ouverture réduite (G1 à G3), sur le modèle de
    l'énumération (0 bis) du brouillon 14 : tous les ordres de S (`SCELLEMENT-T07`), oA (ouverture de l'étape A), fA (fin :
    `SCORES-T07` et `SONDES-T07`), V (`VERDICT-P3BIS`), P (ouverture pleine de P3-bis) et, en mode « réduite », R (ouverture
    réduite au rendez-vous), avec S < oA < fA, P < V en mode « pleine », R avant V et P en mode « réduite » (R après fA :
    impossible, le rendez-vous tombe, compté), × étape A déjà jouée ; prédicats écrits indépendamment, exactement un vrai
    par cas ; aucune étape A admise après une ouverture pleine ; verdict avant oA admis seulement après une ouverture
    réduite et après S ; étape B seulement si S < V et P après fA ; sans ouverture réduite, l'antériorité en vigueur
    (fA < V) tient ; comparaison au texte en vigueur : la proposition n'interdit rien qu'il permet, et tout ce qu'elle
    ajoute passe par une ouverture réduite. Portée : modèle de la RÈGLE écrite dans la proposition, pas d'un module ; ne
    modélise ni G4 (versions), ni G5 (périmètre), ni les sceaux, ni le journal lui-même.
"""
from __future__ import annotations

import difflib
import hashlib
import itertools
import json
import re
import sys
from pathlib import Path

LEGER = "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz"
SHA_LEGER = "701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60"
B14 = "brouillons/T0.7-sondes-v0-v1-brouillon14.md"
SHA_B14 = "fe7b4e6dbc77edecf56bb16baf24e54939e0f845a76927e144a7f0409fd09345"
B15 = "brouillons/T0.7-sondes-v0-v1-brouillon15.md"
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
DEBUT = "[DÉBUT DE LA PROPOSITION « GARDE ADAPTÉE » — NON EN VIGUEUR]"
FIN = "[FIN DE LA PROPOSITION « GARDE ADAPTÉE »]"
MOT = "<<MOT_LAZAR_DS2_GARDE>>"
FAMILLES_P3 = {"difference_moyennes", "lineaire", "perceptron", "attention"}
CONCEPTS_P3 = {"tromperie", "enjeux"}
COUCHES = {7, 15, 23}


def sha256(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def partie_couples(racine: Path) -> bool:
    import numpy as np
    chemin = racine / LEGER
    sha = sha256(chemin)
    compagnon = (racine / (LEGER + ".sha256")).read_text(encoding="utf-8").split()[0]
    ok = sha == SHA_LEGER and compagnon == SHA_LEGER
    with np.load(chemin, allow_pickle=False) as z:
        index = json.loads(bytes(z["index"]).decode("utf-8"))
    sondes = index["sondes"]
    planchers_meta = index["meta"].get("planchers", {})
    noms_planchers = {n for liste in planchers_meta.values() for n in liste}
    couples = [e for e in sondes if e["nom"] not in noms_planchers]
    planchers = [e for e in sondes if e["nom"] in noms_planchers]
    familles = {e["famille"] for e in couples}
    concepts = {e["nom"].split("-")[0] for e in couples}
    couches = {int(e["couche"]) for e in couples}
    triplets = {(e["famille"], e["nom"].split("-")[0], int(e["couche"])) for e in couples}
    mahalanobis = sum(1 for e in couples if e["classe"] == "SondeMahalanobis")
    mahalanobis_tout = sum(1 for e in sondes if e["classe"] == "SondeMahalanobis")
    nom_ok = all(e["nom"] == f"{e['nom'].split('-')[0]}-{e['famille']}-c{int(e['couche'])}" for e in couples)
    produit = len(familles) * len(concepts) * len(couches)
    print("(1) sondes figées de P3, fichier léger")
    print(f"    empreinte égale à 701f73bd… et au compagnon : {'oui' if ok else 'NON'}")
    print(f"    sondes dans l'index : {len(sondes)}")
    print(f"    planchers (noms listés dans meta.planchers) : {len(planchers)} ; listes : {len(planchers_meta)} ;"
          f" tailles : {sorted(len(v) for v in planchers_meta.values())}")
    print(f"    couples hors planchers : {len(couples)} ; triplets distincts (famille, concept, couche) : {len(triplets)}")
    print(f"    familles : {len(familles)} ; concepts : {len(concepts)} ; couches : {len(couches)} ;"
          f" produit {len(familles)} × {len(concepts)} × {len(couches)} = {produit}")
    print(f"    familles égales à l'attendu (différence de moyennes, linéaire, perceptron, attention) :"
          f" {'oui' if familles == FAMILLES_P3 else 'NON'}")
    print(f"    concepts égaux à l'attendu (tromperie, enjeux) : {'oui' if concepts == CONCEPTS_P3 else 'NON'}")
    print(f"    couches égales à l'attendu (7, 15, 23) : {'oui' if couches == COUCHES else 'NON'}")
    print(f"    noms au patron <concept>-<famille>-c<couche> : {'oui' if nom_ok else 'NON'}")
    print(f"    Mahalanobis parmi les couples : {mahalanobis} ; dans tout l'index : {mahalanobis_tout}")
    attendu = (ok and len(couples) == 24 and len(triplets) == 24 and produit == 24 and familles == FAMILLES_P3
               and concepts == CONCEPTS_P3 and couches == COUCHES and mahalanobis == 0 and mahalanobis_tout == 0
               and len(planchers) == 400 and len(sondes) == 424 and nom_ok)
    print(f"    24 couples = 4 × 2 × 3, aucune Mahalanobis, 424 = 24 + 400 : {'oui' if attendu else 'NON'}")
    return attendu


def partie_brouillon(racine: Path) -> bool:
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # code du dépôt, lu depuis la racine passée en argument
    t14 = (racine / B14).read_text(encoding="utf-8")
    t15 = (racine / B15).read_text(encoding="utf-8")
    ok14 = sha256(racine / B14) == SHA_B14
    m14 = sorted(set(GABARIT.findall(t14)))
    occ15 = {m: t15.count(m) for m in sorted(set(GABARIT.findall(t15)))}
    m15 = sorted(occ15)
    print("(2) brouillon 15")
    print(f"    brouillon 14 à l'empreinte fe7b4e6d… : {'oui' if ok14 else 'NON'}")
    print(f"    lignes : brouillon 14 {t14.count(chr(10))} ; brouillon 15 {t15.count(chr(10))}")
    print(f"    marqueurs distincts : brouillon 14 {len(m14)} ; brouillon 15 {len(m15)}")
    print(f"    ajoutés : {sorted(set(m15) - set(m14))} ; retirés : {sorted(set(m14) - set(m15))}")
    for m, n in occ15.items():
        print(f"      {m} : {n}")
    i_debut, i_fin = t15.find(DEBUT), t15.find(FIN)
    dedans = t15[i_debut:i_fin].count(MOT) if 0 <= i_debut < i_fin else 0
    balises = t15.count(DEBUT) == 1 and t15.count(FIN) == 1 and 0 <= i_debut < i_fin and dedans >= 1
    print(f"    balises de la proposition : ouverture {t15.count(DEBUT)}, fermeture {t15.count(FIN)} ; dans l'ordre :"
          f" {'oui' if 0 <= i_debut < i_fin else 'NON'} ; {MOT} entre elles : {dedans} fois ;"
          f" lignes entre elles : {t15[i_debut:i_fin].count(chr(10)) if 0 <= i_debut < i_fin else 0}")
    ds2 = [l for l in t14.splitlines() if l.startswith("| DS-2 ordre de lecture de T0.7 |")]
    ds2_garde = len(ds2) == 1 and t15.count(ds2[0]) == 1
    print(f"    ligne DS-2 du brouillon 14 présente à l'identique dans le brouillon 15 : {'oui' if ds2_garde else 'NON'}")
    # la table « du 14 au 15 » cite l'ancien compte entre guillemets : elle est retirée avant de compter
    tete = "## Table « ce qui change du 14 au 15 »"
    i_t = t15.find(tete)
    j_t = t15.find("\n## ", i_t + len(tete)) if i_t >= 0 else -1
    hors_table = t15[:i_t] + t15[j_t:] if 0 <= i_t < j_t else t15
    restes = {motif: hors_table.count(motif) for motif in ("30 couples figés", "30 figées de P3")}
    neufs = {motif: hors_table.count(motif) for motif in ("24 couples figés", "24 figées de P3")}
    print(f"    table « du 14 au 15 » trouvée : {'oui' if 0 <= i_t < j_t else 'NON'} ; hors de cette table,"
          f" occurrences restantes : {restes} ; occurrences neuves : {neufs}")
    p = problemes(racine / B15)
    seuls_marqueurs = len(p) == 1 and p[0].startswith("marqueurs de gabarit restants")
    print(f"    controle_ia.prereg.problemes : {len(p)} problème(s) ; seule la ligne des marqueurs :"
          f" {'oui' if seuls_marqueurs else 'NON'}")
    chevrons_p3bis = [m for m in m15 if m.startswith("<<T07_B15_") or m == "<<DATE_RENDEZ_VOUS_LAZAR>>"]
    print(f"    marqueurs de P3-bis écrits entre chevrons dans T0.7 : {len(chevrons_p3bis)}")
    diff = list(difflib.unified_diff(t14.splitlines(), t15.splitlines(), lineterm="", n=0))
    plus = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
    moins = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
    blocs = sum(1 for l in diff if l.startswith("@@"))
    print(f"    écart au brouillon 14 : {blocs} blocs, {plus} lignes ajoutées, {moins} lignes retirées")
    attendu = (ok14 and set(m15) - set(m14) == {MOT} and not set(m14) - set(m15) and balises and ds2_garde
               and all(v == 0 for v in restes.values()) and seuls_marqueurs and not chevrons_p3bis)
    print(f"    brouillon 15 conforme aux contrôles (2) : {'oui' if attendu else 'NON'}")
    return attendu


def issues_proposees(r: dict, mode: str, deja: bool) -> list[str]:
    """Règle écrite de la proposition « garde adaptée » (brouillon 15, section « Écrits exigés par P3-bis », (d), G1 à G3),
    en prédicats indépendants : la vérification est qu'un et un seul est vrai dans chaque cas."""
    reduite = mode == "réduite"
    verdict_admis = r["V"] > r["oA"] or (reduite and r["S"] < r["V"])         # G2 (et G1 pour un verdict avant oA)
    ouverte = (not deja) and r["P"] > r["oA"] and verdict_admis
    vraies = []
    if deja:
        vraies.append("refus : étape A déjà jouée")
    if not deja and r["P"] < r["oA"]:
        vraies.append("refus : ouverture pleine de P3-bis avant l'étape A (nœud)")
    if not deja and r["P"] > r["oA"] and not verdict_admis:
        vraies.append("refus : VERDICT-P3BIS avant l'étape A sans ouverture réduite valable (nœud)")
    if ouverte and r["P"] < r["fA"]:
        vraies.append("nœud : ouverture pleine de P3-bis avant la fin de l'étape A")
    if ouverte and r["P"] > r["fA"] and r["V"] < r["S"]:
        vraies.append("nœud : SCELLEMENT-T07 postérieur à VERDICT-P3BIS")
    if ouverte and r["P"] > r["fA"] and r["S"] < r["V"] and reduite:
        vraies.append("étape B possible : ouverture réduite, pleine après fA")
    if ouverte and r["P"] > r["fA"] and r["S"] < r["V"] and not reduite:
        vraies.append("étape B possible : chemin normal")
    return vraies


def etape_b_en_vigueur(r: dict, mode: str, deja: bool) -> bool:
    """Texte en vigueur (brouillon 14, garde d'ordre R-1924 (3) et CLT7B-03 ; écrit (c) du brouillon 15) : étape A ouverte
    seulement si V est absente et qu'aucune ouverture de P3-bis ne la précède ; étape B seulement si fA < V et si aucune
    ouverture de P3-bis (réduite ou pleine) ne précède fA."""
    premiere = min(r["P"], r["R"]) if mode == "réduite" else r["P"]
    return (not deja) and r["V"] > r["oA"] and premiere > r["oA"] and r["fA"] < r["V"] and premiere > r["fA"]


def partie_garde() -> bool:
    cas = defauts = impossibles = 0
    issues: dict[str, int] = {}
    b_vigueur = b_proposee = b_ecarts_non_reduits = 0
    for mode in ("pleine", "réduite"):
        evenements = ("S", "oA", "fA", "V", "P") + (("R",) if mode == "réduite" else ())
        for ordre in itertools.permutations(evenements):
            r = {e: i for i, e in enumerate(ordre)}
            if not (r["S"] < r["oA"] < r["fA"]):      # T0.7 scellé avant la création de 7b ; l'étape A s'ouvre avant de finir
                continue
            if not r["P"] < r["V"] and mode == "pleine":
                continue                               # ouverture pleine (branche 2 ou chemin normal) : le verdict la suit
            if mode == "réduite" and not (r["R"] < r["V"] and r["R"] < r["P"]):
                continue                               # ouverture réduite : le verdict et l'ouverture pleine la suivent
            if mode == "réduite" and r["R"] > r["fA"]:
                impossibles += 2                       # P3-bis b5 : le rendez-vous tombe après SCORES-T07 et SONDES-T07
                continue
            for deja in (False, True):
                cas += 1
                vraies = issues_proposees(r, mode, deja)
                if len(vraies) != 1:
                    defauts += 1
                    continue
                v = vraies[0]
                issues[v] = issues.get(v, 0) + 1
                ouverte = not v.startswith("refus")
                b = v.startswith("étape B")
                if ouverte and r["P"] < r["oA"]:
                    defauts += 1                       # aucune étape A admise après une ouverture pleine
                if ouverte and r["V"] < r["oA"] and not (mode == "réduite" and r["S"] < r["V"]):
                    defauts += 1                       # G2 : verdict avant oA admis seulement après une ouverture réduite
                if b and not (r["S"] < r["V"] and r["P"] > r["fA"]):
                    defauts += 1                       # G1 et G3 : verdict après le scellement, ouverture pleine après fA
                if v == "étape B possible : chemin normal" and not r["fA"] < r["V"]:
                    defauts += 1                       # sans ouverture réduite, l'antériorité en vigueur tient
                en_vigueur = etape_b_en_vigueur(r, mode, deja)
                b_vigueur += en_vigueur
                b_proposee += b
                if en_vigueur and not b:
                    defauts += 1                       # la proposition n'interdit rien que le texte en vigueur permet
                if b and not en_vigueur and mode != "réduite":
                    b_ecarts_non_reduits += 1
    defauts += b_ecarts_non_reduits                    # tout ce que la proposition ajoute passe par une ouverture réduite
    print("(3) garde PROPOSÉE (non en vigueur) de l'ouverture réduite")
    print(f"    cas : {cas} ; configurations impossibles sautées (ouverture réduite après fA, × 2) : {impossibles} ;"
          f" défauts : {defauts}")
    for v in sorted(issues):
        print(f"      {v} : {issues[v]}")
    print(f"    étape B possible : texte en vigueur {b_vigueur} cas ; proposition {b_proposee} cas ; ajoutés par la"
          f" proposition hors ouverture réduite : {b_ecarts_non_reduits}")
    return defauts == 0 and cas > 0


def main() -> int:
    racine = Path(sys.argv[1]).resolve()
    partie = sys.argv[2] if len(sys.argv) > 2 else "tout"
    resultats = []
    if partie in ("couples", "tout"):
        resultats.append(partie_couples(racine))
    if partie in ("brouillon", "tout"):
        resultats.append(partie_brouillon(racine))
    if partie in ("garde", "tout"):
        resultats.append(partie_garde())
    print("TOUT PASSE" if all(resultats) else "ÉCHEC")
    return 0 if all(resultats) else 1


if __name__ == "__main__":
    sys.exit(main())
