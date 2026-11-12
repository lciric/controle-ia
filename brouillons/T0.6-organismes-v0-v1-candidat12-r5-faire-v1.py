"""Révision 5 de T0.6 candidat 12 : r4 + couples U1 à U13 de la contre-lecture 4, puis trois marqueurs remplis par la mère."""
import hashlib, json, sys
from pathlib import Path
R = Path("/home/user/controle-ia-travail")
r4 = R / "brouillons/T0.6-organismes-v0-v1-candidat12-r4.md"
cp = R / "prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r4-cl4-couples-v1.json"
h = lambda b: hashlib.sha256(b).hexdigest()
assert h(r4.read_bytes()) == "eb6f10a061c671a060d8b3a5b85376e5afd85ba919598d32d93ea362e429e611"
assert h(cp.read_bytes()) == "e6ad9c1550031b65b4cf8e079ac79dcc415a6b47c02b5544172a3d3830a9935c"
t = r4.read_text(encoding="utf-8")
for c in json.loads(cp.read_text(encoding="utf-8")):
    n = t.count(c["ancien"])
    if n != 1:
        sys.exit(f"{c['id']}: « ancien » présent {n} fois, arrêt sans écriture")
    t = t.replace(c["ancien"], c["nouveau"])
apres = h(t.encode("utf-8"))
assert apres == "da9936c422c231152a2429a866cd4c13736defc11f14ddc271500d398f185183", apres
valeurs = {
    "EMPREINTE_RAPPORT_CL4_T06": "001352b795c1c74ea896b0e5c733db1e5babfd220690c8cb84b7d7d06d9dac11",
    "PIECES_PUISSANCE_T06": "R-2066 (vérification par la session mère, 10 novembre 2026, sur la branche d'origine `prep/t06-candidat2-v1`, tête `3bf36bfacfdc1ec67ac3b7e23c1375ba45031119`, récupérée par refspec explicite : `brouillons/T0.6-organismes-v0-v1-candidat2-pieces/puissance_t06_v3.py` `0eea1f9e2f840f9b…`, `brouillons/T0.6-organismes-v0-v1-candidat2-pieces/puissance-t06-v3.txt` `8a2205a130cace2e6144426346581118b3180ed56ae8bf26d0ad01e5cc52c0cb`, `tests/test_t06_puissance_v3.py` `ac71890cb759e4f7e1c53d6466a3639c7c6bc9803a03ea533f588dc2ecb9e32b`, égales aux empreintes citées ; les deux pièces v3 de `brouillons/` sont copiées à l'octet dans le commit de scellement ; réserve : `puissance-t06-v2.txt` et `puissance_t06_v2.py`, pièces du brouillon 2, non retrouvées dans le clone)",
    "DECISION_LAZAR_ECART_DT4_R2041": "option (b), isoler et auditer (mot de Lazar, R-2048) ; audit `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1.md` (`4882fe4dc97aab724da24d12e0e3e2f8f7dce2a07d8ffbd170b26d70f7367d13`, R-2057) et complément `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-complement-v1.md` (`cae6ab643536293672d9b996b82bec04a692229ff517d28d6a362f840fc9d354`, R-2067), verdict « aucune trace trouvée », audit structurel et par catégories, réserve sur l'origine des grandeurs de coût de 7a",
}
for k, v in valeurs.items():
    m = f"<<{k}>>"
    n = t.count(m)
    if n != 1:
        sys.exit(f"{k}: {n} occurrences, arrêt sans écriture")
    t = t.replace(m, v)
out = R / "brouillons/T0.6-organismes-v0-v1-candidat12-r5.md"
assert not out.exists(), "R12 : fichier déjà présent"
out.write_text(t, encoding="utf-8")
print("r4+U :", apres)
print("r5   :", h(t.encode("utf-8")))
