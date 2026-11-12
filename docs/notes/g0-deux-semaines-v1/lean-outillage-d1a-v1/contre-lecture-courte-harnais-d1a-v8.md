# Essai Lean, D-1a — contre-lecture courte du harnais v8 (second tour de la v7), avant tout usage sur une machine

- **Lecteur** : sous-agent neuf (Claude Fable 5.2), qui n'a écrit aucun des fichiers lus (R2). Date : 2026-11-12 (UTC).
- **Objet** : branche `prep/lean-outillage-d1a-v7`, code `32a40613eb1ec006cbee4144e1ec94dfe84e8237`, procédure à `67ab6fc7`
  (`procedure-poste-local-d1a-v8.md`, `f3a3a5a8…`) ; base de comparaison `149babdc` (harnais v6).
- **Demandes** : les six corrections de R-2421 (`registres/decisions.md`) ; rapport du premier essai
  `rapport-poste-local-d1a-v1.md` (`c0938a8fea417a878217276dc56bf042de7412bb1d662e146a44f3dfadb26662`, vérifiée), sections
  Incidents et Écarts.
- **Lu** : `installer_chaine_v2.sh` contre v1 ; `piloter_poste_v8.sh` contre v6 ; `essai_lecture_bac_v1.sh` ;
  `mutations_harnais_v8.py` ; `minuterie_v7.py` contre v6 ; `sonde_reseau_v2.py` contre v1 ; les trois fichiers d'essais ;
  la procédure v8 ; le journal des mutations v8 ; et, pour suivre les appels, `garde_go_v1.py`, `minuterie_v2.py`,
  `minuterie_v4.py`, `hetzner_v3.py`, `couper_reseau_v1.sh`, `epreuve_isolement_v4.py`, `executeur_bac_v4.py`, deux relevés de
  sonde du premier essai. Les compagnons `.sha256` des dix fichiers neufs sont égaux aux empreintes recalculées. Les fichiers
  v1 à v6 ne sont pas modifiés entre `149babdc` et `32a40613` (R12).
- **Rejoué ici** (arbre de travail jetable à `32a40613`, en root, aucun réseau payant, aucun serveur, aucun jeton) :
  - `PYTHONPATH=src .venv/bin/python -m pytest -q -k lean_essai` : **613 passés**, aucun sauté (les essais à `runuser` ont
    tourné, root) ;
  - `mutations_harnais_v8.py` : témoin 111 passés, **141 mutations sur 141 tuées**, aucune par délai, égal au journal versé ;
  - une mutation de plus, à la main : « nom inexistant » lu « fermée » dans la sonde v2 : tuée (2 essais en échec) ;
  - quatre épreuves à la main, décrites aux constats 7, 12 et 13.

## Verdict

**Utilisable après corrections.** Le code de `32a40613` fait les six corrections sans régression de sécurité, et ses gardes
neuves sont éprouvées (cas sain et artefact) et bruyantes. Mais la procédure v8 ne peut pas être suivie telle qu'elle est
écrite : elle prescrit un GO neuf que le code refuse.

### Liste bloquante

1. **GO du second essai : la procédure v8 et le code se contredisent** (constats 12 et 13). La procédure (lignes 63 à 65,
   159, 245) fait porter aux commandes « `<GO de la consigne>` : un GO neuf est nécessaire ». Or `preparer`, `creer-et-armer`
   et le client de création refusent tout identifiant autre que `GO-2026-11-10-13`, écrit en dur
   (`garde_go_v1.py:21` et `:88-93`). Avec un GO neuf, L1 s'arrête avant tout appel. Il faut choisir une des deux voies
   du constat 13 et corriger la procédure (ou le code) avant d'écrire la consigne. C'est un nœud : la mère et Lazar
   tranchent.

Rien d'autre n'est bloquant. Quatre précautions pour la consigne, non bloquantes : constat 10 (préfixe quand la mesure
est douteuse ; clé d'hôte d'une adresse réattribuée), constat 11 (lisibilité du vérificateur), constat 14 (déjà-dépensé
déclaré).

## Constats

### Question 1 — les six corrections de R-2421

