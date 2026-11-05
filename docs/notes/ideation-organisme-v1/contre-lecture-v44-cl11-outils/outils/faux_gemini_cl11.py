"""CL11 : faux serveur local de l'interface Gemini (countTokens, generateContent). Aucun réseau. Comportement réglé par
un fichier JSON relu à chaque requête : jetons_par_car_compte (countTokens), jetons_par_car_facture (promptTokenCount),
sortie ("max" = maxOutputTokens demandé, ou entier), pensees (thoughtsTokenCount en plus), fin (STOP / MAX_TOKENS), texte.
Usage : python3 faux_gemini_cl11.py PORT CONFIG JOURNAL"""
import json, math, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
PORT, CONFIG, JOURNAL = int(sys.argv[1]), sys.argv[2], sys.argv[3]
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        cfg = json.load(open(CONFIG))
        n = int(self.headers.get("Content-Length", 0)); corps = json.loads(self.rfile.read(n))
        txt = "".join(p.get("text", "") for c in corps["contents"] for p in c["parts"])
        modele = self.path.split("/models/")[1].split(":")[0]
        if self.path.endswith(":countTokens"):
            rep = {"totalTokens": math.ceil(len(txt) * cfg.get("jetons_par_car_compte", 0.25))}
        else:
            mx = corps["generationConfig"]["maxOutputTokens"]
            sortie = mx if cfg.get("sortie", "max") == "max" else int(cfg["sortie"])
            rep = {"modelVersion": modele, "candidates": [{"finishReason": cfg.get("fin", "STOP"),
                   "content": {"parts": [{"text": ("OK" if txt.startswith("Réponds exactement OK") else
                                                (open(cfg["texte_fichier"]).read() if cfg.get("texte_fichier") else cfg.get("texte", "OK")))}]}}],
                   "usageMetadata": {"promptTokenCount": math.ceil(len(txt) * cfg.get("jetons_par_car_facture", 0.25)),
                                     "candidatesTokenCount": sortie, "thoughtsTokenCount": int(cfg.get("pensees", 0))}}
        with open(JOURNAL, "a") as j:
            j.write(json.dumps({"chemin": self.path.split(":")[-1], "taille": len(txt), "cle_vue": self.headers.get("x-goog-api-key") == "cle-factice",
                                "max_sortie": corps.get("generationConfig", {}).get("maxOutputTokens"), "rep_usage": rep.get("usageMetadata"), "rep": rep.get("totalTokens")}) + "\n")
        b = json.dumps(rep).encode(); self.send_response(200); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
HTTPServer(("127.0.0.1", PORT), H).serve_forever()
