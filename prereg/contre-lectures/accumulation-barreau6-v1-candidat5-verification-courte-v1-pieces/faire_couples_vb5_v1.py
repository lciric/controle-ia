import json, re, sys, hashlib, subprocess
C5 = "/home/user/controle-ia-travail/brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat5.md"
t = open(C5, encoding="utf-8").read()
assert hashlib.sha256(t.encode()).hexdigest().startswith("d4c7f96e")
H = {"src/controle_ia/prereg.py": "3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306",
     "src/controle_ia/sondes/familles.py": "6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e",
     "src/controle_ia/harnais/sondes.py": "f92657a69cf0d5781017e50117aeb1672dda60719aea51ffbfd9e566f3e7d94d",
     "src/controle_ia/premier_test_ia/statistiques.py": "a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a",
     "src/controle_ia/t07/__init__.py": "553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e",
     "src/controle_ia/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
     "src/controle_ia/sondes/__init__.py": "a4ea91421aa179aa7662876afddde30f6558435c6d60c5ee41f7793613b3ba30",
     "src/controle_ia/harnais/__init__.py": "a977e6e9ad612aa96c099b9c5fb34bb42eb659261dd226780cfc441738b5caaa",
     "src/controle_ia/premier_test_ia/__init__.py": "c72da1602f1998e4c7b30b670e89143d6a9c6337b903164f4bc6eed5ab9a5f92"}
for p, s in H.items():   # recoupé au commit du code, par git show
    blob = subprocess.run(["git", "-C", "/home/user/controle-ia-travail", "--no-optional-locks", "show", f"282e295ec8e825b9c045bd30ebfdac3cbe55496f:{p}"], capture_output=True).stdout
    assert hashlib.sha256(blob).hexdigest() == s, p
noms = list(H)
liste = ", ".join(f"`{p}`" for p in noms[:-1]) + f" et `{noms[-1]}`"
emp = ", ".join(f"`{H[p]}`" for p in noms)
fin = "`e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec`), comparaison écrite avant le lancement"
couples = [
 {"id": "VB5-C1", "constat": "VB5-6", "section": "Plan d'analyse", "gelee": True, "statut": "demandé",
  "ancien": "sans être exigé (absent sous G-1), pour les seules réserves",
  "nouveau": "sans être exigé (non lu sous G-1, où rien n'est lu), pour les seules réserves"},
 {"id": "VB5-C2", "constat": "VB5-8", "section": "Plan d'analyse", "gelee": True, "statut": "recommandé",
  "ancien": fin,
  "nouveau": "`e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec`) ; de même les neuf autres fichiers de `src/controle_ia/` que le paquet charge, par transitivité ou à l'écriture du manifeste, sans qu'aucun calcul décisif y soit appelé (VB5-8, vérification courte du candidat 5 ; `prereg.exiger_prereg_scelle` est appelée par `manifeste.creer_manifeste`) : "
             + liste + " (au commit `282e295e…`, dans cet ordre : " + emp + "), comparaison écrite avant le lancement"},
 {"id": "VB5-C3", "constat": "VB5-5", "section": "Critères de lecture gelés", "gelee": True, "statut": "recommandé",
  "ancien": "et ne se lit jamais comme lui ; le niveau de « accumuler bat » et de « le maximum bat » tient à l'intervalle de Δ",
  "nouveau": "et ne se lit jamais comme lui ; le verdict recopie cette réserve à côté de toute phrase rapportée qui porte « au-dessus de son plancher » (VB5-5) ; le niveau de « accumuler bat » et de « le maximum bat » tient à l'intervalle de Δ"},
 {"id": "VB5-C4", "constat": "VB5-6", "section": "Liste d'arrêt", "gelee": True, "statut": "demandé",
  "ancien": "(champ non exigé, absent sous G-1 ; code v2, `lecture_v1.reserves_t07_recopiees`",
  "nouveau": "(champ non exigé ; non lu sous G-1, où sa forme n'arrête donc pas ; code v2, `lecture_v1.reserves_t07_recopiees`"},
 {"id": "VB5-C5", "constat": "VB5-8", "section": "Liste d'arrêt", "gelee": True, "statut": "recommandé (avec VB5-C2, jamais seul)",
  "ancien": "`t07/plancher_v1.py` ou `t07/registre_v1.py` de l'arbre lancé différent de celui du commit cité : aucun lancement, nœud (plan, point 2 ; CCB-7 ; R-2339).",
  "nouveau": "`t07/plancher_v1.py`, `t07/registre_v1.py` ou l'un des neuf autres fichiers chargés que nomme le plan, point 2, de l'arbre lancé différent de celui du commit cité : aucun lancement, nœud (plan, point 2 ; CCB-7 ; R-2339 ; VB5-8)."},
 {"id": "VB5-C6", "constat": "VB5-9", "section": "Reste avant le scellement", "gelee": False, "statut": "recommandé",
  "ancien": "strictement avant la première ouverture des scores par T0.7 (sinon R-B6-CODE).\n3. **Ligne `SCELLEMENT-ACCB6`**",
  "nouveau": "strictement avant la première ouverture des scores par T0.7 (sinon R-B6-CODE). **Fait** (R-2341) : fichier `registres/code-accb6/CODE-ACCB6-v1.json`, `1957d087d92f31d0219531c06dc5d3ad8058ff5fe20ccfc6b183b1fb5fadc090`, ligne `CODE-ACCB6` du 2026-11-11T12:51:23Z au registre propre ; fichier recréé égal à l'octet et ligne relue par la vérification courte du candidat 5 (VB5-7).\n3. **Ligne `SCELLEMENT-ACCB6`**"},
]
GEL = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse", "Critères de lecture gelés", "Liste d'arrêt")
T = re.compile(r"^## +(.+?)\s*$", re.M)
def sec(x):
    m = list(T.finditer(x)); return [(y.group(1).strip(), x[y.start():m[i+1].start() if i+1 < len(m) else len(x)]) for i, y in enumerate(m)]
