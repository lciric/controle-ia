"""Recalcul indépendant (torch + bibliothèque safetensors + numpy, sans le code du script) du couple sonde × couche
de l'essai réel, comparé à la sortie du script. N'affiche aucun jeton ni aucun score : seulement des concordances.
Usage : sortie.json lentille.pt fragment.safetensors sondes.npz tokenizer.json"""
import sys, json, numpy as np, torch
from safetensors.numpy import load_file  # noqa
from safetensors import safe_open
out, pt, st, npz, tokf = sys.argv[1:6]
o = json.load(open(out, encoding="utf-8"))
e = o["sondes"][0]; L = e["couche"]; nom = e["nom"]
z = np.load(npz, allow_pickle=False); idx = json.loads(bytes(z["index"]).decode())
k = [i for i, s in enumerate(idx["sondes"]) if s["nom"] == nom][0]
w = z[f"s{k}_w"].astype(np.float64)
J = torch.load(pt, map_location="cpu", weights_only=True, mmap=True)["J"][L].to(torch.float64)
with safe_open(st, framework="pt") as f:
    WU = f.get_tensor("lm_head.weight").to(torch.float32); g = f.get_tensor("model.norm.weight").to(torch.float64)
res = {}
for lent, v in (("logits", torch.from_numpy(w)), ("jacobienne", torch.from_numpy(w) @ J.T)):
    y = g * v / v.pow(2).mean().sqrt()
    lg = (WU @ y.to(torch.float32)).double().numpy()
    ordre = np.argsort(-lg, kind="stable")
    tp = [t["id"] for t in e["variantes"]["direction"][lent]["plus"]["tete"]]
    tm = [t["id"] for t in e["variantes"]["direction"][lent]["moins"]["tete"]]
    print(f"{lent}: tête + identique (ordre) {tp == ordre[:20].tolist()} ; tête − identique {tm == ordre[::-1][:20].tolist()}")
    for c, info in o["concepts"].items():
        ids = np.array([j["id"] for j in info["jetons"]])
        zz = (lg[ids].mean() - lg.mean()) / lg.std()
        print(f"   concept {c}: z script ≈ z recalculé : {np.isclose(zz, e['variantes']['direction'][lent]['coherence'][c]['z'], atol=1e-4)}")
# jetons du concept : contrôle par la bibliothèque tokenizers
from tokenizers import Tokenizer
tk = Tokenizer.from_file(tokf)
for c, info in o["concepts"].items():
    ok = all(tk.decode([j["id"]]).strip().lower() == j["texte"].strip().lower() for j in info["jetons"])
    print(f"concept {c}: {len(info['jetons'])} jetons, décodage du script = décodage tokenizers : {ok} ; mots sans jeton : {info['mots_sans_jeton']}")
print("vocabulaire :", o["vocabulaire"]); print("lentille_meta :", {k: (v if k != 'source_layers' else f'{len(v)} couches') for k, v in o["lentille_meta"].items()})
print("diagnostics présents :", [k for k in e if k.startswith(("norme", "cosinus"))], "; planchers n =",
      e["variantes"]["direction"]["jacobienne"]["coherence"]["tromperie"]["planchers"].get("n"),
      "; aléatoires n =", e["variantes"]["direction"]["jacobienne"]["coherence"]["tromperie"]["aleatoires"]["n"])
