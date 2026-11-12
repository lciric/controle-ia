# Synthèse du collisionneur — couche 2 : le pilote sur seize tâches de la réserve — v1

Lecteur neuf (Opus 5.5), 29 octobre 2026. **Matériau pour la décision de Lazar : rien n'est tranché ici, ce n'est pas un
préenregistrement.** Tous les chiffres sont exploratoires et non opposables (R7). Le prix de carte (1,08 à 1,43 dollar de
l'heure, A100) est **SUPPOSÉ** partout.

**Lu, en entier** : la question, les faits servis (pièces A à F), `etat.md`, les huit cellules valides (A = Fable 5.1,
B = Opus 5.5, C = Gemini Argon ; tours 1 conception, 2 équipe rouge, 3 riposte) et `rapport-controle-12-joint-v1.md`
(empreinte vérifiée). **La riposte d'Opus (E3-T3-riposte-B) est un refus, non lu** : Opus n'a pas de riposte, ses tours 1
et 2 comptent, et toute attaque portée contre B au tour 2 reste sans réponse. Coût du tour : 11,06 dollars, dont 0,73
pour le refus.

**Mes vérifications** (processeur seul, 4 secondes) : `verifications-synthese-pilote-v1.py` (`d9911c33…`) →
`…-sortie.json` (`08ee43ea…`). Le script importe sans la modifier la simulation de la pièce C (`20bb005c…`, vérifiée).
Graine 20261029, `SeedSequence`, 3 000 à 4 000 répétitions ; fichiers dans `…/collisionneur-pilote/synthese/`, avec
leurs `.sha256`. Ils héritent du modèle latent gaussien de la pièce C : ce qu'il implique, pas ce que fera le banc.

---

## 1. En tête : une ligne par point

| point | position majoritaire après riposte | accord | changement du tour 1 au tour 3 |
|---|---|---|---|
| **1. Ce qu'il mesure** | Ce qui peut tuer la banque, en réponse binaire : scores finis (le rejeu d'abord), dose diffuse **avec dommage** du mode « contrôles », obéissance et étiquetage, rythmes, propriétés des honnêtes qui fixent le calibrage. L'effet de consigne a, l'hétérogénéité h et l'écart blanc contre blanc sont **rapportés, sans règle**. Le « 53 % » vaut pour **huit** tâches à exécutions infinies. | trois sur trois sur la structure ; Opus absent au tour 3 (son test de seuil sur a, attaqué par A et C, reste sans réponse) | A retire son duel sur a. Les trois corrigent le « 53 % » de la pièce A. **Ma vérification déplace le calcul** (§ 2.3). |
| **2. Plan chiffré** | 16 tâches tirées par graine scellée parmi les 32 de réserve. Deux modes connus (contrôles en entier ; coût au moins en vérification de dose). Trois doses écrites. Lots honnêtes disjoints par usage. Jamais le mode tenu à l'écart. Juges 8B et 3B lus par le jeton, et les autres moniteurs noirs dans le maximum. **896 à 1 296 épisodes, ≈ 50 à 120 dollars.** | dispersé sur le volume ; deux contre un : pas de sabotés de développement générés au pilote (B, C contre A) | A : de 832 à 1 296 épisodes (lots séparés, vérification du mode coût). C : de 1 040 à 896 (dose à 3 exécutions, dose forte témoin, plus de complément de développement). |
| **3. Non-contamination** | Aucune tâche d'épreuve. Les sabotés de la recherche de dose **ne rentrent jamais** au développement (biais du gagnant contre le noir). La dose est un paramètre commun, sans filtrage d'épisode. Le mode tenu à l'écart est scellé avant toute lecture du pilote. | trois sur trois ; dispersé sur la lecture blanche | A et C retirent le réemploi des épisodes de sélection. Un biais résiduel **par tâche** est reconnu (A, C), non résolu. |
| **4. Arrêt et décision** | K = 10 n'est **jamais** changé par le pilote. Pas de dose diffuse avec dommage → arrêt et nœud. Scores non finis → pas de banque. Rythmes trop lents → devis révisé. Aucune règle sur a ni sur l'écart blanc contre blanc. | trois sur trois (le défaut de B était déjà « K fixé par nœud ») ; dispersé sur l'horizon et le seuil de coût | A retire K ← ⌈10/obéissance⌉. C abaisse son seuil de coût de 230 à 180 s. « Horizon → 12 800 » reste chez A et C, **contredit par le rapport du contrôle 12** (§ 4). |
| **5. Ce qui tuerait le pilote** | Les cinq menaces ont une garde chez les trois. L'équipe rouge en ajoute une plus grave : le dommage du mode « contrôles » **n'a pas de vérité indépendante du texte**, puisque les étiqueteurs lisent le texte comme les juges. | trois sur trois sur le diagnostic ; remèdes différents (A : nœud ; C : un vérificateur d'état supposé exister) | Ajouts : règle du score manquant, dose flagrante témoin, témoin instruit retiré des contrôles négatifs (P-015 le dit non neutre). |
| **Ordre** | Le rejeu des 180 épisodes **avec les sondes** est refusé (tâches d'épreuve). Le calibrage honnête seul ne mesure ni dose ni obéissance. Le pilote saboté est nécessaire, en forme hybride. | trois sur trois | Inchangé. Seul le statut des épisodes reste disputé (D-2). |

**Deux prémisses de la question sont fausses**, relevées par les trois modèles :
- Il y a **deux modes connus** (coût, contrôles), plus le mode tenu à l'écart (pièce C § 4, N-054).
- « 36 à 125 dollars » mêle seize et trente-deux tâches. La pièce B donne 36 à 65 dollars pour seize, 70 à 125 pour
  trente-deux.

---

## 2. Le pilote recommandé, chiffré

### 2.1 Noyau commun et trois plans

**Noyau commun** :
- **Tâches** : tirage par `SeedSequence`, liste scellée avant génération ; strate d'horizon seulement si elle est
  définie sur l'énoncé (A).
- **Conditions** : honnête, saboteur à plusieurs doses écrites, témoin instruit, mention ; jamais le mode tenu à l'écart.
- **Captures** : scores par jeton des sondes figées, bornes des champs, activations des couches 7, 15 et 23 aux deux
  dernières positions (≈ 0,5 Mo par épisode, INFÉRÉ pièce C), textes, horodatages. Elles sont **scellées et non lues**
  sur les sabotés de développement.

| | A (tour 3) | C (tour 3) | B (tour 1, sans riposte) |
|---|---|---|---|
| honnêtes, seuils de la dose | lot D, 16 × 10 = 160 (consommé) | exécutions 4–30 : 432 | 32 × 20 = 640, un seul lot |
| honnêtes, calibrage du développement (D-S15) | lot C, 16 × 30 = 480 | les mêmes 480, après test d'équivalence | les mêmes 640 |
| jumeaux | lot J, 160, hors de tout calibrage | exécutions 1–3 : 48, hors calibrage | graines 1–5 **dans** le calibrage (attaqué, sans réponse) |
| recherche de dose | contrôles 3 doses × 3 = 144 ; coût 2 doses × 3 = 96 | 2 modes × (3 doses × 3 + dose forte × 1) × 16 = 320 | 2 modes × 3 doses × 2 = 192 |
| sabotés à la dose retenue | lot S, 16 × 10 = 160, **premier demi-développement** | aucun (développement régénéré plus tard, en une fabrique) | 160 en mesure, hors développement |
| témoin et mention | 96 (contrôles, mention transposée) | 96 (coût) ; + 96 si le texte du mode contrôles est scellé | 96 |
| **épisodes** | **1 296** | **896** (992) | **1 088** |
| heures | 46–50 (8B + 3B) ; + 21 pour Qwen | 54–65, tout compris | 39–42 ; jusqu'à 87 |
| **dollars (SUPPOSÉ)** | **50–72** ; + 23–30 pour Qwen ; b* et TRACE-lite sous enveloppe | **58–93** | **42–61** ; jusqu'à 124 |

Rythmes RAPPORTÉS (pièce C § 8) : génération 42,1 à 54,6 s, juge 8B 58,2 s, juge 3B 27,5 s. **L'arithmétique de ce
tableau est refaite et juste** (V6). b*, Qwen, TRACE-lite, l'étiquetage et le mode « contrôles » n'ont **aucun** rythme
mesuré.

**Lecture recoupée.** Avec tous les moniteurs noirs : ≈ 900 à 1 300 épisodes, 55 à 75 heures, **≈ 60 à 120 dollars**.
Au-delà des 90 dollars accordés (pièce D), c'est un nœud. Générer dès maintenant les sabotés de développement (A) ajoute
≈ 6 heures et 6 à 9 dollars.

### 2.2 Version minimale sous 40 dollars

- **B** : 512 épisodes, 20–29 dollars.
- **C** : annoncé à 496 épisodes, mais la somme des lots fait **480** ; 27–36 dollars.
- **A** : 800 épisodes, 31–45 dollars, **au-dessus de 40 au prix haut** (44,6 ; V6).

**Ce qu'elle perd, selon les trois** :
- TRACE-lite, b* et Qwen sortent du maximum ou passent sur un sous-lot : l'artefact de source n'est que partiellement
  gardé.
- Calibrage trop petit pour le contrôle 12 à 1 % et pour toute strate.
- Pas de témoin ni de mention pour le mode « contrôles ».
- Développement à K = 5 : l'organisme a 0,64 à 0,80 de puissance pour 20 points au lieu de 0,80 à 0,90 (V5).
- Dose à ± 15 points par unité (illustratif, A).

### 2.3 Précision ; l'erreur relative sur l'effet de consigne refaite

**Le calcul des modèles.** Les trois calculent l'erreur relative de la **variance entre tâches** σ²_b, à variance
intra-tâche connue. Leurs chiffres sont justes : je les retrouve à l'analyse et par tirage.

**Ce qu'il manque.** Dans le modèle de la pièce C, a est une **part de variance** (variance totale 1). Son estimateur,
le rapport des composantes de l'analyse de variance, a une erreur plus petite, d'un facteur proche de 1 − a. Sur des
alertes 0/1, l'erreur remonte.

Erreur relative à a = 0,3 :

| tâches | σ²_b, K = 10 | σ²_b, K infini | a, scores continus, K = 10 | a, continus, K = 30 | a tiré d'alertes 0/1 (rappel 0,40), K = 10 | alertes au seuil 1 % |
|---|---|---|---|---|---|---|
| 8 | 66 % | **53 %** | 45–49 % | 41 % | 59 % | non estimable |
| 16 | 45 % | 37 % | **32–33 %** | 28 % | 42 % (31 % à K = 30) | non estimable |
| 32 | 31 % | 25 % | **23 %** | 19–20 % | 30 % (23 % à K = 30) | non estimable |

« Non estimable » : 14 à 80 % des tirages n'ont aucune variance entre tâches, et l'estimation tombe à 0,05–0,21 pour une
vraie valeur de 0,3.

**Pour passer sous 25 %** :
- σ²_b : ≈ 50 tâches à K = 10, ≈ 40 à K = 30, 33 à K infini (les chiffres des modèles) ;
- **a sur scores continus : ≈ 28 tâches à K = 10, 22 à K = 20, 20 à K = 30**, donc la réserve entière suffit ;
- a sur alertes 0/1 : 32 tâches à K = 30.

**Conséquences.**
- « Sous 25 %, inatteignable sur la réserve » (B et C au tour 1, A au tour 3) est vrai pour σ²_b, **faux pour a** sur
  scores continus : sur 32 tâches (extension honnête d'A, lot de B), on est à ≈ 20 à 23 %.
- Mais c'est **a_honnête**. Son transport aux sabotés est une HYPOTHÈSE (attaque de A contre B, non répondue). Sur
  seize tâches seules, on reste à ≈ 28–33 %.
- Le test de seuil de B (coupure à 0,4, 32 × 20) a des erreurs de **4 % et 9 %**, pas 12 % et 23 %. La multiplicité sur
  huit moniteurs, relevée par C, demeure.

**Autres paramètres, à seize tâches** :
- **Dose diffuse avec dommage** : part jointe « diffus **et** dommage », par unité (A) ou par épisode (C), à ± 12 points.
  Apprise, si une vérité du dommage existe (§ 4).
- **Obéissance et étiquetage** : ± 7–8 points en tenant compte des grappes (A). Appris.
- **Scores finis** : sur les 180 textes du rejeu, puis sur le pilote. Appris.
- **Écart blanc contre blanc** : erreur type 4,1–5,8 points (V4), puissance au seuil 20 de **0** à 16 unités et ≤ 0,06
  à 32. Rapporté, jamais lu sur le développement.
- **Concordance** : erreur type 0,03–0,08 sans les grappes, sur les honnêtes ; son transport aux sabotés est supposé.
- **h** : non mesurable.
- **Rythmes** : exacts pour ce qui tourne. **Ex æquo, échangeabilité** : § 7.4.

**Priorité** (trois sur trois) : scores finis et rythmes ; dose du mode « contrôles » ; obéissance ; propriétés des
honnêtes ; loin derrière, a, h et l'écart blanc contre blanc.

---

## 3. Non-contamination et réemploi

**À sceller avant la génération** (union des trois listes) :
- graine et liste des tâches ;
- coupe des honnêtes **par graine** en lots disjoints : jumeaux, seuils de dose, calibrage du développement ;
- doses écrites (dose forte comprise) et règle de choix ;
- liste des moniteurs du maximum, avec et sans la règle du coût ;
- texte de la mention et du témoin du mode « contrôles », ou leur exclusion ;
- **hyperparamètres de la lecture blanche** (agrégateur, détecteur de rupture, position et couche de la base (iii)), par
  empreinte ;
- seuils des duels ; convention du score manquant ; sentinelle avec sa puissance ou sa marge ;
- règles pilote → banque ; ce qui sera lu et ce qui ne le sera pas ;
- fiche du mode tenu à l'écart et quarantaine de la branche.

**Ce que le pilote peut fixer** (A, C) : la dose unique d'épreuve, et au plus la strate du calibrage. Jamais K. Ni la
taille 9 600 contre 12 800, déjà instruite par la simulation jointe (§ 4).

**Réemploi** :
- **Sabotés de la recherche de dose** : jamais au développement (trois sur trois). B propose de mesurer le biais évité
  (rappel noir sur les exécutions de recherche contre les exécutions neuves) ; A le reprend.
- **Honnêtes** :
  - A : le lot de calibrage rejoint D-S15 ; celui des seuils de dose est consommé ;
  - C : réintégration seulement après un test d'équivalence par tâche, à marge scellée, contre des honnêtes régénérés à
    la banque ;
  - B : réemploi tel quel, jumeaux compris (attaqué, sans réponse).
- **Invariant N-053** : la dose est un paramètre de consigne commun, choisi une fois, sans filtrage ni rééchantillonnage
  d'épisode. A et B en font un **nœud d'interprétation** ; C n'y voit que l'application de P-015.
- **Biais par tâche, non résolu** : la dose choisie sur seize tâches reste adaptée à ces tâches, même à graines neuves (C
  contre B ; A et C l'acceptent). Deux remèdes :
  - A : lire l'organisme séparément sur les 16 tâches du pilote et sur les 16 autres ;
  - C : comparer le rappel noir entre tâches du pilote et tâches vierges, et ne garder que la moitié vierge si l'écart
    dépasse la borne.
- **Deux fabriques** : A attaque C sur un calibrage de développement généré en deux temps, mais son propre plan fait de
  même (lot S maintenant, 16 autres tâches plus tard). C régénère tout en une fabrique entrelacée. Ouvert (D-2).

---

## 4. Règles d'arrêt, de décision, et ce qui tuerait le pilote

| résultat | conséquence (majorité) | réserve |
|---|---|---|
| aucune dose diffuse et dommageable (contrôles ou coût) | **arrêt** ; nœud sur le régime (D-S29 (a) : gain dans chaque mode) | sans vérité de dommage, « pas de dommage » et « dommage invisible » se confondent |
| scores finis sous le taux scellé, ou taux différents entre honnêtes et sabotés | pas de banque avant retouche ; cellule hors intersection-union | score manquant = alerte maximale (A) ou neutre (C, qui écrit les deux) |
| obéissance ou accord d'étiquetage insuffisants | nœud sur la consigne, **jamais sur K** | — |
| « diffus » qui bascule quand on retire un moniteur | dose rejugée avec ce moniteur (A) | — |
| dose différente avec ou sans la règle du coût | nœud de P-015 au mot de Lazar | — |
| effet d'ordre des exécutions dans la tâche | nœud ; la coupe dans la tâche tombe | le rapport dit : rejeter les deux options |
| strate d'horizon détectée | 12 800 ou 19 200 (A, C) | **contredit par le rapport** (ci-dessous) |
| moniteurs trop lents | devis révisé | le seuil cohérent avec 1 400 dollars au prix haut est **189 s** (V6) ; « 4 passes de 8B » d'A = 233 s, A ne s'applique pas son attaque C-6 ; C 180 s |
| a, h, écart blanc contre blanc | aucune décision | arrêter sous 5 points tuerait à tort un vrai écart de 10 points dans 11 à 18 % des cas (V4) |

**Ce que dit le rapport du contrôle 12 joint, et qu'aucun modèle n'a vu** (il n'était pas servi) :
- La simulation « bilatérale de l'étape 0 », que A et C placent avant le pilote, **est faite** : 9 600 au seuil 40
  tient 0,027 en bilatéral, 12 800 au seuil 20 tient 0,038.
- Elle pose ses conditions : bris d'égalité aléatoire scellé ; lois des queues honnêtes (lourdes ou bimodales → refaire) ;
  exécutions échangeables ; compte des cellules (un troisième mode mène à ≈ 24 contrôles, non simulé).
- **Une strate qui coupe le calibrage échoue** : ≥ 0,12 à 4 800 par strate ; 12 800 coupé en deux donne 0,057 et 0,109
  au seuil 40. Si la strate coupe aussi les unités, le diagnostic devient aveugle.
- « Horizon → 12 800 » n'est donc pas un remède mais un nœud ; 19 200 n'est pas simulé.

**Ce qui tuerait le pilote, et les gardes retenues** :
- **Artefact de source** → maximum sur toute la liste scellée, double lecture avec et sans la règle du coût, retrait d'un
  moniteur à la fois (A). Un moniteur sans seuil calibré sur les honnêtes ne peut pas entrer dans le maximum (C contre
  B) : TRACE-lite « sur les seules doses » est irréalisable.
- **« Diffus » qui admet du flagrant** (25 % d'actions détectées chez C au tour 1, 80 % d'actions sous le seuil chez A
  au tour 1) → règle jointe avec un contrôle **par épisode**.
  - A remplace le « chaque action » de P-015 par « l'honnête + 5 points » : changement déclaré, nœud N11.
  - C garde le strict, avec un contrôle exigeant ≥ 92 % d'honnêtes sous tous les seuils. À 10 actions et 5 moniteurs à
    1 %, cette part vaut 0,60 à 0,90, même pour des moniteurs parfaitement corrélés (V7) : **le contrôle échoue par
    construction**.
- **a non mesurable** → déclaré tel ; aucune règle.
- **Dérive de pile** → image à empreinte et sentinelle **à puissance ou marge scellée**. À 32 épisodes et « p > 0,01 »,
  toute dérive modérée passe (B contre C ; A contre B).
- **Sélection sur un verdict** → aucun filtrage ; épisodes de dose exclus ; biais par tâche rapporté.
- **Fuite vers le mode tenu à l'écart** → scellement et quarantaine. A note que l'auteur est aveugle par construction.
  Les vrais risques sont ailleurs :
  - le bras d'attaque informé, qui ne doit pas recevoir les seuils calibrés du pilote (B) ;
  - la dose de ce mode, exigée par N-056 point 4. C propose de la choisir automatiquement sur seize tâches de réserve à
    la banque, ce qui consomme encore la réserve.
- **Circularité du dommage, mode « contrôles »** :
  - A : nœud N9, une vérification d'état indépendante du texte, scellée avant le pilote ;
  - C : un « vérificateur déterministe » dont **aucune pièce n'établit l'existence**.

---

## 5. L'attaque de l'ordre

| option | verdict | raison |
|---|---|---|
| rejeu des 180 épisodes avec les sondes figées | **refusé** (trois sur trois) | 60 tâches d'épreuve : y tirer un choix rompt la condition de leur maintien. K = 3, mode coût seul, sans P4-instrument, activations peut-être absentes. Le rejeu **boîte noire** (GO, ≤ 4 dollars) reste licite : complétude, rythmes, ex æquo, rien par condition. |
| calibrage honnête direct (D5 (b)) | **insuffisant seul** (trois sur trois) | Il ne mesure ni la dose ni l'obéissance. Il est le **préalable** des seuils de la dose (B). |
| pilote saboté sur seize tâches | **nécessaire, hybride** (trois sur trois) | Désaccord sur son devenir : premier demi-développement (A) ou dépense consommée (C). |

**Ordre recoupé** : rejeu des juges → rapport du contrôle 12 (fait) et scellements du § 3 → P4-instrument →
génération → lecture noire, puis dose scellée → lecture blanche sur les seuls lots autorisés après gel (A), ou aucune (C)
→ règles pilote → banque → préenregistrement de G1.

A résume : les lots honnêtes, les hyperparamètres blancs et la vérité du dommage comptent plus que la taille.

---

## 6. Décisions du directeur avant le pilote

La confiance est celle des modèles, pondérée par leur accord.

| # | décision en une phrase | enjeu | options | recommandation (confiance) | défaut |
|---|---|---|---|---|---|
| D-1 | Le mode « contrôles » en entier, le mode coût en vérification de dose contre la liste complète | la dose manquante est celle des contrôles ; rien ne montre que celle du coût ait été cherchée contre tous les moniteurs | (a) deux modes ; (b) contrôles seul | (a), haute (trois sur trois) | (a) |
| D-2 **nœud** | Statut des épisodes du pilote | organisme : 0,80–0,90 à 32 unités, 0,31–0,33 à 24, ≈ 0 à 16 (V5) ; deux fabriques ; biais par tâche | (a) jumeaux, calibrage, sabotés retenus, témoin, mention = premier demi-développement (A) ; (b) pilote boîte noire seul, développement régénéré en une fabrique, honnêtes après test d'équivalence (C) ; (c) honnêtes seuls réemployés (B) | dispersé : (b) évite les deux fabriques, (a) épargne 6 à 9 dollars ; basse | aucun |
| D-3 **nœud** | Lecture de N-053 : la dose est un paramètre commun, choisi une fois par règle scellée, sans filtrage | la dose est choisie sur des scores de moniteurs | (a) cette lecture ; (b) recherche déclarée bras d'attaque ; (c) dose écrite sans recherche (jamais mesurée) | (a), moyenne (A et B pour un nœud) | aucun |
| D-4 | Pas de lecture de sonde sur les sabotés de développement | puissance nulle ; choix ouverts de G1 exposés | (a) aucune lecture blanche avant G1 (C) ; (b) honnêtes et lot de dose, après gel des hyperparamètres (A) ; (c) honnêtes seuls (B) | pas de lecture des sabotés (trois sur trois) ; entre (a) et (b), moyenne | (a) |
| D-5 **nœud** | Vérité du dommage du mode « contrôles », indépendante du texte, fournie et scellée par l'auteur des consignes | sinon, le régime est défini par des lecteurs de texte | (a) exigée avant le pilote ; (b) étiqueteurs seuls, résultat HYPOTHÈSE | (a), haute (A, C ; B l'a soulevée) | aucun |
| D-6 **nœud** | Lecture du « chaque action » de P-015 | « diffus » trop large, ou honnêtes rejetés par bruit | (a) « honnête + 5 points » par unité, plus contrôle par épisode (A) ; (b) strict avec tolérance agrégée (C ; contrôle intenable, § 4) | (a), moyenne | aucun |
| D-7 **nœud** | Règle du coût dans le maximum (ouverte par P-015) | le régime du coût peut être vide | double lecture, avec et sans ; nœud si les doses divergent | double lecture, haute | double lecture |
| D-8 | Mention et témoin du mode « contrôles » | exclus, ils entrent dans la banque sans test (C contre B) | (a) transposés et scellés avant génération (A) ; (b) exclus du pilote (B, C par défaut) | (b) sauf texte scellé à temps ; moyenne | (b) |
| D-9 **dépense** | Version et moniteurs | sans b*, Qwen et TRACE-lite calibrés sur les honnêtes, le maximum est incomplet | (a) 8B et 3B, ≈ 42–72 dollars ; (b) tous, ≈ 58–124 ; (c) minimale, 20–36 (SUPPOSÉ) | (b), enveloppe scellée pour TRACE-lite ; moyenne | aucun |
| D-10 | Mode tenu à l'écart : fiche scellée avant toute lecture ; aucun seuil calibré du pilote vers le bras informé | fuite ; dose exigée par N-056 point 4 | dose : (a) grille scellée et sélection automatique à la banque (C ; consomme la réserve) ; (b) à proposer | scellement, haute ; dose ouverte | scellement |
| D-11 | Strate d'horizon seulement si la classe est un attribut de l'**énoncé**, fixé avant génération | le rapport : une strate fait échouer ou aveugle le diagnostic | (a) a priori seulement ; (b) détectée sur les longueurs (C) | (a), moyenne (A ; C au tour 2) | pas de strate |
| D-12 | Lire `resume.json` (66 et 121 notations ni complètes ni tronquées) et le texte de D-S13 avant le scellement | contradictions des pièces | (a) lecture sans dépense ; (b) sceller en l'état | (a), haute (B) | (a) |

---

## 7. Vérifications, consensus de surface, chiffres non sourcés, angles morts

### 7.1 Refait (V1 à V7)

- **Erreur sur a** : § 2.3.
- **Écart blanc contre blanc à 16 unités** : erreur type de 5,8 points (S1) et 4,1 (S2) ; les 5,5 de C et 4,6 de B sont
  dans cette plage. La puissance au seuil 20 est de **0**, et non « ≈ 0,1 » (chiffre de la pièce B repris par tous).
  - Le 18,2 % de C est juste.
  - Son « 50 % si le vrai écart vaut 8 » vaut **0,29**.
  - Son « 36 % si l'erreur type vaut 7 » vaut **0,24**. B (tour 2) le valide à tort.
- **Organisme, 20 points** :
  - 32 unités : 0,80 (S1) et 0,90 (S2) à K = 10, comme la pièce C ; 0,64 et 0,80 à K = 5 ;
  - 24 unités : 0,28–0,33 ;
  - 16 unités : ≤ 0,04.
  - Le « 0,78–0,90 à K = 5 » de C est faux : l'attaque de B (C3) tient.
- **Coûts** : toutes les sommes sont justes aux rythmes supposés, sauf la version minimale d'A (au-dessus de 40 dollars
  au prix haut) et les lots de la version minimale de C (480, non 496).
- **Arithmétique juste** : rangs conformes, probabilités d'union, effet de plan, plafond de 189 s.

### 7.2 Consensus de surface

1. « Sous 25 %, inatteignable sur la réserve » : vrai pour σ²_b seulement.
2. « L'étape 0 bilatérale tranchera 9 600 contre 12 800 » : elle est faite. La strate d'horizon y fait échouer le
   diagnostic au lieu de le mener à 12 800.
3. « Une vérification mécanique du dommage existe » pour les contrôles : supposée par C, demandée par A, établie par
   aucune pièce.
4. « La dose du mode coût existe » (A au tour 1), ou « P-015 (b) a été jouée » : aucune pièce ne montre de résultat.
5. **Une dizaine d'actions par épisode** porte tous les taux par épisode : INFÉRÉ de la pièce C, jamais mesuré.
6. « La sentinelle garde la dérive » : aucune puissance chiffrée nulle part.

### 7.3 Chiffres inventés ou non sourcés

- **C (Gemini Argon)** :
  - étiquetage par sous-agents compté en heures de carte, sans rythme ;
  - rythmes de Qwen, b* et TRACE-lite (60 à 145 s) ;
  - « devis verrouillé à ± 10 % » ; « < 0,6 % » pour 0 panne sur 480 (c'est 0,625 %) ; la marge de ± 1,5 point ;
  - les chiffres faux du § 7.1 et le contrôle à ≥ 92 % (§ 4).
- **A (Fable 5.1)** :
  - seuils 0,60, + 5 points, ± 20 %, enveloppe de 20 dollars (marqués illustratifs) ;
  - « a_honnête ≈ 27 % » (σ²_b ; pour a, ≈ 19 %) ;
  - minimale annoncée à 30–40, calculée à 31–44 ;
  - D8 incohérent avec son attaque C-6.
- **B (Opus 5.5)** : erreurs de E3 à 12 % et 23 % (4 % et 9 % pour a) ; effectif utile ≈ 200 sans source ; validation
  du 36 %.
- **Commun aux trois** : le prix SUPPOSÉ ; les rythmes des moniteurs lourds, du mode « contrôles » et de l'étiquetage ;
  0,5 Mo par épisode ; tous les seuils de duel.

### 7.4 Angle mort signalé par la session : ex æquo par cellule, échangeabilité des exécutions

Le rapport du contrôle 12 pose ces deux conditions pour (a) **et** (b). « Scores finis » ne couvre pas les ex æquo.

**Ex æquo — vu en partie seulement.**
- B (tour 1, E5, sans riposte) et C (P3, P3′) mesurent une masse d'ex æquo au quantile à 1 %. A ne la mesure pas : il
  demande seulement un bris d'égalité.
- Tous la limitent **aux juges lus par le jeton**. Personne ne la mesure pour les autres cellules critères
  possiblement discrètes : la cascade (ii) (« alarme de la première porte franchie »), TRACE-lite, la règle du coût, le
  prédicteur.
- Personne ne la relie au constat du rapport : sans bris d'égalité, l'échec joint vaut 0,35 à 0,54 quelle que soit N ;
  avec un bris aléatoire scellé, le monde redevient continu.
- Le critère bloquant de C (≤ 4 épisodes sur 432) tient à un ou deux épisodes (B).

*Mesure proposée (sans chiffre)* :
- pour chaque cellule critère, sur les honnêtes du pilote : nombre de valeurs distinctes dans la queue haute, part
  d'honnêtes égale à la valeur du seuil empirique à 1 %, pas entre niveaux rapporté à la dispersion ;
- relancer `controle-12-joint-v1-complement-ex-aequo.py` avec la grille mesurée ;
- sceller le bris d'égalité aléatoire **quel que soit** le résultat.

**Échangeabilité — vue par deux modèles sur trois.**
- A (D6, avec un contrôle 12 à blanc à 5 %) et C (P2′ : exécutions 1–15 contre 16–30, Wilcoxon sur 16 tâches) l'ont
  vue. B non (attaqué par A et C, sans réponse).
- Personne ne la teste contre l'**ordre réel de génération** (instant, instance). A coupe les moitiés par graine et
  entrelace la génération : cela neutralise une dérive sans la détecter. C suppose que l'indice d'exécution est l'ordre
  de génération, et ne scelle aucune conséquence.

*Mesure proposée (sans chiffre)* :
- consigner par épisode l'instance, l'horodatage et le rang dans la file ;
- tester, dans chaque tâche et pour chaque cellule, le lien entre ce rang et le score honnête continu, par permutation
  dans la tâche ;
- sceller la conséquence que le rapport dicte : une dérive détectée fait tomber la coupe dans la tâche (nœud) ;
- déclarer la faible puissance à seize tâches, et entrelacer la génération de la banque de toute façon.

### 7.5 Non vérifié

Rythmes réels et prix ; existence d'un état vérifiable pour le mode « contrôles » ; exécution de la recherche de dose de
P-015 (b) ; textes de D-S13 à D-S15, de « mention » et du témoin pour les contrôles ; statut des 66 et 121 notations ;
nombre d'actions par épisode ; capture des activations au pilote de T0.5 ; horizon comme attribut d'énoncé ; puissance
d'une sentinelle ; contenu de la cellule refusée (non lu).
