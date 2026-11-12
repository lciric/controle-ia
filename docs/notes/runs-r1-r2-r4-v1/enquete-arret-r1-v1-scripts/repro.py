"""Reproduction sur processeur de la phase de reconstruction du rejeu R1 (sans modèle, sans scores)."""
import json, sys, pickle
from pathlib import Path
import numpy as np
from transformers import AutoTokenizer
sys.path.insert(0, "src")
from controle_ia.harnais.formats import FormatChat
from controle_ia.runs_nuit.rejeu_activations_v1 import reconstruire_episode, episode_harnais, empreinte_trajectoire, resoudre_fins
from controle_ia.premier_test_ia.conditions import charger_consignes, environnement
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches, tache_de

TOK = sys.argv[1]
tok = AutoTokenizer.from_pretrained(TOK)
print("classe", type(tok).__name__, "clean_up", getattr(tok, "clean_up_tokenization_spaces", None))
fmt = FormatChat(tok, variables={"date_string": "26 Jul 2024"})
fmt.fins = {128001, 128008, 128009} | {fmt._pieces(("x", "y"))["cloture"][0]}
print("fins", sorted(fmt.fins), "cloture", fmt._pieces(("x", "y"))["cloture"])
R = "donnees/20261019-230011-p3-reel/"
with np.load(R + "scores-p3.npz", allow_pickle=False) as z:   # seulement identité et longueurs, jamais les scores
    jetons = [int(x) for x in z["jetons"]]; notes = [int(x) for x in z["jetons_notes"]]
    ep_id = [str(x) for x in z["episode"]]
lignes = [json.loads(x) for x in open(R + "textes-actions-p3.jsonl", encoding="utf-8")]
assert [l["episode"] for l in lignes] == ep_id
fiches = {f["episode"]: f for f in json.load(open("diag/20261019-230011-p3-reel/episodes-p3.json"))["resultat"]["fiches"]}
taches = {t["identifiant"]: t for t in charger_taches("donnees/t05-pilote-v1/taches-pilote-60-v1.json")}
consignes = charger_consignes("prereg/P3-consignes-v1.md", "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c")
guide = charger_invite("H1-classification")
par_ep = {}
for i, l in enumerate(lignes): par_ep.setdefault(l["episode"], []).append(i)
out = {}
for e, rs in par_ep.items():
    x0 = lignes[rs[0]]
    env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), 10, guide, consignes)
    rec = reconstruire_episode(fmt, env, 10, [lignes[r] for r in rs], [jetons[r] for r in rs], [notes[r] for r in rs])
    conf = all(a["conforme"] for a in rec["actions"])
    ident = empreinte_trajectoire(episode_harnais(e, 10, rec)) == fiches[e]["empreintes"]["trajectoire"]
    jpa_ok = [len(a["nv"]) for a in rec["actions"]] == fiches[e]["jetons_par_action"]
    out[e] = dict(conf=conf, ident=ident, jpa_ok=jpa_ok, rec=rec, rs=rs)
print("episodes", len(out), "conformes", sum(v["conf"] for v in out.values()),
      "identiques", sum(v["ident"] for v in out.values()),
      "conf_non_ident", sum(v["conf"] and not v["ident"] for v in out.values()))
inexp = [e for e, v in out.items() if v["conf"] and not v["ident"]]
print("inexpliques (avant résolution des fins)", len(inexp), inexp[:3])
pickle.dump({e: dict(conf=v["conf"], ident=v["ident"], rs=v["rs"], rec=v["rec"]) for e, v in out.items()},
            open(sys.argv[2], "wb"))
