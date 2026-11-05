"""CL3 (CL34-05) : la borne de temps de AdaptateurClaudeSDK._executer arrête-t-elle le sous-processus du kit ?
Faux outil en ligne de commande local (aucun réseau, aucune clé) qui pend."""
import asyncio, dataclasses, os, sys, time
sys.path.insert(0, sys.argv[1])
journal = sys.argv[2]
os.environ["FAUX_CLI_JOURNAL"] = journal
import claude_agent_sdk as sdk
from pole import adaptateurs as A
o = A.construire_options(os.path.join(journal, "course", "juges", "j"), 0.2, 1, url_relais="http://127.0.0.1:9",
                         modele="claude-opus-5-5", role="juge_ideation")
os.makedirs(o["cwd"], exist_ok=True)
opts = dataclasses.replace(A.AdaptateurClaudeSDK.options_sdk(sdk, o), cli_path=sys.argv[3],
                           env=dict(o["env"], FAUX_CLI_JOURNAL=journal, FAUX_CLI_IGNORE_TERM=os.environ.get("FAUX_CLI_IGNORE_TERM", "0")))
t0 = time.time()
res = asyncio.run(A.AdaptateurClaudeSDK._executer(sdk, "Réponds OK", opts, 3))
print("retour de _executer après %.1f s :" % (time.time() - t0), res[2], "|", res[3])
pids = [int(n.split("-")[1]) for n in os.listdir(journal) if n.startswith("pid-")]
def vivant(p):
    try:
        os.kill(p, 0)
    except ProcessLookupError:
        return False
    try:
        with open(f"/proc/{p}/stat") as f:
            return f.read().split()[2] != "Z"
    except OSError:
        return False
time.sleep(2)
print("faux CLI lancés :", pids, "; vivants 2 s après le retour (interpréteur encore ouvert) :", [p for p in pids if vivant(p)])
with open(os.path.join(journal, "pids.txt"), "w") as f:
    f.write(" ".join(map(str, pids)))
