"""Extrait le bloc bash numéro k de l'ordre scellé (empreinte vérifiée) vers un fichier. Usage : python -I bloc.py ORDRE k SORTIE"""
import sys, re, hashlib
o, k, sortie = sys.argv[1], int(sys.argv[2]), sys.argv[3]
b = open(o, 'rb').read()
assert hashlib.sha256(b).hexdigest() == "30f265a9a1c49a6af734c71a69cdc444989f9ec1c6e294525f43035a28705f18"
blocs = re.findall(r"^```bash\n(.*?)^```", b.decode('utf-8'), re.M | re.S)
assert len(blocs) == 22
open(sortie, 'w', encoding='utf-8').write(blocs[k - 1])
