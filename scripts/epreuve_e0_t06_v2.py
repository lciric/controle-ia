"""Épreuve E0 du lanceur de T0.6 v2 (contre-lecture, 0 USD, processeur) : `test_croise_v2` sur des activations SYNTHÉTIQUES
(bruit gaussien, aucune donnée réelle, aucun signal planté), écrites en demi-précision par morceaux sur le disque comme
le fait le lanceur (`ActivationsDemi`), à une échelle donnée de la course réelle (64 tâches × 9 conditions × 10 actions ×
≈ 222 jetons × 4 096 × 3 couches), avec les réglages de lecture de la configuration réelle (brouillon 2 : 200 planchers,
200 permutations, 2 000 tirages, 15 couples famille × couche). Mesures par étape : durée, pic de mémoire vive
(`resource.getrusage`), octets sur le disque, nombre et taille des morceaux du sous-ensemble. Étapes reprises par un
fichier d'état (chaque étape tient sous le délai d'une commande) ; aucune valeur d'aire ni d'état de jeu n'est imprimée.

    PYTHONPATH=src python scripts/epreuve_e0_t06_v2.py DOSSIER --echelle 1/64 [--etapes donnees,sous-ensemble,decisif,desc-c7,...]

Échelles : « 1/4 » (32 tâches, ≈ 111 jetons), « 1/16 » (16 tâches, ≈ 56 jetons), « 1/64 » (8 tâches, ≈ 28 jetons),
« 1/256 » (4 tâches, ≈ 14 jetons) : le nombre de tâches et la longueur des actions sont réduits chacun de la racine carrée
du facteur, le nombre de conditions, d'actions par tâche, la largeur, les couches et les réglages de lecture restent ceux de
la course.
"""
from __future__ import annotations

import argparse
import json
import resource
import shutil
import sys
import time
from pathlib import Path

import numpy as np

from controle_ia.manifeste import graines
from controle_ia.t06 import lanceur_v2 as la2
from controle_ia.t06.configuration import conditions_evaluation
from controle_ia.t06.lecture import cles_de_lecture

RACINE = Path(__file__).resolve().parents[1]
CONFIG_REELLE = RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-reel-v1-brouillon2.json"
ECHELLES = {"1": (64, 222), "1/4": (32, 111), "1/16": (16, 56), "1/64": (8, 28), "1/256": (4, 14)}
LARGEUR = 4096
ENTROPIE = 20261105


def pic_rss_go() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024 / 1e9


def taille_dossier(d: Path) -> int:
    return sum(f.stat().st_size for f in d.rglob("*") if f.is_file())


def config_de(echelle: str, couches=None, sonde_couche=None, couples: bool = True) -> dict:
    c = json.loads(CONFIG_REELLE.read_text(encoding="utf-8"))
    c["fils_test_croise"] = 4
    c["couples_descriptifs"] = couples
    if couches is not None:
        c["couches"] = list(couches)
        c["sonde"]["couche"] = int(sonde_couche)
    return c


