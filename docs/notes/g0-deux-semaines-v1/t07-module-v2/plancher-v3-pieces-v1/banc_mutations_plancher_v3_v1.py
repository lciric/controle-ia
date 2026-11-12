"""Banc de mutations du code du plancher v3 de T0.7 (consigne `consigne-code-plancher-v3-t07-v1.md`, point 4), v1.

Méthode de R-2246 : chaque mutation est appliquée à une **copie** de `src/` (jamais dans l'arbre) ; les essais visés sont joués
avec `-o pythonpath=` (le `pythonpath` de `pyproject.toml`, qui met `src` d'abord, neutralisé), `PYTHONPATH=<copie>/src:<arbre>/tests:
<greffon>`, `--rootdir` et `-c` de l'arbre ; le greffon `trace_import_plancher_v3` écrit le chemin et l'empreinte des modules neufs
réellement importés : chacun doit venir de la copie, le fichier muté à son empreinte mutée. Copie saine d'abord (tout passe).

    python -I banc_mutations_plancher_v3_v1.py ARBRE SORTIE.json
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
T_NOT, T_RX, T_LEC = ("tests/test_t07_plancher_v3_notation_v1.py", "tests/test_t07_plancher_v3_reextraction_v1.py",
                      "tests/test_t07_plancher_v3_lecture_v1.py")
P3, RX, L4, PB, RT = (f"src/controle_ia/t07/{n}.py" for n in ("plancher_v3", "reextraction_p3_v1", "lecture_v4", "passe_blanc_v2",
                                                              "repli_etapes_v2"))
MUTATIONS = [
    ("m1", "contrôle en ligne retiré", P3, "    if int(controle) > 0:\n        controler_contre_la_boucle(", "    if False:\n        controler_contre_la_boucle(", [T_NOT]),
    ("m2", "tolérance vectorisée relâchée à 1e-6", P3, "TOLERANCE_VECTORISEE = 1e-12", "TOLERANCE_VECTORISEE = 1e-6", [T_NOT]),
    ("m3", "moyenne au lieu du maximum", P3, "    return np.maximum.reduceat(S, bornes[:-1], axis=0)",
     "    return np.add.reduceat(S, bornes[:-1], axis=0) / np.diff(bornes)[:, None]", [T_NOT]),
    ("m4", "attention sans soustraction du maximum", P3, "        poids = np.exp(lt - lt.max(axis=1, keepdims=True))", "        poids = np.exp(lt)", [T_NOT]),
    ("m5", "biais oublié", P3, '        S = A @ m["W"] + m["b"]', '        S = A @ m["W"]', [T_NOT]),
    ("m6", "dernier lot perdu", P3, "    if total:\n        yield debut, len(longueurs)", "    if False:\n        yield debut, len(longueurs)", [T_NOT]),
    ("m7", "N_PLANCHER_REEL = 200", P3, "N_PLANCHER_REEL = 800 ", "N_PLANCHER_REEL = 200 ", [T_NOT, T_LEC]),
    ("m8", "agrégations mêlées admises", P3, "    if len(agregations) != 1:\n        raise", "    if False:\n        raise", [T_NOT]),
    ("m9", "empan vide admis", P3, "        if s.shape[0] < 1:\n            raise", "        if False:\n            raise", [T_NOT]),
    ("m10", "attention : somme hors de l'axe contigu", P3, "        sortie[j] = np.sum(poids * st, axis=1)",
     "        sortie[j] = (poids * st).T.sum(axis=0)", [T_NOT]),
    ("m11", "palier processeur relâché (5e-3)", RX, '"processeur": 1e-6, "carte_sonde"', '"processeur": 5e-3, "carte_sonde"', [T_RX]),
    ("m12", "palier carte du témoin à 0,9", RX, '"carte_sonde": 1e-2,', '"carte_sonde": 0.9,', [T_RX]),
    ("m13", "témoin non décisif", RX, '        decisifs = [v["garde_identite"]["palier"]]', "        decisifs = []", [T_RX]),
    ("m14", "seconde garde non décisive", RX, '            decisifs.append(gd["palier"])', "            pass", [T_RX]),
    ("m15", "principale « decisive » ignorée", RX, '            if mode_principale == "decisive":\n                decisifs.append(p)',
     "            if False:\n                decisifs.append(p)", [T_RX]),
    ("m16", "garde d'identité sans effet (bascule)", RX, '        if "échec" in decisifs:\n            raise GardeArret(',
     '        if "échec" in decisifs and False:\n            raise GardeArret(', [T_RX]),
    ("m17", "graine de P3 au lieu de celle de T0.7", RX, "int(s.couche), j[\"seqs\"], s.agregation, int(n_plancher), graine_de(cle))",
     "int(s.couche), j[\"seqs\"], s.agregation, int(n_plancher), _graine_p3(p3, f\"plancher/{c}\"))", [T_RX]),
    ("m18", "réglages de torch non rétablis", RX, '        torch.use_deterministic_algorithms(avant["det"])', "        pass", [T_RX]),
    ("m19", "faits exclus non contrôlés", RX, '    if list(exclus) != list(r["donnees"]["faits_exclus"]):', "    if False:", [T_RX]),
    ("m20", "effectifs non contrôlés", RX, '        if (len(idx_e), len(idx_v)) != (int(attendu["entrainement"]), int(attendu["validation"])):',
     "        if False:", [T_RX]),
    ("m21", "n_plancher ignoré (200)", RX, "int(s.couche), j[\"seqs\"], s.agregation, int(n_plancher), graine_de(cle))",
     "int(s.couche), j[\"seqs\"], s.agregation, 200, graine_de(cle))", [T_RX]),
    ("m22", "réglages de P3 non posés", RX, "        r = regler_determinisme(int(fils), appareil)", '        r = {"deterministe": False}', [T_RX]),
    ("m23", "principale autre admise", RX, '            if c not in CONCEPTS_P3 or p3["resultat"]["principales"].get(c) != s.nom:', "            if False:", [T_RX]),
    ("m24", "n_plancher libre en mode réel", L4, "        if isinstance(n, bool) or not isinstance(n, int) or n != pl3.N_PLANCHER_REEL:", "        if False:", [T_LEC]),
    ("m25", "donnees_p3 nulle admise en mode réel", L4, '        if config.get("donnees_p3") is None:', "        if False:", [T_LEC]),
    ("m26", "directions de P3 comptées sur n_plancher", L4, '{**config, "n_plancher": int(config[rx.CLE_CONFIG]["n_p3"])}', "config", [T_LEC]),
    ("m27", "bascule vers les 200 de P3 à l'échec", L4,
     '                         for n, x in reextraction["par_sonde"].items() if x["etat"] != "établi"}\n        planchers_p3 = {**planchers_figees, **planchers_neufs}\n',
     '                         for n, x in reextraction["par_sonde"].items() if False}\n        planchers_p3 = {**descriptifs_p3, **planchers_figees, **planchers_neufs}\n', [T_LEC]),
    ("m28", "planchers notés par la boucle", L4, 'tableaux[f"plancher_{k}"] = pl3.scores_plancher_vectorises(plancher, seqs).T',
     'tableaux[f"plancher_{k}"] = pl.scores_plancher(plancher, seqs).T', [T_LEC]),
    ("m29", "lecture descriptive des directions de P3 absente", L4, '    entrees = [e for e in index["sondes"] if e.get("plancher_p3")]', "    entrees = []", [T_LEC]),
    ("m30", "graines des figées hors du manifeste", L4, '+ [f"plancher/{n}" for n in connus]   # v4', '+ [f"plancher/{n}" for n in neuves]   # v4', [T_LEC]),
    ("m31", "passe à blanc sous la configuration de la v2", PB, "    from .lecture_v4 import exiger_configuration\n", "    from .lecture_v2 import exiger_configuration\n", [T_LEC]),
    ("m32", "repli sous la configuration de la v2", RT, "    from .lecture_v4 import exiger_configuration\n", "    from .lecture_v2 import exiger_configuration\n", [T_LEC]),
]


INVITES = "docs/sources/invites-2606.08892-v1"          # lues par chemin relatif au module (`environnements.invites`)


def copier(arbre: Path, copie: Path) -> None:
    shutil.copytree(arbre / "src", copie / "src")
    shutil.copytree(arbre / INVITES, copie / INVITES)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def jouer(arbre: Path, copie: Path, essais: list, trace: Path) -> dict:
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH",)}
    env.update(PYTHONPATH=f"{copie}/src:{arbre}/tests:{ICI / 'greffon'}", TRACE_IMPORT_SORTIE=str(trace), OPENBLAS_NUM_THREADS="1",
               PYTHONDONTWRITEBYTECODE="1")
    t0 = time.perf_counter()
    p = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-o", "pythonpath=", "--rootdir", str(arbre),
                        "-c", str(arbre / "pyproject.toml"), "-p", "trace_import_plancher_v3", *[str(arbre / e) for e in essais]],
                       cwd=arbre, env=env, capture_output=True, text=True)
    dernieres = [l for l in p.stdout.splitlines() if l.strip()][-3:]
    tue_par = next((l.split(" ")[1] for l in p.stdout.splitlines() if l.startswith("FAILED ")), None)
    return {"code": p.returncode, "duree_s": round(time.perf_counter() - t0, 1), "fin": dernieres, "tue_par": tue_par,
            "trace": json.loads(trace.read_text()) if trace.exists() else None}


def main(arbre: Path, sortie: Path) -> int:
    base = ICI / "copies"
    base.mkdir(exist_ok=True)
    res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "arbre": str(arbre), "mutations": []}
    saine = base / "saine"
    if saine.exists():
        shutil.rmtree(saine)
    copier(arbre, saine)
    r = jouer(arbre, saine, [T_NOT, T_RX, T_LEC], base / "trace-saine.json")
    neufs = {n: str((saine / f"src/controle_ia/t07/{n}.py").resolve()) for n in ("plancher_v3", "reextraction_p3_v1", "lecture_v4",
                                                                                 "passe_blanc_v2", "repli_etapes_v2")}
    r["import_de_la_copie"] = bool(r["trace"]) and all(r["trace"]["modules"].get(n, {}).get("chemin") == c for n, c in neufs.items())
    res["saine"] = r
    print("saine", r["code"], r["import_de_la_copie"], r["fin"], flush=True)
    shutil.rmtree(saine)
    if r["code"] != 0 or not r["import_de_la_copie"]:
        sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return 1
    for mid, quoi, fichier, ancien, nouveau, essais in MUTATIONS:
        copie = base / mid
        if copie.exists():
            shutil.rmtree(copie)
        copier(arbre, copie)
        f = copie / fichier
        texte = f.read_text(encoding="utf-8")
        n = texte.count(ancien)
        if n != 1:
            res["mutations"].append({"id": mid, "quoi": quoi, "erreur": f"motif trouvé {n} fois"})
            print(mid, "MOTIF", n, flush=True)
            shutil.rmtree(copie)
            continue
        f.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        r = jouer(arbre, copie, essais, base / f"trace-{mid}.json")
        nom = Path(fichier).stem
        tr = (r["trace"] or {}).get("modules", {}).get(nom, {})
        r.update(id=mid, quoi=quoi, fichier=fichier, essais=essais, sha256_mute=sha(f),
                 import_de_la_copie=tr.get("chemin") == str(f.resolve()) and tr.get("sha256") == sha(f),
                 issue="tuée" if r["code"] != 0 else "survit")
        res["mutations"].append(r)
        print(mid, r["issue"], r["tue_par"], r["import_de_la_copie"], r["duree_s"], flush=True)
        shutil.rmtree(copie)
    res["fin"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    res["resume"] = {"mutations": len(MUTATIONS), "tuees": sum(1 for m in res["mutations"] if m.get("issue") == "tuée"),
                     "survivantes": [m["id"] for m in res["mutations"] if m.get("issue") == "survit"],
                     "imports_hors_copie": [m["id"] for m in res["mutations"] if m.get("issue") and not m.get("import_de_la_copie")]}
    sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["resume"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
