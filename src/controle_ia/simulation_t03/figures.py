"""Figures descriptives de T0.3, tirées des résultats scellés d'un run (aucun verdict ici).

    PYTHONPATH=src python -m controle_ia.simulation_t03.figures --run-id <run_id>

Chaque figure est écrite dans diag/<run_id>/figures/ et scellée (R6) ; on n'écrase jamais (R12).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from ..gardes import GardeArret  # noqa: E402
from ..manifeste import verifier_resultat  # noqa: E402
from ..scellement import sceller  # noqa: E402
from . import calibrage as cal  # noqa: E402


def charger(racine: Path, run_id: str) -> dict:
    d = racine / "diag" / run_id
    sortie = {}
    for f in sorted(d.glob("*.json")):
        sortie[f.stem] = verifier_resultat(racine, f)["resultat"]
    if not sortie:
        raise GardeArret(f"aucun résultat dans {d}")
    return sortie


def _enregistrer(fig, chemin: Path) -> Path:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    fig.savefig(chemin, dpi=130, bbox_inches="tight", metadata={"Software": None, "CreationDate": None})
    plt.close(fig)
    sceller(chemin)
    return chemin


def figures(racine: str | Path, run_id: str, alpha: float = 0.05) -> list[str]:
    racine = Path(racine)
    r = charger(racine, run_id)
    dossier = racine / "diag" / run_id / "figures"
    dossier.mkdir(exist_ok=True)
    faites = []

    if "bloc-P1a" in r and "bloc-P2" in r:              # F1 : somme plate en m, max qui s'effondre
        fig, ax = plt.subplots(figsize=(6.5, 4))
        g1 = [g for g in r["bloc-P1a"]["groupes"] if g["N"] == 1]
        for k, g in enumerate(sorted(g1, key=lambda g: g["B"])):
            cel = sorted([c for c in r["bloc-P2"]["cellules"] if c["B"] == g["B"]], key=lambda c: c["m"])
            couleur = f"C{k}"
            ax.axhline(g["alarmes_ref_somme"] / g["R"], color=couleur, ls="-", lw=1.5,
                       label=f"somme terminale, B = {g['B']}")
            if not cel:
                continue
            ms = np.array([c["m"] for c in cel])
            ax.plot(ms, [c["alarmes_max"] / c["R"] for c in cel], "o", color=couleur, label=f"max par action, B = {g['B']}")
            mm = np.unique(np.geomspace(1, ms.max(), 60).astype(int))
            ax.plot(mm, [cal.puissance_max(alpha, cel[0]["n0"], g["B"], int(m)) for m in mm], ":", color=couleur)
        ax.axhline(alpha, color="grey", lw=0.8)
        ax.set_xscale("log")
        ax.set_xlabel("nombre d'actions sabotées m (budget B fixé)")
        ax.set_ylabel("puissance")
        ax.set_title("L1 et L2 — n₀ = 200 (pointillés : forme close du max)")
        ax.legend(fontsize=7, ncol=2)
        faites.append(str(_enregistrer(fig, dossier / "F1-L1-L2-fragmentation.png")))

    if "bloc-P1b" in r:                                  # F2 : dépendance en n₀
        fig, ax = plt.subplots(figsize=(6.5, 4))
        cel = r["bloc-P1b"]["cellules"]
        for k, Bv in enumerate(sorted({c["B"] for c in cel})):
            cc = sorted([c for c in cel if c["B"] == Bv], key=lambda c: (c["n0"], c["N"]))
            ax.plot([c["n0"] for c in cc], [c["alarmes_somme"] / c["R"] for c in cc], "o", color=f"C{k}",
                    label=f"B = {Bv}")
            nn = np.geomspace(min(c["n0"] for c in cc), max(c["n0"] for c in cc), 80)
            ax.plot(nn, [cal.puissance_somme(alpha, n, Bv) for n in nn], "-", color=f"C{k}", lw=1)
        ax.set_xscale("log")
        ax.set_xlabel("horizon n₀ = N·T")
        ax.set_ylabel("puissance de la somme terminale")
        ax.set_title("L1 — à B fixé, la puissance décroît avec n₀ (traits : Φ̄(z_α − B/√n₀))")
        ax.legend(fontsize=8)
        faites.append(str(_enregistrer(fig, dossier / "F2-L1-horizon.png")))

    if "bloc-P3" in r:                                   # F3 : calendrier
        groupes = [g for g in r["bloc-P3"]["groupes"] if g["N"] == 1]
        fig, axes = plt.subplots(1, len(groupes), figsize=(4 * len(groupes), 3.6), sharey=True)
        for ax, g in zip(np.atleast_1d(axes), groupes):
            ms = sorted({c["m"] for c in g["cellules"]})
            cal_ = ["debut", "uniforme", "aleatoire", "fin"]
            for j, s in enumerate(cal_):
                ax.bar(np.arange(len(ms)) + 0.2 * j, [next(c["alarmes"] for c in g["cellules"]
                                                         if c["m"] == m and c["calendrier"] == s) / g["R"] for m in ms],
                       width=0.2, label=s)
            ax.axhline(g["alarmes_terminal"] / g["R"], color="k", ls="--", lw=1, label="borne terminale")
            ax.axhline(cal.puissance_somme(alpha, g["n0"], g["B"]), color="grey", ls=":", lw=1, label="test z")
            ax.set_xticks(np.arange(len(ms)) + 0.3, [f"m = {m}" for m in ms])
            ax.set_title(f"B = {g['B']}")
        np.atleast_1d(axes)[0].set_ylabel("alarme d'ici n₀ (processus e unilatéral)")
        np.atleast_1d(axes)[-1].legend(fontsize=7)
        fig.suptitle("L3 — lecture toujours valide selon le calendrier (n₀ = 200)")
        faites.append(str(_enregistrer(fig, dossier / "F3-L3-calendrier.png")))

    if "bloc-P34" in r:                                  # F4 : détection à temps
        cel = r["bloc-P34"]["cellules"]
        noms = list(cel[0]["comptes"])
        fig, ax = plt.subplots(figsize=(7, 3.8))
        for j, a in enumerate(noms):
            ax.bar(np.arange(len(cel)) + 0.13 * j, [c["comptes"][a]["a_temps"] / c["R"] for c in cel], width=0.13, label=a)
        ax.set_xticks(np.arange(len(cel)) + 0.35, [f"B={c['B']}, m={c['m']}" for c in cel], fontsize=7)
        ax.set_ylabel("alarme avant la dernière action sabotée")
        ax.set_title("L3 (d) — sabotage reporté en fin d'horizon")
        ax.legend(fontsize=7)
        faites.append(str(_enregistrer(fig, dossier / "F4-L3d-detection-a-temps.png")))

    if "bloc-P6" in r and "calibrage" in r:              # F5 : classe K, copule AR(1)
        cel = [c for c in r["bloc-P6"]["cellules"] if c["role"] == "copule_temps" and c["loi"].get("marginale", "gauss") == "gauss"]
        if cel:
            cel = sorted(cel, key=lambda c: c["loi"]["phi"])
            cfg = cel[0]["cfg"]
            c0 = r["calibrage"]["configs"][cfg]
            fig, ax = plt.subplots(figsize=(6.5, 4))
            for k, a in enumerate(("somme", "max", "e_unilat_ville", "page", "autocorr_abs")):
                phis = [0.0] + [c["loi"]["phi"] for c in cel]
                ps = [c0["alarmes_p0"][a] / c0["R0"]] + [c["alarmes"][a] / c["R"] for c in cel]
                o = np.argsort(phis)
                ax.plot(np.array(phis)[o], np.array(ps)[o], "o-", color=f"C{k}", label=a)
            ax.axhline(alpha, color="grey", lw=0.8)
            ax.set_xlabel("φ (copule gaussienne AR(1), marginale N(0, 1) préservée)")
            ax.set_ylabel("taux de rejet")
            ax.set_title("Classe K — φ = 0 : taux sous P₀")
            ax.legend(fontsize=8)
            faites.append(str(_enregistrer(fig, dossier / "F5-classe-K-copule.png")))

    if "bloc-P8" in r:                                   # F6 : validité hors hypothèses
        reg = r["bloc-P8"]["reglages"]
        fig, ax = plt.subplots(figsize=(8, 4))
        x = np.arange(len(reg))
        ax.bar(x - 0.2, [s["alarmes"]["e_unilat_ville"] / s["R"] for s in reg], width=0.4, label="Ville (1/α)")
        ax.bar(x + 0.2, [np.mean(s["conforme"]["alarmes_par_tirage"]["e_unilat"]) / s["conforme"]["n_test"] for s in reg],
               width=0.4, label="conforme (épisodes entiers)")
        ax.axhline(alpha, color="k", lw=0.8)
        ax.set_xticks(x, [s["nom"] for s in reg], rotation=60, ha="right", fontsize=7)
        ax.set_ylabel("taux de fausses alarmes")
        ax.set_title("Règle toujours valide hors hypothèses")
        ax.legend(fontsize=8)
        faites.append(str(_enregistrer(fig, dossier / "F6-validite-hors-hypotheses.png")))
    return faites


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--racine", default=".")
    a.add_argument("--run-id", required=True)
    a.add_argument("--alpha", type=float, default=0.05)
    args = a.parse_args(argv)
    print(json.dumps(figures(args.racine, args.run_id, args.alpha), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
