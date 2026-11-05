"""Attestation de lecture humaine factice (pour la simulation seulement), scellée. Usage : attester.py SORTIE ARBRE CHEMIN"""

import json
import os
import sys

sortie, arbre, chemin = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, arbre)
from pole import ideation as idn  # noqa: E402

consigne = os.path.join(sortie, "juges-bras-rapporte", "traces-argon", "consigne-en-attente.md")
if not os.path.exists(consigne):
    consigne = os.path.join(sortie, "juges-bras-rapporte", "argon", "traces", "consigne-en-attente.md")
idn.ecrire_json_scelle(chemin, {"lecteur": "relecteur CL5 (simulation)", "lu_le": "2026-10-28",
                                "fiches_validees_sha256": idn.sha256_fichier(os.path.join(sortie, "fiches-validees.json")),
                                "consignes_en_attente_sha256": {"argon": idn.sha256_fichier(consigne)}})
print(json.dumps({"attestation": chemin}))
