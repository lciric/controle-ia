#!/usr/bin/env python3
"""Faux amont Gemini, version 3 — essais de `commande_argon_v3c.py` (recherche Google), **boucle locale seulement**.

Lignée session-depot, 30 octobre 2026. Copie de `faux_amont_gemini_recherche_v2.py` (inchangée, R12) ; sans option
nouvelle, les réponses sont celles de la v2. Options ajoutées (artefacts de la contre-lecture de la v3b) :
- `--entree-facturee N` : `usageMetadata.promptTokenCount` = N (au lieu du compte factice du corps) : l'amont facture une
  entrée au-delà de l'entrée gardée (contenu de la recherche compté dans l'entrée, bloquant 1) ;
- `--candidats-au-maximum` : `candidatesTokenCount` = `generationConfig.maxOutputTokens` du corps reçu (sortie maximale) ;
  `--candidats N` reste permis et l'emporte s'il est donné ;
- `--requete-nulle` : ajoute un `null` à la fin de `webSearchQueries` (mineur 2).

En-tête de la v2 (inchangé) : Faux amont Gemini, version 2 — essais de `commande_argon_v3b.py`. Copie de
`faux_amont_gemini_recherche_v1.py` (inchangée, R12) ; sans option nouvelle, les réponses sont celles de la v1. Options
ajoutées (artefacts des contre-lectures de la v3) :
- `--sans-usage` : aucun `usageMetadata` ;
- `--requetes-vides` : `webSearchQueries` = [] (sources, appuis et point d'entrée gardés) ;
- `--grounding-vide` : `groundingMetadata` = {"webSearchQueries": []} et rien d'autre ;
- `--partie NOM` : ajoute une partie `{NOM: {...}}` à la réponse (functionCall, functionResponse, executableCode,
  codeExecutionResult) ;
- `--texte-separateurs` : le texte rendu porte U+2028, U+2029 et U+0085 ;
- `--cle-dans-modele` : `modelVersion` = « <modèle>-<clé reçue> » ; `--cle-dans-fin` : `finishReason` = « AUTRE <clé> » ;
- `--cle-coupee-dans-titre` : titre de la première source = la clé reçue coupée en deux par un caractère nul ;
- `--uri-source URI` : adresse de la première source ;
- `--longueur-champs N` : requêtes, titres et adresses complétés jusqu'à N caractères.

En-tête de la v1 (inchangé) : Imite les deux routes que la commande appelle :
`POST /v1beta/models/<modèle>:countTokens` et `POST /v1beta/models/<modèle>:generateContent`. Aucune connexion sortante,
aucune clé réelle : la clé reçue (factice) n'est jamais écrite au journal (seulement sa présence).

Quand le corps de `generateContent` porte l'outil `google_search`, la réponse porte un `candidates[0].groundingMetadata`
**factice** : 2 requêtes (`webSearchQueries`), 3 sources (`groundingChunks[].web.uri` et `.title`), 2 appuis
(`groundingSupports`), et un `searchEntryPoint`. La forme imite la documentation publique de Google ; celle que rendra
réellement gemini-4-argon est SUPPOSÉE.

Options de simulation :
- `--sans-grounding` : aucun `groundingMetadata`, même avec l'outil ;
- `--sans-requetes` : `groundingMetadata` présent, sans `webSearchQueries` ;
- `--requetes N`, `--sources N` : nombres de requêtes et de sources factices (défaut 2 et 3) ;
- `--modele-servi NOM` : `modelVersion` rendu (défaut : le modèle du chemin) ;
- `--tronquee` : `finishReason` = `MAX_TOKENS` ;
- `--refus http400` : HTTP 400 `INVALID_ARGUMENT` qui **recopie la clé reçue** dans son message (pour vérifier que la
  commande la masque) ; `--refus bloque` : `promptFeedback.blockReason` = `SAFETY`, aucun candidat ;
- `--usage-outil N` : `usageMetadata.toolUsePromptTokenCount` = N (absent par défaut) ;
- `--pensees N` (défaut 300), `--candidats N` (défaut 120) : jetons rendus dans l'usage ;
- `--cle-dans-titre` : recopie la clé reçue dans le titre de la première source (pour vérifier le masquage) ;
- `--journal FICHIER` : une ligne JSON par requête reçue (chemin, corps, présence d'une clé ; jamais la clé).

Au démarrage, la première ligne de la sortie standard est `pret http://127.0.0.1:<port>` (port 0 : choisi par le système).
Arrêt : par le PID du processus (R10).
"""

