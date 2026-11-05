# Devis — rejeu de la cellule de juge redéfinie sur les 180 notations du pilote de T0.5 — v2

Écrit par un sous-agent de la lignée « session-depot » le 29 octobre 2026 (UTC), sous **GO-2026-10-29-04** (plafond
4 USD, échéance 5 novembre ; `registres/go.md`, l. 127). **Rien n'est lancé par ce document.** Pièces liées, dans ce
dossier : la fiche de lancement (`fiche-lancement-rejeu-juges-v2.md`, critères gelés) et la configuration
(`config-rejeu-juges-v2.json`). Code : `src/controle_ia/environnements/noter_rejeu_juges_v2.py` (importe la v1, qui
reste telle quelle), essais `tests/test_noter_rejeu_juges_v2.py`. Chaîne : `scripts/amorce_rejeu_juges_v2.sh`,
`scripts/rejeu_juges_instance_v2.sh`, `docs/procedures/rejeu-juges-v2/lancer_rejeu_juges_v2.sh`.

Statut des chiffres : RAPPORTÉ (lu dans un fichier cité, avec son empreinte) ; INFÉRÉ (calculé à partir de fichiers
cités) ; SUPPOSÉ (jamais mesuré sur ce banc). Aucun chiffre n'est opposable (R7).

## 1. Ce qui tourne

