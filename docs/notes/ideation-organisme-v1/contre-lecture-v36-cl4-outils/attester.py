"""CL4 : écrit une attestation de lecture humaine scellée pour une sortie donnée (essai local)."""
import os, sys
code, sortie, chemin = sys.argv[1], sys.argv[2], sys.argv[3]
etiq = sys.argv[4] if len(sys.argv) > 4 else "argon-juge"
sys.path.insert(0, code)
from pole import ideation as idn
from pole.outils import dossier_traces
c = os.path.join(dossier_traces(os.path.join(sortie, "juges-bras-rapporte", etiq)), "consigne-en-attente.md")
idn.ecrire_json_scelle(chemin, {"lecteur": "lecteur-cl4", "lu_le": "2026-10-28",
                                "fiches_validees_sha256": idn.sha256_fichier(os.path.join(sortie, "fiches-validees.json")),
                                "consignes_en_attente_sha256": {etiq: idn.sha256_fichier(c)}})
print("attestation", chemin)
