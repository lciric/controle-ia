"""Diagnostic d'un échec d'appel Anthropic (message d'erreur seulement, tronqué ; aucune clé lue ni écrite ici)."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("cv", "collisionneur_v2.py"); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
r = cv.appeler_anthropic(cv.MODELES["B"]["id"], "Réponds par le seul mot : prêt.", 16)
print("échec :", (r.echec or "")[:300]); print("servi :", r.modele_servi, r.usage)
