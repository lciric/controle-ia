# Relecture courte des corrections du lanceur v2 des notations — rapport du sous-agent neuf — v1

Versé par la session 15 le 2026-10-17, tel que rendu par le sous-agent neuf `a30d7b063bcd176a4` (lancé à 10:13:54 UTC, rendu
à 10:33:50 UTC, heures de sa transcription ; ni auteur du lanceur, du banc, du plan ni de leurs corrections). Texte recopié sans modification, depuis la
transcription du sous-agent. Traitement : section « Relecture courte » de `traitement-R2-lanceur-v2-v1.md` (même dossier).

---

## Relecture courte des corrections du lanceur v2 des notations (relecteur neuf, règle R2)

Je n'ai rien modifié dans le dépôt. Je n'ai fait aucun appel à l'outil de location. Le lanceur n'a tourné que dans le banc, et je n'ai lancé aucune commande git qui écrit.

### (1) Empreintes sha256
J'ai pris les empreintes des 35 fichiers ci-dessous au début et à la fin : elles sont identiques.
- Listes complètes : `/tmp/claude-0/-home-user-controle-ia-travail/adc77dcb-d0c4-5686-b269-a3ad7dc4b310/scratchpad/relecture-courte-v2/empreintes-debut.txt` et `/tmp/claude-0/-home-user-controle-ia-travail/adc77dcb-d0c4-5686-b269-a3ad7dc4b310/scratchpad/relecture-courte-v2/empreintes-fin.txt`.
- Le dossier v2 versé est conforme à ses sceaux : 20 fichiers sur 20.

**Pièces de la correction**
- rapport de la contre-lecture `bb15ec2042df6aeb0a483fd68a0561165488347ba1344f3da71a5c6653088bc4`
- traitement `542bd75b0363d2dcf3ef5c4d71b17d9db4be38b5508ef07a9584d59f58d6ac20`
- versions relues : lanceur `964ce4cab8c382236116efa544d8530da875239a7d0462027a0b0d38070cf0cd`, banc `1c0d66704e8742615d6b051e03e21e844268fc4675e707de71ea7e2adcea00ca`, plan `2b100bb44d5e40d1810a40a35f52dee2dc3832b2653cd29b60cecf622871c85d`
- versions corrigées : lanceur `a0757cb4bb9587926b513f85c43efd00e3e5a9aedf00f9e6fe795894dde4f560`, banc `a1be5300f663e0f85414281497ff6d7a40d8ce57a3b89410fec4884fdabb1d24`, plan `4ecc4bf0795fc887705cdf1b7dda177d15759cb9cb9feddc1a4711f1a93b6518`
- bloc-notes : la copie du lanceur v2 vaut `a0757cb4…`, **identique au dépôt**. La copie du banc v2 vaut `1c0d6670…` : c'est encore la version relue (voir RC-09).

**Références v1 et registres**
- lanceur v1 `8fb447071fceb7c72c79b25e5ea8381e9fec6fa1be40eac656202779a609c8db`, banc v1 `744c6337a6363e20af955ced57a8d254d3f12f6bc9af5bb1efee0a28bdcdd71d`, plan v1 `4c59f32d00829026ca19b67601c6363c873d990633c1041f7f360025f1e42c19`
- `verifications_notations_v1.py` `25d7faf1b71a7b0fab16e15dbf206273db023d80d73e65d2c520d1300640ff03`, `controles_avant_depense_notations_v1.sh` `b62fd0fff1277874b4fb647318fb753c4c2cb4d73125662f9db8cd2c71ecd0ca`
- préenregistrement `66784ceb9c93f699b211fa26a142a8e64e1cccbc2c2fb3479df559f297c474f6`
- `decisions.md` `29645a8cf212dbe813b29442871d6982ba328cb67daddbc200ee4d23b820ff21`, `go.md` `29a7a4927962837d84f1a0b174f5d0091aecf890af856228db3f092cfc5eb43b`, `CLAUDE.md` `1d469390187103fd509ccfa05f3df4ec1df0088fbc99a789f9fec64505cb497d`

