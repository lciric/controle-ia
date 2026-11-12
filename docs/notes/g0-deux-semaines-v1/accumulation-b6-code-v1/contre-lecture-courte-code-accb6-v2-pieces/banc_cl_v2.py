"""Banc borné du contre-lecteur court (CLB6) : mutations neuves sur copies de l'arbre 282e295e ; suite test_accb6_* avec -x, sans
l'essai long aux constantes réelles ; import tracé ; tuée = code 1 de pytest."""
import json, os, shutil, subprocess, sys, time
from pathlib import Path

BAC = Path(sys.argv[1]); ARBRE = BAC / "arbre"; PY = "/home/user/controle-ia-travail/.venv/bin/python"
L = "src/controle_ia/accumulation_b6/lecture_v1.py"
MUT = {
 "T0": (L, 'ID_PLANCHER_NEUF = "plancher neuf"\n', 'ID_PLANCHER_NEUF = "plancher neuf"  # témoin sans effet\n'),
 "N1": (L, "            if plc.shape[0] != et.N_DIRECTIONS:", "            if k == 0 and plc.shape[0] != et.N_DIRECTIONS:"),
 "N2": (L, "    if chaines is None:\n        return sortie", "    if not chaines:\n        return sortie"),
 "N3": (L, 'PREFIXE_PLANCHER_NEUF = "plancher neuf de "', 'PREFIXE_PLANCHER_NEUF = "plancher neuf"'),
 "N4": (L, '                           "sondes_visees": [s["nom"] for s in (sondes or []) if s["nom"] in x]})',
        '                           "sondes_visees": [s["nom"] for s in (sondes or []) if s["nom"] in x]})\n            break'),
 "N5": (L, '        rt07 = reserves_t07_recopiees(e4, so["sondes"] if so else None) if calc is not None else []',
        '        rt07 = reserves_t07_recopiees(e4, so["sondes"] if so else None)'),
 "N6": (L, "            if plc.shape[0] != et.N_DIRECTIONS:", "            if plc.shape[0] not in (et.N_DIRECTIONS, 4 * et.N_DIRECTIONS):"),
 "N7": (L, '                           "sondes_visees": [s["nom"] for s in (sondes or []) if s["nom"] in x]})',
        '                           "sondes_visees": [s["nom"] for s in (sondes or []) if s["concept"] in x]})'),
}
def jouer(mid):
    f, a, b = MUT[mid]
    copie = BAC / "banc" / f"copie-{mid}"
    copie.mkdir()
    for d in ("src", "tests", "scripts"):
        shutil.copytree(ARBRE / d, copie / d)
    p = copie / f; t = p.read_text(encoding="utf-8")
    assert t.count(a) == 1, (mid, t.count(a))
    p.write_text(t.replace(a, b), encoding="utf-8")
    trace = BAC / "banc" / f"trace-{mid}.txt"
    env = {**os.environ, "PYTHONPATH": f"{copie}/src:{BAC}/greffon", "PYTHONDONTWRITEBYTECODE": "1", "TRACE_IMPORT_ACCB6": str(trace)}
    t0 = time.time()
    try:
        r = subprocess.run([PY, "-m", "pytest", "-q", "-x", "-o", "pythonpath=", "-p", "trace_import_accb6_v2", "-p", "no:cacheprovider",
                            "--rootdir", str(copie), "-c", "/dev/null", f"--basetemp={copie}/bt", "-o", "tmp_path_retention_policy=failed",
                            "-k", "not test_commande_aux_constantes_reelles"] + sorted(str(x) for x in (copie / "tests").glob("test_accb6_*.py")),
                           cwd=copie, env=env, capture_output=True, text=True, timeout=900)
        code, fin = r.returncode, r.stdout[-1500:]
    except subprocess.TimeoutExpired:
        code, fin = "délai", ""
    hors = [l for l in trace.read_text().splitlines() if str(copie) not in l] if trace.is_file() else ["trace absente"]
    echec = [l for l in fin.splitlines() if l.startswith("FAILED") or l.startswith("ERROR")]
    out = {"id": mid, "code": code, "duree_s": round(time.time() - t0, 1), "premier_echec": echec[:1], "fin": fin.splitlines()[-1:] , "hors_copie": hors}
    shutil.rmtree(copie)
    print(json.dumps(out, ensure_ascii=False), flush=True)
for m in sys.argv[2:]:
    jouer(m)
