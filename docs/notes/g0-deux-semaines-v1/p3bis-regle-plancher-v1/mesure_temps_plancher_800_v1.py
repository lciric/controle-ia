"""Mesure du temps ajouté par les 800 directions de plancher de P3-bis (règle (a'), R-2320 ; consigne
`consigne-code-p3bis-regle-a-v1.md`, `39300056…`, mandat 3), sur processeur, sans aucune donnée réelle (tableaux tirés au
hasard aux dimensions de P3 : largeur 4 096, actions de 223 jetons en moyenne, 400 au plus).

    OPENBLAS_NUM_THREADS=N PYTHONPATH=<arbre>/src python -I mesure_temps_plancher_800_v1.py <arbre> SORTIE.json

Postes mesurés (chacun : 200 contre 800 directions par plancher, deux planchers, couche 15) :
1. tirage des directions (`plancher_apparie` : `w = L @ z`, l'une après l'autre) : 600 tirages de plus par plancher ;
2. notation en ligne d'une action (`premier_test_ia.notation.Notation.noter`, bloc linéaire de la couche 15 : 6 sondes
   linéaires et 2 × 200 ou 2 × 800 directions), sur processeur (torch, double précision) — le run la fait sur la carte ;
3. garde d'identité du run (`notation.exiger_identite`, toutes sondes, boucle du harnais `score_action`, processeur), une
   action par lot, 30 lots ;
4. lecture (session, processeur) : lecture de P3 (`lecture.lire`, inchangée) et lecture complémentaire v2
   (`lecture_p3bis_v2.lire`) d'un run jouet à la taille de P3-bis (60 tâches, 4 emplacements, 10 actions : 2 400 actions),
   à 200 et à 800 directions (la v2 exige 800 : à 200, seule la lecture de P3 est mesurée).
Les durées sont des médianes de répétitions (nombre écrit). Aucune garde n'est contournée."""
import importlib.util
import json
import os
import platform
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

ARBRE = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ARBRE / "src"))
import torch  # noqa: E402

from controle_ia.manifeste import graines  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402
from controle_ia.premier_test_ia import lecture_p3bis_v1 as v1  # noqa: E402
from controle_ia.premier_test_ia import lecture_p3bis_v2 as l2  # noqa: E402
from controle_ia.premier_test_ia.notation import Notation, exiger_identite  # noqa: E402
from controle_ia.sondes.familles import SondeLineaireJetons  # noqa: E402

D, COUCHE, L_MOY, L_MAX = 4096, 15, 223, 400
ACTIONS, LOTS = 2400, 30


def mediane(f, n):
    t = []
    for _ in range(n):
        t0 = time.perf_counter()
        f()
        t.append(time.perf_counter() - t0)
    return float(np.median(t)), n


def sondes(n_plancher, rng):
    s = [SondeLineaireJetons(f"tromperie-{x}-c15", COUCHE, "max", rng.normal(size=D), 0.1) for x in ("difference_moyennes", "lineaire")]
    s += [SondeLineaireJetons(f"enjeux-{x}-c15", COUCHE, "max", rng.normal(size=D), 0.1) for x in ("difference_moyennes", "lineaire")]
    s += [SondeLineaireJetons(f"{c}-attention-c15", COUCHE, "attention", rng.normal(size=D), 0.0, rng.normal(size=D), "attention")
          for c in ("tromperie", "enjeux")]
    for p in ("tromperie-difference_moyennes-c15", "enjeux-lineaire-c15"):
        s += [SondeLineaireJetons(f"{p}-plancher-plancher-{k}", COUCHE, "max", rng.normal(size=D), 0.0, None, "plancher")
              for k in range(n_plancher)]
    return s


