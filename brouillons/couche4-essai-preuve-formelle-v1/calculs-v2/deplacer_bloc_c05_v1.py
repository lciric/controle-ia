"""Retouche R49 : déplace les puces « Exigence de la mère (CLP-04) » et « Machine (CLP-10 b) » après la puce « Garde de calcul »,
pour que le texte inséré par C05 reste d'un seul tenant."""
import re
from pathlib import Path
F = Path("brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon2.md")
T = F.read_text(encoding="utf-8")
d = T.index("\n- **Exigence de la mère (CLP-04)**")
f = T.index("\n- **Garde de calcul**", d)
bloc = T[d:f]
assert T.count("\n- **Exigence de la mère (CLP-04)**") == 1 and "- **Machine (CLP-10 b)**" in bloc
T = T[:d] + T[f:]
m = list(re.finditer(r"\n- \*\*Garde de calcul\*\* : toute machine louée cite un GO valide[^\n]*\n\s+par identifiant \(R10\)\.", T))
assert len(m) == 1
T = T[:m[0].end()] + bloc + T[m[0].end():]
F.write_text(T, encoding="utf-8")
print("R49 : bloc déplacé (", len(bloc.split()), "mots )")
