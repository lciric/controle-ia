"""Contre-lecture courte : un cache partiel passe-t-il `revision_au_cache` ? Caches factices à la forme du cache de
huggingface_hub (blobs, liens symboliques des snapshots, refs) ; hors ligne ; aucun réseau."""
import json, os, sys
from pathlib import Path
os.environ["HF_HUB_OFFLINE"] = "1"
sys.path.insert(0, sys.argv[1])
base = Path(sys.argv[2])
GardeArret = None
from controle_ia.t07 import reextraction_p3_v1 as rx
GardeArret = rx.GardeArret
REV = "0e9e39f249a16976918f6564b8830bc894c89659"
N = 4
PARTS = [f"model-{i:05d}-of-{N:05d}.safetensors" for i in range(1, N + 1)]
INDEX = json.dumps({"weight_map": {f"p{i}": n for i, n in enumerate(PARTS)}})
COMPLET = {"config.json": "{}", "tokenizer.json": "{}", "tokenizer_config.json": "{}", "model.safetensors.index.json": INDEX, **{n: "poids" for n in PARTS}}

def cache(nom, fichiers, casses=(), ref=None):
    c = base / nom
    if c.exists():
        return c
    m = c / "models--org--nom"
    (m / "blobs").mkdir(parents=True); snap = m / "snapshots" / REV; snap.mkdir(parents=True)
    for i, (n, contenu) in enumerate(fichiers.items()):
        b = m / "blobs" / f"blob{i}"
        if n not in casses:
            b.write_text(contenu, encoding="utf-8")
        (snap / n).symlink_to(os.path.relpath(b, snap))
    if ref:
        (m / "refs").mkdir(); (m / "refs" / ref).write_text(REV)
    return c

def essai(titre, c, rev=REV):
    try:
        r = rx.revision_au_cache("org/nom", rev, str(c)); issue = f"PASSE (poids {r['poids']})"
    except GardeArret as e:
        issue = f"refusé (GardeArret) : {e}"
    except Exception as e:
        issue = f"exception hors garde {type(e).__name__} : {e}"
    print(f"{titre} -> {issue}", flush=True)

essai("0. cache complet (liens symboliques)", cache("complet", COMPLET))
essai("1. index absent, un seul morceau sur quatre présent", cache("sans-index", {k: v for k, v in COMPLET.items() if k != "model.safetensors.index.json" and k not in PARTS[1:]}))
essai("2. index présent, un lien cassé (blob absent)", cache("lien-casse", COMPLET, casses=(PARTS[2],)))
essai("3. index présent, un morceau de taille nulle", cache("vide", {**COMPLET, PARTS[1]: ""}))
essai("4. index illisible (JSON tronqué)", cache("index-tronque", {**COMPLET, "model.safetensors.index.json": INDEX[:40]}))
essai("5. index sans weight_map", cache("index-sans-carte", {**COMPLET, "model.safetensors.index.json": "{}"}))
essai("6. révision donnée par un nom de branche (main)", cache("branche", COMPLET, ref="main"), rev="main")
essai("7. index présent, weight_map vide", cache("carte-vide", {k: v for k, v in {**COMPLET, "model.safetensors.index.json": json.dumps({"weight_map": {}})}.items() if k not in PARTS}))
essai("8. generation_config.json et special_tokens_map.json absents (comme 0)", cache("complet", COMPLET))
