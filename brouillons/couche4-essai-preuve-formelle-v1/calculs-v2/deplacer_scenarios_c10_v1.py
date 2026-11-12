"""Retouche R50 : déplace les phrases « Scénarios (v4, bloc 1b) … (§ 4.3). » après la dernière phrase de C10."""
from pathlib import Path
F = Path("brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon2.md")
T = F.read_text(encoding="utf-8")
d = T.index(" Scénarios (v4, bloc 1b) :")
fin = "le devis de la phase 2 se lit par scénario (§ 4.3)."
f = T.index(fin, d) + len(fin)
bloc = T[d:f]
assert T.count(" Scénarios (v4, bloc 1b) :") == 1
T = T[:d] + T[f:]
ancre = "la fiche de passage le dit, avec la probabilité calculée."
assert T.count(ancre) == 1
i = T.index(ancre) + len(ancre)
T = T[:i] + bloc + T[i:]
F.write_text(T, encoding="utf-8")
print("R50 : phrases déplacées (", len(bloc.split()), "mots )")