**Preuves de la session**
- journal d'essai 5 `a1d7e410184d490acdd695af84db5b676d2148689d98b7b07689572a4a369c81`
- `faire_mutants.py` `aafd571d8232f5edb7dfbd0fe44b053849ed16bff5ec56df7eec9201bc59c5c9`
- journaux des mutants :
  - M01 `7d4d2b75…`, M02 `92c121fb…`, M03 `61ba6d5b…`, M04 `e6ecf8a8…`, M05 `9ecd379a…`
  - M06 `2504def3…`, M07 `6b84492f…`, M08 `5393a0f3…`, M09 `4249b557…`, M10 `f84355b0…`
  - M11 `d1dc6578…`, M12 `eb3599e6…`, M13 `50be1310…`, M14 `9295b6a9…`
  - empreintes complètes dans les listes ci-dessus

**Lus une fois en plus**
- journal du banc v1 `7575140e…`, `banc-v2-essai3.log` `173acdef…`
- `traces/t05-pilote-v1-20261012-1035/offre.json` `4f1eee64…`
- `offres-relues.json` des appels de 08:22 `92c5ed40…` et de 08:46 `22ed3bc9…`
- `traces/t05-instance-55292763-processeur-20261011/processeur.json` `89016e0f…`

### (2) Verdict
- Les 18 corrections sont faites, au bon endroit, et n'introduisent aucune faute : codes de sortie, ordre des étapes, `set -e` et piège d'erreur, `set -u`, citations, blocs Python. Le banc rejoué donne 133 cas, 0 non conforme, et le même journal que l'essai hors chemins et empreintes.
- Aucun constat bloquant ni majeur. Sept mineurs, dont trois à corriger avant C3 :
  - RC-01 : un identifiant en double est accepté. C'est une garde du v1 perdue dès le v2 relu.
  - RC-02 : l'exclusion de relancement laisse passer une offre dont la machine ou l'hôte est illisible.
  - RC-03 : la garde « C3 limité au dossier v3 » peut passer sans rien dire.
- La règle de relancement (option (a)) est juste et sans effet sur le premier lancement. Le plan la dit bien nœud, mais il se contredit (« même règle », RC-05). Il ne dit pas non plus qu'elle bloque une relance après une instance perdue (RC-06).

### (3) Constats

