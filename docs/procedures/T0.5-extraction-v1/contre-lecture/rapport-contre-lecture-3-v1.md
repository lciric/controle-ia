# Contre-lecture 3 (ciblée) — procédure d'extraction de T0.5, v1 : traitement de la contre-lecture 2 — rapport v1

Contre-lecteur : sous-agent neuf. Il n'a écrit ni la procédure ni son code, et n'a fait aucune des deux contre-lectures précédentes. Rapport du 2026-10-07, vers 06:30 UTC.

- Aucun fichier du dépôt n'a été modifié, rien n'a été committé.
- Rien n'a été ouvert sous `donnees/` ni sous `registres/` ; aucun texte de papier n'a été lu.
- Les essais ont tourné dans `…/scratchpad/contre-lecture-extraction-v3/` (appelé `<cl3>` ci-dessous) : dépôts git jetables construits avec les fonctions des tests du dépôt, textes synthétiques, copie corrigée du code hors du dépôt.
- Versions relues et essais : annexe.

## Verdict

**Scellable après corrections** — courtes, sans refonte.

**D-1 : traité.**
- Les montants en dollars ne sont plus pris pour des formules.
- Le module et les deux scripts rendent les mêmes codes partout où je les ai éprouvés, avec 0 écart :
  - 22 cas réalistes ;
  - 200 000 chaînes tirées au hasard ;
  - 2 000 dossiers mutés, passés au script scellé comme en production.
- Reste un faux positif réaliste, mineur (E-3). Pandoc 3.9, avec les réglages du corpus, garde les fins de ligne du source LaTeX à l'intérieur des formules. Une citation recopiée « caractère pour caractère » d'une telle formule est donc refusée. Le message oriente vers une mauvaise correction.

**D-2 : traité.**
- Aucun cas réaliste trouvé où le script rendrait, sur des entrées intactes, d'autres codes que le module. J'ai éprouvé l'ordre, les doublons, l'encodage, les retours chariot, et le texte lu par parties contre le texte entier.
- Mais la correction a déplacé une ligne, et cela introduit une faute : **E-1 (majeure)**.
  - Une réponse « à vérifier » modifiée par un contre-vérificateur fait tomber toute la lecture de sa ronde, par une exception qui n'est pas une garde.
  - La ronde reste « préparée et non lue ». La restauration étant interdite, l'extraction est bloquée pour toujours.
  - La correction tient en une ligne.

**D-3 : en partie (E-2, majeure, condition de lancement).** La règle de perte s'applique pendant le run, mais :
- elle ne couvre pas la période qui va de l'assemblage à la décision N-014 ;
- elle ne prévoit que l'option (a) de N-014 ;
- aucun code n'écrit l'« arrêt consigné par un résultat scellé » ;
- une perte n'est vue qu'à l'étape qui relit une archive : une tentative 2 et l'échantillon passent d'abord sur un run déjà perdu.

**Décompte des remarques nouvelles** : 0 bloquante, 2 majeures, 7 mineures, 5 suggestions.

**Avant le scellement** (texte, scripts et consignes touchés) :
1. E-2 : une ou deux phrases en section 8, ou la décision, écrite, de lancer après N-014.
2. E-3 : compléter le message de `texte.formule` (module et deux scripts).
3. E-9 et E-10 : deux précisions du texte.
4. E-4 : déclarer le résidu en entier.
5. E-13 : retirer `__pycache__/` du dossier de la procédure.

