# Contre-lecture neuve (R2) du lanceur T0.6 v4 (delta v3 → v4) et des ordres E2 et E3 — v1

## Consigne (message de la session mère, recopié mot pour mot)

> Mère — 09:20 UTC, 7 novembre. On continue ici (R-1649). Deux contre-lectures neuves (R2), dans l'ordre ; **recopie ce message mot pour mot en tête de chaque rendu** (il tient lieu de consigne). Sans clé, sans dépense, rien d'existant modifié, aucun `.sha256`.
>
> (A) **Protocole d'audit de fuite**, 30 minutes : `brouillons/audit-fuite-r1-v4-v1-brouillon1.md` (sur `main`, `3f009795…`, écrit par la fille 11 après lecture des deux verdicts, ce qui est déclaré). Questions : la règle de décision est-elle fermée, chiffrée, écrite avant tout calcul et symétrique (elle peut aussi conclure « lecture du sabotage » ou « non tranché ») ? Les bras A1 à A4 répondent-ils à la question des verdicts (coût gonflé ou consigne ; témoins à 27 %) avec le code existant ? Les seuils, fixés après lecture, sont-ils défendables ? Que manque-t-il pour sceller (code d'audit, marqueurs) ? Rendu : `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/contre-lecture-audit-fuite-v1/` (verdict, couples sur le brouillon 1).
>
> (B) **Lanceur T0.6 v4 et ordres E2/E3**, 60 minutes : branche `prep/t06-lanceur-v2` à `b41a3f2d`, rapport `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v4.md` (`028187c3…`), delta v3 → v4 (C-V4-1, C-V4-2, C-V4-3, `T06_REGISTRE_GO`), puis les brouillons `brouillons/ordres-t06-e2-e3-v1/ordre-fille-6-t06-e2-v1.md` et `…-e3-v1.md` : sont-ils exécutables à la lettre par une session qui porte les clés (commandes exactes, clés par nom, GO-2026-11-06-01 cité, plafonds E2 ≤ 1,5 USD, E3 ≤ 3,5 USD, cumul ≤ 5, registre de `main`, arrêts, destruction par l'identifiant) ? Ce qui peut faire perdre l'argent ou la course ? Rendu : `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v4/` (verdict, couples pour les ordres, corrections de code éventuelles).
>
> Pousse chaque rendu sur `prep/fille-9-contre-lectures-v2` et envoie-moi un message après chacun.

## Verdict

**Ordres E2 et E3 : exécutables après couples** (7 couples sur E2, `couples-ordre-e2-v1.json` ; 1 sur E3, `couples-ordre-e3-v1.json`). Un **risque majeur pour la course** ne se règle pas par couple : il demande une vérification à 0 USD avant la première création, puis peut-être une correction de code (C-V5-1 ci-dessous).

Le delta v3 → v4 est conforme sur C-V4-1, C-V4-2, C-V4-3 et `T06_REGISTRE_GO`. Essais v4 rejoués : **85 passed** en 217,93 s (cinq fichiers `tests/test_t06_v4_*.py`, `--basetemp` propre, supprimé). Ce compte correspond aux 10 + 8 + 2 + 12 + 53 du rapport.

- Lecteur : fille 9 (lignée Claude Opus 5.5 ; l'auteur, la fille 10, est sur Sonnet 5.5). 7 novembre 2026, de 09:24 à 09:31 UTC (`date -u`).
- Pièces : branche `prep/t06-lanceur-v2` à `b41a3f2d` ; rapport v4 `028187c3…` (empreinte recalculée égale) ; les deux ordres ; `scripts/lancer_t06_v4.sh` (sous-commandes `creation`, `surveillance`, en-tête) ; `.claude/hooks/garde_calcul.py` ; `session_v3.main` ; les essais v4 ; `registres/go.md` de `main` (`12b850fe`, l. 257) ; `registres/decisions.md` (R-577, R-578) et `registres/depenses.md` de `main`.
- Rien loué, aucune clé lue, aucun `vastai` lancé, aucune dépense.

## Ce qui peut faire perdre l'argent (corrigé par couples)

1. **La surveillance refuse de tourner sans `HF_TOKEN` (couple E2-1 ; grave).**
   - `surveillance` exige `${#HF_TOKEN} -ge 8` et `${#CONTROLE_IA_GITHUB_TOKEN} -ge 8`, sans condition de mode : « jetons absents ou trop courts : masquage impossible, surveillance refusée », code 2.
   - L'ordre d'E2 ne transmet pas `HF_TOKEN` (« n'est pas utilisé par E2 »). L'instance A serait donc créée puis laissée sans surveillance, et la garde de dépense de `surveillance` ne jouerait pas.
   - L'échéance de la minuterie vaut par défaut la fin du GO, 2026-11-11 00:00 UTC (`fin_go_utc_s=1794355200`) : une instance échappée pourrait tourner jusque-là.
   - Aucun essai ne couvre `surveillance` en épreuve sans `HF_TOKEN`.
   - Couple : passer `HF_TOKEN` par son nom, comme à E3. Correction de code facultative : C-V5-2.
2. **Redémarrages sans surveillance (couple E2-6).**
   - Après `FIN`, `surveillance` sort, et son dossier garde la fin du premier run : la relancer après un `vastai start` la ferait sortir aussitôt.
   - Les étapes 6, 7 et 8 redémarrent pourtant A, B et C sans relève. Couple : relève à la main toutes les 5 minutes, et destruction par l'identifiant si l'instance n'est ni arrêtée ni détruite 20 minutes après le démarrage.
3. **« Dépense antérieure » non définie (couple E2-4).** « coût relevé de A » ne dit ni la source ni le calcul, alors que c'est l'entrée de la garde de plafond de B et de C. Couple : la facture, sinon les prix de `lancement.txt` × heures + forfait, le plus grand des deux, calcul écrit.
4. **Marge d'E3 (couple E3-1).** 1,30 USD/h × 2,5 h + stockage + téléchargement ≈ 3,4 USD : à 3,5 USD, `surveillance` arrête l'instance et le run est perdu. Couple : estimer sur 3 h, ce qui impose une offre à environ 1,1 USD/h au plus.

## Ce qui peut faire perdre la course (0 USD)

5. **Relecture de l'offre par identifiant (risque majeur, non corrigé par couple).**
   - `creation` relit l'offre par `vastai search offers "id=$OFFRE" --storage $DISQUE --raw` (C-V3-3).
   - Or R-577 (27 octobre) consigne : « sa relecture d'offre `search offers "id=N"` rend une liste vide sous vastai 1.8.3 pour toute offre » ; et R-578 : « l'identifiant d'une même offre change d'une requête à l'autre ».
   - Je ne trouve dans les registres de `main` aucune preuve ultérieure que cette relecture fonctionne. Les essais la simulent avec un faux `vastai`, et le rapport v4 le dit (risque 1).
   - Si R-577 tient encore, chaque `creation` refuse : code 2 ou 3, rien créé, pas d'argent perdu. E2 et E3, puis la course, ne partent pas.
   - Couple E2-7 : jouer cette relecture seule, à 0 USD, aussitôt après la recherche de l'étape 3 ; liste vide ou identifiant changé → aucune création, message.
   - Correction de code **C-V5-1**, si le défaut se confirme : choisir l'offre dans la liste du filtre, relue juste avant la création, comme `lancer_banque_t05_v3.sh` (R-578), et l'éprouver sur un cas sain réel. Sans elle, la course du 11 novembre est exposée.
6. **Garde de calcul et registre (couple E2-2).** L'étape 2 vérifie le GO dans `registres/go.md` du clone au commit, pas dans `$REGGO` comme le veut R-1626. Couple. Le reste est conforme : `creation` exige `T06_REGISTRE_GO` pour une épreuve, et la garde de `creation` lit le registre du dépôt cloné, que `controles-epreuve` vérifie.
7. **Clone de la branche d'essai (couple E2-3).** « à la manière de l'amorce » n'est pas une commande. Couple : le même moyen que le clone du préalable 1, sans jeton dans l'URL.
8. **Échéance de C (couple E2-5).** « création + DUREE_A − 20 s » : l'heure de création n'est pas connue quand on passe l'argument. Couple : `date -u +%s` au lancement de `creation` + 60 s + DUREE_A − 20 s.
9. **`vastai` hors du PATH (note).** Une note d'inventaire de `main` (`carte-inventaire-v1.json`, l. 754) relève « vastai 1.8.3, pas sur le PATH ». `creation` et `surveillance` utilisent `${VAST:-vastai}` : la session qui exécute doit mettre le dossier de `vastai` dans `PATH`, ou poser `VAST=<chemin>`. La mère peut l'ajouter au préalable 3 des deux ordres.

## Conformité des ordres à la liste de la mère

| exigence | E2 | E3 |
|---|---|---|
| commandes exactes | oui, après les couples 3 et 5 | oui |
| clés par leur nom | oui, après le couple 1 (`HF_TOKEN` ajouté) | oui (trois clés) |
| GO-2026-11-06-01 cité | oui (registre de `main`, l. 257 : 5 USD, E2 et E3 cumulés, échéance 2026-11-10) | oui |
| plafonds | 1,5 USD (configuration, `creation`, `surveillance`), cumul par instance | 3,5 USD ; cumul E2 + E3 ≤ 5 vérifié à la main avant création |
| registre de `main` | oui, après le couple 2 | oui |
| arrêts | deux attendus manquants ; `ARRET depense` ou `ARRET mort` → destruction ; aucune seconde création après « incertaine » | idem ; suite en échec → pas de destruction sans accord |
| destruction par l'identifiant | oui (R10, partout) | oui |

## Delta v3 → v4 du code (lu, avec essais)

- **C-V4-1.**
  - Verrou de fin de run (`flock -w 1500`) ; `commit_verifie` à trois codes ; `git status --porcelain` vide avant la fin normale ; consignation de la minuterie portée à 2 400 s.
  - Lu dans le rapport et dans les essais `-k c_v4_1`, qui sont nommés. Je ne l'ai pas relu ligne à ligne dans l'amorce (421 lignes).
- **C-V4-2.** Essai d'égalité sur 256 jetons réels : clé booléenne sans valeur implicite ; un échec met le couple en « échec ». La mesure réelle vient à E3 (E3-9).
- **C-V4-3** (`creation`, lu ligne à ligne). En épreuve :
  - `T06_REGISTRE_GO` exigé ; GO et plafond de la configuration égaux à ceux des contrôles ;
  - branche `essai/` imposée ; plafond du GO de 5 USD ;
  - `T06_EPUISEMENT_SIMULE_S` refusé hors épreuve ;
  - commande de création sans valeur de clé (`\$HF_TOKEN`, `\$CONTROLE_IA_GITHUB_TOKEN`), passée à la garde de calcul avant d'être imprimée.
- **Cosmétique (C-V5-3)** : `surveillance` écrit « dépense cumulée ≥ 200 USD » dans `surveillance.txt` alors que le seuil appliqué est le plafond de la configuration (`PLC`). C'est trompeur pour qui relit le journal.

## Corrections de code proposées (versions neuves, R12)

- **C-V5-1** (si R-577 se confirme à l'étape 3 d'E2) : relecture de l'offre par la liste du filtre, choix en Python juste avant la création, comme R-578 ; essai sur cas sain réel, à 0 USD, par lecture seule.
- **C-V5-2** (facultative, si l'on ne veut pas transmettre `HF_TOKEN` à une instance jouet) : `surveillance` n'exige `HF_TOKEN` que si `mode` vaut `reel` dans `lancement.txt`, et masque les clés présentes ; cas sain et artefact.
- **C-V5-3** : message de `surveillance` au plafond réel.

## Couples

- E2 (7, chaque « ancien » unique dans `ordre-fille-6-t06-e2-v1.md`, vérifié par script, appliqués dans l'ordre) : 1 clés et `HF_TOKEN` ; 2 registre `$REGGO` à l'étape 2 ; 3 clone de la branche ; 4 dépense antérieure ; 5 échéance de C ; 6 relève après chaque redémarrage ; 7 relecture par identifiant avant toute création.
- E3 (1) : marge de 3 h dans le choix de l'offre.