| Id | Fichier et ligne | Ce qui est | Ce qui devrait être, et pourquoi | Gravité | Correction proposée |
|---|---|---|---|---|---|
| RC-01 | `v3/lancer_notations_v2.sh` l. 273-319 ; v1 l. 179-181 | Aucun contrôle que les identifiants sont uniques. Le v1 s'arrêtait si l'offre apparaissait autrement qu'une fois (`len(d) != 1`). Démontré sur le bloc extrait tel quel : deux entrées 112, à 1,25 et 1,05, donnent « 112 1.05 », code 0. Plafond et crédit sont alors calculés à 1,05 pour une location à un prix inconnu. Le défaut existe dès le v2 relu ; la contre-lecture ne l'a pas relevé. | Une réponse où un identifiant revient est ambiguë. Il faut s'arrêter, comme au v1 : on n'affaiblit pas une garde du v1. | mineur (probabilité très faible) | Identifiants des offres lues tous distincts, sinon code 2 « offres : identifiant en double ». Cas O11 : 112 à 1,05 et à 1,25, code 2. |
| RC-02 | `v3/lancer_notations_v2.sh` l. 294-301 (`exclue`) | En relancement, l'exclusion compare des textes `machine:{…}`. Une offre sans `machine_id` ni `host_id`, à `null` ou à 7001.0 n'est donc pas écartée. Démontré sur le bloc extrait, avec l'exclusion « machine:7001 hote:8001 » : l'offre sans machine est prise ; l'offre à 7001.0 / 8001.0 (la machine même du premier lancement) est gardée. Côté instance, la même lecture exige des entiers, sinon code 2 : les deux côtés ne sont pas traités pareil. Aucun extrait d'offres versé (R-179 à R-190) ne garde `host_id` : si ce champ manquait dans la vraie réponse, l'exclusion par hôte ne ferait rien, sans le dire. | Une offre dont la machine ou l'hôte n'est pas un entier lisible ne prouve pas qu'elle n'est pas sur l'hôte qui a échoué. En relancement, elle doit être écartée (R5 : aucun repli silencieux). | mineur | Si l'exclusion est active, exiger `entier(machine_id)` et `entier(host_id)` pour qu'une offre soit conforme, et comparer des entiers. Cas R07 : offre sans machine ni hôte, moins chère, écartée. Cas R08 : offre à 7001.0, écartée. |
| RC-03 | `v3/lancer_notations_v2.sh` l. 148-149 | (i) Le `… \| grep -v … \|\| true` avale aussi un échec de `git diff` : HORS_V3 reste vide et la garde passe. (ii) Git détecte les renommages : un C3 qui déplace un fichier de v2 vers v3 ne montre que le chemin d'arrivée, et la garde passe. Les deux cas sont démontrés sur un dépôt jetable (git 2.43). | R5 interdit le repli silencieux. « C3 ne touche que ce dossier » doit voir aussi les retraits. | mineur | `D3=$(git -C "$DEPOT" diff --no-renames --name-only "$C3^" "$C3")` (le piège d'erreur rend 2), puis `[ -n "$D3" ]`, puis `HORS_V3=$(printf '%s\n' "$D3" \| grep -v "^$VERSEES3/" \|\| true)`. Cas Q16b : déplacement de v2 vers v3, code 2. |
| RC-04 | plan v2 l. 66-68 (étape 4 bis) | Le seul seuil est 1,30 USD. Or le plafond (en relancement) et le crédit sont calculés au prix choisi, et une hausse sous 1,30 dans la fenêtre passe. Exemple de relance : dépense engagée 1,75 USD, offre choisie à 1,10 (plafond 10,50), louée à 1,25. On obtient 1,75 + 7,5 × 1,25 + 0,5 = 11,63 USD, au-delà des 10,5 de GO-2026-10-12-02 (préenregistrement l. 131, condition (iii)). Au premier lancement, avec une offre à 1,04 louée à 1,30, le crédit exigé passe de 9,00 à 10,95 USD. | Il faut comparer au prix choisi, pas seulement au devis. | mineur | Si le prix relu dépasse celui de la ligne « offre choisie », recalculer (iii) et le crédit à ce prix. Hors plafond, crédit insuffisant ou prix au-dessus de 1,30 : arrêt par identifiant (R10) et nœud. |
| RC-05 | plan v2 l. 4 et l. 77-82 | « Ce qui ne change pas » dit « relancement unique (même règle…) » et « étape 4 bis (journal à 5 minutes) ». Les l. 26-30 (exclusion, nœud LV-02) et 66-68 disent le contraire. La l. 4 dit « ne change qu'une chose : le lanceur », alors que la veille, les registres et l'étape 4 bis changent aussi. | Le plan soumet un nœud à Lazar : il ne doit pas écrire « même règle » ailleurs. | mineur | Écrire « règle du préenregistrement ; lanceur v2 en mode relance, avec l'exclusion de LV-02 (nœud) », et « 4 bis, plus prix et machine ». L. 4 : « le lanceur et ce qui en découle ». |
| RC-06 | plan v2 l. 26-30 ; lanceur l. 261-263 ; préenregistrement l. 127, 131 | « Instance absente de la liste : code 2 » rend la relance impossible après une « instance perdue », qui est une cause d'infrastructure du préenregistrement, si l'instance a disparu de la liste. Avant la correction, une instance absente était tolérée. Le plan ne le dit pas. | Lazar doit trancher en le sachant. | mineur | Une phrase au plan et dans la question à Lazar. Options : accepter (relance impossible, il faudrait un lanceur v3) ; ou, si l'instance est absente, lire machine et hôte dans l'`offre.json` du premier lancement, versé aux traces. |
| RC-07 | banc l. 331-334, 476-477 | Le chemin du code 3, que visait LV-08, n'est pas éprouvé pour `offres-relues.json`. Mon mutant MR1, qui n'écrit l'extrait que s'il existe une offre conforme, passe le banc : 133 cas, 0 non conforme. | R5 : un artefact par garde. | mineur | Après R01 ou O04 : vérifier que `offres-relues.json` existe et porte une offre. |
| RC-08 | banc l. 462-472, 538-540 | Mes mutants MR2 (`machine_id` et `host_id` retirés d'`offre.json`) et MR3 (constantes réduites à `PRIX_MAX`) passent le banc, avec 0 non conforme. | La trace voulue par LV-02 et cinq des six constantes de LV-03 n'ont pas d'artefact. | pour information | O01 : lire `offre.json` (machine 7100, hôte 8100). Cas K02 : `FILTRE` altéré, code 2. |
| RC-09 | traitement l. 37-38 ; journal d'essai 5 l. 3 | L'essai 5 a tourné avec le banc `92279817…`. Le banc versé `a1be5300…` a été modifié 34 s après (10:08:18 contre 10:07:44). Seule différence de sortie : O01 passe de 17 à 18 offres relues. Les 14 mutants et mon rejeu ont tourné sur `a1be5300…`. La copie du banc au bloc-notes est encore `1c0d6670…`. | Le journal cité doit être celui du banc versé. | pour information | Produire le journal officiel avec le banc du dépôt (ou mettre la copie du bloc-notes à jour) et citer son empreinte. Une copie périmée serait de toute façon refusée à l'étape 2 ter, sans dépense. |
| RC-10 | traitement l. 22 | « Consignée par … R-195 » : R-195 n'existe ni dans `decisions.md` ni dans `etat.md`. | Ne pas citer comme fait un numéro non écrit. | pour information | « à consigner par la prochaine ligne R-… », ou écrire la ligne avant C3. |
| RC-11 | plan v2 l. 58-60 ; R-182 | La veille de R-182 attendait « une offre conforme et un crédit suffisant ». La veille du v2 ne garde que le crédit. | Dire si l'on attend encore une offre conforme, sans fixer son identifiant, pour éviter un code 3 après les contrôles. | pour information | Ajouter « … et au moins une offre conforme relue juste avant l'appel ». |
| RC-12 | banc l. 283, 299 | `PREMIERE_ARRETEE` n'a pas de champ secret : la recherche de jetons affichés ne couvre pas la nouvelle lecture des instances. P13e n'a pas de motif : son code 2 vient de la liste des instances, ce que montre le journal. | Couvrir la nouvelle lecture et donner un motif propre. | pour information | Ajouter `"extra_env": [["GH_TOKEN", "secret"]]`. Motif de P13e : « autres instances sur le compte : 12345678 (running, running) ». |
| RC-13 | arbre de travail du dépôt | Quatre fichiers hors v3 attendent : `run.py` et `tests/test_premier_test_ia_run.py` modifiés, `scripts/amorce_instance_p3.sh` et `scripts/p3_instance.sh` non suivis. | Un C3 fait par `git add -A` serait refusé au lancement par la garde de LV-15 (code 2). | pour information | Pour C3, `git add docs/procedures/notations-T0.5-v3` seulement. |

**(a) Constat par constat.** Lignes du lanceur sauf mention contraire.
- Faits et suffisants :
  - LV-01 (l. 287-291), LV-04 (O01, O09, Q10 à Q13), LV-05 (O08, O08b) ;
  - LV-06 (banc l. 178-179 et 300), LV-07 (l. 190-216), LV-09 (l. 298) ;
  - LV-14 (l. 304-305), LV-16, LV-17, LV-18 (l. 47, A01, A02).
- Faits, réserves seulement pour information :
  - LV-03 (l. 152-159 ; artefact pour `PRIX_MAX` seul, RC-08) ;
  - LV-11 (RC-11) et LV-12 (R-195 pas encore écrite, RC-10).
- Faits mais à compléter :
  - LV-02 (l. 252-270, 294-308, 312) : RC-02, RC-05, RC-06 ;
  - LV-08 (l. 283-286, 320) : RC-07 ;
  - LV-10 (plan l. 71-75) : RC-05 ;
  - LV-13 : RC-04 ;
  - LV-15 (l. 147-151) : RC-03.

**(b) Gardes retirées ou affaiblies ?** Par rapport au v2 relu, le différentiel corrigé n'ajoute que des contrôles. Le seul remplacement, `vus.get` par un test d'ensemble, est plus strict. Par rapport au v1, une seule garde manque, depuis le v2 relu : l'unicité de l'identifiant (RC-01). Les six constantes sont égales à celles du v1 versé à S `b604164`.

**(c) Le banc.**
- Les 21 cas nouveaux font 112 + 21 = 133 ; seul N06 du v1 est retiré.
- Chaque cas teste bien ce que son nom annonce, vérifié contre le code et par les motifs. Q10 et Q11 ont le même motif, mais c'est la même sous-garde.
- Les 14 mutants de la session sont attrapés (journaux lus).
- Mon rejeu donne 133 cas, 0 non conforme, en 44 s.
- Mes trois mutants passent le banc : d'où RC-07 et RC-08.

**(d) La règle de relancement.**
- Elle est juste. La lecture vise l'instance nommée par la ligne R-…, n'affiche que `machine:M hote:H`, et rend le code 2 si la liste est illisible, si l'instance est absente, ou si sa machine ou son hôte n'est pas entier.
- Elle est sans effet sur le premier lancement : `EXCLUES=-`, aucun appel de plus, aucune ligne écrite. Le cas R06 le confirme.
- Le plan la dit bien nœud (l. 26-30), mais il faut corriger RC-05 et RC-06.

**(e) Le plan.** Les chiffres sont exacts :
- 7,5 × 1,30 + 0,5 = 10,25 ; 7,5 × 1,04 + 1,2 = 9,00 ; 9,45 USD à 1,10 ;
- veille : 7,5 × (1,30 + autres projets) + 1,2, soit 10,95 USD sans autre projet ;
- 133 cas ; « six fois sur huit », soit R-178, R-179, R-180, R-182, R-188, R-190 (R-177 : tests en échec, signature ; R-185 : arrêt par la session) ;
- 79 000 Mo ; GO-2026-10-12-02 à 10,5 USD au plus.

Restent à corriger dans le plan : RC-04 et RC-05, plus RC-10 et RC-11 pour information.

### (4) Ce que je n'ai pas pu vérifier
- **Le vrai service de location.** Je n'ai pas pu vérifier :
  - si la recherche d'offres rend `host_id`, des identifiants uniques, et `gpu_ram` en Mo (le multiplicateur vient de la lecture de la source par la contre-lecture précédente) ;
  - si une instance perdue reste dans la liste ;
  - si le prix d'une instance se compare à celui de l'offre.

  Un seul appui dans le dépôt : `processeur.json` de l'instance 55292763 montre `machine_id` et `host_id` entiers.
- **Le vrai commit C3 et l'enchaînement réel des contrôles avec le v2** : ni l'un ni l'autre n'existe encore.
- **Le banc `92279817…` de l'essai 5** : il n'est pas gardé, je n'ai pu comparer que sa sortie.
- **Les 14 mutants de la session** : je ne les ai pas rejoués, seulement lu leurs journaux.

### (5) Bilan chiffré
- 13 constats : 0 bloquant, 0 majeur, 7 mineurs (RC-01 à RC-07), 6 pour information (RC-08 à RC-13).
- Corrections LV : 18 faites ; 10 suffisantes telles quelles ; 3 avec seulement des réserves pour information (LV-03, LV-11, LV-12) ; 5 à compléter (LV-02, LV-08, LV-10, LV-13, LV-15).
- Banc : 133 cas, 0 non conforme. Mutants : 14 sur 14 attrapés pour la session, 0 sur 3 pour les miens.
- RC-06 et le choix entre les options de LV-02 vont à Lazar. Le reste relève de la routine.

Tout est dans `/tmp/claude-0/-home-user-controle-ia-travail/adc77dcb-d0c4-5686-b269-a3ad7dc4b310/scratchpad/relecture-courte-v2/` :
- `banc-rejoue-1.log` (`586d7abb…`), le banc rejoué ;
- `mutants-relecture/` : `faire_mutants_rc.py` (`de36294b…`) et les journaux MR1 (`ca6e5f0e…`), MR2 (`4bf2b0c7…`), MR3 (`d8db753e…`) ;
- `demo-choix/bloc_choix_v2c.py` (`3bf7cd67…`), le bloc extrait pour RC-01 et RC-02 ;
- `demo-c3/`, le dépôt jetable de RC-03.
