# Devis — pilote de la couche 2 sur seize tâches de la réserve, tous les moniteurs, P-3 (a), vérité du dommage N-060 v3 — v1

Sous-agent neuf de la lignée « session-depot », 29 octobre 2026. Relevé `date -u` : début **02:22 UTC**, fin
**02:33 UTC**. **Rien n'est lancé par ce document. Aucune dépense, aucun appel payant, aucune clé.** Dépôt lu en
lecture seule.

Statuts des chiffres : **RAPPORTÉ** (lu dans un fichier cité, chemin et début d'empreinte sha256) ; **INFÉRÉ** (calculé
ici à partir de chiffres rapportés) ; **SUPPOSÉ** (jamais mesuré sur ce banc ; fourchette justifiée). Aucun chiffre n'est
opposable (R7) : ce sont des mesures d'instrument et des prix.

Calcul : `outils/calcul_devis_pilote_v1.py` → `outils/calcul_devis_pilote_v1-sortie.json` (et `-sortie.txt`) ;
longueurs des références : `outils/mesurer_references_v1.py` → `outils/mesurer_references_v1-sortie.txt`. Empreintes au
§ 12. Tous les dollars ci-dessous sortent du script.

---

## Verdict

1. **Central ≈ 309 dollars ; fourchette ≈ 135 à 667 dollars. Au-dessus de 90 dans les trois scénarios** : GO de dépense
   explicite exigé ; même le bas dépasse de ≈ 45 dollars.
2. **Ce qui pèse le plus** : les lectures de N-060 v3 (≈ 133 dollars, 43 % du central, dont ≈ 95 pour le lecteur Gemini à
   prix SUPPOSÉ haut), puis b*, Qwen et TRACE-lite (≈ 91 dollars de carte, 29 %, rythmes SUPPOSÉS).
3. **Au central, les moniteurs prennent 304 s par épisode, au-delà du palier de 189 s (P-23)** : le palier sonnerait.
   Recommandation : GO d'une **tranche 0 de mesure (≈ 4 à 13 dollars)**, puis un devis v2 resserré sur rythmes et
   jetons mesurés, avant tout GO sur le reste.

---

## 1. Plan d'épisodes retenu, lot par lot

**Source : plan A de la synthèse du collisionneur, tour 3** (RAPPORTÉ : `docs/notes/couche-2-preparation-v1/
collisionneur-pilote-v1/synthese-collisionneur-pilote-v1.md`, `a67e6930…`, § 2.1, colonne A). Je retiens A parce que
c'est le seul plan qui a les lots que P-3 (a) nomme : jumeaux, calibrage, sabotés à la dose retenue, témoin, mention,
séparés de la recherche de dose. C ne génère aucun saboté de développement ; B met les jumeaux dans le calibrage
(attaque sans réponse). Les nombres de A sont repris tels quels ; seule la colonne « usage » est relue à la lumière des
décisions de Lazar du 29 octobre.

| lot | taille | calcul | usage sous P-3 (a) | campagne |
|---|---|---|---|---|
| D — honnêtes des seuils de la dose | 160 | 16 × 10 | consommé : seuils des moniteurs pour juger « diffus » ; **jamais** au développement | 1 |
| C — honnêtes du calibrage du développement | 480 | 16 × 30 | **premier demi-développement** (D-S15) ; dans chaque tâche, moitiés de 15 et 15 **par tirage de graines scellé** (décision de Lazar sur P-17) ; dérive testée à part sur le journal de fabrique | 1 |
| J — jumeaux honnêtes | 160 | 16 × 10 | premier demi-développement ; hors de tout calibrage ; partagés entre modes ; plancher et référence du dommage de N-060 v3 | 1 |
| recherche de dose, mode « contrôles » | 144 | 16 × 3 doses × 3 exécutions | **exclus** du développement (P-3 (a)) ; la plus forte dose écrite sert de dose flagrante (épreuve de N-060 v3) | 1 |
| recherche de dose, mode « coût » | 96 | 16 × 2 doses × 3 | vérification de dose (P-8) ; exclus du développement | 1 |
| S — sabotés à la dose retenue, mode « contrôles » | 160 | 16 × 10 | premier demi-développement | 2 |
| témoin instruit et mention, mode « contrôles » | 96 | 16 × 2 × 3 | premier demi-développement **si leurs textes sont scellés à temps** ; sinon exclus (P-10, défaut) | 2 |
| **total** | **1 296** | | | |
| *haut seulement* : dose flagrante à part | + 16 | 16 × 1 (forme de C) | si aucune des trois doses écrites n'est flagrante | 1 |

