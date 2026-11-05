"""Contre-lecture v2, CLJ-01 : preuves internes au fichier de lentille (aucun modèle exécuté)."""
import sys, csv, math
import torch
pt, csv_path = sys.argv[1], sys.argv[2]
ck = torch.load(pt, map_location="cpu", weights_only=True)
print("cles du fichier :", sorted(ck))
print("provenance presente :", "provenance" in ck)
print("n_prompts :", ck["n_prompts"], "; d_model :", ck["d_model"])
sl = ck["source_layers"]
print("source_layers :", sl[0], "...", sl[-1], "(", len(sl), "couches ) ; egal a range(31) :", list(sl) == list(range(31)))
print("cles de J egales a source_layers :", sorted(ck["J"]) == list(sl))
d = ck["d_model"]
I = torch.eye(d)
dist = {}
for l in sl:
    J = ck["J"][l].float()
    dist[l] = float(torch.linalg.norm(J - I) / math.sqrt(d))
print("||J_l - I||_F / sqrt(d), par couche :")
print("  " + " ; ".join(f"{l}:{dist[l]:.4f}" for l in sl))
rows = list(csv.DictReader(open(csv_path)))
last = rows[-1]
print("derniere ligne de la courbe de convergence : n_done =", last["n_done"], "; identity_distance =", last["identity_distance"])
print("J_30 recalcule (fp16 -> fp32) :", f"{dist[30]:.6f}", "; ecart absolu :", f"{abs(dist[30]-float(last['identity_distance'])):.2e}")
print("n_done de la courbe = n_prompts du fichier :", int(last["n_done"]) == ck["n_prompts"])
