"""CL11 : six défauts réintroduits dans le code neuf de la v44 ; chacun sur une copie neuve, essais de test_v7_ideation."""
import json, os, shutil, subprocess, sys
SRC, BASE = sys.argv[1], sys.argv[2]
M = {
 "M1-taille-donnee-desarme-la-provision": ("pole/ideation.py", "    if taille_donnee is not None and taille_donnee < propre:\n", "    if taille_donnee is not None:\n"),
 "M2-reprise-claude-jamais-rejouee": ("demonstrations/ideation_v1.py", "        elif actuelle < float(avant) - 1e-9:\n", "        elif False:\n"),
 "M3-somme-externe-passe-2-au-plafond-de-passe-1": ("pole/ideation.py", "        + sum(plafond_passe_externe(budgets, m, n, budget_passe_2_externe_usd)  # v44 (CL43-01) : passe 2 à son plafond\n", "        + sum(plafond_passe_externe(budgets, m, 1)\n"),
 "M4-provision-passe-2-sans-les-grandes-fiches": ("pole/ideation.py", "                taille_fiche = max([TAILLE_FICHE_PROVISIONNEE_PASSE] + [taille_servie(f) for f in admises])\n", "                taille_fiche = TAILLE_FICHE_PROVISIONNEE_PASSE\n"),
 "M5-passe-1-non-gardee-avant-les-controles": ("demonstrations/ideation_v1.py", "                                          garder_passes=True)  # v44 (CL43-02) : passe 1 gardée avant tout contrôle\n", "                                          garder_passes=False)\n"),
 "M6-passerait-passe-1-toujours-vrai": ("demonstrations/ideation_v1.py", "\"origine\": o1, \"passerait\": m[\"consigne_passe_1\"] <= t1,", "\"origine\": o1, \"passerait\": True,"),
}
procs = {}
for nom, (f, a, b) in M.items():
    d = os.path.join(BASE, nom); shutil.copytree(SRC, d)
    p = os.path.join(d, f); t = open(p, encoding="utf-8").read()
    assert t.count(a) == 1, (nom, t.count(a)); open(p, "w", encoding="utf-8").write(t.replace(a, b))
    procs[nom] = subprocess.Popen(["python3", "-B", "-m", "unittest", "essais.test_v7_ideation"], cwd=d,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env={"PATH": "/usr/bin:/bin", "HOME": "/tmp"})
res = {}
for nom, p in procs.items():
    out = p.communicate()[0].decode()
    res[nom] = {"code": p.returncode, "verdict": "tué" if p.returncode else "SURVIT",
                "fin": [l for l in out.splitlines() if l.startswith(("Ran", "FAILED", "OK"))],
                "echecs": [l for l in out.splitlines() if l.startswith(("FAIL:", "ERROR:"))][:6]}
    print(nom, json.dumps(res[nom], ensure_ascii=False))
json.dump(res, open(os.path.join(BASE, "mutants.json"), "w"), ensure_ascii=False, indent=1)
