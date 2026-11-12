"""CL9 : le classement de repli (« sans juge externe ») qui échoue après une tentative du bras non relançable — l'échec
est-il dit (sortie, fichier scellé) ou perdu ? Usage : python3 -B sonde_repli_silencieux.py ARBRE DOSSIER"""
import contextlib, importlib.util, io, json, os, subprocess, sys
A, D = sys.argv[1], sys.argv[2]
OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(D, exist_ok=False)
sys.argv = [sys.argv[0], A, os.path.dirname(D), "_inutile"]
src = open(os.path.join(OUT, "scenarios_cl9.py"), encoding="utf-8").read().split("# -----")[0]
src = src.replace('D = os.path.join(BASE, NOM)\nos.makedirs(D, exist_ok=False)', 'D = ' + repr(D))
g = {"__name__": "prep", "__file__": os.path.join(OUT, "scenarios_cl9.py")}
exec(compile(src, "scenarios_cl9_prep", "exec"), g)
prep = g["preparer"]()
cmd = g["config_argon"](cout=0.01)
code, out, err = g["lancer"](g["args_course"](prep, "course", cmd))
rap = {"course": code}
s = os.path.join(D, "course")
att = g["attester_bras"](s)
spec = importlib.util.spec_from_file_location("lanceur", os.path.join(A, "demonstrations", "ideation_v1.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
orig = L.idn._classer
etat = {"casser": False}
def _classer(*a, **k):
    if etat["casser"]:
        raise RuntimeError("panne simulée du classement de repli (disque plein, par exemple)")
    return orig(*a, **k)
L.idn._classer = _classer
argv = [s, "--bras-rapporte-differe", "--juge-externe", "argon=gemini-argon", "--attestation-lecture-humaine", att,
        "--commande-externe", "/chemin/qui/n/existe/pas"]
for n in (1, 2, 3):
    etat["casser"] = n == 3
    e_ = io.StringIO()
    with contextlib.redirect_stderr(e_):
        c = L.principal(argv)
    rap[f"bras-{n}"] = {"code": c, "stderr": e_.getvalue()[-700:]}
rap["fichiers"] = sorted(f for f in os.listdir(s) if f.startswith(("bras", "manifeste-bras", "classement")))
trouve = []
for r, _, fs in os.walk(s):
    for f in fs:
        p = os.path.join(r, f)
        try:
            if "classement_sans_bras_impossible" in open(p, encoding="utf-8").read():
                trouve.append(os.path.relpath(p, s))
        except (UnicodeDecodeError, OSError):
            pass
rap["fichiers_qui_disent_l_echec_du_repli"] = trouve
rap["stderr_3_dit_l_echec"] = "panne simulée" in rap["bras-3"]["stderr"] or "impossible" in rap["bras-3"]["stderr"]
json.dump(rap, open(os.path.join(D, "rapport.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps(rap, ensure_ascii=False, indent=1))
