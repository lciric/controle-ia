# Fille 6 — rapport de mise en place — v1

Session `session_01Qi7Gr4zGhZnVxbujN7yWBm`, 5 novembre 2026, 15:20 à 15:23 UTC (`date -u`). Base : main `4543224`.

- vastai 1.8.3 installé dans `/home/user/venv-vastai`.
- Jeton `CONTROLE_IA_GITHUB_TOKEN_2` : préfixe classic ; accès au dépôt 200 ; en-tête d'échéance rendu : 2026-11-05 18:01:59 UTC.
- **Mesure non valable** : le mandataire réseau du conteneur injecte son propre jeton pour api.github.com. Sans aucun en-tête : 200 sur le dépôt privé, même échéance, même limite de 15000 requêtes. Avec un faux jeton : 200, même échéance. Cette échéance est celle du jeton de la session, pas celle du jeton de Lazar (R-1565 a sans doute lu la même chose).
- Inventaire filtré (`hote_durable_a1_v3_v4.py` du commit 096d87fa, extrait dans un brouillon hors clone ; le dossier de l'étape 0 n'est pas créé) : seules les trois instances R8 (58936096, 58936099, 58936100), arrêtées.
- **Arrêt avant le préalable 4** : rien loué, aucune dépense. Message envoyé à la mère à 15:23 UTC, avec une recommandation : Lazar confirme l'échéance lue dans les réglages de GitHub.
