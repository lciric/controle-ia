"""Interruption de l'orchestrateur (SIGINT, comme un Ctrl-C) pendant une commande externe : la commande, lancée dans sa
propre session de processus, survit-elle ? Aucun réseau. Usage : python -B interruption.py ARBRE_V37 TRAVAIL"""

import os
import signal
import subprocess
import sys
import time

arbre, travail = sys.argv[1], sys.argv[2]
pid_f = os.path.join(travail, "interruption-commande.pid")
script = os.path.join(travail, "interruption-commande.py")
open(script, "w").write("import os, sys, time\nsys.stdin.read()\nopen(%r, 'w').write(str(os.getpid()))\ntime.sleep(20)\n"
                        "print('{\"texte\": \"x\", \"cout_usd\": 0.1}')\n" % pid_f)
parent = ("import sys; sys.path.insert(0, %r)\n"
          "from pole.adaptateurs import AdaptateurCommandeExterne\n"
          "ad = AdaptateurCommandeExterne([sys.executable, '-I', %r], environnement={}, delai_s=900)\n"
          "ad.lancer('juge_ideation', 'consigne', %r, 1.0, 1)\n") % (arbre, script, travail)
if os.path.exists(pid_f):
    os.remove(pid_f)
p = subprocess.Popen([sys.executable, "-B", "-c", parent], stderr=subprocess.PIPE)
for _ in range(50):
    if os.path.exists(pid_f) and open(pid_f).read():
        break
    time.sleep(0.1)
enfant = int(open(pid_f).read())
p.send_signal(signal.SIGINT)
p.wait(timeout=10)
print("orchestrateur : code", p.returncode, "| dernière ligne d'erreur :", p.stderr.read().decode().strip().splitlines()[-1])
time.sleep(1)
try:
    os.kill(enfant, 0)
    print("commande externe (pid", enfant, ") TOUJOURS VIVANTE après l'interruption de l'orchestrateur")
    os.kill(enfant, signal.SIGKILL)
    print("(arrêtée par la relecture, par son identifiant)")
except ProcessLookupError:
    print("commande externe arrêtée avec l'orchestrateur")
