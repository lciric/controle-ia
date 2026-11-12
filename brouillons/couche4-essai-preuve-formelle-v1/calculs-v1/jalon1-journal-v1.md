# Jalon 1 du journal — rédacteur du devis de l'essai « preuve formelle contre suite bon marché » (couche 4) — v1

Heure relevée par `date -u` à l'écriture : mardi 10 novembre 2026, 13:09:53 UTC. Instantané de jalon, scellé dans le bac à sable ;
le journal final (`brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-journal-v1.md`) le reprend.

## Fait jusqu'ici
1. 13:00:30 UTC : consigne vérifiée (`5403571b…`, égale au compagnon), lue en entier, interdits communs v2 compris.
2. Lectures, empreintes égales aux compagnons : synthèse du tour 2 (`6ef6bc2e…`, lue en entier) ; synthèse v2 (`f0340581…`, lue en
   entier) ; programme complet v2 (`dffe0b63…`, l. 1–61, 142–264, 1319–1331 et lignes trouvées par recherche de « lean ») ;
   registre `registres/decisions.md` (registre vivant, `cbd3f950…` à 13:09:53 UTC) : R-920, R-946, R-957, R-959, R-2199,
   puis R-2200 à R-2226 filtrées par mots (couche 4, preuve formelle, Lean, N12, génération) ; `collisionneur_v8.py`
   (`22e5ed8a…`, l. 60–95 : table des prix).
3. 13:01:14 UTC : inventaire sans réseau — aucun vérificateur installé (lean, lake, elan, coqc, isabelle, agda, z3, cvc5,
   vampire, eprover, sage, maxima, gp : absents) ; pas de `~/.elan`, pas de cache de Mathlib ; `.venv` : Python 3.13.16,
   sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6, scipy 1.17.1, networkx 3.6.1 ; hypothesis, z3 absents ; machine : 4 cœurs,
   15 Go de mémoire, disque `/dev/vda` 252 Go dont **2,7 Go libres (94 % plein)**.
4. Prix : référence locale `claude-api` (table « Current Models (cached: 2026-11-03) ») pour Opus 5.5 (4 / 20 USD par million de
   jetons d'entrée / sortie), Fable 5.1 (10 / 50), Fable 5.2 (8 / 40), Sonnet 5.5 (2 / 10), Haiku 5.5 (0,10 / 0,50) — à vérifier
   sur la page publique ; `collisionneur_v8.py` l. 77 (Kimi K3.1 Pro 2 / 10, « vérifiés le 30 octobre »), l. 73–74 et 80–82
   (Gemini 4 Argon et GPT-6 Astra 10 / 50, SUPPOSÉS hauts).
5. Calculs par script dans le bac à sable : `calculs_devis_essai_v1.py` (`6f374d0c…`), sortie `7fb79ee3…` ; puis
   `calculs_devis_essai_v2.py` (`d57e176b…`, contrôle des graines confié à Gemini Argon, hors des familles des bras), sortie
   `d6492d79…` (sections 1 et 2 identiques à la v1).
6. Repérage, sans ouverture : la « carte des hypothèses v1 » (`f7dfe5fd…`, L0 et 21 lemmes) est citée par
   `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` (`186173d9…`, l. 386, 438, 807 : « Vérification formelle (Lean)
   du lemme maître L0 et des 21 lemmes | conv-audit | à ouvrir ») ; elle n'est pas dans les fichiers suivis de `main` ; son dossier
   est touché par les commits `444bfff13` et `9778cd6f3` (sous `brouillons/canal-reprise-releve-v1/envois/theorie-v1/`) ; non ouverte.

## Choix déjà faits (rédacteur), à reprendre au brouillon
- Contrôle de la graine saine par une famille hors bras (Gemini Argon) : sinon la sélection des graines par la famille qui relit dans
  la suite (Kimi) favoriserait la suite sur les fausses alertes.
- Sceau par jalons dans le bac à sable sous noms versionnés : `scellement sceller` refuse d'écraser une empreinte (R12) ; les deux
  fichiers de sortie sont scellés une fois, à la fin.

## Exposition et limites
Aucun chemin des interdits ouvert ; aucune recherche récursive sur un dossier contenant un chemin interdit sans exclusion (recherches
par `git grep` avec exclusions de `docs/notes/bras-attaque`, `diag`, `runs`, `donnees`, du script d'extraction de T0.6, ou dans des
fichiers nommés) ; `git log --all -- '*carte-des-hypotheses*' '*carte-hypotheses*'` a listé des noms de fichiers de la branche du
canal, rien n'a été ouvert. Aucun appel de modèle, aucun réseau, aucune dépense.
