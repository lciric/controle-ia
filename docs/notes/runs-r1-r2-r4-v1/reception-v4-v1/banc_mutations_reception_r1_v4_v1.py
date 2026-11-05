#!/usr/bin/env python3
"""Banc de mutations de `verifier_reception_r1_v4_v1.py` — v1 (modèle : `banc_mutations_v2.py` de la réception v3).

Une mutation par garde, qui la rend inopérante (`ctl.exiger("<garde>", lambda: …` devient
`ctl.exiger("<garde>", lambda: True or …`, toutes occurrences), plus une par occurrence pour les gardes à plusieurs
contrôles (chaque contrôle doit avoir son propre artefact) ; les gardes génériques des manifestes et des rattachements
(`ctl.exiger(garde, lambda: …`, nom passé en paramètre) sont mutées par occurrence ; le filtre des clés lues garde le
document entier. Chaque mutant doit faire échouer au moins un essai de `test_verifier_reception_r1_v4_v1.py` (tué) ; le
script non muté doit les passer tous. Mutants et dossiers d'essai sous `--tmp`, hors du dépôt de travail, effacés après
chaque mutant (disque) ; rien n'est écrit dans le dépôt, sauf la sortie demandée par `--sortie` (jamais écrasée).

  timeout 900 nice -n 10 .venv/bin/python -I docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/banc_mutations_reception_r1_v4_v1.py \\
      --tmp <dossier hors du dépôt> --sortie <fichier neuf> [--travailleurs 2]

Code de sortie : 0 si le témoin passe et si tous les mutants sont tués ; 1 sinon (R5, aucun repli silencieux)."""
import argparse
import datetime as dt
import hashlib
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "verifier_reception_r1_v4_v1.py"
ESSAIS = ICI / "test_verifier_reception_r1_v4_v1.py"
DEPOT = ICI.parents[3]
GARDES = ("fiche", "runs", "textes", "versement", "octets", "presence", "compagnon", "temoin", "reparation", "table",
          "chaine-locale", "commit-rejeu", "verdict", "table-comparee", "provenance", "comptes",
          "coherence-table", "fichiers", "npz", "recalcul")
MUTATIONS = tuple((g, f'ctl.exiger("{g}", lambda: ', f'ctl.exiger("{g}", lambda: True or ') for g in GARDES) + (
    ("generique", "ctl.exiger(garde, lambda: ", "ctl.exiger(garde, lambda: True or "),
    ("filtre", "garde = {}  # filtre", "garde = dict(doc)  # filtre"))


def remplacer_occurrence(source, avant, apres, i):
    debut = -1
    for _ in range(i + 1):
        debut = source.index(avant, debut + 1)
    return source[:debut] + apres + source[debut + len(avant):]


