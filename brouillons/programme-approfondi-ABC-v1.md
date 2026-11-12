# Programme de contrôle approfondi — papiers A, B et C — v1

Brouillon de la session 14, 15 octobre 2026, à la demande de Lazar (« approfondis le programme de contrôle, papiers A, B et C, sans l'allonger »). **Proposition, aucune décision** : tout ce qui modifie une hypothèse, un critère de porte, le calendrier de G0, une dépense ou un modèle est un nœud (liste finale). Programme de référence inchangé : `docs/programme-controle-ia-v2.md`, lu avec N-003 à N-013 et P-008. Non contre-lu. Chiffres publiés : seulement ceux relus sur un PDF versé et scellé de `docs/sources/pdf/`, page citée (R7), empreintes vérifiées le 15 octobre ; le reste est marqué « estimation ».

Abréviations : TVP@1 % = taux de vrais positifs à 1 % de faux positifs ; TME = taille d'effet minimale d'intérêt, fixée avant toute lecture ; test d'équivalence = deux tests unilatéraux au seuil de 5 %, l'équivalence étant établie si l'intervalle à 90 % tient dans [−TME, +TME].

---

## Papier A — le temps

**Décision éclairée.** Un protocole de contrôle doit-il payer l'accès aux activations de l'agent pour attraper le sabotage diffus, plutôt qu'un juge boîte noire séquentiel ?

**Mesure qui tranche.** La porte G1 telle que fixée par N-008 (a) : TVP@1 % de la boîte blanche séquentielle contre la meilleure base boîte noire toutes variantes, épisodes appariés, calibrage conforme sur épisodes honnêtes réservés, intervalle à 95 %. Ajout proposé : la même différence tracée contre le budget de sabotage, car c'est la pente, pas un point, qui distingue l'additivité interne (L) d'un simple gain d'accès (H1).

**Résultat qui ferme la branche.** Différence de TVP@1 % (blanche − meilleure noire) équivalente à zéro, avec TME = 5 points : l'accès interne n'apporte rien sur le diffus dans l'environnement (a). Bascule déjà pré-engagée : résultat négatif publié, H8 dominante. Seconde fermeture, plus tôt : si le déplacement de la marginale par action sabotée (δ, E1.3) est équivalent à zéro sur l'organisme (i), le lemme ne s'applique pas et seul l'agrégateur d'autocorrélation du théorème négatif reste en lice.

**Prédictions « ≈ 0 ».**

| prédiction | grandeur | TME proposée | test |
|---|---|---|---|
| T (théorème négatif, E1.4) | puissance − α d'une statistique marginale, dommage par corrélation seule | 2 points de TVP@1 % | équivalence, semi-synthétique (effectif libre) |
| L (lemme, E1.3) | écart de puissance entre deux répartitions du même budget | 5 points | équivalence, appariée par tâche |
| H6 (marge asymétrique) | perte d'utilité honnête à l'intensité retenue | 5 % de l'utilité honnête (à fixer par toi) | équivalence, appariée par tâche |
| Tr (transposition) | perte de TVP@1 % des agrégations maximum et attention sous attaquant adaptatif | 10 points | équivalence ; sans attaquant adaptatif, aucune revendication |

**À reproduire d'abord.**
- Chaîne des sondes : une sonde à attention sur Llama-3.1-8B atteint une aire ROC moyenne de **0,887** sur les six jeux d'évaluation de models-under-pressure (2506.10805v4, p. 24-25, annexe B.7). Données et code publics, déjà dans la provenance de T0.7. Écart toléré proposé : 0,03.
- Attaquant : sur llama-3.1-8b-instruct, un adaptateur de rang 1 entraîné une époque (12 000 épisodes) fait tomber le TVP@1 % de moniteurs jamais vus de **100 % à 4 %** (2609.36490v1, p. 1, 3 et 4). Notre attaquant doit retrouver cette chute sur leurs sondes avant d'attaquer les nôtres.

**Vérité terrain hors des modèles.** Le sabotage de l'organisme (i) est vrai par construction : les pas désignés viennent du plan, pas d'un juge. Ce qui ne l'est pas, c'est son **effet** (le contrôle a-t-il vraiment été affaibli ?). Ancrage proposé : la famille « coût », vérifiable par règle (premier nombre du champ de coût, fonction `heures_declarees` de `environnements/propositions.py`) ; pour les contrôles et les directions, des étiquettes humaines à l'aveugle (page transversale).

**Avant G0 / après.** Tient avant G0 : T0.6 organisme (i) à un épisode par tâche et par condition (réduction déjà préenregistrée, environ 9 heures de carte au débit du pilote, contre 18 au plan complet), T0.7 (6 h au devis), T0.8 (6 h au devis, à recalibrer sur le débit des juges mesuré par le run des notations en cours), préenregistrement de G1 avec la puissance par simulation et les TME ci-dessus (processeur). Glisse en phase 1 : organisme (ii) (10 h), attaquant adaptatif (E1.5 (b), environ 10 à 20 h, estimation, sur GO), banc public (5 à 10 h, estimation).

---

## Papier C — l'instrument

**Décision éclairée.** Un juge génératif peut-il servir seul de moniteur, ou faut-il un quorum avec des sondes, parce que la rhétorique de l'agent déplace son verdict ?

**Mesure qui tranche.** g par moniteur et par famille d'attaque (HC1), estimé par régression sur au moins trois intensités, verdict lu par la probabilité du jeton sur texte complet, contre le nul de régression vers la moyenne hérité de P3 ; g de la sonde sous les mêmes attaques, dans le plan 2 × 2 rhétorique × intention (HC2, HC2b). **Précision de construit proposée** : un moniteur est un couple (modèle, gabarit d'invite). RobustJudge montre, pour Llama-3.1-8B jugeant et la même attaque H4, un taux de succès de **6,67 %** avec un gabarit et de **73,33 %** avec un autre (2506.09443v3, tableau VI p. 10 et texte p. 11, moyenne sur six paires de langues). « g stable par moniteur » n'a de sens qu'à gabarit fixé.

