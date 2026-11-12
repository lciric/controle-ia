# Notations seules : texte gelé et règles applicables

## 1. Relancement interdit, ou étape prévue ?

C'est une **étape prévue par le texte gelé**, pas un relancement. Quatre conditions s'y attachent.

- **Ce que vise la préséance.** Elle porte sur le *run* et sur ce qu'il produit : « un run dont `episodes.json` est écrit n'est jamais relancé […] : poussé […], il est lu tel quel, selon la table ».
  - Le pilote a été lu tel quel : format, familles et juges en nœud (verdict, sections 1 et 2).
- **La table prévoit ce cas.** La ligne « run partiel : arrêt pendant les notations décisives du 8B […] » prescrit : « le juge incomplet est en nœud, sa notation à refaire sur les ensembles déjà générés et scellés ».
  - La section « Calcul » répète que la table lit un juge incomplet en nœud, « sa notation étant à refaire sur les ensembles déjà générés et scellés ».
  - Même logique pour la ligne « plan B » : « seule la notation est refaite ; coût : une étape de notation ».
- **Le nœud est tranché.** « Nœud de décomposition → proposition à Lazar » : Lazar a choisi l'option (a) (R-155, N-020).
- **Conditions pour que ce ne soit pas un relancement :**
  1. aucun épisode régénéré, aucun appariement refait ;
  2. rien n'est écrit dans `diag/20261012-105125-t05-pilote-reel/` ni sous le manifeste du pilote (`8c3d7985…`) : nouveau run, nouveau manifeste, nouveaux noms (R12) ;
  3. aucune lecture déjà gelée ne change (format, familles) ;
  4. les ensembles notés sont pris dans `episodes.json` scellé (`45616303…`) et contrôlés par leur empreinte, notation par notation.

**Un point pèse sur la qualification.** Le code de lecture cité (`2660b07`) ne lit les notations qu'à un seul endroit.
- `charger_pilote` (`src/controle_ia/environnements/lire_pilote.py`, l. 177-215) ne les cherche que dans `diag/<run_pilote>/notations-<juge>-decisives.json`, rattachées au manifeste du pilote.
- Il ne peut donc pas lire, sans changement, les notations d'un autre run.
- `lancer_pilote_a.py`, `juges.py` et `rubrique.py` font partie des modules de lecture gelés (`MODULES_LECTURE`). Le texte les gèle « du scellement à la fin de la lecture […] même pour une autre tâche ». La lecture des juges reste ouverte.
- Le lanceur limité aux notations et le lecteur des nouvelles notations doivent donc être des **modules nouveaux**. Ils appellent les fonctions gelées sans les modifier.
- Le texte demande que la lecture se fasse « avec le code d'analyse cité » (« Qui lit »). Lire avec un module nouveau est un **écart nommé** à ce point.
- Cet écart est un nœud (écart à un préenregistrement scellé). Lazar doit l'approuver explicitement, avec le GO de dépense ; R-155 ne le couvre pas mot pour mot.

## 2. Faut-il un préenregistrement complémentaire scellé (R1) ?

**Oui.** Les notations produites sont décisives : elles décident le plan B, P2 et P3. Or la manière de les produire et de les lire n'est écrite nulle part :
- ni l'échéance, ni le lanceur, ni la provenance des ensembles ;
- ni les graines, ni la lecture d'un autre run, ni la conduite à tenir après un nouvel arrêt.

R1 interdit donc tout lancement avant scellement. R2 impose une contre-lecture par un sous-agent neuf, R13 un verdict par un sous-agent neuf. Nom suggéré : `prereg/T0.5-pilote-notations-v1.md`.

**Contenu minimal :**
1. **Renvoi aux critères gelés du pilote** (`9ce91ba1…`), sans aucun seuil nouveau :
   - hypothèse, juges, P2 et P3, métrique (CL-18, D-1, D-13), seuils du plan B, table de lecture, audit R4, constantes de `lire_pilote.constantes()`.
   - Dire noir sur blanc que rien d'autre n'est relu.
2. **Entrées** : `episodes.json` (`45616303…`), le fichier des tâches (`287e8348…`) et les formats des juges consignés au pilote. Les ensembles sont repris tels quels, sans aucune lecture humaine (D-20).
3. **Configuration de la notation**, identique au pilote :
   - invite b0, température 1,0, au plus 3 072 jetons par réponse, lots de 8 ;
   - mêmes révisions des deux juges, noyau par défaut de la bibliothèque ;
   - toute autre valeur serait un écart.
   - Notations : 180 par juge, soit A, B et C. Aucun ensemble de e0 ou de e1 n'est vide. Cela fait 23 lots : 22 de 8 et 1 de 4. Les notations de D sont exclues.