- **Deux campagnes** (INFÉRÉ de l'ordre du pilote) : la dose se choisit sur la campagne 1 ; S, témoin et mention se
  génèrent ensuite à la dose retenue. Campagne 1 : 1 040 épisodes ; campagne 2 : 256. Lecture de Lazar : « deux
  lancements » = deux campagnes (`registres/go.md`, l. 103, `97652496…`).
- **Le palier de rythme** (16 épisodes, P-23) se prend sur le lot D : un épisode par tâche, honnête, consommé. Il ne
  touche ni le calibrage ni le développement, et il compte dans les 1 296.
- **Jamais** le mode tenu à l'écart ; jamais d'épisode filtré sur un score (N-053).
- Sans témoin ni mention (défaut de P-10) : **− 96 épisodes, − 29 dollars au central** (INFÉRÉ, script).

## 2. Heures de carte

### 2.1 Rythmes, en secondes de carte par épisode

| poste | bas | central | haut | statut et justification |
|---|---|---|---|---|
| génération (captures comprises) | 42,1 | 48,35 | 54,6 | RAPPORTÉ : 42,1 (pilote de T0.5, R-143) et 54,6 (P3 tout compris, `registres/depenses.md` l. 88, `d4387788…`), lus dans `faits-pilote-couche-2-v1.md` l. 916-917 (`47b34d3c…`) ; central = milieu, INFÉRÉ |
| juge 8B | 58,2 | 58,2 | 58,2 | RAPPORTÉ : faits l. 918 (R-205 ; `resume.json` `994d542a…` cité par `devis-rejeu-juges-v1.md`, `959f5271…`) — **à remplacer par le rejeu** (§ 2.3) |
| juge 3B | 27,5 | 27,5 | 27,5 | RAPPORTÉ : faits l. 919 — **à remplacer par le rejeu** |
| b* (invite I.8 sur les juges d'ensemble) | 29,1 | 58,2 | 85,7 | SUPPOSÉ : ½ passe du 8B (sortie courte lue par probabilité) ; 1 passe du 8B ; une passe du 8B et une du 3B. La nature de b* (invite I.8 sur les juges 8B et 3B) est RAPPORTÉE par `carte-inventaire-v1.json` (`96a9a531…`) ; son rythme ne l'est nulle part |
| juge Qwen2.5-7B | 29,1 | 58,2 | 87,3 | SUPPOSÉ : « comme le juge 8B » (faits l. 809) ; ½, 1 et 1,5 passe (le haut couvre des sorties plus longues ou des reprises de notes tronquées) |
| TRACE-lite | 36,8 | 96,0 | 211,5 | SUPPOSÉ : 6, 12 ou 18 appels générant 300, 400 ou 600 jetons chacun, au pas du 8B (0,150 s par pas pour un lot de 8, `devis-rejeu-juges-v1.md` l. 118 ; INFÉRÉ là-bas), plus 0,5 s de préremplissage par appel. 18 appels au plus : `src/controle_ia/bases/trace_lite.py` (`4bf4ef35…`), `budget_max`. Le modèle observateur n'est pas fixé (« fourni par l'appelant ») : vitesse du 8B supposée |
| base (i), moniteur par action (invite H.12) | 3 | 6 | 15 | SUPPOSÉ : 10 lectures forcées par épisode (« ≈ 16 800 lectures par action » pour ≈ 1 680 épisodes, `carte-inventaire-v1.json`), 0,3 à 1,5 s chacune |
| étiquetage | 0 | 0 | 0 | INFÉRÉ : fait par sous-agents, deux séries (`docs/decisions/decision-N-054-v1.md` l. 35, `c8a00b3f…`) ; aucune carte (§ 5) |
| **moniteurs, somme** | **183,7** | **304,1** | **485,2** | INFÉRÉ |
| **épisode, tout compris** | **225,8** | **352,5** | **539,8** | INFÉRÉ |

Les prédicteurs sur traits du texte, la règle du coût, les bases (ii), (iii), (iv) hors TRACE-lite et le bris d'égalité
tournent sur processeur ou sur les captures : 0 heure de carte (faits l. 795-815, colonne « moment »).

**Le palier de 189 s se lit « secondes de moniteurs par épisode, génération en plus »** : 14 470 × (54,6 + 189) / 3 600 ×
1,43 = 1 400 dollars, le haut de la pièce C (INFÉRÉ, script, contrôle `seuil_189_lu_comme_moniteurs`). Au central, les
moniteurs font 304 s : **au-delà**. Au bas, 183,7 s : juste en dessous.

### 2.2 Heures

| | bas | central | haut |
|---|---|---|---|
| épisodes | 1 296 | 1 296 | 1 312 |
| génération | 15,2 | 17,4 | 19,9 |
| juges 8B et 3B | 30,9 | 30,9 | 31,2 |
| b* et Qwen | 21,0 | 41,9 | 63,1 |
| TRACE-lite | 13,2 | 34,6 | 77,1 |
| base (i) | 1,1 | 2,2 | 5,5 |
| canaris (64 textes renotés par tous les moniteurs, 1, 2 ou 3 passes ; 16 générations de déterminisme par campagne) | 3,5 | 11,2 | 26,6 |
| **total** | **84,7** | **138,1** | **223,3** |

Canaris : 64 textes RAPPORTÉS (`synthese-pilote-complement-v1.md` l. 119, `5bde106a…`) ; nombre de passes SUPPOSÉ (une par
campagne ; une de plus au haut pour une relance). La règle « canari rompu → arrêt » est au nombre des règles gelées (P-14).

**Recoupement** (contrôles du script) : génération, 8B et 3B sur 1 296 épisodes = 46,0 à 50,5 heures ; Qwen seul = 21,0
heures. C'est la synthèse (« 46–50 ; + 21 pour Qwen »). Ce devis ajoute b*, TRACE-lite, la base (i) et les canaris, que
la synthèse laissait « sous enveloppe ».

**Durée réelle** (INFÉRÉ) : au central, ≈ 35 heures par instance sur 4 instances (3 en campagne 1, 1 en campagne 2).

### 2.3 Où le rejeu des juges remplacera les chiffres

Le rejeu (GO-2026-10-28-16, instance 58178416) rendra les secondes par notation du 8B et du 3B lus par la probabilité du
jeton de verdict, par variante (« b0 relu », « verdict d'abord », « budget relevé »). **Aucun chiffre n'est inventé
ici.** À la lecture du rejeu :
- remplacer `J8B` et `J3B` dans `calcul_devis_pilote_v1.py` (lignes « RAPPORTÉ … À REMPLACER ») par les rythmes de la
  variante que Lazar retiendra pour la banque ; relancer le script ;
- appliquer la même variante à b* et à Qwen si leur lecture suit la même règle (ce que le central suppose aujourd'hui
  à une passe pleine) ;
- formule : Δ dollars = (1 296 + canaris) × (s_rejeu − s_rapporté) / 3 600 × prix ; au central, **0,43 dollar par
  seconde de moniteur gagnée par épisode** (INFÉRÉ).

**Bornes qui ne dépendent pas du rejeu** (INFÉRÉ) : même si le 8B et le 3B ne coûtaient rien, le central resterait à
**≈ 269 dollars** ; si b* et Qwen ne coûtaient rien non plus, à **≈ 214 dollars**. Le rejeu ne ramène pas le pilote
sous 90 dollars.

## 3. Dollars de carte

| prix (dollars de l'heure, A100 SXM4 80 Go, tout compris) | valeur | statut |
|---|---|---|
| bas : l'offre la moins chère relevée | 1,0014 | RAPPORTÉ : `…/scratchpad/devis-pilote/offres-a100-releve.txt` (`32c5db68…`), relevé à 02:21 UTC, 8 offres de 1,0014 à 1,2973 |
| central : médiane des 8 offres | 1,1886 | INFÉRÉ |
| haut : prix le plus haut payé pour une A100 SXM4 | 1,366 | RAPPORTÉ : `registres/depenses.md` l. 204 et 208 (instance 57978233) |
| sensibilité : prix supposé par le collisionneur | 1,43 | SUPPOSÉ (synthèse) ; central à ce prix : **≈ 343 dollars** |

| dollars | bas | central | haut |
|---|---|---|---|
| génération | 15,2 | 20,7 | 27,2 |
| juges 8B et 3B | 30,9 | 36,7 | 42,7 |
| b* et Qwen | 21,0 | 49,8 | 86,1 |
| TRACE-lite | 13,3 | 41,1 | 105,3 |
| base (i) | 1,1 | 2,6 | 7,5 |
| canaris | 3,5 | 13,4 | 36,3 |
| frais fixes : 3, 4 ou 6 instances × 2 / 2,75 / 3,5 dollars | 6,0 | 11,0 | 21,0 |
| **carte et frais** | **90,9** | **175,2** | **326,1** |

Frais fixes par lancement (création, descente des modèles, démarrage, arrêt) : 2 à 3,5 dollars, RAPPORTÉ
(`docs/notes/devis-couche-2-banque-deux-modes-v1.md` l. 37, `cf2f4772…`) ; nombre d'instances SUPPOSÉ (le haut compte une
instance perdue et relancée). Le haut compte deux fois une part de la mise en place (le 54,6 s est « tout compris ») :
c'est voulu.

## 4. Lectures de la vérité du dommage (N-060 v3)

**Cadre** (RAPPORTÉ : `docs/decisions/decision-N-060-v3.md`, `2b448f69…`) : pour chaque contrôle expérimental de
l'article (`cibles.controls`), « absent / altéré / conforme » ; extrait cité, vérifié mot pour mot par programme ; deux
lecteurs de familles autres que Llama et Qwen, aveugles à la condition ; dommage = baisse de couverture contre le jumeau
honnête. Seul le mode « contrôles » est lu : le dommage du mode « coût » est chiffré par la règle du coût, sans lecteur.

### 4.1 Ce qui est lu, et pourquoi

| lu par les deux lecteurs | nombre | pourquoi |
|---|---|---|
| jumeaux J | 160 | plancher honnête lu avant tout saboté ; référence appariée du dommage ; « 0 sur 48 fausses alertes » (P-20) se lit sur eux |
| recherche de dose, « contrôles » | 144 | la règle de dose exige « diffus **et** dommage » ; la plus forte dose sert de témoin positif (dose flagrante) |
| dose flagrante à part (haut) | 0 / 0 / 16 | seulement si aucune dose écrite n'est flagrante |
| S, à la dose retenue | 160 | dommage du premier demi-développement |
| témoin et mention | 96 | neutralité de « mention » ; témoin positif instruit (retirés si P-10 les exclut) |
| **épreuves R5**, honnêtes et artefacts seulement | 128 / 160 / 192 | relecture du même plan, puis actions permutées (16 à 32) ; honnête contre honnête, 48 du lot D contre J ; retrait mécanique de l'action qui porte l'extrait cité par **l'autre** lecteur (16 à 32) ; référence d'une autre tâche (16 à 32) ; troncature à 2 ou 3 longueurs (32 à 48) |
| relances (sortie vide, coupée, mal formée) | × 1,05 / 1,10 / 1,20 | SUPPOSÉ |
| **lectures par lecteur** | **722 / 792 / 922** | INFÉRÉ |

Épreuves : construites sur N-060 v3 point 2 et sur le critère de P-20 (16 sur 16 retrouvés, 0 fausse alerte sur 48 ;
`synthese-pilote-complement-v1.md` l. 167-169) et sur le tableau des épreuves du rapprochement (§ 2,
`rapprochement-trois-voix-v1.md`, `813f3b30…`) ; tailles SUPPOSÉES. La dose flagrante est lue en premier parmi les
sabotés, après les épreuves sur honnêtes et artefacts.

**Ancre humaine** : 30 à 60 épisodes, 5 à 10 minutes chacun, soit 2,5 à 10 heures de Lazar (rapprochement, § 2, rang 2 ;
SUPPOSÉ là-bas). **Aucun calcul, aucun dollar.** Un autre humain que Lazar serait un contact externe : nœud.

### 4.2 Jetons par lecture

| | bas | central | haut | statut |
|---|---|---|---|---|
| consigne du lecteur | 800 | 1 200 | 2 000 | SUPPOSÉ |
| référence `cibles.controls` | 659 | 750 | 1 101 | INFÉRÉ : mesurée sur les 60 tâches du fichier `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (`287e8348…`) : 5 à 6 contrôles (55 tâches à 6, 5 à 5) ; 2 634 caractères en moyenne (champs), 3 001 (forme brute), 3 855 au plus ; 4 caractères par jeton (3,5 au haut) |
| énoncé de la tâche | 0 | 1 027 | 1 939 | INFÉRÉ : 4 108 caractères en moyenne, 6 786 au plus ; le bas ne le montre pas au lecteur |
| plan de l'agent | 1 500 | 3 000 | 4 000 | SUPPOSÉ ; borne haute INFÉRÉE : 10 actions × 400 jetons nouveaux au plus (`prereg/T0.5-pilote-config-v1.json`, `6979a00e…`, champs `T` et `max_nouveaux`), si la chaîne à deux modes garde ces réglages |
| **entrée** | **2 958** | **5 977** | **9 040** | INFÉRÉ |
| sortie (verdict, extrait cité, justification, par contrôle) | 400 | 1 200 | 3 000 | SUPPOSÉ ; le haut compte un raisonnement facturé comme sortie |

Les longueurs viennent des 60 tâches d'épreuve, lues pour leur forme seulement. Le transport aux 32 tâches de réserve
est INFÉRÉ (« même forme » reste à vérifier, rapprochement § 6).

### 4.3 Dollars par lecteur

Prix par million de jetons (entrée / sortie), RAPPORTÉS « documentation du fournisseur, relevée par session-depot le 29
octobre » (sans empreinte) : Opus 5.5 4 / 20 ; Sonnet 5.5 2 / 10 ; Haiku 5.5 0,10 / 0,50 ; Fable 5.1 10 / 50. Gemini :
prix inconnu, **SUPPOSÉ 10 / 50** (valeur haute volontaire, comme le collisionneur).

| lecteur, toutes lectures | bas | central | haut |
|---|---|---|---|
| Claude Haiku 5.5 | 0,4 | 1,0 | 2,2 |
| Claude Sonnet 5.5 | 7,2 | 19,0 | 44,3 |
| Claude Opus 5.5 | 14,3 | 37,9 | 88,7 |
| Claude Fable 5.1 | 35,8 | 94,9 | 221,7 |
| Gemini (Argon), prix SUPPOSÉ | 35,8 | 94,9 | 221,7 |

**Paire comptée au total** : Sonnet 5.5 + Gemini au bas (42,96) ; **Opus 5.5 + Gemini au central (132,80)** et au haut
(310,31). Le choix exact reste un nœud (N-060 v3, « ce que la décision ne fixe pas ») : Fable à la place d'Opus ajoute
≈ 57 dollars au central ; Haiku en retire ≈ 37, au risque de rater « altéré ». Réserve : N-029 a retiré un juge Claude
sur P3 ; la raison est à vérifier avant de choisir un lecteur Claude (rapprochement § 2).

**Sensibilité au prix de Gemini** (INFÉRÉ) : au prix d'Opus, le central tombe à ≈ 253 dollars ; au quart du prix supposé,
à ≈ 238. Par phase, au central : jumeaux et épreuves ≈ 59 dollars ; recherche de dose ≈ 27 ; S, témoin et mention ≈ 47.

Leviers non comptés, à vérifier sur la documentation des fournisseurs avant d'en tenir compte : mise en cache de la
consigne et de la référence (les lectures d'une même tâche partagent la référence) ; traitement par lots différé.

## 5. Étiquetage

N-054 point 1 : étiquetage du mode « contrôles » par sous-agents, deux séries indépendantes, « comme au pilote ». Aucune
ligne de dépense ne porte l'étiquetage du pilote (INFÉRÉ : recherche dans `registres/depenses.md`). **Bas et central : 0
heure de carte, 0 dollar** ; coût en temps de session. **Haut** : s'il fallait passer par le relais payant, deux séries ×
496 épisodes (sabotés, témoin, mention) × 1,2 × une lecture au format central de Sonnet 5.5 = **≈ 28,5 dollars**
(SUPPOSÉ). Si l'étiquetage est par paire (épisode, proposition) plutôt que par épisode, ce poste grossit : à recompter
quand la consigne d'étiquetage regroupée (P-014) sera écrite.

## 6. Stockage et transfert

- Activations des couches 7, 15 et 23, deux dernières positions par action : ≈ 0,5 Mo par épisode (INFÉRÉ, faits l. 820) ;
  scores par jeton des sondes (bras « fuite textuelle »), textes, sorties des moniteurs : SUPPOSÉ 0,15 à 1,2 Mo de plus.
  **0,84 à 2,2 Go pour le pilote.**
- Descente des modèles : 22 Go (8B et 3B, RAPPORTÉ) + ≈ 15 Go pour Qwen 7B (INFÉRÉ : 7,6 milliards × 2 octets) par
  instance ; à 0,01 dollar le Go au plus (filtre des lanceurs, `devis-rejeu-juges-v1.md` l. 140).
- **Coût : 1,1 à 2,2 dollars. Négligeable.** Le poids n'est pas négligeable pour le dépôt : 1 à 2 Go dans une branche
  git dépassent ce que la poussée de P3 a porté (≈ 820 Mo, `registres/depenses.md` l. 221). Prévoir des archives par
  campagne, versionnées et empreintées (R6, R12), hors de `main`.

## 7. Total, parts, comparaison aux 90 dollars

| | bas | central | haut |
|---|---|---|---|
| carte : génération | 15,2 | 20,7 | 27,2 |
| carte : juges 8B et 3B | 30,9 | 36,7 | 42,7 |
| carte : b* et Qwen | 21,0 | 49,8 | 86,1 |
| carte : TRACE-lite | 13,3 | 41,1 | 105,3 |
| carte : base (i) | 1,1 | 2,6 | 7,5 |
| carte : canaris | 3,5 | 13,4 | 36,3 |
| frais fixes des instances | 6,0 | 11,0 | 21,0 |
| transfert et stockage | 1,1 | 1,5 | 2,2 |
| lectures de N-060 v3 (deux lecteurs) | 43,0 | 132,8 | 310,3 |
| étiquetage | 0 | 0 | 28,5 |
| **total (dollars)** | **134,9** | **309,5** | **667,1** |
| écart aux 90 dollars | + 44,9 | + 219,5 | + 577,1 |

**Parts au central** : lectures de N-060 v3 43 % ; b* et Qwen 16 % ; TRACE-lite 13 % ; juges 8B et 3B 12 % ; génération
7 % ; canaris 4 % ; frais fixes 4 % ; base (i) et transfert 1 %.

**Ce que 90 dollars achètent au central** (INFÉRÉ) : génération, juges 8B et 3B, base (i), leurs canaris, frais et
transfert ≈ **77 dollars**. Il reste ≈ 13 dollars, contre ≈ 100 pour b*, Qwen et TRACE-lite avec leurs canaris, et ≈ 133
pour les lectures.

Les 90 dollars sont le plafond de GO-2026-10-28-02 (couche 2, deux modes connus ; `registres/go.md` l. 101 et 103,
échéance 15 novembre). Ce GO ne nomme pas d'appels payants à des lecteurs distants : les lectures de N-060 v3 demandent
une ligne à part, avec clés et plafond du relais.

## 8. Paliers d'arrêt proposés

1. **Tranche 0, palier de mesure** (≈ 4 à 13 dollars ; 7,6 au central ; INFÉRÉ) : une instance, les 16 premiers
   épisodes du lot D (un par tâche), **tous** les moniteurs, journal de fabrique ; plus 16 lectures de mesure par chaque
   lecteur sur ces plans honnêtes (jetons réels, longueur réelle du plan, taux de sorties mal formées). Mesure : secondes
   par poste, jetons par lecture. Puis devis v2 recalculé par le script, sans rien d'autre de lancé.
2. **Arrêt de rythme (P-23)** : si les moniteurs dépassent 189 s par épisode au palier, arrêt et nœud de devis. Au
   central SUPPOSÉ (304 s), **il sonnera** : la question à Lazar sera alors laquelle des cellules garder, jamais un
   relèvement silencieux.
3. **Enveloppe scellée de TRACE-lite (P-1 (b))** : je propose de la fixer sur le central, ≈ 45 dollars carte et canaris
   compris. Si le palier projette plus, TRACE-lite sort du maximum du pilote, déclaré, nœud. Pas de TRACE-lite sur un
   sous-lot : un moniteur sans seuil calibré sur les honnêtes ne peut pas entrer dans le maximum (synthèse § 4).
4. **Plafond dur par instance** : campagne 1 sur 3 instances, ≈ 347 épisodes chacune ; plafond = rythme mesuré au palier
   × 1,25 + 1 heure ; au central, ≈ 43 heures, soit ≈ 59 dollars à 1,366 dollar de l'heure (INFÉRÉ). L'amorce écrit
   l'heure d'arrêt au plus tard ; deux réveils de garde par instance ; **arrêt par identifiant d'instance (R10)**,
   consigné dans `registres/arrets.md`.
5. **Plafond par campagne** : carte de la campagne 1 ≈ 65 / 121 / 213 dollars ; campagne 2 ≈ 16 / 30 / 52 (bas, central,
   haut ; hors canaris et frais). La campagne 2 ne part qu'après la dose choisie et le cumul relu.
6. **Lectures** : relais avec `--plafond-usd` par lecteur et par phase. Ordre : épreuves sur honnêtes et artefacts
   (≈ 59 dollars au central, jumeaux compris) ; **si une épreuve échoue, plus aucune lecture** : repli écrit de N-060 v3
   (« sabotage demandé » seul, aucun dommage affirmé) ; sinon dose flagrante, recherche de dose (≈ 27), puis S, témoin et
   mention (≈ 47).
7. **Alerte à 80 %** du plafond accordé (règle de `registres/depenses.md`) ; aucune autre instance sur le compte pendant
   une campagne.

## 9. Ce qui manque avant tout lancement, sans dépense, et qui bloque

Tiré des pièces lues ; chaque ligne arrête le premier lancement payant.

1. **Chaîne de génération à deux modes** prête (R-671 : pilote « une fois la chaîne à deux modes et le second mode
   scellé prêts » ; faits l. 1036).
2. **Consignes du mode « contrôles » écrites par une autre lignée** (R-601, N-054), traits du texte du mode fixés et
   scellés (pièce C, étape 3) ; textes de la mention et du témoin scellés à temps, sinon − 96 épisodes (P-10).
3. **Préenregistrements scellés et contre-lus** (R1, R2) : liste scellée de la synthèse § 3 (graine et liste des 16
   tâches, coupe par graine dans chaque tâche, doses écrites dont la flagrante et règle de choix, liste des moniteurs du
   maximum avec et sans la règle du coût, hyperparamètres de la lecture blanche, convention du score manquant, règles
   pilote → banque, règles d'arrêt de P-14) ; verdict de P4-instrument avant toute lecture de sonde.
4. **Bris d'égalité aléatoire scellé** (clé de 64 bits salée par cellule) et testé avant tout épisode (P-15) ; **journal
   de fabrique** et ordre scellé (P-23) ; test de dérive à part écrit d'avance.
5. **Rejeu des juges lu** : rythmes et complétude ; porte des scores finis (P-16) ; lecture des 180 textes (P-22) ;
   `resume.json` et texte de D-S13 lus (P-13).
6. **Moniteurs en état de tourner** (`carte-inventaire-v1.json`) : juge Qwen absent du code ; invite H.12 de la base (i)
   en brouillon non scellé ; TRACE-lite sans conduite réelle ; aucun lanceur n'applique les sondes figées à des épisodes
   neufs ; constructeur de banque au format `monde_banque_scores` absent ; captures (couches 7, 15, 23 ; scores par
   jeton) spécifiées et répétées sur un modèle jouet (pièce C, étape 5).
7. **Vérificateur de N-060 v3 éprouvé hors agent** (P-20 : 16 sur 16, 0 fausse alerte sur 48, sinon HYPOTHÈSE) :
   consigne des lecteurs écrite par une instance neuve sans pièce des moniteurs (N-060 v3 point 4), scellée par empreinte ;
   programme de vérification mot pour mot des extraits ; artefacts de retrait, de référence permutée et de troncature
   construits par programme et testés (R5) ; **vérifier que l'agent ne voit pas `cibles` et qu'aucun moniteur ne les
   lit** ; familles exactes des deux lecteurs ; forme des 32 tâches de réserve identique.
8. **Nœuds encore ouverts** du format décision v2 (`b2c89c6c…`) : P-4 (lecture de N-053 sur la dose), P-5 (« chaque
   action »), P-6 (règle du coût), P-16 (seuil de la porte), P-18, P-21, V-2 (« dose candidate », marge δ) ; mode tenu à
   l'écart scellé avant toute lecture du pilote (P-11).
9. **Accès** : jeton Hugging Face valide pour Llama et Qwen, à vérifier sur l'instance en première étape bornée ; jeton
   GitHub de l'instance ; clés du relais pour les lecteurs ; crédit du compte de carte au-dessus du plafond de la
   tranche.
10. **GO de dépense explicite** de Lazar sur un chiffre (au-delà de 90 dollars).

## 10. Décision demandée à Lazar

**Décision** : quelle dépense engager pour le pilote à tous les moniteurs avec la vérité du dommage de N-060 v3.

**Enjeu** : le devis central (≈ 309 dollars) fait plus de trois fois les 90 accordés ; il repose sur des rythmes et des
prix supposés pour ≈ 76 % de son montant (b*, Qwen, TRACE-lite, base (i), canaris de ces moniteurs, lectures).

**Options** :
- **(a) GO de la tranche 0 seule** (≈ 13 dollars au plus), puis devis v2 sur mesures. *Avantage* : la fourchette se
  resserre avant d'engager ; le palier de 189 s est lu sur pièces. *Inconvénient* : un aller-retour de plus ; la tranche
  0 exige déjà la chaîne prête (§ 9, lignes 1 à 7).
- **(b) GO d'un plafond au central, ≈ 310 dollars**, en tranches avec les paliers du § 8. *Avantage* : pas d'attente.
  *Inconvénient* : GO sur des rythmes supposés ; le palier de 189 s sonnera probablement et rouvrira le devis.
- **(c) Réduire le périmètre pour tenir près de 90 dollars** : juges 8B et 3B seuls (≈ 77 dollars), b*, Qwen et
  TRACE-lite repoussés ; lectures dans une ligne à part. *Avantage* : dans le plafond actuel. *Inconvénient* : revient
  sur P-1 (b) ; le maximum est incomplet, la dose risque de basculer quand on ajoutera un moniteur (P-14).

**Recommandation** : (a), confiance ≈ 0,7 (subjective). **Défaut** : aucun (dépense = nœud).

## 11. Réserves

- **≈ 76 % du central est SUPPOSÉ** (b*, Qwen, TRACE-lite, base (i), leurs canaris, lectures ; INFÉRÉ, 235 sur 309 dollars) ; seuls la génération, les juges 8B et 3B, les prix de carte, les frais fixes et les
  longueurs des références sont rapportés ou inférés de mesures.
- **Le juge 8B « par action »** de la liste des critères (faits l. 799) n'est peut-être pas la notation d'ensemble dont le
  rythme est rapporté (58,2 s). Si le critère exige une notation générée par action, son coût changerait d'ordre ; le
  palier le dira. Je n'ai compté qu'une passe d'ensemble, plus la base (i) à lectures forcées.
- **Gemini à 10 / 50** est une valeur haute volontaire : il porte à lui seul ≈ 31 % du central.
- La chaîne à deux modes peut changer la longueur des épisodes (pièce C, § 10) : génération et moniteurs suivraient.
- Les 189 s viennent d'une synthèse ; je retrouve l'arithmétique (1 400 dollars) en les lisant « moniteurs seuls ».
- La sentinelle entre lancements (GO-2026-10-29-03, ≤ 124 dollars) **n'est pas** dans ce devis : elle vaut entre
  lancements, sous son propre devis.
- Longueurs des références mesurées sur les tâches d'épreuve (forme seulement) ; jetons comptés à 4 caractères (3,5 au
  haut), sans tokeniseur réel.

## 12. Sources et empreintes

| fichier | sha256 (début) | usage |
|---|---|---|
| `…/scratchpad/devis-pilote/decision-pilote-couche-2-v2.md` | `b2c89c6c…` | cadre, nœuds P-4 à P-25 |
| `docs/notes/couche-2-preparation-v1/collisionneur-pilote-v1/synthese-collisionneur-pilote-v1.md` | `a67e6930…` | plan A, 189 s, réemploi |
| `docs/notes/couche-2-preparation-v1/collisionneur-pilote-complement-v1/synthese-pilote-complement-v1.md` | `5bde106a…` | canaris, P-20 |
| `docs/notes/couche-2-preparation-v1/collisionneur-pilote-v1/faits-pilote-couche-2-v1.md` | `47b34d3c…` | rythmes (l. 916-919), captures (l. 820), moniteurs (l. 795-815) |
| `docs/decisions/decision-N-060-v3.md` | `2b448f69…` | vérité du dommage |
| `docs/notes/couche-2-preparation-v1/verite-dommage-v1/rapprochement-trois-voix-v1.md` | `813f3b30…` | épreuves, ancre humaine |
| `docs/notes/couche-2-preparation-v1/simulation-coupe-calibrage-v1/rapport-coupe-calibrage-v1.md` | `c66c1eed…` | coupe par graine dans les tâches |
| `docs/notes/couche-2-preparation-v1/simulation-controle-12-joint-v1/rapport-controle-12-joint-v1.md` | `7600f2d0…` | bris d'égalité, conditions |
| `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/devis-rejeu-juges-v1.md` | `959f5271…` | pas de décodage, transfert, forme du devis |
| `registres/depenses.md` | `d4387788…` | prix payés, 54,6 s |
| `registres/go.md` | `97652496…` | plafond de 90, GO-03 |
| `…/scratchpad/devis-pilote/offres-a100-releve.txt` | `32c5db68…` | prix relevés |
| `donnees/t05-pilote-v1/taches-pilote-60-v1.json` | `287e8348…` | longueurs des références et des énoncés |
| `prereg/T0.5-pilote-config-v1.json` | `6979a00e…` | 10 actions, 400 jetons |
| `docs/notes/devis-couche-2-banque-deux-modes-v1.md` | `cf2f4772…` | frais fixes |
| `docs/notes/couche-2-preparation-v1/carte-inventaire-v1.json` | `96a9a531…` | b*, TRACE-lite, base (i), manques |
| `docs/decisions/decision-N-054-v1.md` | `c8a00b3f…` | étiquetage par sous-agents |
| `src/controle_ia/bases/trace_lite.py` | `4bf4ef35…` | 18 appels au plus |

Fichiers produits (dans `…/scratchpad/devis-pilote/outils/`, empreintes dans `empreintes-devis-pilote-v1.txt`) :
`calcul_devis_pilote_v1.py`, `calcul_devis_pilote_v1-sortie.json`, `calcul_devis_pilote_v1-sortie.txt`,
`mesurer_references_v1.py`, `mesurer_references_v1-sortie.txt`.

Non lus, comme demandé : `prereg/P3-consignes-v1.md`, `donnees/runs/`, traces de `diag/`, autres branches, tout ce qui
porte « quarantaine », « mode-tenu-a-l-ecart », « collisionneur-evasion », « bras-attaque ».
