# Journal du rédacteur — programme complet de l'organisme, v3

- **Rédacteur** : même sous-agent que la v1 et la v2 (Claude Opus 5.5), sur la demande de la mère : appliquer la vérification
  orchestrée de la v2. Même consigne (`7335655c…`) et mêmes interdits.
- **Pièce appliquée** : `prereg/contre-lectures/programme-organisme-complet-v2-verification-v1.md`,
  `231118c916830f9fbeec1f6aa6eac24d56e4948ec9748691aca18c46bc9cd9a7` (égale à son compagnon, vérifiée à 13:23 UTC) : « transmissible
  après corrections » ; 42 constats tenus (VP-01 bloquant ; VP-02 à VP-18 à corriger ; VP-19 à VP-42 mineurs).
- **Heures** (`date -u`, 10 novembre 2026) : reprise 13:23:15 ; registre relevé jusqu'à **R-2228** (2 186 lignes ; aucune ligne
  au-delà à 13:27:07) ; v3 assemblée à 13:27 ; v3 et registre v3 scellés, HTML et PDF scellés après le relevé de 13:27:41 ; ce
  journal écrit ensuite.
- **Dépense** : aucune. Aucun appel de modèle, aucun commit, aucune publication. v1 et v2 intactes (R12).

## 1. Fichiers écrits (dossier `docs/notes/rapports-directeur/programme-organisme-complet-v1/`)

| fichier | sha256 | rôle |
|---|---|---|
| `programme-organisme-complet-v3.md` | `bbde32b7eedc05eb5c3bc1f67c2282e4ef01fef61fd88c5afac6c11be93064fc` | source, 1 510 lignes |
| `programme-organisme-complet-v3.html` | `bcc3d68a01424adcd1596b62b7bb59cbf0294e2ca07afe3fd33f87c82ef53fb9` | convertisseur `jalons-architecture-v1/md-vers-html-v2.py` (`5c7c471a…`, scellé, inchangé) |
| `programme-organisme-complet-v3.pdf` | `ee243fea1ca52f67a10c6f0df3a96d7dc13ea1c2f93162ad663c2748c699c536` | **82 pages A4**, constructeur `construire-rapport-pdf-v1.py` (`0d3ad754…`) |
| `registre-affirmations-programme-v3.md` | `c200ca0c6c1954b8ad395c9d7874b7d036e8902105f3b792c0158f69b324c803` | registre v2 + VER2, DEC3, RA144 à RA148 ; RA65, RA89, RA110, RA127 repris |
| `journal-programme-v3.md` | (compagnon) | ce journal |

**Renvois** : 145 renvois [RAn] distincts dans la partie I, **515 occurrences** ; contrôle par programme : aucun renvoi sans
définition (RA119 et RA133 réservés ; RA128 complément de RA100).

**Outillage** (bac à sable, non versé) : `couples_v3.py` (`78bf4d68…`) extrait les couples des blocs de code du rapport, par
constat (42 paires, identifiants vérifiés paire à paire) ; `assembler_v3.py` (`0aefbbb4…`) applique, contrôle et écrit.
Contrôles par assertion : empreinte de la v2 (`dffe0b63…`), du rapport et de l'inventaire v7 ; chaque texte ancien présent
exactement une fois avant son application ; **copie de l'inventaire identique avant et après** (comparaison de chaînes) ; sortie
inexistante avant écriture.

## 2. Couples appliqués par programme dans le texte (30)

VP-01 (préambule de la partie II, comme le couple le dit), VP-02, VP-03, VP-04, VP-05, VP-06, VP-07, VP-08, VP-09, VP-10, VP-11,
VP-12, VP-19, VP-20, VP-21, VP-22, VP-23, VP-24, VP-25, VP-26, VP-27, VP-28, VP-29, VP-30, VP-31, VP-32, VP-33, VP-34, VP-35, VP-36.
Chacun : texte ancien trouvé une seule fois hors de la copie de l'inventaire, remplacé mot pour mot par le texte nouveau.

## 3. Couples traités autrement, déclarés (12) : erratum du préambule de la partie II

VP-13 (BOU-005), VP-14 (BOU-003), VP-15 (MAT-002), VP-16 (OUT-006), VP-17 (OUT-007), VP-18 (OUT-049), VP-37 (BOU-005),
VP-38 (BOU-026), VP-39 (MAT-005), VP-40 (MAT-008), VP-41 (OUT-008), VP-42 (UNI-010).

- **Pourquoi** : leurs textes anciens sont dans la copie de l'inventaire v7. La consigne de la mère dit que la partie II reste
  recopiée à l'octet ; le rapport de vérification (verdict, point 1) laisse deux voies et nomme celle-ci : porter ces corrections dans
  le préambule, « à la manière de VP-01 ».
