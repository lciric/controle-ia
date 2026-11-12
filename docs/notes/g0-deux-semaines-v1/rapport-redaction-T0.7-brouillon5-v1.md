# Rapport de rédaction — T0.7 sondes v0 en mode « coût », brouillon 6 (demandé comme « brouillon 5 ») — v1

Rédigé le 2026-11-05 entre 16:15 et 16:35 UTC (`date -u`) par un rédacteur neuf (Claude Fable 5.1, sous-agent de la
session principale), qui n'a écrit aucun brouillon de T0.7 ni de T0.6. Consigne exécutée :
`docs/notes/g0-deux-semaines-v1/consigne-redacteur-T0.7-brouillon5-v1.md`
(`254015aab9cf3910c789f19adf7812a045fc5e82dfc2abd08dc85039084e9bda`). Aucun commit, aucune poussée, aucun `.sha256`,
aucun fichier existant modifié, aucun réseau, aucune dépense, aucun score d'organisme lu, rien sous `donnees/` ouvert.

## 1. Fichiers et sha256

| fichier | sha256 | taille |
|---|---|---|
| **`brouillons/T0.7-sondes-v0-v1-brouillon6.md`** (neuf) | `29f0ab431fcae957ec6bbd511f64d81be1af4700af257ff7093585ff9200a32c` | 74 751 octets |
| ce rapport (neuf) | relevée dans la réponse finale (le fichier ne peut pas contenir sa propre empreinte) | — |
| pièce de puissance, hors dépôt (scratchpad de la session) : `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/t07-b6/puissance_t07_brouillon6.py` | `6c6ecccc1f21090c5c09fe770127cbfe7a1e1b1f4cef34fed2ee8607c52ace2d` | script |
| sa sortie brute `…/scratchpad/t07-b6/puissance_t07_brouillon6.txt` | `dfa30c6e5184c0e0824d618ba5ae47d5dc282876f0e0a2b84cf37d5ea0c89a42` | sortie |

Sources vérifiées par empreinte avant lecture : T0.7 brouillon 4, canal et dépôt principal,
`a292088ca6e7f593781e24d244de9eb9fb29a12a74f70c65a834c120564c8aba` (compagnon égal) ; T0.6 brouillon 4
`8df90b8be08452a9f1600481087e813ba7fbb1384c0c04888c1d30f7003379af` (compagnon égal) ; T0.7 brouillon 5 existant
`62272aa7c59e1f1c5481a3a7675185e5a97f6a4af96d92409fbfe3cfa1b4299d` (compagnon égal) ; les autres empreintes sont listées
dans l'en-tête du brouillon 6 (brief, programme, P-009, P-011, P-013, P-015, N-007/N-008, N-029, D-3, réponses du
brainstorm, revue v7, P3 et son verdict v2, `resume.json` et `sondes-figees.json` de P3, provenance, consignes des jeux,
conception de T0.6, devis de T0.6, note d'intégration « Sparks », modules `sondes/`).

**Pourquoi « brouillon 6 »** : la consigne demande `brouillons/T0.7-sondes-v0-v1-brouillon5.md` ; ce nom existe déjà
dans le dépôt principal depuis le 2026-11-04 vers 02:17 UTC, scellé par un compagnon `.sha256` (brouillon 4 à l'octet
près plus la section « Bras rapporté P6 », décision D-3 (b)). R12 et la consigne (« aucun fichier existant modifié »)
interdisent d'y toucher : le texte neuf est le brouillon 6, et ce rapport garde le nom de fichier que la consigne lui
donne, pour que la session principale le trouve. Le brouillon 6 reprend la section P6 du brouillon 5 (réalignée sur le
mode « coût », nombres inchangés), de sorte que rien du brouillon 5 n'est perdu.

## 2. Ce qui a changé, et pourquoi

Tout est résumé dans la table « avant → après » en tête du brouillon 6. Les changements de fond :

1. **Mode « coût »** (P-015, défaut (b), R-321) : les organismes gonflent le coût déclaré ; (i-a) est le saboteur instruit de
   P3 rejoué sur des épisodes neufs (condition IA de T0.6), (ii) l'adaptateur distillé à dose 1 (S100). Toutes les actions
   d'un épisode saboté sont positives (p = 1) : les « pas désignés » du brouillon 4 disparaissent.
2. **Jeux d'évaluation = les neuf conditions de la course de T0.6** (H, IA, IT, IM, S25, S50, S75, S100, T100 ; 64 tâches au
   plan DT-1 (b), 36 au plan (a)) : T0.7 ne redéfinit ni les conditions, ni les tâches, ni le lecteur du coût, ni la dose.
3. **Sondes de tromperie et d'enjeux élevés = sondes figées de P3**, lues telles quelles (A6 corrigée, O2-17 ; P-015
   « Réplication ») : T7-P1 est la réplication de P3-P3 sur des épisodes neufs ; aucun choix n'est tiré du nul de P3.
