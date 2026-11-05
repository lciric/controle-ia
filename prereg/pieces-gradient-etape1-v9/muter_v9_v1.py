"""Banc de mutation des corrections de la v9 : R-415 (clé OpenAlex en paramètre de la requête ; valeur masquée dans les
messages d'échec ; parité) et R-417 (clé Semantic Scholar en en-tête ; parité). Décliné de `muter_v8_v1.py`. Usage : python -I -B muter_v9_v1.py SRC SORTIE_TMP COLLISIONNEUR"""
import os, pathlib, shutil, subprocess, sys
SRC, OUT, COLL = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
E415 = "test_r415_cle_openalex_lue_par_le_noyau_masquee_et_appariee"
E417 = "test_r417_cle_semantic_scholar_en_en_tete_masquee_et_appariee"
MUT = [
 ("temoin", None, None, None, E415 + " or " + E417),
 ("r415-api-key", "essaim_m3/noyau/moisson.py", '        params["api_key"] = cle', '        pass  # mutation R-415', E415),
 ("r415-masquage", "essaim_m3/noyau/recherche.py", 'masquer_cles(f"{type(e).__name__}: {e}")[:200]', 'f"{type(e).__name__}: {e}"[:200]  # mutation R-415', E415),
 ("r415-parite", "essaim_m3/noyau/cli.py", '    if "cle_openalex_presente" in m and bool(m["cle_openalex_presente"]) != openalex:', '    if False:  # mutation R-415', E415),
 ("r417-en-tete", "essaim_m3/noyau/moisson.py", 'entetes=({"x-api-key": cle} if cle else None)', 'entetes=None', E417),
 ("r417-parite", "essaim_m3/noyau/cli.py", '    if "cle_semanticscholar_presente" in m and bool(m["cle_semanticscholar_presente"]) != s2:', '    if False:  # mutation R-417', E417),
]
OUT.mkdir(parents=True, exist_ok=True)
for nom, fichier, avant, apres, ESSAI in MUT:
    copie = OUT / nom
    if copie.exists(): shutil.rmtree(copie)
    shutil.copytree(SRC, copie, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", ".git"))
    if fichier:
        f = copie / fichier; t = f.read_text()
        if t.count(avant) != 1:
            print(f"{nom}: MOTIF {t.count(avant)} fois — non appliquée"); continue
        f.write_text(t.replace(avant, apres))
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests/test_noyau.py", "-k", ESSAI],
                       cwd=copie, capture_output=True, text=True, timeout=900,
                       env=dict(os.environ, ESSAIM_M3_COLLISIONNEUR=COLL, PATH="/usr/bin:/bin", HOME=str(copie / "_home"), LANG="C.UTF-8"))
    fin = (r.stdout.strip().splitlines() or ["?"])[-1]
    attendu = r.returncode == 0 if nom == "temoin" else r.returncode != 0
    print(f"{nom:22s}: {'conforme' if attendu else 'NON CONFORME'} (code {r.returncode}) — {fin}")
    shutil.rmtree(copie)