def main():
    sortie = {"processeur": platform.processor() or platform.machine(), "coeurs": os.cpu_count(),
              "fils_openblas": os.environ.get("OPENBLAS_NUM_THREADS"), "fils_torch": torch.get_num_threads(),
              "numpy": np.__version__, "torch": torch.__version__}
    rng = np.random.default_rng(20261111)
    # 1. tirage : 600 directions de plus par plancher (L triangulaire inférieure, largeur 4 096)
    Lc = np.tril(rng.normal(size=(D, D))) / 64.0
    g = np.random.default_rng(1)
    t, n = mediane(lambda: [Lc @ g.standard_normal(D) for _ in range(100)], 3)
    sortie["tirage"] = {"par_direction_s": t / 100, "repetitions": n,
                        "ajoute_deux_planchers_s": t / 100 * 1200}
    # 2 et 3. notation et garde d'identité, couche 15
    for L in (L_MOY, L_MAX):
        A = rng.normal(size=(L, D)).astype(np.float32)
        res = {}
        for n_pl in (200, 800):
            s = sondes(n_pl, np.random.default_rng(5))
            nt = Notation(s, "cpu")
            tn, rn = mediane(lambda: nt.noter({COUCHE: A}), 5)
            sc = nt.noter({COUCHE: A})
            tg, rg = mediane(lambda: exiger_identite(nt, {COUCHE: A}, sc, 1e-6), 2)
            res[n_pl] = {"sondes": len(s), "notation_s": tn, "garde_s": tg, "repetitions": [rn, rg]}
        sortie[f"couche15_L{L}"] = {
            **{str(k): v for k, v in res.items()},
            "notation_ajoutee_par_action_s": res[800]["notation_s"] - res[200]["notation_s"],
            "notation_ajoutee_2400_actions_processeur_s": (res[800]["notation_s"] - res[200]["notation_s"]) * ACTIONS,
            "garde_ajoutee_par_lot_s": res[800]["garde_s"] - res[200]["garde_s"],
            "garde_ajoutee_30_lots_s": (res[800]["garde_s"] - res[200]["garde_s"]) * LOTS,
            "flops_ajoutes_par_action": 2 * 2 * L * D * 1200}
    # 4. lectures d'un run jouet à la taille de P3-bis
    spec = importlib.util.spec_from_file_location("ev3", ARBRE / "scripts" / "essai_fermeture_p3bis_v3.py")
    ev3 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ev3)
    ev3.N_TACHES, ev3.T_PAS = 60, 10
    lectures = {}
    with tempfile.TemporaryDirectory(dir=sys.argv[3] if len(sys.argv) > 3 else None) as tmp:
        for n_pl in (200, 800):
            ev3.N_PLANCHER = n_pl
            d = ev3.depot_vide(Path(tmp) / f"d{n_pl}")
            run = "20261120-120000-jouet"
            ev3.fabriquer_run(d, run, "vu", ev3.graine("vu"), config={"mode": "jouet", "max_nouveaux": 64})
            source = lp.charger_source(d, run)
            pr = [source["sondes-figees"]["principales"][c] for c in ("tromperie", "enjeux")]
            t0 = time.perf_counter()
            l3 = json.loads(json.dumps(lp.lire(source, graines(lp.cles_de_lecture(pr), 4242))))
            t_p3 = time.perf_counter() - t0
            r = {"actions": int(source["tables"]["scores"].shape[0]), "colonnes": int(source["tables"]["scores"].shape[1]),
                 "lecture_de_P3_s": t_p3}
            if n_pl == 800:
                textes = v1.charger_textes(d, source)
                t0 = time.perf_counter()
                s = l2.lire(source, l3, textes, 64, graines(list(l2.CLES_DE_LECTURE), 4242))
                r["lecture_complementaire_v2_s"] = time.perf_counter() - t0
                r["issue"] = s["issue_mecanique"]
                m = (source["tables"]["condition"] == "saboteur") | (source["tables"]["condition"] == "temoin")
                t0 = time.perf_counter()
                noms = source["tables"]["noms_sondes"].tolist()
                j = noms.index(pr[0])
                pl = [noms.index(f"{pr[0]}-plancher-{k}") for k in range(800)]
                S = source["tables"]["scores"]
                l2.lire_regle_a(S[m, j], np.ascontiguousarray(S[np.ix_(m, pl)].T),
                                (source["tables"]["condition"][m] == "saboteur").astype(np.int64),
                                source["tables"]["tache"][m], 7, 0.95)
                r["regle_a_jeu_decisif_s"] = time.perf_counter() - t0
            lectures[str(n_pl)] = r
    sortie["lectures"] = lectures
    sortie["lectures"]["lecture_de_P3_ajoutee_s"] = lectures["800"]["lecture_de_P3_s"] - lectures["200"]["lecture_de_P3_s"]
    # tailles ajoutées aux fichiers du run (8 octets par double)
    sortie["tailles_ajoutees_octets"] = {
        "sondes_figees_et_legeres_w": 2 * 1200 * D * 8, "scores_p3_npz": ACTIONS * 1200 * 8,
        "total_second_paquet": 2 * 1200 * D * 8 + ACTIONS * 1200 * 8}
    Path(sys.argv[2]).write_text(json.dumps(sortie, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(sortie, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
