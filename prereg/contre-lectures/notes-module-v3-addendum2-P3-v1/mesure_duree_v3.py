"""Mesure de la durée de la ligne de commande complète de l'addendum 2 (module v3), sur un dépôt jouet de taille réelle
(CV2-04 : commande complète, imports seuls, fonction pure, mémoire maximale en Mio et en Mo ; mesures brutes versées).

Données synthétiques seulement (aides du fichier de tests v3 et du code gelé) : 60 tâches, 4 conditions, 10 pas, 600
actions par condition, 430 sondes (2 principales, 214 sondes de plancher chacune), coûts plantés, les cinq formes
présentes (`PROBAS_SAIN` des tests : honnête et témoin portent les cinq ; c'est le cas le plus chargé, chaque `E_-f` et
chaque écart de forme calculés). Dépôt git jouet construit sous `module-v3/tmp/` (code de `src/` copié,
préenregistrement de P3, run source décisif scellé, lecture décisive par le code gelé, commit de N-025, module v3 aux
constantes du run jouet, tests v3, texte de l'addendum 2 scellé : S2). Puis, pour chacune de N copies du dépôt :
- la vraie commande, dans un processus séparé, aux paramètres du texte (10 000 tirages) : durée murale, temps processeur
  (utilisateur + système) et mémoire maximale (`ru_maxrss` rendu par `os.wait4` pour ce processus, en Kio) ;
- un processus qui ne fait qu'importer le module (démarrage, imports, sortie) : durée murale ; et, dans ce processus,
  la durée des imports eux-mêmes, en trois parts : numpy, `controle_ia.harnais.validation_reelle`, le reste du module ;
- un processus vide (`python -B -c pass`) : durée murale (démarrage de l'interpréteur seul) ;
- la fonction pure `analyser_addendum2` seule, dans ce processus (entrées chargées avant, 10 000 tirages).
Charge de la machine (`os.getloadavg`) relevée avant chaque mesure. Le dépôt jouet est supprimé à la fin.
Mesures brutes écrites dans `module-v3/mesures-duree-v1.txt` (une ligne par mesure), refusé si le fichier existe (R12).

Usage (depuis la racine du dépôt de travail) : PYTHONPATH=src python -B <ce fichier> [N]
"""
import sys

sys.dont_write_bytecode = True

import datetime  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import platform  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pytest  # noqa: E402

ICI = Path(__file__).resolve().parent
V3 = ICI.parent
sys.path.insert(0, str(V3))

import test_audit_verdict_p3_v1 as T  # noqa: E402

av, lp = T.av, T.lp
TMP = V3 / "tmp" / "mesure-duree"
SORTIE = V3 / "mesures-duree-v1.txt"
RUN, LEC = "20261020-100000-p3-synthetique-mesure", "20261020-110000-lecture-mesure"
N_TACHES, N_PLANCHER = 60, 214


def charge():
    return "{:.2f}/{:.2f}/{:.2f}".format(*os.getloadavg())


