"""Banc du développeur accb6-v2 (R-2330) : chaque mutation est appliquée à une copie de l'arbre de la branche (`src`, `tests`,
`scripts`), jamais à l'arbre ; la suite `tests/test_accb6_*.py` (sept fichiers, essais du contre-lecteur compris) est jouée sur la copie
avec `-x`, `-o pythonpath=` et `PYTHONPATH` vers la copie, import tracé (greffon `trace_import_accb6_v2`) ; l'essai aux constantes
réelles est exclu (`-k`, 260 s et 150 Mo de jouet ; joué dans la suite entière) ; les deux essais d'égalité de l'énumération sont
désélectionnés (ils tuent toute mutation de `etats_v1.py` par l'empreinte écrite) : pour `etats_v1.py` et `phrases_v1.py`, l'énumération
v2 est rejouée à part et comparée, hors lignes « module : », à la sortie versée du code v2.
v2d (après le redémarrage du conteneur, 11 novembre vers 10:20 UTC) : bornes de temps — délai de 900 s par course de pytest
(dépassé : « délai dépassé », non tuée, non comptée comme survivante) et échéance globale (BANC_ECHEANCE, secondes epoch) au-delà de
laquelle aucune mutation neuve n'est lancée (« non jouée (échéance) ») ; borne de taille : copie seule (src, tests, scripts), dossiers
d'essais effacés au fil de l'eau (« failed », -x), 1 Go libre exigé avant chaque course.
v2c : `tmp_path_retention_policy=failed` (avec « none », pytest garde les dossiers de tous les essais jusqu'à la fin de la session :
le disque se remplissait, les témoins T00 et T01 tombaient sur Errno 28 ; avec « failed » et `-x`, seul le dossier de l'essai en
échec reste, effacé avec la copie).
v2b : une mutation dont la course rencontre un disque plein (Errno 28, dans les essais ou l'énumération) est rejouée, jusqu'à
quatre fois, après une attente d'au moins 1 Go libre (disque partagé avec d'autres sessions) ; chaque tentative est écrite.
Usage : python banc_accb6_v2d.py ARBRE SORTIE.jsonl MODULE_DE_MUTATIONS [PROCESSUS] [IDS…]"""
import importlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI / "mutations"))
PY = "/home/user/controle-ia-travail/.venv/bin/python"
OUTILS = ICI.parent / "outils"
COPIES = ICI / "copies"
DESELECT = ["tests/test_accb6_etats_v1.py::test_enumeration_rejouee_egale_a_la_sortie_versee",
            "tests/test_accb6_etats_v1.py::test_enumeration_du_code_v2_egale_a_celle_du_code_v1_hors_empreinte_de_etats_v1"]
ESSAIS = ["tests/test_accb6_etats_v1.py", "tests/test_accb6_lecture_v1.py", "tests/test_accb6_garde_v1.py", "tests/test_accb6_code_v1.py",
          "tests/test_accb6_relance_v1.py", "tests/test_accb6_phrases_texte_v1.py", "tests/test_accb6_contre_lecture_v1.py"]
SORTIE_ENUM = "scripts/enumeration-etats-accb6-v2-code-v2.txt"


def libre_mo() -> int:
    st = os.statvfs("/")
    return st.f_bavail * st.f_frsize // 2 ** 20


def attendre_disque(minimum_mo: int = 1024) -> None:
    while libre_mo() < minimum_mo:
        time.sleep(5)


ECHEANCE = float(os.environ.get("BANC_ECHEANCE", "inf"))
DELAI_S = 900


def jouer(arbre: Path, mut, essais=None) -> dict:
    tentatives = []
    if time.time() > ECHEANCE:
        return {"id": mut[0], "fichier": mut[1], "quoi": mut[4], "erreur": "non jouée (échéance du banc atteinte)"}
    for _ in range(4):
        attendre_disque()
        s = jouer_une_fois(arbre, mut, essais or ESSAIS)
        tentatives.append({k: s.get(k) for k in ("code_pytest", "premier_echec", "disque_plein", "enumeration", "duree_s")})
        if not s.get("disque_plein"):
            break
    s["tentatives"] = tentatives
    return s