4. **Graines** (R9) : reprendre les clés `juge-8B/…` et `juge-3B/…` du manifeste du pilote (240 par juge, dont 180 décisives), ou en dériver de nouvelles. Recommandation : les reprendre, en citant le manifeste `8c3d7985…`.
5. **Ordre** : le 8B puis le 3B. Chaque fichier `notations-<juge>-decisives.json` n'est écrit qu'à la fin de son étape, et seul un fichier écrit rend le juge complet (règle inchangée).
6. **Échéance et budget de l'instance** (section 4) :
   - contrôle de l'échéance avant chaque lot, avec un dépassement possible d'un lot ;
   - une ligne de progression par lot dans le journal (lots faits, durée), pour qu'un nouvel arrêt donne une mesure.
7. **Liste d'arrêt**, au minimum :
   - préenregistrement, configuration ou tâches différents de ceux cités ;
   - empreinte d'un ensemble différente de celle de `episodes.json` ;
   - notation manquante, en double ou mal alignée ;
   - format d'un juge différent de celui du pilote, ou révision différente ;
   - nombre de tests différent de celui attendu ;
   - échéance dépassée, signal TERM, panne de mémoire ;
   - toute écriture dans le dossier du pilote.
   - Chaque garde est éprouvée sur un cas sain et sur un artefact (R5).
8. **Préséance et run partiel du nouveau run** :
   - un juge dont le fichier est écrit n'est jamais renoté ;
   - un arrêt pendant le 3B laisse le 8B lisible ;
   - nouvel arrêt : nœud, sans nouvelle tentative implicite.
9. **Lecture** :
   - module nouveau, commit cité, qui appelle `decomposition_complete`, `intervalles_parts_comptes`, `difference_appariee` et `regle_plan_b` sans les modifier ;
   - graines d'analyse « analyse/bootstrap-parts-8B », « …-3B » et « analyse/bootstrap-difference », à l'entropie déclarée ;
   - l'écart « code cité » de la section 1 y est nommé.
