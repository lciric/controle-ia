# Lecture préenregistrée de la course de convergence — quatre règles de mise à jour de la défense et témoin figé (PREREG-REGLES-DEFENSE-V2) — v1

## En-tête

- Lecteur : sous-agent neuf (modèle Claude Fable 5.1, `claude-fable-5-1`), qui n'a écrit ni le préenregistrement, ni le code, ni les contre-lectures, ni le gel ; il ne décide rien, ne recommande rien, ne modifie aucun fichier existant, ne scelle rien, ne commet rien. Aucun appel payant, aucun réseau. Rien lu sous `donnees/` (une réserve, § 8).
- Date relevée par `date -u` avant écriture : **1er novembre 2026, 16:36:02 UTC** (première lecture des fichiers à 16:32:23 UTC).
- Empreintes SHA-256 recalculées par le lecteur (`sha256sum`), toutes conformes aux fichiers compagnons `.sha256` (`controle_ia.scellement verifier` : six « OK ») :
  - préenregistrement scellé `prereg/preregistrement-regles-defense-convergence-v1.md` — `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` ;
  - `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` — `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b` ;
  - `diag/20261101-160323-regles-defense-convergence/analyse-regles-defense.json` — `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` ;
  - `runs/20261101-160323-regles-defense-convergence/manifeste.json` — `36db58cfac9bfc4cf199ca5cdf74ac17ea24afab84b95ffd0aac945b922a6720` ; `pids-travail.txt` — `767aa28fb8cee94a1a130c151d7ed4487985d8f4fb2efdcd7ab805efc59e4bcd` ;
  - code `docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v2.py` — `9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3` ;
  - gel v2 sur disque `gel-regles-defense-v2.md` — `9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3` (CL-08, vérifié par le lecteur) ;
  - bibliothèque sur disque : `gardes.py` `a83c48ce…`, `prereg.py` `3b2e3ee5…`, `scellement.py` `93beeb1c…`, `manifeste.py` `1a5c7464…` (conformes au bloc d'identité).
- Méthode : lecture du texte scellé (sections « Plan d'analyse », « Critères de lecture gelés », Tables A à E, « Liste d'arrêt ») ; lecture du manifeste et des deux fichiers JSON ; lecture du code pour les champs et la méthode d'analyse (`analyser_regles`, `_boot`, `resume_variante`) ; **recalcul indépendant** des contrastes appariés, des indicateurs et des bornes de rééchantillonnage depuis `resultats-regles-defense.json` avec `numpy` seul (script dans le dossier de travail temporaire du lecteur, non versé au dépôt), graines `SeedSequence(entropy=20266201, spawn_key=(code_delta, code, 0, 0, 99))`, code = 200 + 100 × j + rang pour les contrastes (j = 0 V, 1 (ii), 2 X finale, 8 X̄) et 500 + 100 × j + rang pour les indicateurs (j = 0 I1, 1 I3 − nul, 2 I2), rangs R0 0, R1 1, R2 2, R3 3, R4 4, 20 000 tirages, quantiles linéaires de `numpy.quantile` aux niveaux 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques, exactement comme le § Métrique du texte scellé.
- **Écart entre le recalcul et `analyse-regles-defense.json` : 0,0** (écart maximal en valeur absolue sur toutes les moyennes et tous les quantiles de tous les contrastes et indicateurs, aux deux δ). Les chiffres ci-dessous sont donc ceux du recalcul et du fichier d'analyse, identiques.

Notations : δ 1,4 (code 1) ; δ 1,6 (code 2) ; est = moyenne sur les 100 instances ; B2 = [q0,00625 ; q0,99375] ; B8 = [q0,003125 ; q0,996875] ; E8 = [q0,00625 ; q0,99375] ; m = S1 = 0,02 ; S5 = 0,02 ; S15 = 0,02 ; α = 0,01. Δ sur V et sur (ii) : + = la variante détecte mieux ; D̄ sur X̄ : + = la variante est plus exploitable. R4 désigne partout R4[moyenne, λ = 0,3].

## 1. Plomberie : V0 et conformité du manifeste au préenregistrement

| Élément de V0 | Attendu (texte scellé) | Observé | Conforme |
|---|---|---|---|
| Racines | 20266201 ; 20266202 | manifeste `racine` 20266201, `racine_tenue` 20266202 ; chaque tâche des résultats porte ces deux racines (200 sur 200) | oui |
| N par δ ; tâches | N = 100 ; 2 × N = 200 | `n_instances` 100, `--instances 0:100`, `temps.taches` = 200 ; 100 instances 0 à 99 à chaque δ, sans doublon | oui |
| T ; δ ; α ; oracle | T = 8 ; (1,4 ; 1,6) ; 0,01 ; « detection » | identiques dans `config` | oui |
| λ* et référence | 0,3 ; « moyenne » | commande `--lambda 0.3 --reference moyenne` ; manifeste `lambda` 0.3, `reference` « moyenne » ; chaque tâche : R4 `lam` 0,3, `reference` « moyenne » | oui |
| Cinq variantes par tâche | R0, R1, R2, R3, R4 | `['R0', 'R1', 'R2', 'R3', 'R4[moyenne,λ=0.3]']` dans les 200 tâches | oui |
| Empreinte du code | `9f0dcf5e…` | `versions.code_sha256` `9f0dcf5e…` ; recalculée sur disque : identique | oui |
| Arène v4 | `70c77fd5…` | `versions.arene_v4_sha256` `70c77fd5…` (non recalculée : fichier sous `donnees/`, non lu) | oui (manifeste) |
| Gel v2 | `9977d7df…` | `gel_sha256` `9977d7df…` (deux fois dans le manifeste) ; recalculée sur disque : identique | oui |
| Configuration | `3fbb27fc…` | `config_sha256` `3fbb27fc…` dans `config` et dans chaque tâche | oui |
| Bibliothèque | quatre empreintes du bloc d'identité | `bibliotheque_sha256` identiques ; recalculées sur disque : identiques | oui |
| Versions | numpy 2.4.6 ; scipy 1.17.1 ; Python 3.13.18 | identiques | oui |
| Préenregistrement cité | scellé, `d82dea33…` | `preenregistrement.sha256` `d82dea33…`, `prereg_sha256` idem ; `decisif: true` | oui |
| Une seule invocation ayant écrit des résultats | au plus une reprise complète consignée | un seul dossier `diag/…regles-defense-convergence` et un seul `runs/…` ; `commande` conforme au § Plan 5 (mode `decision`, `--processus 2`, `--run-id` au format) ; `depot_propre: true` ; `reserves: []` ; `registres/decisions.md` R-967 : deux lancements arrêtés par garde **avant tout calcul** (identifiant hors format, arbre non propre), troisième passé ; commit du run `51097e83` « non lu » | oui |
| Commit | code au commit `ed3377bd` (texte) | manifeste `commit` `1dc492ba…` (commit qui ajoute le préenregistrement scellé, 16:02:05 UTC) ; le code y est à l'empreinte `9f0dcf5e…` : conforme (le texte épingle l'empreinte du code, pas le commit du run) | oui |

