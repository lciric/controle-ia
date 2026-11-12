# Brief de reprise — session mère sur Claude Code — 8 novembre 2026 — v2

Écrit par la session mère `session_016QhUrsAjLE7txxBLhnMnyM` (mère depuis 07:23 UTC, R-1765) le 8 novembre 2026 à 09:44 UTC (`date -u`), sur le mot de Lazar : « fais la passationa  une session claude code, on rperend dessus ». Tu ne connais rien des conversations précédentes : la continuité vit dans les fichiers. Lis `CLAUDE.md`, puis ce brief, puis `registres/passations/2026-11-08-0944.md`. Le brief v1 (`brief-reprise-nouvelle-mere-2026-11-08-v1.md`, `634d939f…`) reste valable pour les **commandes** de l'étiqueteur (sa section 3) et ses règles (sa section 6) ; ce brief le remplace pour l'état, la mise en place et l'ordre du travail.

## 0. Où on en est
1. **Épreuve de l'étiqueteur, phase 1** (test d'un étiqueteur automatique contre une construction connue ; deux lecteurs, Argon et Kimi, 456 items chacun) : générée, déposée chez le tiers, essai de format conforme. **Lecture principale prête, jamais lancée.** Il ne manque que les deux clés des lecteurs et la phrase écrite de Lazar **dans ta session**. La restauration et les contrôles ont été refaits entre 06:37Z et 06:51Z dans un autre conteneur, conformes (R-1765), mais ce conteneur n'est pas le tien : tu refais la restauration.
2. **Les clés** : Lazar dit qu'elles sont « dans l'env de claude code ». Une tâche programmée lancée depuis l'ancienne session (la « fille clés 1 », 09:21Z) n'en a trouvé **aucune des sept** et s'est arrêtée à son étape 0, sans rien lancer ni dépenser (`rapports/fille-cles-1-v1/`, R-1774). Une tâche programmée part dans l'environnement de la session qui la crée : les variables sont donc ailleurs, ou pas encore posées.
3. **Nul v9 de l'organisme** (neuvième version de l'hypothèse nulle du juge statistique qui promeut ou refuse les lois proposées) : **validation scellée finie**, code 0, de 08:16:01Z à 09:46:43Z, sur processeur, 0 dollar (R-1768, R-1774). Sortie scellée par le banc, **jamais ouverte**, poussée sur la branche privée `donnees/validation-nul-v9-v1` (commit `0705eb0e`). Reste le verdict par un lecteur neuf (3.3).
4. **Brèche de W2** (W2 : monde planté de l'attaque de Goodhart, où une loi vaut pour un groupe et une autre pour l'autre ; l'attaque cherche des lois que le juge promeut à tort) : note rendue (R-1768). 42 des 48 lois promues sous le nul v8 sont exactement la loi du monde ; la brèche n'existe que si « une loi par groupe » ne compte pas comme une découverte. **La question de sens est à Lazar, sans défaut.**
5. **T0.6** (fabrication d'organismes par adaptateurs à bas rang, puis lecture de leurs activations par des sondes) : **E3 bis close** (répétition de bout en bout sur une vraie machine, R-1769), conforme sauf **E3-6** (bloc `equivalence_99e_centile` absent pour les six états S100, S25, S50, S75, T100, dose0) ; réserve **E3-3** (45 pas déclarés, 4 entrées par adaptateur au journal des pas). **Contre-lecture neuve de la chaîne de la course en cours** dans le conteneur de l'ancienne mère (R-1770) ; elle te sera poussée.
6. **Pages publiques** à jour depuis ce matin : organisme `lciric/ideation-organism` commit `8947bc8` (R-1771) ; copie `lciric/controle-ia` commit `fc9acde` (R-1773).
7. **Organisme, code v65** (boucle réelle) : développeur arrêté par Lazar vers 07:45Z (R-1767) ; travail inachevé `c2c39794`, branche `prep/organisme-v65-boucle-reelle` du dépôt public ; **relance sur le mot de Lazar seulement**.

## 1. Mise en place
- **Dépôts** : `lciric/controle-ia-travail` (privé, en poussée ; `main` = dépôt de travail) ; `lciric/ideation-organism` (public ; poussée seulement sur un mot de publication de Lazar). **Ne jamais pousser le dépôt de travail vers `lciric/controle-ia`.**
- **Chemin** : clone le dépôt de travail **exactement** à `/home/user/controle-ia-travail` (l'ordre scellé de l'étiqueteur écrit ce chemin et `/home/user/controle-ia-travail/.venv/bin/python`). Si ta session ne peut pas créer ce chemin (par exemple une session sur l'ordinateur de Lazar), l'étiqueteur ne peut pas partir tel quel : changer un chemin scellé est un écart au préenregistrement, donc un nœud de Lazar. Tout le reste tourne partout.
- **Python** : `cd /home/user/controle-ia-travail && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` (numpy ≥ 1.25 ; ici Python 3.13.18 et numpy 2.4.6). Pour les essais du programme, un second environnement en Python 3.11 aux mêmes dépendances (ici `/home/user/venv311`), comme la fille 10.
- **Clés, par leur nom seulement** (jamais lire, afficher ni recopier une valeur ; jamais `env`, `printenv`, `set`, `export -p`, ni `/proc/*/environ`) :
  ```bash
  for N in GEMINI_API_KEY_2 KIMI_API_KEY VAST_API_KEY OSF_TOKEN HF_TOKEN CONTROLE_IA_GITHUB_TOKEN_2 GEMINI_API_KEY; do
    [ -n "${!N:-}" ] && echo "$N présente" || echo "$N absente"; done
  ```
  `GEMINI_API_KEY_2` (Argon) est **réservée à l'étiqueteur** (R-1754) ; `KIMI_API_KEY` passe par le relais local ; `VAST_API_KEY` sert à la course de T0.6 et à l'inventaire. Si elles sont absentes, dis-le à Lazar en une ligne : elles doivent être posées dans l'environnement de cette session Claude Code, puis il faut ouvrir une session neuve dans cet environnement. En attendant, fais le travail sans clé (section 3).
- **Réseau** : vérifie sans clé que `generativelanguage.googleapis.com`, `api.moonshot.ai`, `api.osf.io`, Vast, Hugging Face et GitHub répondent. Un refus par le réseau de la session (et non par le site) : dis à Lazar quels hôtes ouvrir.
- **Outil Vast** : `pip install vastai` dans `.venv` si absent ; aucune sortie brute affichée.
- **Mot de Lazar** : le contrôle de permissions refuse une dépense ou une publication sans le mot de Lazar écrit **dans la session qui l'engage**. Un texte de tâche programmée qui reproduit son mot n'en tient pas lieu.

## 2. Routine de reprise (règle R14), avec les résultats attendus
1. `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` → attendu : un seul problème, l'orpheline connue (R-1600).
2. Lis `registres/etat.md` (sections du 8 novembre) et la passation de 09:44.
3. Défauts échus : aucun à 07:23Z (R-1765) ; la question de sens de W2 n'a pas de défaut.
4. Inventaire Vast par identifiant (si la clé est là) : attendu 58936096, 58936099, 58936100 (instances de R8, arrêtées, laissées à Lazar : **ne jamais y toucher**) et 59288960 (« sparks-exp7-nul-v5 », arrêtée, stockage facturé 0,033 dollar par heure ; destruction par son identifiant avec `-y`, sur le mot de Lazar, puis `registres/arrets.md`). 59671807 (E3 bis) est détruite depuis 07:35:36Z.
5. Suite complète des essais **seule** sur la machine, avec un dossier temporaire propre : `python -m pytest -q --basetemp=<dossier neuf>`. Dernier passage (R-1767, 06:51Z → 07:41Z) : 2 539 passés, 5 échecs, 214 erreurs, tous de la machine (3 par `pypandoc` absent, hors de `requirements-cpu.txt` ; le reste par disque plein et par la rotation des dossiers temporaires, partagés entre trois sessions). Elle n'est pas certifiée.

## 3. Ordre du travail
**3.1 Étiqueteur — première action si les deux clés des lecteurs sont là.** Suis le brief v1, sections 3.1 à 3.4, à la lettre. Écart connu et sans effet : `relais-format/console-relais-kimi-v1.log` manque à l'archive par construction (journaux de console exclus) ; le contrôle des empreintes de l'essai de format donne 15 « OK » sur 16. Tout autre écart est un arrêt. Avant le bloc 19, demande à Lazar d'écrire dans ta session : « go lecture principale de l'étiqueteur sous GO-2026-11-07-07 et GO-2026-11-08-03 » (GO-2026-11-07-07 : son accord du 7 novembre pour la dépense de la phase 1, plafond 300 dollars ; GO-2026-11-08-03 : sa levée, le 8 au matin, du contrôle des factures de l'essai de format). Dépense attendue : environ 35 dollars au barème scellé, 3 à 4 heures. Le compte rendu restauré ne porte pas la section de la reprise de 06:37Z à 06:51Z : ajoute la tienne et cite R-1765. Pendant la lecture, fais 3.2 à 3.5.

**3.2 Rendus de l'ancienne session.** Relève : `git ls-remote origin refs/heads/donnees/validation-nul-v9-v1 refs/heads/prep/contre-lecture-t06-course-v2-b refs/heads/rapports/garde-ancienne-mere-v1`. Récupère chaque branche par une refspec explicite ; vérifie les compagnons `.sha256`. La contre-lecture s'intègre à `main` (avec une ligne de décision) ; la sortie de la validation reste sur sa branche jusqu'au verdict.

**3.3 Validation du nul v9 (0 dollar).** Texte scellé : `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` (`54c5713d…`), commit `66dbcf1` du dépôt public de l'organisme. Sortie : branche `donnees/validation-nul-v9-v1`, dossier `diag/validation-nul-v9-v1/` (lis d'abord son `LISEZ-MOI-validation-nul-v9-v1.md` : commande, heures, empreintes ; `banc-tricheurs-v9.json` `be22bf67…`). Un **lecteur neuf** (ni auteur du texte, ni lanceur, ni toi) applique les critères gelés à la sortie scellée et dit si le v9 tient son erreur et ce qu'il coûte en puissance ; tu scelles le verdict (règle R13), puis tu le soumets à Lazar. La publication de la sortie et du verdict sur le dépôt public est un nœud de Lazar.

**3.4 Chaîne de la course de T0.6.** Applique les couples de la contre-lecture (un couple remplace un « ancien » trouvé une seule fois par un « nouveau ») ; corrige E3-6 et lis E3-3 ; puis scelle, dans cet ordre : addendum v3 du bras B (**avant toute lecture**), candidat 12 révision 2, ordre de la course v2, devis v3 (pièces des branches `prep/t06-bras-b-v4` `84a62edd`, `prep/t06-course-v12` `7822a65b`, `prep/t06-ordre-course-v2` `8cb539f9`). Puis la course, avec `VAST_API_KEY` et le mot de Lazar dans ta session : GO-2026-11-02-28 (plafond 200 dollars) ; carte GO-2026-11-07-02 (A100 SXM4 de 80 Go à 1,30 dollar par heure au plus pendant 3 heures de recherche, sinon H200 NVL à 4,70 au plus). Devis v3 : environ 18 à 28 dollars sur A100, 46 à 78 sur H200 NVL ; **pire cas environ 198 sur 200** ; débit de la H200 NVL non mesuré. Lazar veut la course tout de suite (« lance les courses du 11 nov now ») : le chemin le plus court est celui-ci, rien ne le saute (règle R1).

**3.5 Organisme.**
- **Suite de W2** (note `docs/notes/ideation-organisme-v1/breche-w2-v1/note-breche-w2-v1.md`, section 2 ; ajouts à la course réelle : section 3) : question de sens (Lazar) ; rejeu des 48 lois sous le v9 (texte à sceller d'abord ; 0 dollar ; 9 600 évaluations, 40 à 46 minutes sur un cœur aux durées mesurées) ; W2 gradué (texte à écrire ; 0 dollar) ; attaque v4 sur W2 et W2 gradué à la place de W1 (clé d'Argon ; 68 à 104 dollars ; changement de périmètre : nœud de Lazar).
- **Code v65** : sur le mot de Lazar, un développeur neuf repart de `c2c39794` (consigne `docs/notes/organisme-boucle-reelle-v1/consigne-developpeur-organisme-v65-v1.md`, `2dc207e7…`) et revérifie tout ; puis contre-lecture, machine à bac à sable `bwrap` (5 dollars au plus), texte scellé, course (GO-2026-11-08-02 : 40 dollars de modèles et 5 de machine). Les ajouts proposés par la note W2 (juge v9 en ombre en génération 2, forme de chaque carte, porte d'héritage, deux témoins plantés) se décident avant le scellement.
- **Courses d'idéation sur les deux projets** (demande de Lazar : « trouver des expériences, idées ou résultats inédits ») : clés de Kimi et d'Argon, devis, puis son GO.

**3.6 Les trois faiblesses** (demande de Lazar du 8 novembre au matin) : la sonde du run R1 lit la consigne (fuite établie) ; les sondes génériques sont au niveau du hasard ; le juge de 3 milliards de paramètres est au hasard (0,523, p = 0,19). Il veut des sondes qui ne lisent pas la consigne, qui battent des directions au hasard, et un juge meilleur que le hasard, « quitte à prendre un modèle plus gros et à scaler ». L'ancienne mère a répondu et reformulé sa demande **dans la conversation seulement** ; demande-lui de confirmer ou de recoller la reformulation avant d'en faire un texte. Changer de modèle demande son GO.

## 4. Nœuds de Lazar en attente (rien ne part sans son mot)
- phrase de la lecture principale de l'étiqueteur (3.1) ;
- question de sens de W2 : Q1 et Q2 de la note (section 5) ;
- périmètre de l'attaque v4 ;
- ajouts à la plus petite course réelle de l'organisme ;
- relance du développeur v65 ;
- accord sur la reformulation des trois faiblesses ;
- devis des courses d'idéation ;
- destruction de 59288960 ;
- publication de la validation du v9 après son verdict ;
- nœuds plus anciens : `registres/etat.md`, section « GO et nœuds en attente ».

## 5. Ce que fait encore l'ancienne session, et les replis
L'ancienne session **n'écrit plus sur `main`**. La validation du v9 est déjà poussée (`donnees/validation-nul-v9-v1`, `0705eb0e`). Il lui reste un travail, puis elle s'arrête :
- **contre-lecture de la chaîne de la course** (sous-agent neuf lancé avant 09:11Z, R-1770 ; deux heures au plus ; consigne `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2-consigne-v1.md`, `dcb21799…`) → branche `prep/contre-lecture-t06-course-v2-b`, sous `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/`, avec les compagnons `.sha256` ;
- un compte rendu court (heures, codes, empreintes) → branche `rapports/garde-ancienne-mere-v1`.

**Si la branche de la contre-lecture manque à 13:00Z** (conteneur repris), relance-la toi-même : un sous-agent neuf, même consigne, arbre neuf au commit `8cb539f9`, avec les deux constats d'E3 bis à vérifier (E3-6 et E3-3).

## 6. Règles et leçons (en plus de `CLAUDE.md` et du brief v1, section 6)
- Un processus détaché ne survit à la fin d'un tour que si une tâche de fond suivie tourne encore : garde toujours un guet lancé en fond (R-1765).
- Disque : deux environnements Python (5,6 et 5,7 Go) et le cache de pip (3,8 Go) ont rempli le disque le 8 novembre (R-1767) ; `pip cache purge` après chaque installation.
- Clone peu profond : un commit manquant se récupère par `git fetch --depth=1 origin <empreinte complète>`.
- Poussée vers un dépôt public : le contrôle de permissions la refuse sans un mot de Lazar qui nomme l'action et le dépôt (R-1770, R-1771). Ne jamais contourner un refus, ni le faire faire ailleurs.
- La copie `lciric/controle-ia` est publique depuis R-1773 (décision de Lazar, pour cette copie seulement) ; le dépôt de travail reste privé.

## 7. Empreintes et commits utiles (en plus du brief v1, section 7)
| objet | chemin ou référence | empreinte ou commit |
|---|---|---|
| passation de ce brief | `registres/passations/2026-11-08-0944.md` | compagnon `.sha256` |
| rapport de la fille clés 1 | `rapports/fille-cles-1-v1/compte-rendu-fille-cles-1-v1.md` | `f6b8620c…` ; branche au `7d0c5cee` |
| note sur la brèche de W2 | `docs/notes/ideation-organisme-v1/breche-w2-v1/note-breche-w2-v1.md` | `4d3a6d1c…` ; zip `livrables/breche-w2-v1.zip`, `b7fb0531…` |
| texte scellé de la validation du v9 | dépôt public, `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` | `54c5713d…`, commit `66dbcf1` |
| sortie de la validation du v9 (jamais ouverte) | `donnees/validation-nul-v9-v1`, `diag/validation-nul-v9-v1/` | commit `0705eb0e` ; `banc-tricheurs-v9.json` `be22bf67…` |
| verdict de la troisième course de l'attaque | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` | `7dade9ef…` |
| consigne de la contre-lecture de la course | `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2-consigne-v1.md` | `dcb21799…` |
| compte rendu final d'E3 bis | `rapports/fille-6-e3bis-v1`, `compte-rendu-e3bis-v3-3.md` | commit `b1ee1ce7` ; run sur `essai/t06-e3bis-v1`, `a5c0e298` |
| pages publiques | `lciric/ideation-organism` ; `lciric/controle-ia` | `8947bc8` ; `fc9acde` |
| décisions de cette session | `registres/decisions.md` | R-1765 à R-1774 ; GO-2026-11-08-04 |
