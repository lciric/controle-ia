# SPARKS-EXP7-NUL — contre-lecture du delta v4 : brouillon 4, code v4 (`53d4eda6`) et répétition jouée

Contre-lecteur neuf (R2, sous-agent Claude, Opus 5.5). Je n'ai écrit ni le texte, ni le code, ni aucune contre-lecture
précédente. Consigne : `consigne-contre-lecture-delta-sparks-v4-v1.md`, compagnon « OK » avant lecture. Travail du
4 novembre 2026, de 23:40 à 23:58 UTC (`date -u`), interrompu une fois par un redémarrage du conteneur (repris vers 23:46
sans rien refaire). Lecture seule du dépôt et de l'arbre `/home/claude/wt/sparks-exp7-nul-v4` (`git status` vide avant et
après). Aucun commit, aucun `.sha256`, aucun réseau, aucun modèle, aucune dépense. Moins de 100 Mo employés au bloc-notes,
nettoyés.

## Verdict

**À reprendre : le code (v5) et la commande du tir réel. Le texte sera scellable après les 8 couples ci-joints et le tir réel.**
Le brouillon 4 est exactement brouillon 3 + K1 à K10 + H-1 à H-6, et les huit changements sont dans le code ; la répétition atteint ses attendus, mais deux d'entre eux pour une autre raison que celle annoncée.
Trois défauts bloquent : (1) le lanceur retire `VAST_API_KEY` (création, redémarrage et destruction de repli échouent, la destruction s'affiche « code 0 ») ; (2) la borne de la machine compte les plafonds, jamais les durées : la phase causale est refusée au coin haut du devis ; (3) le tir réel n'a pas de commande, et le lanceur ne peut pas le produire avant le scellement.

## Empreintes vérifiées (compagnons, depuis le dossier de chaque fichier)

Toutes « OK » :
- brouillon 4 `925c11fe…` et brouillon 3 `12e47e51…` ;
- rapport v4 `7eaaecb8…` et contre-lecture du delta v3 `cf2ffcb0…` ;
- les 8 compagnons de `contre-lecture-delta-v3-v1/`, les 2 de `brouillon4-addendum-1-v1/`, les 6 de
  `essais-et-banc-sparks-v4/` et les 10 de `repetition-jouet-v4-v1/` ;
- les 10 compagnons du commit `53d4eda6` (`git diff --name-status --no-renames 4c3bf146 53d4eda6` : 20 « A », aucun autre
  statut). Le script de répétition est égal à l'octet à celui de la section 5 du rapport.

## Points (gravité ; une ligne chacun)

### Q1. Brouillon 4 = brouillon 3 + K1 à K10 + H-1 à H-6
1. **Conforme.** J'ai rejoué le script (`4df7ed5f…`) sur une racine copiée, avec l'heure 23:05. Sortie identique à l'octet
   (`91a12e7c…`). L'empreinte intermédiaire est `4ea5636bc604000c2a47d895ed0ce536d1e5d8d4cb8cedd03550c63c794f512b`, égale au
   texte d'essai de la contre-lecture v3. Le brouillon rendu est identique à l'octet (`925c11fe…`) et garde 3 marqueurs. Le
   script ne fait que 10 + 8 remplacements, chacun unique au moment de son application. Les textes de H-1 à H-6 décrivent
   bien le code v4, sauf pour la clé de Vast (point 14).
2. **Mineur — noms restés de la v3.** On lit encore `scripts/amorce_instance_sparks_exp7_nul_v3.sh` et deux fois
   `sparks-v3-detruire`, alors que le code v4 pose `sparks-v4-detruire` (couples L1 à L3).
3. **Mineur — marqueur du commit final.** Il cite la branche `prep/sparks-exp7-nul-v2` (couple L8, marqueur gardé).
4. **Nœud (règle, non couplé) — tir avant scellement et GO.** L'extension de GO-2026-11-04-04 (`registres/go.md`, l. 245)
   dit « contre-lu et scellé avant tout lancement ». Or le texte exige un tir réel sur Vast **avant** le scellement. Ce tir
   est une dépense : il faut que la mère dise sous quel GO il tourne (ou qu'elle demande la décision à Lazar).

### Q2. Les huit changements, ligne par ligne (`scripts/amorce_instance_sparks_exp7_nul_v4.sh`, sauf mention)
5. **(1) `timeout` : fait.**
   - Bornés : clone, `sparse-checkout` et `checkout` (l. 109-114, `T_GIT`) ; `fetch`, `archive` et `tar` (l. 131-133,
     `T_ORDRES`) ; gardes Python (l. 98, 102, 104, 105, 119, 134, 141, `T_GARDE`) ; lot (l. 149) ; `vastai destroy`
     (l. 65) ; `borne_t` (l. 84), qui refuse tout allongement.
   - Restent hors `timeout`, sans danger : `git config` et `rev-parse`, qui sont locaux (l. 111, 129), et `sleep CM×60`,
     borné par `copie_minutes` ≤ 60.
   - Les étapes du script d'instance sont bornées par le seul `timeout` global du démarrage (jusqu'à 24 h). C'est voulu.
6. **(2) Attente sur `$!` : faite** (l. 73-79). Sans contrôle de tâches, `setsid` ne fourche pas, donc `PM` est bien la
   minuterie.
   - **Faible :** la dernière tentative de la minuterie peut finir jusqu'à MARGE + 245 s après la demande (`curl` 60 s, puis
     `vastai` 125 s, après un `sleep 60` passé `FIN`). L'attente, elle, s'arrête à MARGE + 120 s.
   - Correction proposée : ne pas lancer de tentative si maintenant + 190 s > `FIN`.
