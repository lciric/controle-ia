"""Dépense réelle au pire sur le domaine admis par `choisir_offre_v4.evaluer` (script du commit, importé par chemin).
Facturation supposée : prix relu = 1,05 × l'offre pour tous les postes (tolérance admise), location de la création à
l'arrêt (durée plafonnée + latence de la surveillance), descente des poids et des roues, remontée des résultats,
24 h de stockage après l'arrêt. Aucune donnée réelle, aucun réseau."""
import importlib.util, itertools, json, subprocess, sys
import numpy as np
WT = "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v4/scripts"
spec = importlib.util.spec_from_file_location("of", WT + "/choisir_offre_v4.py")
OF = importlib.util.module_from_spec(spec); spec.loader.exec_module(OF)
T = OF.TOLERANCE_PRIX

def offre(dph, desc, mont, stock):
    return {"id": 1, "gpu_ram": 81920, "num_gpus": 2, "cuda_max_good": 13.2, "inet_down": 5000.0,
            "dph_total": dph, "inet_down_cost": desc, "inet_up_cost": mont, "storage_total_cost": stock}

def reelle(o, duree, latence_s, descente_go, montee_go, stockage_h=24.0):
    return ((duree + latence_s) / 3600 * T * o["dph_total"] + T * descente_go * o["inet_down_cost"]
            + T * montee_go * o["inet_up_cost"] + T * stockage_h * o["storage_total_cost"])

dphs = np.round(np.arange(0.05, 3.5001, 0.05), 4)
descs = np.round(np.linspace(0, 0.005, 11), 6)
monts = [0.0, 0.004, 0.02, 0.1, 0.5, 1.0, 2.0]
admis, pires = 0, {}
cas = {"latence 80 s, 160 Go, 1 Go (hypothèses du texte)": (80, 160, 1),
       "latence 80 s, 164 Go (roues pip et image comptées), 0,3 Go": (80, 164, 0.3),
       "latence 120 s, 164 Go, 0,3 Go": (120, 164, 0.3),
       "latence 196 s, 160 Go, 1 Go": (196, 160, 1),
       "latence 300 s, 160 Go, 1 Go": (300, 160, 1)}
for dph, desc, mont in itertools.product(dphs, descs, monts):
    for stock in np.round(np.linspace(0, min(dph * 0.999, 0.9), 19), 5):
        o = offre(float(dph), float(desc), float(mont), float(stock))
        e = OF.evaluer(o, 3.5, 0.005, 8.0)
        if e is None:
            continue
        admis += 1
        assert e[2] <= 8.0, (o, e)
        for nom, (lat, dg, mg) in cas.items():
            v = reelle(o, e[1], lat, dg, mg)
            if v > pires.get(nom, (0,))[0]:
                pires[nom] = (round(v, 4), {k: o[k] for k in ("dph_total", "inet_down_cost", "inet_up_cost", "storage_total_cost")}, e[1])
print(f"offres admises balayées : {admis} ; pire calculé ≤ 8 USD pour toutes")
for nom, (v, o, d) in pires.items():
    print(f"  {nom} : dépense réelle maximale {v} USD (offre {o}, durée {d} s)")
# rejeu du choix sur la trace des 45 offres relues
D = "/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v4"
SB = "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5/offres"
import os; os.makedirs(SB, exist_ok=True)
r = subprocess.run([sys.executable, "-I", "-B", WT + "/choisir_offre_v4.py", D + "/offres-relues-reference-v2.json",
                    SB + "/offre.json", "3.50", "0.005", "8.00", SB + "/journal.txt", SB + "/relues.json"],
                   capture_output=True, text=True)
print("rejeu sur offres-relues-reference-v2.json : code", r.returncode, "; sortie", r.stdout.strip())
print(open(SB + "/journal.txt").read().strip())
