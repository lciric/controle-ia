#!/usr/bin/env python3
"""Répétition jouet, sur une racine locale, du script remis à l'instance de la variante B (`scripts/etape_a_t07_variante_b_v1.sh` ;
ordre d'exécution de l'étape A, brouillon 2 ; consigne de la mère, R-2112 : « répète le bloc remis à l'instance sur une racine
locale, en mode jouet ») — v1.

1. **Course 7b jouet** : chaîne de T0.6 du commit `1609a4bf` (arbre `--arbre-t06`, lu seulement), mode jouet, entropie fixée
   (`repetition_jouet_t07_v2.ENVELOPPE`), dans un dépôt jetable ; le run écrit aussi un `lecture-sondes-t06.json` factice, que
   ce script **n'ouvre jamais** et dont il vérifie qu'il n'entre pas dans l'arbre de T0.7.
2. **Dépôt distant local** (`origin.git`, nu, filtres permis) portant :
   - `main` : C7 (code de cette branche : `src/`, `tests/`, `scripts/`, exigences, pièces lues par le repli), puis S7 (texte de
     T0.7 jouet scellé, configuration jouet avec `code_t07_exige` vrai, jeux, phrases, sondes légères factices), puis H
     (registre : `RUN-CONFIRMATION-T06`, `SCELLEMENT-T07`, jeux, concepts, `GO-LECTURE-T07` et son extrait, **`CODE-T07`** écrite
     par `code_t07_v1.ecrire_fichier_code` pour C7 ; tâches et consignes citées par la configuration de 7b) ;
   - `calcul/t06-confirmation-7b-v1` : ce que l'amorce v11 pousse (`runs/<run>/`, `diag/<run>/` dont le `lecture-sondes-t06.json`
     factice, et dans `donnees/<run>/` les adaptateurs, mesures, textes, manifeste du sous-ensemble et ses morceaux ; jamais les
     activations complètes).
3. **Le script de l'instance**, joué tel quel par `bash` sous `env -i` (aucune clé de la session), en essai local
   (`ESSAI_LOCAL=1` : racine locale, dépôt local, interpréteur de la session, liste d'essais réduite, ni minuterie, ni appel à
   Vast, ni modèle descendu) : essais, `CODE-T07`, repli (recalcul et garde d'équivalence), passe à blanc, étape A après le repli,
   poussées sur `donnees/t07-etape-a-v1`.
4. **Contrôles** : code 0 et fin demandée ; trois commits poussés (repli, passe à blanc, étape A) ; `SCORES-T07` et `SONDES-T07`
   au registre poussé ; sorties scellées ; `lecture-sondes-t06.json` ni dans l'arbre de l'instance, ni descendu dans son dépôt
   (objet manquant du clone partiel) ; puis **artefact** : le même script, sur une racine neuve, refuse la branche déjà poussée
   (R12), code 2, avant tout repli.

    PYTHONPATH=src python scripts/repetition_jouet_variante_b_t07_v1.py --arbre-t06 /home/user/wt-t07-jouet --dossier <neuf> \\
        --sortie <résumé.json>
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ICI / "src"))
sys.path.insert(0, str(ICI / "scripts"))

import repetition_jouet_t07_v1 as r1  # noqa: E402
import repetition_jouet_t07_v2 as r2  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
from controle_ia.t07 import code_t07_v1 as ct  # noqa: E402
from controle_ia.t07 import registre_v1 as rg  # noqa: E402

SCRIPT = ICI / "scripts" / "etape_a_t07_variante_b_v1.sh"
BR, BR7B = "donnees/t07-etape-a-v1", "calcul/t06-confirmation-7b-v1"
CODE = ("src", "tests", "scripts", "requirements-cpu.txt", "requirements-gpu.txt", "pyproject.toml", "docs/sources/invites-2606.08892-v1",
        "prereg/P3-consignes-v1.md", "prereg/P3-consignes-v1.md.sha256")
ESSAIS = "tests/test_t07_journal_p3bis_d3_v1.py"
ATTENDU = "20 passed"
MOTIFS_7B = ("adaptateur-", "mesures-t06.npz", "textes-actions-t06.jsonl", "activations-sous-ensemble-t06-")


def git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True).stdout.strip()


def copier_code(maison: Path) -> None:
    """Fichiers suivis de la tête de cette branche, sous les chemins de `CODE` (lus par `git show`, jamais l'arbre de travail)."""
    tete = git(ICI, "rev-parse", "HEAD")
    for f in git(ICI, "ls-tree", "-r", "--name-only", tete, "--", *CODE).splitlines():
        p = maison / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(subprocess.run(["git", "-C", str(ICI), "show", f"{tete}:{f}"], check=True, capture_output=True).stdout)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--arbre-t06", required=True)
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--entropie-t06", type=int, default=1)
    a = ap.parse_args(argv)
    base, arbre = Path(a.dossier).resolve(), Path(a.arbre_t06).resolve()
    if base.exists():
        print(f"REFUS : {base} existe déjà (R12)", file=sys.stderr)
        return 2
    if not git(arbre, "rev-parse", "HEAD").startswith(r1.COMMIT_T06):
        print(f"REFUS : arbre de T0.6 autre que {r1.COMMIT_T06}", file=sys.stderr)
        return 2
    base.mkdir(parents=True)
    journal = base / "journal-repetition.txt"
    resume = {"debut": datetime.now(timezone.utc).isoformat(), "commit_t07": git(ICI, "rev-parse", "HEAD"),
              "script": {"chemin": str(SCRIPT.relative_to(ICI)), "sha256": ct._sha(SCRIPT.read_bytes())}}
    # 1. course 7b jouet
    t06 = base / "t06"
    r1.depot_neuf(t06)
    config6 = r1.preparer_t06(t06, arbre)
    r6 = r1.lancer([a.python, "-c", r2.ENVELOPPE, str(a.entropie_t06), "--config", config6.name, "--run-id", r1.RUN_T06], t06,
                   arbre / "src", journal)
    resume["t06"] = {k: r6[k] for k in ("code", "duree_s")}
    if r6["code"] != 0:
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        return 1
    run6 = r1.RUN_T06
    # 2. dépôt distant local : main (C7, S7, H) et la branche de 7b
    origine = base / "origin.git"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(origine)], check=True)
    git(origine, "config", "uploadpack.allowFilter", "true")
    git(origine, "config", "uploadpack.allowAnySHA1InWant", "true")
    maison = base / "maison"
    r1.depot_neuf(maison)
    copier_code(maison)
    r1.committer(maison)
    c7 = git(maison, "rev-parse", "HEAD")
    for x in ("runs", "diag"):                                  # le manifeste de 7b, le temps d'en lire l'empreinte (preparer_t07)
        shutil.copytree(t06 / x / run6, maison / x / run6)
    shutil.copytree(t06 / "donnees" / "t06-jouet", maison / "donnees" / "t06-jouet")
    (maison / "registres").mkdir(exist_ok=True)
    shutil.copy(t06 / "registres" / "go.md", maison / "registres" / "go.md")
    avant = rg.date_utc(int(time.time()) - 3600)
    config7 = r1.preparer_t07(maison, avant)                    # commit « etape » : S7 et registre ensemble, séparés ci-dessous
    for x in ("runs", "diag"):
        shutil.rmtree(maison / x / run6)
    cfg = json.loads(config7.read_text(encoding="utf-8"))
    cfg["code_t07_exige"] = True
    config7.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(config7)
    registre = (maison / "registres" / "scellements-v1.md").read_text(encoding="utf-8")
    (maison / "registres" / "scellements-v1.md").unlink()
    r1.committer(maison)
    s7 = git(maison, "rev-parse", "HEAD")
    reg = maison / "registres" / "scellements-v1.md"
    reg.write_text(registre.replace("| GO-ETAPE-A-T07 |", "| GO-LECTURE-T07 |"), encoding="utf-8")
    f = ct.ecrire_fichier_code(maison, c7, maison / "registres" / "code-t07" / "CODE-T07-v1.json")
    with open(reg, "a", encoding="utf-8") as h:
        h.write(rg.ecrire_ligne(rg.CODE_T07, avant, "registres/code-t07/CODE-T07-v1.json", sceller(f)) + "\n")
    r1.committer(maison)
    h_main = git(maison, "rev-parse", "HEAD")
    git(maison, "checkout", "-q", "-b", BR7B, c7)
    for x in ("runs", "diag"):
        shutil.copytree(t06 / x / run6, maison / x / run6)
    (maison / "donnees" / run6).mkdir(parents=True)
    poussees = []
    for p in sorted((t06 / "donnees" / run6).iterdir()):
        if p.is_file() and p.name.startswith(MOTIFS_7B):
            shutil.copy(p, maison / "donnees" / run6 / p.name)
            poussees.append(p.name)
    r1.committer(maison)
    git(maison, "push", "-q", str(origine), "main", BR7B)
    resume["depot"] = {"C7": c7, "S7": s7, "H": h_main, "branche_7b": git(maison, "rev-parse", BR7B), "donnees_7b": poussees,
                       "lecture_sondes_factice_sur_7b": (t06 / "diag" / run6 / "lecture-sondes-t06.json").is_file()}
    # 3. le script de l'instance, tel quel, sous env -i
    def jouer(racine: Path) -> dict:
        env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(base), "LANG": "C.UTF-8", "GH_TOKEN": "essai-local",
               "ESSAI_LOCAL": "1", "RACINE_INSTANCE": str(racine), "DEPOT_URL": f"file://{origine}", "ESSAIS_LISTE": ESSAIS,
               "VENV_EXISTANT": str(Path(a.python).parents[1]), "GIT_CONFIG_NOSYSTEM": "1"}
        debut = time.perf_counter()
        p = subprocess.run(["bash", str(SCRIPT), s7, c7, run6, config7.name, BR, BR7B, ATTENDU, str(int(time.time()) + 6 * 3600)],
                           env=env, capture_output=True, text=True)
        with open(journal, "a", encoding="utf-8") as h:
            h.write(f"$ bash {SCRIPT.name} … (racine {racine.name})\ncode {p.returncode} en {round(time.perf_counter() - debut, 1)} s\n"
                    f"--- sortie\n{p.stdout[-8000:]}\n--- erreur\n{p.stderr[-4000:]}\n\n")
        fin = racine / "t07-etape-a-b-v1" / "fin-demandee"
        return {"code": p.returncode, "duree_s": round(time.perf_counter() - debut, 1),
                "fin": fin.read_text().strip() if fin.is_file() else None,
                "lignes": [l for l in p.stdout.splitlines() if " T07 " in l]}
    rj = jouer(base / "instance")
    resume["script"].update({k: rj[k] for k in ("code", "duree_s", "fin")})
    resume["lignes_t07"] = [l.split(" T07 ", 1)[1] for l in rj["lignes"]]
    # 4. contrôles
    depot_i = base / "instance" / "t07-etape-a-b-v1" / "depot"
    c = {}
    if rj["code"] == 0:
        commits = git(origine, "log", "--format=%s", f"{h_main}..{BR}").splitlines()
        c["commits_pousses"] = commits[::-1]
        ajoutes = git(origine, "diff", "--name-only", "--diff-filter=A", s7, BR).splitlines()
        c["fichiers_ajoutes"] = len(ajoutes)
        c["sorties_scellees"] = sorted(x for x in ajoutes if x.endswith(".sha256") and not x.startswith("traces/"))
        reg_pousse = git(origine, "show", f"{BR}:registres/scellements-v1.md")
        c["lignes_scores_sondes"] = [l.split("|")[1].strip() for l in reg_pousse.splitlines() if l.startswith(("| SCORES-T07 |", "| SONDES-T07 |"))]
        c["src_tests_inchanges"] = subprocess.run(["git", "-C", str(origine), "diff", "--quiet", c7, BR, "--", "src", "tests"]).returncode == 0
    c["lecture_sondes_dans_l_arbre"] = (depot_i / "diag" / run6 / "lecture-sondes-t06.json").exists()
    oid = git(origine, "rev-parse", f"{BR7B}:diag/{run6}/lecture-sondes-t06.json")
    manquants = subprocess.run(["git", "-C", str(depot_i), "rev-list", "--objects", "--missing=print", f"refs/remotes/origin/{BR7B}"],
                               capture_output=True, text=True).stdout.split()
    c["lecture_sondes_descendu"] = (oid in manquants)
    c["lecture_sondes_objet_manquant_du_clone"] = (f"?{oid}" in manquants)
    resume["controles"] = c
    # artefact : branche déjà poussée → refus R12, code 2, avant tout repli
    ra = jouer(base / "instance-artefact")
    resume["artefact_branche_deja_poussee"] = {"code": ra["code"], "fin": ra["fin"], "derniere": ra["lignes"][-1].split(" T07 ", 1)[1] if ra["lignes"] else None,
                                               "repli_joue": any("repli, essai" in l for l in ra["lignes"])}
    resume["fin"] = datetime.now(timezone.utc).isoformat()
    Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    ok = (rj["code"] == 0 and rj["fin"] == "fin 0" and not c["lecture_sondes_dans_l_arbre"] and not c["lecture_sondes_descendu"]
          and c.get("src_tests_inchanges") and len(c.get("lignes_scores_sondes", [])) == 2 and ra["code"] == 2)
    print(json.dumps({"script": rj["code"], "fin": rj["fin"], "commits": len(c.get("commits_pousses", [])), "artefact": ra["code"],
                      "lecture_sondes": {"arbre": c["lecture_sondes_dans_l_arbre"], "descendu": c["lecture_sondes_descendu"]},
                      "conforme": bool(ok)}, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