7. **(3) Ordres : fait.**
   - Branche `ordres/…-<court>` (l. 93).
   - Clé `instance` exigée (l. 134 ; `redemarrage.py`, l. 77-81).
   - `fait … || exit 2` (l. 141-142).
8. **(4) `deja_usd` et borne : fait.** Une baisse est refusée (`redemarrage.py`, l. 122-124). Le max est pris (l. 97-101,
   139). Les plafonds sont consignés avant chaque lancement (l. 121, 148, 156).
9. **Majeur — la borne de la machine rend le plan infaisable au coin haut du devis.**
   - La fabrication consigne son plafond (1 440 min, la borne de 24 h), et rien ne le remplace par la durée réelle.
   - La répétition le montre : après une fabrication de 1,5 min, « borne retenue 19.2013 USD » (`2-copie.txt`).
   - Mon calcul (`faisabilite-borne-machine-v1.py`, sortie jointe) prend une création le 5 novembre à 12:00, des copies de
     30 min et 6 h de fabrication réelle. À 0,80 USD/h de carte et 0,05 USD/h de stockage, seules 11 copies sur 14 ou 18
     sont admises, et la phase causale est **refusée** (13 min < 60). Le pire cas réel du devis vaut pourtant 29,8 à
     31,4 USD.
   - Le sens est prudent (refus, pas de dépassement), mais un refus à ce stade gâche la dépense déjà faite.
   - Correction : consigner à la fin de chaque démarrage sa durée réelle, mesurée par l'amorce. La borne prend la durée
     réelle quand une fin est consignée, et le plafond sinon (couple L6).