**Avant `preparer --tentative 1`** (les modules sont épinglés dès l'ouverture du run) : E-1, E-5, E-6, E-7, E-8. Les correctifs d'E-1, E-6 et E-7 ont été éprouvés sur une copie corrigée, hors du dépôt (annexe, essai 7).

**Échelle**, celle des contre-lectures 1 et 2 :
- **bloquante** : la procédure scellée produirait en silence des données fausses, ou arrêterait l'extraction sans raison ;
- **majeure** : à corriger ou à trancher avant le scellement ou le lancement, parce qu'un fichier scellé est touché ou qu'une garantie annoncée n'est pas tenue ;
- **mineure** : correction simple ;
- **suggestion** : facultatif.

E-1 a une conséquence de type « bloquante » (un arrêt sans raison), mais son déclencheur est peu probable : un contre-vérificateur qui enfreint sa consigne en cassant la structure d'un fichier. Je la classe **majeure**, comme la contre-lecture 2 avait classé D-2, de même nature.

## A. Les 19 remarques de la contre-lecture 2

Abréviations :
- **texte** : `docs/procedures/T0.5-extraction-v1.md` ;
- **ex** : `src/controle_ia/environnements/extraction.py` ;
- **et** : `src/controle_ia/environnements/extraire_t05.py` ;
- **vs** et **va** : `verifier-sortie-v1.py` et `verifier-avis-v1.py` ;
- **ce** et **cc** : consignes de l'extracteur et du contre-vérificateur ;
- **t5** : `tests/test_extraire_t05.py` ; **tx** : `tests/test_extraction.py` ;
- **tr1** : `contre-lecture/traitement-contre-lecture-1-v1.md`.

Les fichiers de la procédure sont dans `docs/procedures/T0.5-extraction-v1/`.

| remarque | état | preuve |
|---|---|---|
| D-1 (majeure) | **traité** ; faux positif résiduel : E-3 ; faux négatifs non déclarés : E-4 | Règle identique, caractère pour caractère : ex l. 39-41 et 83-101, vs l. 25-27 et 67-83, va l. 18-20 et 62-78. Message (« write the amounts without $ ») : ex l. 121-122, vs l. 97-98, va l. 92-93. Exception de forme : ce l. 22, cc l. 31. Texte l. 106 et 109. Tests t5 l. 153-161 et 194-196. Essais 1 et 2 : 0 écart sur 22 cas, 200 000 chaînes et 2 000 dossiers ; deux montants dans deux paragraphes, et des montants échappés, acceptés ; « \nabla » dans `$$…$$` et « \nu » dans `$…$` refusés. |
| D-2 (majeure) | **traité** ; faute nouvelle E-1 ; résidus E-7, E-8 | Script scellé exécuté (`sys.executable -I`) : et l. 238-245. Comparaison des listes triées : et l. 248-252. Validation : et l. 368 et 374-375 ; lecture : et l. 646 et 668-669. Annonce seulement consignée : et l. 228-235, 386 et 672. Texte l. 123 ; ce l. 23 ; cc l. 31. Tests t5 l. 600-652. Essais 2 et 3 : aucun écart sur entrées intactes. |
| D-3 (majeure) | **en partie** : E-2 | Règle écrite au texte l. 243 (une session, arrêt scellé, rien de relu, run nouveau). Aucun code n'écrit l'arrêt. Perte vue tardivement (essai 3, `test_perte_detectee_tardivement`). Options (b) et (c) de N-014 non couvertes (texte l. 242). |
| D-4 (mineure) | **traité** ; déclaration du résidu incomplète : E-4 | Extrait de 30 caractères autour de la première occurrence : ex l. 78-80 et 114-128, vs l. 63-64 et 91-104, va l. 58-59 et 86-99. Conseil pour une tabulation : ex l. 115-116, vs l. 92. Résidu déclaré : texte l. 106, ex l. 88-89. |
| D-5 (mineure) | **traité** | Texte l. 129, 170 et 208. Code inchangé et conforme : ex l. 499-500, et l. 592. Déroulé t5 l. 485 et 489. |
| D-6 (mineure) | **traité** | et l. 698-699 et 711-733 (`accord_audit`, `_accord_audit_cote_sale`). Texte l. 173. Test t5 l. 578-579. |
| D-7 (mineure) | **traité** ; suggestion E-11 | Dénominateur : et l. 508-510 et 842-843. Bases sur les seules références non nulles : et l. 806-809. Désaccords par rôle : et l. 821-834. Texte l. 188-190. Test t5 l. 495-497. |
| D-8 (mineure) | **traité** | Valeurs de H.10 copiées : ex l. 44-48. `manifeste.py` épinglé : et l. 69-70. Test d'accord : tx l. 76-82. Texte l. 218. |
| D-9 (mineure) | **en partie** : E-5 | Texte corrigé : l. 6, 129 et 131. Les deux docstrings ne le sont pas : ex l. 31 (« section 2 », à lire 3) et ex l. 417 (« section 5 », à lire 6), identiques à 73559c8. |
| D-10 (mineure) | **en partie** : E-6 | Code `texte.substitut` : ex l. 38 et 124-129, vs l. 24 et 100-105, va l. 17 et 95-100. Sortie des scripts robuste : vs l. 214, va l. 143. Écritures atomiques et idempotentes : et l. 151-175 et 185-194. Octets empreintés archivés : et l. 380-383. Tests t5 l. 737-746 et 916-933. Mais un texte brut dans deux messages rend les détails non encodables et arrête toute la validation, pour toujours ; l'archive est déjà écrite quand le message dit « rien n'est écrit » (essai 3). |
| D-11 (mineure) | **traité** | Tirets U+2010 à U+2014, trait d'union conditionnel, guillemets : t5 l. 162-172. Clé morte corrigée : t5 l. 129-132 et 193. Entier trop grand refusé : ex l. 185-194. Codes `fichier.absent` et `json.illisible` à la lecture : et l. 654-664, éprouvés en déroulé (t5 l. 689 et 693). |
| D-12 (mineure) | **traité** | Texte l. 77. « Write all answers in English » : ce l. 25, cc l. 33. |
| D-13 (mineure) | **traité** ; emplacement des fichiers de retours : E-10 | Deux clés exactement, au plus 3 lancements : et l. 214-225. Forme contrôlée : et l. 57 et 228-235. Ligne brute dans `donnees/` seulement : et l. 387 et 686-687. Tests t5 l. 600-618 et 758-759. Texte l. 122 et 229. |
| D-14 (mineure) | **traité** (formulation) | Texte l. 221, tr1 l. 14 : « supposés servis par le modèle de la session » ; repli non observable. La consigne de la plateforme reste invérifiable depuis le dépôt. |
| D-15 (suggestion) | **traité** | tr1 l. 31 ramené à ce que garantit la fuite mécanique. Message « edit the statement, not the quote » : vs l. 207-209, ex l. 253-255. |
| D-16 (suggestion) | **traité** | `LANCEMENTS_MAX` et `AVIS_MAX_PAR_ROLE` : et l. 54-55, 221-225 et 602-606. Texte l. 124 et 171. Tests t5 l. 678-695 et 756-757. L'arrêt n'est pas scellé : E-8. |
| D-17 (suggestion) | **traité** ; pas de suite si aucun faux positif n'est établi : E-8 | et l. 56, 396-405 et 436-437. Texte l. 197. Test t5 l. 655-675. |
| D-18 (suggestion) | **traité** | Texte l. 181. Recalcul de `scipy.stats.binom.sf(4, 16, p)` : 0,0170 ; 0,0791 ; 0,3698. Intervalles de 0 à 0,2059 et de 0,0727 à 0,5238 : justes. |
| D-19 (suggestion) | **traité** ; suggestion E-12 | Bloc « references » de l'essai à blanc. Texte l. 34. Empreinte du code reproduite : 2e1b9417… = sha256 de la concaténation des sources de `copie_de_lecture` puis d'`exiger_copie`. Code de découpage identique entre 73559c8 et l'arbre. 96 papiers, 403 parties, ligne maximale de 3 775 : conformes au fichier. Recalcul sur les textes non vérifié (`donnees/` interdit). |

**Bilan** : 16 remarques traitées, 3 en partie (D-3, D-9, D-10), aucune non traitée.
- Les 66 gardes des deux modules sont toutes exercées par les 118 tests (19 dans `extraction.py`, 47 dans `extraire_t05.py`). Relevé par mon traçage : 0 garde non exercée.
- Les 118 tests passent.

## B. Remarques nouvelles

### E-1 — majeure — une réponse « à vérifier » modifiée par un contre-vérificateur fait tomber toute la lecture de la ronde (faute introduite par la correction de D-2 et D-11)

**Où** : et l. 665-671, dans `lire_contre_verification`. Garantie annoncée au texte l. 79 et l. 171 (« Une entrée modifiée est une anomalie de son seul papier », « Aucune restauration n'est permise », « Avis illisible (… entrée modifiée) : il est consigné et ne compte pas »).

**Problème**
- À 73559c8, l'anomalie `entrees.modifiees` était ajoutée avant `if not anomalies:` (l. 579-582). Les réponses d'un dossier modifié n'étaient donc jamais relues.
- La correction de D-2 l'a déplacée après la comparaison au script (l. 668-671). Désormais, `anomalies_avis` lit `a-verifier/*.json` dans le dossier même quand le contre-vérificateur les a modifiées (l. 665-667).
- Selon la modification, la lecture lève une exception qui n'est pas une `GardeArret`. Rien n'est écrit. La ronde reste « préparée et non lue », ce qui bloque `assembler` (CL-4) et toute ronde « audit » ou « reprise ».
- La restauration étant interdite (texte l. 79), l'extraction est bloquée pour toujours, par un seul sous-agent.

**Preuve** : essai 3, `test_entree_a_verifier_modifiee_fait_tomber_la_ronde`. Pour chacune des quatre altérations, `lire_contre_verification` lève l'exception indiquée :

| altération | exception levée |
|---|---|
| `cibles.json` supprimé | `FileNotFoundError` |
| `cibles.json` réduit à « { » | `JSONDecodeError` |
| famille `sterile_directions` retirée | `KeyError` |
| `h9.json` remplacé par une liste | `AttributeError` |

Dans les quatre cas, `assembler` s'arrête ensuite sur « ronde 1 préparée et non lue ».

**Correction**
- Juger l'avis seulement sur des entrées intactes : `if not anomalies and not modifiees:` à la l. 665.
- Mieux encore : lire les réponses à vérifier dans l'archive validée, pas dans le dossier.
- Ajouter un test sur les quatre altérations.
- Éprouvé sur une copie corrigée (essai 7) : le papier altéré rend `["entrees.modifiees"]`, l'autre papier reste lisible, et les 118 tests du dépôt passent, sauf une assertion de message liée à E-6.

### E-2 — majeure (condition de lancement ; touche la section 8) — règle de perte : sans issue après l'assemblage, limitée à l'option (a) de N-014, arrêt non écrit, perte vue tard

**Où**
- texte l. 9, 234-244, en particulier l. 242-243 ;
- et l. 139-144 (`_ouvrir_run`) et 197-201 (`lire_archive`) ;
- `docs/decisions/proposition-N-014-v1.md` l. 26-28 et 34-37.

**Problème**
1. **Après l'assemblage.** Les tâches assemblées (énoncés et cibles) ne vivent que dans `donnees/<run>/`, sur le disque éphémère, jusqu'à leur copie dans le dépôt, qui attend N-014. N-014 est un nœud, sans défaut. Si la session se termine avant la réponse, qu'il s'agisse d'une passation ou d'une inactivité, la règle déclare un arrêt et un run nouveau. Le texte ne dit pas que la session doit rester active jusqu'à la copie, ni qu'il vaut mieux lancer après N-014.
2. **Options de N-014.** Le texte l. 242 ne prévoit que l'option (a), une copie « telle quelle ». Avec (b), une copie chiffrée, le texte scellé ne s'applique plus : ce serait un écart. Avec (c), aucune exception, il n'y a aucun lieu persistant, et donc aucune issue.
3. **Arrêt non écrit.** Aucune fonction n'écrit l'« arrêt, consigné par un résultat scellé dans `diag/` ». L'étape suivante lève seulement « fichier absent sur disque » (essai 3, `test_perte_de_donnees_arret_non_consigne` : `diag/` ne contient aucun résultat de perte). Le nom et le contenu de ce résultat ne sont fixés nulle part.
4. **Perte vue tard.** Une perte de `donnees/<run>/` après la validation 1 n'est vue qu'à `preparer-contre-verification`. Entre-temps, `preparer --tentative 2`, `valider --tentative 2` (qui recrée `donnees/<run>/` avec une archive neuve) et `echantillonner` passent sur un run déjà perdu (essai 3, `test_perte_detectee_tardivement`).
5. **Audit du côté sale.** Après un arrêt de seuil, l'audit R4 relit les archives. Une perte le rend impossible, ce que le texte ne prévoit pas.

Point fort à garder et à écrire : un run nouveau sous la même procédure a la même entropie, celle de l'empreinte de la procédure. Il a donc la même permutation de l'échantillon : aucune réélection n'est possible après avoir vu des codes (CL-11).

**Correction**, avant le scellement : l'option la plus simple reste celle recommandée par la contre-lecture 2, lancer après N-014. Sinon :
- remplacer la l. 242 par une phrase de ce type : « le run n'est lancé qu'après la décision N-014 ; selon elle, les fichiers de `donnees/<run>/` sont copiés tels quels (a) ou chiffrés, avec les empreintes des fichiers clairs et des fichiers chiffrés (b) ; sans stockage persistant (c), pas de lancement ; la session reste active jusqu'à cette copie » ;
- dans le code, à chaque étape (`_ouvrir_run`) : contrôler la présence et l'empreinte de chaque fichier de `donnees/<run>/` déjà consigné dans `diag/` ; sur une absence, écrire `arret-perte` (étape, fichiers manquants) puis arrêter.

### E-3 — mineure (touche les scripts scellés) — faux positifs résiduels de `texte.formule` sur des fins de ligne réelles ; le message oriente vers une mauvaise correction

**Où**
- ex l. 83-101 et 121-122 ; vs l. 67-83 et 97-98 ; va l. 62-78 et 92-93 ;
- `invite-cibles-v1.txt` l. 3 (« copy each quote character for character … markup included ») ;
- ce l. 17 et 22 ;
- conversion du corpus : `corpus_arxiv.py` l. 389 (pandoc 3.9, `--wrap=none`) et règle de sélection l. 65-67.

**Problème**

Pandoc 3.9, avec les réglages exacts du corpus, joint les lignes de prose. Mais il garde les fins de ligne du source LaTeX dans les formules en ligne et dans les formules d'affichage. Essai 4, sur un source synthétique :
- `$a +` ⏎ `b = c$` ;
- `$$\begin{align}` ⏎ `a &= b \\` ⏎ `c &= d` ⏎ `\end{align}$$` ;
- `\label{eq:x}` ⏎ `y = \sigma(Wx + b)`.

Une citation fidèle d'un tel passage contient une fin de ligne suivie d'une minuscule entre deux `$`. Elle est refusée alors que le JSON est juste (essai 4, `essai_d1_citation_pandoc.py`) :
- citation fidèle : `[texte.formule]` ;
- même citation, fin de ligne remplacée par une espace : acceptée, et la citation est retrouvée ;
- même citation, fin de ligne écrite « \\n », comme le message peut le laisser croire : `[cibles.citation_introuvable]`.

Autres faux positifs, plus rares (essai 1) :
- une fin de ligne simple suivie d'une minuscule entre deux montants (« …$100M⏎and fine-tuning adds $5M ») ;
- une énumération en minuscules entre deux montants (« a. … $2M ;⏎b. … $0.5M ») ;
- un mot « ablation » ou « ablate » en début de ligne : la règle « abla » s'applique partout.

Le message parle de barres obliques et de dollars, jamais d'une fin de ligne réelle. L'exception de forme de la consigne (ce l. 22) laisse une issue, mais au prix d'un ou deux tours de plus, avec un risque de reprise. Le biais est dirigé vers les papiers riches en formules. L'arrêt D-17 le détecterait s'il devenait systématique.

**Correction**
- Ajouter au message, dans le module et les deux scripts : « if this line break is a real one (copied from the paper, or intended), replace it with a space ».
- Ajouter au texte l. 109 : « saut de ligne réel, recopié du papier : remplacé par une espace ».
- Ajouter deux cas de test : une citation fidèle d'une formule sur deux lignes (refusée, faux positif documenté) et la même avec une espace (acceptée).
- Restreindre la règle aux noms de commandes LaTeX en « \n… » réduirait ces faux positifs, mais c'est un changement de règle ; je ne le recommande pas à ce stade.

### E-4 — suggestion — faux négatifs de la règle des formules, non déclarés

**Où** : texte l. 106 ; ex l. 88-89.

**Problème** : le résidu déclaré ne cite que le désappariement par un montant et le « saut de ligne voulu ». Ne sont pas détectés non plus (essai 1) :
- une commande en « \n » hors de toute paire de `$` : « \\(\nu\\) », ou LaTeX sans délimiteur ;
- un « \n » suivi d'une majuscule (`\nRightarrow`, `\nLeftarrow`).

L'effet est une corruption silencieuse d'un symbole dans l'énoncé ou dans une description. Dans une citation, la corruption est déjà rattrapée par `citation_introuvable`. C'est rare : pandoc n'emploie que `$`.

**Correction** : compléter la déclaration du résidu (texte et docstring).

### E-5 — mineure — D-9 en partie : deux renvois de docstring non corrigés

**Où** : ex l. 31 (« procédure v1, section 2 » : les alertes sont en section 3) ; ex l. 417 (« procédure v1, section 5 » : la contre-vérification est la section 6). Mêmes lignes qu'à 73559c8 (`git show 73559c8:…extraction.py`, l. 32 et 368).

**Correction** : 2 → 3 et 5 → 6, avant `preparer` (le module est épinglé).

### E-6 — mineure — D-10 en partie : un texte brut dans deux messages bloque toute la validation, pour toujours

**Où**
- ex l. 223 et 225 : `{ident}` brut ;
- ex l. 232-233 : `str(h)[:40]` brut ;
- et l. 157-160 (`ecrire_donnees`) et l. 388-389 (archive écrite avant les détails).

**Problème**
- Un identifiant de cible qui contient un substitut isolé, avec une citation courte ou introuvable, met le substitut tel quel dans le message. Il en va de même d'une `reference_gpu_hours` textuelle qui en contient un.
- Le fichier `details-validation-tentative-K.json` n'est alors plus encodable. `ecrire_donnees` arrête toute la validation, pour tous les papiers, et l'étape refaite s'arrête à l'identique : le contenu est déterministe.
- Le message dit « rien n'est écrit », mais l'archive `sorties-tentative-K.tar` et son sceau sont déjà écrits.
- Le déclencheur est très improbable, mais la garantie de CL-5 (« anomalie de son seul papier ») n'est pas tenue.

**Preuve** : essai 3, `test_substitut_dans_un_message_bloque_la_validation`, dans les deux variantes. Le même arrêt survient deux fois de suite, et l'archive est présente.

**Correction** : `!r` dans ces trois messages du module, en mettant à jour l'assertion de tx l. 52 ; ou `ensure_ascii=True` pour les détails. Les codes des scripts ne changent pas. Éprouvé sur la copie corrigée (essai 7) : la validation passe, et le papier rend `cibles.calcul_valeur`, `cibles.citation_courte` et `texte.substitut`.

### E-7 — mineure — un fichier ajouté sous `papier/` n'est pas une « entrée modifiée », mais il change le texte que lit le script : désaccord, puis arrêt de toute la validation

**Où** : vs l. 216 (`glob("partie-*.md")`) ; et l. 208-211 (`_entrees_modifiees` ne voit que les entrées consignées) ; texte l. 79.

**Problème**
- Un sous-agent qui dépose, par exemple, `papier/partie-01-notes.md` et y prend une citation : le script la trouve, le module non. C'est un désaccord « en production », et il arrête la tentative entière, au lieu de rester une anomalie du seul papier.
- C'est improbable, mais c'est le seul écart script-module que j'aie trouvé sur des entrées « intactes ».

**Preuve** : essai 3, `test_fichier_ajoute_dans_papier_arrete_toute_la_validation`. Résultat : « le script scellé rend [], le module ['cibles.citation_introuvable'] : désaccord en production ».

**Correction** : compter comme `entrees.modifiees` tout fichier présent sous `papier/` et absent des entrées. Éprouvé sur la copie corrigée (essai 7).

### E-8 — mineure — arrêts sans résultat scellé ni suite écrite

**Où**
- désaccord du script et du module : et l. 248-252, texte l. 123 ;
- script hors forme : et l. 238-245 (et un `subprocess.TimeoutExpired`, qui n'est pas converti en garde) ;
- trois avis sans avis lisible : et l. 605-606, texte l. 171 ;
- arrêt D-17 : et l. 396-405 et 436-437, texte l. 197.

**Problème**
- Ces arrêts lèvent une `GardeArret` sans résultat dans `diag/`, à la différence des arrêts de seuil et de D-17 (CL-16 : « arrêts scellés »).
- Le texte ne dit pas la suite :
  - un désaccord est définitif, parce que scripts et modules sont épinglés : il faut une version 2 et un run nouveau ;
  - une panne passagère du processus (hors forme, délai) n'a rien écrit et pourrait se relancer à l'identique.
- Pour D-17, si l'audit n'établit aucun faux positif, le code interdit tout tirage, et le texte ne prévoit rien.

**Correction**
- Écrire un résultat scellé avant chaque arrêt (`arret-desaccord-script` avec le papier et les deux listes de codes, `arret-avis-refaits`).
- Convertir `TimeoutExpired` en garde.
- Ajouter au texte une phrase par cas : désaccord, version 2 et run nouveau ; panne de processus, une relance de l'étape, qui n'a rien écrit ; trois avis illisibles, nœud ; D-17 sans faux positif établi, nœud.

### E-9 — mineure — texte en deçà des consignes et du code

**Où et problème**
- Texte l. 91-95 : il énumère quatre exceptions, « écrites dans sa consigne ». La consigne en a cinq : la cinquième (ce l. 22, cc l. 31) permet de corriger une erreur de forme en réécrivant les caractères en cause.
- Texte l. 103 : « référence de coût présente mais non strictement positive ». Depuis D-11, un entier non représentable en flottant est aussi refusé (ex l. 185-194).

**Correction** : ajouter la cinquième exception au texte, et « ou non représentable en flottant ».

### E-10 — mineure — emplacement des fichiers de retours non fixé : la ligne brute peut entrer dans le dépôt, contre D-13

**Où** : texte l. 122 et 196 ; et l. 858-859 (`_retours` lit n'importe quel chemin).

**Problème**
- `valider --retours FICHIER` et `lire-contre-verification --retours FICHIER` lisent un fichier écrit par la session. Ce fichier contient les dernières lignes brutes, qui peuvent porter du texte du papier quand elles sont hors format.
- Ni le texte ni le code ne fixent où il vit. Rangé dans `runs/` ou à la racine, puis committé (« chaque résultat est committé et poussé »), il ferait entrer ce texte dans le dépôt, ce que D-13 et la section 8 excluent.

**Correction**
- Texte, section 8 : « les fichiers de retours s'écrivent hors du dépôt, dans `donnees/<run>/` ; leur empreinte est consignée ».
- Code : refuser un chemin de retours situé dans le dépôt hors de `donnees/`, comme le fait `_hors_depot`.

### E-11 — suggestion — bilan

**Où** : et l. 793-812 ; texte l. 142 et 190.

**Problème**
- `taches_assemblees` compte ensemble les tâches d'évaluation et celles d'entraînement (le test l. 497 le dit). Or la famille « coût » se mesure sur les tâches d'évaluation.
- Les désaccords entre l'annonce du sous-agent et le module, consignés papier par papier, ne sont agrégés nulle part. Ce compte révélerait une consigne mal suivie, comme une retouche après le dernier contrôle (R4).

**Correction** : ventiler ces comptes par liste, et compter les désaccords d'annonce par tentative et par rôle.

### E-12 — suggestion — essai à blanc : recette de l'empreinte du code

**Où** : `essai-a-blanc-copie-de-lecture-v1.json`, champ `references.code_de_decoupage`.

**Problème** : « source des deux fonctions » ne dit pas comment l'empreinte se calcule. Je l'ai reproduite : sha256 de `inspect.getsource(copie_de_lecture) + inspect.getsource(exiger_copie)`, dans cet ordre, sans séparateur.

**Correction** : écrire cette recette dans le champ (R6).

### E-13 — suggestion — `__pycache__/` dans le dossier qui sera scellé

**Où** : `docs/procedures/T0.5-extraction-v1/__pycache__/`, deux `.pyc` des scripts, datés de 05:36.

**Problème** : git les ignore, mais `verifier-arbre`, qui parcourt `docs/` sur disque (`scellement.py` l. 91-99), les signale comme non scellés. La routine de reprise échouerait donc dans ce conteneur après le scellement. Constaté : « empreinte compagnon … absente » pour les deux fichiers.

**Correction** : supprimer le dossier avant le scellement ; importer les scripts avec `PYTHONDONTWRITEBYTECODE=1`.

### E-14 — suggestion — tenue des fichiers

- `tr1` a été réécrit après la contre-lecture 2 (empreinte relue par elle : 2ea3112b ; aujourd'hui : e0989fec ; lignes de CL-8 et CL-25). C'est déclaré dans les cellules, mais pas dans le traitement de la contre-lecture 2. Le dire, ou garder la version relue (R12).
- Texte l. 7 : « Les 19 remarques sont traitées ici et dans le code » est à reprendre après cette contre-lecture : D-3, D-9 et D-10 sont en partie traitées.

## C. Réponses courtes aux cinq priorités

**1. D-1**
- Règle identique au module et aux deux scripts, vérifiée par l'exécution : 0 écart.
- Faux positifs plausibles :
  - une citation fidèle d'une formule que pandoc garde sur plusieurs lignes (le cas réaliste) ;
  - une fin de ligne simple ou une énumération en minuscules entre deux montants ;
  - le mot « ablation » en début de ligne.
- Aucun faux négatif grave : les commandes en « \n » hors de `$` ou suivies d'une majuscule échappent à la règle, mais c'est rare et c'est à déclarer (E-4).

**2. D-2**
- Sur des entrées intactes, aucun cas réaliste d'écart :
  - **ordre et doublons** : listes triées comparées en multiensemble ;
  - **encodage** : sortie en UTF-8 avec `backslashreplace` ; un identifiant brut coupé par `splitlines()` garde son code en tête de ligne ;
  - **sortie interrompue** : garde « hors forme », rien n'est écrit ;
  - **parties contre texte entier** : identiques à la normalisation près ; le retour chariot traduit par `read_text` est sans effet (essai 3, textes en CRLF et en CR isolé, parties de 120 caractères).
- L'interpréteur des sous-agents (`/usr/bin/python3`, 3.11.15, Unicode 14.0.0) est celui du module.
- Seuls écarts possibles : un fichier ajouté sous `papier/` (E-7) et une panne du processus (E-8).
- La faute réelle est ailleurs : E-1.

**3. D-3** : applicable pendant le run, insuffisante après l'assemblage et pour les options (b) et (c) de N-014 ; l'arrêt n'est ni écrit ni vu à temps (E-2).

**4. D-4 à D-19** : traitement réel, sauf D-9 et D-10, en partie (E-5, E-6).

**5. Fautes nouvelles** :
- dans le code épinglé : E-1 et E-6 ;
- dans les fichiers qui seront scellés : E-3 (messages des scripts), E-9 et E-10 (texte), E-13 (dossier).

## Annexe — versions relues et essais

**Fichiers relus**, avec les 8 premiers chiffres de l'empreinte, au début et à la fin de la relecture : inchangés.

| fichier | empreinte |
|---|---|
| texte `docs/procedures/T0.5-extraction-v1.md` | 97d0ac32 |
| `invite-cibles-v1.txt` (inchangée depuis la contre-lecture 2) | 8fc41e48 |
| `consigne-extracteur-v1.txt` | 4c9c38e3 |
| `consigne-contre-verificateur-v1.txt` | ff21420f |
| `verifier-sortie-v1.py` | eeebaeef |
| `verifier-avis-v1.py` | 898f2d41 |
| `essai-a-blanc-copie-de-lecture-v1.json` | 41927cc1 |
| `rapport-contre-lecture-2-v1.md` | 1d170dc6 |
| `traitement-contre-lecture-2-v1.md` | 5e3f4199 |
| `traitement-contre-lecture-1-v1.md` (lignes CL-8 et CL-25) | e0989fec |
| `extraction.py` (inchangé de 34dbbf8 à HEAD f406eb4) | 0d4c05aa |
| `extraire_t05.py` (idem) | d78cce32 |
| `tests/test_extraire_t05.py` | 365df2e6 |
| `tests/test_extraction.py` | 30b462de |

Lus en plus, parce que cités et utiles :
- `manifeste.py` (1a5c7464), `scellement.py` (93beeb1c), `invites.py`, `gardes.py`, `tests/conftest.py` ;
- les invites H.9 et H.10 ;
- la règle de sélection (8f43dcae ; sections 7 à 9 : conversion par pandoc 3.9) ;
- `corpus_arxiv.py` l. 65 et 385-397 ;
- la proposition N-014 (34725463) ;
- le différentiel `git diff 73559c8 34dbbf8 -- src tests`.

Fichiers de travail de la contre-lecture 2 (archive tar) : seulement la liste des membres, plus des statistiques de caractères de deux fichiers synthétiques, sans lecture de leur contenu.

**Essais**, tous dans `<cl3>/essais/`, sorties dans les fichiers `sortie_*.txt`. Commandes lancées depuis `/home/user/controle-ia`, avec `PYTHONDONTWRITEBYTECODE=1`, `--basetemp=<cl3>/pytest-tmp*` et `-p no:cacheprovider`.

1. `essai_d1_formules.py` (`PYTHONPATH=src`) : 22 cas réalistes, faux positifs et faux négatifs listés en E-3 et E-4 ; accord du module et des deux scripts, importés depuis des copies empreintées hors du dépôt, sur 200 000 chaînes : 0 écart.
2. `essai_d2_accord_aleatoire.py 1000` (`PYTHONPATH=src:tests`) : 1 000 dossiers de sorties et 1 000 avis mutés au hasard (graine 7), dont des textes en CRLF et des parties de 120, 200 et 25 000 caractères. Script scellé exécuté par `et.codes_du_script`, comme en production. Résultat : 0 écart, 0 exception, 26 codes rencontrés.
3. `test_cl3_scenarios.py` (pytest, `PYTHONPATH=src:<cl3>/essais:tests`) : 10 déroulés dans des dépôts jetables, tous conformes à ce que décrit le rapport :
   - E-1 : quatre altérations ;
   - E-6 : deux variantes ;
   - E-7 ;
   - D-2 : accord avec des retours chariot ;
   - D-3 : perte non consignée, et perte vue tardivement.
4. `<cl3>/pandoc/` : `synthetique.tex` et `variantes.tex`, convertis par le pandoc 3.9 de la roue `pypandoc_binary` du dépôt, avec la commande exacte de `corpus_arxiv.convertir`. Puis `essai_d1_citation_pandoc.py` : citation fidèle refusée, citation avec une espace acceptée, citation avec « \\n » introuvable.
5. Les deux fichiers de tests du dépôt : 118 réussis.
6. `traceur_cl3.py`, greffon pytest (`-p traceur_cl3`) : 66 gardes, 0 non exercée.
7. `<cl3>/correctif/src`, copie du code avec trois correctifs (E-1 : une ligne ; E-6 : `!r` dans trois messages ; E-7 : fichiers ajoutés sous `papier/`), et `test_cl3_correctif.py` (`-o pythonpath=`). Résultat : 123 réussis sur 124. Le seul échec est l'assertion de message de tx l. 52, attendu avec E-6.
8. Recalculs : probabilités binomiales et intervalles de Clopper-Pearson (scipy), résumé de l'essai à blanc, empreinte du code de découpage.