Remarque de forme : le manifeste porte un `config_sha256` de premier niveau (`c390479a…`) différent de celui du bloc d'identité ; c'est l'empreinte du bloc `config` complet du manifeste (configuration plus racines, λ, référence, versions), produite par la bibliothèque `manifeste.py` ; l'empreinte de la configuration canonique (`config.config_sha256`) est bien `3fbb27fc…`.

**Gardes et liste d'arrêt** (sur les 200 tâches, recalculé par le lecteur depuis les résultats bruts) :
- entraînements non convergés : 0 (sur 3 400 par δ, 6 800 en tout) ; départs de l'attaquant non finis : 0 sur 63 500 par δ (127 000 en tout) ; réponses à la limite : 0 ; statuts de l'optimiseur : uniquement `0` dans chaque tâche ;
- temps processeur par tâche : moyenne 15,9 s (δ 1,4) et 17,4 s (δ 1,6), maximum 19,3 s et 20,9 s, loin du plafond de 600 s ; mur total 1 692,7 s (≈ 28,2 min) sur 2 processus, sous `timeout 3600` ; somme des temps de tâche 3 327 s (≈ 55,5 min) ; cohérent avec la projection du § Plan 5 (17,3 s par tâche, ≈ 30 min de mur) ;
- fausses alertes des défenses finales : aucune hors de α ± 0,005 (0 sur 1 000 défenses) ;
- R0 : zéro entraînement dans la trajectoire et dans la finale de chacune des 200 tâches (compteur), 7 paramètres stockés, 1 moniteur stocké (M0) ; R1 à R4 : 8 entraînements par tâche, 9 moniteurs stockés, 63 paramètres stockés ; déployés : 7 pour R0, R1, R2, R4, 63 pour R3 — conforme au § Métrique (CL-09) ;
- R3 : programmes linéaires résolus (35 par tâche), aucun poids pur ;
- aucune condition de la liste d'arrêt n'apparaît déclenchée dans les fichiers ; les PID consignés (5753, 5754) et leur empreinte sont conformes ; `reserves: []`.

Condition de lancement S8 (charge relevée par `uptime` avant lancement et consignée) : le lecteur n'a pas trouvé de relevé `uptime` dans `registres/decisions.md` (R-967) ni dans les passations ; ce n'est pas un élément de V0 (voir § 8).

**V0 : vraie.**

## 2. Déclencheurs d'audit (R4), appliqués tels quels

