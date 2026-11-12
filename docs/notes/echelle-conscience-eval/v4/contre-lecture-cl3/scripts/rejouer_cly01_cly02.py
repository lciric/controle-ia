"""Rejoue CLY-01 et CLY-02 de cl2 sur les MÊMES activations synthétiques, analysées par `analyser_echelle_v2.py` (commit
495b8bd, sous echelle-v2/) puis par `analyser_echelle_v3.py` (c08a5b2), toutes deux TELLES QUELLES, mode --repetition,
300 tirages. Générateur : `banc_v4.fabriquer` (repris du test v3).
  CLY-01 : signature du jeu a au petit (2,0), aucun concept, tau 0,4 ;
  CLY-02 : fuite purement spécifique (1,0 ; 0,1), forces de paires inégales (kappa 0,5), tau 0,15.
Usage : python -I -B rejouer_cly01_cly02.py CAS GRAINE_DEPART N SORTIE_JSONL"""
import importlib.util
import json
import pathlib
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import banc_v4  # noqa: E402

WT = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1")


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.N_BOOT = 300
    return m


AN2 = charger(WT / "echelle-v2/scripts/analyser_echelle_v2.py", "an2")
AN3 = banc_v4.AN
CAS = {"CLY-01": (0.0, 0.0, {"signature": 2.0, "tau": 0.4}, {"tau": 0.4}),
       "CLY-02": (1.0, 0.1, {"kappa": 0.5, "tau": 0.15}, {"kappa": 0.5, "tau": 0.15})}


def principal(argv):
    cas, g0, n, sortie = argv[0], int(argv[1]), int(argv[2]), pathlib.Path(argv[3])
    a8, a70, o8, o70 = CAS[cas]
    st = json.loads(banc_v4.STIMULI.read_text(encoding="utf-8"))["stimuli"]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        for k in range(n):
            g = g0 + 2 * k
            b = tmp / str(g)
            banc_v4.fabriquer(b / "p", st, a8, g, **o8)
            banc_v4.fabriquer(b / "g", st, a70, g + 1, **o70)
            ligne = {"cas": cas, "graine": g}
            for nom, AN, fich in (("v2", AN2, "analyse-echelle-v2.json"), ("v3", AN3, "analyse-echelle-v3.json")):
                code = AN.principal([str(banc_v4.STIMULI), str(b / "p"), str(b / "g"), str(g), str(b / f"s{nom}"),
                                     "--repetition"])
                if code != 0:
                    ligne[nom] = {"code": code}
                    continue
                r = json.loads((b / f"s{nom}" / fich).read_text(encoding="utf-8"))
                lec = r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")")
                if nom == "v2":
                    ligne[nom] = {"lecture": lec, "reserves": len(r["reserves"]),
                                  "lambda_petit": round(r["petit"]["lambda"], 3), "nu_petit": round(r["petit"]["nu"], 3),
                                  "dl_ic": [round(x, 3) for x in r["delta_lambda_ic"]],
                                  "spec_ic": [round(x, 3) for x in r["specificite_ic"]]}
                else:
                    ligne[nom] = {"lecture": lec, "reserves": len(r["reserves"]),
                                  "lambda_ab_petit": round(r["petit"]["ab"]["lambda"], 3),
                                  "lambda_ba_petit": round(r["petit"]["ba"]["lambda"], 3),
                                  "nu_ab_petit": round(r["petit"]["ab"]["nu"], 3),
                                  "nu_ba_petit": round(r["petit"]["ba"]["nu"], 3),
                                  "dl_ab_ic": [round(x, 3) for x in r["delta_lambda_ic"]["ab"]],
                                  "dl_ba_ic": [round(x, 3) for x in r["delta_lambda_ic"]["ba"]],
                                  "spec_ab_ic": [round(x, 3) for x in r["specificite_ic"]["ab"]]}
            with open(sortie, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
            print(json.dumps(ligne, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
