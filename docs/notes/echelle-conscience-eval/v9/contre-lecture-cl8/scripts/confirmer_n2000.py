"""Confirme une analyse du banc à composante commune avec 2 000 tirages (taille du bootstrap décisif)."""
import importlib.util, json, pathlib, sys
s = importlib.util.spec_from_file_location("bz", "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v9/scripts/banc_cl8_commun.py")
BZ = importlib.util.module_from_spec(s); s.loader.exec_module(BZ)
nom, g = sys.argv[1], int(sys.argv[2])
orig = BZ.AN.N_BOOT
def un(t):
    BZ.AN.N_BOOT = 2000
    return BZ.un.__wrapped__(t) if hasattr(BZ.un, "__wrapped__") else None
# un() fixe N_BOOT à 300 : on le remplace localement
import types
src = BZ.un.__code__
def un2000(t):
    nom, g = t
    a8, a70, o8, o70, tau = BZ.SC[nom]
    import tempfile
    st = json.loads(BZ.STIM.read_text(encoding="utf-8"))["stimuli"]
    BZ.AN.N_BOOT = 2000
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        BZ.fabriquer(base / "p", BZ.STIM, st, a8, g, tau, **o8)
        BZ.fabriquer(base / "g", BZ.STIM, st, a70, g + 1, tau, **o70)
        assert BZ.AN.principal([str(BZ.STIM), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"]) == 0
        r = json.loads((base / "s" / "analyse-echelle-v8.json").read_text(encoding="utf-8"))
    return {"scenario": nom, "graine": g, "n_boot": r["n_boot"], "lecture": r["lecture"], "reserves": r["reserves"],
            "e": r["ecart_sens"], "e_ic": r["ecart_sens_ic"], "q": r["rapport_Ec"], "q_ic": r["rapport_Ec_ic"],
            "dl": r["delta_lambda_ic"], "spec": r["specificite_ic"],
            "lambda": {s: [r[m][s]["lambda"] for m in ("petit", "grand")] for s in ("ab", "ba")},
            "lambda_ic": {s: [r[m][s]["lambda_ic"] for m in ("petit", "grand")] for s in ("ab", "ba")},
            "coherence": r["coherence_des_sens"]}
print(json.dumps(un2000((nom, g)), ensure_ascii=False))
