"""Épreuve E0 du lanceur de T0.6 v3 (C-V3-4, 0 USD, processeur) : mesure de la durée des couples descriptifs d'une couche sur
les activations SYNTHÉTIQUES de l'épreuve E0 v2 (`scripts/epreuve_e0_t06_v2.py`, bruit gaussien, aucune donnée réelle), par
`lanceur_v3.test_croise_v3` sous le calcul de Mahalanobis choisi (paquet gelé ou produit matriciel v2), avec les réglages de
lecture de la configuration réelle brouillon 3. Seules des durées, des comptes et les comptes rendus des essais d'égalité
(écart relatif, jamais une aire ni un état) sortent de l'épreuve.

    PYTHONPATH=src python scripts/epreuve_e0_t06_v3.py DOSSIER --echelle 1/64 --calcul produit_matriciel_v2 [--couche 7]

Le dossier reçoit les activations (`donnees` de la v2, reprises si déjà écrites) et un fichier d'état `etat-e0-v3.json`.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import epreuve_e0_t06_v2 as e0  # noqa: E402

from controle_ia.manifeste import graines  # noqa: E402
from controle_ia.sondes.familles_v2 import CALCULS_MAHALANOBIS  # noqa: E402
from controle_ia.t06 import lanceur_v3 as la3  # noqa: E402
from controle_ia.t06.configuration_v3 import exiger_config_t06_v3  # noqa: E402
from controle_ia.t06.lecture import cles_de_lecture  # noqa: E402

CONFIG_REELLE_V3 = e0.RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-reel-v1-brouillon3.json"


def config_v3(couche: int, calcul: str) -> dict:
    c = json.loads(CONFIG_REELLE_V3.read_text(encoding="utf-8"))
    exiger_config_t06_v3(c)
    c["fils_test_croise"] = 4
    c["couples_descriptifs"] = True
    c["couches"] = [int(couche)]
    c["sonde"]["couche"] = int(couche)
    c["mahalanobis_calcul"] = calcul
    return c


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dossier")
    ap.add_argument("--echelle", default="1/64", choices=sorted(e0.ECHELLES))
    ap.add_argument("--calcul", default="produit_matriciel_v2", choices=CALCULS_MAHALANOBIS)
    ap.add_argument("--couche", type=int, default=7)
    a = ap.parse_args(argv)
    dossier = Path(a.dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin_etat = dossier / "etat-e0-v3.json"
    etat = json.loads(chemin_etat.read_text(encoding="utf-8")) if chemin_etat.exists() else {"echelle": a.echelle, "etapes": {}, "lignes": None}
    if etat["echelle"] != a.echelle:
        print(f"état à l'échelle {etat['echelle']} ≠ {a.echelle} : dossier neuf exigé", file=sys.stderr)
        return 2
    n_taches, jetons_moyen = e0.ECHELLES[a.echelle]
    base = config_v3(a.couche, a.calcul)
    if "donnees" not in etat["etapes"]:
        t0 = time.perf_counter()
        print(f"E0 v3 {a.echelle} : étape donnees ({n_taches} tâches, ≈ {jetons_moyen} jetons par action, largeur {e0.LARGEUR}, couche {a.couche})", flush=True)
        e0.etape_donnees(etat, dossier, base, n_taches, jetons_moyen)
        chemin_etat.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"E0 v3 : données écrites en {time.perf_counter() - t0:.1f} s : {json.dumps({k: v for k, v in etat['etapes']['donnees'].items()}, ensure_ascii=False)}", flush=True)
    nom = f"desc-c{a.couche}-{a.calcul}"
    if nom in etat["etapes"]:
        print(f"E0 v3 : étape {nom} déjà faite : {json.dumps(etat['etapes'][nom], ensure_ascii=False)}")
        return 0
    g = graines(cles_de_lecture(base), e0.ENTROPIE)
    act = la3.ActivationsDemi.__new__(la3.ActivationsDemi)
    act.dossier, act.couches = dossier / "activations", [int(c) for c in base["couches"]]
    import torch
    torch.set_num_threads(int(base["fils_test_croise"]))
    print(f"E0 v3 {a.echelle} : étape {nom}", flush=True)
    debut = time.perf_counter()
    r = la3.test_croise_v3(etat["lignes"], act, base, g)
    # aucune valeur d'aire ni d'état : durées, comptes, écarts des essais d'égalité
    verifs = r["verifications_mahalanobis"]
    etat["etapes"][nom] = {"duree_s": round(time.perf_counter() - debut, 1), "durees_s": r["durees_s"], "calcul": r["mahalanobis_calcul"],
                           "jeux_descriptifs": len(r["jeux"].get("descriptifs") or {}), "pic_rss_go": round(e0.pic_rss_go(), 3),
                           "jetons": etat["etapes"]["donnees"]["jetons"], "essais_egalite": len(verifs),
                           "essais_egaux": int(sum(1 for v in verifs.values() if v["egal"])),
                           "ecart_relatif_max": max([v["ecart_relatif_max"] for v in verifs.values()] or [0.0]),
                           "couples_en_echec": sorted(k for k, v in r["jeux"]["descriptifs"].items() if "echec" in v)}
    chemin_etat.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"E0 v3 {a.echelle} : étape {nom} faite : {json.dumps(etat['etapes'][nom], ensure_ascii=False)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