import argparse
import json
import math
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "faux-amont-gemini-recherche-v3"
HOTE = "127.0.0.1"  # boucle locale seulement : aucune option ne le change


def a_l_outil_recherche(corps):
    outils = corps.get("tools") if isinstance(corps, dict) else None
    return isinstance(outils, list) and any(isinstance(o, dict) and ("google_search" in o or "googleSearch" in o)
                                            for o in outils)


def jetons_de(corps):
    """Compte factice : ⌈caractères / 4⌉ du texte des contenus (au moins 1)."""
    total = 0
    for c in (corps.get("contents") or []) if isinstance(corps, dict) else []:
        for p in (c.get("parts") or []) if isinstance(c, dict) else []:
            if isinstance(p, dict) and isinstance(p.get("text"), str):
                total += len(p["text"])
    return max(1, math.ceil(total / 4))


def grounding_factice(args, cle_recue):
    requetes = [f"requête factice {i + 1} sur le contrôle des agents" for i in range(args.requetes)]
    sources = [{"web": {"uri": f"https://vertexaisearch.cloud.google.com/grounding-api-redirect/FAUX{i + 1}",
                        "title": f"source-factice-{i + 1}.example.org"}} for i in range(args.sources)]
    if args.longueur_champs:
        n = args.longueur_champs
        requetes = [(q + " " + "r" * n)[:n] for q in requetes]
        for s in sources:
            s["web"]["title"] = (s["web"]["title"] + " " + "t" * n)[:n]
            s["web"]["uri"] = (s["web"]["uri"] + "/" + "a" * n)[:n]
    if args.cle_dans_titre and sources:
        sources[0]["web"]["title"] = f"titre avec clé {cle_recue}"
    if args.cle_coupee_dans_titre and sources:
        m = len(cle_recue) // 2
        sources[0]["web"]["title"] = f"titre {cle_recue[:m]}\x00{cle_recue[m:]} fin"
    if args.uri_source is not None and sources:
        sources[0]["web"]["uri"] = args.uri_source
    if args.grounding_vide:
        return {"webSearchQueries": []}
    gm = {"searchEntryPoint": {"renderedContent": "<div>suggestions factices</div>"},
          "groundingChunks": sources,
          "groundingSupports": [
              {"segment": {"startIndex": 0, "endIndex": 7, "text": "Réponse"}, "groundingChunkIndices": [0],
               "confidenceScores": [0.9]},
              {"segment": {"startIndex": 8, "endIndex": 16, "text": "factice"}, "groundingChunkIndices": [1, 2],
               "confidenceScores": [0.8, 0.7]}]}
    if args.requetes_vides:
        gm["webSearchQueries"] = []
    elif not args.sans_requetes:
        gm["webSearchQueries"] = requetes + ([None] if args.requete_nulle else [])  # v3 : un élément illisible
    return gm


