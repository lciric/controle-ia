"""CL3 : construit (sans l'exécuter) la ligne de commande du kit d'agent pour les rôles de l'idéation, v35."""
import dataclasses, json, sys
sys.path.insert(0, sys.argv[1])  # racine de l'arbre v35 relu
import claude_agent_sdk as sdk
from claude_agent_sdk._internal.transport.subprocess_cli import SubprocessCLITransport
from pole import adaptateurs as A

for role in ("proposeur_ideation", "juge_ideation", "experimentateur"):
    o = A.construire_options("/srv/course-cl3/proposeur/" + role, 2.0, 2, url_relais="http://127.0.0.1:9", modele="claude-opus-5-5", role=role)
    opts = A.AdaptateurClaudeSDK.options_sdk(sdk, o)
    opts = dataclasses.replace(opts, cli_path="/bin/true")
    t = SubprocessCLITransport(prompt="consigne", options=opts)
    cmd = t._build_command()
    def val(f):
        return [cmd[i+1] if i+1 < len(cmd) and not cmd[i+1].startswith("--") else "(drapeau)" for i, c in enumerate(cmd) if c == f] or ["ABSENT"]
    print("==", role)
    for f in ("--tools", "--allowedTools", "--disallowedTools", "--effort", "--permission-mode", "--max-turns", "--max-budget-usd", "--model"):
        print("  ", f, repr(val(f)))
    print("   setting-sources:", [c for c in cmd if c.startswith("--setting-sources")])
    print("   mcp:", [c for c in cmd if "mcp" in c], " plugin:", [c for c in cmd if "plugin" in c], " add-dir:", [c for c in cmd if "add-dir" in c])
    s = val("--settings")[0]
    print("   settings:", s[:600])
    print("   skills option:", opts.skills, " mcp_servers:", opts.mcp_servers, " can_use_tool:", opts.can_use_tool, " agents:", opts.agents)