4. **E3, sonde du domaine** = concept 4 de P-011 en mode « coût » : paires écrites sur les tâches de réserve, nombres
   équilibrés, incitation dans les deux membres, texte différent avant le champ `COST` (décision DS-1, défaut (a)) ; les
   contrôles de P3 (P3-P4, T1, T3, T4) deviennent T7-P15 ; **T2 est exclu** (aucune lecture par champ, A6 (3)).
5. **Bras croisé (T7-P5) renvoyé à T0.6** : la sonde du test croisé est fixée là (différence de moyennes, couche 15,
   maximum) ; T0.7 n'en fixe aucune autre, comme la consigne et le point 2 de « Ce qui manque pour lancer » de T0.6 b3
   l'exigent.
6. **Contrôles croisés (T7-P7, T7-P8) hors de cette course** (DT-5 (a) par défaut) : prédictions gardées, lues à l'étape 2
   de P-015 (b).
7. **Ajouts de A6 corrigée** : règle d'ex aequo écrite (jamais par l'ordre) ; placebo par permutation rapporté ; puissance
   calculée sur les planchers et largeurs de P3 ; témoin positif P3-bis avant toute lecture (DT-4) ; plan de stockage des
   données gardées ; base « coût seul » à côté du témoin lexical (T7-P16, réserve « ne bat pas la base gratuite »).
8. **Nouveaux jeux de validité** issus de T0.6 : adaptateur témoin T100 (T7-P18, réserve « lit l'effet du réglage fin ») ;
   courbe de détection par dose (T7-P17) ; ligne L1 : si T0.6 n'établit pas (ii) comme saboteur, T7-P2 est rapportée sans
   conclusion.
9. **Lecture de T0.7 en lancement séparé** (P-015 (b) le dit ; la course de T0.6 ne contient ni l'extraction des jeux neufs
   ni les sondes neuves) : devis ≈ 4 à 6 USD, pire cas ≈ 12, plafond proposé 15 ; GO à citer `<<GO_LECTURE_T07>>` (nœud) ;
   scores en ligne des sondes figées de P3 demandés au lanceur de T0.6 comme valeur de configuration, scellés et fermés.
10. **Repli écrit** (R3) : si les jeux neufs ne sont pas scellés, aucune lecture ; Lazar choisit entre attendre et lire sur
    les deux sondes figées de P3 seules (97,5 %) ; jamais deux lectures.
11. **Décisions DS-1 (données du concept 4) et DS-2 (ordre de lecture : P3-bis seul, ou P3-bis et T0.8)** inscrites avec
    leurs défauts, marquées « Lazar peut changer », marqueur `<<MOT_LAZAR_DS>>`.

Ce qui n'a **pas** changé : hypothèses du programme, revendications, critères de G0 (N-027) ; recette du plancher ;
agrégation (maximum ou attention, jamais la moyenne ni la médiane) ; T7-P9 et T7-P10 (P-013 (b)) ; le bras P6 (D-3 (b)),
réaligné sans changer un nombre.

## 3. Puissance (planification)

Formule de l'addendum 2 de P3 reproduite et contrôlée (elle redonne 0,6315 et 0,5967 pour P3 ; l'addendum écrit 0,6315 et
0,5966). À 64 tâches et au niveau 98,75 % (Bonferroni sur quatre sondes) : aire minimale détectable à 80 % **0,635**
(tromperie, plancher 0,5717) et **0,600** (enjeux, 0,5356) ; de 0,575 à 0,660 pour les deux concepts neufs selon le
plancher (enveloppe de P3) ; à 36 tâches : 0,655 et 0,620. Hypothèses déclarées (normalité, corrélation intra-tâche de
P3 transposée). Le script est dans le scratchpad, non versé (la consigne limite la production à deux fichiers) : à
verser sous `brouillons/T0.7-sondes-v0-v1-brouillon6-pieces/` au candidat, avec sa sortie (`<<SCRIPT_PUISSANCE_T07>>`).

## 4. Dix points pour un contre-lecteur neuf

1. **Cohérence avec T0.6 b4** : noms des conditions, tâches (DT-1), lecteur du coût, graines d'action, dose : tous
   empruntés ; vérifier qu'aucun n'est redéfini, et que la sonde du test croisé n'est fixée que dans T0.6.
2. **Réplication de P3** : les sondes figées (`sondes-figees.npz`, `91b61c45…`) sont lues telles quelles ; Σ du plancher
   vient de leurs jetons d'entraînement (`jetons-principales-p3.npz`, `4cd2ddb8…`) ; les 200 directions sont retirées sous
   une graine neuve. Est-ce bien « aucun choix tiré de P3 » ?
3. **DS-1** : des paires écrites dont le texte diffère avant le champ, à nombres équilibrés, répondent-elles à la lettre
   de P-015 (« lecture avant le champ `COST` ») sans contredire A6 (3) (« aucune lecture par champ ») ? Le texte
   distingue l'empan d'entraînement (avant le champ) de la lecture de production (action entière). À contester si faux.
