"""Banc de mutations du script v4 de la variante B (`scripts/etape_a_t07_variante_b_v4.sh`), v1 : corrections CLC-P3-02 et
CLC-P3-05 (R-2311). Chaque mutation porte sur une **copie** du script (jamais le fichier de l'arbre) ; chaque passage joue la copie
en essai local contre une **copie nue** d'un dépôt distant de la répétition v4 (les dépôts de la répétition ne sont pas touchés),
sous une racine neuve ; rien n'est retiré. Copie saine d'abord, pour chaque cas.

Cas :
- `controle` (dépôt « sans témoin ») : sain → code 2 à l'étape 8, dernière ligne « ARRET : contrôle avant l'ouverture … »,
  aucun repli ; s1 (issue du contrôle ignorée), s3 (code de l'arrêt changé) doivent être tués ;
- `tete` (tête du script jusqu'à `MESURE=`, hors essai, `CPU_ESSAI` posée) : sain → code 2, refus ; s4 (CPU_ESSAI hors de la liste
  des variables d'essai) doit être tué ;
- `epyc` (dépôt sain, `CPU_ESSAI` EPYC, branche neuve) : sain → code 0, `ENV_CPU` vide ; s5 (forme du v3, `"${ENV_CPU[@]}"`) :
  mutant **équivalent sous bash ≥ 4.4** (bash de cette machine : 5.2), attendu survivant, rapporté comme tel.

    python -I banc_script_v4_v1.py ARBRE REPETITION.json SORTIE.json DOSSIER_NEUF
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent / "script"            # remplacé par le 4e argument (dossier neuf)
PY_VENV = "/home/user/controle-ia-travail/.venv"
SCRIPT = "scripts/etape_a_t07_variante_b_v4.sh"
CPU_EPYC = "AMD EPYC 7763 64-Core Processor"
MUTATIONS = [
    ("s1", "étape 8 : issue du contrôle avant l'ouverture ignorée", "controle",
     '[ "$c" = 0 ] || arret "contrôle avant l\'ouverture (réextraction de P3)', 'true || arret "contrôle avant l\'ouverture (réextraction de P3)'),
    ("s3", "étape 8 : arrêt du contrôle en code 4 au lieu de 2", "controle",
     "| tr '\\n' ' ') : rien n'est ouvert\" 2", "| tr '\\n' ' ') : rien n'est ouvert\" 4"),
    ("s4", "CPU_ESSAI hors de la liste des variables d'essai", "tete", " BORNE_ESSAI CPU_ESSAI\"", " BORNE_ESSAI\""),
    ("s5", "forme du v3 pour ENV_CPU (équivalente sous bash ≥ 4.4)", "epyc",
     'env CUBLAS_WORKSPACE_CONFIG=:4096:8 ${ENV_CPU[@]+"${ENV_CPU[@]}"} PYTHONPATH=src', 'env CUBLAS_WORKSPACE_CONFIG=:4096:8 "${ENV_CPU[@]}" PYTHONPATH=src'),
]


def git(*a: str) -> str:
    return subprocess.run(["git", *a], check=True, capture_output=True, text=True).stdout.strip()


def copie_nue(source: Path, cible: Path) -> Path:
    if cible.exists():
        raise SystemExit(f"{cible} existe déjà (R12)")
    git("clone", "-q", "--bare", str(source), str(cible))
    git("-C", str(cible), "config", "uploadpack.allowFilter", "true")
    git("-C", str(cible), "config", "uploadpack.allowAnySHA1InWant", "true")
    return cible


def jouer(script: Path, cas: str, o: dict, run6: str, racine: Path, branche: str) -> dict:
    base = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(ICI), "LANG": "C.UTF-8"}
    args = [o["S7"], o["C7"], run6, o["config"], branche, "calcul/t06-confirmation-7b-v1", "20 passed", str(int(time.time()) + 6 * 3600),
            "JD,JA,JC,CONCEPTS"]
    t0 = time.perf_counter()
    if cas == "tete":
        lignes = script.read_text(encoding="utf-8").splitlines(keepends=True)
        n = next(i for i, l in enumerate(lignes) if l.startswith("MESURE="))
        p = subprocess.run(["bash", "-c", "".join(lignes[: n + 1]), "bash", *args], env={**base, "CPU_ESSAI": CPU_EPYC},
                           capture_output=True, text=True, timeout=60)
    else:
        env = {**base, "GH_TOKEN": "essai-local", "ESSAI_LOCAL": "1", "RACINE_INSTANCE": str(racine), "DEPOT_URL": f"file://{o['origine']}",
               "ESSAIS_LISTE": "tests/test_t07_journal_p3bis_d3_v1.py", "VENV_EXISTANT": PY_VENV, "GIT_CONFIG_NOSYSTEM": "1",
               **({"CPU_ESSAI": CPU_EPYC} if cas == "epyc" else {})}
        p = subprocess.run(["bash", str(script), *args], env=env, capture_output=True, text=True, timeout=1800)
    lignes = [l.split(" T07 ", 1)[1] for l in p.stdout.splitlines() if " T07 " in l]
    return {"code": p.returncode, "duree_s": round(time.perf_counter() - t0, 1), "derniere": lignes[-1] if lignes else p.stdout[-300:],
            "repli_joue": any(l.startswith("repli, essai") for l in lignes), "unbound": "unbound variable" in p.stdout + p.stderr}


def sain(cas: str, r: dict) -> bool:
    if cas == "controle":
        return (r["code"] == 2 and not r["repli_joue"]
                and r["derniere"].startswith("ARRET : contrôle avant l'ouverture (réextraction de P3) : code 2 : REFUS : "))
    if cas == "tete":
        return r["code"] == 2 and "T07 REFUS : CPU_ESSAI n'est permise qu'en essai local" in r["derniere"]
    return r["code"] == 0 and r["derniere"].startswith("FIN : étape A menée au bout") and not r["unbound"]


def main(arbre: Path, repetition: Path, sortie: Path) -> int:
    ICI.mkdir(parents=True, exist_ok=False)
    rep = json.loads(repetition.read_text(encoding="utf-8"))
    run6 = "20261110-060000-t06-jouet"                         # r1.RUN_T06 (repetition_jouet_t07_v1), présent à la branche de 7b
    git("-C", rep["depots"]["sain"]["origine"], "cat-file", "-e", f"calcul/t06-confirmation-7b-v1:runs/{run6}/manifeste.json")
    depots = {"controle": dict(rep["depots"]["sans_temoin"]), "epyc": dict(rep["depots"]["sain"]), "tete": dict(rep["depots"]["sain"])}
    for cas, o in depots.items():
        if cas != "tete":
            o["origine"] = str(copie_nue(Path(o["origine"]), ICI / f"origine-{cas}.git"))
    texte = (arbre / SCRIPT).read_text(encoding="utf-8")
    res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "script": SCRIPT, "bash": subprocess.run(
        ["bash", "-c", "echo $BASH_VERSION"], capture_output=True, text=True).stdout.strip(), "saines": {}, "mutations": []}
    (ICI / "sain.sh").write_text(texte, encoding="utf-8")
    for cas in ("controle", "tete", "epyc"):
        r = jouer(ICI / "sain.sh", cas, depots[cas], run6, ICI / f"racine-sain-{cas}", f"donnees/t07-banc-sain-{cas}")
        r["sain"] = sain(cas, r)
        res["saines"][cas] = r
        print("sain", cas, r["sain"], r["code"], r["derniere"][:120], flush=True)
    if not all(r["sain"] for r in res["saines"].values()):
        sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return 1
    for mid, quoi, cas, ancien, nouveau in MUTATIONS:
        n = texte.count(ancien)
        if n != 1:
            res["mutations"].append({"id": mid, "quoi": quoi, "erreur": f"motif trouvé {n} fois"})
            print(mid, "MOTIF", n, flush=True)
            continue
        f = ICI / f"{mid}.sh"
        f.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        r = jouer(f, cas, depots[cas], run6, ICI / f"racine-{mid}", f"donnees/t07-banc-{mid}")
        r.update(id=mid, quoi=quoi, cas=cas, issue="survit" if sain(cas, r) else "tuée")
        res["mutations"].append(r)
        print(mid, r["issue"], r["code"], r["derniere"][:140], flush=True)
    res["fin"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    res["resume"] = {"mutations": len(MUTATIONS), "tuees": [m["id"] for m in res["mutations"] if m.get("issue") == "tuée"],
                     "survivantes": [m["id"] for m in res["mutations"] if m.get("issue") == "survit"]}
    sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["resume"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    ICI = Path(__file__).resolve().parent / sys.argv[4]
    sys.exit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve()))
