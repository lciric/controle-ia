"""Contre-lecture courte : `controler_avant_ouverture` joué en mode réel sur les fichiers réels de P3 (processeur ; cache du
modèle absent ici : seul le dernier contrôle doit refuser), puis avec un cache factice complet à la révision de P3."""
import json, os, sys
os.environ["HF_HUB_OFFLINE"] = "1"
sys.path.insert(0, sys.argv[1])
racine, cfg, caches = sys.argv[2], sys.argv[3], sys.argv[4]
from pathlib import Path
from controle_ia.t07 import reextraction_p3_v1 as rx, lecture_v4 as lv4
config = lv4.charger_configuration(Path(cfg)) if hasattr(lv4, "charger_configuration") else json.load(open(cfg))
print("configuration : empreinte canonique", lv4.empreinte_configuration(Path(cfg)))
try:
    rx.controler_avant_ouverture(Path(racine), config)
    print("sans cache : PASSE (inattendu)")
except rx.GardeArret as e:
    print("sans cache : refusé :", e)
# cache factice complet au nom du modèle et à la révision de P3
import importlib
m = json.load(open(Path(racine) / config["donnees_p3"]["manifeste_p3"]["chemin"]))["config"]["agent"]
base = Path(caches) / "p3-factice"
snap = base / ("models--" + m["modele"].replace("/", "--")) / "snapshots" / m["revision"]
if not snap.exists():
    snap.mkdir(parents=True)
    for n in ("config.json", "tokenizer.json", "tokenizer_config.json"):
        (snap / n).write_text("{}")
    (snap / "model.safetensors.index.json").write_text(json.dumps({"weight_map": {"a": "model-00001-of-00001.safetensors"}}))
    (snap / "model-00001-of-00001.safetensors").write_text("x")
r = rx.controler_avant_ouverture(Path(racine), config, cache_dir=str(base))
print("cache factice complet : passe ;", json.dumps({k: v for k, v in r.items() if k in ("figees",)}, ensure_ascii=False))
print("modele_p3 :", {k: v for k, v in r["modele_p3"].items() if k != "dossier"})
print("p3 :", json.dumps(r["p3"], ensure_ascii=False)[:600])
