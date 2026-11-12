"""CL8 : S12, fenêtre makedirs → manifeste de départ. Usage : python3 -B scenario_fenetre.py ARBRE DOSSIER"""
import json, os, subprocess, sys
A, D = sys.argv[1], sys.argv[2]
OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
os.makedirs(D, exist_ok=False)
sys.argv = [sys.argv[0], A, os.path.dirname(D), "_inutile"]
# reprise des préparatifs du scénario S1 (pièces, témoins, liste blanche) sans jouer de scénario
import importlib.util
src = open(os.path.join(OUT, "scenarios_cl8.py"), encoding="utf-8").read().split("# -----")[0]
src = src.replace('D = os.path.join(BASE, NOM)\nos.makedirs(D, exist_ok=False)', 'D = ' + repr(D))
g = {"__name__": "prep", "__file__": os.path.join(OUT, "scenarios_cl8.py")}
exec(compile(src, "scenarios_cl8_prep", "exec"), g)
prep = g["preparer"]()
cmd = g["config_argon"](cout=0.01)
args = g["args_course"](prep, "course", cmd)
rap = {}
for i, fen in enumerate(("1", "0")):
    env = {k: v for k, v in os.environ.items() if k in ("PATH", "HOME", "LANG")}
    env["CL8_FENETRE"] = fen
    p = subprocess.run([sys.executable, "-B", os.path.join(OUT, "lanceur_fenetre.py"), A, "--", *args], capture_output=True,
                       env=env, timeout=300)
    rap[f"essai{i + 1}"] = {"code": p.returncode, "erreur": p.stderr.decode()[-700:]}
ctl = os.path.join(D, "course-controle")
rap["controle"] = sorted(os.listdir(ctl))
rap["sortie_existe"] = os.path.exists(os.path.join(D, "course"))
rap["sortie_contenu"] = sorted(os.listdir(os.path.join(D, "course"))) if rap["sortie_existe"] else None
t = os.path.join(ctl, "tentative-1.json")
if os.path.exists(t):
    r = json.load(open(t))["reglages"]
    rap["tentative-1"] = {k: r.get(k) for k in ("cout_claude_usd", "cout_externe_usd", "relancable", "motifs_relance", "erreur")}
json.dump(rap, open(os.path.join(D, "rapport.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps(rap, ensure_ascii=False, indent=1))
