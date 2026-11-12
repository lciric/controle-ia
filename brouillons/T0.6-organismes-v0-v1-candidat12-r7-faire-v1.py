"""Révision 7 de T0.6 candidat 12 : r6 + couples K1 à K7 de la contre-lecture 5, puis marqueur EMPREINTE_RAPPORT_CL5_T06 rempli par la mère.
Chaque « ancien » doit être présent exactement une fois au moment de son application ; sinon arrêt sans écriture (R12)."""
import hashlib, json, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
h = lambda b: hashlib.sha256(b).hexdigest()
r6 = (R / "brouillons/T0.6-organismes-v0-v1-candidat12-r6.md").read_bytes()
assert h(r6) == "b00ed0711f9a979496e3b7b811f7001ac67eb8b5ccfe1baef080d30ec0a7e0fe"
cb = (R / "prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r6-cl5-couples-v1.json").read_bytes()
assert h(cb) == "ccfc6ca2ad4aac5861ae40903a3d864389d8a5c0141922ff5260ff23b4e6d71c"
t = r6.decode("utf-8")
for c in json.loads(cb):
    n = t.count(c["ancien"])
    if n != 1: sys.exit(f"{c['id']} : « ancien » présent {n} fois ; arrêt sans écriture")
    t = t.replace(c["ancien"], c["nouveau"])
assert h(t.encode()) == "aa9368fdc14002cd187a411c1e7340816a7aca5cc24e85ee8225fa310c37ca3e", h(t.encode())
m = "<<EMPREINTE_RAPPORT_CL5_T06>>"; assert t.count(m) == 1
t = t.replace(m, "a951aaaa52c68703777b9098669ac53c7f5b5c7e9c6540f7845a189a21cd6ff0")
o = R / "brouillons/T0.6-organismes-v0-v1-candidat12-r7.md"
assert not o.exists(), "R12"
o.write_text(t, encoding="utf-8")
print("r7 :", h(t.encode()))
