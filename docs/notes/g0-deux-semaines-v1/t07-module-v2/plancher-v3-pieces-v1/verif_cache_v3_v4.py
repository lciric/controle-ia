"""Formes de cache de la contre-lecture et voisines, jouées contre `revision_au_cache` du v3 (7e23a554) et du dernier tour."""
import json, os, re, sys, tempfile
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from controle_ia.gardes import GardeArret
from controle_ia.t07 import reextraction_p3_v1 as rx4
src = Path(sys.argv[2]).read_text(encoding="utf-8")
a = src.index("def revision_au_cache("); b = src.index("def controler_avant_ouverture(")
ns = {"GardeArret": GardeArret, "Path": Path, "FICHIERS_MODELE": rx4.FICHIERS_MODELE}
exec("from __future__ import annotations\n" + src[a:b], ns)
v3 = ns["revision_au_cache"]
REV = "0e9e39f249a16976918f6564b8830bc894c89659"
idx = lambda m: json.dumps({"weight_map": m})
C = {"config.json": "{}", "tokenizer.json": "{}", "tokenizer_config.json": "{}",
     "model.safetensors.index.json": idx({"a": "model-00001-of-00002.safetensors", "b": "model-00002-of-00002.safetensors"}),
     "model-00001-of-00002.safetensors": "x", "model-00002-of-00002.safetensors": "x"}
sans = lambda *ks: {k: v for k, v in C.items() if k not in ks}
formes = {
 "complet": C,
 "un seul model.safetensors sans index": {**sans("model.safetensors.index.json", "model-00001-of-00002.safetensors", "model-00002-of-00002.safetensors"), "model.safetensors": "x"},
 "index absent, un morceau sur deux": sans("model.safetensors.index.json", "model-00002-of-00002.safetensors"),
 "morceau de taille nulle": {**C, "model-00002-of-00002.safetensors": ""},
 "config.json vide": {**C, "config.json": ""},
 "carte vide, aucun poids": {**sans("model-00001-of-00002.safetensors", "model-00002-of-00002.safetensors"), "model.safetensors.index.json": idx({})},
 "index nomme 1 morceau sur 2": {**C, "model.safetensors.index.json": idx({"a": "model-00001-of-00002.safetensors"})},
 "nombres annoncés mêlés": {**C, "model.safetensors.index.json": idx({"a": "model-00001-of-00002.safetensors", "b": "model-00002-of-00003.safetensors"}), "model-00002-of-00003.safetensors": "x"},
 "JSON faux": {**C, "model.safetensors.index.json": "{"},
 "sans weight_map": {**C, "model.safetensors.index.json": json.dumps({"metadata": {}})},
 "weight_map liste": {**C, "model.safetensors.index.json": json.dumps({"weight_map": ["x"]})},
 "index liste": {**C, "model.safetensors.index.json": json.dumps([1, 2])},
}
def issue(f, base, rev=REV):
    try:
        f("org/nom", rev, str(base)); return "passe"
    except GardeArret as e:
        return "GardeArret : " + str(e)[:90]
    except Exception as e:
        return f"{type(e).__name__}"
racine = Path(tempfile.mkdtemp(dir=sys.argv[3]))
os.environ["HF_HUB_OFFLINE"] = "1"
for i, (nom, fichiers) in enumerate(formes.items()):
    base = racine / str(i)
    d = base / "models--org--nom" / "snapshots" / REV
    d.mkdir(parents=True)
    for k, v in fichiers.items():
        (d / k).write_text(v, encoding="utf-8")
    print(f"{nom} | v3 : {issue(v3, base)} | dernier tour : {issue(rx4.revision_au_cache, base)}")
base = racine / "dossier"
d = base / "models--org--nom" / "snapshots" / REV
d.mkdir(parents=True)
for k, v in sans("model.safetensors.index.json").items():
    (d / k).write_text(v, encoding="utf-8")
(d / "model.safetensors.index.json").mkdir()
print(f"index qui est un dossier | v3 : {issue(v3, base)} | dernier tour : {issue(rx4.revision_au_cache, base)}")
(base / "models--org--nom" / "refs").mkdir()
(base / "models--org--nom" / "refs" / "main").write_text(REV)
print(f"révision « main » par refs | v3 : {issue(v3, base, 'main')} | dernier tour : {issue(rx4.revision_au_cache, base, 'main')}")