10. **(5) Branches des sorties : fait** (l. 94-95, 124, 158 ; script d'instance l. 21-22, 43). Dans la répétition, la
    branche causale est neuve et poussée : le défaut 21 de la v3 a disparu.
11. **(6) Lanceur : fait en partie.** `timeout`, sortie dans un fichier, marqueur, `--label` et variables du mandataire
    sont là. Restent les points 14 à 17.
12. **(7) Mutations : faites.** 30 neuves, 144 « TUÉE » dans le banc, 226 essais verts (je n'ai pas rejoué le banc).
    - **Faible :** aucune mutation ne retire la consignation du démarrage de fabrication ou de copie (l. 121, 148), ni le
      `timeout` de `sparse-checkout`, de `checkout` et des gardes `T_GARDE`.
13. **(8) Répétition : faite et jouée** (Q3).

### Q5. Lanceur v4 (`scripts/lancer_sparks_exp7_nul_v4.sh`)
14. **Majeur — `VAST_API_KEY` retirée.**
    - `prefixe_env` (l. 24-30) ne garde que PATH, HOME, LANG et les variables du mandataire. Or `vastai` lit sa clé dans
      `VAST_API_KEY` (R-032), et cette session n'a aucun fichier de clé (`~/.vast_api_key` et
      `~/.config/vastai/vast_api_key` absents).
    - Conséquence : création, `start` et `destroy` partent sans clé.
    - Démontré (`demo-lanceur-cle-et-r1506-v1.sh`, cas 1) : avec un faux `vastai` qui refuse sur stderr avec le code 0, la
      destruction de repli affiche « vastai destroy : code 0 ». L'essai `AUTRE_SECRET` ne passe pas, et c'est justement ce
      qui écarte la clé.
    - Correction : ajouter `VAST_API_KEY` à la liste, par son nom (couple L4).
15. **Conforme — R-1506 à la création.** Un code 0 sans identifiant n'est jamais un succès : il faut `new_contract` **et**
    « success » vrai (l. 39-41). Démontré : un refus sur stderr avec le code 0 donne « CRÉATION INCERTAINE (code 0) »,
    marqueur posé, code 4 (cas 2). La forme `--raw` en JSON est lue (cas 4). La commande imprimée n'emploie pas `--raw`,
    et les deux formes sont lues.
16. **Moyen — R-1506 au redémarrage et à la destruction.** Le lanceur n'imprime que « code $? » (l. 50, 85). Avec le code 0
    sur refus, ni le `start` ni le repli de destruction ne prouvent quoi que ce soit. Il faut une lecture de la sortie et un
    inventaire filtré après chacun (couple L5).
17. **Moyen — le certificat passe avant l'identifiant** (l. 36). Si la sortie contient une erreur de certificat **et**
    `new_contract` avec « success » vrai, le lanceur dit « NON PARVENUE » sans marqueur, alors qu'une instance existe
    (cas 3). Correction : tester d'abord l'identifiant, et ne lire le certificat qu'en son absence.
18. **Moyen — l'amorce passée n'est pas celle du commit.** `--args bash -c "$(cat scripts/amorce_…_v4.sh)"` (l. 75) lit
    l'arbre courant de la session, pas `COMMIT`. Remplacer par `"$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v<N>.sh")"`.

### Q3. Répétition jouée (`repetition-jouet-v4-v1/`)
19. **Attendus atteints, raisons à préciser.**
    - Étape 1 (« fabrication, durée plafonnée ») : la fabrication s'arrête à « essais en échec : 12 failed » et non à
      « 0/28 dans les bornes » (réserve 4 du rapport).
    - **Cause, reproduite par moi :** `env -i PATH="$J/faux-bin:/usr/bin:/bin"` ôte `/usr/sbin`, donc `chroot`, et la garde
      du bac refuse. Mêmes 12 échecs avec le même PATH (`sortie-essais-instance-path-sans-sbin-v1.txt`). C'est un artefact
      du jouet, pas du code : le PATH de l'image contient `/usr/sbin`.
    - Conséquence : ni le calcul jouet de fabrication ni celui de la phase causale n'ont été joués. Le « sans poussée
      vérifiée » de l'étape 3 vient des essais, non du calcul.
    - L'étape 2 (« lot impossible ») échoue sur `fabrication-v1.json` absent. Les étapes 4 (ordre 2 déjà fait) et 5 (fin,
      DELETE) donnent la bonne raison.
    - Les `grep` des attendus sont trop larges pour voir ces écarts.
20. **DELETE × 5 : artefact du jouet, non un défaut, sous une condition à éprouver.**
    - Le code ne tue jamais une minuterie antérieure. Il compte sur le conteneur : la sortie du processus principal tue
      tout l'espace de processus, et `vastai start` relance un conteneur neuf.
    - Dans le jouet, aucun espace de processus : les 5 minuteries (699, 3821, 3946, 6837, 6920) vivaient ensemble, lisaient
      le même `sparks-v4-detruire` et ont tiré à 23:38:57-23:39:00. Le « 1 » attendu par le rapport était faux pour ce
      dessin de jouet.
    - Vrai sur une vraie machine **si** le conteneur sort quand l'amorce sort. C'est à prouver au tir (point 24).
    - Correction de la répétition : chaque étape sous `unshare -pf --mount-proc`, qui marche dans cette session (code 0).
      Faible, en plus : l'amorce peut journaliser si le numéro de la minuterie précédente vit encore (`kill -0`), comme
      témoin.
21. **Moyen — branches restantes.**
    - Les ordres de `ordres/sparks-exp7-nul-v4-093c83596acf` ne peuvent valoir pour une vraie instance. Leur branche est
      liée au commit de répétition, et leur `"instance": "1"` ne peut égaler un `CONTAINER_ID` réel : double garde, sans
      danger.
    - **Mais** `essai/sparks-v4-repetition` (commit `093c8359…`) porte un addendum **fictif** que la garde de lancement
      accepte (« LANCEMENT CONFORME … addendum ae907caf5274 », `1-creation.txt`). `verifier_lancement` ne contrôle que le
      compagnon et la citation du commit du code. Un `COMMIT=093c8359…` passé par erreur lancerait donc un vrai calcul
      sans addendum réel.
    - Correction (code v5) : en `MODE=reel`, l'amorce et le lanceur exigent l'empreinte attendue de l'addendum scellé,
      passée à la création, ou bien un commit lancé descendant de `main`.
    - Suppression des 4 branches par Lazar, puisque le mandataire refuse les suppressions.
22. **Faible.** Le nettoyage de la répétition n'a arrêté aucune minuterie : toutes étaient sorties après leur DELETE simulé.
    Aucun processus ne reste.

