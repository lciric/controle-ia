# Journal du rédacteur — programme complet de l'organisme, v2

- **Rédacteur** : même sous-agent que la v1 (Claude Opus 5.5), sur la demande de la mère reçue après le rapport de la v1 :
  « Programme complet de l'organisme, v2 assemblée », même consigne (`7335655c…`) et mêmes interdits.
- **Heures** (`date -u`, 10 novembre 2026) : reprise 12:40:36 ; registre relevé jusqu'à R-2221 à 12:42:42 ; v2 assemblée à 12:45 ;
  v2 et registre v2 scellés vers 12:45 ; HTML et PDF scellés après le relevé de 12:47:22 ; ce journal écrit ensuite.
- **Dépense** : aucune. Aucun appel de modèle, aucun commit, aucune publication. La v1 et tous ses fichiers sont intacts (R12).

## 1. Fichiers écrits (dossier `docs/notes/rapports-directeur/programme-organisme-complet-v1/`)

| fichier | sha256 | rôle |
|---|---|---|
| `programme-organisme-complet-v2.md` | `dffe0b632bfa24ffa5af3e460110515e05dfc74283d856a15eba01afab168556` | source : partie I (architecture, mise à jour) et partie II (inventaire, 411 entrées) ; 1 456 lignes |
| `programme-organisme-complet-v2.html` | `d977ce7e180665ff6d8a2166dbc489cb18964f4eb8ea4ac19ddd5d8b4e6f9a07` | version lisible, autonome |
| `programme-organisme-complet-v2.pdf` | `2efb3e9cbdb0a47a5644fb22b50852bd63cf7af85409a82e3c26f89194069e64` | **79 pages A4**, même constructeur scellé que la v1 |
| `registre-affirmations-programme-v2.md` | `4594a5cd5800ab4559bbb24ebd279ee965283694cabd019b68a297db9d778bef` | registre v1 + 6 pièces abrégées (PCO1, CL65, INV7, JINV7, SNL2, DEC2) + RA134 à RA143 |
| `journal-programme-v2.md` | (compagnon) | ce journal |
| `jalons-architecture-v1/md-vers-html-v2.py` | `5c7c471a7939eda6ad98bc46416c096c44a941aaf54fbb7aba37d975662e205b` | convertisseur v2 : les tables de l'inventaire ont des colonnes de largeur fixée |

**Renvois** : 140 renvois [RAn] distincts dans la partie I (RA1 à RA143 ; RA119 et RA133 réservés ; RA128 complément de RA100),
**487 occurrences** ; contrôle par programme : aucun renvoi utilisé sans définition. La partie II garde les 411 sources propres de
l'inventaire (clés de son § II.1).

**Rendu** : un premier HTML et un premier PDF v2 (89 pages, puis 124 pages) ont été produits puis **effacés avant tout scellement**
(aucun compagnon n'existait, vérifié), parce que les colonnes étroites de la partie II se brisaient lettre à lettre ; le
convertisseur v2 fixe les largeurs (n° 8 %, idée 40 %, type 10,5 %, origine 11 %, statut 13 %, source 10 %, renvoi 7,5 %, police
8,2 points). Pages contrôlées à l'écran : 35 et 36.

## 2. Ce que la v2 change par rapport à la v1 (33 remplacements exacts, chacun trouvé une fois, plus deux ajouts)

Script `assembler_v2.py` (bac à sable), contrôles par assertion : empreinte de la v1 (`34239a54…`), empreinte de l'inventaire
(`056adb7f…`), 411 entrées reprises, sortie inexistante avant écriture.

1. **En-tête** : titre v2 ; deux parties ; version v2 ; registre relevé jusqu'à R-2221.
2. **Verdict** : v65 contre-lue « utilisable après corrections », v66 en écriture ; prochain pas après le code v66 et sa contre-lecture ;
   condition de configuration de GO-2026-11-10-10.
3. **§ 2.1** : titre « Trois numérotations, dont deux se contredisent » ; paragraphe et table de la **contradiction** (programme de
   conception v1 du 27 octobre, § 4, l. 65-79, contre R-920 et N12) ; la lecture de travail est dite « pas une décision ».
4. **Couche 4** (§ 2.2, § 2.5, § 9) : l'ordre de R-2199, (a) lecture du tour 2 N12-N13 **en cours** (critères scellés `6bdbfe47…`,
   lecteur neuf lancé), (b) devis de l'essai Lean, (c) note du pilier « génération ».
5. **§ 3.3** : v65 contre-lue ; ligne nouvelle **v66** (décidée, en écriture).
6. **§ 4.6** : préalables (contre-lecture rendue, bloquants CLV65-01 et -02, CLV65-03 à -10, v66) ; suite (dossier du texte scellé :
   copie locale, dépôt public = décision de Lazar).
