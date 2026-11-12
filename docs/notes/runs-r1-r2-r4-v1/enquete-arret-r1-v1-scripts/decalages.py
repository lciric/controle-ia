"""Pour chaque épisode conforme en longueur à trajectoire différente : résolution des fins (code du rejeu), puis
recherche des retokenisations de même longueur qui redonnent l'empreinte de P3 (une paire de jetons voisins redécoupée)."""
import json, sys, pickle, copy, hashlib, time
import numpy as np
from transformers import AutoTokenizer
sys.path.insert(0, "src")
from controle_ia.harnais.formats import FormatChat
from controle_ia.runs_nuit.rejeu_activations_v1 import episode_harnais, empreinte_trajectoire, resoudre_fins
from controle_ia.premier_test_ia.conditions import charger_consignes, environnement
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches, tache_de

tok = AutoTokenizer.from_pretrained(sys.argv[1])
fmt = FormatChat(tok, variables={"date_string": "26 Jul 2024"})
fmt.fins = {128001, 128008, 128009}
recs = pickle.load(open(sys.argv[2], "rb"))
fiches = {f["episode"]: f["empreintes"]["trajectoire"] for f in json.load(open("diag/20261019-230011-p3-reel/episodes-p3.json"))["resultat"]["fiches"]}
R = "donnees/20261019-230011-p3-reel/"
with np.load(R + "scores-p3.npz", allow_pickle=False) as z:
    jetons = [int(x) for x in z["jetons"]]; notes = [int(x) for x in z["jetons_notes"]]
lignes = [json.loads(x) for x in open(R + "textes-actions-p3.jsonl", encoding="utf-8")]
taches = {t["identifiant"]: t for t in charger_taches("donnees/t05-pilote-v1/taches-pilote-60-v1.json")}
consignes = charger_consignes("prereg/P3-consignes-v1.md", "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c")
guide = charger_invite("H1-classification")
# octets de chaque jeton (BPE au niveau de l'octet)
def bytes_to_unicode():
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]; n = 0
    for b in range(256):
        if b not in bs: bs.append(b); cs.append(256 + n); n += 1
    return dict(zip(bs, map(chr, cs)))
b2u = bytes_to_unicode(); u2b = {v: k for k, v in b2u.items()}
vocab = tok.get_vocab()
def octets(i):
    s = tok.convert_ids_to_tokens(i)
    return bytes(u2b[c] for c in s)
par_octets = {}
for s, i in vocab.items():
    if i < 128000:
        par_octets[bytes(u2b[c] for c in s)] = i

def variante_hash(e, rec, t, k, nouv):
    r2 = copy.deepcopy(rec)
    a = r2["actions"][t]
    a["nv"] = list(a["nv"]); a["nv"][k:k + 2] = nouv
    p = a["debut"] + k
    r2["ids"] = list(r2["ids"]); r2["ids"][p:p + 2] = nouv
    return empreinte_trajectoire(episode_harnais(e, 10, r2)), r2

inexp = [e for e, v in recs.items() if v["conf"] and not v["ident"]]
bilan = {}
for e in inexp:
    rs = recs[e]["rs"]; x0 = lignes[rs[0]]
    env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), 10, guide, consignes)
    tr = resoudre_fins(fmt, env, 10, [lignes[r] for r in rs], [jetons[r] for r in rs], [notes[r] for r in rs], fiches[e], e)
    if tr is not None:
        bilan[e] = {"cause": "jeton de fin", "detail": [a["nv"][-1] for a in tr[0]["actions"] if a["nv"]]}
        print(e, "-> résolu par substitution du jeton de fin"); continue
    rec = recs[e]["rec"]; trouve = []; essais = 0
    for t, a in enumerate(rec["actions"]):
        n = len(a["nv"]) - (1 if (jetons[rs[t]] - notes[rs[t]]) == 1 else 0)
        for k in range(n - 1):
            x, y = a["nv"][k], a["nv"][k + 1]
            B = octets(x) + octets(y)
            for c in range(1, len(B)):
                if c == len(octets(x)): continue
                g, d = par_octets.get(B[:c]), par_octets.get(B[c:])
                if g is None or d is None: continue
                essais += 1
                h, r2 = variante_hash(e, rec, t, k, [g, d])
                if h == fiches[e]:
                    trouve.append({"pas": t, "rang": k, "canonique": [x, y], "p3": [g, d],
                                   "canonique_txt": [tok.convert_ids_to_tokens(x), tok.convert_ids_to_tokens(y)],
                                   "p3_txt": [tok.convert_ids_to_tokens(g), tok.convert_ids_to_tokens(d)],
                                   "decode_egal": tok.decode(r2["actions"][t]["nv"], skip_special_tokens=True) == a["texte"]})
    bilan[e] = {"essais": essais, "trouve": trouve}
    print(e, "essais", essais, "trouvé", trouve, flush=True)
json.dump(bilan, open(sys.argv[3], "w"), ensure_ascii=False, indent=1)
print("résolus par un redécoupage", sum(1 for v in bilan.values() if v.get("trouve")), "/", len(bilan))
