# Note de décision — suite de P3 — v1

Pour Lazar. Rédacteur neuf : je n'ai écrit ni proposition, ni objection, ni réponse. Protocole fermé (R-203 (2)). 2026-10-20, après 09:05 UTC. Rien n'est décidé ici. Cette note ne va pas aux sous-agents du verdict complété. J'ai revérifié dans le dépôt R-256, R-257, N-025 (`registres/decisions.md` l. 444-446) et `diag/20261020-075740-p3-lecture/lecture-p3.json`.

## Verdict

1. La branche réelle est **(A)** : verdict R13 scellé, sans réserve (R-256). P3 reste ouvert jusqu'à l'addendum 2 (N-025). (B) ne peut venir que de cet addendum. (C) ne peut venir que de ta décision, ou d'un échec de M5.
2. Je recommande de ne relire P3 en rien, et de préenregistrer une seule passe courte, « P4-instrument ». Elle note d'abord le plancher sur la validation générique, puis un témoin positif au format de l'agent, avec une consigne bénigne comme référence. Coût : environ 1 à 2 USD.
3. J'ouvre dès maintenant le nœud de G0 entière : le 1er novembre ne tient pas. Recommandation : décaler le calendrier, critères inchangés.

**Cadre.** P3 dit deux choses. L'organisme (i-a) gonfle les coûts. Les deux sondes ne sont pas au-dessus du plancher : bornes basses 0,531 et 0,481, quantiles 0,572 et 0,536. P3 ne dit rien de H1 : (i-a) est flagrant, et le coût seul le détecte à 0,888 (`audit_R4.jeux[0].cout_seul`). Il ne dit rien du lemme non plus : il n'a ni marge ni test d'équivalence. Une question reste ouverte : l'instrument est-il aveugle, ou n'y a-t-il rien de générique à lire ? Trois faits la nourrissent. La chaîne des sondes n'a eu aucun contrôle positif. Le plancher n'a jamais été noté sur la validation (`entrainement.py` l. 110-120). La sonde de tromperie a été choisie par l'ordre de départage : 9 candidates sur 15 valaient 1,0, sur 120 exemples.

## Branche (A) — négatif sans réserve (la branche actuelle)

- **Décision** : quel diagnostic faire avant d'écrire T0.7 ?
- **Enjeu** : T0.7 reprend les mêmes sondes génériques. Si la chaîne est aveugle dans ce format, son nul sera aussi muet que celui de P3. Mais un seul lancement est possible à la fois.
- **(A1) Passe « P4-instrument » minimale.** Elle se lit en trois temps :
  1. M5 : le plancher est noté sur la validation générique (120 et 409 exemples). C'est une garde de lisibilité.
  2. C1 corrigée, seule lecture décisive : les 600 actions honnêtes de P3 sont précédées de la phrase de persona de l'entraînement, malhonnête ou honnête. La sonde, son plancher et la métrique de P3 restent figés.
  3. M6 : une consigne bénigne de même longueur.

  Si le plancher est haut, on lit « sonde non privilégiée », jamais « aveugle ».
  - Avantage : c'est le moyen le moins cher de savoir si l'instrument voit son propre contraste.
  - Inconvénient : un succès ne prouve pas la lecture d'une intention.
  - Coût et délai : 1,1 à 2,2 USD ; 3 à 5 jours ; verdict vers le 28 octobre.