1. **Lecture par `bac` et essai R5 avant la coupure : fait.** `installer_chaine_v2.sh:83` ajoute `chmod -R a+rX` sur
   `/opt/elan`, `/opt/mathlib`, `/opt/pybac`, après `go-w` (`:82`) et avant les montages en lecture seule (`:97-104`).
   Garde de lisibilité `:29-46`, appelée `:84-96`, arrêt code 5 avec ligne « ARRÊT » au journal. `essai_lecture_bac_v1.sh`
   (cas sain : un octet vraiment lu ; témoin 0644 ; artefact 0600) est lancé par le pilote à la fin de « avant »
   (`piloter_poste_v8.sh:46`), donc avant la coupure. Sécurité : le droit ajouté est la lecture seule, sur des arbres
   publics (chaîne, Mathlib, Python) ; aucune écriture rendue ; le propriétaire distinct et les montages `ro` restent.
   Aucun secret n'est sur la machine. Pas de régression de l'isolement de `bac`.
2. **`scp` en `accept-new` et `~/.ssh` en 700 : fait.** `piloter_poste_v8.sh:33` et `:35`. Même confiance au premier
   contact que `ssh` avait déjà (`:32`) ; une clé différente d'une clé connue reste refusée. Pas de régression.
3. **Sonde sur un nom aléatoire jamais demandé : fait.** `sonde_reseau_v2.py:90-104` ; les trois sondes du pilote sont la v2
   (`piloter_poste_v8.sh:45`, `:52`, `:63`). L'exécuteur du bac garde la v1 (`:54`), couverte par le vidage du cache (`:51`).
4. **Source du pare-feu en /24, contrôlée, mesure à la section 0 : fait.** Voir constats 8 et 10 ; procédure v8, lignes 137 à 140.
5. **`fichier_pousse` sur clone `--single-branch` : fait par la procédure, pas par le code.** `fichier_pousse`
   (`minuterie_v7.py:776-806`) est identique à la v6. La procédure v8 (L3, lignes 195 à 198) prescrit la référence de suivi.
   Épreuve à la main sur un clone `--single-branch` local : après `git push -u`, la garde refuse (« branche sans amont ») ;
   après la recette de L3, `@{upstream}` rend `origin/<branche>` et la garde passe ; un commit non poussé est de nouveau
   refusé. La recette tient. Réserve mineure : le message de la garde (« pousser avec `git push -u` ») n'indique pas la
   recette ; la consigne doit la reprendre mot pour mot.
6. **Procédure (WSL, jeton de `gh` par l'environnement, essai à blanc par relance réelle) : fait.** Procédure v8, section 0,
   points 1 et 4 (lignes 114 à 118, 130 à 133). Le contrôle par l'heure de démarrage des processus est vérifiable.

   Sécurité d'ensemble : la coupure (`couper_reseau_v1.sh`, `regles_coupure_reseau` `minuterie_v7.py:113-116` : seule règle
   sortante ICMP vers `192.0.2.1/32`, inchangée), `verifier-coupure`, la destruction par identifiant (R10), la minuterie et
   la création ne changent pas : le différentiel v6 → v7 de la minuterie ne touche que la source SSH, `adresses-sortie`,
   `garde-poste` et les noms. Aucun jeton n'est lu, écrit ni envoyé par le code neuf.

### Question 2 — gardes neuves, R5, bruit