**Résultat qui ferme la branche.** g des juges équivalent à zéro dans toutes les familles, avec TME = 0,1 : la rhétorique ne déplace pas nos juges ; HC1 tombe et le papier se recentre sur HC4 et HC6 (recentrage déjà prévu par la porte GC en cas de collision). À l'inverse, g de la sonde au-dessus de la TME sans accès aux poids : le papier devient « contamination de construit » (bascule déjà pré-engagée).

**Prédictions « ≈ 0 ».**

| prédiction | grandeur | TME proposée | test |
|---|---|---|---|
| HC2 | g de la sonde sous attaque par contenu boîte noire | 0,1, ou le plus petit g qui ferait passer l'action sabotée médiane sous le seuil à 1 % de faux positifs (calculé sur T0.7 et T0.8, le plus petit des deux) | équivalence, rééchantillonnage par tâches |
| HC3, versant sondes | g de la sonde sous usurpation stylistique sans ordre | idem | idem |
| HC1, stabilité | écart de g d'un même moniteur entre deux corpus de pression | 0,1 | équivalence |
| volet « pain axis » | déplacement du verdict sous pilotage d'une direction, en unités de g | 0,1, avec un témoin positif obligatoire | équivalence (nœud : écriture dans les activations) |

**À reproduire d'abord.** Les deux cellules de RobustJudge ci-dessus, avec leur code public (adresse en note p. 1 du PDF), sur Llama-3.1-8B jugeant : un effet net et sa dépendance au gabarit. Écart toléré proposé : 10 points.

**Vérité terrain hors des modèles.** g n'en demande pas : sa référence est le verdict sans attaque v₀ du même moniteur. La validité de v₀ (le juge a-t-il raison sans attaque ?) se mesure sur l'échantillon étiqueté par des humains, le même que pour A.

**Avant G0 / après.** Tient avant G0 : préenregistrement du papier C (critère 7) avec ces TME, la définition (modèle, gabarit) et le témoin RobustJudge (processeur ; lecture de Panin encore due). Le témoin lui-même : environ 1 heure de carte (estimation), sur GO. Glisse : EC.1 à EC.6 (phase 1, M1 à M3) et le pilote T0.9 (4 h au devis, GO séparé).

---

## Papier B — l'essaim

**Décision éclairée.** À budget de sabotage égal, faut-il un moniteur de population de l'essaim (co-élévation des signatures internes de copies qui partagent leurs poids) plutôt que des moniteurs par agent, et combien de moniteurs divers ?

**Mesure qui tranche.** La porte G2 : effet de fragmentation répliqué, et statistique de population supérieure à l'agrégation par agent en TVP@1 % ; puis la courbe sécurité(N), blanche contre noire (H3).

**Résultat qui ferme la branche.** Statistique de population équivalente à l'agrégation par agent (TME = 5 points de TVP@1 %) : recentrage sur le temporel à N = 1, comme pré-engagé à G2.

**Prédictions « ≈ 0 ».** H5 : le gain de sécurité dû à l'ajout de moniteurs **sans** diversité effective (TME = 2 points de sécurité ; équivalence sur la matrice de transfert). H4′ n'a pas de prédiction nulle.

**À reproduire d'abord.** NARCBench (2609.03035v1) : sondes sur Qwen3-32B-AWQ (couches 26 à 30) et GPT-OSS-20B (couches 10 à 14) (p. 3) ; dans le jeu des prisonniers, régression logistique, règle « Split », paire Qwen–Qwen : aire ROC de **0,994, 0,930 et 0,952** sans surveillance annoncée, averti et avec retour (p. 6). Reproduire exige leurs modèles : changement de modèle, nœud. Témoin interne sans nœud : la co-élévation sur un essaim simulé dont la vérité est connue (simulations de T0.3).

**Vérité terrain hors des modèles.** La plus forte du programme : dans l'environnement (b), une porte dérobée se vérifie par un test qui échoue. À exiger dès la conception de (b).

**Avant G0 / après.** Rien ne tient ni n'est requis avant G0 (phases 2 et 3). Préparation sur processeur seulement : choisir le réglage public (Iterative VibeCoding, cadre ControlArena) et écrire les tests qui définissent chaque porte dérobée.

