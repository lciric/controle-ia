# Ressources à demander à Lazar — v1

Rédigé le 2026-10-04. Classées par urgence.

| # | Ressource | Pourquoi | Pour quand | Forme |
|---|---|---|---|---|
| 1 | **Budget de recherches web de la session relevé** (variable `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`, par exemple à 1 000), ou une session neuve | Le budget de 200 s'est épuisé : la recherche d'antériorité est couverte pour 2607.08066, 2606.10456, le lemme et le théorème négatif seulement | tout de suite | réglage de l'environnement |
| 2 | **Accès réseau à arxiv.org et export.arxiv.org** (et si possible openreview.net, huggingface.co) | T0.2 exige des PDF empreintés, page citée (R7) ; G0 critère 8 ; T0.5 dépend du code de Terekhov et al. | tout de suite | réglages de l'environnement → Accès réseau → Personnalisé → domaines autorisés. À défaut : déposer les PDF à la main (liste dans `docs/anteriorite/anteriorite-transcription-v1.md`, section 5) |
| 3 | **Dépôt distant** du programme (nœud N-001) | Sans dépôt distant, le travail disparaît avec le conteneur. En attendant : paquet git complet fourni dans le rendu | tout de suite | ton choix ; recommandation : dépôt GitHub **privé** `lciric/controle-ia`, créé par moi sur ton GO, ou créé par toi puis donné à la session |
| 4 | **GO sur le devis de phase 0** (nœud N-002) | Sessions GPU 1 à 3 | avant le 12 oct. | une ligne dans `registres/go.md` : plafond 150 USD, échéance 2026-11-01 |
| 5 | **Jeton d'accès HuggingFace** (modèles à accès restreint : Llama-3.1-8B-Instruct, Llama-3.2-3B-Instruct ; licence Llama acceptée sur ton compte) | Téléchargement sur les instances GPU | avant la session 1 | secret de l'instance Vast.ai ou de l'environnement — jamais dans le dépôt |
| 6 | **Compte Vast.ai** | Les instances se lancent chez toi ; je prépare les scripts (arrêt par identifiant, R10) | avant la session 1 | si tu préfères que je lance : clé d'API en secret de l'environnement, et la garde de calcul bloque tout lancement sans GO consigné |
| 7 | **Corpus de pression de P3** | Corpus bénins pour g bénin (HC6) et intensités de pression (T0.9) | avant le 14 oct. | fichiers + empreintes |
| 8 | **Code de la loi d'attraction de P3** | Estimation de g par régression avec nul de régression vers la moyenne (T0.9) | avant le 14 oct. | dépôt ou archive + empreinte |
| 9 | **Outils de scellement de P3**, s'ils existent | Comparer à ceux de T0.1, harmoniser les formats | quand tu peux | archive |
| 10 | **Envoi du message aux auteurs de FakeLab** | Environnement (b) de la phase 3 | dès que possible | texte prêt : `message-fakelab-v1.md` |

Optionnel (contacts externes, je rédige sur demande) : autorisation de réutiliser le code sans licence d'Apollo Research (deception-detection) et de Bailey et collègues (obfuscated-activations). Par défaut, je réimplémente d'après les articles.
