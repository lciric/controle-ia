# Devis — épreuve de l'étiqueteur — v4 (par phase, plafond accordé de 300 dollars)

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, 7 novembre 2026. Pièce du brouillon 5 du préenregistrement `preenregistrement-epreuve-etiqueteur-v1-brouillon5.md` (même dossier). Remplace, pour ce brouillon, `devis-epreuve-etiqueteur-v3.md`, qui reste tel quel (R12).
- **Pourquoi une v4** : le directeur a accordé **300 dollars** pour la phase 1, et non les 400 proposés (GO-2026-11-07-07) ; la contre-lecture du delta du brouillon 4 demande d'écrire les réglages de lancement du relais de Kimi (`--max-appels`) et de dire ce que le plafond fait au feu vert de l'essai de format.
- **Statut** : estimation, **non opposable**. Prix de Kimi (2 et 10 dollars par million de jetons) vérifié par la contre-lecture 1 sur la page de prix versée au dépôt (`pricing_chat.html`, `a26c7080…`). **Prix d'Argon : toujours à vérifier** : la page publique des prix de Google (`ai.google.dev`) n'est pas joignable depuis cette session (hôte hors du réseau permis) ; le barème volontairement haut du programme (10 et 50) reste celui de la garde.
- **Repères** : ceux du préenregistrement.

## 1. Phase 1 — lecteurs modèles seuls, en deux lancements

Les estimations ne changent pas depuis le devis v3 (mêmes consignes rendues, mêmes réglages gelés ; script `devis_phase1_v3.py`, `b4876e733635148b6ee74cb5a41cf6a4ddef8dd342c7ec4b0ef5f54e1b50853d`) :

| lancement | central | haut | prudent |
|---|---|---|---|
| essai de format (21 appels par lecteur) | 7,6 dollars | 13,7 | 25,1 |
| lecture principale et relecture (479 appels par lecteur) | 176,9 | 315,6 | 574,9 |
| **phase 1** | **≈ 185** | **≈ 329** | **≈ 600** |

### Plafond accordé : 300 dollars (GO-2026-11-07-07)

- Le script de lecture (`lire_items_phase1_v3.py`) refuse tout `--plafond-dollars` au-dessus de 300 ; le second lancement doit passer le **même** plafond que l'essai de format et une dépense déjà engagée au moins égale à la sienne (contrôlé par le script).
- **Feu vert de l'essai de format** : la lecture principale extrapolée (coût moyen mesuré par appel, majoré de 25 %, fois 479 appels par lecteur) doit tenir dans 300 dollars moins la dépense de l'essai de format. Le seuil vaut donc environ **(300 − F) / 1,25 dollars de lecture principale mesurée**, F étant la dépense de l'essai de format : **234 dollars** si F vaut 7,6 (centre), **229** si F vaut 13,7 (haut).
- Lecture : **l'hypothèse centrale passe** (1,25 × 176,9 = 221 ≤ 292) ; **l'hypothèse haute donne un feu rouge** (1,25 × 315,6 = 394,5 > 286) ; entre les deux, tout dépend des jetons mesurés. Un feu rouge n'engage rien de plus que l'essai de format : il appelle un nouveau devis ou une décision du directeur.
- La borne prudente (600) n'est pas couverte : la garde arrête avant de franchir 300 ; un arrêt en cours de lecture principale laisserait plus de 2 % d'items non lus, donc aucun verdict ; c'est ce que le feu vert sur extrapolation doit éviter.

### Relais de Kimi (version 4) : réglages de lancement

| lancement | `--max-appels` (au moins) | `--plafond-usd` | `--modeles-permis` |
|---|---|---|---|
| essai de format (20 items de formation) | 100 (5 tentatives par item) | 300 | `kimi-k3.1-pro` |
| lecture principale et relecture (456 items) | 2 280 | 300 moins la dépense de l'essai de format | `kimi-k3.1-pro` |

Le défaut du relais (64 appels) ferait échouer la lecture principale dès le 65e appel. En mode réel, le script exige `--relais-max-appels` au moins égal à cinq fois le nombre d'items du lancement, et l'écrit au manifeste ; une réponse 402 du relais (son plafond atteint) arrête le lecteur Kimi.

### Durée

Inchangée depuis le devis v3 : un jour pour la génération, le tirage et le dépôt ; moins d'une heure pour l'essai de format ; un jour pour la lecture principale ; deux à trois jours pour l'analyse et le verdict.

## 2. Phase 2 — humains sur 80 items (seulement si la phase 1 valide)

Inchangée : 37,6 à 60,5 heures (centre 48,6), soit **≈ 1 500 à 3 630 euros** (centre 2 430) à 40 à 60 euros de l'heure, hors charges, taxes et frais de paiement.

## 3. Résumé

| ligne | fourchette | plafond |
|---|---|---|
| phase 1 | ≈ 185 au centre ; 329 en hypothèse haute ; 600 au plus prudent | **300 dollars, accordé** (GO-2026-11-07-07) ; feu vert si la lecture principale mesurée reste sous ≈ 229 à 234 dollars |
| phase 2 (conditionnelle) | ≈ 1 500 à 3 630 euros, centre 2 430 | à fixer par le directeur |