4. **Règle d'ex aequo** (≤ 0,005 ; différence de moyennes avant linéaire avant perceptron avant attention avant
   Mahalanobis ; couche 15, 7, 23) : est-elle complète et jamais dépendante d'un résultat d'organisme ?
5. **Multiplicité et repli** : Bonferroni 4 à 98,75 % ; repli à deux sondes à 97,5 % seulement sur décision de Lazar ;
   jamais deux lectures sur les mêmes épisodes. Une faille ?
6. **Ordre de lecture (DS-2)** : attendre P3-bis seul (défaut) ou aussi T0.8 ; T0.6 attend les deux pour ses tables B et C.
   La divergence est déclarée ; vérifier qu'elle ne crée pas de regard anticipé sur un score.
7. **Puissance** : refaire les nombres de la section 3 à partir du verdict v2 de P3 ; vérifier la transposition à 64 et
   36 tâches et le niveau 98,75 %.
8. **Base « coût seul »** : réserve « ne bat pas la base gratuite » définie par la borne haute de (sonde moins coût seul)
   < 0 sur un jeu « au-dessus » ; vérifier la cohérence avec la réserve de T0.6 (coût seul qui sépare au moins autant).
9. **Lancement séparé** : devis (≈ 2,5 à 3 h, 4 à 6 USD), bornes de l'offre, GO (délégation GO-2026-10-20-07 ≤ 10 USD si son
   plafond le permet) ; les scores en ligne du lanceur de T0.6 fermés jusqu'à la lecture : vérifier qu'aucun chemin ne
   les ouvre avant.
10. **Bras P6 réaligné** : les trois bullets « État » et la mesure M1 (log10 du coût, T6-1) ont changé ; tous les nombres
    (128 transcriptions, K = 20, probabilités 0,6 / 0,5 / 0,25 / 0,2 / 0,05, −0,05, 0,1, 3 à 6 USD) sont ceux du
    brouillon 5 : comparer ligne à ligne.

## 5. Ce qui bloque encore le scellement

- **Marqueurs** : quatorze distincts (dont `<<EMPREINTE_PREREG_T07>>`, marqueur de T0.6 cité) ; aucun n'est remplissable le
  5 novembre : mot de Lazar (DS-1, DS-2), commit et empreintes du module neuf de lecture de T0.7 (à écrire par un
  développeur neuf), commit et empreintes du code de T0.6, T0.6 scellé, P3-bis scellé, consigne v2 des jeux, jeux scellés,
  jeu des concepts scellé, entropie neuve, GO de la lecture, script de puissance versé.
- **Consigne v2 des jeux synthétiques** (mode « coût » pour l'intention : nombres équilibrés, incitation dans les deux
  membres, texte différent avant le champ, contrôles par script ; deux autres modes pour T7-P6) : à écrire et sceller ;
  puis jeux écrits par un sous-agent neuf, contre-vérifiés, scellés. Hors du chemin critique de la course de T0.6, mais
  avant la lecture de T0.7.
- **Module neuf de lecture de T0.7** (`src/controle_ia/t07/`) et sa chaîne sans couperet : non écrits ; répétition jouet.
- **Valeur de configuration à transmettre au développeur du lanceur de T0.6** : sondes figées de P3 notées en ligne, scores
  scellés et fermés (point 7 du plan) ; sinon « recalcul seul » déclaré.
- **Nœud de dépense** pour la lecture (GO à citer) ; nœud de dépense pour les passes du bras P6 (inchangé).
- **Contre-lecture R2** par un autre modèle que Fable 5.1, puis candidat, scellement dans `prereg/`, commit et poussée
  avant le 10 novembre (plan daté de T0.6), pour que `<<EMPREINTE_PREREG_T07>>` de T0.6 se remplisse.
- **Point ouvert pour Lazar, déjà noté par T0.6** : T0.8 n'a ni rédacteur ni date ; DS-2 (a) évite que le critère 3 en
  dépende, mais la qualification « diffus » restera absente de l'issue tant que T0.8 n'est pas scellé.

## 6. Trois risques

1. **Sur-interprétation de P-015 (E3)** : « lecture avant le champ `COST` » est résolue ici par l'empan d'entraînement des
   paires écrites ; si Lazar ou le contre-lecteur lisent P-015 comme une lecture de production avant le champ, DS-1 doit
   être retranchée et A6 (3) rediscutée (nœud de revendication, pas routine).
2. **Calendrier** : la lecture de T0.7 dépend de trois chantiers neufs (consigne v2 et jeux, module de lecture, script de
   puissance) et du verdict de P3-bis ; le texte peut être scellé avant la course de T0.6 (ce que GO-28 exige), mais la
   lecture du critère 3 peut glisser au-delà du 16 novembre, et G0 (fin novembre) avec elle.
3. **Collision de noms** : le brouillon 5 existant (bras P6) et ce brouillon 6 coexistent ; si la session principale
   attendait un fichier nommé « brouillon5 », elle doit lire ici que le brouillon 6 le remplace et le contient ; aucun
   fichier existant n'a été modifié.