| # | Déclencheur | Observé | Déclenché | Effet bloquant |
|---|---|---|---|---|
| 1 | P1 : Table A ligne 5 ou 6 à un δ | ligne 4 aux deux δ (§ 3) | non | — |
| 1 | P12 : Table B′, classe autre que « R2 > R1 » à un δ | δ 1,4 : « R2 > R1 » ; δ 1,6 : « R2 ≳ R1 » (§ 5) | **oui (δ 1,6)** | **bloque la Table B′** |
| 1 | P13 : Table B, classe autre que « R2 > R0 » à un δ, y compris « ≈ » | « ≈ » aux deux δ (§ 4) | **oui (deux δ)** | **bloque la Table B** ; l'audit prévu est une relecture du code de R0 et du compteur d'entraînements |
| 1 | P7 : Table D autre que ligne 2 à un δ | ligne 2 aux deux δ (§ 7) | non | — |
| 1 | P11 : \|moyenne des fausses alertes − α\| ≤ 0,001 par règle | écarts maximaux 0,00019 (δ 1,4, R3) et 0,00016 (δ 1,6, R1, R3, R4) | non | — |
| 2 | S10 trop beau / trop mauvais : V moyenne ≥ 0,99 ; V ≤ 2α pour les cinq variantes ; Δ(R3, R2) > 0,30 ; \|D̄\| > 0,30 | V moyennes entre 0,056 et 0,227 ; Δ(R3, R2) 0,104 et 0,124 ; \|D̄\| maximal 0,066 | non | — |
| 3 | R3 : poids purs (≥ 1 − 10⁻⁹) sur plus de la moitié des tâches d'un δ | part pure 0,00 aux deux δ ; support moyen 3,5 et 3,58 | non | — |
| 4 | S12 : cosinus consécutif moyen de R4 ≥ 0,999 sur plus de la moitié des tâches d'un δ | part des tâches à cosinus ≥ 0,999 : **5 sur 100** (δ 1,4) et **2 sur 100** (δ 1,6) ; cosinus moyen 0,967 et 0,955 | non | — |
| 5 | optimiseur : (V standard − V renforcé) > 0,01 pour une variante ; ou écart « standard seul − renforcé seul » d'un contraste de la Table B > 0,01 en valeur absolue | maximum 0,00039 (R0, δ 1,4) ; écarts des contrastes : maximum 0,00043 (R4, δ 1,4) | non | — |
| 6 | dérive des fausses alertes > 0,001 | voir P11 | non | — |
| 7 | conforme et trop propre : (P1, P12 et P13 conformes aux deux δ et P7 conforme) ou P5 conforme | P12 non conforme au δ 1,6, P13 non conforme ; P5 (régression de R1 sur (ii)) : non conforme, l'inverse est observé (§ 6) | non | — |

Deux déclenchements, tous deux du déclencheur 1 : **la Table B′ est bloquée (P12) et la Table B est bloquée (P13)** tant que l'audit n'est pas rendu. Les Tables A, C, D et E ne sont bloquées par rien. Conformément au § Critères (« les classes sont toujours recopiées, avec est [B8] »), les classes des Tables B et B′ sont recopiées ci-dessous ; les verdicts de HR0, HR3 (Table B) et HR2 (Table B′) sont **suspendus** ; le lecteur indique, à part, ce que la règle gelée rendrait si l'audit concluait « pas d'artefact », sans en faire un verdict.

## 3. Table A — plomberie et HR1 : Δ(R3, R2) sur V, bornes B2

| δ | est | B2 | est ≥ S1 | borne basse B2 > 0 |
|---|---|---|---|---|
| 1,4 | +0,1045 | [+0,0906 ; +0,1185] | oui | oui |
| 1,6 | +0,1236 | [+0,1127 ; +0,1341] | oui | oui |

Lecture de haut en bas : ligne 0 (V0 fausse) : non ; ligne 1 (déclencheur bloquant la Table A, audit non rendu) : aucun déclencheur ne bloque la Table A ; ligne 2 : sans objet ; ligne 3 (V ≤ 2α pour les cinq variantes) : non (V moyennes 0,124 ; 0,108 ; 0,122 ; 0,227 ; 0,142 au δ 1,4 et 0,069 ; 0,056 ; 0,065 ; 0,188 ; 0,079 au δ 1,6) ; **ligne 4 vraie aux deux δ**.

**HR1 : confirmée** (le mélange d'équilibre bat l'historique). P1 : classe prédite « ligne 4 », ordre de grandeur ≥ +0,05 (contexte v4 ≈ +0,13) : observé +0,10 et +0,12, conforme.

## 4. Table B — classement sur V contre R2, à chaque δ (B8, E8, m = 0,02) — **table bloquée par le déclencheur 1 (P13), classes recopiées**

| Variante | δ | est | B8 | E8 | Classe gelée |
|---|---|---|---|---|---|
| R0 | 1,4 | +0,0024 | [−0,0100 ; +0,0145] | [−0,0088 ; +0,0134] | « ≈ » (E8 ⊂ ]−0,02 ; +0,02[) |
| R0 | 1,6 | +0,0037 | [−0,0066 ; +0,0146] | [−0,0056 ; +0,0133] | « ≈ » |
| R1 | 1,4 | −0,0137 | [−0,0275 ; −0,0012] | [−0,0263 ; −0,0022] | « R2 ≳ R1 » (borne haute B8 < 0 ; E8 non contenu dans ]−m ; m[ : −0,0263 < −0,02) |
| R1 | 1,6 | −0,0086 | [−0,0210 ; +0,0036] | [−0,0200 ; +0,0026] | « ? » (E8 bas −0,02005 < −0,02 ; B8 chevauche 0) |
| R3 | 1,4 | +0,1045 | [+0,0896 ; +0,1195] | [+0,0906 ; +0,1185] | « R3 > R2 » |
| R3 | 1,6 | +0,1236 | [+0,1117 ; +0,1349] | [+0,1127 ; +0,1341] | « R3 > R2 » |
| R4 | 1,4 | +0,0202 | [+0,0102 ; +0,0331] | [+0,0109 ; +0,0318] | « R4 ≳ R2 » (borne basse B8 0,0102 < m ; > 0) |
| R4 | 1,6 | +0,0142 | [+0,0064 ; +0,0240] | [+0,0069 ; +0,0231] | « R4 ≳ R2 » |

