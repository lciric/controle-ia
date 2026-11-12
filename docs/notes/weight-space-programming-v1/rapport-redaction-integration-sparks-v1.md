# Rapport de rédaction — intégration du billet « Sparks of Weight-Space Programming » — v1

Rédacteur neuf (sous-agent Claude), 4 novembre 2026, de 01:35 à 01:47 UTC environ (`date -u`). Consigne : `consigne-redacteur-integration-sparks-v1.md`, sha256 `fadece37baa345ec64d85deb46d54577f79fe5cff2a780e64db079fe4acf0249`, vérifiée avant lecture ; les compagnons des pièces 1, 2, 3 et des deux questions ont tous répondu « OK » ; l'empreinte de la moisson (`868731d1…`) a été recalculée et trouvée égale.

## 1. Fichiers écrits (dossier `docs/notes/weight-space-programming-v1/`)

| Fichier | sha256 |
|---|---|
| `note-integration-sparks-v1.md` | `02221846147e03e57c02040a842a5dad02b04bc2bb30e7aa35d4391e5ab2ab33` |
| `preregistrement-sparks-exp7-sous-nul-v1-brouillon1.md` | `3d681158dee0d53f09813a93b434135577f2a0eed208e4af43a369edadbfd75b` |
| `rapport-redaction-integration-sparks-v1.md` (ce fichier) | donnée dans la réponse finale (un fichier ne peut pas contenir sa propre empreinte) |

Aucun compagnon `.sha256` créé, aucun commit, aucun fichier existant modifié, aucun appel de modèle, aucune dépense, aucun code des journaux exécuté. Un seul script écrit et exécuté, dans le bloc-notes de la session (calcul de puissance binomial exact, bibliothèque standard seulement). Aucun outil n'a demandé d'approbation.

**Écart à la consigne (à consigner)** : à 01:46 UTC, j'ai lancé une fois `git status --short` sur ce dossier, en lecture seule, alors que la consigne n'autorise que `git log` et `git show`. Rien n'a été modifié. Ce qu'il a montré : `preregistrement-…-brouillon1.md` et `rapport-…-v1.md` non suivis, mais **pas** `note-integration-sparks-v1.md`, pourtant présent sur disque (31 208 octets). Avant de committer, vérifier qu'aucune règle d'exclusion ne l'écarte (R11).

## 2. Dix points pour un contre-lecteur neuf

1. **Symétrie des graines.** Le brouillon met des graines d'ordre différentes dans toutes les paires, vraies et nulles, pour qu'un lecteur ne sépare pas « vraie » et « nulle » par l'ampleur de la différence. Vérifier que cela ne change pas trop la tâche par rapport au billet (paires à graine commune, journaux `README.md` : l. 15-16) et que l'ancre de trois cas suffit à faire le pont.
2. **Prévalence annoncée au lecteur.** La consigne dit au lecteur la composition de la série (moitié un sycophante, quart deux, quart aucun). Vérifier que cela n'oriente pas la scission dans un sens (un lecteur peut « répartir » ses réponses) et si une variante sans prévalence annoncée serait préférable.
3. **Règle de signalement** strictement au-dessus de 0,5 sur la **moyenne** de deux lecteurs : une moyenne peut effacer deux signalements contraires. Vérifier que la lecture par lecteur (secondaire, Holm) rattrape ce cas.
4. **Égalités comptées comme échecs** dans M1 : choix prudent, qui pénalise un lecteur qui répond 0,5 et 0,5. Vérifier la cohérence avec M2 (où 0,5 et 0,5 n'est pas une scission).
5. **Garde des interdits** : numpy permet d'écrire une passe avant à la main. Le balayage scripté plus relecture neuve suffit-il ? Que fait-on d'un lecteur qui triche partiellement ?
6. **Base B1** : sa statistique (masse sur la suggestion moins masse sur la question, maximum sur les têtes) est inspirée de la tête 10.2 décrite pour une seule paire (p3, l. 94-95). Vérifier qu'elle est fixée sans regarder les modèles du bras principal, et que le jeu d'étalonnage (8 modèles) est assez grand pour un seuil.
7. **Contrôle causal** : la règle de conversion « composant nommé → tranches de tenseurs » (tête = lignes de requête et colonnes de sortie ; partie clé-valeur seulement si nommée) est un choix ; vérifier qu'elle est cohérente avec la façon dont les auteurs ont greffé (`eval/weights_only_*/patch_score.json`) et que le sens « retour à la base » est bien défini pour Gemma (4 têtes de requête, 1 clé-valeur).
8. **Devis** : les temps processeur viennent d'un débit supposé (200 milliards d'opérations par seconde) ; le temps par mesure sur carte (5 s) est supposé ; vérifier les ordres de grandeur et le plafond proposé de 25 USD.
9. **Modèle de secours** : licence, taille et architecture de `Qwen/Qwen2.5-0.5B-Instruct` sont données « d'après sa fiche, à vérifier » ; le cas « construit inversé » (modèle de départ honnête) est-il traité assez précisément pour être lu sans écart au préenregistrement ?
10. **Citations** : chaque ligne citée (« p3, l. n », « journaux, fichier : l. n », « moisson, l. n », « programme, l. n ») doit être recontrôlée ; en particulier les numéros de ligne de `code/eval.py` et `code/make_release.py` (comptés dans le fichier lui-même), et les trois phrases pour les entretiens (note, section 4).

