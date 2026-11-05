"""Rejoue, avec le générateur et les graines de `simuler_atteignabilite_v3.py`, les quatre analyses « H1 (1,0 et 0,2) ;
tau 0.8 » (graines 3066 à 3072) et imprime les grandeurs du sens b→a : quelle lecture « positif non confirmé » ?"""
import importlib.util, json, pathlib, sys, tempfile
SC = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v3/scripts")
spec = importlib.util.spec_from_file_location("sim", SC / "simuler_atteignabilite_v3.py")
SIM = importlib.util.module_from_spec(spec); spec.loader.exec_module(SIM)
stim = SC.parent / "stimuli" / "echelle-v2.json"
st = json.loads(stim.read_text(encoding="utf-8"))["stimuli"]
# ordre de la simulation : H0 (3 tau x 4), pas de fuite (3 x 4), H1 tau 0.15 (4), 0.4 (4), 0.8 (4)
graines = [3000 + 2 * k for k in range(1, 70)]
idx0 = 12 + 12 + 4 + 4
with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    for g in graines[idx0:idx0 + 4]:
        b = tmp / str(g)
        SIM.fabriquer(b / "p", stim, st, 1.0, g, 0.8)
        SIM.fabriquer(b / "g", stim, st, 0.2, g + 1, 0.8)
        SIM.AN.principal([str(stim), str(b / "p"), str(b / "g"), str(g), str(b / "s"), "--repetition"])
        r = json.loads((b / "s" / "analyse-echelle-v3.json").read_text(encoding="utf-8"))
        print(g, r["lecture"], {s: {"dl_ic": [round(x, 3) for x in r["delta_lambda_ic"][s]],
                                   "lp_ic": [round(x, 3) for x in r["petit"][s]["lambda_ic"]],
                                   "lg_ic": [round(x, 3) for x in r["grand"][s]["lambda_ic"]],
                                   "cert": [round(r[m][s]["A_ctx_fixe_ic"][0], 3) for m in ("petit", "grand")]}
                               for s in ("ab", "ba")}, flush=True)
