"""Contre-lecture GD6 : tableau des sorties de gd6-dispersion-beta.py (lots 1 à 4).
Usage : python -I -B tableau-beta-gd6.py SORTIE.md LOT1.json [LOT2.json …]"""
import json
import sys

sortie, lots = sys.argv[1], sys.argv[2:]
cel, equiv = {}, None
for p in lots:
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    cel |= d["cellules"]
    equiv = d["equivalences_icc"]
lignes = ["| loi | n | K_h | K_s | biais | retenue e-BH (A), seuil 40 | min 8 gardes à 40 | min 8 contrastes à 40 | "
          "min 8 gardes à 160 | fiche à 160 |", "|---|---|---|---|---|---|---|---|---|---|"]
for et, c in cel.items():
    loi, n, kh, ks, b = [x.split("=")[-1] for x in et.split("|")]
    s40, s160 = c["seuil_40"], c["seuil_160"]
    lignes.append(f"| {loi} | {n} | {kh} | {ks} | {b} | {c['retenue_fiche_mode1_ebhA']:.3f} | {s40['min_8_gardes']:.3f} | "
                  f"{s40['min_8_contrastes']:.3f} | {s160['min_8_gardes']:.3f} | {s160['fiche']:.3f} |")
texte = "## Équivalences de dispersion\n\n```\n" + json.dumps(equiv, indent=1) + "\n```\n\n## Cellules\n\n" + "\n".join(lignes) + "\n"
with open(sortie, "x", encoding="utf-8") as f:
    f.write(texte)
print(texte)
