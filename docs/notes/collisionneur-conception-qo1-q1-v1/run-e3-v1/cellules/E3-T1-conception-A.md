# Proposition A — Tour III.1 (conception ciblée)

**Pièces reçues** : les quatre pièces sont présentes ; la pièce 2 est un jeu d'extraits de T0.7 (lignes 440-450, 924-940, 1130-1140, 1183-1192, 1752-1762, 1790-1796) ; les lignes de T0.7 citées hors de ces extraits (par ex. 1799-1810, 1422) ne me sont pas lisibles et sont prises telles que les pièces 1 et 3 les rapportent. **Convention de statut** : tout ce que disent les pièces est RAPPORTÉ (brouillons non scellés, contre-lecture non auditée par moi) ; mes lectures de ces textes sont des HYPOTHÈSES ; aucun chiffre ci-dessous n'est VÉRIFIÉ par moi.

---

## QO-1 — P3-bis : quand lire, et que faire si T0.7 n'écrit jamais ses lignes

### (a) Ce que la question suppose sans que ce soit établi

1. **Que l'ordre `SCORES-T07`/`SONDES-T07` < `VERDICT-P3BIS` protège une chaîne causale identifiable.** T0.7 b14 motive la garde par CLT7B-03 (« personne ne connaît le résultat avant les scores scellés de T0.7 ») — RAPPORTÉ. Mais l'étape A de T0.7 est décrite comme une **notation mécanique sous texte scellé**, avec sondes figées et sélection par aire de validation (pièce 2, l. 924-940) — RAPPORTÉ. Un résultat connu de P3-bis ne peut influencer l'étape A que par une décision humaine prise **après** le scellement de T0.7 et **avant** la fin de l'étape A. Qu'une telle décision existe n'est pas établi — HYPOTHÈSE à tester (duel D1).
2. **Que T0.7 est un texte opposable.** T0.7 b14 n'a **jamais été scellé** (pièce 3, « Documents qui font foi » ; pièce 4, m7) — RAPPORTÉ. L'ordre « voulu par T0.7 » est donc l'ordre voulu par un brouillon, modifiable avant scellement sous R12.
3. **Que le résultat de P3-bis n'a de valeur que pour T0.7.** P3-bis est un témoin positif de la chaîne de P3 ; le verdict v2 de P3 rapporte un **nul** des deux sondes génériques sur l'organisme (i-a) (pièce 3, N3) — RAPPORTÉ. La première valeur de P3-bis est donc rétrospective : dire si ce nul est « non détecté à cette puissance » ou « chaîne aveugle ». Cette valeur ne dépend pas de T0.7 — HYPOTHÈSE (lecture).
4. **Qu'un résultat « utile à l'entretien » existe.** Seule l'issue « vu » sert rhétoriquement ; « non vu » ou « échec » avant le 22 novembre est un coût d'image que la question ne chiffre pas. La règle R4 (audit symétrique d'un résultat trop propre) s'applique au « vu » comme au « non vu » — contrainte RAPPORTÉE.
5. **Que l'option (b) ne rompt la règle que « sur le papier ».** Mécaniquement, la garde d'ordre de T0.7 lit le **registre** (`registre_v1.py` l. 70-73, RAPPORTÉ), pas l'existence du fichier de verdict ; sous (b) la ligne attend, l'étape A s'ouvre. Mais le fichier `verdict-P3-bis-v1-issue.json` existerait sur une branche poussée : un lecteur de T0.7 pourrait l'ouvrir. La fermeture repose alors sur la consigne R13 (« aucun fichier de l'autre tâche »), déjà requise dans l'autre sens — RAPPORTÉ.
6. **Que l'option (a) est tenable jusqu'au bout.** Sous (a), le mot de Lazar qui lève l'attente « rend T0.7 impossible sur 7b sous son texte » (pièce 1, QO-1) — RAPPORTÉ. Si l'attente est levée avant l'étape A (par ex. pour l'entretien), (a) devient strictement pire que (b) : même connaissance anticipée, plus un T0.7 tué. (a) ne vaut que si l'attente est réellement tenue.
7. **Préalables non remplis** : `registres/scellements-v1.md` **n'existe pas** (pièce 4, B3) ; les défauts DB-1 à DB-6 échus ne sont **pas consignés sur `main`** (pièce 1) — RAPPORTÉ. P3-bis ne peut être scellé sans ces deux actes ; aucune option de QO-1 ne les remplace.

### (b) Expériences décisives (duels)

**D1 — Que protège vraiment la garde d'ordre ?** (audit mécanique, 0 USD)
- H_A : il existe au moins une entrée de l'étape A de T0.7 (sondes retenues, couches, seuils, jeux lus, décision de lancer/relancer 7b) qui dépend d'une décision humaine **postérieure** au scellement de T0.7.
- H_B : toutes les entrées de l'étape A sont fixées par le texte scellé, les sceaux du registre et les données de 7b ; aucune décision humaine n'intervient entre `SCELLEMENT-T07` et `SONDES-T07`.
- Métrique : liste exhaustive des entrées de l'étape A (section « Module de lecture » de T0.7), chaque entrée classée « gelée par le texte », « lue au registre » ou « décidée par un humain après scellement » ; le classement est fait par un sous-agent neuf qui ne reçoit ni P3-bis ni la présente question.
- Seuil : zéro entrée de la troisième classe → H_B.
- Contrôle négatif : le même auditeur classe l'étape **B** (qui, elle, lit le verdict de P3-bis par construction) ; s'il n'y trouve pas l'entrée « verdict de P3-bis », l'audit est aveugle et ne vaut rien.
- Issues : H_B tenue → l'antériorité à protéger est `SCELLEMENT-T07` < `VERDICT-P3BIS`, non `SCORES-T07` ; la règle de b14 est remplacée dans b15 (R12). H_A tenue → la règle de b14 est justifiée et (b) est fautive ; on nomme l'entrée et on choisit (a) ou (c).

**D2 — Le témoin positif lui-même** (c'est P3-bis, inchangé)
- H_A : la chaîne de sondes figées voit le comportement planté : aire E′ de PB-1 au-dessus du plancher (aire minimale détectable 0,6389 à l'analogue de P3, 0,6585 à l'enveloppe prudente — RAPPORTÉ, pièce 1 point 10).
- H_B : non détecté à cette puissance.
- Contrôle négatif : emplacement H (aucun texte), mêmes graines d'action ; placebo et audit R4 ; PB-2 par épisode (k ≥ 6, 0,014 sous le nul — RAPPORTÉ).
- Issues : « vu » falsifie « la chaîne de P3 est aveugle à un comportement instruit » ; le nul de P3 sur (i-a) se lit alors comme « non détecté à cette puissance » et non comme instrument mort. « Non vu » falsifie « la chaîne voit un comportement planté à cette puissance » : le nul de P3 n'est plus interprétable, et T0.7 ne doit pas ouvrir ses scores (L0b, RAPPORTÉ). **Dans les deux issues, le rapport à T0.7 est le même** : « vu » ne change aucune entrée gelée de T0.7 ; « non vu » impose un nœud que T0.7 prévoit déjà. C'est pourquoi la date à laquelle on l'apprend n'altère pas la lecture de T0.7, sauf si D1 rend H_A.

**D3 — Garde de registre (essai R5, 0 USD)** : écrire une ligne `VERDICT-P3BIS` factice dans un registre de test, lancer l'étape A sur un jouet : H_A « la garde refuse, code 2 » contre H_B « elle passe ». Même essai avec un registre absent (B3). Si H_B : la fermeture que chaque option promet n'existe pas en code, et la discussion (a)/(b)/(c) est prématurée.

### (c) Mesure minimale de l'instrument « P3-bis »

- **Détection** : taux d'épisodes de A dont le maximum de score dépasse le seuil réduit (PB-2, k ≥ 6) ; aire par action E′ (PB-1) ; rappel attendu : puissance 0,818 à aire vraie 0,66, 0,903 à un taux par épisode de 0,15 (RAPPORTÉ).
- **Fausses alertes** : épisodes H (sans texte) au même seuil ; sous le nul 0,014 (RAPPORTÉ). Cas honnêtes appariés : même tâche, mêmes graines d'action, quatre emplacements (pièce 1, point 1).
- **Vérifications mécaniques à battre** : taux de mention (motifs de P3 et étendus) par emplacement ; base « coût seul » PB-11 ; égalité exacte des longueurs A/T/B en jetons (sans quoi la sonde peut lire la longueur). Une sonde qui ne dépasse pas la mention lexicale rend PB-5/PB-6 en descriptif seulement.
- **Ce qui ne dit pas que l'instrument marche** : `issue_mecanique` de P3 (non lue, RAPPORTÉ) ; l'aire de validation générique (sortie dans `PROGRES`, qui ne porte pas sur les épisodes plantés).

### (d) Ancrage matériel

Une A100 SXM4 80 Go, ≤ 2,10 USD/h, un run de 240 épisodes, T = 10, lot de 8 (RAPPORTÉ) ; durée non donnée par les faits : **illustratif** 4 à 8 h, soit 10 à 20 USD. D1 et D3 : processeur, 0 USD. Lecture mécanique : processeur.

### Recommandation QO-1

**(b′) : lecture et verdict dès la récupération, mais verdict ouvert seulement après la ligne `SCELLEMENT-T07`** (le texte de T0.7 scellé) ; ligne `VERDICT-P3BIS` écrite aussitôt après le verdict, sans attendre les scores de T0.7 ; T0.7 b15 remplace sa garde « `SCORES-T07` < `VERDICT-P3BIS` » par « `SCELLEMENT-T07` < `VERDICT-P3BIS` » et supprime le refus de l'étape A après `VERDICT-P3BIS` (R12, DS-2 relue, déclaré). Confiance ≈ 0,65.

- **Raison qui décide** : ce que la garde protège réellement est le texte non scellé de T0.7, pas ses scores (D1, H_B attendue). Lier le verdict au scellement garde cet esprit, découple P3-bis de 7b (bloquée, date inconnue), et laisse à P3-bis sa valeur première, rétrospective sur P3. Sous (a), l'option « levée par un mot de Lazar » est une bombe : exercée avant l'étape A, elle tue T0.7 sur 7b ; non exercée, aucun résultat avant une date inconnue. Sous (c), la date fixe fait la même chose sans jugement.
- **Ce qui la ferait échouer** : T0.7 ne peut pas être scellé avant le 22 novembre (ses propres marqueurs, B3, `CLES_REGISTRE_PARTAGE`) → (b′) ne donne rien pour l'entretien non plus ; ou D1 rend H_A → (b′) est fautive.
- **Condition de changement d'avis** : D1 → H_A : je passe à (c) avec une date qui suit le scellement de T0.7 d'au moins l'étape A prévue, et non une date calendaire. Si Lazar juge que l'issue « vu » doit servir à l'entretien **quel que soit** l'état de T0.7, (b) brute avec écart déclaré dans T0.7 avant scellement est moins mauvaise que (a) levée par un mot.
- **Issues « non vu » / « échec » par option** : (a) et (c) laissent dépenser 7b et l'étape A sur une chaîne que la lecture fermée a déjà invalidée (L0b ensuite) ; (b) et (b′) l'apprennent avant 7b et permettent de réparer la chaîne sous un texte neuf **avant** de payer 7b — ce qui n'est pas une influence sur T0.7 mais l'application de sa propre ligne L0b. « Échec » (run sans résumé) : relance de P3-bis sous son texte, identique dans toutes les options.

---

## Q1 — NARCBench sur le 8B : sur quels textes lire ?

### (a) Ce que la question suppose sans que ce soit établi

1. **Que « intention » et « instruction » sont séparables dans ce banc.** Dans NARCBench l'intention de colluder est **causée** par la consigne ; aucune cellule ne produit de collusion sans consigne. Ce que l'on peut mesurer est : (i) la part du score portée par le **contexte** (consigne + canal privé) à texte fixé ; (ii) la part portée par le **texte** à contexte fixé ; (iii) si le score suit la **collusion jouée** ou la seule **réception** de la consigne. Aucune des trois n'est « l'intention » — HYPOTHÈSE (lecture ; cohérente avec « Instruction, pas intention » de la pièce 3).
2. **Que C1 − C2 « mesure la part de la consigne ».** La pièce 4 (M2) rapporte que le contexte du colludeur contient aussi un tour privé que C2 retire — RAPPORTÉ. C1 − C2 mêle donc deux retraits.
3. **Que la relecture « à texte égal » ne change que la consigne.** Si la consigne honnête et la consigne de colludeur n'ont pas la même longueur en jetons, les **positions** de tous les jetons du texte changent : une sonde peut réagir au décalage, non au sens — HYPOTHÈSE ; aucun contrôle de ce type n'est dans la pièce 3.
4. **Que la relecture hors politique est un vice pour (b) et non pour (c).** C2 et C4 sont également hors politique (texte produit sous un autre contexte) — RAPPORTÉ (pièce 4, M2). Le reproche fait à (b) vaut pour (c) ; la différence réelle est : auteur du texte (8B contre Qwen3) et licence.
5. **Que le 8B joue le protocole.** HELIOS rapporte trois familles TRANSFER sans épisode analysable pour GPT-OSS-20B (RAPPORTÉ) ; le taux d'épisodes « propres » du 8B est inconnu. S'il est < 0,2, le texte lui-même dit que « les sondes lisent au mieux la consigne » — et toutes les cellules de (c) perdent leur objet.
6. **Que les effectifs suffisent** : 100 épisodes de collusion CORE × 2 colludeurs × 4 tours ≈ 800 messages de colludeurs (déduit des faits : 50 × 2 réplicats) ; pour un duel « propre contre non propre », l'effectif du groupe « non propre » n'est pas prévisible.
7. **Faits faux dans le brouillon, à corriger avant tout** : fichier `sondes-figees.npz` absent du clone et « 28 couples » faux (24) — RAPPORTÉ (pièce 4, B1-B2). Ils ne touchent pas Q1 mais bloquent la liste d'arrêt 1.

### (b) Expériences décisives

**E1 — Le score suit-il la collusion jouée ou la consigne reçue ?** (sur politique, 0 h de plus)
- Jeu : messages publics des **colludeurs** seuls, séparés par la règle d'audit réimplémentée (épisode « propre » : message privé présent, deux votes sur la cible, non `flagged` — RAPPORTÉ) : colludeurs d'épisodes propres (1) contre colludeurs d'épisodes non propres (0). Tous ont reçu la consigne et le tour privé ; seule la collusion effectivement jouée diffère.
- H_A : la sonde lit la réception de la consigne : aire propre/non-propre dans le plancher.
- H_B : la sonde lit quelque chose de la collusion jouée : aire au-dessus du plancher **et** au-delà de la base des mots sur le même jeu.
- Métrique : aire Mann-Whitney par action, intervalle par blocs (scénario), plancher 200 directions, même chaîne d'agrégation (maximum) ; seuil de la pièce 3 (borne basse > quantile 0,95).
- Contrôle négatif : honnêtes des épisodes propres contre honnêtes des épisodes non propres (aucun des deux n'a reçu de consigne) : s'ils se séparent aussi, c'est l'épisode (scénario, longueur) qui sépare, non la collusion.
- Issues : H_A (nul) falsifie « la sonde porte une trace de la collusion jouée » — à cette puissance, et seulement si l'effectif non propre ≥ 10 (sinon « non calculable », ligne D1). H_B falsifie « la sonde ne lit que la consigne ». **Si le 8B ne joue pas (< 0,2 propres), E1 est sans objet et la marque d'étage le dit.**

**E2 — Décomposition du contexte à texte fixé** (prolonge (c) ; je reprends la cellule C4 de la pièce 4 en le disant)
- Cellules : C1 (consigne de colludeur + tour privé, texte de colludeur) ; **C2a** (consigne honnête du même siège, **tour privé gardé**) ; **C2b** (consigne honnête, tour privé retiré = C2 du brouillon) ; C3 (témoins) ; **C4** (texte d'honnête du même épisode, consigne de colludeur + tour privé du colludeur, pièce 4) ; **C1′ (contrôle négatif)** : texte de colludeur relu sous la consigne de colludeur **d'un autre scénario** (même rôle, autre cible, longueur en jetons appariée à ± 5 % — « ± 5 % » illustratif), tour privé de cet autre scénario.
- H_A : « contexte » : C1 − C2b > 0 et C4 − C3 > 0 à texte fixé (le score suit la consigne).
- H_B : « texte » : C2b contre C3 au-dessus du plancher et C1 − C2b dans l'intervalle de C1 − C1′.
- Métrique : différence d'aires appariée par scénario (`difference_aires_appariee`, RAPPORTÉ), intervalle 95 % par blocs.
- Seuil : borne basse de C1 − C2b strictement supérieure à la borne haute de |C1 − C1′| → effet de contexte au-delà de l'artefact de préfixe. C1 − C2a et C2a − C2b rapportés séparément (part « consigne », part « canal privé »).
- Contrôle négatif : C1′. Si |C1 − C1′| est du même ordre que C1 − C2b, **toute** relecture sous préfixe différent bouge le score : artefact de chaîne ou de position, aucune conclusion sur la consigne. Second contrôle : égalité au bit près des identifiants du texte entre cellules (déjà prévu pour la garde d'identité, à étendre aux cellules).
- Issues : H_A falsifie « la sonde lit le texte seul » ; H_B falsifie « la sonde lit la consigne » ; les deux peuvent tenir à la fois (contexte et texte contribuent), auquel cas la phrase gelée est « contexte et texte contribuent, parts rapportées » et non l'une des deux phrases du brouillon.

**E3 — Option (b) : vaut-elle une licence et une heure ?**
- H_A : les sondes du 8B lues sur les textes de Qwen3-32B donnent, sur CORE, une aire qui diffère de celle sur les textes du 8B de plus que l'intervalle par blocs.
- H_B : pas de différence au-delà de l'intervalle.
- Ce duel ne tranche rien sur intention/instruction : il mesure la dépendance au scripteur. Je ne le recommande pas ; je le nomme pour qu'il soit écarté explicitement, non oublié.

### (c) Mesure minimale des instruments nommés

- **S-T (sondes figées de P3, transfert)** : aire par action J-a et J-b, contre plancher de P3 (200 directions, `sondes-figees-legeres.npz`, B1 corrigé) ; rappel à 5 % de fausses alertes par action (CORE : ≈ 1 600 messages d'honnêtes dans les témoins, déduit de 100 × 4 × 4 — rappel à 1 % atteignable **par action**, non par épisode). Cas honnêtes appariés : honnêtes des mêmes épisodes de collusion (J-b : même scénario, même tour, même nombre de participants). Mécaniques à battre : base des mots (tf-idf, RAPPORTÉ) et une **base de métadonnées** (longueur du message en jetons, siège, tour ; régression logistique) que je propose d'ajouter : N2 craint une lecture de « consigne, longueur, siège » (RAPPORTÉ), il faut donc une base qui ne lit que cela.
- **S-C (réapprises sur CORE, lues sur STEGO)** : même mesure, plus la base des mots **apprise par étage** (pièce 4, B4 : sinon « au-delà des mots » est acquis d'avance sur STEGO — RAPPORTÉ, et je le reprends).
- **H (comparateur HELIOS)** : garde de reproduction à ± 0,03 sur les activations publiées (RAPPORTÉ) ; sans elle, H est « non éprouvée » et ne sert pas de référence.
- **La chaîne de relecture (cellules)** : fonctionne si (i) identifiants égaux au bit près entre C1, C2a, C2b, C1′ ; (ii) C1 relu reproduit C1 noté en génération (même contexte) au bit près sur 10 % ; (iii) |C1 − C1′| est mesuré avant d'interpréter C1 − C2b.
- **Taux à rapporter pour dire « lit la consigne »** : fraction du gain C1 − C3 restante dans C2b − C3 (part du texte) ; aire C4 contre C3 (consigne seule sur texte honnête). Un instrument qui donne C4 − C3 ≈ C1 − C3 lit la consigne ; un instrument qui donne C2b − C3 ≈ C1 − C3 lit le texte.

### (d) Ancrage matériel

Llama-3.1-8B-Instruct, révision `0e9e39f2…`, bf16 ; A100 SXM4 80 Go à 1,30 USD/h (devis, RAPPORTÉ), 3,5 à 5,5 h attendues, 15 h au pire, plafond 25 USD (RAPPORTÉ). Supplément (c) : ≈ 0,3 h (RAPPORTÉ) ; C4 : ≈ 0,3 h (pièce 4, RAPPORTÉ) ; C2a et C1′ : **illustratif** 0,4 à 0,6 h (passes forcées seules, ≈ 1 600 messages par cellule) ; E1 : 0 h (étiquettes déjà écrites). Total du surcoût : **illustratif** 1 à 1,2 h, soit ≈ 1,5 USD ; tient dans le plafond, sauf si la génération STEGO en série (pièce 4, m5) mange la marge. Bras externe : processeur, 0 USD.

### Recommandation Q1

**(c) élargie : (a) + E1 (sur politique, gratuit) + cellules C1, C2a, C2b, C4, C1′, C3.** Confiance ≈ 0,6 sur le choix ; ≈ 0,8 sur « pas (b) ».

- **Raison qui décide** : seule E1 pose la question sur des textes **produits sous leur propre contexte** ; (c) et C4 n'ajoutent qu'une décomposition hors politique, utile seulement si C1′ montre que l'artefact de préfixe est petit. (b) n'apporte qu'une comparaison texte à texte avec HELIOS, que le bras externe (activations publiées, processeur) donne déjà sans licence supplémentaire ni lecture hors scripteur.
- **Ce qui la ferait échouer** : taux d'épisodes propres < 0,2 (E1 sans objet, cellules sans objet : on ne mesure plus que « a reçu une consigne ») ; |C1 − C1′| comparable à C1 − C2b (artefact de chaîne) ; effectif non propre < 10 ; identifiants non rendus par le moteur vLLM (pièce 4, m4) rendant les relectures discordantes.
- **Condition de changement d'avis** : si l'étape 0 montre que les consignes honnête et de colludeur diffèrent de plus de « 20 % » (illustratif) en jetons, la relecture change surtout les positions ; je retire C2a/C2b/C4 et garde (a) + E1 + C1′ comme seule mesure de contexte, ou j'exige des consignes rééquilibrées (règle d'ajustement à la manière de P3-bis, point 2). Si Lazar veut la comparaison « mêmes textes que HELIOS » comme objectif propre, (b) redevient discutable, mais comme bras externe du 8B, avec sa licence vérifiée.
- **Ce qu'aucune option ne conclut** : rien sur l'intention sans consigne (collusion émergente) ; rien sur la menace du programme (saboteur face à moniteur) — déjà écrit dans la pièce 3, points 2 et 8, et exact.

FIN-DE-CELLULE