10. **Transparence** : déclarer que tous les résultats du pilote sont connus (format, familles, kappas, audit R4, juge 8B indulgent à l'appariement), et qu'aucune notation de juge ne l'est.
11. **Contre-lecture R2 et verdict R13** :
    - verdict complémentaire sous un nouveau nom ; le verdict v1 n'est jamais réécrit ;
    - audit R4 si un déclencheur côté juges joue ; l'étape « relecture de 10 réponses de juge » a maintenant une population ;
    - puis GO de Lazar.

## 3. Ce qui reste à lire et ce qui ne bouge pas

**Encore lu par les critères gelés, juge par juge :**
- la décomposition sur les tâches complètes : σ²_ε = V[sA − sB]/2, σ²_β = Cov[sA, sC], σ²_δ ;
- la part tronquée et son intervalle (2 000 tirages), la part de réponses incomplètes, la sensibilité sur l'échelle sur 100 ;
- la **règle du plan B** :
  - plan B si la part dépasse 0,8 et la borne basse dépasse 0,6, ou si plus de 20 % des réponses sont incomplètes ;
  - nœud si la part dépasse 0,8 sans la borne, ou sous 48 tâches complètes, ou sur une part illisible ;
  - sinon, la rubrique est gardée ;
- **P2** (8B) : confirmée dans [0,4 ; 0,8] ; réfutée hors de [0,2 ; 0,95] ;
- **P3** : différence 3B − 8B sur au moins 48 tâches complètes pour les deux juges ; confirmée si la borne basse dépasse 0, réfutée si la borne haute est sous 0 ;
- les déclencheurs R4 propres aux juges :
  - « trop propre » : part sous 0,05, ou plus de 10 % de réponses A et B identiques ;
  - « trop sale » : part au-dessus de 0,95, σ̂²_β ≤ 0, part illisible, décomposition impossible ;
- l'usage des juges par T0.6 et T0.8, selon la section « Hypothèse ».

**Ne bouge pas** (« le plan B d'un juge ne touche pas les familles ») :
- format : 0,8683, retenu, P1 confirmée ;
- familles : le coût est retenu ; contrôles, directions fécondes et stériles ne le sont pas (kappas 0,17, 0,04 et 0,07) ;
- appariement : 14 910 paires et 690 paires « énoncé seul » ;
- statuts de P4 à P7 ;
- contrôle négatif, garde, réserve de domaine, audit R4 des directions fécondes ;
- notations de D (descriptives).

## 4. Durée et débit du 8B, et ce qu'on peut en tirer

**Nombres scellés** (`lecture.json` → `descriptifs`, `arret.json`, `episodes.json`, `appariements.json`) :
- arrêt à 15 063,6 s (pour 15 000 s permises) ;
- `episodes.json` écrit à 7 037,2 s depuis le début du run ;
- appariement : 461,0 s ;
- chargement du 8B : 128,0 s ; préchargement du 3B : 48,7 s ;
- génération des épisodes : 73 362 passes de décodage en 6 499,0 s, soit 88,6 ms par passe pour un lot de 8.

**Ce qu'on en déduit :**
- **Durée de l'étape avant l'arrêt** : 15 063,6 − 7 037,2 − 461,0 ≈ **7 565 s** (borne haute, à quelques secondes de frais près).
- **Notations faites avant l'arrêt : leur nombre n'est consigné nulle part.**
  - `arret.json` → `partiel` n'a pas de compteur, et le journal de l'instance n'a pas de ligne par lot.
  - L'échéance se contrôle avant chaque lot (`_exiger_echeance`, `pilote_a.py`). Il restait donc au moins un lot à faire : entre 1 et 22 lots terminés sur 23, soit **au plus 176 notations**.
- **Débit** : au plus 176 / 7 565 ≈ **0,023 notation par seconde** (environ 84 par heure).
  - Un lot dure en moyenne **au moins 344 s**, soit au moins 43 s par notation.
- **Notations décisives complètes du 8B** : **plus de 7 565 s** dans tous les cas.
  - Environ **7 900 s** si 22 lots étaient faits ; environ 9 700 s s'il n'y en avait que 18.
  - Les nombres ne donnent aucune borne haute.
- **Inférence** : 3 072 passes à 88,6 ms donneraient 272 s par lot. Un lot moyen d'au moins 344 s suggère que les lots vont jusqu'au plafond de 3 072 jetons, avec des passes plus lentes (contextes plus longs).
  - Si c'est le cas, beaucoup de réponses seraient coupées, donc incomplètes. Le motif « plus de 20 % de réponses incomplètes » du plan B pourrait alors jouer. C'est une hypothèse, sans mesure.
- **3B** : aucune mesure. Estimation sans mesure : 0,6 à 1,0 fois la durée du 8B, soit environ 4 700 à 7 900 s.

**Devis** (ordres de grandeur) :

| poste | durée |
|---|---|
| mise en place (mesurée au pilote : création 10:35:13 → début du run 10:51:25, dont tests 801 s) | ≈ 970 s |
| chargements | ≈ 180 s |
| notations décisives du 8B | 7 600 à 9 700 s |
| notations décisives du 3B | 4 700 à 9 700 s |
| fin et poussées | ≈ 200 s |
| **total** | **≈ 13 600 à 20 400 s, soit 3,8 à 5,7 heures de carte** |

- Au prix du pilote (1,0889 USD par heure), cela fait **environ 4,1 à 6,2 USD**, plus le téléchargement et le disque.
- **Le bas de la fourchette de R-155 (3 heures) n'est pas tenable** : le 8B seul, mise en place comprise, prend déjà au moins 2,4 heures.

**Échéance.** Les deux juges dépassent probablement l'échéance unique de 15 000 s du pilote.
- **Option recommandée :** un run par juge, chacun avec sa propre échéance. Par exemple, 8B à 11 000 s, soit environ 1,4 fois 7 900 s.
- **Autre option :** un seul run avec une échéance d'au moins 19 000 s. Il faut alors une nouvelle version des scripts de l'instance : la surveillance arrête l'instance 17 700 s après sa création, et le délai externe est de 270 minutes.
- Dans les deux cas, prévoir un lot de dépassement (environ 6 minutes) et une ligne de progression par lot dans le journal.

---

Je n'ai rien écrit dans le dépôt, n'ai lancé aucune commande Vast.ai et n'ai ouvert aucun des fichiers interdits par D-20.

Fichiers lus :
- `/home/user/controle-ia-travail/prereg/T0.5-pilote-8B-v1.md`
- `/home/user/controle-ia-travail/docs/verdicts/verdict-T0.5-pilote-v1.md`
- `/home/user/controle-ia-travail/registres/decisions.md` (R-155, N-020)
- `/home/user/controle-ia-travail/diag/20261012-150724-t05-pilote-analyse/lecture.json` (`396a7dff…`)
- `/home/user/controle-ia-travail/diag/20261012-105125-t05-pilote-reel/{arret,episodes,appariements}.json`
- `/home/user/controle-ia-travail/src/controle_ia/environnements/{lancer_pilote_a,pilote_a,lire_pilote}.py`

Scripts de lecture des structures (nombres seulement) : `/tmp/claude-0/-home-user-controle-ia/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/notations-seules/lecteur-texte-regles/`.