7. **Éprouvées sur cas sain et artefact, et bruyantes.**
   - Garde de lisibilité : `tests/test_lean_essai_pilote_v8.py:58-90` (arbre sain ; `.olean` 0600 ; autres artefacts ;
     arbre absent : code 2) et `:111` (`runuser`, sain et artefact, joué ici en root). Échec : code 5, « ARRÊT » au journal.
   - Essai de lecture : `:233` (0644 : code 0 ; 0600 : code 1), joué ici. Le pilote s'arrête (`set -e`).
   - Sonde v2 : `tests/test_lean_essai_sonde_v2.py:35` (l'artefact du premier essai), `:55` (quatre classes), `:60`.
   - Source en réseau, adresses de sortie, /24 de garde-poste : `tests/test_lean_essai_minuterie_v7.py:1114-1191` et `:450`.
   - Mutations l01 à l11, s01 à s03, f01 à f08 : toutes tuées.
   - Limite : la suite de l'installateur (`:83-96`) n'a jamais tourné sur une machine ; ses fonctions sont éprouvées par
     extraction, son ordre par lecture du texte. La procédure le dit (ligne 17).

### Question 3 — source en /24

8. **Bornée à 24 au plus large, à deux endroits.** `source_poste` (`minuterie_v7.py:93-101`) refuse tout préfixe hors de
   24 à 32, les booléens et les non-entiers ; `regles_installation_reseau` (`:104-110`) refuse de nouveau une source plus
   large que /24. `acces-creer` (`:839`, `:847`) et `acces-couper` (`:871`) passent tous deux par là ; défaut 32 (`:1095`).
   Un refus ne pose aucune règle (essai `:1138`). **`garde-poste`** refuse toute adresse `a.b.c.x` du /24 du poste
   (`:1033-1034`), `a.b.c.0/24` comprise ; `masquer_regles` masque déjà toute source. Le fichier d'accès ne porte ni adresse
   ni règle (essai `:1151`).
   - Réserve ancienne, non une régression : `verifier-coupure` (`hetzner_v3.py:92-109`) ne juge que les règles sortantes ;
     la largeur de la source entrante n'est relue par aucune garde après la pose. Elle n'est bornée qu'à la pose.
   - Le préfixe n'est pas lié à la mesure : `--prefixe-poste 24` est accepté sans `adresses-sortie`. C'est conforme à
     l'accord de Lazar (/24 accordé) ; la mesure conseille, elle n'autorise pas.

### Question 4 — classement de la sonde v2

9. **Le relevé d'ensemble ne peut pas donner un faux « fermée » par la seule cible du résolveur ; la cible seule le peut,
   moins que la v1.**
   - La cible « résolveur système » lit « fermée » sur `EAI_AGAIN` (`sonde_reseau_v2.py:102-103`). `EAI_AGAIN` vient aussi
     d'un résolveur local arrêté ou d'un résolveur amont en panne, sortie ouverte. Donc cette cible, seule, peut dire
     « fermée » à tort.
   - Mais `juger` (`:129-137`) exige « fermée » sur **chacune** des sept cibles extérieures : trois TCP et trois DNS UDP
     directs, par adresse, sans résolveur. Une sortie ouverte laisse passer au moins celles-là. Le faux « fermée »
     d'ensemble demanderait une sortie ouverte par une voie qu'aucune cible ne sonde (ancienne limite de la v1, inchangée ;
     IPv6 est désactivé à la création).
   - La v2 est strictement plus sévère que la v1 : la v1 lisait « fermée » sur toute erreur de résolution ; la v2 seulement
     sur `EAI_AGAIN`, « ouverte » sur `EAI_NONAME` et `EAI_NODATA`, « indéterminée » (toujours un écart) sinon.
   - Fait de terrain : le relevé du premier essai après coupure (`apres-essai2-sonde-apres-coupure-v1.json`) porte
     « résolution impossible (-3) », soit `EAI_AGAIN` : la machine coupée rend bien le code que la v2 attend. Le risque
     inverse (faux « ouverte » ou « indéterminée » après coupure) arrêterait le pilote, bruyamment.
   - `resolvectl flush-caches` réussi juste avant (`piloter_poste_v8.sh:51`) prouve en plus que `systemd-resolved` tourne :
     le cas « résolveur arrêté » est écarté pour la sonde d'après coupure.

### Question 5 — `resolvectl flush-caches` et `adresses-sortie`

10. **`resolvectl flush-caches`** (`piloter_poste_v8.sh:51`) : sans risque pour l'isolement ; il vide, il n'ouvre rien, et
    réseau coupé le cache ne se remplit plus. S'il manque ou échoue, le pilote s'arrête après la coupure, serveur vivant :
    fin par la section 5 de la procédure, coût d'une heure. `systemd-resolved` était présent au premier essai (rapport,
    incident 6).
    **`adresses-sortie`** (`minuterie_v7.py:119-150`, `:1159-1162`) :
    - 16 requêtes HTTPS à `api.ipify.org`, sans en-tête d'authentification, sans jeton ; le service ne voit que l'adresse du
      poste, qu'il verrait de toute façon. La sortie ne porte que des comptes (essais `:1161`, `:1184`). Acceptable.
    - Une réponse fausse du service ne peut pas élargir au-delà de /24 : elle ne choisit qu'entre 32, 24 et l'arrêt.
    - Dépendance à un tiers : service muet → code 1, aucune préparation (sûr). `--service` permet un autre service ; la
      consigne doit alors le nommer, l'argument n'est pas contrôlé.
    - Mesure faible dans deux cas : une seule réponse sur 16 suffit à conseiller un préfixe ; et si la traduction d'adresse
      du réseau du poste est collante par destination, les 16 réponses peuvent rendre la même adresse et conseiller 32 à
      tort. Effet : SSH joignable par intermittence, comme au premier essai (temps perdu sur un serveur payant, pas un
      défaut de sécurité). **Précaution pour la consigne** : le premier essai a établi que ce poste sort par
      plusieurs adresses du même /24 (rapport, incident 4). Si la mesure rend 32 sur ce même réseau, le signaler à Lazar
      avant L2 plutôt que de poser une règle à une seule adresse ; jamais plus large que 24.
    - Le mandataire : `urllib` suit le mandataire de l'environnement ; l'essai à blanc de la section 0 (point 4) le contrôle
      avant.

    **Clé d'hôte d'une adresse réattribuée** (précaution, hors des six corrections) : si le second serveur reçoit une
    adresse IPv4 déjà inscrite dans `known_hosts` du poste (celle du premier serveur, par exemple), `accept-new` refuse et
    le pilote s'arrête à la première copie, serveur payant en marche. La consigne peut prescrire, après L5,
    `ssh-keygen -R <adresse du serveur>` avant le pilote.

