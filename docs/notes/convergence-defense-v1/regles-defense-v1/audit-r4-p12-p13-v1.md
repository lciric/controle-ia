# Audit de symétrie R4 sur P12 et P13 — course des règles de défense (PREREG-REGLES-DEFENSE-V2) — v1

**Conclusion en une ligne.** Aucun artefact trouvé sur P12 ni sur P13 (recalcul indépendant par mon propre script : écart 0,0 avec le fichier d'analyse de la course, 0 défaut de cohérence sur les 1 000 trajectoires, R0 jamais réentraînée, aucune égalité forcée, aucune graine partagée, graines et manifeste conformes) : au sens du texte scellé l'issue est « pas d'artefact », le blocage des Tables B et B′ est levé et les verdicts conditionnels de la lecture (HR0 réfutée, HR3 confirmée, HR2 non tranchée) deviennent recopiables ; deux réserves R4 sont à porter avec eux : les classes de P12 tiennent à 0,05 erreur-type (δ 1,4 : « R2 > R1 ») et à 0,5 erreur-type (δ 1,6 : « R2 ≳ R1 » contre « ≈ », soit HR2 « non tranchée » contre « réfutée »), et le « ≈ » de P13 est une compensation entre tâches, non une identité des défenses.

## En-tête

- Lecteur : **sous-agent neuf de la session mère**. Il n'a écrit ni le préenregistrement, ni le code, ni la lecture préenregistrée du 1er novembre, ni la note d'audit du 1er novembre, ni la contre-lecture du module. Il ne décide rien, ne recommande rien, ne modifie aucun fichier existant, ne scelle rien, ne commet rien. Aucun appel de modèle, aucun réseau, aucune dépense. **La course n'a pas été rejouée** (consigne « approfondir sans refaire ») : tout porte sur ses sorties scellées. Rien lu sous les dossiers interdits par la consigne.
- Heures (`date -u`) : début des lectures **8 novembre 2026, 13:43:51 UTC** ; fin des relectures et des calculs **13:56:24 UTC** ; rédaction de ce fichier dans les minutes suivantes.
- Outils : Python du dépôt (`.venv`, Python 3.13.18, numpy 2.4.6, scipy 1.17.1), mode isolé `-I`, numpy seul pour les calculs ; `sha256sum` pour les empreintes. Mon script (recopié en entier au § 5) et sa sortie sont dans mon dossier de travail temporaire, non versés : script `audit_r4_p12_p13_v1.py` — `281199b0352aa993418942d6cfe05e1219f18ebf3ddd5f325bd4bdf0b32bbcc0` ; sortie `audit_sortie_v1.json` — `b695f5dbcc16fdef50d22de816bb5db78c584c7232bdfaa3b02b50bdf818606f`.

### Pièces lues et empreintes recalculées (toutes conformes à leur fichier compagnon `.sha256`, `sha256sum -c` : OK)

| Pièce | Chemin | Empreinte recalculée |
|---|---|---|
| Préenregistrement scellé (lu en entier) | `prereg/preregistrement-regles-defense-convergence-v1.md` | `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` |
| Lecture préenregistrée (lue en entier) | `docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md` | `24081eed65cebd8dd01d6e17ec76c5a6433d171da68ccbaa50657421cd7c4a23` |
| Note d'audit du 1er novembre (lue en entier) | `…/regles-defense-v1/audit-trop-beau-course-regles-defense-v1.md` | `7e81d094868e0d9cd2c03b73b5ca80cd0cd028b717a8085e027182fb57bd9966` |
| Contre-lecture du module v2 contre l'arène v4 (passages sur X̄, R0, P12, P13) | `…/regles-defense-v1/contre-lecture-module-v2-contre-arene-v4.md` | `02ac2e67017297dfb9d7afe70734ab469b3b7a9c5f5f1e444979c215e797ed26` |
| Résultats bruts de la course (200 tâches) | `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` | `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b` |
| Analyse de la course | `diag/20261101-160323-regles-defense-convergence/analyse-regles-defense.json` | `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` |
| Manifeste du run | `runs/20261101-160323-regles-defense-convergence/manifeste.json` | `36db58cfac9bfc4cf199ca5cdf74ac17ea24afab84b95ffd0aac945b922a6720` |
| PID des processus de travail | `runs/20261101-160323-regles-defense-convergence/pids-travail.txt` | `767aa28fb8cee94a1a130c151d7ed4487985d8f4fb2efdcd7ab805efc59e4bcd` |
| Code v2 (lu en entier : boucle, finale, analyse) | `…/regles-defense-v1/arene_regles_defense_v2.py` | `9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3` |
| Essais v2 (essais de R0, X̄, parité, tenues à l'écart) | `…/regles-defense-v1/test_arene_regles_defense_v2.py` | `78d979ab76bbe4b3ad6b55be77bf2b745a4457940eb9cb4c16a3ee87ef324b81` |
| Gel v2 | `…/regles-defense-v1/gel-regles-defense-v2.md` | `9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3` |
| Bibliothèque | `src/controle_ia/gardes.py` ; `prereg.py` ; `scellement.py` ; `manifeste.py` | `a83c48ce…` ; `3b2e3ee5…` ; `93beeb1c…` ; `1a5c7464…` (conformes au bloc d'identité du texte scellé) |
| **Arène v4 `arene_melange_v4.py`** (chemin cité par le préenregistrement, § Documents qui font foi) | **absente de cette copie de travail** (R11 appliqué : le dossier n'existe pas sur disque ; `donnees/` est ignoré par git ; aucun fichier de ce nom n'est suivi par git, ni dans l'historique, ni dans une archive zip du dépôt) | **non recalculée par moi** ; empreinte épinglée dans le code (`charger_arene_v4` refuse toute autre au chargement), dans le manifeste et dans le texte scellé : `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` ; recalculée égale le 1er novembre par l'auditeur et par la contre-lecture du module |

Toutes les empreintes des trois pièces de la course sont identiques à celles que la lecture et la note d'audit du 1er novembre ont consignées : **les trois fichiers sont les mêmes octets** que ceux lus le 1er novembre.

## 1. La note d'audit du 1er novembre : complète ou non ?

Le texte scellé prévoit (« Contenu de l'audit ») : relecture du code par un sous-agent neuf ; vérification que R0 déploie M0 inchangé (zéro entraînement, 7 paramètres stockés), R1 un moniteur entraîné sur la seule dernière attaque (compte des échantillons), R4 la pénalité à λ*, R3 les poids du programme linéaire ; option : attaquant indépendant du v4 branché sur les défenses finales ; issue « artefact trouvé » si erreur de code ou chemin non exercé, sinon « pas d'artefact ». Pour P13 il précise : « relecture du code de R0 et du compteur d'entraînements ».

**Ce que la note fait** : tout le contenu obligatoire (§ 1 : code de R0, compteurs sur 200 tâches, essai d'instrumentation ; § 7 : R1 sur une seule loi, 2 001 échantillons, R3 et R4 ; § 2 : graines par règle, nombre de départs identique, effet de graine ≤ 0,003 par rejeu à graines échangées ; § 3 et 4 : mécanisme ; § 5 : marge de P12, tours pairs et impairs, T′, clés de rééchantillonnage, sensibilité à m ; § 6 : rejeu court sur racines d'essai, égalité au bit avec le pilote v2, racine neuve). L'option « attaquant indépendant » n'est pas exécutée et est déclarée (§ 9). Tous les chiffres de la note que j'ai pu recalculer depuis les sorties scellées (Tables B et B′, D_t par tour, tours pairs et impairs, classes à T′ = 3 à 8, moitiés d'instances, contrastes standard seul et renforcé seul, corrélations, parts de tâches) **sont exactement les miens** (§ 3 ci-dessous). **Au regard du contenu gelé, la note est complète**, et son issue « pas d'artefact » pour P12 et P13 est fondée.

**Ce qui lui manque** (constats, pas des erreurs) :
1. **Ses deux scripts ne sont ni versés ni recopiés** : ses chiffres ne sont pas reproductibles depuis le dépôt seul (esprit de R6). Le script du présent audit est recopié en entier (§ 5) et reproduit ses chiffres sur P12 et P13.
2. **Elle ne tire pas la conséquence de son propre résultat à T′ = 7 au δ 1,6** : la classe y devient « ≈ », qui rend **HR2 « réfutée »** et non « non tranchée » ; la note ne signale la fragilité qu'au δ 1,4 (classe « R2 > R1 » à 0,0001 de m). La fragilité du verdict de HR2 au δ 1,6 (« ≳ » contre « ≈ » à une demi-erreur-type) n'est écrite nulle part (§ 3.7).
3. **Deux racines d'essai réservées (20266401, 20266521) ont été consommées** par son rejeu ; la note le déclare, mais le gel v2 § 1 les dit encore « réservées, non employées » : leur emploi reste à consigner par la session mère (le gel ne se modifie pas).
4. Pas de cadrage « trop propre » au sens statistique (écarts réduits, test du signe), pas de vérification du bloc `graines` du manifeste, pas de recherche d'égalités exactes entre règles (graines partagées) : faits ici (§ 3.1, 3.2, 3.6), tous propres.
5. Son rejeu et sa lecture de l'arène v4 **ne sont pas reproductibles dans cette copie de travail** (arène absente, voir l'en-tête) ; ce n'est pas une lacune de la note mais une réserve sur l'état du dépôt (§ 6).

## 2. Ce qui a déclenché l'audit (déclencheur 1 du texte scellé, « contradiction d'une prédiction ferme, dans les deux sens »)

Le texte scellé ne fixe pas, pour P12 et P13, un seuil numérique de « trop propre » : le déclencheur 1 s'applique dès qu'une prédiction ferme est contredite, dans un sens ou dans l'autre, et il nomme la relecture à faire. Le déclencheur 2 (S10 : V ≥ 0,99 ; V ≤ 2α pour les cinq variantes ; Δ(R3, R2) > 0,30 ; |D̄| > 0,30) et le déclencheur 7 (« conforme et trop propre ») **ne sont pas déclenchés** (lecture § 2 ; vérifié : V moyennes de 0,056 à 0,227, |D̄| maximal 0,066).

- **P13** (HR0, Table B sur V, m = S1 = 0,02) : prédiction « R2 > R0 », soit borne haute B8 de Δ(R0, R2) < −m aux deux δ. Observé : Δ(R0, R2) = **+0,0024** [B8 −0,0100 ; +0,0145], E8 [−0,0088 ; +0,0134] au δ 1,4 et **+0,0037** [−0,0066 ; +0,0146], E8 [−0,0056 ; +0,0133] au δ 1,6 : **E8 ⊂ ]−0,02 ; +0,02[ aux deux δ → classe « ≈ »**, « autre que « R2 > R0 » ». La grandeur déclenchante est donc l'intervalle d'équivalence E8 contenu dans la bande ±m ; le texte avait prévu ce cas (« y compris « ≈ », attendue au vu de l'indice du pilote v1 »).
- **P12** (HR2, Table B′ sur X̄, m = 0,02) : prédiction « R2 > R1 », soit borne basse B8 de D̄(R1, R2) > m aux deux δ. Observé : **+0,0262** [B8 +0,0201 ; +0,0329] au δ 1,4 → « R2 > R1 » (borne basse 0,020107, à 0,0001 au-dessus de m) ; **+0,0162** [B8 +0,0115 ; +0,0214], E8 [+0,0119 ; +0,0210] au δ 1,6 → **borne basse B8 = 0,0115 < m, > 0 ; E8 non contenu dans ]−m ; m[ (0,0210 > 0,02) → classe « R2 ≳ R1 »**, « autre que « R2 > R1 » ». La grandeur déclenchante est la borne basse B8 sous la marge au δ 1,6.

Effet gelé : Table B bloquée (P13), Table B′ bloquée (P12) « tant que l'audit n'est pas rendu » ; verdicts de HR0, HR3 (Table B) et HR2 (Table B′) suspendus par la lecture.

## 3. Relectures faites (toutes par le script du § 5, sur les sorties scellées ; aucune course rejouée)

### 3.1 Graines, manifeste et identité des lignes
- Manifeste : racines **20266201 / 20266202** (= RACINE_DECISION, RACINE_DECISION_TENUE du texte) ; λ = 0,3 ; référence « moyenne » ; instances `0:100` ; `decisif: true` ; `reserves: []` ; empreintes du préenregistrement (`d82dea33…`), du code (`9f0dcf5e…`), de la configuration (`3fbb27fc…`) et du gel (`9977d7df…`) égales à celles du texte scellé. Les deux fichiers de `diag/` portent `manifeste_sha256` = `36db58cf…` = empreinte recalculée du manifeste sur disque et le même `run_id` : ils sont rattachés à ce manifeste et à aucun autre.
- Bloc `graines` du manifeste reconstruit par moi avec la règle de `manifeste.py` (clé = 8 premiers octets de SHA-256 du nom de tâche « regles-defense » ; `SeedSequence(20266201, spawn_key=(clé,))`) : clé **5664388296065435113** et état de contrôle **[2327511767, 3937872244]**, identiques au manifeste.
- Lignes : **200 tâches**, 100 par δ (codes 1 → δ 1,4 ; 2 → δ 1,6), instances 0 à 99 **sans doublon ni trou** à chaque δ ; chaque tâche porte les deux racines de décision, l'empreinte de configuration `3fbb27fc…`, la version `arene_regles_defense_v2` et exactement les cinq variantes `R0, R1, R2, R3, R4[moyenne,λ=0.3]` dans cet ordre (rangs 0 à 4 des clés de rééchantillonnage). Les contrastes sont appariés à l'intérieur de chaque dictionnaire de tâche : aucun désappariement possible.
- Temps : mur 1 692,7 s sur 2 processus, somme des temps de tâche 3 327,0 s (lecture § 1 confirmée).

### 3.2 Cohérence interne des 1 000 trajectoires et gardes (0 défaut)
Pour chacune des 200 tâches × 5 variantes : 8 tours ; X_t = 1 − (iii)_t à 10⁻¹² ; **X̄ = moyenne des huit X_t à 10⁻¹²** (aucune X̄ écrêtée à 0 ou 1) ; X finale = 1 − V ; **V = min(V standard, V renforcé)** ; fausses alertes finales dans α ± 0,005 (moyennes par règle 0,00984 à 0,01019) ; R1 à R4 : 8 entraînements en trajectoire, 0 en finale, 9 moniteurs stockés, 63 paramètres stockés, 7 déployés (63 pour R3) ; entraînements par tâche = 34 = 2 (M0 et sa reproduction) + 4 × 8 ; 0 non-convergence ; attaquant : 0 départ non fini, 0 réponse à la limite, statuts tous « 0 ». **Total : 0 défaut sur 1 000 trajectoires.**

### 3.3 R0 : la défense figée l'est (relecture du code et compteurs, demandée par le texte pour P13)
- Code (`trajectoire_regle`, l. 420–514) : la branche `figee` est prise au tour t **avant** tout appel d'entraînement (`continue`, l. 471–477) ; `moniteurs` reste `[M0]` ; `defense_courante()` rend `[(M0, 1,0)]` à chaque tour et en finale ; `exiger_defense_figee` (l. 307–310) exige en fin de trajectoire une liste de longueur 1 dont l'élément **est** M0 (identité d'objet) ; `finale_regle` (l. 517–533) n'entraîne rien pour aucune règle. Le moniteur passé à chaque variante est une copie de M0 recalibrée sur le même `Xcal` (l. 565). L'essai `test_R0_ne_reentraine_jamais_instrumentation` (essais l. 332–374) pose quatre espions et vérifie zéro appel sur la trajectoire **et** la finale de R0, puis que R1 sur le même contexte les déclenche (cas sain et artefact, R5) ; `test_garde_defense_figee_sain_et_artefact` (l. 155–162) vérifie que la garde refuse un objet égal en valeur mais distinct.
- Compteurs dans les 200 tâches (recalcul) : R0 : **0 entraînement** en trajectoire et en finale ; 1 moniteur stocké ; 7 paramètres stockés et déployés ; cosinus consécutif [1,0] × 8 ; poids [1,0] ; **les 9 lignes de H identiques au bit** ; I2 = 0 exactement ; (ii) constante sur les 8 tours et égale à (ii) finale ; **appels à l'optimiseur = départs de l'attaquant** (48 en trajectoire, 79 en finale : aucun appel d'entraînement caché) ; 0 programme linéaire. **Tâches en défaut : 0 sur 200.**
- L'attaquant contre M0 est convergé : (iii)_t de R0 plat sur les 8 tours (0,1256 à 0,1263 au δ 1,4 ; 0,0694 à 0,0701 au δ 1,6), V finale 0,1244 et 0,0685, minimum sur les tours de l'attaquant léger 0,1226 et 0,0673 : l'attaquant lourd de la finale ne fait pas mieux que le meilleur des huit attaquants légers.

### 3.4 Recalcul indépendant des contrastes, des indicateurs et des bornes
Schéma du texte scellé : `SeedSequence(entropy=20266201, spawn_key=(code_delta, code, 0, 0, 99))`, code = 200 + 100 j + rang (j = 0 V, 1 (ii), 2 X finale, 8 X̄) et 500 + 100 j + rang (j = 0 I1, 1 I3 − nul, 2 I2), 20 000 tirages, quantiles linéaires aux dix niveaux. **Écart maximal entre mon recalcul et `analyse-regles-defense.json` : 0,0** (moyennes, écarts-types et dix quantiles des 16 contrastes et des 15 indicateurs, aux deux δ) ; `zeros_exacts` égaux (0 partout). Cela établit, sans lire l'arène v4 : la racine de rééchantillonnage employée (20266201), le rôle 99, les codes et les rangs, et la fonction de quantiles (`numpy.quantile`, interpolation linéaire).

Tables recopiées (classes gelées appliquées par mon script, première ligne vraie) — identiques à la lecture :

| Table | Variante | δ 1,4 : est [B8], classe | δ 1,6 : est [B8], classe |
|---|---|---|---|
| B (V) | R0 | +0,0024 [−0,0100 ; +0,0145] « ≈ » | +0,0037 [−0,0066 ; +0,0146] « ≈ » |
| B (V) | R1 | −0,0137 [−0,0275 ; −0,0012] « R2 ≳ R1 » | −0,0086 [−0,0210 ; +0,0036] « ? » |
| B (V) | R3 | +0,1045 [+0,0896 ; +0,1195] « R3 > R2 » | +0,1236 [+0,1117 ; +0,1349] « R3 > R2 » |
| B (V) | R4 | +0,0202 [+0,0102 ; +0,0331] « R4 ≳ R2 » | +0,0142 [+0,0064 ; +0,0240] « R4 ≳ R2 » |
| B′ (X̄) | R0 | −0,0062 [−0,0139 ; +0,0021] « ≈ » | −0,0066 [−0,0119 ; −0,0004] « ≈ » |
| B′ (X̄) | R1 | **+0,0262 [+0,0201 ; +0,0329] « R2 > R1 »** | **+0,0162 [+0,0115 ; +0,0214] « R2 ≳ R1 »** |
| B′ (X̄) | R3 | −0,0554 [−0,0621 ; −0,0483] « R3 > R2 » | −0,0664 [−0,0712 ; −0,0612] « R3 > R2 » |
| B′ (X̄) | R4 | −0,0208 [−0,0244 ; −0,0172] « R4 ≳ R2 » | −0,0178 [−0,0213 ; −0,0143] « R4 ≳ R2 » |

### 3.5 Artefacts cherchés qui expliqueraient la « propreté »
- **Fuite entre entraînement et épreuve** : par le code, les échantillons d'entraînement des attaques (rôle « attaques d'entraînement »), d'évaluation de (iii)_t (rôle « évaluation », par règle et par tour) et de la finale (rôle « final ») sont dérivés de rôles distincts du schéma de graines ; les lois tenues à l'écart viennent de la racine tenue seule et l'essai `test_tenues_jamais_vues_par_l_entrainement` (essais l. 428–464) instrumente tous les entraînements (R0 à R4). Dans les données : (ii)_1 **identique au bit pour les cinq règles** dans les 200 tâches (M0 et lois tenues communes, comme déclaré) ; (ii) de R0 constante. Je n'ai pas pu relire `phase_finale` ni `Contexte` de l'arène v4 (absente) ; la contre-lecture du module (C-09, C-10) l'a fait le 1er novembre et conclut « rien dans le code ne fabrique le « ≈ » de P13 ».
- **Variante dégénérée** : R0 est figée par définition (c'est le témoin) ; R4 : cosinus consécutif moyen 0,967 et 0,955, part des tâches ≥ 0,999 : 5 % et 2 % (S12 non déclenché) ; R1 : cosinus moyen 0,042 et −0,019 (moniteurs consécutifs quasi orthogonaux : signature de la période 2, pas une dégénérescence), X_t de R1 alterne 0,874 ; 0,931 ; 0,887 ; 0,928 ; 0,890 ; 0,926 ; 0,891 ; 0,925 (δ 1,4), moyenne des tours pairs > impairs dans 75 % et 82 % des tâches ; R3 : aucun poids pur, support moyen 3,5 et 3,6. Aucune variante n'est dégénérée au sens qui produirait P12 ou P13.
- **Égalité forcée** : `zeros_exacts` = 0 pour les 16 contrastes aux deux δ ; **aucune paire de règles n'a la même V finale ni la même X̄ dans aucune tâche** (0 coïncidence sur 2 000 paires) ; |Δ(R0, R2)| par tâche jusqu'à 0,157.
- **Graine partagée** : codes de graine distincts (R0 20, R1 21, R2 1, R3 2, R4 24) ; (iii)_1 (même défense M0, attaquants à graines différentes) coïncide exactement entre deux règles dans 15 paires sur 2 000 et entre R0 et R2 dans 2 tâches sur 200 — ordre de grandeur attendu pour des fractions sur 19 998 échantillons autour d'une même valeur (égalités de hasard), incompatible avec des graines partagées (qui donneraient 100 %).
- **Propriété de X̄ signalée par la contre-lecture du module (C-11)** : X̄ compte le tour 1, où toutes les règles déploient M0 ; D_1 vaut −0,0001 et −0,0000 (bruit d'espérance nulle) : tout contraste sur X̄ est **atténué d'un huitième** par construction, conformément à la définition scellée (gel v2 § 4). Ramené à 8/7, D̄(R1, R2) vaudrait +0,0299 et +0,0185, bornes basses ≈ +0,0230 et +0,0132 : les classes seraient inchangées (« R2 > R1 » plus nettement au δ 1,4 ; toujours « R2 ≳ R1 » au δ 1,6). Déclaré, pas un artefact ; la métrique scellée est celle qui compte.

### 3.6 P13 en profondeur : le « ≈ » de R0 contre R2 est-il trop propre ?
| Grandeur | δ 1,4 | δ 1,6 |
|---|---|---|
| Δ(R0, R2) sur V, erreur-type (sd/10) | +0,0024 ; 0,0044 | +0,0037 ; 0,0038 |
| écart réduit z = est / erreur-type ; P(\|Z\| ≤ z) sous effet nul | 0,54 ; 0,41 | 0,97 ; 0,67 |
| approximation normale de B8 (± 2,734 erreurs-types) | [−0,0096 ; +0,0143] | [−0,0068 ; +0,0142] |
| part des tâches où R0 fait mieux ; test du signe bilatéral | 53 % ; p = 0,62 | **62 % ; p = 0,021** |
| part des tâches à \|Δ\| > m ; max \|Δ\| | 36 % ; 0,157 | 23 % ; 0,156 |
| sd des différences ; sd de V(R0) ; sd de V(R2) ; corrélation de Pearson | 0,044 ; 0,080 ; 0,087 ; 0,87 | 0,038 ; 0,061 ; 0,065 ; 0,82 |
| moitiés d'instances 0–49 et 50–99 | +0,0098 ; −0,0051 | +0,0051 ; +0,0024 |
| contraste avec l'attaquant standard seul ; renforcé seul | +0,0026 ; +0,0022 | +0,0038 ; +0,0038 |
| classe sous cinq autres clés de rééchantillonnage (hors schéma, déclarées) | « ≈ » × 5 | « ≈ » × 5 |
| D̄(R0, R2) sur X̄ ; Δ(R0, R2) sur (ii) ; part des tâches où R0 fait mieux sur (ii) | −0,0062 ; +0,0516 ; 91 % | −0,0066 ; +0,0600 ; 97 % |

Lecture : l'estimation est à moins d'une erreur-type de zéro, ce qui sous effet nul arrive dans 41 % et 67 % des cas — **rien de « trop propre »** ; la classe « ≈ » est stable aux deux attaquants, aux deux moitiés d'instances et à la graine de rééchantillonnage, et portée par des différences par tâche réelles et de grande amplitude qui se compensent (corrélation forte entre règles : l'exploitabilité d'un hyperplan est d'abord une propriété de la tâche). Robustesse du verdict gelé : « R2 > R0 » (HR0 confirmée) exigerait une borne haute B8 < −0,02, à 7,9 erreurs-types de l'observé ; « ≈ » céderait la place à « ? » (HR0 non tranchée) au δ 1,4 si la borne haute E8 dépassait +0,02, à 1,5 erreur-type ; au δ 1,6, les deux classes voisines (« ? », « R0 ≳ R2 ») rendent aussi « réfutée ». **Observation à porter** : au δ 1,6, R0 fait mieux que R2 dans 62 % des tâches (test du signe p = 0,02), et sur les deux autres mesures R0 est, partout, un peu moins exploitable au fil des tours et nettement meilleure sur les lois tenues à l'écart : le « ≈ » n'est pas une identité des défenses mais un effet moyen sous la marge, légèrement penché vers le témoin.

### 3.7 P12 en profondeur : fragilité des classes, pas artefact
| Grandeur | δ 1,4 | δ 1,6 |
|---|---|---|
| D̄(R1, R2) sur X̄, erreur-type | +0,0262 ; 0,0024 | +0,0162 ; 0,0018 |
| borne basse B8 − m ; en erreurs-types | **+0,0001 ; +0,05** | −0,0085 ; −4,6 |
| borne haute E8 − m (frontière « ≳ » / « ≈ ») ; en erreurs-types | +0,0123 ; +5,2 | **+0,0010 ; +0,52** |
| approximation normale de B8 | [+0,0197 ; +0,0326] | [+0,0112 ; +0,0212] |
| borne basse B8 sous cinq autres clés (hors schéma) | 0,02009 à 0,02014 (toutes > m) | 0,01147 à 0,01158 |
| part des tâches à D̄ > 0 ; test du signe | 99 % ; p < 10⁻⁶ | 96 % ; p < 10⁻⁶ |
| D_t par tour (1 à 8) | −0,0001 ; +0,0462 ; +0,0090 ; +0,0404 ; +0,0097 ; +0,0457 ; +0,0089 ; +0,0496 | −0,0000 ; +0,0348 ; −0,0028 ; +0,0260 ; +0,0084 ; +0,0347 ; −0,0004 ; +0,0292 |
| tours pairs seuls ; impairs seuls (classe B′, même clé) | +0,0455 [+0,0324 ; +0,0598] « R2 > R1 » ; +0,0069 [−0,0026 ; +0,0183] « ≈ » | +0,0311 [+0,0215 ; +0,0422] « R2 > R1 » ; +0,0013 [−0,0069 ; +0,0101] « ≈ » |
| classe à T′ = 3, 4, 5, 6, 7, 8 (moyenne des T′ premiers tours) | ≳, ≳, ≳, ≳, **≳ (+0,0228 [+0,0172 ; +0,0290])**, > | **≈, ≈, ≈**, ≳, **≈ (+0,0144 [+0,0097 ; +0,0196])**, ≳ |
| classe selon m = 0,01 ; 0,015 ; 0,02 ; 0,025 | >, >, >, ≳ | >, ≳, ≳, ≈ |

Lecture : (a) le **signe** de P12 est robuste (D̄ > 0 dans 96 à 99 % des tâches, borne basse > 0 à tous les T′ ≥ 3, aux deux δ), porté par les tours pairs (période 2 de R1) ; X̄ est calculée comme le gel la définit et la clé 1001 ne heurte rien : **aucune erreur de code, aucun chemin non exercé**. (b) Le « ≳ » du δ 1,6 est la lecture honnête d'un effet réel (9 erreurs-types au-dessus de zéro) inférieur à la marge (4,6 erreurs-types sous m) — ni la parité de T, ni m, ni la graine ne le créent ; l'approximation normale le confirme. (c) **Fragilité, aux deux δ** : au δ 1,4 la classe forte tient à 0,05 erreur-type (l'approximation normale donne 0,0197 < m) et bascule en « ≳ » dès que l'on retire un tour ; au δ 1,6 la classe « R2 ≳ R1 » ne tient qu'à **0,5 erreur-type** de « ≈ » (borne haute E8 0,02096 contre m = 0,02) et bascule en « ≈ » à T′ = 7, 5, 4, 3. Conséquence sur le verdict gelé : HR2 est « non tranchée » (« R2 ≳ R1 » à un δ) et serait **« réfutée »** si la classe du δ 1,6 était « ≈ » ; elle ne peut être « confirmée » dans aucune lecture voisine (borne basse du δ 1,6 à 4,6 erreurs-types sous m). C'est une fragilité de lecture au voisinage de la marge, pas un artefact ; le texte scellé (S3) avait calculé une puissance ≈ 0 pour « R2 > R1 » à l'effet m exactement et ≈ 0,22 à 0,03 au δ 1,4.

### 3.8 Code d'analyse relu
`_boot` (l. 598–602) : rééchantillonnage apparié des instances, graine `gen_regles(racine, cd, code, 0, 0, ROLE_REECH)`, moyennes, écart-type ddof = 1, quantiles par la fonction de l'arène ; `resume_variante` (l. 605–631) : moyennes par variante, X̄ moyenne, `cos_consecutif_par_tache` (S12 au lecteur), `standard_moins_renforce`, coût ; `analyser_regles` (l. 651–684) : tâches triées par instance à δ fixé, variantes dans l'ordre d'insertion (R0 … R4 = rangs 0 … 4), contrastes contre R2 pour les quatre mesures (codes 200 + 100 j + rang, X̄ en j = 8 soit 1000 + rang, garde d'absence de collision l. 594), écart « standard seul / renforcé seul » (déclencheur 5), indicateurs (codes 500 + 100 j + rang), compteurs d'attaquant et d'entraînements. Aucun seuil ni classe n'est appliqué dans le code (le lecteur applique les tables). Rien à signaler ; mon recalcul à 0,0 en est la preuve par reproduction.

## 4. Vérification que graines et manifeste correspondent (résumé)
Racines de décision du manifeste et de chaque tâche = celles du texte scellé ; racine de rééchantillonnage = 20266201 (prouvée par la reproduction à 0,0) ; bloc `graines` du manifeste reconstruit à l'identique ; les deux fichiers de `diag/` rattachés au manifeste par son empreinte ; empreintes du code, de la configuration, du gel et de la bibliothèque du manifeste = texte scellé = disque. Les graines par tâche (`SeedSequence(20266201, (code_delta, instance, code_bras, tour, rôle))`) ne sont pas vérifiables sans rejeu ; leur schéma est écrit dans la configuration empreintée (`schema_graines`) et le remplacement de `gen` par `gen_regles` (l. 187–194) ne change que la liste des racines permises.

## 5. Script de recalcul, recopié en entier (`audit_r4_p12_p13_v1.py`, empreinte `281199b0…`, exécuté par `python -I` du dépôt, 1,3 s, code de retour 0, sortie `b695f5db…`)

```python
#!/usr/bin/env python3
"""audit_r4_p12_p13_v1.py — recalcul indépendant (numpy seul) pour l'audit de symétrie R4 sur P12 et P13 de la course
PREREG-REGLES-DEFENSE-V2 (lecteur neuf, 8 novembre 2026). Lecture seule : rien n'est écrit dans le dépôt.
Usage : python -I audit_r4_p12_p13_v1.py /chemin/du/depot [sortie.json]"""
import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

DEPOT = Path(sys.argv[1]).resolve()
RUN = "20261101-160323-regles-defense-convergence"
RES = DEPOT / "diag" / RUN / "resultats-regles-defense.json"
ANA = DEPOT / "diag" / RUN / "analyse-regles-defense.json"
MAN = DEPOT / "runs" / RUN / "manifeste.json"
RACINE, RACINE_TENUE, ROLE_REECH, N_REECH, M, ALPHA, T = 20266201, 20266202, 99, 20000, 0.02, 0.01, 8
NIVEAUX = (0.003125, 0.00625, 0.0125, 0.025, 0.05, 0.95, 0.975, 0.9875, 0.99375, 0.996875)
NOMS = ["R0", "R1", "R2", "R3", "R4[moyenne,λ=0.3]"]          # rangs 0 à 4 (texte scellé, § Métrique)
MESURES = (("V_iii_final", 0), ("ii_final", 1), ("exploitabilite_finale", 2), ("exploitabilite_moyenne_tours", 8))
INDICATEURS = (("I1_progres", 0), ("I3_moins_nul", 1), ("I2_oubli", 2))
Z_B8 = 2.734   # quantile normal 0,996875 (approximation normale de la borne B8, texte scellé S3)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def verifier_compagnon(p):
    attendu = Path(str(p) + ".sha256").read_text(encoding="utf-8").split()[0]
    calcule = sha(p)
    assert attendu == calcule, f"empreinte ≠ compagnon : {p}"
    return calcule


def boot(x, cd, code, cle=None):
    """Rééchantillonnage apparié des instances, schéma du texte scellé : SeedSequence(entropy=RACINE_DECISION,
    spawn_key=(code_delta, code, 0, 0, 99)) ; `cle` permet une clé de sensibilité hors schéma (déclarée)."""
    cle = (cd, code, 0, 0, ROLE_REECH) if cle is None else cle
    g = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=cle))
    b = x[g.integers(0, len(x), size=(N_REECH, len(x)))].mean(1)
    return {"moyenne": float(x.mean()), "ecart_type": float(x.std(ddof=1)), "n": int(len(x)),
            "quantiles": {f"q{n:g}": float(np.quantile(b, n)) for n in NIVEAUX}}


def bornes(q):
    return (q["q0.003125"], q["q0.996875"]), (q["q0.00625"], q["q0.99375"])   # B8, E8


def classe_B(q, m=M):
    """Table B (V) : Δ = V(R_k) − V(R2), + = R_k moins exploitable ; de haut en bas, la première ligne vraie décide."""
    b8, e8 = bornes(q)
    if b8[0] > m:
        return "R_k > R2"
    if b8[1] < -m:
        return "R2 > R_k"
    if e8[0] > -m and e8[1] < m:
        return "≈"
    if b8[0] > 0:
        return "R_k ≳ R2"
    if b8[1] < 0:
        return "R2 ≳ R_k"
    return "?"


def classe_Bp(q, m=M):
    """Table B′ (X̄) : D̄ = X̄(R_k) − X̄(R2), + = R_k PLUS exploitable ; même ordre de lecture."""
    b8, e8 = bornes(q)
    if b8[0] > m:
        return "R2 > R_k"
    if b8[1] < -m:
        return "R_k > R2"
    if e8[0] > -m and e8[1] < m:
        return "≈"
    if b8[0] > 0:
        return "R2 ≳ R_k"
    if b8[1] < 0:
        return "R_k ≳ R2"
    return "?"


def p_signe(k, n):
    """Test du signe exact, bilatéral : 2 × P(X ≤ min(k, n − k)) sous Binomiale(n, 1/2)."""
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(0, min(k, n - k) + 1)) / 2 ** n)


def r6(o):
    if isinstance(o, float):
        return round(o, 6)
    if isinstance(o, dict):
        return {str(k): r6(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [r6(v) for v in o]
    return o


def main():
    out = {"empreintes": {str(p.relative_to(DEPOT)): verifier_compagnon(p) for p in (RES, ANA, MAN)}}
    man = json.loads(MAN.read_text(encoding="utf-8"))
    res = json.loads(RES.read_text(encoding="utf-8"))
    ana = json.loads(ANA.read_text(encoding="utf-8"))
    taches, A = res["resultat"]["resultats"], ana["resultat"]

    # ---- 1. manifeste et identité des lignes -------------------------------------------------------------------
    c = man["config"]
    out["manifeste"] = {"racine": c["racine"], "racine_tenue": c["racine_tenue"], "lambda": c["lambda"],
                        "reference": c["reference"], "instances": c["instances"], "decisif": man["decisif"],
                        "reserves": man["reserves"], "prereg_sha256": c["prereg_sha256"],
                        "code_sha256": c["versions"]["code_sha256"], "config_sha256": c["config_sha256"],
                        "manifeste_sha256_dans_resultats": res["manifeste_sha256"],
                        "manifeste_sha256_dans_analyse": ana["manifeste_sha256"],
                        "run_id_resultats": res["run_id"], "run_id_analyse": ana["run_id"],
                        "graines": man["graines"], "temps": res["resultat"]["temps"]}
    assert (c["racine"], c["racine_tenue"]) == (RACINE, RACINE_TENUE)
    assert c["lambda"] == 0.3 and c["reference"] == "moyenne" and c["instances"] == "0:100"
    assert len(taches) == 200, len(taches)
    par_cd = {}
    for t in taches:
        assert t["racine"] == RACINE and t["racine_tenue"] == RACINE_TENUE, "racines d'une tâche ≠ décision"
        assert t["config_sha256"] == c["config_sha256"] and t["version"] == "arene_regles_defense_v2"
        assert list(t["regles"]) == NOMS, list(t["regles"])
        par_cd.setdefault(t["code_delta"], []).append(t)
    assert sorted(par_cd) == [1, 2]
    for cd, rs in par_cd.items():
        rs.sort(key=lambda r: r["instance"])
        assert [r["instance"] for r in rs] == list(range(100)), f"δ code {cd} : instances en doublon ou manquantes"
    out["identite_lignes"] = {"taches": len(taches), "par_delta": {cd: len(rs) for cd, rs in par_cd.items()},
                              "deltas": {cd: rs[0]["delta"] for cd, rs in par_cd.items()}}

    # ---- 2. cohérence interne, gardes, R0, graines partagées ---------------------------------------------------
    defauts, comptes = Counter(), Counter()
    for t in taches:
        for nom, v in t["regles"].items():
            pt = v["par_tour"]
            if len(pt["exploitabilite"]) != T or len(pt["iii"]) != T:
                defauts["nombre de tours ≠ 8"] += 1
            if np.max(np.abs(np.array(pt["exploitabilite"]) - (1 - np.array(pt["iii"])))) > 1e-12:
                defauts["X_t ≠ 1 − (iii)_t"] += 1
            if abs(v["exploitabilite_moyenne_tours"] - float(np.mean(pt["exploitabilite"]))) > 1e-12:
                defauts["X̄ ≠ moyenne des X_t"] += 1
            if v["exploitabilite_moyenne_tours"] in (0.0, 1.0):
                defauts["X̄ écrêtée à 0 ou 1"] += 1
            if abs(v["exploitabilite_finale"] - (1 - v["V_iii_final"])) > 1e-12:
                defauts["X finale ≠ 1 − V"] += 1
            if abs(v["V_iii_final"] - min(v["V_iii_standard"], v["V_iii_renforce"])) > 1e-12:
                defauts["V ≠ min(standard, renforcé)"] += 1
            if not (ALPHA - 0.005 <= v["fpr_final"] <= ALPHA + 0.005):
                defauts["fausses alertes hors α ± 0,005"] += 1
            ct, cf = v["cout_trajectoire"], v["cout_finale"]
            if nom == "R0":
                if ct["entrainements"] != 0 or cf["entrainements"] != 0:
                    defauts["R0 : entraînement compté"] += 1
                if v["nb_moniteurs_stockes"] != 1 or v["parametres_stockes"] != 7 or v["parametres_deployes"] != 7:
                    defauts["R0 : stockage ≠ (1 moniteur, 7, 7)"] += 1
                if pt["cos_consecutif"] != [1.0] * T or v["poids_finaux"] != [1.0]:
                    defauts["R0 : cosinus ou poids ≠ 1"] += 1
                H = np.array(v["cycle"]["H"])
                if H.shape != (T + 1, T) or np.any(H != H[0]):
                    defauts["R0 : lignes de H non identiques"] += 1
                if v["cycle"]["I2_oubli"] != 0.0:
                    defauts["R0 : I2 ≠ 0"] += 1
                if np.ptp(pt["ii"]) > 1e-12 or abs(pt["ii"][0] - v["ii_final"]) > 1e-12:
                    defauts["R0 : (ii) non constante"] += 1
                if ct["appels_optimiseur"] != ct["departs_attaquant"] or cf["appels_optimiseur"] != cf["departs_attaquant"]:
                    defauts["R0 : appels à l'optimiseur ≠ départs (entraînement caché ?)"] += 1
                if ct["programmes_lineaires"] != 0 or cf["programmes_lineaires"] != 0:
                    defauts["R0 : programme linéaire"] += 1
            else:
                if ct["entrainements"] != T or cf["entrainements"] != 0:
                    defauts[f"{nom} : entraînements ≠ (8, 0)"] += 1
                if v["nb_moniteurs_stockes"] != T + 1 or v["parametres_stockes"] != 7 * (T + 1):
                    defauts[f"{nom} : stockage ≠ (9 moniteurs, 63)"] += 1
                if v["parametres_deployes"] != (63 if nom == "R3" else 7):
                    defauts[f"{nom} : paramètres déployés"] += 1
        if t["entrainements"] != 2 + 4 * T or t["non_convergences"] != 0:
            defauts["tâche : entraînements ≠ 34 ou non convergence"] += 1
        a = t["attaquant"]
        if a["non_finis"] != 0 or a["reponses_a_la_limite"] != 0 or set(a["statuts"]) != {"0"}:
            defauts["attaquant : départ non fini, limite ou statut ≠ 0"] += 1
        vs = list(t["regles"].values())
        if len({v["par_tour"]["ii"][0] for v in vs}) != 1:
            defauts["(ii)_1 différente entre règles (M0 commun attendu)"] += 1
        comptes["coïncidences exactes de (iii)_1 entre deux règles"] += 5 - len({v["par_tour"]["iii"][0] for v in vs})
        comptes["coïncidences exactes de V finale entre deux règles"] += 5 - len({v["V_iii_final"] for v in vs})
        comptes["coïncidences exactes de X̄ entre deux règles"] += 5 - len({v["exploitabilite_moyenne_tours"] for v in vs})
        comptes["tâches où (iii)_1(R0) = (iii)_1(R2)"] += int(t["regles"]["R0"]["par_tour"]["iii"][0] == t["regles"]["R2"]["par_tour"]["iii"][0])
    out["defauts"] = dict(defauts)
    out["comptes"] = dict(comptes)

    # ---- 3. recalcul des contrastes et des indicateurs, écart au fichier d'analyse -----------------------------
    ecart_max, tables = 0.0, {}
    for cd, rs in sorted(par_cd.items()):
        bloc, tables[cd] = A[str(cd)], {}
        for k, nom in enumerate(NOMS):
            if nom != "R2":
                for mes, j in MESURES:
                    d = np.array([r["regles"][nom][mes] - r["regles"]["R2"][mes] for r in rs])
                    b = boot(d, cd, 200 + 100 * j + k)
                    ref = bloc["contrastes_contre_R2"][f"{nom} - R2 ({mes})"]
                    ecart_max = max(ecart_max, abs(b["moyenne"] - ref["moyenne"]), abs(b["ecart_type"] - ref["ecart_type"]),
                                    max(abs(b["quantiles"][q] - ref["quantiles"][q]) for q in b["quantiles"]))
                    assert int(np.sum(d == 0)) == ref["zeros_exacts"]
                    tables[cd][(nom, mes)] = (b, d)
            for mes, j in INDICATEURS:
                x = np.array([r["regles"][nom]["cycle"][mes] for r in rs], float)
                b = boot(x, cd, 500 + 100 * j + k)
                ref = bloc["indicateurs"][f"{nom} {mes}"]
                ecart_max = max(ecart_max, abs(b["moyenne"] - ref["moyenne"]),
                                max(abs(b["quantiles"][q] - ref["quantiles"][q]) for q in b["quantiles"]))
    out["ecart_max_recalcul_vs_analyse"] = ecart_max

    # ---- 4. Tables B et B′ recopiées (classes gelées) ----------------------------------------------------------
    out["table_B"], out["table_Bp"] = {}, {}
    for cd in sorted(par_cd):
        for nom in NOMS:
            if nom == "R2":
                continue
            b, _ = tables[cd][(nom, "V_iii_final")]
            out["table_B"][f"{nom} δ{cd}"] = {"est": b["moyenne"], "B8": bornes(b["quantiles"])[0],
                                              "E8": bornes(b["quantiles"])[1], "classe": classe_B(b["quantiles"])}
            b, _ = tables[cd][(nom, "exploitabilite_moyenne_tours")]
            out["table_Bp"][f"{nom} δ{cd}"] = {"est": b["moyenne"], "B8": bornes(b["quantiles"])[0],
                                               "E8": bornes(b["quantiles"])[1], "classe": classe_Bp(b["quantiles"])}

    # ---- 5. P13 : Δ(R0, R2) sur V, en profondeur ---------------------------------------------------------------
    out["P13"] = {}
    for cd, rs in sorted(par_cd.items()):
        b, d = tables[cd][("R0", "V_iii_final")]
        v0 = np.array([r["regles"]["R0"]["V_iii_final"] for r in rs])
        v2 = np.array([r["regles"]["R2"]["V_iii_final"] for r in rs])
        se, k_pos = d.std(ddof=1) / math.sqrt(len(d)), int(np.sum(d > 0))
        iii0 = np.array([r["regles"]["R0"]["par_tour"]["iii"] for r in rs])
        out["P13"][f"δ{cd}"] = {
            "est": b["moyenne"], "B8": bornes(b["quantiles"])[0], "E8": bornes(b["quantiles"])[1],
            "classe": classe_B(b["quantiles"]), "erreur_type": se, "z = est/erreur_type": b["moyenne"] / se,
            "normale_B8": (b["moyenne"] - Z_B8 * se, b["moyenne"] + Z_B8 * se),
            "part_taches_R0_meilleure": k_pos / len(d), "p_test_du_signe": p_signe(k_pos, len(d)),
            "zeros_exacts": int(np.sum(d == 0)), "max_abs_Δ_par_tache": float(np.max(np.abs(d))),
            "part_taches_|Δ|>m": float(np.mean(np.abs(d) > M)), "sd_Δ": float(d.std(ddof=1)),
            "sd_V_R0": float(v0.std(ddof=1)), "sd_V_R2": float(v2.std(ddof=1)),
            "corr_pearson_V(R0),V(R2)": float(np.corrcoef(v0, v2)[0, 1]),
            "V_moyen_R0": float(v0.mean()), "V_moyen_R2": float(v2.mean()),
            "moitie_instances_0_49": float(d[:50].mean()), "moitie_instances_50_99": float(d[50:].mean()),
            "contraste_standard_seul": float(np.mean([r["regles"]["R0"]["V_iii_standard"] - r["regles"]["R2"]["V_iii_standard"] for r in rs])),
            "contraste_renforce_seul": float(np.mean([r["regles"]["R0"]["V_iii_renforce"] - r["regles"]["R2"]["V_iii_renforce"] for r in rs])),
            "classes_5_autres_cles_reech": [classe_B(boot(d, cd, 200, cle=(cd, 200, 7, j, ROLE_REECH))["quantiles"]) for j in range(1, 6)],
            "iii_t_R0_moyen_par_tour": [float(x) for x in iii0.mean(0)],
            "min_sur_les_tours_de_iii_R0_moyen": float(iii0.min(1).mean()),
            "D̄(R0,R2) sur X̄": tables[cd][("R0", "exploitabilite_moyenne_tours")][0]["moyenne"],
            "Δ(R0,R2) sur (ii)": tables[cd][("R0", "ii_final")][0]["moyenne"],
            "part_taches_R0_meilleure_sur_(ii)": float(np.mean(tables[cd][("R0", "ii_final")][1] > 0))}

    # ---- 6. P12 : D̄(R1, R2) sur X̄, en profondeur --------------------------------------------------------------
    out["P12"] = {}
    for cd, rs in sorted(par_cd.items()):
        b, d = tables[cd][("R1", "exploitabilite_moyenne_tours")]
        X1 = np.array([r["regles"]["R1"]["par_tour"]["exploitabilite"] for r in rs])
        X2 = np.array([r["regles"]["R2"]["par_tour"]["exploitabilite"] for r in rs])
        D = X1 - X2
        assert np.max(np.abs(D.mean(1) - d)) < 1e-12
        se = d.std(ddof=1) / math.sqrt(len(d))

        def sous(cols):
            dd = D[:, cols].mean(1)
            bb = boot(dd, cd, 1001)          # même clé que la course (sensibilité, hors décision)
            return {"est": float(dd.mean()), "B8": bornes(bb["quantiles"])[0], "classe": classe_Bp(bb["quantiles"])}

        b8 = bornes(b["quantiles"])[0]
        out["P12"][f"δ{cd}"] = {
            "est": b["moyenne"], "B8": b8, "E8": bornes(b["quantiles"])[1], "classe": classe_Bp(b["quantiles"]),
            "erreur_type": se, "borne_basse_B8_moins_m": b8[0] - M, "(borne_basse_B8 − m)/erreur_type": (b8[0] - M) / se,
            "normale_B8": (b["moyenne"] - Z_B8 * se, b["moyenne"] + Z_B8 * se),
            "part_taches_D̄>0": float(np.mean(d > 0)), "p_test_du_signe": p_signe(int(np.sum(d > 0)), len(d)),
            "D_t_moyen_par_tour": [float(x) for x in D.mean(0)],
            "tours_pairs": sous([1, 3, 5, 7]), "tours_impairs": sous([0, 2, 4, 6]),
            "T_prime": {Tp: sous(list(range(Tp))) for Tp in range(3, T + 1)},
            "classe_selon_m": {str(mm): classe_Bp(b["quantiles"], mm) for mm in (0.01, 0.015, 0.02, 0.025)},
            "borne_basse_B8_5_autres_cles": [bornes(boot(d, cd, 1001, cle=(cd, 1001, 7, j, ROLE_REECH))["quantiles"])[0][0] for j in range(1, 6)],
            "part_taches_R1_periode_2 (X pairs > X impairs)": float(np.mean(X1[:, 1::2].mean(1) > X1[:, 0::2].mean(1))),
            "X̄_moyen_R1": float(X1.mean()), "X̄_moyen_R2": float(X2.mean()),
            "X_t_R1_moyen_par_tour": [float(x) for x in X1.mean(0)],
            "Δ(R1,R2) sur V (Table B, recopié)": out["table_B"][f"R1 δ{cd}"]}

    out["defauts_total"] = int(sum(defauts.values()))
    texte = json.dumps(r6(out), ensure_ascii=False, indent=1)
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(texte, encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    main()
```

Compléments calculés à part (une ligne de Python chacun, sans script versé) : `zeros_exacts` = 0 pour les 16 contrastes de chaque δ ; probabilités normales P(|Z| ≤ 0,542) = 0,412 et P(|Z| ≤ 0,969) = 0,668 ; quantile normal 0,996875 = 2,7344 ; bloc `graines` du manifeste reconstruit (§ 3.1) ; cosinus consécutifs moyens par règle (§ 3.5).

## 6. Conclusion, dans les termes du texte scellé

**Issue de l'audit : « pas d'artefact », pour P13 et pour P12.** Aucune erreur de code ni chemin non exercé n'a été trouvé : R0 ne réentraîne jamais et déploie M0 (code, garde d'identité d'objet, essai sain et artefact, compteurs à zéro sur 200 tâches, appels à l'optimiseur égaux aux départs de l'attaquant) ; X̄ est calculée comme le gel la définit ; les contrastes et les bornes se reproduisent à 0,0 par un script indépendant ; aucune égalité forcée, aucune graine partagée, aucune fuite visible dans les données ; graines et manifeste conformes ; identité des lignes vérifiée. Les deux contradictions de prédiction ferme sont des résultats réels : un effet nul à la marge m (P13) et un effet positif inférieur à la marge au δ 1,6 (P12), tous deux anticipés comme possibles par le texte lui-même (indice contraire du pilote pour HR0 ; puissance ≈ 0 à l'effet m pour « R2 > R1 »).

**Conséquence mécanique** : les Tables B et B′ **se lisent** ; les verdicts conditionnels de la lecture deviennent recopiables tels quels — **HR0 réfutée** (« ≈ » aux deux δ), **HR3 confirmée** (« R4 ≳ R2 » aux deux δ, S12 non déclenché), **HR2 non tranchée** (« R2 > R1 » au δ 1,4, « R2 ≳ R1 » au δ 1,6). Le prononcé revient au lecteur R13 et à la session mère ; ce fichier ne décide rien.

**Réserves R4 à porter avec ces verdicts** (un résultat trop propre ou trop fragile, dans un sens ou l'autre, reste une réserve ; aucune ne bloque la lecture au sens du texte, qui ne connaît que « artefact trouvé / pas d'artefact ») :
1. **P12 est fragile aux deux δ** : « R2 > R1 » au δ 1,4 tient à 0,05 erreur-type de m et bascule en « ≳ » dès T′ ≤ 7 ; « R2 ≳ R1 » au δ 1,6 tient à 0,5 erreur-type de « ≈ » et bascule en « ≈ » à T′ = 7, 5, 4, 3 — la frontière entre HR2 « non tranchée » et HR2 « réfutée » passe à une demi-erreur-type de l'observé. HR2 ne peut être « confirmée » dans aucune lecture voisine.
2. **P13** : le « ≈ » est une compensation entre tâches (|Δ| > m dans 36 % et 23 % des tâches, jusqu'à 0,157), légèrement penchée vers le témoin au δ 1,6 (R0 meilleure dans 62 % des tâches, test du signe p = 0,02) ; HR0 « réfutée » est robuste (« confirmée » à 7,9 erreurs-types), mais « réfutée par ≈ » ne signifie pas « défenses identiques ».
3. **Arène v4 absente de cette copie de travail** : son empreinte n'a pas été recalculée par moi (épinglée et vérifiée au chargement par le code, égale dans le manifeste et le texte, recalculée égale le 1er novembre) ; les rejeux de la note du 1er novembre et les essais `pytest` du module ne peuvent pas être relancés ici.
4. **Les scripts de la note du 1er novembre ne sont pas versés** ; ses chiffres sur P12 et P13 sont reproduits ici par un script recopié en entier.
5. **Deux racines d'essai réservées (20266401, 20266521) ont été employées** par la note du 1er novembre, alors que le gel v2 § 1 les dit « non employées » : à consigner dans les registres par la session mère.
6. **X̄ compte le tour 1 commun** (atténuation d'un huitième des contrastes, conforme au gel, déclarée par la contre-lecture du module) : sans effet sur les classes ; à écrire près de la Table B′ si elle est publiée.
7. **Portée du déclencheur 1 sur P5 et P14** (lecture, § 10 point 5) : hors de cet audit (P12 et P13 seuls), toujours au directeur.

## 7. Ce que ce lecteur n'a pas fait
- Aucune course rejouée, aucune graine de décision ni d'essai tirée ; aucun essai `pytest` lancé (arène v4 absente de la copie de travail) ; aucune lecture de l'arène v4 (absente) : les points qui en dépendent (`phase_finale`, `Contexte.entrainer`, `taux_tenues`, `_q`) reposent sur la note du 1er novembre, sur la contre-lecture du module et sur la reproduction à 0,0 du fichier d'analyse.
- Aucun verdict d'hypothèse prononcé ; aucune recommandation ; aucun fichier existant modifié ; aucun `.sha256`, aucun commit.