def construire(racine: Path) -> dict:
    d = racine / "depot"
    d.mkdir(parents=True)
    T.git(d, "init", "-q", "-b", "main")
    T.git(d, "config", "user.email", "test@example.invalid")
    T.git(d, "config", "user.name", "test")
    shutil.copytree(T.DEPOT / "src" / "controle_ia", d / "src" / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (d / "README").write_text("x\n")
    T.committer(d)
    c0 = T._rev(d)
    sha_config = hashlib.sha256(T.config_canonique(T.CONFIG_SOURCE)).hexdigest()
    T._prereg_conforme(d / av.PREREG_P3, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                          f"- Configuration de P3 (empreinte canonique) : `{sha_config}`"])
    T.committer(d)
    src = T._src(0, n_taches=N_TACHES, n_pl=N_PLANCHER, probas=T.PROBAS_SAIN)
    t = src["tables"]
    taille = {"actions": int(t["condition"].size), "sondes": int(len(t["noms_sondes"])),
              "taches": int(np.unique(t["tache"]).size), "pas": int(np.unique(t["pas"]).size),
              "par_condition": {c: int((t["condition"] == c).sum()) for c in T.CONDITIONS_TEXTE},
              "formes_presentes": [f for f in T.FORMES_TEXTE if np.asarray(t[f]).astype(bool).any()]}
    assert taille == {"actions": 2400, "sondes": 430, "taches": 60, "pas": 10,
                      "par_condition": {c: 600 for c in T.CONDITIONS_TEXTE},
                      "formes_presentes": list(T.FORMES_TEXTE)}, taille
    T._ecrire_run_source(d, RUN, src, T._textes_lisibles(src))
    T.committer(d)
    with pytest.MonkeyPatch.context() as mp:            # lecture décisive synthétique (moins de tirages des aires)
        mp.setattr(lp, "TIRAGES_AIRE", 300)
        mp.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
        lp.analyser(d, RUN, LEC, av.PREREG_P3, av.ENTROPIE_P3, autoriser_depot_sale=True)
    T.committer(d)
    (d / "registres").mkdir()
    (d / "registres" / "decisions.md").write_text("N-025 : option (a), synthétique\n", encoding="utf-8")
    T.committer(d)
    n025 = T._rev(d)
    module, tests = d / av.CHEMIN_MODULE, d / av.CHEMIN_TESTS
    module.parent.mkdir(parents=True)
    module.write_bytes(T._module_pour(RUN, LEC, n025, T._entrees(d, RUN, LEC)))
    tests.write_bytes(Path(T.__file__).read_bytes())
    T._prereg_conforme(d / av.PREREG_ADDENDUM2, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                                 f"- Module de l'addendum 2 (sha256) : `{T.empreinte(module)}`",
                                                 f"- Tests du module (sha256) : `{T.empreinte(tests)}`"])
    T.committer(d)
    return {"depot": d, "taille": taille}