### Question 6 — lisibilité du vérificateur du noyau copié par `scp`

11. **Non bloquant ; précaution conseillée.** `piloter_poste_v8.sh:53` crée `/opt/harnais/noyau` en 0755 ; `:56` y copie
    `verificateur_noyau_v4.lean` par `scp` sans `-p` : le fichier prend les droits du fichier du poste, sous le masque de
    root du serveur. Il est lu par Lean **sous `bac`**, par un montage lié (`executeur_bac_v4.py:367`). Clone du poste en
    0644 (masque 022, cas ordinaire de WSL) : lisible. Clone en 0600 (masque 077) : `bac` ne le lit pas, G-L7 échoue,
    `noyau` non conforme, arrêt du pilote (`:59`, `set -e`). L'échec est bruyant et sans effet sur l'isolement ; il coûte un
    essai. Le premier essai ne l'a pas éprouvé (arrêt à G-L1). **Précaution pour la consigne**, sans toucher au code :
    avant le pilote, `stat -c %a src/controle_ia/lean_essai/verificateur_noyau_v4.lean` doit rendre `644` sur le poste
    (sinon `chmod 644` de ce fichier dans le clone, sans commit). Pour une version suivante : `chmod 0644` côté serveur et
    le fichier ajouté à l'essai de lecture (`essai_lecture_bac_v1.sh` prend déjà un chemin en argument).

### Question 7 — seconde préparation sous un GO dont la dépense est inscrite

