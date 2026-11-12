"""Banc de mutations de la contre-lecture courte (CLC-P3) : méthode de R-2246, une seule copie de `src/` (mutée puis rétablie,
empreinte comparée à l'arbre), essais de l'arbre, `-o pythonpath=`, import tracé. Aucune suppression récursive.

    python -I banc_cl2.py ARBRE COPIE SORTIE.json [id ...]
"""
import hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path

PY = "/home/user/controle-ia-travail/.venv/bin/python"
ICI = Path(__file__).resolve().parent
T_RX, T_LEC = "tests/test_t07_plancher_v3_reextraction_v1.py", "tests/test_t07_plancher_v3_lecture_v1.py"
RX, L4, PB, RT = (f"src/controle_ia/t07/{n}.py" for n in ("reextraction_p3_v1", "lecture_v4", "passe_blanc_v2", "repli_etapes_v2"))
INVITES = "docs/sources/invites-2606.08892-v1"
SANS = "not miroir"
M = [
    # les trois survivantes de la première contre-lecture, rejouées avec puis sans le miroir
    ("n34", "lecture descriptive de P3 écrite dans les scores décisifs", L4, '    t2, idx2, absentes = dict(t), {"sondes": []}, {}', '    t2, idx2, absentes = t, {"sondes": []}, {}', [T_LEC], None),
    ("n34-sm", "n34 sans le miroir", L4, '    t2, idx2, absentes = dict(t), {"sondes": []}, {}', '    t2, idx2, absentes = t, {"sondes": []}, {}', [T_LEC], SANS),
    ("n25c", "palier global = le meilleur des paliers", RX, '        v["palier"] = max(decisifs, key=PALIERS.index)', '        v["palier"] = min(decisifs, key=PALIERS.index)', [T_RX], None),
    ("n28", "reserve_principale non recopiée à l'étape B", L4, '        for cle in ("reserve", "reserve_principale"):', '        for cle in ("reserve",):', [T_LEC], None),
    ("n28-sm", "n28 sans le miroir", L4, '        for cle in ("reserve", "reserve_principale"):', '        for cle in ("reserve",):', [T_LEC], SANS),
    # mutations du développeur tuées par le seul miroir : rejouées sans lui
    ("c12-sm", "passe à blanc sans contrôle de la réextraction, sans le miroir", PB, "        reextraction_p3 = controler_avant_ouverture(racine, config)\n", "        reextraction_p3 = None\n", [T_LEC], SANS),
    ("c14-sm", "nombre de directions non exigé (appel), sans le miroir", L4, "            exiger_nombre_de_directions(t, index, config)        # note 05", "            pass        # note 05", [T_LEC], SANS),
    ("c17-sm", "état des figées non affiché, sans le miroir", RT, "sondes lues {r['index']['sondes_lues']} ; plancher des \"", "sondes lues {r['index']['sondes_lues']} ; \"", [T_LEC], SANS),
    # mutations neuves
    ("x1", "note 05 : tableau non contrôlé (index seul)", L4, "        if m is None or int(m.shape[0]) != n or int(", "        if int(", [T_LEC], None),
    ("x2", "AttributeError et IndexError hors des fautes du bras", RX, "MemoryError, TypeError, AttributeError, IndexError)", "MemoryError, TypeError)", [T_RX], None),
    ("x3", "cache : nom du dossier non comparé à la révision", RX, "    if dossier.name != revision:\n", "    if False:\n", [T_RX], None),
    ("x4", "contrôle avant l'ouverture : principales non comparées", RX, "        if p3[\"resultat\"][\"principales\"].get(c) != nom:\n            raise GardeArret(f\"sonde figée {nom} ({c}) : principale", "        if False:\n            raise GardeArret(f\"sonde figée {nom} ({c}) : principale", [T_RX], None),
    ("x5", "contrôle avant l'ouverture : sceaux de P3 non lus (lire_p3 sans controle)", RX, "    fichiers = d3.controler(racine, d)\n", "    fichiers = {}\n", [T_RX], None),
    ("x6", "cache : sans index, absence de poids admise", RX, "    elif not poids:\n        manquants.append(\"*.safetensors\")", "    elif False:\n        manquants.append(\"*.safetensors\")", [T_RX], None),
    ("x7", "passe à blanc : refus du contrôle avalé", PB, "        raise RefusPasse(f\"réextraction des jetons de P3 non jouable (CLP3-03) : {e}\") from None", "        reextraction_p3 = {\"etat\": str(e)}", [T_LEC], SANS),
    ("x8", "contrôle avant l'ouverture : sonde figée absente du fichier léger admise", RX, "        if nom not in par:\n            raise GardeArret(f\"sonde figée {nom} absente du fichier léger\")\n", "", [T_RX], None),
    ("x9", "contrôle avant l'ouverture : aucune sonde figée admise", RX, "    if not figees:\n        raise GardeArret(\"aucune sonde figée de P3 nommée par la configuration\")\n", "", [T_RX], None),
    ("x10", "note 05 : n_plancher de l'index non contrôlé", L4, "    if int(index.get(\"n_plancher\", -1)) != n:\n", "    if False:\n", [T_LEC], None),
    ("x11", "note 05 : nombre écrit non contrôlé", L4, " or int((e.get(\"plancher\") or {}).get(\"n\", -1)) != n:", ":", [T_LEC], None),
]

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def jouer(arbre, copie, essais, trace, k, tmp):
    env = {x: v for x, v in os.environ.items() if x != "PYTHONPATH"}
    env.update(PYTHONPATH=f"{copie}/src:{arbre}/tests:{ICI.parent / 'greffon'}", TRACE_IMPORT_SORTIE=str(trace), OPENBLAS_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
    if trace.exists():
        trace.unlink()
    cmd = [PY, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-o", "pythonpath=", "--rootdir", str(arbre), "-c", str(arbre / "pyproject.toml"),
           "-p", "trace_import_plancher_v3", f"--basetemp={tmp}", *[str(arbre / e) for e in essais]]
    if k:
        cmd += ["-k", k]
    t0 = time.perf_counter()
    p = subprocess.run(cmd, cwd=arbre, env=env, capture_output=True, text=True)
    return {"code": p.returncode, "duree_s": round(time.perf_counter() - t0, 1), "fin": [l for l in p.stdout.splitlines() if l.strip()][-1:],
            "tue_par": [l.split(" ")[1] for l in p.stdout.splitlines() if l.startswith("FAILED ")],
            "trace": json.loads(trace.read_text()) if trace.exists() else None}

def main(arbre, copie, sortie, ids):
    if not copie.exists():
        shutil.copytree(arbre / "src", copie / "src"); shutil.copytree(arbre / INVITES, copie / INVITES)
    res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "mutations": []}
    tmp = copie.parent / "pytest-tmp-banc"
    for mid, quoi, fichier, ancien, nouveau, essais, k in M:
        if ids and mid not in ids:
            continue
        f = copie / fichier
        assert sha(f) == sha(arbre / fichier), f"copie non saine avant {mid}"
        texte = f.read_text(encoding="utf-8")
        if texte.count(ancien) != 1:
            print(mid, "MOTIF", texte.count(ancien), flush=True); res["mutations"].append({"id": mid, "erreur": "motif"}); continue
        f.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        mute = sha(f)
        try:
            r = jouer(arbre, copie, essais, copie.parent / f"trace-{mid}.json", k, tmp)
        finally:
            f.write_text(texte, encoding="utf-8")
        assert sha(f) == sha(arbre / fichier)
        tr = (r["trace"] or {}).get("modules", {}).get(Path(fichier).stem, {})
        r.update(id=mid, quoi=quoi, fichier=fichier, k=k, sha256_mute=mute, import_de_la_copie=tr.get("chemin") == str(f.resolve()) and tr.get("sha256") == mute,
                 issue="tuée" if r["code"] != 0 else "survit")
        res["mutations"].append(r)
        print(time.strftime("%H:%M:%S", time.gmtime()), mid, r["issue"], r["tue_par"][:3], r["import_de_la_copie"], r["duree_s"], r["fin"], flush=True)
        sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), sys.argv[4:]))