def fabriquer(args, verrou):
    class Gestionnaire(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, format, *a):  # noqa: A002
            pass

        def _json(self, statut, objet):
            brut = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(statut)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(brut)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(brut)
            self.close_connection = True

        def do_POST(self):
            longueur = int(self.headers.get("content-length") or 0)
            brut = self.rfile.read(longueur) if longueur else b""
            try:
                corps = json.loads(brut.decode("utf-8"))
            except (UnicodeDecodeError, ValueError):
                corps = None
            cle_recue = self.headers.get("x-goog-api-key") or ""
            if args.journal:
                with verrou, open(args.journal, "a", encoding="utf-8") as f:
                    f.write(json.dumps({"chemin": self.path, "corps": corps, "cle_presente": bool(cle_recue)},
                                       ensure_ascii=False) + "\n")
            chemin = self.path.split("?", 1)[0]
            if not chemin.startswith("/v1beta/models/") or ":" not in chemin:
                return self._json(404, {"error": {"code": 404, "status": "NOT_FOUND"}})
            modele, action = chemin[len("/v1beta/models/"):].rsplit(":", 1)
            if not isinstance(corps, dict):
                return self._json(400, {"error": {"code": 400, "message": "JSON illisible", "status": "INVALID_ARGUMENT"}})
            if action == "countTokens":
                return self._json(200, {"totalTokens": jetons_de(corps)})
            if action != "generateContent":
                return self._json(404, {"error": {"code": 404, "status": "NOT_FOUND"}})
            if args.refus == "http400":
                return self._json(400, {"error": {"code": 400, "status": "INVALID_ARGUMENT",
                                                  "message": f"champ refusé (clé reçue {cle_recue})"}})
            entree = jetons_de(corps) if args.entree_facturee is None else args.entree_facturee  # v3
            candidats = args.candidats
            if candidats is None:  # v3 : --candidats-au-maximum, sinon le défaut de la v2 (120)
                config = corps.get("generationConfig") if isinstance(corps.get("generationConfig"), dict) else {}
                candidats = config.get("maxOutputTokens", 120) if args.candidats_au_maximum else 120
            usage = {"promptTokenCount": entree, "candidatesTokenCount": candidats,
                     "thoughtsTokenCount": args.pensees,
                     "totalTokenCount": entree + candidats + args.pensees + (args.usage_outil or 0)}
            if args.usage_outil is not None:
                usage["toolUsePromptTokenCount"] = args.usage_outil
            servi = args.modele_servi or modele
            if args.cle_dans_modele:
                servi = f"{servi}-{cle_recue}"
            if args.refus == "bloque":
                return self._json(200, {"promptFeedback": {"blockReason": "SAFETY"}, "usageMetadata": usage,
                                        "modelVersion": servi})
            texte = "Réponse factice d'Argon." + ("\u2028ligne\u2029paragraphe\x85suite" if args.texte_separateurs else "")
            parties = [{"text": texte}]
            if args.partie:
                parties.append({args.partie: {"name": "factice"}})
            fin = "MAX_TOKENS" if args.tronquee else "STOP"
            if args.cle_dans_fin:
                fin = f"AUTRE {cle_recue}"
            candidat = {"content": {"role": "model", "parts": parties}, "finishReason": fin, "index": 0}
            if a_l_outil_recherche(corps) and not args.sans_grounding:
                candidat["groundingMetadata"] = grounding_factice(args, cle_recue)
            reponse = {"candidates": [candidat], "usageMetadata": usage, "modelVersion": servi, "responseId": "faux-1"}
            if args.sans_usage:
                del reponse["usageMetadata"]
            return self._json(200, reponse)

    return Gestionnaire


def analyseur():
    a = argparse.ArgumentParser(prog="faux_amont_gemini_recherche_v3", description="Faux amont Gemini (boucle locale).")
    a.add_argument("--port", type=int, default=0)
    a.add_argument("--journal")
    a.add_argument("--sans-grounding", action="store_true")
    a.add_argument("--sans-requetes", action="store_true")
    a.add_argument("--requetes", type=int, default=2)
    a.add_argument("--sources", type=int, default=3)
    a.add_argument("--modele-servi")
    a.add_argument("--tronquee", action="store_true")
    a.add_argument("--refus", choices=("aucun", "http400", "bloque"), default="aucun")
    a.add_argument("--usage-outil", type=int)
    a.add_argument("--pensees", type=int, default=300)
    a.add_argument("--candidats", type=int)  # v3 : défaut 120 posé plus bas
    a.add_argument("--cle-dans-titre", action="store_true")
    # v2
    a.add_argument("--sans-usage", action="store_true")
    a.add_argument("--requetes-vides", action="store_true")
    a.add_argument("--grounding-vide", action="store_true")
    a.add_argument("--partie", choices=("functionCall", "functionResponse", "executableCode", "codeExecutionResult"))
    a.add_argument("--texte-separateurs", action="store_true")
    a.add_argument("--cle-dans-modele", action="store_true")
    a.add_argument("--cle-dans-fin", action="store_true")
    a.add_argument("--cle-coupee-dans-titre", action="store_true")
    a.add_argument("--uri-source")
    a.add_argument("--longueur-champs", type=int)
    # v3
    a.add_argument("--entree-facturee", type=int)
    a.add_argument("--candidats-au-maximum", action="store_true")
    a.add_argument("--requete-nulle", action="store_true")
    return a


def principal(argv=None):
    args = analyseur().parse_args(argv)
    serveur = ThreadingHTTPServer((HOTE, args.port), fabriquer(args, threading.Lock()))
    serveur.daemon_threads = True
    print(f"pret http://{HOTE}:{serveur.server_address[1]}", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        serveur.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(principal())