def lancer_essais(script, base):
    env = {**os.environ, "SCRIPT_RECEPTION_V4": str(script), "PYTHONDONTWRITEBYTECODE": "1"}
    base.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.perf_counter()
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-rf", "-p", "no:cacheprovider", f"--basetemp={base}",
                        str(ESSAIS)], capture_output=True, text=True, env=env, cwd=str(ICI))
    sortie = r.stdout + r.stderr
    echecs = re.findall(r"^FAILED (\S+)", sortie, flags=re.M)
    fin = [x for x in sortie.strip().splitlines() if x.strip()][-1:] or [""]
    shutil.rmtree(base, ignore_errors=True)
    return r.returncode, echecs, fin[0], time.perf_counter() - t0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tmp", required=True)
    ap.add_argument("--sortie", default=None)
    ap.add_argument("--travailleurs", type=int, default=2)
    ap.add_argument("--motifs", default=None, help="sous-ensemble de motifs, séparés par des virgules (passe partielle, "
                                                   "pour tenir sous le délai de 900 s par commande)")
    a = ap.parse_args(argv)
    tmp = Path(a.tmp).resolve()
    if DEPOT in tmp.parents or tmp == DEPOT:
        print("ARRÊT : --tmp doit être hors du dépôt de travail", file=sys.stderr)
        return 1
    if a.sortie and Path(a.sortie).exists():
        print(f"ARRÊT : {a.sortie} existe déjà (R12)", file=sys.stderr)
        return 1
    source = SCRIPT.read_text(encoding="utf-8")
    entete = (f"Banc de mutations de {SCRIPT.name} (sha256 {hashlib.sha256(source.encode('utf-8')).hexdigest()}) ; "
              f"essais {ESSAIS.name} (sha256 {hashlib.sha256(ESSAIS.read_bytes()).hexdigest()}) ; début "
              f"{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} ; python {sys.version.split()[0]}")
    print(entete, flush=True)
    code, echecs, fin, duree = lancer_essais(SCRIPT, tmp / "essais" / "temoin")
    temoin_ok = code == 0
    lignes = [entete, f"témoin (script non muté) : code {code} ; « {fin} » ; {duree:.1f} s ; "
                      f"{'conforme' if temoin_ok else 'NON CONFORME'}",
              "mutation (garde entière, ou garde#rang pour une seule occurrence) | occurrences mutées | issue | "
              "premier essai en échec | durée"]
    variantes, inapplicables = [], []
    choisis = None if a.motifs is None else set(a.motifs.split(","))
    if choisis is not None and not choisis <= {m[0] for m in MUTATIONS}:
        print(f"ARRÊT : motifs inconnus {sorted(choisis - {m[0] for m in MUTATIONS})}", file=sys.stderr)
        return 1
    for garde, avant, apres in MUTATIONS:
        if choisis is not None and garde not in choisis:
            continue
        n = source.count(avant)
        if n == 0:
            inapplicables.append(garde)
            continue
        if garde != "generique":
            variantes.append((garde, source.replace(avant, apres), str(n)))
        if n > 1:
            variantes += [(f"{garde}#{i + 1}", remplacer_occurrence(source, avant, apres, i), f"1 (rang {i + 1})")
                          for i in range(n)]

    def un(v):
        nom, texte, combien = v
        d = tmp / "mutants" / nom.replace("#", "-")
        d.mkdir(parents=True, exist_ok=False)
        mutant = d / SCRIPT.name
        mutant.write_text(texte, encoding="utf-8")
        code, echecs, fin, duree = lancer_essais(mutant, tmp / "essais" / nom.replace("#", "-"))
        tue = code == 1 and bool(echecs)
        essai = (echecs[0] if echecs else fin).split("::")[-1]
        ligne = f"{nom} | {combien} | {'tuée' if tue else 'SURVIVANTE (code ' + str(code) + ')'} | {essai} | {duree:.1f} s"
        print(ligne, flush=True)
        return tue, ligne

    with ThreadPoolExecutor(max_workers=max(1, a.travailleurs)) as ex:
        res = list(ex.map(un, variantes))
    lignes += [x[1] for x in res] + [f"{g} | 0 | MUTATION INAPPLICABLE | — | —" for g in inapplicables]
    tous = all(x[0] for x in res) and not inapplicables
    bilan = temoin_ok and tous
    lignes.append(f"bilan : {len(variantes)} mutants ({len(choisis) if choisis else len(MUTATIONS)} motifs"
                  f"{' : ' + ','.join(sorted(choisis)) if choisis else ''}, entiers et par occurrence), "
                  f"{'tous tués' if tous else 'au moins un survivant ou inapplicable'} ; témoin "
                  f"{'conforme' if temoin_ok else 'non conforme'} ; fin "
                  f"{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} → {'CONFORME' if bilan else 'NON CONFORME'}")
    texte = "\n".join(lignes) + "\n"
    print(lignes[-1])
    if a.sortie:
        Path(a.sortie).write_text(texte, encoding="utf-8")
    return 0 if bilan else 1


if __name__ == "__main__":
    sys.exit(main())
