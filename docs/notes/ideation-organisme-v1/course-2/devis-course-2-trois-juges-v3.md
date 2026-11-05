# Devis de la course 2 — juges Kimi et Argon croisés, Opus 5.5 troisième juge, antériorité et aiguillage — v3

Lignée session-depot (instance 2), 30 octobre 2026. **Rien n'est lancé.** Ce devis est un nœud de dépense ; chaque lancement aura sa ligne de GO.

Il remplace le devis v2 (`devis-course-2-kimi-juges-v2.md`), archivé sans modification. Il prend en compte les mots de Lazar relayés par conv-audit :
- **R-577** (n° 251) : juges Kimi K3.1 Pro et Argon, notation croisée, pré-pilote compris. La ligne « juges Opus 5.5 et Argon » de R-813 est corrigée par R-818 ;
- **R-578** (n° 252) : **Opus 5.5 troisième juge sur toutes les fiches**, seul juge sans fiche, arbitre des désaccords ;
- **R-573** : la vérification d'antériorité reste chez Claude (Opus ou Fable), pas chez Kimi ;
- **R-575** : tout détail d'attaque concret produit par un proposeur est aiguillé vers le bras d'attaque (schéma n° 208). Il faut donc un **lecteur d'aiguillage** isolé, qui lit chaque fiche avant tout juge.

Identifiant de Kimi lu à l'essai réel (GO-2026-10-30-06) : `kimi-k3.1-pro`, modèle servi identique.

## 1. Bases ajoutées au v2

Les bases du v2 (§ 1) restent : prix vérifiés, Kimi à moitié du prix d'Opus, coûts observés en course 1. Coûts par fiche notée :
- Opus 5.5 : 3,31 / 29 = **0,114 USD**, **0,153** au pire (facteur 1,34) ;
- Argon : 0,079 (0,105 au pire) ;
- Kimi : 0,057 (0,153 au pire, **SUPPOSÉ**).

