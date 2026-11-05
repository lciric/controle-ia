"""Règles du mandataire de sortie de la machine A (Agentic Scientist v3), v1 — session-depot, 30 octobre 2026 (R-561, R-808).

Fonctions pures, sans dépendance, essayées hors de mitmproxy (`essais/test_mandataire_regles_v1.py`).

Politique : Web des agents **ouvert**, avec deux familles de refus seulement :
1. **La future copie publique du programme** (mot de Lazar, R-561) : tout chemin qui commence par `/lciric/controle-ia`
   sur les hôtes de GitHub (le préfixe couvre aussi `controle-ia-travail`, privé), sans égard à la casse ni aux
   barres répétées ou à l'encodage `%2F` ; sur l'interface de programmation, `/repos/lciric/controle-ia…`.
2. **Les contournements du relais** : appels directs aux fournisseurs de modèles (Anthropic, OpenAI, Codex, Bedrock,
   Gemini). Ce n'est pas le Web des agents : un tel appel échapperait au plafond et à la trace du relais.
"""
from urllib.parse import unquote

HOTES_GITHUB_CHEMIN = frozenset({"github.com", "www.github.com", "raw.githubusercontent.com", "codeload.github.com",
                                 "gist.github.com", "objects.githubusercontent.com"})
HOTE_API_GITHUB = "api.github.com"
PREFIXE_INTERDIT = "/lciric/controle-ia"

HOTES_FOURNISSEURS = frozenset({"api.anthropic.com", "api.openai.com", "chatgpt.com", "chat.openai.com",
                                "generativelanguage.googleapis.com", "aiplatform.googleapis.com"})
SUFFIXES_FOURNISSEURS = (".anthropic.com", ".openai.com", ".amazonaws.com")


def _normaliser_hote(hote):
    hote = (hote or "").strip().lower().rstrip(".")
    if hote.startswith("[") and "]" in hote:  # IPv6 entre crochets
        return hote
    return hote.split(":", 1)[0]


def _normaliser_chemin(chemin):
    chemin = (chemin or "/").split("?", 1)[0].split("#", 1)[0]
    for _ in range(3):  # %252F → %2F → /
        decode = unquote(chemin)
        if decode == chemin:
            break
        chemin = decode
    while "//" in chemin:
        chemin = chemin.replace("//", "/")
    return chemin.lower()


def decision(hote, chemin):
    """Rend (permis, motif). `motif` est vide si permis."""
    h = _normaliser_hote(hote)
    c = _normaliser_chemin(chemin)
    if h in HOTES_FOURNISSEURS or h.endswith(SUFFIXES_FOURNISSEURS):
        return False, "contournement du relais : fournisseur de modèles"
    if h in HOTES_GITHUB_CHEMIN and c.startswith(PREFIXE_INTERDIT):
        return False, "copie publique du programme (R-561)"
    if h == HOTE_API_GITHUB and c.startswith("/repos" + PREFIXE_INTERDIT):
        return False, "copie publique du programme (R-561)"
    if h == HOTE_API_GITHUB and c.startswith("/search/") and "lciric" in unquote(chemin or "").lower():
        return False, "copie publique du programme (R-561), recherche"  # la requête compte ici, pas seulement le chemin
    return True, ""