### Q4. Ce que le tir réel doit éprouver, et sa commande
23. **Majeur — la commande n'est pas écrite.** Le lanceur v4 refuse avant d'imprimer quoi que ce soit sans addendum scellé
    (l. 64-67, garde `lancement`), et le tir doit précéder le scellement. Il faut un mode « tir » du lanceur (v5) :
    - offre la moins chère qui convient, même image, `--disk` réduit ;
    - échéance courte, au plus T + 60 min ;
    - étiquette `sparks-exp7-nul-tir-<court>` ;
    - même amorce, au commit du code. La création s'arrête alors d'elle-même à « code ou addendum non conformes » après le
      clone, et le conteneur sort ;
    - puis un ordre « fin » sur `ordres/…-<court>` et un `vastai start` ;
    - inventaire filtré à chaque pas.

    Le coût est de quelques dizaines de minutes de carte, sous le GO du point 4.
24. **À éprouver par ce tir :**
    - `curl`, `git`, `unshare`, `chroot`, `prlimit` présents dans `pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime` ;
    - ≈ 8 Ko passés par `--args bash -c` ;
    - clone partiel par le mandataire de Vast, avec sa durée ;
    - à la sortie de l'amorce, conteneur sorti, instance « exited », carte non facturée, minuterie morte (point 20) ;
    - `vastai start` relance les mêmes arguments et le même environnement ; l'amorce prend la voie « redémarrage »,
      relit l'échéance et lit l'ordre ;
    - ordre « fin » → `DELETE` par `CONTAINER_API_KEY` → instance introuvable à l'inventaire ;
    - corps de la réponse au DELETE : la minuterie croit tout 2xx (l. 63), alors que Vast peut répondre `"success": false`.
      Moyen : garder le corps, qui ne contient pas de secret, et refuser `"success": false`.

    Restent hors du tir, risque à déclarer : `vastai copy` depuis un conteneur lancé par ses arguments (il faudrait un lot)
    et un redémarrage quand la carte de l'hôte est louée par un autre.
    Une partie de cette liste est peut-être déjà acquise par les sondes d'A1-v3 (R-1497 à R-1506), si l'image et la
    minuterie sont les mêmes. Ce n'est pas vérifié ici.

## Changements de code requis (v5, R12 ; puis essais, banc, répétition, tir, contre-lecture neuve du delta)
1. Lanceur : `VAST_API_KEY` transmise par son nom (point 14) ; essai : le sous-processus la reçoit, aucune valeur n'est
   imprimée ; mutation.
2. Lanceur : identifiant et « success » vrai testés **avant** le certificat (point 17) ; `start` et `destroy` lus comme la
   création (refus sur stderr avec le code 0, R-1506) et suivis d'un inventaire filtré imprimé (point 16).
3. Borne de la machine : durée réelle de chaque démarrage consignée à sa fin, et plafond seulement sans fin consignée
   (point 9) ; essai au coin 0,80/0,05 ; mutation.
4. Garde de lancement en `MODE=reel` : empreinte attendue de l'addendum (variable de création), ou commit lancé descendant
   de `main` (point 21).
5. Création : amorce prise par `git show "$COMMIT:…"` (point 18).
6. Minuterie : corps du DELETE gardé, `"success": false` = échec (point 24) ; aucune tentative qui dépasse `FIN` (point 6).
7. Mode « tir » du lanceur, avec sa commande écrite et ses contrôles (point 23).
8. Répétition : PATH avec `/usr/sbin` et `/sbin`, chaque étape sous `unshare -pf --mount-proc`, attendus précis (« 0/28 »,
   échec du calcul jouet causal, `DELETE au journal : 1`), branches d'essai laissées à supprimer par Lazar (point 21).
9. Mutations du point 12.

## Fichiers (ce dossier, neufs, sans compagnon)
- `couples-brouillon5-v1.json` (`68230e9a…`) : 8 couples, L1 à L8, chacun unique dans le brouillon 4 et au moment de son
  application, 3 marqueurs gardés. Texte d'essai `56992343ecb410eddd520dec24962eb59ab228234caf236cbed35472a7558c9d` (non
  versé). L4 à L7 supposent les changements 1, 2, 3 et 7 ; L1 à L3 et L8 sont indépendants.
- `couples-brouillon5-contre-lecteur-v1.py` : script qui écrit et vérifie les couples.
- `faisabilite-borne-machine-v1.py` et `sortie-faisabilite-borne-machine-v1.txt` (point 9).
- `demo-lanceur-cle-et-r1506-v1.sh` et `sortie-demo-lanceur-v1.txt` (points 14 à 17 ; `vastai` factice, aucun réseau).
- `sortie-essais-instance-path-sans-sbin-v1.txt` : fin de la sortie des 226 essais d'instance sous le PATH de la répétition,
  12 échecs, cause `chroot` absent (point 19).