Vérification de l'ordre des lignes de la table gelée pour R0 : « R0 > R2 » (borne basse B8 > m) : non ; « R2 > R0 » (borne haute B8 < −m) : non ; « ≈ » (E8 ⊂ ]−m ; +m[) : oui aux deux δ. Pour R4 : « R4 > R2 » non (0,0102 et 0,0064 < 0,02) ; « R2 > R4 » non ; « ≈ » non (bornes hautes E8 0,0318 et 0,0231 > m) ; « R4 ≳ R2 » oui.

- **HR0 (R2 moins exploitable que R0 d'un effet d'intérêt) : verdict suspendu, audit en attente** (déclencheur 1, P13 : classe autre que « R2 > R0 » aux deux δ ; le texte gelé prévoyait précisément le cas « ≈ » et fixe l'audit à une relecture du code de R0 et du compteur d'entraînements). Ce que la règle gelée rend si l'audit conclut « pas d'artefact » : « ≈ » à un δ ⇒ **HR0 réfutée** (ici aux deux δ). Le texte scellé déclare que cette issue « serait attendue au vu du pilote et n'est pas une surprise » (§ Hypothèse, HR0). Information pour l'audit, tirée des fichiers : R0 compte 0 entraînement dans les 200 tâches (trajectoire et finale), 7 paramètres stockés, 1 moniteur stocké ; I2 de R0 = 0 exactement ; (ii) de R0 constant sur les huit tours (défense figée), (iii)_t de R0 entre 0,1256 et 0,1263 au δ 1,4.
- **HR3 (R4(λ*) pas plus exploitable que R2) : verdict suspendu, audit en attente** (la Table B est bloquée par le déclencheur 1 sur P13 ; S12 non déclenché, § 2). Ce que la règle gelée rend si l'audit conclut « pas d'artefact » : classes « R4 ≳ R2 » aux deux δ, S12 non déclenché ⇒ **HR3 confirmée**. P3 : signe ≥ 0, ordre de grandeur [0 ; +0,05], classe « R4 ≳ R2 » ou « ≈ » : observé +0,020 et +0,014, « R4 ≳ R2 » : conforme à la prédiction.
- **R1 : classe recopiée sans verdict** (P2 descriptive, CL-05) : « R2 ≳ R1 » au δ 1,4 (−0,0137), « ? » au δ 1,6 (−0,0086) ; signe − aux deux δ, ordre de grandeur prédit ≈ 0 à −0,02 : dans la bande. Rappel du texte : X finale de R1 lit la phase du cycle à la parité de T près (T = 8, pair) ; la trajectoire moyenne de X_t de R1 au δ 1,4 alterne bien 0,874 ; 0,931 ; 0,887 ; 0,928 ; 0,890 ; 0,926 ; 0,891 ; 0,925 (tours 1 à 8).
- **R3 : classe recopiée sans verdict sur HR1** : « R3 > R2 » aux deux δ (HR1 se lit par la Table A seule, § 3).

## 5. Table B′ — classement sur X̄ contre R2, à chaque δ (B8, E8, m = 0,02 ; D̄ > 0 = plus exploitable) — **table bloquée par le déclencheur 1 (P12), classes recopiées**

| Variante | δ | est (D̄) | B8 | E8 | Classe gelée |
|---|---|---|---|---|---|
| R0 | 1,4 | −0,0062 | [−0,0139 ; +0,0021] | [−0,0132 ; +0,0015] | « ≈ » |
| R0 | 1,6 | −0,0066 | [−0,0119 ; −0,0004] | [−0,0115 ; −0,0009] | « ≈ » (E8 ⊂ ]−m ; m[, testé avant « R0 ≳ R2 ») |
| R1 | 1,4 | +0,0262 | [**+0,0201** ; +0,0329] | [+0,0205 ; +0,0323] | « R2 > R1 » (borne basse B8 0,020107 > 0,02) |
| R1 | 1,6 | +0,0162 | [+0,0115 ; +0,0214] | [+0,0119 ; +0,0210] | « R2 ≳ R1 » (borne basse B8 > 0, < m ; E8 haut 0,0210 > m donc pas « ≈ ») |
| R3 | 1,4 | −0,0554 | [−0,0621 ; −0,0483] | [−0,0614 ; −0,0489] | « R3 > R2 » |
| R3 | 1,6 | −0,0664 | [−0,0712 ; −0,0612] | [−0,0708 ; −0,0617] | « R3 > R2 » |
| R4 | 1,4 | −0,0208 | [−0,0244 ; −0,0172] | [−0,0240 ; −0,0175] | « R4 ≳ R2 » (borne haute B8 −0,0172 > −m ; < 0) |
| R4 | 1,6 | −0,0178 | [−0,0213 ; −0,0143] | [−0,0209 ; −0,0146] | « R4 ≳ R2 » |