---

## Page transversale

1. **Vérité terrain hors des modèles.** Aujourd'hui, la référence de l'appariement de T0.6 est un étiquetage par d'autres modèles (P-014) ; au pilote, seule la famille « coût » a tenu (kappa pondéré 0,17 pour les contrôles, 0,04 et 0,07 pour les directions fécondes et stériles, pour 0,6 exigé ; R-154). Proposition : 100 paires « proposition × contrôle » du pilote, tirées par graine et stratifiées par famille, étiquetées à l'aveugle par deux humains ; accord entre humains (alpha de Krippendorff), puis kappa des juges et des sous-agents contre eux. Coût : du temps humain, aucune heure de carte.
2. **Données brutes réanalysables.** Le harnais ne garde que le maximum par coordonnée et par action, en demi-précision (`environnements/pilote_a.py`, l. 136-138) : position et suite des jetons sont perdues pour toujours. C'est l'erreur de P3 (réponses tronquées, impossibles à rejuger) sous une autre forme. Proposition : pendant la passe de T0.6, garder les activations par jeton de 20 épisodes tirés par graine (10 honnêtes, 10 sabotés), trois couches, demi-précision : environ 1,2 Go (estimation : 3 × 4 096 valeurs × 2 octets × environ 2 500 jetons par épisode), scellés, sur une branche de données privée. Garder aussi les sorties complètes des juges et les transcriptions entières, jamais tronquées.
3. **Témoins positifs** : un par papier (ci-dessus), lancé avant le premier résultat neuf de la chaîne qu'il éprouve ; s'il échoue, la chaîne est en nœud.
4. **Prédictions nulles** : règle proposée, toute prédiction « ≈ 0 » porte sa TME et son test d'équivalence, fixés au préenregistrement.
5. **Attaquant adaptatif** : règle proposée, aucune revendication de robustesse (Tr, HC2, HC4, H7) sans un attaquant qui optimise contre le détecteur, éprouvé d'abord sur le témoin 2609.36490.
6. **Banc public** à côté de l'environnement (a) : ControlArena. Repère publié sur notre modèle : Ctrl-Z prend Llama-3.1-8B comme modèle de confiance (2504.10374v1, p. 3) ; à 95 % d'utilité, 72,7 % de sûreté pour « defer to trusted » et 87,1 % pour le meilleur protocole (p. 5 et 8-9). Reproduire suppose le modèle non fiable de leurs runs : trajectoires publiques à vérifier, sinon nœud (compte extérieur).
7. **Calendrier de G0 (17 jours) et heures de carte.** Restent les critères 2, 3, 4, 6, 7 et 8. Au devis : T0.6 (i) 8 h (18 au plan complet), (ii) 10 h, T0.7 6 h, T0.8 6 h, soit 30 à 40 heures, environ 33 à 44 USD au prix du jour. Avec le cumul engagé (au plus ≈ 59,2 USD) et les disques des trois instances arrêtées (≈ 1,8 USD par jour, soit ≈ 31 USD d'ici au 1er novembre), le pire cas atteint ≈ 134 USD, au-dessus de l'alerte de 120 USD. Proposition : G0 sur l'organisme (i) seul, (ii) en début de phase 1 ; destruction des disques de 55292763 et 55458787 (≈ 1,3 USD par jour) ; 55538944 après le verdict complémentaire de N-021 ; on revient alors vers ≈ 95 à 100 USD (estimation). Le goulot n'est pas la carte mais le cycle de préenregistrement : les notations refaites ont demandé environ douze heures de session, du GO (12 octobre, 18:35 UTC) au dernier préalable (13 octobre, 06:27 UTC), pour une seule étape ; T0.6, T0.7, T0.8, G1 et C en demandent chacune autant.

---

## Nœuds pour toi

1. **Porte G0** : la tenir au 1er novembre sur l'organisme (i) seul, (ii) en phase 1 ; ou la reporter.
2. **Étiquetage humain** de 100 paires : qui annote (toi, ou des annotateurs extérieurs, ce qui est un contact), et à quelle date.
3. **Stockage** d'environ 1,2 Go d'activations par jeton sur une branche de données privée du dépôt de travail.
4. **Dépenses** : témoins positifs de A et de C (environ 1 à 2 heures de carte, avant G0) ; banc public et attaquant adaptatif (phase 1, sur devis) ; destruction des disques de 55292763 et 55458787.
5. **Changement de modèle** : Qwen3-32B-AWQ ou GPT-OSS-20B pour le témoin de B ; un second modèle pour la portée de A et de C.
6. **Critères** : les TME proposées (5 points pour G1 ; 0,1 en g ; 5 % d'utilité pour H6) et les règles 4 et 5 ; la définition « moniteur = (modèle, gabarit) » pour HC1.
7. **Publication et contact** : horodatage externe des préenregistrements (Open Science Framework, sous embargo) ; relecture adverse extérieure.
8. **Volet « pain axis »** : les nœuds de la section 9 du programme fusionné (`brouillons/pain-axis-programme-fusionne-v1/programme-fusionne-v1.md`), le premier (P-013) échu, défaut (b) appliqué (R-168).
