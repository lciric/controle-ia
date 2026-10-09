"""Mémoire de la carte pour la phase de logique en double précision (T0.4, version 2) : calcul reproductible.

Entrées scellées (lues sur disque, empreintes vérifiées par l'appelant) :
- sonde de mémoire, instance 54311651 : traces/t04-20261005-121227-nRet/sonde-memoire.json ;
- run A de la v1 : diag/20261005-102042-validation-reelle/arret.json et ses trajectoires de logique.

Modèle : surcroît de mémoire d'un lot de 8 en génération, pour une longueur remplie L, s(L) = a·L² + b·L (les
matrices d'attention du noyau « math » sont quadratiques en L ; cache, activations et couches denses sont linéaires).
Deux points : la sonde (double précision, L = 1 400) et le pic de la v1 (simple précision, L = 2 329, doublé pour la
double précision ; c'est une borne haute si le pic de la v1 venait d'ailleurs que de la génération).

    python docs/notes/memoire-T0.4-v2/calcul_memoire_v1.py   (depuis la racine du dépôt)
"""
import glob
import json
import math

sonde = json.load(open("traces/t04-20261005-121227-nRet/sonde-memoire.json"))
arret = json.load(open("diag/20261005-102042-validation-reelle/arret.json"))
arret = arret.get("resultat", arret)

poids64 = sonde["etapes"]["chargement"]["alloue_go"]
L1 = sonde["charge"]["longueur_max"]
s1 = sonde["etapes"]["generation"]["pic_go"] - poids64

# trajectoires de logique de la v1 : longueur remplie de chaque lot (plus long contexte des 8 lignes, par pas et agent),
# et surcoût par pas entre deux actions d'une même transcription (clôture, observation, en-têtes)
remplies, ecarts, premiers, max_action = {}, [], [], 0
for f in sorted(glob.glob("diag/20261005-102042-validation-reelle/logique-episode-*-trajectoire.json")):
    r = json.load(open(f))
    r = r.get("resultat", r)
    for tr in r["transcriptions"]:
        acts = tr["actions"]
        premiers.append(acts[0]["debut"])
        for a in acts:
            remplies[(a["pas"], a["agent"])] = max(remplies.get((a["pas"], a["agent"]), 0), a["debut"])
            max_action = max(max_action, a["fin"] - a["debut"])
        ecarts += [b["debut"] - a["fin"] for a, b in zip(acts, acts[1:])]
L2 = max(remplies.values())
poids32 = poids64 / 2
s2 = 2 * (arret["partiel"]["logique"]["memoire_max_go"] - poids32)

# s(L) = a L² + b L passant par (L1, s1) et (L2, s2)
a = (s2 / L2 - s1 / L1) / (L2 - L1)
b = s1 / L1 - a * L1


def pic(L):
    return poids64 + a * L * L + b * L


T, max_nouveaux = 10, 256
L_borne = max(premiers) + (T - 1) * (max_nouveaux + max(ecarts))
carte = {"A100 80 Go": 79.25 * 2 ** 30 / 1e9, "H200 141 Go": 140.4 * 2 ** 30 / 1e9, "B200": 179.1 * 2 ** 30 / 1e9}


def L_max(capacite_go, reserve_go=1.0):
    disponible = capacite_go - reserve_go - poids64
    return (-b + math.sqrt(b * b + 4 * a * disponible)) / (2 * a)


sortie = {
    "poids_double_go": poids64, "sonde": {"L": L1, "surcroit_go": round(s1, 3)},
    "v1": {"L_remplie_max": L2, "surcroit_double_estime_go": round(s2, 3),
           "longueurs_remplies_par_pas_agent": {f"{p},{i}": v for (p, i), v in sorted(remplies.items())}},
    "modele": {"a_go_par_jeton2": a, "b_go_par_jeton": b},
    "pic_estime_go": {str(L): round(pic(L), 1) for L in (1400, 2329, L_borne)},
    "borne_theorique": {"premier_contexte_max": max(premiers), "action_max_v1": max_action,
                        "surcout_par_pas_max": max(ecarts), "L_borne": L_borne,
                        "formule": "premier contexte + (T − 1) × (256 + surcoût par pas maximal de la v1)"},
    "L_max_par_carte": {k: round(L_max(v)) for k, v in carte.items()},
}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
