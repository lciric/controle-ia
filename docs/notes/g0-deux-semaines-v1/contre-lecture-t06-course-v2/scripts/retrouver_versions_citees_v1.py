"""Pour chaque empreinte citée par le candidat 12 r2 qui diffère du fichier au commit 8cb539f9, cherche dans l'histoire locale
(ancêtres de 8cb539f9) la version du fichier qui porte cette empreinte. Lecture seule.

Usage : python -I retrouver_versions_citees_v1.py DEPOT
"""
import hashlib
import subprocess
import sys

DEPOT = sys.argv[1]
CAS = [("scripts/lancer_t06_v11.sh", "a0aea3d3ab36d991"), ("scripts/amorce_instance_t06_v9.sh", "be2183b04fa5101f"),
       ("scripts/tests-cibles-t06-v1.txt", "edc1c70e790655ac"), ("scripts/tests-exclus-t06-v1.txt", "3db58d1da2f41273"),
       ("tests/test_t06_cibles_invisibles_v1.py", "0eada74659bbd04f"),
       ("brouillons/ordres-t06-e2-e3-v5/ordre-fille-6-t06-e3-v5.md", "f00e143d0ef3a84c")]


def git(*a):
    return subprocess.run(["git", "-C", DEPOT, *a], capture_output=True)


for chemin, prefixe in CAS:
    commits = git("rev-list", "8cb539f9", "--", chemin).stdout.decode().split()
    trouve = None
    for c in commits:
        r = git("show", f"{c}:{chemin}")
        if r.returncode == 0 and hashlib.sha256(r.stdout).hexdigest().startswith(prefixe):
            trouve = c
            break
    actuel = hashlib.sha256(git("show", f"8cb539f9:{chemin}").stdout).hexdigest()[:16]
    print(f"{chemin} cité {prefixe} ; au commit 8cb539f9 {actuel} ; version citée trouvée au commit {trouve[:8] if trouve else 'aucun (histoire locale de ' + str(len(commits)) + ' commits)'}")
