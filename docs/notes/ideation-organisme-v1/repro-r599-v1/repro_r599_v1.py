"""Reproduction à zéro dépense de R-599 : une session du kit d'agent, avec les options exactes de v31, contre le relais réel
tenu avec une clé factice et un amont mort. Aucune vraie clé, aucun appel payant possible."""
import json, os, sys, tempfile
O = sys.argv[1]; URL = sys.argv[2]; SANS_BAC = len(sys.argv) > 3 and sys.argv[3] == "sans-bac"
sys.path.insert(0, O)
from pole import adaptateurs as ad
base = tempfile.mkdtemp(prefix="course-", dir=os.environ.get("TMPDIR", "/tmp"))
dossier = os.path.join(base, "fiche", "juge")
os.makedirs(dossier)
a = ad.AdaptateurClaudeSDK(URL, environnement={}, arme=True)
if SANS_BAC:
    # variante de diagnostic : mêmes options sans bac à sable, pour isoler son effet sur le chemin réseau
    orig = ad.construire_options
    def sans(*x, **k):
        o = orig(*x, **k); o["sandbox"] = {"enabled": False}; return o
    ad.construire_options = sans
r = a.lancer("juge_ideation", "Réponds exactement : OK", dossier, 0.05, 1, modele="claude-opus-5-5")
print(json.dumps({"statut": r.statut, "cout": r.cout_declare_usd,
                  "erreur": r.erreur, "texte": (r.texte_final or "")[:300]}, ensure_ascii=False, default=str))