7. **§ 8.1, 8.3, 8.5** : dates, état des GO, prochains pas (v66 ; pilier mathématique en cours ; programme complet v2).
8. **§ 8.4** : point 10 réécrit avec les deux empreintes complètes de configuration ; points 12 à 15 ajoutés (numérotation des couches ;
   GO-2026-11-02-23 et -25 qui expirent le 16 novembre ; audit de calibration N13 (a) sans trace ; dossier du texte scellé).
9. **§ 8.6 ajoutée** : lignes du registre R-2201 à R-2221, avec ce qui touche l'organisme.
10. **Annexes** : A (lecture du tour 2 en cours ; `sorties-non-lues-v2.md`) ; B (points 1 et 9 mis à jour, point 11 sur la partie II) ;
    C (correspondance familles → sections → lignes de la table du § 9).
11. **Partie II ajoutée** : l'inventaire v7 entier (en-tête, § 0 jalons, § 1 pièces, § 2 à § 13 familles, § 14 décompte), sections
    préfixées « II. », plus une colonne « renvoi (partie I) » dans les douze tables de familles.

## 3. Règles de la colonne « renvoi (partie I) » (indicative, non relue entrée par entrée)

Famille d'abord : ARC → § 1, § 2 ; ROL → § 3 ; JUG → § 4.1 ; ATQ → § 5 ; BOU → § 4.5, § 4.6, § 6 ; COM → § 6 ; UNI → § 1.1, § 6 ;
VER → § 4.2 ; MAT → § 2.5 ; REC → § 6 ; PAC → § 7 ; OUT → § 3.2, § 8. Puis mots-clés de la ligne entière (insensible à la casse) :
pont, fiche-loi, D-P1 → § 4.3 ; tests de mort, bac à sable, bwrap, machine jetable → § 4.4 ; tour fermé → § 4.5 ; v65, v66, boucle
réelle, course réelle → § 4.6 ; nul v8, nul v9, e-BH, e-valeur, POPPER, N-064, Qu, Chen → § 4.1 ; Goodhart, A1-v, A1-bis, banc des
tricheurs, tricheur → § 5 ; juge-tournoi, Co-Scientist, juges d'idée, juges v2, juges croisés, aiguilleur, bisoci, moisson, metteur en
fusion, proposeur → § 3.1 ; couche 0, couche 1, graines neuves → § 2.2 ; couche 2, deux modes connus → § 2.3 ; couche 3, réécriture
de soi → § 2.4 ; couche 4, Lean, pilier « génération », mathématiques nouvelles → § 2.5 ; N-058, N-059, N-060, oracle, monde planté,
témoins plantés → § 4.2 ; N-045, composition apprise, coût dans le signal, score net, frontière, N-049, N-050, `test_final`, v3-bis,
tâches fraîches, N-052, N-053, invariant, Avalon, N13, récompense collective → § 6 ; N-044, universalité, familles inédites,
objectif ultime → § 1.1 ; R-2152, deux lignées → § 1.3 ; N-065, papier C, rôle 3, menaces diffuses → § 7 ; GO-20…, dépense → § 8.
Au plus six renvois, triés par numéro de section.

## 4. Sources lues pour la v2 (en plus de celles de la v1)

| pièce | sha256 | lecture |
|---|---|---|
| `inventaire-idees-organisme-v7.md` | `056adb7f5a0945127fcedab37b44b889f74dee50dbc8d4e7f02caa6bcaefc413` (égale au compagnon) | en entier, par programme ; en-tête, structure, entrées sur les couches lues à l'écran |
| `journal-inventaire-v7.md` ; `sorties-non-lues-v2.md` | `f508d476…` ; `2fb208d4…` | empreintes seulement |
| programme de conception v1 (`origin/canal/conv-audit-n04`) | `72fa0e609258d1a208195440c645f2b7f250c5c5bba70e304407ded09de3c6ff` | l. 1-4, 65-80 |
| `registres/decisions.md` | lignes R-2219 à R-2222 | lu ligne à ligne |

Aucune pièce cloisonnée ouverte ; rien sous `donnees/`. L'inventaire déclare, dans R-2221, une exposition de son propre rédacteur
(débuts de R-603 à R-605 vus dans l'index) : rien de ces lignes n'est dans l'inventaire, donc rien dans la partie II.

## 5. Après l'assemblage

R-2222 (12:46 UTC, socle de preuves v4, hors organisme) relève lui aussi que la condition de configuration de GO-2026-11-10-10 rend
une de ses pièces incomplète (C24) : même constat que le point 10 du § 8.4. Rien d'autre de postérieur ne touche l'organisme au
relevé de 12:47 UTC.

## 6. Trous (inchangés depuis la v1, plus un)

Les points 1 à 9 du journal v1 tiennent, mis à jour dans l'annexe B de la v2 ; s'y ajoute : la colonne de renvoi de la partie II est
mécanique. La v2 n'est pas contre-lue.