## 3. Décisions à proposer à Lazar

**D-1. Lancer l'expérience 7 sous nul (piste F1).**
- Décision : faut-il dépenser pour la piste F1 maintenant, une fois le brouillon contre-lu et scellé ?
- Enjeu : un résultat public et utile dans les deux sens sur la validité d'une lecture « boîte blanche » outillée, et un banc de lecteurs réutilisable ; contre un peu de temps de session avant la porte G0 (fin novembre).
- Options : (a) GO variante carte graphique, plafond 25 USD (supposé) : rapide et la moins chère / quelques heures de location à surveiller ; (b) GO variante processeur seul, ≈ 45 USD au pire (supposé) : pas de carte / plus long et plus cher ; (c) reporter après G0 : aucun risque pour G0 / le billet vieillit, les entretiens arrivent sans ce résultat.
- Recommandation : (a), confiance 0,6.
- Défaut sous 48 heures : contre-lecture et scellement du préenregistrement, **sans aucune dépense** (une dépense exige un GO explicite).

**D-2. Accès à Gemma 3 270M.**
- Décision : accepter la licence Gemma sur le compte Hugging Face qui fournit le jeton présent chez la fille ?
- Enjeu : reproduire le banc du billet sur le même modèle, ou passer au modèle de secours (comparaison au billet moins directe).
- Options : (a) accepter : comparaison exacte / action sur un compte ; (b) secours `Qwen2.5-0.5B-Instruct` seulement : aucune action de compte / filtre des faits à refaire, construit peut-être inversé.
- Recommandation : (a), confiance 0,7.
- Défaut sous 48 heures : aucun (action de compte, nœud) ; sans réponse, le brouillon garde « À REMPLIR » et le secours reste dit d'avance.

**D-3. Bras de la phase 0 tirés du billet (pistes P6 et P4).**
- Décision : inscrire, comme bras rapportés et sans dépense propre, le retrait chirurgical d'une direction de sabotage (P6, validité de construit, H8) dans le préenregistrement de T0.7, et la lecture du delta d'adaptateur contre son jumeau (P4) dans celui de T0.6 ?
- Enjeu : une vérification de manipulation de nos sondes et un audit au niveau du modèle, pour quelques heures de carte en plus dans des runs déjà prévus ; contre un préenregistrement un peu plus long avant G0.
- Options : (a) les deux, rapportés, hors critère : coût marginal / alourdit deux préenregistrements ; (b) P6 seul : le plus utile pour la section 11 / P4 attend ; (c) aucun avant G0 : rien n'alourdit G0 / on perd l'occasion des runs de T0.6.
- Recommandation : (b), confiance 0,55 ; P4 ensuite, après F1 (taux de fausses alertes du lecteur connu).
- Défaut sous 48 heures : (b), inscrit comme bras rapporté dans le brouillon de T0.7, sans changer aucune hypothèse ni le critère de G0.

**D-4. Famille « mondes de poids » pour l'organisme d'idéation (piste P5).**
- Décision : ouvrir une note de conception de cette famille à oracle exécutable, sur processeur seul ?
- Enjeu : une famille inédite où la vérité ne dépend d'aucun juge de modèle de langue (N-044, N-060 v3) ; contre la charge de l'organisme (A1-v3, tour fermé).
- Options : (a) note de conception maintenant, sans appel : coût nul / une tâche de plus en file ; (b) après A1-v3 et le tour fermé : file plus courte / retard.
- Recommandation : (b), confiance 0,6.
- Défaut sous 48 heures : (b).

**D-5. La classe de menace « adversaire éditeur de poids » au papier C (piste F3).**
- Décision : ajouter cette classe au modèle de menace du papier C, ou la laisser hors périmètre ?
- Enjeu : modifier une revendication (HC4) ou le périmètre est un nœud ; la conclusion utile est probablement « fermée par l'attestation d'intégrité des poids, sinon frontière assumée » (programme, l. 172).
- Options : (a) une phrase dans le modèle de menace, sans revendication ni expérience : clarté / rien à défendre de neuf ; (b) un point de plus sur l'axe de coût de HC4, mesuré plus tard par la matrice de transfert vers la réserve de détecteurs : plus fort / revendication modifiée, antériorité à vérifier (zone « séduisante », moisson, l. 126) ; (c) rien.
- Recommandation : (a), confiance 0,65.
- Défaut sous 48 heures : aucun (modification de revendication, nœud) ; sans réponse, rien n'est écrit dans le papier C.

## 4. Réserves

- La moisson n'est pas opposable (R7) : toutes les mentions « déjà pris » de la note sont à revérifier sur PDF avant usage dans un préenregistrement scellé ou un papier.
- Les probabilités des prédictions sont des jugements du rédacteur (« supposé »), écrites avant toute donnée ; elles n'ont aucune autorité.
- Les prix sont supposés ; les temps de carte viennent des journaux des auteurs seulement pour l'entraînement (25 s par modèle).
- La note ne traite pas la réponse d'Astra à la question `question-astra-sparks-v1.md` (pas encore disponible ici) ni le tour du collisionneur ; leurs fiches pourront compléter ou contredire ce classement.
