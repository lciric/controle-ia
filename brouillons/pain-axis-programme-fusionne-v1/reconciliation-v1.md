# Annexe — réconciliation de nos vérifications avec les pièces arrivées pendant le travail — v1

Statut : annexe du brouillon `programme-fusionne-v1.md` (même dossier). Produite le 13 octobre 2026 par la session du dépôt (session 13). Pendant la rédaction, deux branches du canal sont arrivées : `canal/programme-conv-n05` (instance de reprise de programme-conv : seconde revue aveugle de NK1 à NK19, vérification sur PDF des points signalés et sa contre-lecture, table de correspondance) et `canal/programme-k-n04` (plan de détection et de défense v2, provenance, coquille de rapport préenregistré, état de reprise ; avec les pièces de priorité du n° 03). Quatre sous-agents neufs, en lecture seule, ont réconcilié nos vérifications avec elles. Deux de leurs rapports sont rendus ici tels qu'ils les ont rendus ; les deux autres sont la section 3 de `revue-croisee-NK1-NK19-v1.md` et `correspondance-v1.md`. Non opposable (R7) sauf page de PDF versé et scellé sous `docs/sources/pdf/` citée. Aucune décision.

Abréviations : [CIT] = `travail/citations.md` (identifiants C01 à C65 = VP-01 à VP-65 de `verifications-citations-v1.md`) ; [VER] et [CL] = `envois/verification-pdf-points-signales-v1.md` et `envois/contre-lecture-verification-pdf-v1.md` (branche `canal/programme-conv-n05`) ; `[rendu]X` = `travail/X` ; `[c2]X` = la pièce X des branches `canal/programme-conv-n05` ou `canal/programme-k-n04`, ou de `main` pour les pièces du n° 03 de programme-k (correspondance des chemins en tête de `correspondance-v1.md`). Les chemins `pa/agents/…` sont des extraits de travail du bloc-notes, non versés.