def _env(d: Path) -> dict:
    return {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1"}


def _processus(cmd, d: Path) -> dict:
    """Un processus séparé : durée murale, temps processeur et `ru_maxrss` (Kio) de ce processus (`os.wait4`)."""
    sortie, erreurs = d.parent / "sortie.txt", d.parent / "erreurs.txt"
    with open(sortie, "w") as so, open(erreurs, "w") as se:
        debut = time.perf_counter()
        p = subprocess.Popen(cmd, cwd=d, env=_env(d), stdout=so, stderr=se)
        _, statut, ru = os.wait4(p.pid, 0)
        duree = time.perf_counter() - debut
    p.returncode = os.waitstatus_to_exitcode(statut)
    texte = sortie.read_text(encoding="utf-8")
    if p.returncode != 0:
        raise SystemExit(f"processus en échec ({p.returncode}) : {erreurs.read_text(encoding='utf-8')[-2000:]}")
    return {"duree_s": duree, "cpu_s": ru.ru_utime + ru.ru_stime, "maxrss_kio": ru.ru_maxrss, "sortie": texte}


def commande(d: Path, run_add: str) -> dict:
    r = _processus([sys.executable, "-B", av.CHEMIN_MODULE, "--run-source", RUN, "--lecture", LEC, "--run-addendum2",
                    run_add, "--prereg", av.PREREG_ADDENDUM2, "--entropie", str(av.ENTROPIE_P3)], d)
    corps = T.verifier_resultat(d, d / "diag" / run_add / "lecture-addendum2-p3.json")["resultat"]
    n = corps["nombre_de_controles"]
    r["verification"] = (f"sortie scellée vérifiée ; tirages {corps['constantes']['tirages']} ; contrôles écrits "
                         f"{n['ecrits']}, lus {n['lus']} (dont non lus {n['dont_non_lus']}), sans objet {n['sans_objet']}")
    return r


IMPORTS = """import json, time
t0 = time.perf_counter()
import numpy
t1 = time.perf_counter()
import controle_ia.harnais.validation_reelle
t2 = time.perf_counter()
import importlib.util
s = importlib.util.spec_from_file_location("m", {chemin!r}); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
t3 = time.perf_counter()
print(json.dumps({{"numpy_s": t1 - t0, "validation_reelle_s": t2 - t1, "reste_du_module_s": t3 - t2, "imports_s": t3 - t0}}))
"""


def imports_seuls(d: Path) -> dict:
    r = _processus([sys.executable, "-B", "-c", IMPORTS.format(chemin=av.CHEMIN_MODULE)], d)
    return {**r, **json.loads(r["sortie"].strip().splitlines()[-1])}


def processus_vide(d: Path) -> dict:
    return _processus([sys.executable, "-B", "-c", "pass"], d)


def fonction_pure(d: Path, nom: str) -> float:
    m = T._charger_copie(d / av.CHEMIN_MODULE, nom)
    assert m.TIRAGES == 10_000
    source = lp.charger_source(d, RUN)
    lecture = json.loads((d / "diag" / LEC / "lecture-p3.json").read_text(encoding="utf-8"))["resultat"]
    g = T.graines(m.cles_addendum2(), m.ENTROPIE_P3)
    debut = time.perf_counter()
    m.analyser_addendum2(source, lecture, g)
    return time.perf_counter() - debut


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    if SORTIE.exists():
        raise SystemExit(f"{SORTIE} existe déjà : une nouvelle mesure prend un nouveau nom (R12)")
    if TMP.exists():
        shutil.rmtree(TMP)
    TMP.mkdir(parents=True)
    lignes = []
    try:
        debut = time.perf_counter()
        g = construire(TMP / "gabarit")
        construction = time.perf_counter() - debut
        lignes += [
            "# Mesures brutes de durée, addendum 2 de P3, module v3 (CV2-04). Une ligne par mesure.",
            f"# date (UTC) : {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}",
            f"# module v3 : {T.empreinte(Path(av.__file__))} ; tests v3 : {T.empreinte(Path(T.__file__))}",
            f"# script : module-v3/mesure-duree/mesure_duree_v3.py ({T.empreinte(Path(__file__))})",
            f"# machine : {platform.machine()}, {os.cpu_count()} cœurs, Python {platform.python_version()}, "
            f"numpy {np.__version__} ; machine partagée avec d'autres sessions (charge relevée à chaque mesure)",
            f"# dépôt jouet : {json.dumps(g['taille'], ensure_ascii=False)} ; lecture décisive par le code gelé ; "
            f"construction {construction:.1f} s",
            "# unités : durées en secondes ; mémoire : ru_maxrss en Kio (1 Kio = 1 024 octets), "
            "Mio = Kio / 1 024, Mo = Kio × 1 024 / 10^6",
            "# colonnes : passage ; mesure ; valeurs ; charge (1/5/15 min) avant la mesure",
        ]
        for k in range(n):
            d = TMP / f"copie-{k}" / "depot"
            shutil.copytree(g["depot"], d, symlinks=True)
            c = charge()
            r = commande(d, f"20261020-15000{k}-addendum2-p3")
            kio = r["maxrss_kio"]
            lignes.append(f"{k + 1} ; ligne de commande complète ; murale {r['duree_s']:.3f} s ; processeur {r['cpu_s']:.3f} s"
                          f" ; ru_maxrss {kio} Kio = {kio / 1024:.1f} Mio = {kio * 1024 / 1e6:.1f} Mo ; "
                          f"{r['verification']} ; charge {c}")
            c = charge()
            r = imports_seuls(d)
            lignes.append(f"{k + 1} ; processus qui ne fait qu'importer le module ; murale {r['duree_s']:.3f} s ; "
                          f"imports mesurés dans le processus {r['imports_s']:.3f} s (numpy {r['numpy_s']:.3f} s, "
                          f"controle_ia.harnais.validation_reelle {r['validation_reelle_s']:.3f} s, reste du module "
                          f"{r['reste_du_module_s']:.3f} s) ; ru_maxrss {r['maxrss_kio']} Kio ; charge {c}")
            c = charge()
            r = processus_vide(d)
            lignes.append(f"{k + 1} ; processus vide (python -B -c pass) ; murale {r['duree_s']:.3f} s ; charge {c}")
            c = charge()
            f = fonction_pure(d, f"module_mesure_{k}")
            lignes.append(f"{k + 1} ; fonction pure analyser_addendum2 (10 000 tirages, dans le processus de mesure) ; "
                          f"murale {f:.3f} s ; charge {c}")
            print(*lignes[-4:], sep="\n", flush=True)
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"écrit : {SORTIE}")


if __name__ == "__main__":
    main()
