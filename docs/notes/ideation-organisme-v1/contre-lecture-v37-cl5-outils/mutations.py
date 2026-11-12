"""Essais de mutation de la relecture CL5 (v36 -> v37) : chaque mutation réintroduit un défaut dans une copie neuve de
l'arbre v37, puis relance `essais.test_v7_ideation` seul. « tuée » = au moins un essai échoue ; « survit » = tout passe.
Usage : python -B mutations.py ARBRE_V37 DOSSIER_TRAVAIL [M1 M2 …]"""

import os
import shutil
import subprocess
import sys
import time

MUTATIONS = {
    # CL35-13 : groupe de processus -> processus seul
    "M1-killpg": ("pole/adaptateurs.py", "os.killpg(p.pid, signal.SIGKILL)", "p.kill()"),
    # CL36-01 : branche « non joué » retirée (retour au comportement v36)
    "M2-non-joue": ("pole/ideation.py", "if rien_envoye and not os.path.exists(chemin_manifeste):",
                    "if False and rien_envoye and not os.path.exists(chemin_manifeste):"),
    # CL36-01 : commande introuvable -> plafond compté, coût inconnu (v36)
    "M3-oserror-cout": ("pole/adaptateurs.py",
                        'return Resultat("", [], 0.0, "erreur", "commande externe non lancée ("',
                        'return Resultat("", [], plafond, "erreur", "commande externe non lancée ("'),
    # CL36-03 noyau : garde retirée
    "M4-ext-noyau-retire": ("pole/ideation.py",
                              'if moteur == "claude-sdk" and not (juges_externes and proposeurs_externes):  # v37 (CL36-03)',
                              'if False:'),
    # CL36-03 noyau : seul le proposeur externe exigé (juge externe oublié permis)
    "M5-ext-juge-oublie": ("pole/ideation.py",
                             'if moteur == "claude-sdk" and not (juges_externes and proposeurs_externes):  # v37 (CL36-03)',
                             'if moteur == "claude-sdk" and not proposeurs_externes:'),
    # CL36-03 lanceur : garde retirée
    "M6-ext-lanceur-retire": ("demonstrations/ideation_v1.py",
                                'if args.moteur == "claude-sdk" and not (prop_ext and juges_ext):  # CL36-03',
                                'if False:'),
    # CL36-02 lanceur : contrôle d'Argon proposeur retiré
    "M7-controle-ext-retire": ("demonstrations/ideation_v1.py",
                                 "for e, m in prop_ext:  # CL36-02", "for e, m in []:  # CL36-02"),
    # CL35-04 (proposeur) : un proposeur externe simulé accepté sur une course réelle
    "M8-proposeur-simule": ("pole/ideation.py",
                            'if a is None or (moteur == "claude-sdk" and getattr(a, "nom", None) != "commande-externe"):',
                            'if a is None:'),
    # v37 : plafond dur retiré
    "M9-plafond-dur": ("pole/ideation.py", "or not 1 <= taille_max_pieces <= TAILLE_MAX_PIECES_ABSOLUE:",
                       "or not 1 <= taille_max_pieces:"),
    # v37 : troncature silencieuse au lieu d'un refus
    "M10-troncature": ("pole/ideation.py",
                       'raise PieceInterdite(f"pièces trop longues ({total} caractères > {taille_max})")',
                       't = t[:max(0, len(t) - (total - taille_max))]; total = taille_max'),
    # CL36-04 : défaut Opus proposeur revenu au devis v6
    "M11-defaut-opus": ("demonstrations/ideation_v1.py", '("proposeur_ideation", "claude-opus-5-5"): 5.0',
                        '("proposeur_ideation", "claude-opus-5-5"): 2.0'),
    # CL36-05 M3 : médiane -> moyenne
    "M12-moyenne": ("pole/ideation.py", "agg = statistics.mean if nj <= 2 else statistics.median",
                    "agg = statistics.mean"),
    # CL35-14 : sceau de l'attestation non vérifié
    "M13-sceau": ("pole/ideation.py", "    if not verifier_scelle(chemin):\n        raise CourseInterrompue(f\"attestation non",
                  "    if False:\n        raise CourseInterrompue(f\"attestation non"),
    # CL35-09 : --delai-session-s 0 accepté
    "M14-delai-zero": ("demonstrations/ideation_v1.py",
                       "if args.delai_session_s is not None and not args.delai_session_s > 0:",
                       "if False:"),
    # CL36-01 : reponse.md écrit toujours (v36)
    "M15-reponse-toujours": ("pole/ideation.py",
                             'if r.statut == "ok" or cout > 0 or texte:  # CL36-01',
                             'if True:  # CL36-01'),
    # CL36-02 : coût du contrôle externe non repris au journal
    "M16-cout-controle-externe": ("pole/ideation.py",
                                  '"cout_externe_usd": float(cout_externe_deja_engage_usd),',
                                  '"cout_externe_usd": 0.0,'),
    # CL35-07 : --commande-externe accepté avec --juge-externe seul hors bras (garde vidée)
    "M17-commande-seule": ("demonstrations/ideation_v1.py",
                           "if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe):",
                           "if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe or args.juge_externe):"),
    # CL35-08 : exception du lanceur rendue en trace (pas de code 2)
    "M18-trace": ("demonstrations/ideation_v1.py", "    except Exception as e:  # noqa: BLE001 — CL35-08", "    except ZeroDivisionError as e:  # noqa: BLE001 — CL35-08"),
    # CL35-07a : --commande-externe seul accepté
    "M19-commande-seule-a": ("demonstrations/ideation_v1.py", "if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe):  # CL35-07a", "if False:  # CL35-07a"),
}


def main():
    arbre, travail = sys.argv[1], sys.argv[2]
    choisies = sys.argv[3:] or sorted(MUTATIONS)
    py = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "venv-pole", "bin", "python")
    py = os.path.abspath(py)
    for nom in choisies:
        fichier, avant, apres = MUTATIONS[nom]
        copie = os.path.join(travail, nom)
        if os.path.exists(copie):
            shutil.rmtree(copie)
        shutil.copytree(arbre, copie)
        chemin = os.path.join(copie, fichier)
        texte = open(chemin, encoding="utf-8").read()
        n = texte.count(avant)
        if n != 1:
            print(f"{nom}: motif trouvé {n} fois, mutation NON appliquée", flush=True)
            continue
        open(chemin, "w", encoding="utf-8").write(texte.replace(avant, apres))
        t0 = time.time()
        r = subprocess.run([py, "-B", "-m", "unittest", "essais.test_v7_ideation"], cwd=copie, capture_output=True,
                           text=True, env={"PATH": "/usr/bin:/bin", "HOME": travail, "LANG": "C.UTF-8"})
        duree = time.time() - t0
        fin = (r.stderr.strip().splitlines() or ["?"])[-1]
        echecs = [l for l in r.stderr.splitlines() if l.startswith(("FAIL:", "ERROR:"))]
        verdict = "survit" if r.returncode == 0 else "tuée"
        print(f"{nom}: {verdict} ({fin} ; {duree:.0f} s) {'; '.join(echecs)[:400]}", flush=True)
        if r.returncode and os.environ.get("DETAIL"): print(r.stderr[-3000:])
        shutil.rmtree(copie)


if __name__ == "__main__":
    main()