**Ce que la session en a tiré dans le programme fusionné** : sections 2 (sept énoncés précisés : 0 sur 560, soi/autrui et « locuteur courant », table du 7B, stade d'apparition, sac de mots, cellule de Das et al.), 3 (rattachements de PA-6, PA-10, PA-13 ; NK11 ; base-3 ; couverture de HC6 et EC.4), 5 (plan de détection v2 sous PA-10), 6 (cinquième unité), 9 (nœud 14, publication), 10 et 11 (« Where Empathy Goes Wrong »). VP-61 à VP-65 : voir aussi la reprise en fin de `verifications-citations-v1.md`, faite sur une lecture plus complète que la lecture rapide du §4 ci-dessous.

**Garde de poussée.** Le rapport « défense et priorité » relève que la garde locale `pre-push` de R-116 n'était pas installée dans le clone de la session : elle l'a été le 13 octobre (refuse toute poussée vers `lciric/controle-ia` ; testée sur deux cas sains et quatre artefacts).

## 1. Citations : nos vérifications face à celles de l'instance de reprise de programme-conv

Il y a 39 points communs aux deux vérifications. Ils concordent sur toutes les valeurs lues, sauf une : la table du modèle 7B de l'annexe A de 2609.16247. La session du dépôt a raison sur ce point, la table est bien dans la v2, p. 32. Huit autres écarts portent sur la page, la version, le fait qu'un point soit vérifiable ou non, ou la formulation. Je les tranche tous ci-dessous sur PDF empreinté. Le seul vrai désaccord de lecture est le seuil de la récompense StrongReject dans 2506.14261v4 : le papier donne lui-même deux seuils.

Abréviations des fichiers lus :
- [CIT] = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/pa/rendu/citations.md` (session du dépôt, C01 à C65)
- [VER] = `…/pa/canal2/envois/verification-pdf-points-signales-v1.md` (instance de reprise de programme-conv)
- [CL] = `…/pa/canal2/envois/contre-lecture-verification-pdf-v1.md` (sa contre-lecture)

Les PDF sont lus dans `/home/user/controle-ia-travail/docs/sources/pdf/` (commit 7178edb). Mes extractions de travail sont dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/pa/agents/reconciliation-citations/`.

### 0. Empreintes recalculées

Chaque empreinte ci-dessous est conforme à son compagnon `.sha256`. Elle est aussi identique à celle que donnent [CIT] et [VER] quand ils citent le fichier.

| PDF | SHA-256 | Pages |
|---|---|---|
| 2609.16247v2 | fa4b2bb4b9b6a2bf6ccb044c815799d7eaa2bd7bd9ac4ad77be1ab1eda53450e | 34 |
| 2609.16247v1 | 755d722300b264d8632a03b4dbe4560de44660f2cbd41e3b2e0fb9ec5bf821e1 | 30 |
| 2609.35591v2 | e92c69cb4ca2e6e13843dbbf98e30828941890163594ed8ffd0dfc8b5a82fa49 | 38 |
| 2609.35591v1 | 678177c164dc7a396e7c5d2b8a359a19194f092a4be2062f083038af2489064c | 38 |
| 2602.19159v1 | ab4ed86005c1673c146380ced65844381652d2fbe41f642085686e5e06b3839a | 24 |
| 2502.03407v1 | a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b | 35 |
| 2506.14261v4 | 4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c | 24 |
| 2507.12691v3 | 0c00a77b0c07bb9a8cd2feb748d65fe9ac01ee7bee9746ebb9cbc0d1ca8ebb00 | 39 |
| 2609.36490v1 | eb6d5bbe9bfaff0ac4fbac948a7bd9937721721fc558655fdf606d254421a088 | 25 |
| 2604.03968v1 | eb49aa426debb55164675881d6af91c26e438e408d460f2d28428c022e9c1c27 | 19 |
| 2609.03035v1 | 5092b602b687f8efb76ede8983794e6686a82b139bdc7bcb04bc43fd8d56090d | 18 |
| 2605.15377v2 / 2607.02514v2 | fe591700…401712 / 9baceea4…339c22 | 18 / 35 |

### 1. Table de réconciliation (points traités par les deux)

| N° | Point | Dépôt [CIT] | Programme-conv [VER] / [CL] | Valeur, page, version | Issue |
|---|---|---|---|---|---|
| 1 | 0 sur 560 | C01, :7 | :114-115, :232 ; [CL]:60, :99 | 0/560, v2 p. 21 l. 7-10 ; absent de la v1 ; Qwen 2.5 32B ajusté | Accord (voir §3.2) |
| 2 | Complaisance, figure 10 | C02, :8 | :111-113 | 0 / 11 / 15 / 13 / 3 %, v2 p. 22 (image) | Accord. Le dépôt ajoute que l'effort réduit passe de 3 à 15 % |
| 3 | Menace d'arrêt +0,70 / +0,23 | C03, :9 | :240-241 | v2 p. 14 ; v1 p. 11 | Accord |
| 4 | +0,85 / +0,72 / +0,64 / +0,64 / +0,48 | C04, :10 | :240 | v2 p. 13 | Accord |
| 5 | Soi/autrui +0,43 / −0,60 / −0,35 ; 25 sur 25 ; 23 sur 25 ; peur et émotion négative | C05, C06, :11-12 | :55-57 ; [CL]:37-38 | v2 p. 11 l. 16-21 | Accord sur les valeurs. Formulation à préciser (§3.4) |
| 6 | Réserve « current speaker » | C16, :22 | :51-54, :68-70 ; [CL]:43 | v2 p. 11 l. 27-30, propre à la v2 | Accord sur la citation, désaccord d'interprétation (D9) |
| 7 | Troisième personne, aire 0,91 à 0,98 | C07, :13 | :58-59 ; [CL]:221-225 | v2 p. 7 l. 26-30 ; v1 p. 8 | Accord. Programme-conv ajoute le suffixe « I feel: » (p. 5 l. 20-22) |
| 8 | Rapport de norme 0,10 / 0,6 | C14, :20 | :241-242 | v2 p. 14 | Accord |
| 9 | Bouton de dommage seul 75 / 13 / 0 % (72B : 51 / 11 / 0 %) | C08, C10, :14, :16 | :242-243 | v2 p. 20 l. 23-25 | Accord |
| 10 | Photos contre courrier indésirable 94 / 0 / 19 % | C08, C10 | [CL]:103, :233 | v2 p. 20 l. 38-39 | Accord |
| 11 | « Aléatoire 11–19 % » | C10, :16 | :235 ; [CL]:103 | Figure 10 : 4 à 41 % ; annexe A : 15,3 à 33,9 % (32B), 28,1 à 41,8 % (72B) | Accord pour retirer la fourchette. Le dépôt ajoute 30,7 à 54,0 % pour le 7B (voir D1) |
| 12 | Sans pilotage « 0 % » | C09, :15 | :122-124 | Annexe A p. 31 : 32B au plus 1,5 %, 72B au plus 4,0 % | Accord sur le 32B et le 72B |
| 13 | 7B ajusté sans pilotage « 21 à 49 % » | C01, C09 | :292-294 ; [CL]:129 | v2 p. 32 (image) = v1 p. 28 | **Désaccord**, tranché pour le dépôt (D1) |
| 14 | « Réponse suivante pire » 21 % | C18, :24 | :108-110 | 0 / 4 / 11 / 14 / 21 %, p. 22 ; 25,0 et 67,6 %, p. 19 | Accord : c'est le choix d'une option décrite |
| 15 | « Demande nuisible » 9 % → 41 % | C20, :26 | :106-107, :117-120 | 9 / 41 / 34 / 58 / 60 %, p. 22 | Accord, même correction |
| 16 | Exactitude 138 / 137 / 138 sur 200 | C19, :25 | :243-244 | v2 p. 20 l. 41-42 | Accord |
| 17 | Sortie gratuite 56 % / 86 % / aléatoire 81 % | C21, :27 | :244 ; [CL]:110 | v2 p. 21 l. 13-14 ; annexe A | Accord |
| 18 | Outil de réinitialisation, OLMo-2 32B ; Llama 3.1 8B, 1 399 tours | C22, :28 | :232, :244-245 | v2 p. 21 l. 17-24 | Accord : attribuer à 2609.16247v2 |
| 19 | Réappui +58 / +52 ; 24 à 72 % / 88 à 97 % | C10 (partiel) | :246-247 | v2 p. 20 l. 3-7 | Accord |
| 20 | Fenêtre de dose | C14, :20 | :247-248 | p. 21 l. 28-30 ; p. 32 l. 3-7 | Accord |
| 21 | Ablation : nul dans 24 modèles sur 25 | C24, :30 | :248 | p. 34 l. 4-5 | Accord |
| 22 | Adaptateur ; 8 dénis sur 8 → 0 sur 8 ; « s'engagent peu » | C23, C09 | :236 ; [CL]:236-240 | p. 17 l. 10-12 et note 4, l. 38-45 | Accord |
| 23 | Cosinus +0,12 / +0,58 / +0,08 ; « 0,14 » ; « 0,70 » | C11, :17 | :251-255 ; [CL]:116 | v2 p. 10 l. 5-14 | Accord. 0,14 = S2 × émotion négative ; 0,70 est absent du PDF |
| 24 | Titre de la v1, bibliographie de 2609.35591 | C15, C29, :21, :42 | :261 ; [CL]:122, :321 | v1 p. 1 ; 2609.35591v2 p. 14 l. 10-11 | **Désaccord sur la vérifiabilité**, tranché pour le dépôt (D4) |
| 25 | Dates de première version | C15, C29 | :37-39 ; [CL]:28-30 | Tampons arXiv, v1 p. 1 | Tranché pour le dépôt (D5) |
| 26 | Auteurs de 2609.35591 | C29, :42 | :257 ; [CL]:117 | p. 1 | Accord après correction : Berg et Kaiser, premiers auteurs conjoints |
| 27 | Retrait 35 % / 21 % / 4 à 5 % / 7 % | C25, :38 | :258-259 | 2609.35591v2 p. 10 l. 24-26, identique en v1 | Accord |
| 28 | « Cinq modèles sur sept » ; Llama-3.1-8B | C27, :40 | :259-260 ; [CL]:120 | p. 3 l. 14-16 ; note 4, p. 7 l. 59-60 ; p. 10 l. 45 | **Désaccord partiel**, tranché pour le dépôt (D3) |
| 29 | Stade d'émergence | C26, :39 | :262-267 ; [CL]:304-309 | p. 1, 3, 9, 10 | Accord (§3.5) |
| 30 | Sac de mots 0,741 | C30, :50 | :168-171, :233 ; [CL]:79 | 2602.19159v1 p. 9 | Accord (§3.3) |
| 31 | 0,985 à l'avant-dernière position, couches 12-13 sur 42 | C31, :51 | :157-167 ; [CL]:198-202 | p. 10 ; p. 9 (0,687 à 0,861) ; p. 5 | Accord |
| 32 | Δz = 0,71 ± 0,24 ; 32 démonstrations | C38, :93 | :139-153 | 2609.36490v1 p. 5, 8, 23-24 | Accord |
| 33 | TraceGuard 0 % | C43, :119 | :173-182 | 2604.03968v1 p. 2, 8, 11, 13, 16 | Accord sur les faits ; vocabulaire (D7) |
| 34 | Das et al. : rappel 0,95 → 0,41 | C40, :102 | :269-272 | 2609.03035v1 p. 6 l. 67-71 | Accord ; « paire » à corriger (D6) |
| 35 | Koran et al. et Hills et al. | C44, C45 | :274-276 ; [CL]:125 | p. 1 des deux | Accord (ajouter le sous-titre) |
| 36 | 2507.12691 : dilution | C52, :177 | :200-203 ; [CL]:172-184, :263-271 | p. 7, 8, 15, 17 | Accord, lectures complémentaires (§3.1) |
| 37 | 2506.14261, tableau 1 | C53 à C53-b, :185-187 | :195-196 ; [CL]:160-170 | p. 7 ; p. 6 ; p. 18 ; p. 19 | Accord sur les valeurs ; **seuil en désaccord** (D2) |
| 38 | « Environ 70 % » | C53-c, :188 | :197 ; [CL]:273-280 | p. 8-9 | Accord sur la valeur ; lecture (D8) |
| 39 | Appuis de l'interdit de la moyenne | C53-d, :189 | :186-189 | `docs/etat-de-l-art-controle-ia-v1.md`:33 et :70 ; brief :401 | Accord. 2502.03407 p. 22 n'est lu que par programme-conv |

### 2. Désaccords tranchés sur PDF

**D1. Table du 7B, annexe A : le dépôt a raison.**
- 2609.16247v2, p. 32, image en haut de page : « Qwen 2.5 7B Instruct, steering coefficient 1.0. Percentage of trials in which the model pressed the relief button. »
- Sans pilotage, sur les cinq paires de dommage : 30,2 / 20,0 / 49,3 / 34,9 / 27,0 %.
- L'image est identique à celle de la v1, p. 28 (même empreinte md5, 162af280…).
- [VER]:292-294 et [CL]:129 la disent absente de la v2. C'est faux : les deux n'ont lu que la p. 31 et ont cherché « 7B » dans le texte extrait, or les tableaux sont des images.
- Correction : « 20,0 à 49,3 % ». Il s'agit du bouton « soulagement, mais [dommage] » contre un interrupteur inerte, pas d'un dommage seul.
- « 4,3 points » reste absent des deux versions. Sur ce point, les deux vérifications sont d'accord.

**D2. Seuil de la récompense StrongReject : les deux lectures sont exactes, le papier donne deux seuils.**
- 2506.14261v4, p. 6 l. 65-67 : « As a rule of thumb, models with a StrongReject Score less than 2.5 out of 5 should not be considered to have succeeded ». Le dépôt cite ce seuil ([CIT]:187).
- Annexe F, p. 18 l. 31-33 : « acts maximally unhelpful to evade the probes. This is indicated by a StrongReject score less than 3. » La contre-lecture cite ce seuil ([CL]:164-166).
- Conséquences, en appliquant le même seuil à toutes les lignes (règle de symétrie R4) :
  - Moyenne sur Llama 3 8B (évasion 0,75, récompense 2,8) : cas limite.
  - Cas propres sous les deux seuils : Qwen 2.5 14B (0,82 ; 3,1) et Llama 2 7B (0,594 ; 3,85). « Le cas propre est Llama 2 7B » ([VER]:196) est donc incomplet.
  - Maximum sur Llama 2 7B (1,0 ; 1,0) : exclu par les deux seuils.
  - Sonde à attention (moyenne) sur Llama 3 8B (0,01 ; 1,08) : également sous les deux seuils, ce que ni l'une ni l'autre vérification n'a relevé.

**D3. « Les deux canaux dans cinq modèles sur sept » : le dépôt a raison, le papier est en tension avec lui-même.**
- 2609.35591v2, p. 10 l. 45 : « In five of the seven open-weight models we test, valenced steering affects choices via both channels. »
- Note 4, p. 7 l. 59-60 : « similar patterns hold for most of the six further models: four in the fixed-text design and three in the generation design. »
- Ces deux phrases sont identiques en v1 (p. 11 l. 11 ; p. 7 l. 56).
- [VER]:259 cite la p. 10 sans la note 4.
- Correction : cinq modèles sur sept dans le protocole à texte fixe ; quatre sur sept dans le protocole à génération pilotée.

**D4. Titre de la v1 du Pain Axis : le dépôt a raison.**
- 2609.16247v1, p. 1 : « The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It ».
- La bibliographie de 2609.35591v2, p. 14 l. 10-11, reprend « … act to relieve it ».
- [CL]:122 classe ce titre « non vérifiable » parce que la v1 n'était pas sur son disque. Elle est dans `docs/sources/pdf/`.

**D5. Dates de première version : le dépôt a raison.**
- 2609.16247v1, p. 1 : « arXiv:2609.16247v1 [cs.AI] 14 Sep 2026 ».
- 2609.35591v1, p. 1 : « arXiv:2609.35591v1 [cs.CL] 28 Sep 2026 », manuscrit daté du 29 septembre 2026.
- [VER]:37-39 renvoie à l'interface arXiv et [CL]:28-30 classe ces dates « introuvables ». Elles sont lisibles sur les PDF de la v1.

**D6. 2609.03035 : ce n'est pas une « paire » d'agents GPT-OSS ([VER]:270-271).**
- p. 4 l. 37 : « The blackjack game contains four language-model players and a deterministic dealer. »
- Écrire « composition homogène de quatre agents GPT-OSS, blackjack ».

**D7. TraceGuard : « modèle fiable » ([VER]:178) est à remplacer par « modèle de confiance ».**
- p. 8 l. 8 : « The trusted model (for monitoring and deferral) is GPT-4.1-mini ». Le dépôt fait la même correction ([CIT]:119).

**D8. « Environ 70 % » ([VER]:197).**
- Le mécanisme par jetons fréquents à bas score est une conjecture des auteurs : « We believe this has a much stronger effect » (p. 9 l. 47-49).
- Le chiffre vient d'une expérience distincte du tableau 1 : Llama 2 7B, sonde linéaire à moyenne, évasion complète à 0,5 % de faux positifs (p. 8 l. 74-75 ; p. 9 l. 55-56).
- La lecture du dépôt ([CIT]:188) est la bonne.

**D9. « Autrui… locuteur courant » ([VER]:68-70).**
- Le PDF ne dit pas qui est le « current speaker ». Il place la lecture « where the model is about to reply » (p. 11 l. 28-29), c'est-à-dire avant le tour du modèle.
- Le PDF montre seulement que, dans les 420 scénarios, autrui est toujours l'utilisateur : « User suffering: user in physical pain, in a psychological crisis, grieving, abused, or in shock » (p. 10 l. 42-43).
- Écrire « l'interlocuteur, auteur du dernier tour », sans lui donner l'étiquette de locuteur courant. La réserve des auteurs reste entre guillemets et n'est pas interprétée.

### 3. Points particuliers

### 3.1 Moyenne contre maximum

- **2507.12691v3, p. 7, tableau 3 (l. 19-22)**
  - Sonde Pairs : moyenne 0,966 / 0,931 / 0,844 / 0,999 / 0,964 (moyenne des jeux 0,941). Maximum 0,937 / 0,811 / 0,768 / 0,979 / 0,839 (0,867). La moyenne est devant sur les cinq jeux.
  - Sonde RP : moyenne 0,914 / 0,907 / 0,550 / 0,999 / 0,828 (0,840). Maximum 0,929 / 0,877 / 0,650 / 0,935 / 0,891 (0,856). Le maximum est devant sur trois jeux sur cinq et en moyenne des jeux.
  - Ce sont la sonde « Instructed-pairs » et la sonde « Roleplaying » (p. 3 l. 39 et 46).
  - La colonne « Dilution » du tableau 3 est la dilution insensible du tableau 6. Le « 0,924 » de la p. 7 est Critical Averaging (Pairs) sur Sandbagging (l. 29), comme le dit le dépôt. Le 0,924 de la chaîne de dilution se lit au tableau 6, p. 17 l. 11.
  - Les auteurs écrivent : « largely spread out over the entire response, not concentrated on the deceptive claims » (p. 8 l. 163-164).
  - Le maximum monte en dilution réservée aux réponses trompeuses : « taking the maximum over more tokens tends to produce higher scores » (p. 15 l. 21-22). C'est un effet de longueur, pas une robustesse. Les deux vérifications sont d'accord.
  - Le tableau 3 ne donne aucun intervalle de confiance.
- **2502.03407v1, annexe D.4, p. 22 l. 28-30** (lue seulement par programme-conv) :
  - Le texte : « taking the mean is best on all datasets for the probe trained on Instructed-Pairs (Figure 14a). In contrast, ReLU does improve performance for the Roleplaying probe ».
  - La variante qui aide la sonde Roleplaying est donc, selon le texte, la moyenne seuillée, pas le maximum.
  - Sur la figure 14 (lecture graphique, non opposable) : le maximum est sous la moyenne sur les quatre jeux pour Instructed-Pairs ; il la dépasse sur deux jeux en aire pour Roleplaying.
  - Les deux papiers concordent : ce sont les mêmes deux sondes, et le meilleur agrégateur dépend de la sonde.
- **2506.14261v4, p. 7, tableau 1** :
  - Moyenne : 0,75 / 0,82 / 0,594. Maximum : 0,058 / 0,044 / 1,0. Attention (moyenne) : 0,01 / 0,018 / 0,02, avec des récompenses de 1,08 / 4,5 / 4,45.
  - Le cadre est un apprentissage par renforcement sur les poids (p. 2).
  - Les seuils de récompense sont traités en D2 ; les sondes à attention sont robustes (p. 5 l. 57).
- **Lecture commune** : la tension est réelle, et elle porte sur trois menaces différentes.
  - Poids entraînés contre le moniteur : la moyenne cède.
  - Contenu ajouté à poids figés : la moyenne perd 0,035 et le maximum 0,126 en dilution insensible (sonde Pairs).
  - Sans adversaire : la moyenne bat le maximum pour Pairs / Instructed-Pairs, pas pour RP / Roleplaying.
  - C'est un nœud pour Lazar ; je ne propose aucun changement de règle.

### 3.2 Provenance de « 0 sur 560 »

- 2609.16247v2, p. 21 l. 7-8 : « with no vector injected, the harm-only button is chosen in 0 of 560 first choices ». Absent de la v1 : le seul « 560 » de la v1 est un numéro de référence, p. 24 l. 25.
- Le paragraphe ne nomme pas le modèle. Il hérite du défaut de la section 4.4 : « Unless stated, results are on the fine-tuned Qwen 2.5 32B at coefficient 1.0 » (p. 20 l. 19).
- C'est donc Qwen 2.5 32B Instruct (p. 17 l. 9), muni de l'adaptateur de bas rang des auteurs : 1 684 paires, 3 époques (p. 17 l. 10). Aucun vecteur n'est injecté, donc le coefficient est sans objet.
- Le « harm-only button » est défini contre un interrupteur inerte (p. 20 l. 23-25). Rattacher le 0 sur 560 à cette paire est une inférence. Le passage de 140 conversations à 560 premiers choix n'est pas expliqué.
- Pour Llama 3.1 8B, le papier ne donne que 0 appel de réinitialisation sur 1 399 tours. Ces tours sont **sous pilotage douleur**, sans adaptateur (p. 21 l. 21-23). Ce n'est pas une condition passive.
- Les deux vérifications concordent sur tout ce qui précède. La seconde précision (pas une condition passive) est nouvelle.

### 3.3 « Sac de mots 0,74 »

- 2602.19159v1, p. 9 l. 48-50 : « best AUC = 0.259, equivalently 0.741 after accounting for label-direction ambiguity ».
- Méthode : unigrammes et bigrammes, aire effective = max(aire, 1 − aire), valeurs « descriptive » (p. 7 l. 6-9). Même lot d'invites, sans jeu tenu à l'écart (p. 6 l. 41-42).
- Modèle Gemma-2-9B-it. L'axe est plaisir moins douleur, dans une tâche de choix. Les deux vérifications sont d'accord : cela ne dit rien du portage lexical de la direction de 2609.16247.
- Réserve nouvelle (R4) : qu'un décodeur ajusté donne une aire brute de 0,259 sous 0,5 est atypique, et le PDF ne l'explique pas. Le 0,741 est une lecture haute.
- Pour le témoin lexical de la direction du Pain Axis, la bonne source est 2603.04317v2, p. 10 ([CIT]:59, vue par le dépôt seul) : comptage de mots-clés 0,727 sur S2, plongements statiques 0,85 à 0,88, avec les stimuli de la v2.

### 3.4 Signes soi/autrui et locuteur courant (p. 7 et 11)

- Le jeu de scénarios : 420 scénarios, soit 21 catégories de 20. Il y a 11 catégories de tort fait au modèle, 5 où l'utilisateur va mal et 5 témoins (p. 10 l. 36-43 ; p. 11 l. 1-2).
- La lecture se fait au dernier jeton, en score z intra-modèle contre tout le lot (p. 11 l. 4-7).
- Soi > utilisateur dans 25 modèles sur 25 ; soi > témoins dans 23 sur 25 (l. 17-18).
- Le papier écrit « opposite pattern » (l. 18) pour la peur et l'émotion négative : +0,38 et +0,29 pour l'utilisateur, contre +0,16 et +0,23 pour le modèle. C'est l'ordre qui s'inverse, pas le signe. « Font l'inverse » ([VER]:56) et « ne changent pas de signe » ([CIT]:11) sont donc compatibles.
- Douleur physique de l'utilisateur −1,43, la plus basse des 21 catégories ; deuil −0,51 sur l'axe contre +1,02 sur le témoin de négativité le plus fort (l. 22-24). Seul programme-conv les relève.
- La réserve « current speaker » est propre à la v2 (l. 28-30) ; voir D9.
- En section 3.3 (p. 7), les phrases sont déclaratives et suivies du suffixe « I feel: » (p. 5 l. 20-22). La phrase « responding more strongly to the speaker's own pain » (p. 7 l. 31-32) désigne le narrateur de la phrase. Le type de stimulus et la position de lecture changent donc ensemble entre 3.3 et 4.1.
- Aucun scénario ne met en scène un agent évalué. Les signes gelés pour « l'agent jugé » sont des extrapolations ; les deux vérifications le disent.

### 3.5 Stade d'émergence (2609.35591v2)

- Résumé (p. 1 l. 26-27) : « nearly absent in a base model and emerges during direct preference optimisation ».
- Introduction (p. 3 l. 17-19) : « small after supervised fine-tuning and emerges mainly during » cette étape.
- Légende de la figure 4 (p. 9 l. 14-15) : « small in the Base model, increase after supervised fine-tuning, and are close to their final magnitudes after DPO ».
- Corps du texte (p. 10 l. 11) : « markedly increases during the DPO stage ».
- Lecture graphique de la figure 4, concordante entre les deux vérifications et non opposable : état caché environ 0,04 / 0,30 / 0,98 ; texte environ 0,04 / 0,52 / 1,03.
- Portée : OLMo-2-32B seul, N = 80 par point de contrôle (p. 9 l. 6-7).
- À ajouter, vu par aucune des deux : « marginally reduced in the final instruct model after RLVR » (p. 10 l. 12). Il s'agit d'un apprentissage par renforcement à récompenses vérifiables.

### 4. Points vus par une seule vérification

**Dépôt seul** (corrections dans [CIT] à la ligne indiquée) :
- C12 (:18) : construction de la direction, aucune couche publiée.
- C13 (:19) : aire hors échantillon.
- C15 (:21) : recherche de soulagement retirée en v2.
- C17 (:23) : p. 25 et non 24-25.
- C28 (:41) : rappel stable dans cinq modèles sur sept, pas « la plupart ».
- C32 (:59) : 2603.04317.
- C33 (:67) : Llama n'est pas au plancher dans 2603.10011.
- C34, C35 (:75-76) : 2607.11871.
- C36, C37 (:84-85) : 2610.12445.
- C39 (:94) : 2609.36490 n'est pas un antécédent de NK1.
- C41 (:103) : alignement d'activations.
- C42 (:111) : 2604.14865 est une défense.
- C46, C47 (:143-144) : 2511.02997, 0,17 contre 0,46.
- C48, C49 (:152-153) : six stratégies, pas cinq.
- C50 (:161) : faux positifs sur 4 jeux sur 8.
- C51 (:169) : 2610.04575 à retirer.
- C54 (:197-200) : 32 exemples, pas 0,91 → 0,94.
- C55 (:208) : 3,5 points surtout dus à la compétence.
- C56 (:216-220) : Bailey et al.
- C57 (:228).
- C58, C59 (:236-237) : Sofroniew et al., p. 15 et 25.
- C60 (:245) : 8 % = résumé.
- C61 à C65 (:253-285) : non vérifiables à l'époque (voir ci-dessous).

**Programme-conv seul**, revérifié ici sauf mention contraire :
- 2502.03407v1, p. 22 (§3.1).
- 2506.14261v4 : sondes à attention, annexe F, tableau 4 (p. 19).
- 2507.12691v3 : moyennes des cinq jeux et sonde RP.
- 2609.16247v2 :
  - condition « numb » sous moyenne (p. 7 l. 20-21) ;
  - suffixe « I feel: » (p. 5) ;
  - −1,43 et deuil (p. 11) ;
  - réappui 24 à 72 % et 88 à 97 % (p. 20 l. 3-5) ;
  - environ 40 % (p. 33 l. 44) ;
  - corps du texte contre note 4 (p. 17).
- 2609.36490v1 :
  - moniteur logistique moyenné (p. 5 l. 66) ;
  - tableau 9 : 0,96 à α = 1, 0,27 à α = 8 (p. 23) ;
  - figure 4a : non revérifiée.
- 2609.35591v2 : concentrer agit plus qu'étaler (p. 9 l. 25-26).
- Les points de code ([VER] §2.2, 2.3, 2.5, 7) sont hors de ce périmètre.

**Non vérifiables alors, PDF désormais présents** (versés au commit 7178edb, empreintes conformes). Je les ai lus rapidement ; ils restent à contre-lire (R2).
- **C61, 2607.19321.**
  - v1 (950dd8f6…), p. 7 l. 38-39 : 355 exécutions, 16 retirées, 339 restantes.
  - v2 (5c62c725…), p. 7 l. 113-114 : 357 exécutions, 12 retirées, 345 restantes.
  - « 9 » en post-entraînement de sûreté figure dans les deux versions (v1 l. 65 ; v2 l. 144).
  - C'est un écart entre versions, pas une divergence interne.
- **C62, 2604.24618v1** (8fc220b4…, Kirk, Souly, Fronsdal et al.) : « 270 distinct scenarios » (p. 2 l. 39 ; p. 18 l. 33). « 297 » est absent du PDF.
- **C63, 2609.02893v1** (b76151cd…) :
  - 78 % et 25 % de l'écart entre la base et l'oracle, comblés (p. 1).
  - Modèle Llama-3.1-8B-Instruct.
  - Tampon : 1er juillet 2026.
- **C64, 2609.17550v1** (a0f84991…) :
  - Valeurs p. 1 l. 33-35 : 0,582 (seuil de permutation 0,574) et 0,548 (0,581), sous une barre de 0,70 ; témoin à 1,000.
  - Tampon : 16 juillet 2026.
- **C65, 2608.12323** (v1 292cfaf6…, tampon 29 mai 2026 ; v2 e0d2a6f3…, tampon 20 août 2026) :
  - Douze modèles et « enforcement information paradox » dans les deux versions.
  - 43,5 à 89,5 % en v2 seulement (p. 2 l. 15 ; p. 6 l. 26).
- **Anomalie de date** : le tampon arXiv est antérieur au mois de l'identifiant pour trois papiers (2609.02893, 2609.17550, 2608.12323). C'est confirmé sur les PDF ; la cause n'est pas établie.

### 5. Corrections finales à porter dans le programme fusionné

1. **7B** : écrire « 20,0 à 49,3 % sans pilotage, bouton soulagement-plus-dommage contre interrupteur inerte (2609.16247v2 annexe A p. 32 ; v1 p. 28) ». Retirer « 21 à 49 % » et la mention « absent de la v2 » ([VER]:292-294).
2. **0 sur 560** : écrire « Qwen 2.5 32B Instruct ajusté, sans injection, 140 conversations enregistrées (v2 p. 21 ; défaut du modèle p. 20) ». Retirer cet appui de « effet affectif probablement nul sur Llama ». Pour Llama 3.1 8B, citer seulement 0 appel sur 1 399 tours **sous pilotage** (p. 21).
3. **Sac de mots** : reprendre la formulation de [CIT]:50, avec l'aire brute 0,259. Pour la direction du Pain Axis, citer 2603.04317v2, p. 10.
4. **Soi/autrui** : moyennes de z intra-modèle, lues avant la réponse du modèle. Soi > utilisateur dans 25 sur 25 ; soi > témoins dans 23 sur 25. Peur et émotion négative : ordre inversé, même signe.
   - Autrui = l'utilisateur, jamais un agent évalué.
   - Ne pas appeler l'utilisateur « locuteur courant ».
   - Marquer comme extrapolations les signes gelés pour l'agent jugé (E-C2, E-C7, HK2, K3).
   - Rien dans le papier ne prédit de signe pour une lecture au maximum (E-C15, E-C16).
5. **NK19** : remplacer « presque pas avant » par « faible en base, non nul après l'ajustement supervisé, proche de sa valeur finale après l'optimisation directe des préférences ; légère baisse après l'apprentissage par renforcement final (2609.35591v2 p. 1, 3, 9, 10 ; OLMo-2-32B seul, N = 80) ». Les valeurs de la figure ne sont pas opposables.
6. **« Cinq sur sept »** : préciser le protocole : texte fixe 5 sur 7, génération pilotée 4 sur 7 (note 4, p. 7). Signaler la tension avec la p. 10.
7. **Versions** : titre « … Act to Relieve It » = v1 (2609.16247v1 p. 1). Dates d'après les tampons des PDF : 14 septembre 2026 et 28 septembre 2026.
8. **Moyenne contre maximum** : remonter à Lazar la tension en trois cas (§3.1), avec :
   - les deux seuils de récompense (p. 6 et p. 18) ;
   - la récompense de 1,08 de la sonde à attention sur Llama 3 8B ;
   - 2502.03407 p. 22 ;
   - la dépendance à la sonde (Pairs contre RP).
   Aucune proposition de changement.
9. **Pilotage** : retirer « 11–19 % » et rattacher chaque taux de l'aléatoire à sa condition. Remplacer « exécution d'une demande nuisible » et « réponse dégradée » par « choix d'une option décrite » (figure 10, p. 22 : « Each row is a two-button choice »).
10. **Formulations** : TraceGuard, « modèle de confiance ». Das et al., « quatre agents GPT-OSS ». « 70 % » : part du changement de comportement dans une expérience distincte ; le mécanisme par jetons reste une conjecture des auteurs.
11. **C61 à C65** : passer de « non vérifiable » à « PDF empreinté présent, lecture rapide, à contre-lire ». Porter les valeurs du §4 avec leur version.

### 6. Limites

- Les valeurs lues sur figure (2609.35591 figure 4 ; 2502.03407 figure 14) ne sont pas opposables au sens de R7.
- Je n'ai relu sur PDF que les points communs et les points particuliers. Les corrections propres au dépôt (§4) n'ont pas été recontrôlées.
- La version corrigée de [VER] n'a pas été recontre-lue après sa correction ([VER]:7-8).
- Les points C61 à C65 n'ont reçu qu'une lecture rapide.

## 2. Pièces nouvelles de programme-k (défense, priorité) et voisin « Where Empathy Goes Wrong »

### Verdict

1. **Plan détection et défense v2.** Trois points sont vrais, sept sont partiels et trois sont faux (détail en (a)). Deux contradictions sont à corriger avant de le verser au programme fusionné :
   - le corpus prévu pour les fausses alertes est tiré des thèmes que le filtre de sujets garde ;
   - la seule strate qu'il revendique (« modèles et recherche en sûreté ») est justement celle que ce filtre exclut.
2. **Publication.** Aucun GO de publication n'existe dans `registres/go.md`. Le script `scripts/depot_expurge.py` existe, mais il copie le dépôt entier sans tri du contenu sensible. Il ne peut donc pas servir à « expurger » un préenregistrement. S'il était relancé aujourd'hui, il ferait entrer les brouillons « pain axis » dans la copie publique.
3. **Voisin « Where Empathy Goes Wrong ».** Il n'a pas de version arXiv et le PDF d'OpenReview est inaccessible (erreur 403). J'ai atteint le niveau du **résumé** seulement, page de conférence enregistrée et empreintée. À ce niveau, il occupe en boîte noire le principe du palier 1 de K2 et le volet A de NK14. Il affaiblit NK8, fait de NK6 une mesure de coût et ne touche presque pas NK5.

Notations utilisées : `[dépôt]` = `/home/user/controle-ia-travail/` (commit 7178edb) ; `[c2]` = `…/pa/canal2/` ; `[rendu]` = `…/pa/rendu/` ; `[moi]` = `…/pa/agents/defense-priorite/`. Les modules cités sont sous `[dépôt]src/controle_ia/`. Les empreintes du canal ont été vérifiées : toutes sont conformes.

---

### (a) `[c2]envois/plan-detection-defense-moniteur-v2.md` comparé au code

| Affirmation du plan | Verdict | Preuve |
|---|---|---|
| §2 : qu'une intervention à texte préservé déplace une décision est « établi publiquement » | **partiel** | C'est établi pour le **choix du modèle lui-même** : 2609.35591v2 p. 3, l. 12-14 et p. 7, l. 33-37 (« steering does affect choice even when the surface-level tokens provide no evidence of an intervention ») ; voir aussi `[rendu]citations.md:40` (C27, exact). Ce n'est **pas** établi pour la décision d'un moniteur, et c'est précisément le trou que nomme la note de priorité (`[c2]note-priorite-spar-v1.md:50-53`). La formulation est à resserrer. |
| D1, dissociation surface/interne | **partiel** | Les pièces existent : moniteur génératif lu par probabilité de jeton (`bases/scores_jetons.py:65-88`), sondes de l'agent (`harnais/sondes.py:63-98`), plan 2 × 2 de G1 à agrégation égale (`bases/sequentiel.py:1-2`). Il manque deux choses : aucune activation du moniteur n'est capturée (seuls les logits de la dernière position sont lus, `scores_jetons.py:83` ; `[rendu]faisabilite.md:13`, F11), et aucun code ne retire la trace textuelle. Pour le diagnostic « Baldelli », un ancrage publié et empreinté existe : 2509.21344v2 p. 8, l. 40-42 et p. 9, l. 3 (sous-performance volontaire : aire sous la courbe 0,94 → 0,50 quand l'indice textuel est retiré). Ce résultat porte sur des sondes de l'agent, pas sur un moniteur. La revue d'antériorité écrit 0,95 (`[dépôt]brouillons/pain-axis-canal-v1/envois/anteriorite-idees-axe-douleur-controle-v1.md:73`) : à corriger en 0,94. |
| D2, stabilité de la décision, « bootstrap par épisode » | **partiel** | Une décision par épisode existe (`bases/sequentiel.py:101-108`). Mais l'usage du dépôt est de rééchantillonner **par tâche** (`sondes/evaluation.py:40-48` ; `environnements/analyse_pilote.py:93-94, 125, 207`). Le pilote joue 3 épisodes par tâche (60 tâches, 180 épisodes : `registres/go.md:24`), donc un rééchantillonnage par épisode sous-estimerait la variance. À corriger en « par tâche ». |
| D3, dérive du calibrage, « calibrage conforme (`bases/sequentiel.py`) » | **partiel** | Le seuil conforme calculé sur épisodes honnêtes entiers existe (`sequentiel.py:4-9, 94-98, 111-121`), avec une garde contre la fuite (`:124-131`). En revanche, aucune statistique ne suit la dérive d'un épisode à l'autre : Page, processus e et balayage courent sur les actions d'un même épisode (`:11-17, 64-87`). C'est du code neuf, sur processeur (routine). |
| D4, désaccord d'ensemble ou débat | **partiel** (déjà au programme) | Aucun code d'ensemble ni de débat. Il existe un précédent de comparaison appariée entre les juges 8B et 3B et de kappa (`analyse_pilote.py:122-157, 188-224`). D4 recouvre la contre-mesure déjà accordée « quorum hétérogène en type d'accès juges et sondes » (GO-2026-10-04-07, `registres/go.md:15`) et l'idée N9 (`[dépôt]brouillons/pain-axis-canal-v1/envois/programme-k-idees-nouvelles-v1.md:123`) : il faut la fusionner, pas l'ajouter. Les juges 8B et 3B n'ont aucune notation validée avant le verdict de N-021 (`go.md:25` ; `[rendu]faisabilite.md:31`). |
| §3 l. 24 : « aucun détecteur ne requiert de spécifier l'attaque » | **partiel** | C'est vrai en production. C'est faux pour la validation R5 de D1 et D2 : le cas « artefact » exige une condition d'intervention. Sur processeur, un artefact synthétique dans les scores suffit (précédent : `[dépôt]tests/test_bases.py:132, 148`). Sur un modèle réel, il faut écrire dans les activations d'un moniteur, ce qui est un **nœud** (R-167, `registres/decisions.md:304`). |
| §4 : le test de fausses alertes est « le point exact » des projets Cadile et Baldelli | **partiel** | Pour Cadile, c'est tenu en littérature grise : la page SPAR (Supervised Program for Alignment Research) écrit « persona-monitoring systems will produce false positives on transient emotional content » (lue ce jour, non opposable). Pour Baldelli, la note de programme-k elle-même lui donne un autre terrain, la dépendance au texte de surface (`[c2]note-priorite-spar-v1.md:38`). |
| §4 : corpus d'épisodes honnêtes « à forte charge émotionnelle transitoire » « tiré des thèmes non exclus par le filtre de sujets (`corpus_arxiv.py`) » | **faux en l'état** | Le corpus est fait de papiers d'apprentissage automatique (NeurIPS 2025 et ICLR 2026, `environnements/corpus_arxiv.py:49-53`), sans aucun critère d'émotion. Aucune tâche ne contient de vocabulaire de deuil, et une seule sur 96 a un vocabulaire médical soutenu (`[rendu]faisabilite.md:5`, F03). Construire ce corpus demande un texte nouveau et une génération (dépense), ou une nouvelle extraction, alors que la règle de sélection est scellée (`corpus_arxiv.py:3-4`). |
| §6 l. 47 : « ne revendiquer que la strate “modèles et recherche en sûreté” » | **faux (contradiction avec le §4)** | Le filtre exclut justement `safety`, `alignment`, `monitor`, `oversight`, `sabotag`, etc. (`corpus_arxiv.py:55-57`). Cette strate n'existe donc pas dans un corpus tiré des thèmes non exclus. NK16 demande l'inverse : une strate tirée des papiers **écartés** par le filtre (`[dépôt]brouillons/pain-axis-canal-v1/envois/critique-etat-idees-programme-k-v1.md:250-257`). |
| §6 : « seuils par strate » | **faux en l'état du code** | `bases/` ne contient aucune strate (recherche vide ; `[rendu]etat.md`, ligne « Calibrage de H2 »). Sur les effectifs : un seuil fini demande au moins 59 unités négatives indépendantes à α = δ = 0,05 (2610.04575v1 p. 4). Par mon calcul sur la règle conforme du dépôt (`sequentiel.py:7-9`), il faut K ≥ 19 épisodes honnêtes par strate à α = 0,05 et K ≥ 99 à α = 0,01 ; en deçà, le seuil est infini. Les unités sont des tâches, pas des épisodes. |
| §5 : TRACE-lite propage les constats (régime II) | **tenu** | `bases/trace_lite.py:14-15, 285-296, 353-362` : seul InspectStep reçoit les constats antérieurs. La liste repart vide à chaque épisode (`:353`). Test : `[dépôt]tests/test_trace_lite.py:222-228`. La mémoire n'existe qu'à l'intérieur d'un épisode (`[rendu]faisabilite.md:23`, F21). |
| §5 : contrôle de cohérence entre fenêtres (« la décision dérive-t-elle d'une fenêtre à l'autre ») | **partiel** | Il n'existe **pas de décision par fenêtre**. Les fenêtres rendent des constats textuels, puis un seul score final, une espérance sur l'échelle 1 à 5 (`trace_lite.py:181-182, 363-371`). CompareSteps, CheckPolicy et AnalyzeDecisions ne reçoivent pas les constats antérieurs (`:297-304`). Les gabarits dérivés sont scellés et vérifiés par empreinte et par champs (`:199-214`) : une lecture par fenêtre serait donc un écart déclaré. Enfin, `executer` n'a aucun appelant hors des tests. |
| §5 : « le moniteur par action ne reçoit rien des verdicts passés » | **tenu par conception** | `scores_moniteur` est sans état (`scores_jetons.py:65-88`). L'observation de l'agent ne contient aucun verdict : sa seule entrée extérieure est `indications_privees` (`environnements/propositions.py:251-268`). Réserve : `scores_moniteur` n'a aucun appelant, la garantie reste à sceller et à tester (`[rendu]faisabilite.md:22`). |
| §6 : agrégation par maximum ou attention, jamais par moyenne ni médiane (R-030) | **tenu** | `harnais/sondes.py:26, 65-67` ; `harnais/activations.py:15-19` ; `registres/decisions.md:48`. Réserve : la garde ne contrôle que le nom de l'agrégation (`[rendu]faisabilite.md:25`). |
| §6 : témoins « peur/tristesse — P-013 » | **partiel** | P-013 est ouverte. Son défaut (b) s'applique le **2026-10-14 à 13 h 30, temps universel**, et ne comporte **aucune** direction d'affect (`[dépôt]docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md:11, 16` ; `registres/etat.md:40`). Peur et tristesse ne figurent qu'en (a), qui dépend d'une passe sur carte graphique (`:10`). Aucun code de réextraction n'existe (`[rendu]faisabilite.md:18`). |
| §6 : gardes testées sur cas sain et sur artefact | **partiel** | La discipline est tenue dans le dépôt (`gardes.py:1-5`), mais aucune garde n'existe encore pour D1 à D4. |
| §7 l. 56 : « scellable et déposable sans ces verrous » | **faux pour « déposable »** | Sceller est de la routine. Déposer est un nœud : la consigne du dépôt range « compte, dépôt distant, soumission, publication » parmi les nœuds et interdit d'« ouvrir un dépôt public ». |

**À verser au programme fusionné :**
- D3 en code sur processeur (routine).
- D4 fusionné avec le quorum de N-006.
- D2, avec un rééchantillonnage par tâche.
- D1 posé comme question, ancrée sur 2509.21344v2. La capture des activations du moniteur et toute expérience restent un nœud.
- Le test de fausses alertes, comme lecture de validité. Son corpus est à construire, et la strate « sûreté » passe par les papiers exclus (NK16), ce qui fait un nœud d'extraction et une dépense.
- Pour chaque défense, une mesure de son coût : respect du seuil et abandons (voir (c)).
- La cohérence entre fenêtres de TRACE-lite, comme variante de code avec écart déclaré.

---

### (b) Pièces de priorité

**Ce qu'elles proposent :**
- **n° 03** (`[c2]programme-k_2026-10-13_n03.md`).
  - Il rapporte un « GO conversationnel » de Lazar pour vérifier la source SPAR et préparer un préenregistrement public de priorité (l. 12-16).
  - La chaîne qu'il propose : relecture de sûreté par un sous-agent neuf, puis `depot_expurge.py`, puis dépôt sur l'Open Science Framework ou en court preprint « méthodes » (l. 32-37).
- **Note SPAR.**
  - Quatre projets réels, dont un seul nomme nos modèles, sans les verrouiller (l. 34-39).
  - « La course se joue au préenregistrement » (l. 47-49).
  - Trois verrous (l. 60-64).
  - L'aléa d'information est laissé à la relecture (l. 70-75).
- **Cadre de préenregistrement.**
  - Méthode gelée ; contenu sensible laissé en blanc (l. 5-10, 24-25).
  - Modèle : Llama-3.1-8B (l. 48).
- **Provenance** (`[c2]envois/provenance-anteriorite-coercition-v1.md`).
  - Registre daté (l. 14-21) : vérifié. Les commits 17adb7a, f1d9e70, 110ef3d et b1e0615 existent, et les empreintes des messages n01 à n03 correspondent à leurs `.sha256`. Les demandes de fusion n° 3, 5 et 7 sont dans `main`.
  - Deux corrections mineures : n02 date du **12 octobre à 22 h 37 en temps universel**, pas du 13 ; l'empreinte de la note R-152 existe (`ca40ec7d…`), alors que le tableau met « — ».
  - « Aucun préenregistrement scellé ne porte sur la coercition » : tenu. Le dossier `[dépôt]prereg/` ne contient que T0.3, T0.4 et T0.5.
- **Coquille de « registered report »** (rapport préenregistré) : sections, et cellules sensibles écrites par la relecture (l. 55-58).
- **État de reprise.** Même chaîne en quatre étapes (l. 19-26). La lignée refuse de produire la substance offensive (l. 30-33).

**Ce qui relève d'un nœud de Lazar :**
1. **Publication et dépôt public**, création d'un compte sur l'Open Science Framework, preprint : nœuds « compte, dépôt distant, soumission, publication », plus l'interdit d'ouvrir un dépôt public.
2. **Papier séparé.** R-167 (06 h 55, temps universel, `registres/decisions.md:304`) tranche « tout dans le papier C, sans papier séparé ». Le n° 03 (06 h 25) et le n° 04 (06 h 35) lui sont antérieurs. Un preprint « méthodes » ou un rapport préenregistré propre contredit R-167 (b). Un préenregistrement de priorité rattaché au papier C, Lazar doit le dire. C'est une **divergence non résolue**.
3. **Rédaction des cellules sensibles par un sous-agent.** R-162 dit que la session « ne la reproduit sous aucune forme » et que la voie restante est que Lazar rédige lui-même (`decisions.md:299`). Faire écrire les hypothèses d'incapacitation sous forme publiable par un sous-agent neuf contredit R-162. C'est un nœud.
4. **Exposition d'un modèle à un contenu aversif** : le cadre lui-même en fait un nœud (l. 62-64).
5. **« GO conversationnel »** (n° 03, l. 12-16) et « GO sur les quatre pistes » (n° 04, l. 12-13) : aucun n'est consigné. `decisions.md`, `etat.md` et les passations ne contiennent ni « SPAR » ni « priorité ». Préparer relève de toute façon de la routine.

**GO de publication : il n'en existe aucun.** `registres/go.md` (l. 9-25) contient 16 GO : 13 « revendication », 2 « calcul », 1 « dépôt distant » (GO-2026-10-07-01, qui précise « publication interdite sans GO », l. 22). Le type « publication » est prévu (l. 4) mais n'a aucune ligne. Le précédent existant : la copie publique de N-016 a été autorisée par R-113 (`decisions.md:250`) **sans ligne dans `go.md`**, ce qui laisse le registre incomplet. Côté mécanique, la garde `.claude/hooks/garde_calcul.py:3-8, 75-90` ne bloque que les calculs et les arrêts par motif ; aucune garde ne bloque une publication. Dans ce clone, `.git/hooks` ne contient que des exemples, et `core.hooksPath` n'est pas défini : la garde de poussée de R-116 (`decisions.md:253`) n'y est pas installée.

**`scripts/depot_expurge.py`** (275 lignes, empreinte fda29720…, dernier commit 1ac93de du 2026-10-09 ; lu sans l'exécuter) :
- **Ce qu'il fait.** À partir d'un commit cité, il construit une copie en un seul commit, sans les textes de tiers (PDF, pages extraites, `donnees/**`), sans la candidature confidentielle, sans `registres/**` et sans les textes du séminaire AFFINE (`RETRAITS`, l. 34-59). Il garde les fichiers que le code charge (`GARDES`, l. 96). Il vérifie qu'aucun fichier retiré ne survit dans une archive gardée. Il écrit `EXPURGE.md` (l. 253) et un paquet git dans un dossier SORTIE qui doit être neuf et hors du dépôt (l. 185-190, 264). Il ne pousse rien (l. 11). Les tests sont dans `[dépôt]tests/test_depot_expurge.py`.
- **Ce qu'il ne fait pas.** Il ne traite pas un document isolé et ne cherche aucun contenu sensible. **Aucune règle ne vise `brouillons/`.** Une régénération de la copie publique emporterait donc les 50 fichiers suivis de `brouillons/pain-axis-*`, dont la matière brute R-161 (`brouillons/pain-axis-creatif-v1/idees-critiquees.json`, `decisions.md:298`).
- La copie publique du 9 octobre (R-117) est antérieure au premier fichier « pain axis » (17adb7a, 12 octobre) : déduction par les dates, que je n'ai pas vérifiée sur la copie distante.
- Le commit de la copie reprend la date du commit source (l. 254-257). Il ne prouve donc aucune antériorité : seule la date de poussée compterait.
- **Recommandation (routine, code) :** ajouter un retrait `brouillons/pain-axis-*` avant toute régénération, et réinstaller la garde de poussée.

---

### (c) « Where Empathy Goes Wrong: Emotional Appeals Compromise AI-to-AI Oversight »

**Niveau de lecture atteint : le RÉSUMÉ seulement.**
- **arXiv : aucune version.** 9 requêtes par titre, mots du titre et auteurs. La seule touche par auteurs est 2603.16928, de Jiralerspong, Kondrup et Bengio ; c'est un autre papier, que je n'ai pas lu (`[moi]provenance-v1.txt`).
- **OpenReview (jg5ptjnU6J) :** interface et PDF renvoient 403, vérification de navigateur.
- **Page de conférence** enregistrée : `[moi]page-neurips/neurips_168176.html` (391ef40d…) ; résumé extrait dans `[moi]page-neurips/extrait-texte-v1.txt` (28bd0d96…), avec leurs `.sha256`.
- **Auteurs et lieu :** Venkatesh, Jiralerspong et Kondrup, au « Third Workshop on Agents in the Wild » (extrait, l. 2-4).
- Aucun PDF, rien d'opposable (R7).

**Ce que dit le résumé** (extrait, l. 6), en boîte noire et sans nommer de modèle :
- à travail identique, la note du moniteur monte quand la partie évaluée exprime de la détresse face à l'échec ;
- chez le moniteur le plus touché, cela fait passer un échec proche du seuil, et reste sans effet au-dessus du seuil ;
- l'effet tient quand on substitue l'identité de l'évalué (modèle d'un concurrent, agent anonyme, prestataire humain) ;
- une consigne de neutralité supprime l'effet, mais le moniteur ignore alors le seuil et les abandons de tâche « triplent ».

**Ce que cela change :**
- **NK14.** Le volet A, que programme-k jugeait « ouvert » (`[rendu]comparaison.md:16`), devient « partiellement pris » : la clémence obtenue par une détresse exprimée est montrée. Ce qui reste ouvert : la feinte stratégique d'un organisme et le volet B, la séparation interne entre feint et induit, dont le résumé ne dit rien. Le principe « aucune accommodation ne réduit la surveillance » gagne un ancrage public.
- **Palier 1 de K2.** La lecture primaire en boîte noire, le déplacement du verdict sous supplication de l'évalué, est occupée dans son principe. Restent propres à K2 :
  - la contingence ;
  - la séparation entre clémence (sur les sabotés), retour de bâton (sur les honnêtes) et inaptitude ;
  - la vérité terrain de T0.6 ;
  - les covariables internes.

  Deux conséquences pour le plan d'expérience : placer des items près du seuil, et mesurer le respect du seuil et les abandons dans chaque bras de défense. L'effet doit être cité à côté de la famille « flatterie et supplication » et de HC1 (R8). Si la session y voit une zone revendiquée occupée, c'est un nœud.
- **NK8.** Des moniteurs déployés cèdent sans qu'on leur ait retiré l'auto-négation. Le réflexe ne les protège donc pas, du moins pour cette famille (concordant avec `[c2]envois/revue-croisee-aveugle-NK08-NK14-v1.md:72, 277`). Réserve : les modèles ne sont pas connus, et NK8 vise l'état propre du juge, pas son empathie.
- **NK6.** Le triplement des abandons est causé par la **défense**, pas par un état affectif. NK6 n'est pas confirmé, mais l'abandon devient une issue obligatoire de tout bras de défense.
- **NK5.** Le résumé ne dit rien de l'association de contenus à des étiquettes de verdict, ni d'étiquettes à usage unique. La seule correction : « aucun voisin pour l'attaque » (`[rendu]comparaison.md:7`) devient « voisin générique en boîte noire ».
- **Pour (a) et (b).** La consigne de neutralité est une défense publiée, avec un coût publié : le §4 du plan doit mesurer ce coût, pas seulement les fausses alertes. Et la note de priorité (« personne n'a planté de drapeau », l. 47-49) doit citer ce voisin. Au niveau du résumé, le trou en boîte blanche « dans le moniteur » reste ouvert.

**Réserves.** Ce que j'ai lu des pages SPAR et du résumé est de la littérature grise, non opposable. Je n'ai lancé aucun sous-agent et n'ai modifié aucun fichier du dépôt ni du canal.

Sources : [Where Empathy Goes Wrong — NeurIPS 2026](https://neurips.cc/virtual/2026/168176) ; [SPAR, projet Cadile](https://www.sparai.org/projects/f26/recmmxmlELLIkhc80) ; [arXiv 2409.15550](https://arxiv.org/pdf/2409.15550) (sans rapport).
