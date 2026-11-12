import json, hashlib, sys, re
D = sys.argv[1]
b3 = open(f"{D}/preenregistrement-epreuve-etiqueteur-v1-brouillon3.md", encoding="utf-8").read()
b4 = open(f"{D}/preenregistrement-epreuve-etiqueteur-v1-brouillon4.md", encoding="utf-8").read()
couples = json.load(open(f"{D}/couples-contre-lecture-epreuve-etiqueteur-brouillon3-v1.json", encoding="utf-8"))
j = json.load(open(f"{D}/journal-couples-brouillon4-v1.json", encoding="utf-8"))
# annexe B : script embarqué
dev = open(f"{D}/devis_phase1_v3.py", encoding="utf-8").read()
m = b4.split("**`devis_phase1_v3.py`**", 1)[1]
code = m.split("```python\n", 1)[1].split("```", 1)[0]
print("annexe B == devis_phase1_v3.py :", code == dev, hashlib.sha256(code.encode()).hexdigest())
print("empreinte citée :", re.search(r"\*\*`devis_phase1_v3.py`\*\* \(`([0-9a-f]{64})`", b4).group(1))
# couples
for c, jc in zip(couples, j["couples"]):
    assert c["id"] == jc["id"]
    assert hashlib.sha256(c["ancien"].encode()).hexdigest() == jc["empreinte_ancien"]
    assert hashlib.sha256(c["nouveau"].encode()).hexdigest() == jc["empreinte_nouveau"]
    nb3 = b3.count(c["ancien"]); n4new = b4.count(c["nouveau"]); n4old = b4.count(c["ancien"])
    flag = "" if (n4new == c["n"] and nb3 == c["n"]) else "  <-- ÉCART"
    print(f'{c["id"]:45s} n={c["n"]} b3(ancien)={nb3} b4(nouveau)={n4new} b4(ancien)={n4old}{flag}')
