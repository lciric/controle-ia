"""Épisodes restants : deux redécoupages de paires (même action ou actions différentes), empreinte de P3 comme arbitre."""
import json, sys, pickle, hashlib, itertools, time
from transformers import AutoTokenizer
sys.path.insert(0, "src")
from controle_ia.runs_nuit.rejeu_activations_v1 import episode_harnais, empreinte_trajectoire
exec(open(sys.argv[4]).read())  # bytes_to_unicode
tok = AutoTokenizer.from_pretrained(sys.argv[1])
recs = pickle.load(open(sys.argv[2], "rb"))
bilan = json.load(open(sys.argv[3]))
fiches = {f["episode"]: (f["empreintes"]["trajectoire"]) for f in json.load(open("diag/20261019-230011-p3-reel/episodes-p3.json"))["resultat"]["fiches"]}
u2b = {v: k for k, v in bytes_to_unicode().items()}
par_octets = {bytes(u2b[c] for c in s): i for s, i in tok.get_vocab().items() if i < 128000}
oc = lambda i: bytes(u2b[c] for c in tok.convert_ids_to_tokens(i))
def h(e, rec, ids, nvs):
    d = {"identifiant": e, "N": 1, "T": 10, "transcriptions": [{"agent": 0, "ids": ids, "actions": [
        {"agent": 0, "pas": a["pas"], "debut": a["debut"], "fin": a["debut"] + len(nv), "ids": nv, "texte": a["texte"]}
        for a, nv in zip(rec["actions"], nvs)]}]}
    return hashlib.sha256(json.dumps(d, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
res = {}
for e, b in bilan.items():
    if b.get("cause") or b.get("trouve"): continue
    rec = recs[e]["rec"]; ids0 = [int(x) for x in rec["ids"]]; nv0 = [[int(x) for x in a["nv"]] for a in rec["actions"]]
    assert h(e, rec, ids0, nv0) == empreinte_trajectoire(episode_harnais(e, 10, rec))
    cands = []
    for t, nv in enumerate(nv0):
        for k in range(len(nv) - 1):
            x, y = nv[k], nv[k + 1]
            if x >= 128000 or y >= 128000: continue
            B = oc(x) + oc(y)
            for c in range(1, len(B)):
                if c == len(oc(x)): continue
                g, d = par_octets.get(B[:c]), par_octets.get(B[c:])
                if g is not None and d is not None: cands.append((t, k, g, d))
    t0 = time.time(); trouve = None; n = 0
    for c1, c2 in itertools.combinations(cands, 2):
        if c1[0] == c2[0] and abs(c1[1] - c2[1]) < 2: continue
        n += 1
        nvs = [list(v) for v in nv0]; ids = list(ids0)
        for (t, k, g, d) in (c1, c2):
            nvs[t][k:k + 2] = [g, d]; p = rec["actions"][t]["debut"] + k; ids[p:p + 2] = [g, d]
        if h(e, rec, ids, nvs) == fiches[e]:
            trouve = [dict(pas=c[0], rang=c[1], p3_txt=[tok.convert_ids_to_tokens(c[2]), tok.convert_ids_to_tokens(c[3])],
                           canonique_txt=[tok.convert_ids_to_tokens(x) for x in nv0[c[0]][c[1]:c[1] + 2]]) for c in (c1, c2)]
            break
    res[e] = {"candidats": len(cands), "paires_essayees": n, "trouve": trouve, "s": round(time.time() - t0)}
    print(e, res[e], flush=True)
json.dump(res, open(sys.argv[5], "w"), ensure_ascii=False, indent=1)
print("résolus par deux redécoupages", sum(1 for v in res.values() if v["trouve"]), "/", len(res))
