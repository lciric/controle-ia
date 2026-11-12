"""Faux relais local (aucun appel réseau) : lit le corps envoyé par commande_kimi_v6.py et rend une réponse 'stop' ; on lit
max_tokens et pire_cas de la dernière ligne de la commande, sous v6 et sous v7, pour une consigne de la taille réelle du
corps de la course 2 (15 405 octets)."""
import http.server, json, os, subprocess, sys, threading, tempfile
CMD, CONF6, CONF7 = sys.argv[1:4]
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers["Content-Length"]); corps = json.loads(self.rfile.read(n))
        rep = json.dumps({"model": corps["model"], "choices": [{"message": {"content": "ok"}, "finish_reason": "stop"}],
                          "usage": {"prompt_tokens": 1, "completion_tokens": 1}}).encode()
        self.send_response(200); self.send_header("Content-Length", str(len(rep))); self.end_headers(); self.wfile.write(rep)
    def log_message(self, *a): pass
srv = http.server.HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=srv.serve_forever, daemon=True).start()
port = srv.server_address[1]
def args(conf):
    c = json.load(open(conf, encoding="utf-8"))
    cmd = c["fournisseurs"]["kimi"]["commande"]
    a = cmd[cmd.index("--url-relais"):]
    a[a.index("--url-relais") + 1] = f"http://127.0.0.1:{port}"
    return a, c["plafonds_session"]["proposeur"]
# consigne dont le corps JSON fait ≈ 15 405 octets (ASCII, sans échappement)
for nom, conf in (("v6", CONF6), ("v7", CONF7)):
    a, ps = args(conf)
    for taille in (15405 - 75, 17900 - 75):  # corps génération 1 observé ; génération 2 estimé (devis : +2 178 caractères)
        reg = tempfile.mktemp()
        a2 = [x.replace("{REGISTRE}", reg) for x in a]
        env = {"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": repr(float(ps)), "ROLE_POLE": "proposeur_ideation",
               "MODELE_DEMANDE_POLE": "kimi-k3.1-pro"}
        p = subprocess.run([sys.executable, "-I", "-B", CMD] + a2, input=("x" * taille).encode(), capture_output=True, env=env)
        d = json.loads(p.stdout.decode().strip().splitlines()[-1])
        print(nom, "plafond de session", ps, "USD ; corps", d.get("octets_corps"), "octets ; code", p.returncode,
              "; max_tokens", d.get("max_tokens"), "; pire cas réservé", d.get("pire_cas_usd"), "USD")
srv.shutdown()
