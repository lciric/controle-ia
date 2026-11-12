import importlib.util, json, os, shutil, subprocess, sys
from pathlib import Path
BAC = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("b", BAC / "banc" / "banc_cl_v2.py")
src = (BAC / "banc" / "banc_cl_v2.py").read_text(encoding="utf-8")
ns = {}
exec(src.split("def jouer")[0].replace("BAC = Path(sys.argv[1]); ", ""), {"Path": Path, "sys": sys, "BAC": BAC, **{k: __import__(k) for k in ("json", "os", "shutil", "subprocess", "time")}}, ns)
for mid in sys.argv[2:]:
    f, a, b = ns["MUT"][mid]
    copie = BAC / "banc" / f"sondage-{mid}"
    copie.mkdir(); shutil.copytree(BAC / "arbre" / "src", copie / "src"); shutil.copytree(BAC / "essais-cl", copie / "essais", ignore=shutil.ignore_patterns("__pycache__"))
    p = copie / f; t = p.read_text(encoding="utf-8"); assert t.count(a) == 1; p.write_text(t.replace(a, b), encoding="utf-8")
    trace = BAC / "banc" / f"trace-sondage-{mid}.txt"
    r = subprocess.run(["/home/user/controle-ia-travail/.venv/bin/python", "-m", "pytest", "-q", "-o", "pythonpath=", "-p", "trace_import_accb6_v2", "-p", "no:cacheprovider",
                        "--rootdir", str(copie / "essais"), "-c", "/dev/null", f"--basetemp={copie}/bt", "-o", "tmp_path_retention_policy=failed", "test_clb6_sondages_v1.py"],
                       cwd=copie / "essais", env={**os.environ, "PYTHONPATH": f"{copie}/src:{BAC}/greffon", "PYTHONDONTWRITEBYTECODE": "1", "TRACE_IMPORT_ACCB6": str(trace)},
                       capture_output=True, text=True, timeout=600)
    hors = [l for l in trace.read_text().splitlines() if "controle_ia" in l.split("\t")[0] and str(copie) not in l]
    print(json.dumps({"id": mid, "code": r.returncode, "fin": r.stdout.splitlines()[-1:], "echecs": [l[:150] for l in r.stdout.splitlines() if l.startswith("FAILED")], "hors_copie": hors}, ensure_ascii=False), flush=True)
    shutil.rmtree(copie)
