"""Banc de mutation des quatre changements du noyau de la v8 (trois corrections et le contrat ; étendu de trois à quatre
mutants, R-402, avant tout versement) : R-395 (arrêt sur crédit épuisé rendu en 400), R-396 (import de la
réponse à la question dans la vue du bras apparié), R-398 (le contrat dit la réflexion comprise dans `max_tokens`), R-402 (types de blocs au journal des appels).
Décliné de `muter_r395_r396_v1.py`. Usage : python -I -B muter_v8_v1.py SRC SORTIE_TMP COLLISIONNEUR"""
import os, pathlib, shutil, subprocess, sys
SRC, OUT, COLL = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
MUT = [
 ("temoin", None, None, None, "test_r395_credit_epuise_rendu_en_400_arrete_la_course or test_r396_import_conception_recopie_la_reponse_a_la_question_dans_la_vue or test_r398_contrat_dit_la_reflexion_comprise_dans_max_tokens or test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait"),
 ("r395-credit-400", "essaim_m3/noyau/appels.py", "if self.credit_epuise is None and credit_epuise(rep.echec):",
  'if self.credit_epuise is None and re.match(r"\\s*HTTP 402\\b", str(rep.echec)):  # mutation R-395', "test_r395_credit_epuise_rendu_en_400_arrete_la_course"),
 ("r396-import-reponse", "essaim_m3/noyau/archive.py", 'for nom in ("organisme.tar.gz", "organisme.tar.gz.sha256", "reponse-question.md"):',
  'for nom in ("organisme.tar.gz", "organisme.tar.gz.sha256"):  # mutation R-396', "test_r396_import_conception_recopie_la_reponse_a_la_question_dans_la_vue"),
 ("r398-reflexion-comprise", "essaim_m3/noyau/contrat.py", "     Réflexion comprise : les espèces Anthropic",
  "     Réflexion : les espèces Anthropic", "test_r398_contrat_dit_la_reflexion_comprise_dans_max_tokens"),
 ("r402-types-blocs", "essaim_m3/noyau/appels.py", '"types_blocs": [str(x)[:40] for x in (getattr(rep, "types_blocs", None) or [])][:20],',
  '"types_blocs": [],  # mutation R-402', "test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait"),
]
OUT.mkdir(parents=True, exist_ok=True)
for nom, fichier, avant, apres, essai in MUT:
    copie = OUT / nom
    if copie.exists(): shutil.rmtree(copie)
    shutil.copytree(SRC, copie, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", ".git"))
    if fichier:
        f = copie / fichier; t = f.read_text()
        if t.count(avant) != 1:
            print(f"{nom}: MOTIF {t.count(avant)} fois — non appliquée"); continue
        f.write_text(t.replace(avant, apres))
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests/test_noyau.py", "-k", essai],
                       cwd=copie, capture_output=True, text=True, timeout=900,
                       env=dict(os.environ, ESSAIM_M3_COLLISIONNEUR=COLL, PATH="/usr/bin:/bin", HOME=str(copie / "_home"), LANG="C.UTF-8"))
    fin = (r.stdout.strip().splitlines() or ["?"])[-1]
    attendu = r.returncode == 0 if nom == "temoin" else r.returncode != 0
    print(f"{nom:22s}: {'conforme' if attendu else 'NON CONFORME'} (code {r.returncode}) — {fin}")
    shutil.rmtree(copie)
