"""Harnais d'épisodes et de journalisation des activations (T0.4).

Modules : `modeles` (modèle et tokeniseur jouets hors ligne, liste blanche des modèles réels, réglages de
déterminisme), `activations` (crochets sur le flux résiduel, passe avant unique, vecteur d'action par
maximum, garde d'équivalence), `episode` (épisodes indexés par agent et par pas, génération à graine
explicite, empreintes de rejeu), `sondes` (scores d'action en ligne, maximum ou attention sur les
jetons, garde « en ligne = hors ligne »), `stockage` (estimation), `run_harnais_factice` (bout en bout).
"""
