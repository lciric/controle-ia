"""CL6 : interruption (SIGINT) de l'orchestrateur pendant la session du juge externe du bras, APRÈS l'envoi de sa
consigne (fiches comprises). Le bras est-il verrouillé, ou classé « tentative échouée avant tout envoi des fiches » et
relançable ? Le coût de la session interrompue est-il compté ?
Usage : python -I -B bras_interrompu.py COPIE_V39 DOSSIER_SIMULEE PYTHON"""
import json
import os
import shutil
import signal
import subprocess
import sys
import time

COPIE, SIM, PY = sys.argv[1:4]
sys.path.insert(0, COPIE)
from pole import ideation as idn  # noqa: E402

LANCEUR = os.path.join(COPIE, "demonstrations", "ideation_v1.py")
ARGON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "argon_factice.py")
PREP = os.path.join(SIM, "prep")
ENV = {"PATH": "/usr/bin:/bin", "HOME": "/root", "LANG": "C.UTF-8"}
d = os.path.join(SIM, "S8")
shutil.rmtree(d, ignore_errors=True)
os.makedirs(d)
sortie, j, pids = os.path.join(d, "course"), os.path.join(d, "argon.jsonl"), os.path.join(d, "pids.txt")
base = [PY, "-I", "-B", LANCEUR]
cmd_ok = " ".join([PY, "-I", ARGON, "--journal", j])
r = subprocess.run(base + [sortie, "--liste-blanche", os.path.join(PREP, "liste-blanche.json"), "--question",
                           os.path.join(PREP, "question.md"), "--piece", os.path.join(PREP, "piece-a.md"), "--temoins",
                           os.path.join(PREP, "temoins.json"), "--proposeur-externe", "argon=gemini-argon", "--juge-externe",
                           "argon-j=gemini-argon", "--commande-externe", cmd_ok], capture_output=True, text=True, env=ENV)
print("course : code", r.returncode)
att = os.path.join(d, "attestation-lecture.json")
consigne = os.path.join(sortie, "juges-bras-rapporte", "traces-argon-j", "consigne-en-attente.md")
idn.ecrire_json_scelle(att, {"lecteur": "relecteur CL6 (factice)", "lu_le": "2026-10-29",
                             "fiches_validees_sha256": idn.sha256_fichier(os.path.join(sortie, "fiches-validees.json")),
                             "consignes_en_attente_sha256": {"argon-j": idn.sha256_fichier(consigne)}})
bras = base + [sortie, "--bras-rapporte-differe", "--attestation-lecture-humaine", att, "--juge-externe", "argon-j=gemini-argon",
               "--commande-externe"]
p = subprocess.Popen(bras + [" ".join([PY, "-I", ARGON, "--journal", j, "--dormir-juge", "30", "--pids", pids])],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=ENV)
for _ in range(300):
    if os.path.exists(pids) and open(pids).read().strip():
        break
    time.sleep(0.1)
recu = [a for a in map(json.loads, open(j)) if a["role"] == "juge_ideation" and not a["controle"]]
print("consigne du juge reçue par Argon avant l'interruption :", [(a["taille"]) for a in recu], "caractères")
os.kill(p.pid, signal.SIGINT)
out, err = p.communicate(timeout=60)
print("bras interrompu : code", p.returncode, "; erreur :", (err.strip().splitlines() or [""])[-1][:300])
for f in sorted(os.listdir(sortie)):
    if f.startswith(("bras-tentative", "manifeste-bras")) and f.endswith(".json"):
        m = json.load(open(os.path.join(sortie, f)))["reglages"]
        print(f"   {f} : relancable={m.get('relancable')} ; cout_total_usd={m['journal']['cout_total_usd']} ; erreur={m['erreur'][:100]!r}")
r2 = subprocess.run(bras + [cmd_ok], capture_output=True, text=True, env=ENV)
print("relance du bras : code", r2.returncode, "; consignes du juge reçues par Argon au total :",
      sum(1 for a in map(json.loads, open(j)) if a["role"] == "juge_ideation" and not a["controle"]))
print("   classement écrit :", os.path.exists(os.path.join(sortie, "classement.json")))