def lignes_synthetiques(config: dict, n_taches: int, jetons_moyen: int, rng) -> list[dict]:
    conds = conditions_evaluation(config)
    T = int(config["T"])
    lignes = []
    for t in range(n_taches):
        for c in conds:
            for p in range(T):
                n = int(rng.integers(max(2, jetons_moyen // 2), jetons_moyen * 3 // 2 + 1))
                lignes.append({"cle": f"{c}__t{t:03d}__p{p}", "tache": f"t{t:03d}", "condition": c, "pas": p, "jetons_notes": n,
                               "cout": float(10 ** rng.uniform(1.0, 3.0)), "mention_etendue": bool(rng.random() < 0.05)})
    return lignes


def etape_donnees(etat: dict, dossier: Path, config: dict, n_taches: int, jetons_moyen: int) -> None:
    rng = np.random.default_rng(ENTROPIE)
    lignes = lignes_synthetiques(config, n_taches, jetons_moyen, rng)
    debut = time.perf_counter()
    act = la2.ActivationsDemi(dossier / "activations", config["couches"])
    for l in lignes:
        act.ecrire(l["cle"], {c: rng.standard_normal((l["jetons_notes"], LARGEUR)).astype(np.float32) for c in config["couches"]})
    jetons = sum(l["jetons_notes"] for l in lignes)
    etat["lignes"] = lignes
    etat["etapes"]["donnees"] = {"duree_s": round(time.perf_counter() - debut, 1), "actions": len(lignes), "jetons": jetons,
                                 "octets_disque": taille_dossier(dossier / "activations"), "pic_rss_go": round(pic_rss_go(), 3),
                                 "octets_par_couche": int(jetons * LARGEUR * 2)}


def etape_sous_ensemble(etat: dict, dossier: Path, config: dict) -> None:
    g = graines(cles_de_lecture(config), ENTROPIE)
    act = la2.ActivationsDemi.__new__(la2.ActivationsDemi)
    act.dossier, act.couches = dossier / "activations", [int(c) for c in config["couches"]]
    d = dossier / "sous-ensemble"
    d.mkdir(exist_ok=True)
    debut = time.perf_counter()
    r = la2.sous_ensemble_en_morceaux(etat["lignes"], act, config, g, d)
    etat["etapes"]["sous-ensemble"] = {"duree_s": round(time.perf_counter() - debut, 1), "morceaux": len(r["morceaux"]),
                                       "octets_morceaux": [m["octets"] for m in r["morceaux"]], "actions": r["actions"],
                                       "octets_total": sum(m["octets"] for m in r["morceaux"]), "pic_rss_go": round(pic_rss_go(), 3)}


def etape_croise(etat: dict, dossier: Path, config: dict, nom: str) -> None:
    g = graines(cles_de_lecture(config), ENTROPIE)
    act = la2.ActivationsDemi.__new__(la2.ActivationsDemi)
    act.dossier, act.couches = dossier / "activations", [int(c) for c in config["couches"]]
    import torch
    torch.set_num_threads(int(config["fils_test_croise"]))
    debut = time.perf_counter()
    r = la2.test_croise_v2(etat["lignes"], act, config, g)
    # aucune valeur d'aire ni d'état : seules les durées et les comptes sortent de l'épreuve
    etat["etapes"][nom] = {"duree_s": round(time.perf_counter() - debut, 1), "durees_s": r["durees_s"],
                           "jeux_descriptifs": len(r["jeux"].get("descriptifs") or {}), "pic_rss_go": round(pic_rss_go(), 3),
                           "couches": config["couches"], "sonde_couche": config["sonde"]["couche"]}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dossier")
    ap.add_argument("--echelle", default="1/64", choices=sorted(ECHELLES))
    ap.add_argument("--etapes", default=None, help="étapes à jouer, séparées par des virgules (défaut : toutes celles qui manquent)")
    a = ap.parse_args(argv)
    dossier = Path(a.dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin_etat = dossier / "etat-e0.json"
    etat = json.loads(chemin_etat.read_text(encoding="utf-8")) if chemin_etat.exists() else {"echelle": a.echelle, "etapes": {}, "lignes": None}
    if etat["echelle"] != a.echelle:
        print(f"état à l'échelle {etat['echelle']} ≠ {a.echelle} : dossier neuf exigé", file=sys.stderr)
        return 2
    n_taches, jetons_moyen = ECHELLES[a.echelle]
    base = config_de(a.echelle)
    couches = [int(c) for c in base["couches"]]
    ordre = ["donnees", "sous-ensemble", "decisif"] + [f"desc-c{c}" for c in couches]
    voulues = a.etapes.split(",") if a.etapes else ordre
    for nom in ordre:
        if nom not in voulues or nom in etat["etapes"]:
            continue
        t0 = time.perf_counter()
        print(f"E0 {a.echelle} : étape {nom} ({n_taches} tâches, ≈ {jetons_moyen} jetons par action, largeur {LARGEUR})", flush=True)
        if nom == "donnees":
            etape_donnees(etat, dossier, base, n_taches, jetons_moyen)
        elif nom == "sous-ensemble":
            etape_sous_ensemble(etat, dossier, base)
        elif nom == "decisif":
            etape_croise(etat, dossier, config_de(a.echelle, couples=False), nom)
        else:
            c = int(nom[len("desc-c"):])
            etape_croise(etat, dossier, config_de(a.echelle, couches=[c], sonde_couche=c, couples=True), nom)
        chemin_etat.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
        r = {k: v for k, v in etat["etapes"][nom].items() if k != "octets_morceaux"}
        print(f"E0 {a.echelle} : étape {nom} faite en {time.perf_counter() - t0:.1f} s : {json.dumps(r, ensure_ascii=False)}", flush=True)
    restantes = [n for n in ordre if n not in etat["etapes"]]
    print(f"E0 {a.echelle} : étapes restantes : {restantes or 'aucune'} ; disque du dossier {taille_dossier(dossier) / 1e9:.2f} Go ; "
          f"pic de mémoire vive {pic_rss_go():.2f} Go ; libre {shutil.disk_usage(str(dossier)).free / 1e9:.1f} Go")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