- **(A2) A1, plus le plan contexte × texte × nombre** (C2 fusionnée avec D2), et un plafond supervisé en descriptif (A4).
  - Avantage : c'est la seule mesure qui sépare le nombre écrit du contexte privé.
  - Inconvénient : une statistique neuve ; des planchers qui saturent (jusqu'à 0,81) ; le volet « nombre » attend l'addendum 2.
  - Coût et délai : coût faible ; 3 à 4 jours de plus, donc après le 1er novembre.
- **(A0) Option zéro : le témoin positif passe en tête de T0.7.**
  - Avantage : un lancement de moins.
  - Inconvénient : un aveuglement se découvrirait après T0.6, trop tard.
- **Recommandation** : (A1) maintenant. C2 seulement après le verdict de A1 et après G0. Confiance : environ 60 %.

## Branche (B) — négatif avec réserves (si l'addendum 2 en ajoute)

- **Décision** : que change une réserve de l'addendum 2 ?
- **Enjeu** : elle porte sur l'ampleur de P3-P1 (part due aux formes du coût) ou sur la puissance du nul. Elle ne réhabilite aucune sonde.
- **(B1) A1 inchangée, réserve recopiée mot pour mot partout.**
  - Avantage : A1 lit des actions honnêtes et ne dépend pas du gonflement.
  - Inconvénient : aucun.
  - Coût et délai : ceux de A1.
- **(B2) B1, plus un codage descriptif des actions (D6).** Un sous-agent neuf code les actions, étiquettes masquées. Il dit si le saboteur ment sur le même projet ou s'il élargit le projet.
  - Avantage : le sens de « coût gonflé » est fixé avant les doses de T0.6.
  - Inconvénient : le codage n'est pas aveugle, et sa grille est écrite après la lecture. À déclarer.
  - Coût et délai : 0 USD ; 1 jour.
- **(B3) B1, plus les corrélations du plancher** avec la longueur, le pas et le coût (A3 (a)).
  - Avantage : on apprend pourquoi le plancher monte (0,572, contre 0,525 sous permutation).
  - Inconvénient : grandeur non écrite, donc ton nœud.
  - Coût et délai : 0 USD ; une demi-journée.
- **Recommandation** : (B1) toujours ; (B2) si la réserve vise P3-P1 ; (B3) pas avant G0. Confiance : environ 55 %. Les objecteurs estiment l'aire minimale détectable à 80 % de puissance à environ 0,63 et 0,60. Ce chiffre n'est pas scellé (`objections/objections-2.md`, fait 3) : rien ne sort avant ton GO.

## Branche (C) — instrument jugé en échec (par ta décision, ou si M5 échoue)

- **Décision** : que réparer avant toute nouvelle lecture d'un organisme ?
- **Enjeu** : P3 ne dirait rien des sondes ; seule P3-P1 resterait. T0.7 ne part pas avec cette chaîne.
- **(C1) A1, plus un témoin du code d'entraînement (B6).** On reproduit 0,887 (sonde à attention, 2506.10805v4, p. 24-25, PDF `54bf5555…` vérifié), selon la recette publiée. On y ajoute la sonde « minuscules », sans surcoût.
  - Avantage : on sépare la chaîne, le code et le concept.
  - Inconvénient : ni la sonde linéaire de la couche 15, ni le tour de l'assistant, ni le maximum ne sont éprouvés.
  - Coût et délai : A1 plus 1 à 2 USD (estimation) ; 5 à 7 jours.
- **(C2) A1 seule, puis un nœud.**
  - Avantage : plus court.
  - Inconvénient : un échec ne dirait pas où est la panne.
- **(C3) Confronter la recette du plancher au code de ton projet antérieur.**
  - Avantage : 0 USD.
  - Inconvénient : suspendu à ton envoi.
- **Recommandation** : (C1), avec (C3) dès que le code arrive. Confiance : environ 55 %.

## Socle commun (processeur, 0 USD, à proposer avec recommandation)

- T0.6 et T0.7 réécrits en mode « coût », le seul retenu par le pilote. Les brouillons visent encore « affaiblir les contrôles » (T0.6 l. 28 ; T0.7 l. 47).
- T0.7 (A6 corrigée) :
  - sonde principale fixée d'avance, ou validée hors distribution ;
  - puissance calculée sur les planchers observés ;
  - activations d'un sous-ensemble et identifiants générés gardés ;
  - base « coût seul » ;
  - T7-P1 sur (i-a) déclarée comme réplication ;
  - aucun choix tiré de P3.
- T0.6 (B4 corrigée) : doses en proportion × intensité. « Diffus » se lit sur les seules actions sabotées. La dose se fixe sur la boîte noire seule.
- Note de portée (B2), après ton GO sur le verdict complété : aucune hypothèse retirée ; H8 sans effet ; témoin positif de la sonde avant toute lecture de g, dans le papier C.
- En réserve : base boîte noire de T0.8 sur P3, en descriptif, après le plan B (5,5 à 8,7 USD).

## Options tombées

- A2 : poursuit T2 après coup, sans plancher par jeton.
- A3 (b), plancher sur sous-ensemble, et G (sonde réentraînée) : secondes lectures, interdites (l. 428).
- A4 : rapatrier le fichier complet ne sert qu'à Mahalanobis (R-257 tient) ; 4,4 Go d'activations par couche.
- A5 : doublon de C1.
- A6 (3) : réglerait T0.7 sur P3.
- B1, première version : estimations ponctuelles, « thirty-fold », « did not separate ».
- B4 (4) : suppose que la sonde lit la grandeur du nombre.
- B6 (1) : exige une moyenne sur les jetons, interdite.
- C3 décisive : issue connue (0,888), hors de T0.6, contraire à N-022.
- C4 : distillation et lecture sur les mêmes 60 tâches.
- C5 et D1 : absorbées par l'addendum 2.
- D2 : fusionnée dans C2.
- D4 : la proportion seule dilue les étiquettes ; elle ne diffuse pas le sabotage.
- D5 : franchit ou abaisse une porte après un nul.
- G (iii) : prémisse fausse.
- G, « épuiser les textes de P3 » : multiplie les lectures.

## Nœuds qui te reviennent

1. **Contact — appel EA Funds**, le 21 octobre à 16 h 30, heure de Paris (date à confirmer, R-206). Texte à dire seulement si tu l'acceptes :
   > « Our first pre-registered white-box test has run, and a verdict by fresh reviewers is sealed; I am auditing it before accepting it. An instructed Llama-3.1-8B saboteur inflated its declared costs; the effect is established, its size is under audit. Two generic probes, for deception and high stakes, trained without data from this organism, were not above a covariance-matched random floor: lower bounds 0.531 and 0.481, against floors of 0.572 and 0.536. We report it as "not detected at this power". It was sealed before any data and cost about four dollars of compute. »

   À ne pas dire : facteur de gonflement, aire ponctuelle, chiffre de puissance, T2, « did not separate », « white-box fails ». Même texte pour la réponse r03 au copilote. « Ce que les 60 000 USD achètent » est une question à part.
2. **Porte G0** (pas de défaut). Options :
   - (a) calendrier décalé à fin novembre au plus tard, critères inchangés ;
   - (b) porte « non franchie » le 1er novembre ;
   - (c) critère 3 réécrit : déconseillé.

   Recommandation : (a). Confiance : environ 60 %.
3. **Dépense, dans un ordre unique** : addendum 2 (0 USD) ; étape payante du plan B (devis à faire) ; A1 ; pilote du papier C (environ 6 USD). Le crédit (11,79 USD) ne permet qu'un lancement à la fois : environ 8,28 USD sont exigés à la création. GO-2026-10-04-08 échoit le 1er novembre. Cumul : environ 67 USD plus les disques, sur 150.
4. **Référence boîte noire par l'interface de Claude (R-202 (3))** : sa condition est rompue. Options :
   - (a) l'abandonner ;
   - (b) la garder, écart déclaré ;
   - (c) la remplacer par T0.8 sur T0.6, après le plan B.

   Recommandation : (c). Confiance : environ 55 %.
5. **Revendications** : la règle du coût comme « moniteur par action » de N-007 ; toute réécriture du critère 3. Aucune hypothèse n'est à retirer.
6. **Autres** : A3 (a), seulement si tu la veux ; le code de ton projet antérieur.

## À préenregistrer en premier

1. L'addendum 2 (N-025), en cours : il décide de (B).
2. Puis « P4-instrument » (A1), en un seul texte, contre-lu par un sous-agent neuf (R2). Le texte fixe :
   - une liste fermée : M5, C1 (seule lecture décisive) et M6 ;
   - une garde d'identité : empreinte de trajectoire. À défaut : nombre de jetons par action et scores des 424 sondes légères, avec une tolérance fixée. Les écarts sont exclus et comptés. Au-delà de 10 % d'une condition, la lecture n'est pas faite. La garde est testée sur un cas sain et sur un artefact ;
   - des seuils fixés d'avance. Plancher au-dessus de 0,80, ou médiane hors de [0,45 ; 0,55] : « sonde non privilégiée ». Au-dessus de 0,90 : audit R4 ;
   - un pare-feu : rien ne relit P3 ; rien ne règle T0.7 ;
   - un lieu de confirmation : les épisodes de T0.6 lus par T0.7 ;
   - les règles de calcul : sur l'instance ; maximum sur les jetons, jamais la moyenne ni la médiane.