pos = []
for c in couples:
    assert t.count(c["ancien"]) == 1, (c["id"], t.count(c["ancien"]))
    dans = [n for n, s in sec(t) if c["ancien"] in s]; assert dans == [c["section"]], (c["id"], dans)
    assert (c["section"] in GEL) == c["gelee"]
    pos.append(t.index(c["ancien"]))
assert pos == sorted(pos), pos
u = t
for c in couples:
    assert u.count(c["ancien"]) == 1; u = u.replace(c["ancien"], c["nouveau"])
v = u
for c in reversed(couples):
    assert v.count(c["nouveau"]) == 1, c["id"]; v = v.replace(c["nouveau"], c["ancien"])
assert v == t
MOT = re.compile(r"\w+(?:[.,/]\w+)*|[^\w\s]")
import difflib
for c in couples:
    a, b = MOT.findall(c["ancien"]), MOT.findall(c["nouveau"])
    sup = [(" ".join(a[i1:i2]), " ".join(b[j1:j2])) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if op in ("replace", "delete")]
    print(c["id"], c["section"], "| retirés ou remplacés :", sup)
sys.path.insert(0, "/home/user/controle-ia-travail/src")
out = sys.argv[1]
json.dump({"objet": "couples proposés par la vérification courte du candidat 5 du barreau 6", "candidat_5_sha256": hashlib.sha256(t.encode()).hexdigest(),
           "sections_gelees": list(GEL), "couples": couples}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(out, "a").write("\n")
print("écrit", out, "; texte après les six couples :", hashlib.sha256(u.encode()).hexdigest(), "; aller-retour égal à l'octet ; ordre du texte")
import tempfile, os
from controle_ia.prereg import problemes
p = os.path.join(os.path.dirname(out), "essai-candidat6.md"); open(p, "w", encoding="utf-8").write(u); print("prereg.problemes :", problemes(p))