- **Comment** : par programme, chaque texte ancien vérifié présent une fois dans la copie, l'entrée retrouvée par sa ligne ; table
  « constat | entrée | texte de l'inventaire (inchangé dans la copie) | lecture corrigée », textes ancien et nouveau recopiés mot pour
  mot, à une exception de forme : les barres « | » internes aux textes de VP-17 (qui couvrent trois cellules de l'inventaire) sont
  rendues par « / » pour ne pas casser la table.
- **État relevé après les couples** : VP-15 et VP-39 disent le pas (b) « lancé », « en rédaction » ; depuis R-2227, dessin et devis
  sont rendus et en contre-lecture : dit sous le titre de l'erratum, le texte des couples restant tel quel.

## 4. Retouches à la main, déclarées (18)

Faites par remplacements exacts (chaque texte ancien trouvé une fois), après les couples :

1. Titre « (v3) ».
2. En-tête : relevé jusqu'à R-2228 ; statut (v2 vérifiée, v3 corrigée sans nouvelle contre-lecture).
3. **Suivi de VP-02** : le couple renvoyait au registre v2, compagnon de la v2 ; la v3 a son propre registre : renvoi porté à
   `registre-affirmations-programme-v3.md` (intention du couple appliquée à la v3).
4. Puce « Version v3 » et phrase « les passages corrigés tiennent leur source du rapport de vérification » [RA148].
5. Verdict, point 2 : l'essai de la couche 4 est dessiné et devisé, en contre-lecture.
6. § 2.2, couche 4 (**ligne 181 de la v2, signalée sans couple par le rapport**, verdict point 2) : (a) fait (R-2226), (b) rendu
   (R-2227).
7. § 2.4 : tour 2 N12-N13 lu ; synthèse `6ef6bc2e…` ; résultats de R-2226.
8. § 2.5 (**lignes 242-243 de la v2, signalées sans couple**) : (a) fait, (b) rendu ; deux puces neuves : ce que le tour 2 apporte
   à la couche 4 (R-2226) ; l'essai Lean dessiné et devisé (R-2227).
9. § 8.1 : ligne « 12:49 à 13:23 UTC ».
10. § 8.4 : points 16 (GO de phase 1 de l'essai Lean, D-1 à D-6) et 17 (points du tour 2 pour Lazar).
11. § 8.5 : pilier mathématique (ligne 666 de la v2, même état périmé, sans couple).
12. § 8.5 : « ce programme complet » (v3).
13. § 8.6 : titre jusqu'à R-2228.
14. § 8.6 : lignes R-2223 et R-2228, R-2224 et R-2225, R-2226, R-2227.
15. § 9, couche 4, **après VP-10** : le couple disait « (b) devis de l'essai Lean en écriture (rédacteur neuf lancé, R-2226) »,
    périmé par R-2227 ; porté à « dessin et devis rendus, en contre-lecture (R-2227) », renvois RA144 et RA145 ajoutés.
16. Annexe B, point 9 : « portée depuis la v2 ».
17. Annexe B, point 10 (vérification) et point 12 (restes de la vérification).
18. Préambule de la partie II : « la partie I les met à jour jusqu'à R-2228 ».

**Non fait, déclaré** : l'harmonisation des deux formules voisines sur le bac à sable (VP-04 au § 4.4, VP-12 au § 9 ; verdict du
rapport, point 3, « si souhaité ») ; les deux couples sont appliqués tels quels et l'annexe B, point 12, le dit.

## 5. Registre des affirmations v3

Registre v2 recopié, plus : pièces VER2 (rapport de vérification) et DEC3 (R-2222 à R-2228) ; RA144 (R-2226), RA145 (R-2227),
RA146 (R-2223, R-2228), RA147 (R-2224, R-2225), RA148 (rapport de vérification) ; quatre entrées reprises sur le relevé du rapport :
RA65 et RA89 (contre-lecture v65 rendue depuis, R-2215), RA110 (dernière mention de N13 : R-1036 et non R-964), RA127 (page
publique, l. 7 et non l. 8).

## 6. Limites

- La v3 n'a pas été contre-lue après correction ; les « affirmations non vérifiables » du rapport le restent.
- Mise en page : dans l'erratum (page 30 du PDF), les identifiants des deux premières colonnes se coupent sur plusieurs lignes ;
  lisible, non corrigé.
- Rien d'ouvert sous la cloison ni sous `donnees/` ; aucune sortie non lue ouverte (la synthèse du tour 2 et le devis de l'essai Lean
  sont cités par le registre seulement, non ouverts).
