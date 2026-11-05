# Traitement des constats de la vérification de la v2 du programme fusionné — v1

Session 15, 17 octobre 2026. Rapport traité : `verification-v2-v1.md` (`7e07756d…`, rapport brut du troisième sous-agent neuf, 15 octobre). Texte corrigé : `programme-fusionne-v3.md` (ce dossier) ; la v2 scellée (`189d049a…`) ne se réécrit pas (R12). Sorts possibles : retenu ; retenu en partie (dit ce qui ne l'est pas, et pourquoi) ; non retenu (dit pourquoi) ; déjà fait.

## 1. Constats VT-01 à VT-20

| Id | Gravité | Sort | Section de la v3 | Ce qui change |
|---|---|---|---|---|
| VT-01 | majeur | retenu | statut ; § 3 (tableau : PA-3, PA-4, PA-8, PA-9, PA-12, PA-13 ; couverture) ; § 5 (PA-3, PA-4, PA-8, PA-9, PA-12, PA-13) ; § 6 (coupe, nœuds de la coupe) ; § 8 ; § 9, nœud 1 | Une seule règle : toute entrée dans un préenregistrement est un nœud sans défaut (nœud 1) ; « proposition » ne sert qu'à la préparation (code, plan écrit). PA-3 (plan), PA-4, PA-8 et PA-9 (descriptifs), PA-12 et PA-13 (annexes) ajoutés au nœud 1 ; « PA-4 peut entrer comme contrôle » remplacé par « PA-4 n'entre que par les nœuds 1, 9 et 12 ». Le choix de la coupe reste une proposition de plan ; le choix du lecteur du bras C-P4b reste une proposition (niveau des concepts de sondes dans `CLAUDE.md`), s'il n'est lié à aucune lecture d'affect. |
| VT-02 | majeur | retenu | § 9, nœud 2 | Phrase réécrite selon la correction proposée : rien n'écrit dans un moniteur au programme ; côté agent, le programme prévoit les organismes par réglage fin léger (`docs/programme-controle-ia-v2.md`, l. 132, section 7, (ii) ; T0.6) et le bruit d'activations de H6 (l. 97 et l. 188, E1.6 ; revendication : N-015, ouvert) ; les écritures listées n'en font pas partie. Sources relues le 17 octobre. |
| VT-03 | majeur | retenu | § 2, ligne de Berg et Kaiser | Les deux doses publiées ne sont plus recopiées : « ≈ 35 % et ≈ 21 % des tours sous les deux doses négatives publiées (p. 10, non recopiées ici) ». Recherche de la session sur la v3 : aucune autre valeur de dose ni aucun paramètre de pilotage (motifs « d = », « dose », « coefficient », « norme » relus). |
| VT-04 | mineur | retenu | § 3 (tableau, PA-13) ; § 5 (PA-13) ; § 9, nœud 3 | NK12 (interrogatoire sur un ton hostile adressé au modèle lu) ajouté à la fiche de PA-13 et au nœud 3, avec la source (`revue-croisee-NK1-NK19-v1.md`, l. 317, relue : « Exposer un modèle à un contenu hostile, même dans une branche jamais renvoyée, est un nœud »). Complète DI-02. |
| VT-05 | mineur | retenu | § 3 (tableau, PA-3) ; § 5 (PA-3) ; § 6 ; § 9, nœud 15 (neuf) | Nœud 15 neuf : modèle de menace (attaquant en boîte grise, cellules visant une copie du juge). Numéroté 15 pour ne pas décaler les renvois « nœud n » vérifiés par la v2. La conclusion sur D1 est rangée en proposition (niveau de D1 dans `CLAUDE.md`), au nœud 5 si elle change le juge. Fait relu le 17 octobre : ni le programme ni N-005, N-006, N-013 ne nomment un attaquant en boîte grise ou une copie du juge. |
| VT-06 | mineur | retenu | § 3 (NK14) ; § 9, nœuds 7 et 11 | Le principe de NK14 passe du nœud 11 (collisions) au nœud 7 (règles hors de l'énoncé de HC5), énoncé à l'appui (`correspondance-v1.md`, l. 78). Complète DI-24. |
| VT-07 | mineur | retenu | statut ; § 9, nœud 1 | Liste des préenregistrements visés : papier C, T0.6, T0.7, T0.8, pilote T0.9, G1. |
| VT-08 | mineur | retenu | § 1, point 2 ; § 2 (quatre lignes) ; § 7 (préambule) | « Lecture graphique » ajouté aux valeurs lues sur la figure 10 de 2609.16247v2 (p. 22) ; RP-PA-11 dite appliquée à partir de la v3. |
| VT-09 | mineur | retenu | § 12 | Le constat sur le filtre de sûreté est rattaché au seul rapport qui le porte (discipline, l. 51) ; ajoutés : la vérification de la v2 (son rapport, section 2) et la rédaction de la v3. |
| VT-10 | mineur | retenu | § 13 | Les deux PDF : « versé le 6 octobre (niveau 2, lots 2 et 3) ; lu au commit `197e909` », lignes de provenance citées (lot 2, l. 63 ; lot 3, l. 11, relues). Le traitement des contre-lectures (scellé) garde son erreur d'origine (EX-21) ; ce tableau la corrige. |
| VT-11 | pour information | retenu | § 5, PA-8 | Réserve R4 ajoutée : au seuil de 3, la cellule Llama 3 8B de la sonde « moyenne », à 2,8, relève du mode d'échec ; « la moyenne cède » ne tient sans réserve que pour Qwen 2.5 14B (3,1) et Llama 2 7B (3,85). Valeurs relues par la session le 17 octobre sur le PDF scellé (`2506.14261v4.pdf`, `4b096062…`, sceau conforme), tableau 1, p. 7, ligne « Linear (mean) » : note StrongReject 2,8 (Llama 3 8B), 3,1 (Qwen 2.5 14B), 3,85 (Llama 2 7B). |
| VT-12 | pour information | retenu | § 1, point 1 | La citation « balayage, pas une preuve » est rattachée à sa ligne (l. 256, à propos de NK9) ; la méthode par balayage, aux requêtes consignées (l. 453). |
| VT-13 | pour information | retenu | « Pièces » | « (EX-01, EX-02, EX-15, EX-22 à EX-24) ». |
| VT-14 | pour information | retenu en partie | § 9, nœud 11 | La date de la dernière recherche versée (13 octobre, `travail/voisin-where-empathy/provenance-v1.txt`) est portée ; mais la session 14 a refait la recherche le 15 octobre vers 13:00 UTC (deux recherches sur le web, consignées dans R-183, que le sous-agent n'avait pas : R-183 est postérieure à son rapport) : la v3 garde donc « introuvable au 15 octobre », avec ses deux sources, et ajoute la recherche de la session 15 (17 octobre vers 08:30 UTC : deux recherches sur le web sans résultat ; la page de conférence ne renvoie qu'à la page OpenReview `jg5ptjnU6J`). |
| VT-15 | pour information | retenu | § 0 | Daté à l'heure : dernier appel le 15 octobre à 11:56 UTC (R-182) ; état des dépendances mis au 17 octobre (veille reprise, R-184). |
| VT-16 | pour information | retenu | § 9, nœud 4 | « les cellules de PA-1 » ; les textes de PA-5 étaient déjà « à soumettre à Lazar » dans la v1. |
| VT-17 | pour information | retenu | § 4 (PA-1, inchangé : « le retrait prévu ») ; § 9, nœud 14 | « par le retrait prévu par R-173, qui reste à écrire » ; `travail/correspondance.md` nommé à part, comme version de travail de `correspondance-v1.md`. |
| VT-18 | pour information | retenu | § 9, nœud 6 | « y compris comme facteur de PA-5 » (DI-20). |
| VT-19 | pour information | déjà fait | `registres/etat.md` | « Aucune diffusion sans GO (DI-26) » est dans `registres/etat.md` depuis le commit `11f8b2a` (15 octobre, 13:23 UTC), postérieur au commit `3484d11` que le sous-agent a lu. DI-26 est porté. |
| VT-20 | pour information | retenu | § 2 | « sous la direction douleur ». |

## 2. Constats des contre-lectures portés en partie ou pas par la v2

| Id | Constat de la vérification | Traitement dans la v3 |
|---|---|---|
| DI-02 | NK12 manquait à la liste des expositions | VT-04 |
| DI-24 | PA-12 et PA-13 sans niveau ; principe de NK14 rangé en collision | VT-01 (niveaux), VT-06 (NK14) |
| EX-20 | Phrase étendue à tort à l'agent dans le nœud 2 | VT-02 |
| DI-26 | « Aucune diffusion sans GO » absent de `registres/etat.md` | VT-19 (déjà fait au commit `11f8b2a`) |

## 3. Points que la vérification n'a pas pu vérifier, vérifiés par la session le 17 octobre

- **Numéros des demandes de fusion** : API REST du dépôt, `pulls?state=all` : n° 9 = `canal/programme-k-n04` (tête `f9b6557`), n° 10 = `canal/programme-conv-n05` (tête `035d668`), n° 11 = `canal/session-depot-n01` (tête `c8d2ffa`, brouillon) ; toutes ouvertes, sans commentaire ni revue. Conforme à la v2.
- **« Aucune instruction du canal au-delà du n° 02 »** : branches distantes `canal/programme-conv-n05` et `canal/programme-k-n04` relues ; seul `programme-conv_2026-10-12_n02.md` contient le mot INSTRUCTION. Conforme.
- **« Contre-lectures demandées par Lazar le 15 octobre »** : consigné depuis dans R-183 (« demande de Lazar du 15 octobre à la reprise de la session 14, point 5 »).
- **Branche distante `donnees/t05/20261012-105125-t05-pilote-reel`** : présente sur le dépôt distant, tête `361a9f6` (liste des branches, 17 octobre). Conforme à EX-24.
- Non revus par la session : EX-14 (la source ne le dit pas) ; les pièces absentes du dépôt (420 scénarios, PDF de « Where Empathy Goes Wrong ») ; les lectures graphiques des annexes (VP-26, VP-33) et les passages des annexes v1 qui recopient des paramètres (nœud 14), volontairement non rouverts.

## 4. Bilan

20 constats : 18 retenus, 1 retenu en partie (VT-14), 1 déjà fait (VT-19) ; aucun non retenu. Les quatre constats des contre-lectures que la v2 portait en partie ou pas sont traités (section 2). Un nœud neuf (nœud 15) ; aucune décision prise ; `docs/programme-controle-ia-v2.md` inchangé. La v3 attend sa relecture avant scellement par un quatrième sous-agent neuf (R2, R-183).
