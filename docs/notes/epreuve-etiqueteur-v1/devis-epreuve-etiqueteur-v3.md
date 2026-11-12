# Devis — épreuve de l'étiqueteur — v3 (par phase, réglages gelés)

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, 7 novembre 2026. Pièce du brouillon 4 du préenregistrement `preenregistrement-epreuve-etiqueteur-v1-brouillon4.md` (même dossier). Remplace, pour ce brouillon, `devis-epreuve-etiqueteur-v2.md`, qui reste tel quel (R12).
- **Pourquoi une v3** : la contre-lecture 1 du brouillon 3 (bloquants B2 et B3) a fait geler des réglages de lecteurs que le devis v2 ne comptait pas : Argon avec une pensée bornée à 8 192 jetons et provisionnée dans la garde ; Kimi sans température envoyée, `reasoning_effort` « high », `max_tokens` 32 000 (raisonnement compris).
- **Statut** : estimation, **non opposable** ; prix d'Argon **non vérifié** (barème volontairement haut du programme) ; prix de Kimi (2 et 10 dollars par million de jetons) vérifié par la contre-lecture 1 sur la page de prix versée au dépôt (`docs/notes/ideation-organisme-v1/relais-kimi-v1/doc-moonshot-lue-2026-10-30-v1/pricing_chat.html`, `a26c708041c8ee3c0d7012f9cebaf70103f1d22be19cc33add0e00c621760323`), non revérifié par moi. Chaque phase attend sa décision du directeur.
- **Repères** : ceux du préenregistrement (sections « Termes » des brouillons 1 et 2).

## 1. Phase 1 — lecteurs modèles seuls, en deux lancements

### Ce qui est compté

Les consignes réellement rendues (`epreuve_phases_v1.rendre_consigne`) sur la génération d'essai refaite par `generer_items_v2.py` (graine 20261107 ; items `f11ba2734f7a961c396aff11f7042283b03d7af3ce4ccf8545575bc8048dba62`) ; la réponse visible la plus longue que le format admet ; les plafonds gelés de `lire_items_phase1_v2.py`. Script : `devis_phase1_v3.py`, recopié à l'octet à l'annexe B du brouillon 4 (`b4876e733635148b6ee74cb5a41cf6a4ddef8dd342c7ec4b0ef5f54e1b50853d`). Appels : 5 % de secondes demandes ajoutés partout.

| lancement | appels par lecteur | jetons d'entrée par lecteur (central ; prudent) |
|---|---|---|
| essai de format, seul (`--lectures format`) | 21 | 0,088 M ; 0,117 M |
| lecture principale et relecture (`--lectures principale+relecture`) | 479 | 2,127 M ; 2,836 M |

Sortie par appel selon trois hypothèses :

| hypothèse | Argon (A) | Kimi (B) |
|---|---|---|
| **centrale** (celle de la contre-lecture 1) | réponse visible + 4 000 jetons de pensée | réponse visible + 8 000 jetons de raisonnement |
| **haute** | réponse visible + 8 192 (pensée au budget) | réponse visible + 16 000 (la moitié du plafond) |
| **prudente** (borne de la garde) | 8 000 + 8 192 = 16 192 (plafond et budget) | 32 000 (plafond) |

### Coût (dollars ; Argon 10 et 50, à vérifier ; Kimi 2 et 10)

| lancement | central A ; B | haut A ; B | prudent A ; B |
|---|---|---|---|
| essai de format | 5,64 ; 1,97 | 10,04 ; 3,65 | 18,18 ; 6,95 |
| principale et relecture | 131,47 ; 45,45 | 231,83 ; 83,75 | 415,99 ; 158,89 |
| **phase 1, deux lecteurs** | **≈ 185** | **≈ 329** | **≈ 600** |

### Plafond proposé et garde

- **Plafond de la phase 1 proposé : 400 dollars** (au-dessus de l'hypothèse haute, sous la borne prudente). La garde réserve, avant chaque tentative, son pire cas (entrée à 3 caractères par jeton ; sortie et pensée à leurs plafonds) et s'arrête avant de franchir le plafond ; le plafond vaut pour la phase entière : le second lancement part avec `--depense-engagee` égale à la dépense de l'essai de format.
- **Feu vert de l'essai de format** (contrôle écrit par le script) : aucune réponse tronquée, aucun item de formation illisible, aucune pensée au-delà du budget, aucune sortie au-delà de la réserve, et la lecture principale extrapolée (coût moyen mesuré par appel, majoré de 25 %, fois 479 appels par lecteur) tient dans le reste du plafond. Sinon, feu rouge écrit : nouveau devis au directeur, sur les jetons mesurés.
- Un arrêt de la garde en cours de lecture principale laisserait plus de 2 % d'items non lus, donc aucun verdict : c'est la raison du feu vert sur extrapolation, et du plafond au-dessus de l'hypothèse haute.

### Durée

Génération, tirage et dépôt chez le tiers : un jour. Essai de format et contrôle : moins d'une heure. Lecture principale et relecture : un jour (deux fils, un par lecteur ; raisonnement long chez Kimi). Analyse et verdict : deux à trois jours.

## 2. Phase 2 — humains sur 80 items (seulement si la phase 1 valide)

Inchangée depuis le devis v2 (section 2) : 37,6 à 60,5 heures (centre 48,6), soit **≈ 1 500 à 3 630 euros** (centre 2 430) à 40 à 60 euros de l'heure, hors charges, taxes et frais de paiement (à vérifier par le directeur, T-7). Arithmétique revérifiée par la contre-lecture 1.

## 3. Résumé

| ligne | fourchette | plafond proposé |
|---|---|---|
| phase 1, essai de format | ≈ 8 (central) à 25 (prudent) dollars | dans le plafond de la phase |
| phase 1, principale et relecture | ≈ 177 (central) à 575 (prudent) dollars | dans le plafond de la phase |
| **phase 1, total** | **≈ 185 au centre ; 329 en hypothèse haute ; 600 au plus prudent** | **400 dollars** |
| phase 2, humains (conditionnelle) | ≈ 1 500 à 3 630 euros, centre 2 430 | à fixer par le directeur |

Par rapport au devis v2 (45 dollars au centre, 275 au plus prudent), la phase 1 coûte environ quatre fois plus au centre : le raisonnement des deux lecteurs, désormais compté et borné, domine la sortie.
