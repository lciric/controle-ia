"""Banc de mutations du plancher v3, v5 : corrections du dernier tour (contre-lecture courte des corrections, R-2311 :
CLC-P3-02, CLC-P3-03, CLC-P3-06), au commit du dernier tour. Même méthode que la v1 (R-2246 : copies de `src/`, `-o pythonpath=`,
`PYTHONPATH=<copie>/src:<arbre>/tests:<greffon>`, `--rootdir` et `-c` de l'arbre, import tracé, copie saine d'abord), deux
différences : **aucune copie n'est retirée** (consigne R-2311 : pas de suppression récursive ; copies laissées sous
`copies/<id>`, un dossier neuf par passage, refus si le dossier existe) et `--basetemp` neuf dans le bac à sable pour chaque
passage. Les mutations c14 et c17 (tenues par le seul miroir au v3) sont rejouées contre les seuls essais de comportement
(`test_t07_plancher_v3_comportement_v1.py`, sans miroir).

    python -I banc_mutations_plancher_v3_v5.py ARBRE SORTIE.json
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
PY = "/home/user/controle-ia-travail/.venv/bin/python"
T_NOT, T_RX, T_LEC, T_AO, T_CO = (f"tests/test_t07_plancher_v3_{n}_v1.py" for n in ("notation", "reextraction", "lecture",
                                                                                     "avant_ouverture", "comportement"))
TOUS = [T_NOT, T_RX, T_LEC, T_AO, T_CO]
RX, L4, RT = (f"src/controle_ia/t07/{n}.py" for n in ("reextraction_p3_v1", "lecture_v4", "repli_etapes_v2"))
NEUFS = ("plancher_v3", "reextraction_p3_v1", "lecture_v4", "passe_blanc_v2", "repli_etapes_v2")
INVITES = "docs/sources/invites-2606.08892-v1"
REELS = ("runs/20261019-230011-p3-reel", "diag/20261019-230011-p3-reel", "donnees/20261019-230011-p3-reel")

MUTATIONS = [
    # CLC-P3-03 : revision_au_cache
    ("x3", "cache : nom du dossier non comparé à la révision", RX, "    if dossier.name != revision:", "    if False:", [T_AO]),
    ("k1", "cache : fautes de l'index hors garde (aucune attrapée)", RX,
     "        except (OSError, ValueError, KeyError, TypeError) as e:", "        except () as e:", [T_AO]),
    ("k2", "cache : weight_map vide admise", RX, "            if not isinstance(carte, dict) or not carte:",
     "            if not isinstance(carte, dict):", [T_AO]),
    ("k3", "cache : morceaux sans index admis", RX, "    if nommes and not index.is_file():", "    if False:", [T_AO]),
    ("k4", "cache : nombre de morceaux non comparé", RX,
     "        if len(annonces) > 1 or (annonces and len(attendus) != annonces.pop()):", "        if False:", [T_AO]),
    ("k5", "cache : nombres annoncés mêlés admis", RX, "        if len(annonces) > 1 or (annonces and", "        if (annonces and", [T_AO]),
    ("k6", "cache : tailles nulles admises", RX, '    manquants += [f"{x} (taille nulle)" for x in', '    manquants += [] and [f"{x} (taille nulle)" for x in', [T_AO]),
    ("k7", "cache : index jamais lu", RX, "    if index.is_file():\n        try:", "    if False:\n        try:", [T_AO]),
    # CLC-P3-06 : contrôle avant l'ouverture
    ("x8", "contrôle : sonde figée absente du fichier léger admise", RX,
     '        if nom not in par:\n            raise GardeArret(f"sonde figée {nom} absente du fichier léger")\n', "", [T_AO]),
    ("x9", "contrôle : aucune sonde figée nommée admise", RX,
     '    if not figees:\n        raise GardeArret("aucune sonde figée de P3 nommée', '    if False:\n        raise GardeArret("aucune sonde figée de P3 nommée', [T_AO]),
    # CLC-P3-02 : sous-commande controle-avant-ouverture
    ("p1", "sous-commande non aiguillée", L4, '    if argv and argv[0] == "controle-avant-ouverture":', "    if False:", [T_AO]),
    ("p2", "sous-commande sans le contrôle de la réextraction", L4,
     "        r = rx.controler_avant_ouverture(Path(a.racine), config, a.cache_dir)", '        r = {"figees": {}, "modele_p3": {}}', [T_AO]),
    ("p3", "sous-commande : fautes hors garde non attrapées", L4, "    except rx.FAUTES_DU_BRAS as err:", "    except ZeroDivisionError as err:", [T_AO]),
    ("p4", "sous-commande : cache désigné ignoré", L4, "rx.controler_avant_ouverture(Path(a.racine), config, a.cache_dir)",
     "rx.controler_avant_ouverture(Path(a.racine), config)", [T_AO]),
    ("p5", "sous-commande : configuration lue sans les contrôles de la v4", L4,
     "        config = charger_configuration(Path(a.config_t07))\n        r = rx.controler",
     '        config = json.loads(Path(a.config_t07).read_text(encoding="utf-8"))\n        r = rx.controler', [T_AO]),
    ("p6", "sous-commande : refus rendu en code 0", L4,
     "        print(f\"REFUS : contrôle avant l'ouverture : {err}\", file=sys.stderr)\n        return CODE_REFUS",
     "        print(f\"REFUS : contrôle avant l'ouverture : {err}\", file=sys.stderr)\n        return CODE_OK", [T_AO]),
    ("p7", "sous-commande : résumé non écrit", L4, "    print(json.dumps(r, ensure_ascii=False, sort_keys=True))\n    return CODE_OK",
     "    return CODE_OK", [T_AO]),
    # CLC-P3-06 : notes 05 et 10, sans le miroir
    ("c14", "note 05 : appel retiré de etape_b (essais de comportement seuls)", L4,
     "            exiger_nombre_de_directions(t, index, config)        # note 05", "            pass        # note 05", [T_CO]),
    ("c17", "note 10 : état des figées non affiché après le repli (essais de comportement seuls)", RT,
     "sondes lues {r['index']['sondes_lues']} ; plancher des \"", "sondes lues {r['index']['sondes_lues']} ; \"", [T_CO]),
    ("c17b", "note 10 : état des figées non affiché par etape-a (essais de comportement seuls)", L4,
     "sondes lues {r['index']['sondes_lues']} ; plancher des \"", "sondes lues {r['index']['sondes_lues']} ; \"", [T_CO]),
]


def copier(arbre: Path, copie: Path) -> None:
    if copie.exists():
        raise SystemExit(f"{copie} existe déjà : rien n'est écrasé ni retiré (R12, R-2311)")
    shutil.copytree(arbre / "src", copie / "src")
    shutil.copytree(arbre / INVITES, copie / INVITES)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def jouer(arbre: Path, copie: Path, essais: list, trace: Path, basetemp: Path) -> dict:
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH",)}
    env.update(PYTHONPATH=f"{copie}/src:{arbre}/tests:{ICI / 'greffon'}", TRACE_IMPORT_SORTIE=str(trace), OPENBLAS_NUM_THREADS="1",
               PYTHONDONTWRITEBYTECODE="1")
    t0 = time.perf_counter()
    p = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-o", "pythonpath=", "--rootdir", str(arbre),
                        "-c", str(arbre / "pyproject.toml"), f"--basetemp={basetemp}", "-p", "trace_import_plancher_v3",
                        *[str(arbre / e) for e in essais]], cwd=arbre, env=env, capture_output=True, text=True)
    dernieres = [l for l in p.stdout.splitlines() if l.strip()][-3:]
    tue_par = next((l.split(" ")[1] for l in p.stdout.splitlines() if l.startswith("FAILED ") or l.startswith("ERROR ")), None)
    return {"code": p.returncode, "duree_s": round(time.perf_counter() - t0, 1), "fin": dernieres, "tue_par": tue_par,
            "trace": json.loads(trace.read_text()) if trace.exists() else None}


def main(arbre: Path, sortie: Path) -> int:
    base, bt = ICI / "copies", ICI / "basetemp"
    base.mkdir(exist_ok=True)
    bt.mkdir(exist_ok=True)
    res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "arbre": str(arbre),
           "commit": subprocess.run(["git", "-C", str(arbre), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
           "reels_p3_presents": all((arbre / r).is_dir() for r in REELS), "mutations": []}
    saine = base / "saine"
    copier(arbre, saine)
    r = jouer(arbre, saine, TOUS, base / "trace-saine.json", bt / "saine")
    neufs = {n: str((saine / f"src/controle_ia/t07/{n}.py").resolve()) for n in NEUFS}
    r["import_de_la_copie"] = bool(r["trace"]) and all(r["trace"]["modules"].get(n, {}).get("chemin") == c for n, c in neufs.items())
    res["saine"] = r
    print("saine", r["code"], r["import_de_la_copie"], r["fin"], flush=True)
    if r["code"] != 0 or not r["import_de_la_copie"]:
        sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return 1
    for mid, quoi, fichier, ancien, nouveau, essais in MUTATIONS:
        copie = base / mid
        copier(arbre, copie)
        f = copie / fichier
        texte = f.read_text(encoding="utf-8")
        n = texte.count(ancien)
        if n != 1:
            res["mutations"].append({"id": mid, "quoi": quoi, "erreur": f"motif trouvé {n} fois"})
            print(mid, "MOTIF", n, flush=True)
            continue
        f.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        r = jouer(arbre, copie, essais, base / f"trace-{mid}.json", bt / mid)
        nom = Path(fichier).stem
        tr = (r["trace"] or {}).get("modules", {}).get(nom, {})
        r.update(id=mid, quoi=quoi, fichier=fichier, essais=essais, sha256_mute=sha(f),
                 import_de_la_copie=tr.get("chemin") == str(f.resolve()) and tr.get("sha256") == sha(f),
                 issue="tuée" if r["code"] != 0 else "survit")
        res["mutations"].append(r)
        print(mid, r["issue"], r["tue_par"], r["import_de_la_copie"], r["duree_s"], flush=True)
    res["fin"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    res["resume"] = {"mutations": len(MUTATIONS), "tuees": sum(1 for m in res["mutations"] if m.get("issue") == "tuée"),
                     "survivantes": [m["id"] for m in res["mutations"] if m.get("issue") == "survit"],
                     "motifs_introuvables": [m["id"] for m in res["mutations"] if "erreur" in m],
                     "imports_hors_copie": [m["id"] for m in res["mutations"] if m.get("issue") and not m.get("import_de_la_copie")]}
    sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["resume"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
