"""Fichier des tâches du pilote de T0.5 réduit (N-019) : les N premières tâches du fichier des tâches d'évaluation
assemblé par l'extraction, dans son ordre (ordre du tirage, rang de garde ; `extraire_t05.assembler`), recopiées à
l'identique (objets JSON inchangés). La source est vérifiée par son sceau et par l'empreinte attendue ; la sortie est
écrite en mode exclusif (R12), puis scellée par l'appelant. Aucun texte de tâche n'est lu ni affiché.

Usage : python -I deriver_taches_pilote_v1.py SOURCE EMPREINTE_SOURCE N SORTIE"""
import hashlib
import json
import sys
from pathlib import Path


def arret(msg: str) -> None:
    sys.exit(f"ARRÊT de la dérivation : {msg}")


if len(sys.argv) != 5:
    arret("quatre arguments attendus")
source, attendue, n, sortie = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4])
if not n.isdigit() or not 0 < int(n):
    arret("N entier positif attendu")
n = int(n)
octets = source.read_bytes()
sha = hashlib.sha256(octets).hexdigest()
if sha != attendue:
    arret(f"source {source} : empreinte {sha} ≠ {attendue}")
sceau = Path(str(source) + ".sha256")
if not sceau.is_file() or sceau.read_text(encoding="utf-8").split()[0] != sha:
    arret(f"source {source} : sceau absent ou différent")
brut = json.loads(octets)
taches = brut["resultat"]["taches"]
if len(taches) < n:
    arret(f"source : {len(taches)} tâches, moins que {n}")
if brut["resultat"].get("remplacements"):
    arret("source : remplacements présents ; l'ordre du tirage n'est plus celui du fichier")
ids = [t["identifiant"] for t in taches]
if len(set(ids)) != len(ids):
    arret("source : identifiants en double")
corps = {"source": {"chemin": str(source), "sha256": sha, "taches": len(taches)},
         "regle": (f"les {n} premières tâches de la source, dans son ordre (ordre du tirage, rang de garde), "
                   "recopiées à l'identique (N-019)"),
         "taches": taches[:n]}
with open(sortie, "x", encoding="utf-8") as f:
    json.dump(corps, f, ensure_ascii=False, indent=1)
    f.write("\n")
print(json.dumps({"sortie": str(sortie), "sha256": hashlib.sha256(sortie.read_bytes()).hexdigest(), "taches": n,
                  "premiere": ids[0], "derniere": ids[n - 1]}, ensure_ascii=False))
