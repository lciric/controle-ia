"""Refait quelques analyses du banc de cl7 : générateur `banc_cl7.py` versé (importé tel quel), analyse v8 du commit."""
import importlib.util, json, pathlib, sys, tempfile
V8 = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8")
s = importlib.util.spec_from_file_location("banc_cl7", "/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v8/contre-lecture-cl7/scripts/banc_cl7.py")
BANC = importlib.util.module_from_spec(s); s.loader.exec_module(BANC)
s = importlib.util.spec_from_file_location("an8", V8 / "scripts" / "analyser_echelle_v8.py")
AN = importlib.util.module_from_spec(s); s.loader.exec_module(AN)
AN.N_BOOT = 300
stim = V8 / "stimuli" / "echelle-v2.json"
st = json.loads(stim.read_text(encoding="utf-8"))["stimuli"]
rejeu = {(x["scenario"], x["graine"]): x for x in map(json.loads, open("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v8/rejeu-banc-cl7/rejeu-banc-cl7-v8-principal.jsonl", encoding="utf-8")) if "scenario" in x}
for nom, g in (("D_H0_07_k133_inv_8b_70a_s1.2", 41306), ("B_H0_d020_pos_8a_70b_s0.5", 40006), ("E_H0_09_k08", 43202)):
    a8, a70, o8, o70 = BANC.SCENARIOS[nom]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        BANC.fabriquer(base / "p", st, a8, g, **o8); BANC.fabriquer(base / "g", st, a70, g + 1, **o70)
        assert AN.principal([str(stim), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"]) == 0
        r = json.loads((base / "s" / "analyse-echelle-v8.json").read_text(encoding="utf-8"))
    x = rejeu[(nom, g)]
    mien = {"lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"), "reserves": r["reserves"],
            "ecart_sens": {k: round(v, 3) for k, v in r["ecart_sens"].items()},
            "rapport_Ec": {k: round(v, 3) for k, v in r["rapport_Ec"].items()}}
    print(nom, g, "identique au rejeu versé" if all(mien[k] == x[k] for k in mien) else ("ÉCART", mien, {k: x[k] for k in mien}), mien["lecture"], [y[:30] for y in mien["reserves"]], mien["rapport_Ec"])
