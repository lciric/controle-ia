#!/usr/bin/env python3
"""Contrôle du GO cité au lancement de la comparaison d'échelle v5 (lignée « session-depot », 27 octobre 2026 ;
contre-lecture n° 4, CLW-03). La garde de calcul héritée (`.claude/hooks/garde_calcul.py`) n'admet qu'un GO de type
« calcul », accordé par Lazar et en cours de validité, mais ne lit ni son périmètre ni son plafond. Ce contrôle, appelé
par le lanceur avant toute création, lit la ligne du GO dans `registres/go.md` (8 colonnes : id, accordé le, type,
périmètre, plafond, échéance, accordé par, référence) et arrête si :
  - le GO est absent, en double hors ligne d'extension, ou d'un autre type que « calcul » ;
  - il n'est pas accordé par Lazar ;
  - son périmètre ne cite pas le nom du préenregistrement scellé ET les 16 premiers caractères de son empreinte (un GO
    ne peut citer l'empreinte qu'après le scellement : il est donc nouveau et propre à cette expérience) ;
  - son plafond, en USD, est illisible ou inférieur au plafond du lanceur.
Les lignes d'extension (périmètre commençant par « extension ») ne sont pas lues : le contrôle porte sur la ligne
première, celle qu'un GO nouveau porte seule.
    python -I -B verifier_go_v5.py REGISTRE_GO GO_ID NOM_PREREG EMPREINTE_PREREG PLAFOND_USD
Codes : 0 conforme ; 1 non conforme ; 2 registre illisible ou usage.
"""
import pathlib
import re
import sys


def lignes_go(texte):
    """Lignes du tableau des GO : listes de 8 cellules, sans les espaces de bord."""
    out = []
    for ligne in texte.splitlines():
        if not ligne.startswith("| GO-"):
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split(" | ")]
        if len(cellules) != 8:
            raise ValueError(f"ligne de GO à {len(cellules)} colonnes : {ligne[:80]}")
        out.append(cellules)
    return out


def plafond_usd(cellule):
    m = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*USD\s*", cellule.replace(" ", " ").replace("\xa0", " "))
    return float(m.group(1).replace(",", ".")) if m else None


def verifier(texte, go_id, nom_prereg, empreinte, plafond):
    """(conforme, motifs)."""
    lignes = [l for l in lignes_go(texte) if l[0] == go_id]
    premieres = [l for l in lignes if not l[3].lower().startswith("extension")]
    if not premieres:
        return False, [f"{go_id} absent du registre"]
    if len(premieres) > 1:
        return False, [f"{go_id} en double (hors ligne d'extension)"]
    ident, accorde, type_, perimetre, plaf, echeance, par, reference = premieres[0]
    motifs = []
    if type_ != "calcul":
        motifs.append(f"type « {type_} », et non « calcul »")
    if par != "Lazar":
        motifs.append(f"accordé par « {par} », et non par Lazar")
    if nom_prereg not in perimetre:
        motifs.append(f"le périmètre ne cite pas {nom_prereg}")
    if not re.fullmatch(r"[0-9a-f]{64}", empreinte or ""):
        motifs.append("empreinte du préenregistrement illisible")
    elif empreinte[:16] not in perimetre:
        motifs.append(f"le périmètre ne cite pas l'empreinte du préenregistrement scellé ({empreinte[:16]}…)")
    p = plafond_usd(plaf)
    if p is None:
        motifs.append(f"plafond « {plaf} » illisible (attendu : « N USD »)")
    elif p < plafond:
        motifs.append(f"plafond du GO {p} USD inférieur au plafond du lanceur {plafond} USD")
    return not motifs, motifs


def principal(argv):
    if len(argv) != 5:
        print("usage : verifier_go_v5.py REGISTRE_GO GO_ID NOM_PREREG EMPREINTE_PREREG PLAFOND_USD", file=sys.stderr)
        return 2
    registre, go_id, nom, empreinte, plafond = argv
    try:
        texte = pathlib.Path(registre).read_text(encoding="utf-8")
        ok, motifs = verifier(texte, go_id, nom, empreinte, float(plafond))
    except Exception as e:
        print(f"registre des GO illisible : {e}", file=sys.stderr)
        return 2
    if ok:
        print(f"{go_id} : conforme (calcul, Lazar, périmètre {nom} et {empreinte[:16]}…, plafond ≥ {plafond} USD)")
        return 0
    print(f"{go_id} : non conforme : " + " ; ".join(motifs))
    return 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