- **HR2 (R1 plus exploitable que R2 au fil des tours, d'un effet d'intérêt) : verdict suspendu, audit en attente** (déclencheur 1, P12 : classe autre que « R2 > R1 » au δ 1,6). Ce que la règle gelée rend si l'audit conclut « pas d'artefact » : « R2 > R1 » au δ 1,4 et « R2 ≳ R1 » au δ 1,6 ⇒ **HR2 non tranchée** (« « ? » ou « R2 ≳ R1 » à un δ : non tranchée », CL-02). Le signe de P12 (+) est observé aux deux δ ; l'ordre de grandeur ≥ +0,02 est atteint au δ 1,4 (+0,026) et non au δ 1,6 (+0,016). Le texte scellé (S3) avait calculé qu'à un effet vrai proche de m la puissance de la classe « R2 > R1 » est faible (≈ 0,22 à 0,03 au δ 1,4 ; ≈ 0 à 0,02).
- R0 (P14, descriptif) : D̄(R0, R2) prédit > 0 ; observé −0,006 aux deux δ, classe « ≈ » : signe contraire à P14, recopié sans verdict (le texte déclarait l'indice contraire du pilote v2, −0,006 ; −0,006, CL2-01 : la valeur observée est du même signe et du même ordre).
- R3 (P15) : D̄ prédit − : observé −0,055 et −0,066, « R3 > R2 » : conforme. R4 (P15) : prédit ≈ 0 ; observé −0,021 et −0,018, « R4 ≳ R2 » (R4 moins exploitable que R2 au fil des tours, effet d'intérêt non démontré à la marge) : recopié sans verdict.

## 6. Table C — attaques tenues à l'écart, Δ(R_k, R2) sur (ii), bornes B8, tolérance S5 = 0,02

| Variante | δ | est | B8 | Ligne gelée (première vraie) | Lecture |
|---|---|---|---|---|---|
| R0 | 1,4 | +0,0516 | [+0,0363 ; +0,0688] | 4 | amélioration sur (ii) (recopiée, sans verdict) |
| R0 | 1,6 | +0,0600 | [+0,0439 ; +0,0771] | 4 | amélioration sur (ii) (recopiée) |
| R1 | 1,4 | +0,0227 | [+0,0069 ; +0,0402] | 4 | **amélioration sur (ii)** |
| R1 | 1,6 | +0,0242 | [+0,0072 ; +0,0433] | 4 | **amélioration sur (ii)** |
| R3 | 1,4 | −0,0664 | [−0,0840 ; −0,0477] | 1 | régression avérée au-delà de la tolérance |
| R3 | 1,6 | −0,0768 | [−0,0945 ; −0,0586] | 1 | régression avérée au-delà de la tolérance |
| R4 | 1,4 | +0,0290 | [+0,0146 ; +0,0455] | 4 | amélioration sur (ii) |
| R4 | 1,6 | +0,0370 | [+0,0219 ; +0,0545] | 4 | amélioration sur (ii) |

Verdicts selon la règle gelée (« HR4 : conforme pour R3 et R1 si lignes 1 à 3 aux deux δ ; conforme pour R4 si lignes 4 ou 5 aux deux δ ; R0 : ligne recopiée sans verdict ») :
- **HR4 pour R3 : conforme** (ligne 1 aux deux δ) ; P4 : signe −, ≈ −0,05 (contexte v4) : observé −0,066 et −0,077.
- **HR4 pour R1 : non conforme** (ligne 4 aux deux δ, c'est-à-dire la branche opposée de P5, « borne basse B8 > 0 ») : R1 détecte mieux les attaques tenues à l'écart que R2, de +0,023 et +0,024. Le texte scellé avait déclaré (CL-06) que le pilote v1 indiquait le signe contraire de P5 (+0,010 ; +0,066) et que P5 était maintenue par principe ; la valeur observée est du signe du pilote. Le déclencheur 7 ne vise que la **confirmation** de P5 ; il ne s'applique pas. Le déclencheur 1 n'énumère pas P5 parmi les prédictions fermes ; la phrase générale du § Prédiction (« la branche opposée déclenche l'audit (R4, déclencheur 1) ») et la liste nominative du déclencheur 1 (P1, P12, P13, P7, P11) ne disent pas la même chose pour P5 : le lecteur applique la liste nominative (texte des « Critères de lecture gelés ») et signale la divergence au directeur (§ 8), sans trancher.
- **HR4 pour R4 : conforme** (ligne 4 aux deux δ) ; P6 : ≥ −S5, ordre de grandeur [−0,02 ; +0,05] : observé +0,029 et +0,037, dans la bande.
- R0 (P14, descriptif) : + par principe ; observé +0,052 et +0,060, ligne 4 : conforme au signe prédit.
- Lecture sans seuil (est [B8]) recopiée dans la table ci-dessus pour les huit cas.

Le texte ne définit pas de verdict d'ensemble pour HR4 ; le lecteur n'en forme pas : deux de ses trois composantes (R3, R4) sont conformes, la troisième (R1) ne l'est pas.

## 7. Table D — condition d'application (R2), par δ, bornes B2, marge S15 = 0,02

| δ | I1 de R2 : est [B2] | I3 − 0,7345 de R2 : est [B2] | I2 de R2 : est [B2] | Ligne gelée |
|---|---|---|---|---|
| 1,4 | +0,0017 [−0,0044 ; +0,0080] | +0,1405 [+0,1071 ; +0,1721] | +0,0687 [+0,0562 ; +0,0814] | 2 (borne haute de I1 0,0080 < 0,02 ∧ borne basse de I3 − nul 0,1071 > 0) |
| 1,6 | +0,0010 [−0,0030 ; +0,0053] | +0,1755 [+0,1488 ; +0,2021] | +0,0902 [+0,0784 ; +0,1018] | 2 (0,0053 < 0,02 ∧ 0,1488 > 0) |

Ligne 1 (borne basse de I1 > S15) : fausse aux deux δ ; ligne 2 vraie aux deux δ : **« ne progresse pas, retours au-delà du hasard (cycle) »**.

**HR5 (condition d'application) : vérifiée** (lignes 2 à 4 aux deux δ, ici ligne 2). P7 conforme (I1 ≈ 0 ; I3 − nul ≈ +0,1 à +0,2 : observé +0,14 et +0,18).

Saturation (CL-13) : part des tâches de R2 où I3 − nul est au plafond +0,2655 : 44 sur 100 (δ 1,4) et 55 sur 100 (δ 1,6), sous le seuil de 90 % : la mention « indicateur saturé » ne s'applique pas ; I3 par tâche n'a pas à être recopié. Note : l'estimation est à plus de 0,09 du plafond aux deux δ, les percentiles ne sont pas collés à la borne.

Indicateurs des autres règles, recopiés sans verdict (P8, P9 descriptifs ; est [B2]) :

| Règle | δ | I1 | I3 − 0,7345 | I2 |
|---|---|---|---|---|
| R0 | 1,4 | −0,0000 [−0,0005 ; +0,0004] | +0,0038 [−0,0379 ; +0,0438] | 0 exactement (par construction) |
| R0 | 1,6 | +0,0002 [−0,0001 ; +0,0006] | −0,0345 [−0,0762 ; +0,0071] | 0 |
| R1 | 1,4 | −0,0029 [−0,0045 ; −0,0013] | +0,2655 [+0,2655 ; +0,2655] (au plafond dans 100 tâches sur 100) | +0,1609 [+0,1456 ; +0,1758] |
| R1 | 1,6 | −0,0025 [−0,0040 ; −0,0012] | +0,2655 [+0,2655 ; +0,2655] (100 sur 100) | +0,1889 [+0,1766 ; +0,2014] |
| R3 | 1,4 | +0,0784 [+0,0721 ; +0,0848] | −0,0029 [−0,0512 ; +0,0438] | +0,0365 [+0,0259 ; +0,0474] |
| R3 | 1,6 | +0,0839 [+0,0784 ; +0,0894] | +0,0071 [−0,0429 ; +0,0555] | +0,0440 [+0,0341 ; +0,0535] |
| R4 | 1,4 | +0,0055 [+0,0028 ; +0,0085] | −0,0812 [−0,1362 ; −0,0295] | −0,0034 [−0,0087 ; +0,0020] |
| R4 | 1,6 | +0,0046 [+0,0021 ; +0,0075] | −0,0712 [−0,1212 ; −0,0212] | −0,0010 [−0,0073 ; +0,0057] |

P8 (R1 : I3 − nul > 0, au moins celui de R2) : observé +0,2655 contre +0,1405 et +0,1755 : conforme (I3 de R1 vaut 1 dans chaque tâche : chaque déplacement d'attaque à partir du tour 3 est plus proche d'une attaque d'au moins deux tours plus tôt que de la précédente, ce qui est la signature de la période 2). P9 (R4 : I3 − nul plus bas que R2) : −0,081 et −0,071 contre +0,140 et +0,175 : conforme. R0 (descriptif) : I1 et I3 − nul de l'attaquant seul contre une défense fixe, proches de zéro.

R3′ (descriptif, valeur du jeu restreint, moyenne des tâches) : par tour, δ 1,4 : 0,127 ; 0,253 ; 0,254 ; 0,254 ; 0,253 ; 0,247 ; 0,243 ; 0,242 ; finale 0,243. δ 1,6 : 0,070 ; 0,224 ; 0,221 ; 0,225 ; 0,223 ; 0,214 ; 0,209 ; 0,206 ; finale 0,208. À côté, (iii)_t de R3 : δ 1,4 : 0,127 ; 0,072 ; 0,167 ; 0,179 ; 0,198 ; 0,213 ; 0,224 ; 0,223 ; δ 1,6 : 0,070 ; 0,030 ; 0,121 ; 0,130 ; 0,153 ; 0,168 ; 0,181 ; 0,184.

## 8. Table E — coût (descriptif, sans verdict)

Moyennes par tâche (trajectoire + finale ; recalculées par le lecteur, identiques au fichier d'analyse) :

| Variante | δ | Processeur trajectoire (s) | Processeur finale (s) | Total (s) | Ratio contre R2 (moyennes) | Moyenne des ratios par tâche | Appels à l'optimiseur | Programmes linéaires | Entraînements | Départs de l'attaquant | Paramètres déployés / stockés |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R0 | 1,4 | 0,705 | 1,199 | 1,904 | 0,676 | 0,679 | 127 | 0 | 0 | 127 | 7 / 7 |
| R1 | 1,4 | 1,319 | 1,287 | 2,606 | 0,925 | 0,928 | 167 | 0 | 8 | 127 | 7 / 63 |
| R2 | 1,4 | 1,521 | 1,297 | 2,818 | 1 | 1 | 198 | 0 | 8 | 127 | 7 / 63 |
| R3 | 1,4 | 2,168 | 3,467 | 5,635 | 2,000 | 2,008 | 192,7 | 35 | 8 | 127 | 63 / 63 |
| R4 | 1,4 | 1,546 | 1,273 | 2,819 | 1,000 | 1,006 | 198 | 0 | 8 | 127 | 7 / 63 |
| R0 | 1,6 | 0,761 | 1,329 | 2,090 | 0,679 | 0,683 | 127 | 0 | 0 | 127 | 7 / 7 |
| R1 | 1,6 | 1,400 | 1,413 | 2,813 | 0,914 | 0,918 | 167 | 0 | 8 | 127 | 7 / 63 |
| R2 | 1,6 | 1,628 | 1,451 | 3,079 | 1 | 1 | 198 | 0 | 8 | 127 | 7 / 63 |
| R3 | 1,6 | 2,358 | 3,961 | 6,319 | 2,052 | 2,065 | 193,0 | 35 | 8 | 127 | 63 / 63 |
| R4 | 1,6 | 1,623 | 1,369 | 2,992 | 0,972 | 0,978 | 198 | 0 | 8 | 127 | 7 / 63 |

Paramètres stockés (CL-09) : toutes les règles gardent la liste des T + 1 = 9 moniteurs pour la matrice H (63 paramètres), R0 n'en garde qu'un (7) ; déployés par requête : 7 pour R0, R1, R2, R4, 63 pour R3.

Ordre observé du temps processeur : **R3 > R2 ≈ R4 > R1 > R0** aux deux δ, c'est-à-dire l'ordre de P10 ; les trois ordres de grandeur de P10 sont tenus (R3 ≈ 2,0 × R2 ≥ 1,3 ; R1 ≈ 0,92 × R2 ≤ 1 ; R0 ≈ 0,68 × R2 ≤ 0,7). Sur les appels à l'optimiseur, l'ordre de P10 n'est pas exactement observé : R3 (192,7 ; 193,0) est légèrement sous R2 = R4 (198), R1 167, R0 127 ; le coût supplémentaire de R3 vient des 35 programmes linéaires par tâche et de la finale (évaluation d'un mélange de 9 moniteurs : 3,5 à 4,0 s contre 1,2 à 1,5 s). Descriptif, sans effet sur les tables. Temps total : 3 327 s de processeur, 1 693 s de mur sur 2 processus (efficacité ≈ 0,98).

## 9. Phrase de synthèse (gabarit du texte scellé, recopiée sans rien omettre)

« Table A : ligne 4 aux deux δ, Δ(R3, R2) sur V +0,1045 [B2 +0,0906 ; +0,1185] et +0,1236 [+0,1127 ; +0,1341] : HR1 confirmée ; Table B (V) : R0 « ≈ » (+0,0024 [−0,0100 ; +0,0145]) et « ≈ » (+0,0037 [−0,0066 ; +0,0146]), R1 « R2 ≳ R1 » (−0,0137 [−0,0275 ; −0,0012]) et « ? » (−0,0086 [−0,0210 ; +0,0036]), R3 « R3 > R2 » (+0,1045 [+0,0896 ; +0,1195]) et « R3 > R2 » (+0,1236 [+0,1117 ; +0,1349]), R4 « R4 ≳ R2 » (+0,0202 [+0,0102 ; +0,0331]) et « R4 ≳ R2 » (+0,0142 [+0,0064 ; +0,0240]) ; HR0 : suspendue, audit en attente (déclencheur 1, P13 ; la règle rendrait « réfutée ») ; HR3 : suspendue, audit en attente (Table B bloquée ; la règle rendrait « confirmée ») (S12 : non déclenché, 5 % et 2 % des tâches à cosinus ≥ 0,999) ; Table B′ (X̄) : R0 « ≈ » (−0,0062 [−0,0139 ; +0,0021]) et « ≈ » (−0,0066 [−0,0119 ; −0,0004]), R1 « R2 > R1 » (+0,0262 [+0,0201 ; +0,0329]) et « R2 ≳ R1 » (+0,0162 [+0,0115 ; +0,0214]), R3 « R3 > R2 » (−0,0554 [−0,0621 ; −0,0483]) et « R3 > R2 » (−0,0664 [−0,0712 ; −0,0612]), R4 « R4 ≳ R2 » (−0,0208 [−0,0244 ; −0,0172]) et « R4 ≳ R2 » (−0,0178 [−0,0213 ; −0,0143]) ; HR2 : suspendue, audit en attente (déclencheur 1, P12 au δ 1,6 ; la règle rendrait « non tranchée ») ; Table C : R0 ligne 4 (+0,0516 [+0,0363 ; +0,0688] ; +0,0600 [+0,0439 ; +0,0771]), R1 ligne 4 (+0,0227 [+0,0069 ; +0,0402] ; +0,0242 [+0,0072 ; +0,0433]) : HR4 non conforme pour R1, R3 ligne 1 (−0,0664 [−0,0840 ; −0,0477] ; −0,0768 [−0,0945 ; −0,0586]) : conforme, R4 ligne 4 (+0,0290 [+0,0146 ; +0,0455] ; +0,0370 [+0,0219 ; +0,0545]) : conforme ; Table D : ligne 2 aux deux δ, R2 I1 +0,0017 [−0,0044 ; +0,0080] et +0,0010 [−0,0030 ; +0,0053], I3 − 0,7345 +0,1405 [+0,1071 ; +0,1721] et +0,1755 [+0,1488 ; +0,2021], I2 +0,0687 [+0,0562 ; +0,0814] et +0,0902 [+0,0784 ; +0,1018] ; condition d'application vérifiée (saturation : 44 % et 55 % des tâches au plafond, sous 90 % : non saturé) ; R3′ : valeur du jeu restreint par tour 0,127 → 0,242 (δ 1,4) et 0,070 → 0,206 (δ 1,6), finale 0,243 et 0,208 ; Table E : R3 ≈ 2,0 × R2, R4 ≈ 1,0 × R2, R1 ≈ 0,92 × R2, R0 ≈ 0,68 × R2 ; ordre du temps processeur R3 > R2 ≈ R4 > R1 > R0 conforme à P10 ; déclencheurs : 1 (P12 au δ 1,6 ; P13 aux deux δ) ; 2 à 7 : non ; issue des audits : non rendus (audits à faire par un sous-agent neuf : relecture du code de R0 et du compteur d'entraînements pour P13 ; relecture du code pour P12, selon le « Contenu de l'audit ») ; portée : résultat local au monde, à l'oracle, aux δ, à T, à λ* et à l'attaquant du tour pour X̄. »

## 10. Ce que le préenregistrement n'avait pas prévu (observations hors tables, sans verdict)

1. **Marge de P12 au δ 1,4** : la borne basse B8 de D̄(R1, R2) vaut 0,020107, soit 0,0001 au-dessus de m = 0,02 ; la classe « R2 > R1 » y tient de justesse. Observation sur la fragilité de la classe à ce δ, sans effet sur la lecture gelée (la première ligne vraie décide).
2. **Classe « ? » de R1 au δ 1,6 (Table B)** : la borne basse E8 vaut −0,02005, à 0,00005 de −m ; une largeur à peine plus petite aurait donné « ≈ ». Descriptif, P2 étant sans verdict.
3. **R4 au fil des tours** : P15 prédisait D̄(R4, R2) ≈ 0 ; l'observation est −0,021 et −0,018 avec des intervalles étroits (écart-type des différences 0,013), c'est-à-dire R4 moins exploitable que R2 au fil des tours, sans atteindre la marge d'intérêt ; de même sur (ii), R4 fait mieux que R2 de +0,03 à +0,04 (ligne 4 « amélioration », pas seulement « sans régression »). Non prévu en ce sens par le texte ; aucune table ne l'interprète.
4. **R1 sur les attaques tenues à l'écart** : la branche opposée de P5 est observée aux deux δ (R1 meilleure que R2 sur (ii)), alors que (i) sur les attaques vues est plus élevé pour R1 (0,321 contre 0,291 au δ 1,4) et que I2 (oubli) de R1 est le plus fort (0,16 et 0,19). Le texte ne prévoit pas de lecture de (i) ni de I2 des autres règles ; recopié.
5. **Ambiguïté textuelle sur la portée du déclencheur 1** : la phrase du § Prédiction (« la branche opposée déclenche l'audit (R4, déclencheur 1) ») couvre toutes les prédictions, la liste nominative du déclencheur 1 n'en couvre que cinq (P1, P12, P13, P7, P11). Le lecteur a appliqué la liste nominative ; si la phrase générale devait primer, la branche opposée de P5 (et de P14 sur X̄) relèverait aussi du déclencheur 1, avec pour effet de bloquer les Tables C et B′. Ce point revient au directeur.
6. **R0 et R2 sur (ii) et sur X̄** : R0 (M0 jamais réentraîné) détecte **mieux** les attaques tenues à l'écart que R2 (+0,05 et +0,06, ligne 4) et est légèrement moins exploitable que R2 au fil des tours (−0,006), tout en étant équivalent en finale (« ≈ »). Le texte avait prédit le signe + sur (ii) (P14, conforme) et le signe + sur X̄ (contraire). Recopié, sans verdict (HR0 ne compare pas « historique » au meilleur moniteur figé, § n'autorise pas).
7. **I3 de R1 exactement au plafond dans 100 % des tâches** aux deux δ (écart-type 6 × 10⁻¹⁷) : la réserve CL-13 (saturation) ne visait que R2 ; pour R1 l'intervalle est dégénéré. Descriptif.
8. **R3 progresse** (I1 +0,078 et +0,084, bornes basses > S15) : le mélange d'équilibre, seul, satisfait la ligne 1 de la Table D (« progresse ») là où la table ne vise que R2. Recopié sans verdict.
9. **Relevé `uptime`** (condition de lancement S8) : non trouvé dans les registres consultés (`registres/decisions.md` R-967, passations) ; le mur observé (28 min) est sous la projection (30 min), ce qui ne suggère pas de charge concurrente. Hors V0.
10. **Projection du coût** : 15,9 s et 17,4 s de processeur par tâche contre 17,3 s projetés ; aucune garde interne ni externe sollicitée.
11. **Réserve de méthode du lecteur** : pour localiser la fonction de quantiles `_q` et le rôle de rééchantillonnage, le lecteur a lancé un `grep` (numéros de lignes et signatures seulement) sur `donnees/argon-seul-convergence-v1/arene_melange_v4.py`, malgré la consigne de ne rien lire sous `donnees/` ; aucun contenu de données n'a été lu ; le recalcul n'importe pas ce module (méthode prise au § Métrique du texte scellé). L'empreinte de l'arène v4 n'a pas été recalculée sur disque pour la même raison (prise au manifeste).

## 11. Ce que le lecteur n'a pas fait

- Aucun audit (déclencheurs 1 sur P12 et P13) : l'audit est confié par le texte à un sous-agent neuf (relecture du code, compteur de R0, option attaquant indépendant) ; le lecteur a seulement recopié les compteurs utiles (§ 4).
- Aucun scellement, aucun commit, aucune modification de fichier existant ; ce fichier est neuf.
- Aucune interprétation au-delà des tables ; aucune recommandation.