Une cellule redéfinie, sur les **mêmes 180 notations** (mêmes épisodes, mêmes textes : garde d'alignement de la v1,
clé à clé et par empreinte d'ensemble) :
- variante « verdict-echelles » : invite b0, puis la consigne v2 (dix lignes « NOM (lo to hi): <integer> », valeurs
  admises seules, s'arrêter après la dixième) ;
- génération bornée au bloc (arrêt de chaque ligne dès que la ligne du dixième critère est close), au plus 256 jetons ;
- lecture par la probabilité du jeton de verdict, valeurs admises seules (valeur suivie d'une fin de ligne), branches
  lues par le cache des clés et valeurs ;
- **8B en cellule décisive** (phase 1), **3B en cellule descriptive** (phase 2, seulement si le temps restant couvre
  sa durée maximale).

## 2. Rythmes de la v1 (référence)

RAPPORTÉ, `diag/20261029-021158-rejeu-juges-reel/resume.json` (branche `calcul/rejeu-juges-v1`, `a2af5d17…`) :

| phase v1 | durée | s par notation | pic de mémoire |
|---|---|---|---|
| 8B, verdict d'abord (192 jetons) | 1 101,1 s | 6,12 | 34,67 Gio |
| 3B, verdict d'abord (192 jetons) | 703,3 s | 3,91 | 31,40 Gio |
| 8B, b0 relu (lecture seule) | 219,6 s | 1,22 | 23,26 Gio |

Chargements : 8B 40,7 s, 3B 2,1 s. Instance de la v1 : 1,18 USD/h, de 01:50 à 03:21:40 UTC, **1,92 USD** au total
(RAPPORTÉ, `registres/depenses.md`, l. 227) ; démarrage, installation et suite ciblée ont pris ≈ 20 minutes (INFÉRÉ :
de la création à la fin de l'amorce, 89 minutes, moins 67 minutes de run et ≈ 2 minutes de poussées).

En v1, 179 des 180 réponses du 8B sont allées au plafond de 192 jetons (RAPPORTÉ, `rejeu-8B-verdict-d-abord.json`,
`4c95fbef…`, champ `jetons_reponse`) : le juge continue après le bloc. D'où ≈ 0,21 s par pas de décodage pour un lot
de 8 (INFÉRÉ : (1 101 − 180 × 1,2) s / (23 lots × 192 pas)) ; 3B ≈ 0,14 s.

## 3. Ce que la v2 coûte en plus et en moins

- **En moins** : la génération s'arrête au bloc clos. Le bloc à échelles fait 128 jetons au vrai tokeniseur du 8B
  (contre-lecture R2 ; supposé ≈ 130 au premier devis). Un lot s'arrête à sa ligne la plus longue ; plafond 256.
- **En plus** : la fin de ligne exigée demande une branche par valeur non écrite (≈ 40 par notation). Elles se lisent en
  prolongeant le cache d'un à trois jetons : ≈ 40 petites passes de ≈ 25 ms pour le 8B (SUPPOSÉ), plus une passe
  principale avec cache (≈ 1 s, comme b0 relu). Lire par passes complètes coûterait ≈ 40 passes de 10 000 jetons par
  notation : hors budget, d'où le cache.
- **Attendu** (SUPPOSÉ) : 8B ≈ 23 lots × (150 pas × 0,21 s + 8 × 2 s) ≈ 18 minutes (≈ 6 s par notation, le rythme de
  la v1) ; 3B ≈ 23 × (150 × 0,14 + 8 × 1 s) ≈ 11 minutes.
- **Pire** (SUPPOSÉ) : chaque lot au plafond de 256 pas : 8B ≈ 23 × (54 + 24) s ≈ 30 minutes ; 3B ≈ 20 minutes.

## 4. Bornes et facture

| poste | attendu | pire |
|---|---|---|
| démarrage, mise en place, garde d'encodage préalable et suite ciblée (226 essais) | 20 min (v1) | 45 min |
| chargements, terminaux, garde d'encodage | 4 min | 6 min |
| phase 1 : 8B (durée maximale 35 min) | 18 min | 30 min |
| phase 2 : 3B (durée maximale 20 min) | 11 min | 20 min |
| poussées, arrêt par identifiant | 8 min | 15 min |
| **total** | **≈ 61 min** | **≈ 116 min** |

- Une instance A100 SXM4 80 Go, prix plafond du lanceur 1,43 USD/h ; ≈ 1,2 USD/h attendu (v1 : 1,18).
- **Attendu ≈ 1,2 USD** (1,02 h × 1,2), plus le téléchargement (≈ 27 Go au plus à 0,01 USD/Go) et le disque : **≈ 1,5 USD**
  (v1, six phases au lieu de deux : 1,92 USD).
- **Plafonds de temps** : module 55 minutes (`duree_globale_s` 3 300 ; phases 2 100 et 1 200 s, chacune ne commence que
  si le temps restant la couvre) ; délai externe du run 65 minutes ; amorce 120 minutes, puis KILL 5 minutes plus
  tard ; le run ne commence pas si son délai tombe sous 45 minutes, c'est-à-dire s'il reste moins de 58 minutes avant
  le plafond de l'amorce (délai = temps restant − 13 minutes ; la phase décisive ne tiendrait plus).
- **Pire cas facturé** : démarrage 5 + amorce 120 + KILL 5 + arrêt par la session 10 = 140 minutes, soit
  2,33 h × 1,43 = 3,34 USD, plus ≤ 0,32 USD de téléchargement et de disque : **≈ 3,7 USD, sous le plafond de 4 USD.**
  Le lanceur écrit l'heure d'arrêt au plus tard (création + 8 400 s).
- **Réveils de garde** (à programmer par la session dès la création) : création + 135 et + 150 minutes (contre-lecture
  R2, CLR2-09 : après la fin au pire de l'amorce, + 130 minutes). Session perdue, arrêt par le second : ≈ 152 minutes,
  2,53 h × 1,43 + 0,32 ≈ **3,9 USD**, sous le plafond.
- Crédit exigé par le lanceur : au moins 4,50 USD ; aucune autre instance sur le compte.
- Une seule instance. Une seconde n'est permise que si la première est perdue par l'hôte avant la première ligne
  `PROGRES` **et a coûté au plus 0,20 USD** (pire de la seconde ≈ 3,7 USD ; contre-lecture R2, CLR2-07). Toute autre
  relance demande un nouveau GO.
- **Garde d'encodage** (contre-lecture R2, CLR2-06) : éprouvée sur le vrai tokeniseur du 8B (`tokenizer.json`
  `79e3e522…`, R-067 ; même tokeniseur pour le 3B à sa révision, R-068) : 94 sur 94 valeurs, 204 jetons terminaux. Elle
  est en plus faite avant la suite de tests de l'instance, sur les tokeniseurs seuls : un échec coûterait ≈ 3 minutes au
  lieu de ≈ 25.

## 5. Ce que ce devis ne couvre pas

- Aucune régénération de b0, aucun budget relevé, aucun « b0 relu » : déjà mesurés en v1.
- Aucune tâche neuve : la généralisation de la cellule redéfinie se vérifie sur textes neufs à la tranche 0 du pilote
  (GO-2026-10-29-05), pas ici.

## 6. Avant le lancement

1. Contre-lecture R2 (sous-agent neuf) de la fiche, du devis, de la configuration, du module, des essais et de la
   chaîne ; traitement des constats.
2. Commit du code ; remplir « Commit du code d'analyse » dans la fiche ; sceller fiche, devis et configuration (R6) ;
   pousser sur `main`.
3. Banc de la chaîne en mode jouet contre un dépôt local (cas sain, branche existante, temps insuffisant, fiche à
   marqueur, TERM), puis lanceur devant un faux `vastai` 1.8.3 (cas sain et refus) — fait par la contre-lecture R2
   (rapport `b156da9f…`, journaux dans son dossier) ; après les corrections, lanceur rejoué par l'auteur devant le même
   faux `vastai` : cas sain code 0 (réveils à + 135 et + 150 minutes), code changé code 2.
4. Aucune autre instance ; appel du lanceur ; réveils de garde ; surveillance des lignes `PROGRES` ; arrêt par
   identifiant (R10) à la fin de l'amorce.
5. Lecture : `python -m controle_ia.environnements.noter_rejeu_juges_v2 --lire <run>` (écrit
   `diag/<run>/lecture-rejeu-v2.json`, scellé), puis compte rendu à Lazar.