12. **Non : l'inscription de la dépense ne fait pas refuser la seconde préparation.** Épreuves à la main sur
    `minuterie_v7.preparer`, horloge fixée au 12 novembre :
    - A. registres de la branche `32a40613` (sans ligne de dépense), `V` sans pièce du premier essai, `GO-2026-11-10-13` :
      **acceptée** ;
    - B. `registres/depenses.md` et `registres/go.md` de `main` (dépense de 0,28 USD inscrite, ligne 422), `V` sans pièce :
      **acceptée**. `machines_anterieures` (`minuterie_v4.py:120-128`) cherche `Hetzner\s+(\d{6,})`
      (`minuterie_v2.py:32`) ; la ligne inscrite dit « Hetzner ccx33 hel1, serveur 175751342 » : aucun motif trouvé, liste
      vide. La garde « seconde machine » ne lit donc pas la dépense telle qu'elle est écrite ;
    - C. `main` plus le journal des créations du premier essai dans `V` : **refusée** (« journal : intention 7b833a33… ») ;
    - D. `main` plus l'ancien fichier `rattrapage-machine-d1a-7b833a333f09-v1.json` dans `V` : **refusée** (CLC5-03) ;
    - E. un GO neuf fictif, ligne valide dans `go.md` : **refusée**, « GO cité …, GO-2026-11-10-13 attendu ».

    Le refus d'une seconde préparation tient donc aux **pièces du premier essai présentes dans `V`** (cas C et D), non à
    la ligne de dépense. L'affirmation de R-2424 (« refuse … une fois sa dépense inscrite ») et le point 7 de la procédure
    v8 sont inexacts sur ce point. Défaut ancien (v2 et v4 de la minuterie), non une régression du second tour.

13. **Ce qu'il faut exactement pour un second essai — deux voies, une seule à retenir.**
    - **Voie (a), sans changer le code, sous `GO-2026-11-10-13`** (R-2421 : il couvre le second essai). Il faut : une
      branche du poste partie de `32a40613` (ou de `67ab6fc7`), dont `V` ne contient **ni** fichier
      `rattrapage-machine-d1a-*-v1.json` **ni** `journal-creations-machines-v1.jsonl` du premier essai ; la ligne
      `GO-2026-11-10-13` dans le `registres/go.md` du clone (elle y est) ; les commandes avec `--go GO-2026-11-10-13`. La
      procédure v8 se corrige alors au point 7 et aux lignes 159 et 245 (plus de « GO neuf »). À savoir : la garde « une
      seule machine par GO » est ainsi contournée par construction ; c'est un choix à écrire dans la consigne, pas un
      silence.
    - **Voie (b), sous une ligne de GO neuve** (lecture de R-2424). Il faut alors **du code neuf**, sous des noms neufs
      (R12) : l'identifiant attendu de `garde_go_v1.autoriser_creation_machine` (`garde_go_v1.py:21`, `:88-93`), appelé par
      `minuterie_v7.preparer` (`minuterie_v7.py:717`), par `creer_et_armer` (`:936`) et par le client de création
      (`hetzner_v4.py:44`) ; plus la ligne du GO neuf, de type « calcul », accordée par Lazar, en cours de validité,
      **présente dans le `registres/go.md` du clone du poste** (la branche du poste doit la porter) ; essais, mutations et
      contre-lecture courte de ce seul différentiel. Sans cela, L1 échoue avant tout appel (cas E) : sûr, mais l'essai n'a
      pas lieu.
    - Dans les deux voies, le motif `Hetzner\s+(\d{6,})` gagnerait à lire les lignes de dépense telles qu'elles s'écrivent
      (« serveur N ») ; à défaut, la garde « seconde machine » ne repose que sur les pièces de `V`.

14. **Déjà-dépensé déclaré** (procédure v8, ligne 246 : `--deja-depense-usd 0`). Sous la voie (a), le GO porte déjà
    0,28 USD : déclarer `0.28`, pour que le devis compte la dépense réelle (une déclaration inférieure au registre est
    refusée, supérieure est admise). Sous la voie (b), `0` est exact. Sans effet sur le plafond de 65 USD, mais le chiffre
    doit être juste.

## Ce qui n'a pas été fait

- Aucun appel à Hetzner, aucun serveur, aucune requête à `api.ipify.org` (essais sur faux lecteur seulement).
- Rien n'a tourné sur une machine Ubuntu de l'essai : l'installateur v2 en entier, `resolvectl`, la sonde v2 sur un vrai
  résolveur restent à voir au second essai. Le seul fait de terrain repris est le code `-3` du premier essai (constat 9).
- Les fichiers hors de la liste de lecture (procédure v7, premier tour `65167979`, pilote v7) n'ont pas été contre-lus.