def jouer_une_fois(arbre: Path, mut, essais) -> dict:
    ident, fichier, ancien, nouveau, quoi = mut
    COPIES.mkdir(exist_ok=True)
    copie = Path(os.path.realpath(tempfile.mkdtemp(prefix=f"{ident}-", dir=COPIES)))
    try:
        for d in ("src", "tests", "scripts"):
            shutil.copytree(arbre / d, copie / d, ignore=shutil.ignore_patterns("__pycache__"))
        (copie / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
        cible = copie / "src" / "controle_ia" / "accumulation_b6" / fichier
        texte = cible.read_text(encoding="utf-8")
        n = texte.count(ancien)
        if n != 1:
            return {"id": ident, "fichier": fichier, "quoi": quoi, "erreur": f"ancien présent {n} fois"}
        cible.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        trace = copie / "trace-import.txt"
        env = {k: v for k, v in os.environ.items() if k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR")}
        env.update(PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=f"{OUTILS}:{copie / 'src'}", TRACE_IMPORT_ACCB6=str(trace))
        t0 = time.time()
        try:
          r = subprocess.run([PY, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-p", "trace_import_accb6_v2", "-o", "pythonpath=",
                            "--rootdir", str(copie), "-c", str(copie / "pytest.ini"), "--basetemp", str(copie / "bt"),
                            "-o", "tmp_path_retention_policy=failed", "-k", "not constantes_reelles", "--tb=line", "-rf",
                            *[a for d in DESELECT for a in ("--deselect", d)], *essais],
                           cwd=copie, env=env, capture_output=True, text=True, timeout=DELAI_S)
        except subprocess.TimeoutExpired:
            return {"id": ident, "fichier": fichier, "quoi": quoi, "erreur": f"délai dépassé ({DELAI_S} s)", "tuee": False,
                    "duree_s": round(time.time() - t0, 1)}
        lignes = trace.read_text(encoding="utf-8").splitlines() if trace.is_file() else []
        chemins = [x.split("\t", 1)[1] for x in lignes if "\t" in x]
        trace_ok = (bool(chemins) and all(p.startswith(str(copie) + "/") for p in chemins) and str(cible) in chemins
                    and nouveau in cible.read_text(encoding="utf-8"))
        echecs = [x for x in r.stdout.splitlines() if x.startswith("FAILED") or x.startswith("ERROR")]
        s = {"id": ident, "fichier": fichier, "quoi": quoi, "code_pytest": r.returncode, "tuee": r.returncode == 1,
             "premier_echec": echecs[0][:260] if echecs else None,
             "disque_plein": "Errno 28" in r.stdout + r.stderr or "No space left" in r.stdout + r.stderr, "libre_mo_apres": libre_mo(),
             "derniere_ligne": r.stdout.strip().splitlines()[-1][:160] if r.stdout.strip() else r.stderr[-300:],
             "import_dans_la_copie": trace_ok, "modules_traces": len(chemins), "duree_s": round(time.time() - t0, 1)}
        if fichier in ("etats_v1.py", "phrases_v1.py"):
            out = copie / "enum.txt"
            e = subprocess.run([PY, "-I", "-B", str(copie / "scripts" / "enumeration_etats_accb6_v2.py"), str(out)], capture_output=True,
                               text=True, timeout=600)
            corps = [x for x in (arbre / SORTIE_ENUM).read_text(encoding="utf-8").splitlines() if not x.startswith("module :")]
            if "No space left" in e.stderr or "Errno 28" in e.stderr:
                s["disque_plein"] = True
                s["enumeration"] = "disque plein"
            elif e.returncode != 0:
                s["enumeration"] = f"écart relevé par le script : {e.stderr.strip()[-300:]}"
            else:
                autre = [x for x in out.read_text(encoding="utf-8").splitlines() if not x.startswith("module :")]
                s["enumeration"] = "sortie égale (hors empreintes)" if autre == corps else (
                    f"sortie différente ({sum(1 for a, b in zip(autre, corps) if a != b) + abs(len(autre) - len(corps))} lignes)")
        return s
    finally:
        shutil.rmtree(copie, ignore_errors=True)


def main() -> None:
    arbre, sortie, module = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), sys.argv[3]
    processus = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    ids = set(sys.argv[5:])
    mutations = [m for m in importlib.import_module(module).MUTATIONS if not ids or m[0] in ids]
    cl = "tests/test_accb6_contre_lecture_v1.py"
    essais = [cl] + [e for e in ESSAIS if e != cl] if "_cl_" in module else list(ESSAIS)   # lots du contre-lecteur : ses essais d'abord
    with ThreadPoolExecutor(max_workers=processus) as ex, open(sortie, "a", encoding="utf-8") as f:
        for res in ex.map(lambda m: jouer(arbre, m, essais), mutations):
            f.write(json.dumps(res, ensure_ascii=False) + "\n")
            f.flush()
            print(res["id"], "TUÉE" if res.get("tuee") else ("ERREUR" if res.get("erreur") else "SURVIT"),
                  res.get("premier_echec") or res.get("erreur") or res.get("derniere_ligne"), res.get("enumeration", ""),
                  "| import dans la copie :", res.get("import_dans_la_copie"), "|", res.get("duree_s"), "s | tentatives :",
                  len(res.get("tentatives", [])), "| disque plein :", res.get("disque_plein"), flush=True)


if __name__ == "__main__":
    main()