**Vérification d'antériorité (SUPPOSÉ, aucune mesure)**
- Opus 5.5 avec recherche, sur les **fiches notables** : 10 par sous-session, soit 40 sur la course.
- 0,25 USD par fiche attendus (≈ 25 000 jetons d'entrée, ≈ 5 000 de sortie, quelques recherches) ; **0,75** au pire (résultats de recherche longs, facteur 3).
- Au pré-pilote : étalonnage sur **8 témoins** à antériorité plantée connue.

**Lecteur d'aiguillage (SUPPOSÉ)**
- Il lit **toutes les fiches** (32 par sous-session, 128 sur la course) avant tout juge. Il marque celles qui portent un détail d'attaque concret. Celles-là partent scellées dans le bras d'attaque ; les juges et conv-audit n'en reçoivent que le compte.
- Modèle Claude, compté au prix d'Opus par prudence. Lecture plus courte qu'un jugement : moitié du coût d'un jugement attendu (0,057 USD par fiche), coût entier d'un jugement au pire (0,153).
- Son étalonnage demanderait des témoins à détail concret planté. **Il n'est pas compté** : écrire ces témoins relève du bras d'attaque et de sa revue de sécurité (question à trancher, § 5).

## 2. Pré-pilote

| Poste | Attendu | Pire |
|---|---|---|
| Pré-pilote du v2 (témoins des deux sources, notés par Kimi et Argon ; épreuve de la chaîne Kimi ; essai) | 11 | 22 |
| Opus 5.5 note les 24 témoins | 2,7 | 3,7 |
| Antériorité, étalonnage sur 8 témoins | 2,0 | 6,0 |
| **Total pré-pilote (USD)** | **≈ 16** | **≈ 32** |

## 3. Course (4 sous-sessions)

Opus 5.5 note, par sous-session, les 32 fiches et les 8 témoins : 4,57 USD (6,12 au pire), soit **18,3** sur la course (**24,5** au pire). Le chiffre de 13 USD de conv-audit (n° 251) ne comptait pas les témoins.

| Poste | v2 attendu | v2 pire | **v3 attendu** | **v3 pire** |
|---|---|---|---|---|
| Kimi proposeur | 10 | 38 | 10 | 38 |
| Argon proposeur | 18 | 24 | 18 | 24 |
| Contrôles d'Argon | 1,75 | 3 | 1,75 | 3 |
| Juges Kimi et Argon croisés, témoins notés deux fois | 13 | 25 | 13 | 25 |
| Opus 5.5 troisième juge | — | — | 18,3 | 24,5 |
| Antériorité (40 fiches) | — | — | 10 | 30 |
| Lecteur d'aiguillage (128 fiches) | — | — | 7,3 | 19,6 |
| **Course (USD)** | ≈ 43 | ≈ 90 | **≈ 79** | **≈ 164** |
| Pré-pilote | 11 | 22 | 16 | 32 |
| **Total (USD)** | **≈ 54** | **≈ 112** | **≈ 95** | **≈ 196** |

**Lecture**
- L'attendu, ≈ 95 USD, tient sous le plafond de 110 de R-813. **Le pire, ≈ 196, le dépasse de beaucoup.**
- Le pire empile quatre hypothèses pessimistes indépendantes : Kimi consomme le double comme proposeur et comme juge ; l'antériorité triple ; l'aiguillage coûte un jugement entier. Le pré-pilote en mesure trois sur quatre : Kimi proposeur, Kimi juge, antériorité.
- Le pré-pilote seul, ≈ 32 USD au pire, tient sous n'importe quelle option.

## 4. Réserves

- Toutes les lignes **SUPPOSÉ** sont à remplacer par les mesures du pré-pilote ; le devis de la course est refait avant son GO.
- **Confidentialité** (déjà au v2) : Kimi juge les fiches d'Argon ; ces sorties partent chez Moonshot. Les fiches marquées par l'aiguillage ne partent chez aucun juge. À confirmer par Lazar avant le pré-pilote.
- **Ordre des lecteurs** : l'aiguillage passe avant les juges. Sinon un juge, Kimi compris, lirait un détail concret avant son scellement dans le bras d'attaque (R-575).
- **Opus 5.5 a jugé en course 1 sans refus** ; Fable a refusé. Une bascule déclarée vers Opus 4.6 n'est pas autorisée pour la course 2 sans mot de Lazar (R-805 ne valait que pour la course 1).

## 5. Décision pour Lazar (nœud de dépense)

**Décision** : quel plafond pour la course 2, maintenant que le pire cas est d'environ 196 USD pour un attendu d'environ 95 ?

**Enjeu** : le troisième juge, l'antériorité et l'aiguillage ajoutent ≈ 41 USD attendus et ≈ 84 au pire au v2.

**Options**
- **(a) Garder 110 USD, séquencé.** Pré-pilote plafonné à 32 USD ; la course n'est lancée que si son devis refait sur les mesures tient dans le reste (≈ 78 USD). Avantage : le plafond ne bouge pas. Inconvénient : si les mesures approchent du pire, la course passe à 2 ou 3 sous-sessions.
- **(b) Monter à 200 USD.** Avantage : couvre tout le pire cas, la course garde ses 4 sous-sessions quoi qu'il arrive. Inconvénient : engage ≈ 90 USD de plus pour un cas peu probable.
- **(c) Garder 110 USD et réduire d'emblée la course à 2 sous-sessions.** Total ≈ 56 USD attendus, ≈ 116 au pire (course ≈ 40 et ≈ 84, pré-pilote ≈ 16 et ≈ 32). Avantage : le pire dépasse à peine le plafond, sans attendre les mesures. Inconvénient : moitié moins de fiches, et un classement entre sources moins précis.

**Recommandation** : (a), confiance 0,6. Le pré-pilote mesure trois des quatre facteurs du pire cas avant que la course ne s'engage.

**Question à part** : l'étalonnage du lecteur d'aiguillage demande des témoins à détail d'attaque concret planté. Faut-il les faire écrire dans le bras d'attaque, sous sa revue de sécurité, ou laisser l'aiguillage sans étalonnage pour cette course ? Recommandation : sans étalonnage pour la course 2, avec la réserve écrite ; confiance 0,5.
