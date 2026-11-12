import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1] + "/src")
from controle_ia.accumulation_b6 import code_accb6_v1 as ca, garde_v1 as gv
from controle_ia.t07 import registre_v1 as rg
R = Path("/home/user/controle-ia-travail")
out = Path(sys.argv[2])
p = ca.ecrire_fichier_code(R, "282e295ec8e825b9c045bd30ebfdac3cbe55496f", out, entropie=186246456082298562823446322699284949559)
print("fichier recréé égal à l'octet :", p.read_bytes() == (R / "registres/code-accb6/CODE-ACCB6-v1.json").read_bytes())
lignes, reste = rg.lire_registre_detail(R / gv.REGISTRE_PROPRE, (gv.CODE_ACCB6,), (gv.SCELLEMENT_ACCB6, gv.LECTURE_ACCB6))
print(gv.REGISTRE_PROPRE, lignes, reste)
_, date, chemin, sha = lignes[gv.CODE_ACCB6]
rg.sceau_conforme(R / chemin, sha); print("sceau conforme")
d = gv.lire_fichier_code(R / chemin); print("forme conforme ; entropie", d["entropie"], d["entropie"].bit_length(), "bits")
