# Marche à suivre — lancement réel de la course d'idéation (voie (β), GO-2026-10-28-14) — v1

Lignée session-depot, sous-agent de préparation. Relevés `date -u` : début **08:52 UTC**, écrit à **09:10–09:25 UTC**, le
29 octobre 2026. Rien n'est lancé, rien n'est payé, aucune clé lue, aucun appel à un modèle. Sources : devis v6 (« Ordre »),
v7 à v7 octies (`43fc1d2a…`) de `refs/canal-local/conv-audit` (c9370d09) ; LISEZMOI v31 à v43 ; CL9 et CL10 ; `registres/go.md`
(GO-2026-10-28-14, ligne (β) du 29 octobre, 52,8 USD, enveloppe 60) ; `registres/decisions.md` (R-379 de conv-audit, R-383,
R-656, R-663, R-675, R-715, R-718, R-720, R-735, R-737).

## En tête

**Durée totale estimée jusqu'au classement à trois juges : ≈ 5 h 30 (fourchette 4 h 30 à 8 h) à partir de l'arrivée de la v44**,
soit, si la v44 arrive vers 10:00 UTC, un classement vers **15:30 UTC (14:30 à 18:00)** — dans la fenêtre d'autonomie jusqu'à
≈ 16:45 UTC (R-735) au mieux, au-delà au pire. Détail : v44 reçue et vérifiée 0:15 ; relecture ciblée v43 → v44 (CL11) 0:45
à 1:15 ; préparation de la machine, pièces, liste, attestation du matériau 0:45 à 1:00 (en parallèle de CL11) ; mesure v44 et
mot de passage 0:15 ; course 1:15 (0:45 à 3:00) ; lecture et attestation 1:00 (0:45 à 1:30) ; bras 0:15 (0:10 à 0:40) ;
versement 0:20.

**Bloquant neuf, trouvé par la mesure (démontré) — à corriger dans la v44, sans quoi aucun lancement :** `anonymiser`
(`pole/ideation.py` l. 567) normalise la typographie **sur le texte JSON** des fiches : un « » ou “ ” dans une valeur devient
un `"` non échappé, `json.loads` lève `JSONDecodeError`. Quatre des six témoins du tiers contiennent « ; toute fiche écrite
en français par un proposeur en contiendra. Dans la course, l'appel vient **après toutes les passes des proposeurs, avant le
premier juge** : course arrêtée, aucune note, dépense des proposeurs perdue (au pire ≈ 28,6 + 0,4 USD Claude et ≈ 8,7 USD
Argon). Démontré : `--mesurer-consignes` avec les témoins (code 2) et course simulée (`travail/sim-guillemets/manifeste-fin.json` :
trois passes jouées et comptées, puis l'arrêt). Correction : normaliser valeur par valeur (`json.loads(json.dumps(...))` puis
parcours des chaînes), essai avec une fiche et un témoin à guillemets français servis aux juges. **À transmettre à conv-audit
tout de suite (v44).** Les témoins n'ont pas à changer.

**Ce qui dépend de la v44** (garde par passe d'Argon avec provision, vraie option de plafond de passe 2, reprise des contrôles
Claude ; plus le correctif ci-dessus) : le nom exact de l'option du plafond de passe 2 (étape 9) ; le réglage de la garde de
la course (`--taille-max-consigne-externe` donné ou non : sous la v43, la garde par défaut refuse la course, 1 013 975 <
1 077 663 ; sous la v44, à remesurer) ; la règle de reprise des contrôles Claude après un relais relancé (CL43-03) ; le
nombre de tentatives (CL43-05 : le code garde trois) ; la mesure finale (étape 8) ; la relecture CL11. **Sans la v44, rien ne
part** (bloquant des guillemets et CL43-01).

**Ce que Lazar doit faire lui-même** (tout le reste est fait par la session) :
1. **Maintenant, avant le lancement (5 minutes)** : sur la console de facturation de la clé n° 2 de Gemini, (a) vérifier qu'il
   reste du crédit (R-379 de `main` : la clé n° 1 avait rendu HTTP 402) ; (b) **lire le prix de sortie** de gemini-4-argon
   (le prix d'entrée ≤ 8,3 est lu, R-718 ; la sortie 41,5 est SUPPOSÉE) et le dire à la session en une ligne. Sans réponse, la
   commande garde 8,3 / 41,5 (prudent : coûts déclarés au-dessus du réel probable).
2. **Lecture humaine pour le bras d'Argon** : par sa décision du 28 octobre (R-656, R-663), le lecteur est **un sous-agent neuf
   de session-depot qui n'a vu aucun moniteur** ; Lazar n'a rien à lire. **Quand la course a rendu le code 0** (« en attente du
   bras »), la session lui écrit une ligne : « course finie, N fiches validées, M en quarantaine, lecteur neuf lancé ; bras dans
   ≈ 1 h sauf veto ». **S'il veut lire lui-même** (droit du devis v4, point 1), il le dit à ce moment ; il lit alors, dans la
   SORTIE : `fiches-en-quarantaine.json`, `fiches-validees.json` (≈ 48 fiches, ≈ 220 000 caractères, ≈ 1 h 30), les réponses
   brutes des proposeurs et la partie « fiches et témoins » de `juges-bras-rapporte/argon-juge/…/consigne-en-attente.md` (les
   pièces des juges sont celles de la liste blanche, vérifiées par empreinte), puis répond « lu, aucune objection » ou
   « objection : … » ; la session écrit l'attestation avec `"lecteur": "Lazar"`.
3. Aucun autre mot n'est requis pour la voie (β) **si la v44 la rend lançable telle qu'écrite** (Argon 12,8 : contrôle 3,1 +
   passe 1 2,5 + passe 2 3,1 + juge 3,5 + contrôle du bras 0,2 + marge 0,4 ; Claude 40 ; 52,8 ≤ GO). **Un mot est requis** si :
   la v44 ne porte pas d'option de passe 2 (choix β-1, β-2 ou β-3 de CL10 : β-3 = 53,0 > 52,8) ; une relance après une
   tentative payée (CL40-01 (c) : seuls les contrôles échoués sont repayés ; au-delà de trois tentatives : mot de Lazar) ;
   dépense au-delà de 52,8 (l'enveloppe de 60 couvre « une relance ou un imprévu » : le dire avant de l'entamer) ; alerte à
   80 % du devis (42,2 USD) : une ligne, sans attendre.

## Étapes, dans l'ordre

Chaque étape : **qui** · **durée** · **ce qui la bloque**. « Session » = session-depot ; « sous-agent » = sous-agent neuf de la
session (fichiers à lire donnés explicitement, R2).

### 0. Reprise et vérifications (session · 10 min · rien)
`date -u` ; routine R14 (empreintes, `verifier-arbre`, `registres/etat.md`, dernière passation) ; `vastai show instances`
(aucune instance attendue) ; `git status` propre. Lire GO-2026-10-28-14 (ligne (β), 52,8, enveloppe 60, « lancement après la
relecture CL10 de la v43 et la mesure des consignes réelles ») : la v44 et sa mesure prennent la place de la v43.

### 1. Transmettre le bloquant des guillemets à conv-audit (session · 10 min · rien)
Message au canal : constat, démonstration (`mesure-consignes-v43.txt`, bloc A ; `travail/sim-guillemets/`), correction et essai
proposés ; demander qu'il entre dans la v44 (ou une v44 bis) et dans le devis v7 nonies, avec la liste blanche retenue (v4 ou
v5, ci-dessous) et le nom de l'option de passe 2.

### 2. Réception de la v44 (session · 15 min · **la v44**)
Extraire l'arbre de la branche (`git archive refs/canal-local/conv-audit <chemin>/orchestrateur-pole-v7 | tar -x -C $DOS/v44`),
`sha256sum -c EMPREINTES-orchestrateur-pole-v7-v44.txt` (tout conforme), lire le LISEZMOI v44 et le devis v7 nonies ;
noter l'option de passe 2, la garde par passe, la règle de reprise.

### 3. Relecture ciblée v43 → v44, CL11 (sous-agent Opus neuf · 45 à 75 min · v44)
Fichiers à lui donner : différentiel v43 → v44, CL10, devis v7 nonies, cette marche, `mesure-consignes-v43.txt`,
`commande_argon_v1.py` et ses essais. Points : guillemets corrigés et essayés ; somme externe de (β) acceptée par le lanceur
(12,8, refus démontré à 12,9) ; passe 2 gardée avec provision sous son propre plafond ; reprise Claude refusée après un relais
relancé (essai : relais neuf → contrôles Claude rejoués) ; les 405 + n essais passent. **Bloque le lancement** si « non lançable ».
Pendant ce temps, étapes 4 à 7.

### 4. Pièces et liste blanche (session · 20 min · rien)
- Dossier hors du dépôt : `DOS=/root/ideation-v1` (mode 700). Pièces : `git archive refs/canal-local/conv-audit` des chemins
  de la liste (question, `extraits-v1/`, quatre documents entiers, `corpus-primaire-v1/` à `-v3/` — et `-v4/` si v5 —,
  `preideation-interne-v1/fiches-anonymes.md`) vers `$DOS/pieces/`. Témoins : copier
  `…/scratchpad/temoins-ideation-tiers-v1.json` dans `$DOS/temoins/` et vérifier `4c6c375c…` (scellé, non versé au dépôt avant
  la course, R-657).
- **Liste retenue : v4** (devis v7 octies, point 6 ; 39 fichiers, `7fbe5dec…` chez conv-audit) **+ témoins = 40**. La v5 (avec
  PACE, `18927104…`, 40 + témoins = 41) **tient aussi** (contrôle 1 102 303 < 1 493 975) et sert mieux Q2 (PACE est l'occupant
  relevé, R8) : à trancher en une ligne au devis v7 nonies ; défaut : v4.
- Reconstruire chez soi : `python3 -I -B demonstrations/ideation_v1.py $DOS/liste-blanche-ideation-v4-session-depot-v1.json
  --construire-liste-blanche <les 40 chemins>` ; vérifier que les 39 empreintes non-témoins coïncident avec
  `liste-blanche-sans-temoins-v4.json` (fait ici sur les 40 de la v5 : toutes conformes) ; sceller
  (`sha256sum … > ….sha256`, nom nu) ; consigner l'empreinte au registre. Lecture humaine de la liste : la session la relit
  (40 lignes, aucun chemin de `donnees/`, de banque, de préenregistrement, de quarantaine).

### 5. Attestation du matériau (sous-agent neuf, n'a vu aucun moniteur · 15 à 20 min · étape 4)
Il lit `preideation-interne-v1/fiches-anonymes.md` (36 938 caractères, `d896a915…`), en entier, avant tout envoi à Argon (R-663),
et rend « rien à retirer » ou la liste de ce qui ne doit pas sortir. La session écrit alors, scellé (nom nu) :
`$DOS/attestation-materiau-v1.json` = `{"lecteur": "sous-agent neuf de session-depot (modèle, date), aucun moniteur vu",
"lu_le": "<date -u>", "materiau_sha256": {"fiches-anonymes.md": "d896a91509f07a1f14b58b06be1e4a2d1ab52aab4dcb38d5447e77c9c39865d6"}}`.
Une objection du lecteur arrête tout : mot de Lazar.

### 6. Machine (session · 25 à 35 min · rien ; R-379 (i), R-589, CL34-05)
1. **Bac à sable** : `bwrap` présent ; contrôle `/proc` neuf : `demonstrations/verification_cle_proc_v7.py` rejoué et versé (cas
   sain et artefact, R5). Le lanceur refuse sous root sans `/proc` neuf.
2. **Utilisateur distinct d'Argon** : `useradd --system --create-home --home-dir /home/argon --shell /usr/sbin/nologin argon` ;
   `chmod 700 /home/argon`. Clé : `umask 077; printf '%s\n' "$GEMINI_API_KEY_2" > /home/argon/.cle-gemini; chown argon:argon
   /home/argon/.cle-gemini; chmod 600 /home/argon/.cle-gemini` (jamais affichée ; jamais sous `$DOS`, jamais dans la SORTIE).
   Certificats lisibles par argon : `install -m 644 /root/.ccr/ca-bundle.crt /opt/argon/ca-bundle.crt` (`/root` est en 700).
3. **Commande** : `install -m 755 -o root -g root commande_argon_v1.py /opt/argon/commande_argon_v1.py` (empreinte consignée,
   R6) et l'**enveloppe** `/opt/argon/appel-argon-v1.sh` (root, 755), exécutée **sous** argon :
   ```sh
   #!/bin/sh
   # Enveloppe d'utilisateur distinct pour Argon (session-depot, v1). Pose la clé, le mandataire, borne le temps.
   set -eu
   umask 077
   [ "$(id -un)" = argon ] || { echo '{"texte": "", "cout_usd": 1e-06, "erreur": "enveloppe hors utilisateur argon"}'; exit 2; }
   GEMINI_API_KEY=$(cat /home/argon/.cle-gemini); export GEMINI_API_KEY
   HTTPS_PROXY=http://127.0.0.1:40191; SSL_CERT_FILE=/opt/argon/ca-bundle.crt; export HTTPS_PROXY SSL_CERT_FILE
   exec /usr/bin/timeout -k 20 1700 /usr/bin/python3 -I -B /opt/argon/commande_argon_v1.py --compter-jetons --delai-s 1500 \
        --prix-entree 8.3 --prix-sortie 41.5 "$@"
   ```
   (`"$@"` sert seulement à l'essai du point 4, qui ajoute `--url-base http://127.0.0.1:PORT/v1beta` ; la ligne du noyau
   n'ajoute rien.)
   Délais emboîtés : commande 1 500 s < enveloppe 1 700 s (SIGTERM, puis SIGKILL 20 s après) < noyau `--delai-commande-s 1800`.
   L'orchestrateur tourne sous root : la ligne de commande externe est
   `/usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v1.sh` (même processus, même groupe :
   le `killpg` du noyau l'atteint ; l'environnement minimal du noyau — `PLAFOND_SESSION_USD`, `ROLE_POLE` — passe tel quel).
   Si l'orchestrateur ne tourne pas sous root : `sudo -n -u argon` avec `env_keep += "PLAFOND_SESSION_USD ROLE_POLE"` pour
   cette seule commande ; le noyau ne peut plus tuer le groupe d'un autre utilisateur : seul `timeout` sous argon borne le temps.
   Aucun argument n'est un fichier qui change (CL43-06 : `setpriv` et l'enveloppe seulement, empreintes fixes).
4. **Essai de la commande sans dépense** : `python3 -m pytest -q test_commande_argon_v1.py` (29 essais, faux serveur local) ;
   puis, sous argon, l'enveloppe pointée sur le faux serveur (même essai que `test_adaptateur_v43_lit_la_sortie`) : prouve que
   la clé est lue, que la ligne JSON sort, que `setpriv` passe le plafond et le rôle.
5. **Relais** (clé n° 3, `RR_ANTHROPIC_API_KEY_3`) : `umask 077; printf '%s' "$RR_ANTHROPIC_API_KEY_3" > $DOS/cle-relais` (lecture
   unique, supprimé par le relais), puis, PID consigné :
   `cd $O && setsid nohup env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 python3 -I pole/relais_reel.py --port 8787
   --fichier-cle $DOS/cle-relais --plafond-usd 40 --reserve-par-appel 4 --journal $DOS/relais-journal-v1.jsonl
   > $DOS/relais-v1.log 2>&1 & echo $! > $DOS/relais.pid`. Vérifier `curl -s http://127.0.0.1:8787/relais/etat` (dépense 0,
   plafond 40). **Réserve** : la variable `RR_ANTHROPIC_WORKSPACE_ID` existe dans la session ; si la clé n° 3 exige l'en-tête
   `anthropic-workspace-id` (cas de `RR_ANTHROPIC_API_KEY`, R-481), le relais v43 ne l'envoie pas : l'appel de contrôle Claude
   échouera en HTTP 400, **sans dépense** (Argon aura payé son contrôle, ≈ 2,24 USD déclarés). La clé n° 3 a servi au collisionneur
   (R-633) : vérifier dans son journal si l'en-tête était posé ; sinon, demander à conv-audit d'ajouter l'en-tête au relais.

### 7. Inscriptions (session · 10 min · étapes 4 à 6)
`registres/decisions.md` : commande d'Argon (empreintes de `commande_argon_v1.py` et de l'enveloppe), liste blanche scellée,
attestation du matériau, relais (PID, plafond, réserve), choix v4/v5, barème retenu. GO cité au lancement :
`GO_ID=GO-2026-10-28-14` (la garde de calcul l'exige).

### 8. Mesure finale sans dépense (session · 10 min · v44, étape 4)
`--mesurer-consignes` de la **v44** avec les vrais fichiers, la liste scellée, les témoins et les réglages de l'étape 9 ;
rediriger, sceller (R6). Critères : contrôle d'Argon ≤ 1 493 975 (v43 : **1 077 663**, tient) ; « passerait » vrai sous la garde
retenue ; aucune erreur (la v43 s'arrête sur les témoins : bloquant des guillemets) ; consigne du juge réelle sous la garde du
bras (≈ 648 000 + 48 × taille moyenne de fiche ; tient jusqu'à ≈ 8 400 caractères par fiche avec un juge à 3,3, ≈ 10 400 à 3,5).

### 9. Course (session lance ; durée 45 min à 3 h, attendu ≈ 1 h 15 · étapes 2 à 8 et CL11 « lançable »)
Ligne exacte (arbre v44 ; `P=$DOS/pieces/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1`) :
```sh
cd $O && GO_ID=GO-2026-10-28-14 setsid nohup env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 \
 python3 -I -B demonstrations/ideation_v1.py $DOS/sortie-course-v1 \
 --liste-blanche $DOS/liste-blanche-ideation-v4-session-depot-v1.json \
 --question $P/question-collisionneur-priorites-sept-questions-v3.md \
 --piece $P/extraits-v1/brief-notre-marque-v1.md --piece $P/extraits-v1/questions-section-A-v1.md \
 --piece $P/extraits-v1/classement-v2-sections-1-a-4-v1.md \
 --piece $P/extraits-v1/anteriorite-Q1-sections-1-a-3-v1.md … (Q2 à Q7, Qpont) \
 --piece $P/anteriorite-coevolution-et-boite-blanche-v1.md --piece $P/anteriorite-universalite-metriques-v1.md \
 --piece $P/conception-pole-scientifique-v1.md --piece $P/integration-proposeurs-ia-v1.md \
 --piece $P/corpus-primaire-v1/extrait-….md … (les 22 extraits de corpus-primaire-v1 à -v3 ; + v4 si liste v5) \
 --piece-juge $P/extraits-v1/anteriorite-Q1-sections-1-a-3-v1.md … (les huit) \
 --piece-juge $P/anteriorite-coevolution-et-boite-blanche-v1.md --piece-juge … (les mêmes 22 extraits de corpus) \
 --materiau $P/preideation-interne-v1/fiches-anonymes.md --seconde-passe \
 --attestation-materiau $DOS/attestation-materiau-v1.json --temoins $DOS/temoins/temoins-ideation-tiers-v1.json \
 --proposeur opus=claude-opus-5-5 --proposeur fable=claude-fable-5-1 \
 --juge juge-fable=claude-fable-5-1 --juge juge-opus=claude-opus-5-5 \
 --proposeur-externe argon=gemini-argon --juge-externe argon-juge=gemini-argon \
 --commande-externe "/usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v1.sh" \
 --budget 'proposeur_ideation|claude-opus-5-5=5' --budget 'proposeur_ideation|claude-fable-5-1=9.3' \
 --budget 'juge_ideation|claude-opus-5-5=4' --budget 'juge_ideation|claude-fable-5-1=7' \
 --budget 'proposeur_ideation|gemini-argon=2.5' <OPTION v44 : plafond de la passe 2 d'Argon = 3.1> \
 --budget 'juge_ideation|gemini-argon=3.5' \
 --budget-total-usd 40 --budget-externe-usd 12.8 --budget-controle-externe-usd 3.1 \
 --prix-entree-usd-par-million-jetons 8.3 <garde de la course : selon la v44 et la mesure de l'étape 8> \
 --taille-max-pieces 750000 --nombre 8 --graine 20261028 --delai-session-s 3600 --delai-commande-s 1800 \
 --racine-depot /home/user/controle-ia-travail \
 --moteur claude-sdk --url-relais http://127.0.0.1:8787 --confirmer-moteur-reel --horodatage "$(date -u)" \
 > $DOS/course-v1.log 2>&1 & echo $! > $DOS/course.pid
```
Les listes `…` se complètent mot pour mot depuis `travail/mesurer_v1.sh` (même ordre, chemins de `$P`). **Sous la v43 seule**
(si Lazar l'exigeait malgré le bloquant des guillemets — à déconseiller) : `--budget 'proposeur_ideation|gemini-argon=3.1'
--budget 'juge_ideation|gemini-argon=3.3' --taille-max-consigne-externe 1490000` (β-1 de CL10, marge 0) et la même option
`juge…=3.3` au bras. Ordre joué par le code : contrôle d'Argon (consigne réelle ≈ 1,08 million de caractères, ≈ 2,24 USD
déclarés), contrôles Claude (0,2 chacun), passes 1 et 2 d'Argon, passes Claude, juges Claude, consigne d'Argon en attente.
**Attendu** : Claude ≈ 22 à 40 (devis v7 ter) ; Argon déclaré ≈ 6 à 7 au barème 8,3 / 41,5 (contrôle 2,24 ; passe 1 ≈ 1,42 +
sortie ; passe 2 ≈ 1,58 + sortie), réel probablement ≈ 4 fois moins si le barème réel est 2 / 10. Codes : **0** en attente du
bras ; **4** témoins échoués chez un juge Claude (illisible) ; **2** arrêt (tentative scellée dans `SORTIE-controle/` si avant
le manifeste de départ).

### 10. Réveils de garde pendant la course (session · toutes les 20 à 30 min · rien)
Réveils programmés dans la session (rappel à soi, R-735 : point à Lazar à chaque demi-heure). À chaque réveil : PID vivant
(`kill -0 $(cat $DOS/course.pid)`), fin du journal, `curl -s 127.0.0.1:8787/relais/etat` (dépense contre 40), dossiers de la SORTIE
(sessions finies), coûts déclarés d'Argon au journal du cœur ; alerte à Lazar à **42,2 USD** cumulés (80 %). Un réveil de
dernier recours à 4 h 30 après le départ (bornes : six sessions Claude × 3 600 s, trois appels d'Argon × 1 800 s).

### 11. Arrêt (session · 5 min · sur besoin ou en fin de course)
Arrêt anticipé : `kill -TERM <PID de course.pid>` seulement (R10, jamais par motif) — le lanceur arrête Argon et son groupe,
compte la session au plafond, écrit le manifeste de fin ; puis le relais : `kill -TERM <PID de relais.pid>`. Fin normale :
relais arrêté par PID après le code 0 (le bras n'en a pas besoin) ; consigner dans `registres/arrets.md`. Relance : seulement
si `relancable` est vrai, relais **relancé à neuf** (dépense 0) ; contrôles réussis repris (R-715) ; au-delà, mot de Lazar.

### 12. Lecture humaine et attestation (sous-agent neuf, aucun moniteur vu ; ou Lazar · 45 min à 1 h 30 · course code 0)
Ligne à Lazar (ci-dessus). Le lecteur lit les réponses brutes, `fiches-en-quarantaine.json`, **toutes** les fiches validées, et
la consigne d'Argon en attente (ce qui sort du périmètre : question, pièces des juges — vérifiées par empreinte —, fiches,
témoins). La session écrit, scellé (nom nu), `$DOS/attestation-lecture-v1.json` =
`{"lecteur": "…", "lu_le": "<date -u>", "fiches_validees_sha256": "<sha256 de SORTIE/fiches-validees.json>",
"consignes_en_attente_sha256": {"argon-juge": "<sha256 de la consigne-en-attente.md d'argon-juge>"}}`. Objection → pas de bras,
mot de Lazar.

### 13. Bras d'Argon (session · 10 à 40 min · étape 12)
```sh
cd $O && GO_ID=GO-2026-10-28-14 env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 \
 python3 -I -B demonstrations/ideation_v1.py $DOS/sortie-course-v1 --bras-rapporte-differe \
 --attestation-lecture-humaine $DOS/attestation-lecture-v1.json --juge-externe argon-juge=gemini-argon \
 --commande-externe "/usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v1.sh" \
 --budget 'juge_ideation|gemini-argon=3.5' --budget-externe-usd 12.8 --prix-entree-usd-par-million-jetons 8.3 \
 --delai-commande-s 1800 --horodatage "$(date -u)"
```
Sans `--taille-max-consigne-externe-bras` (CL43-04 : le défaut garde la provision ; ≈ 1,15 million de caractères à 3,5).
Juge d'Argon réel : ≈ 870 000 caractères (≈ 1,8 USD d'entrée déclarés), sortie bornée par la commande au reste du plafond
(≈ 40 000 jetons). Codes : **0** classement à trois juges lisible ; **4** témoins échoués chez Argon ; **5** sans juge externe
(classement à deux juges écrit, « illisible au sens du devis ») ; **2** arrêt. Tentative non relançable → mot de Lazar.

### 14. Versement, dépense, passation (session · 20 à 30 min · étape 13)
SORTIE, `SORTIE-controle`, journal du relais, journaux de la commande (sans clé : vérifier par recherche du préfixe de clé),
attestations, liste, manifeste de run (R9 : configuration, versions, graine 20261028, commit) : `EMPREINTES-…-v1.txt` scellé,
zip versionné dans `livrables/` (R12), branche orpheline de données comme pour les tours du collisionneur, servi à conv-audit.
`registres/depenses.md` : Claude au journal du relais ; Argon aux coûts déclarés (`cout_origine` par appel) et, dès que Lazar le
lit, au relevé de la console ; cumul contre 52,8. Contre-lecture (sous-agent d'un autre modèle) **après** le classement ; aucune
lecture ne tranche l'ordre des questions (devis v4, point 5). Passation R14.

## Réserves de la préparation
- **Sortie d'Argon SUPPOSÉE** (41,5) ; si le prix réel est plus bas, les coûts déclarés surestiment (sens sûr) ; s'il est plus
  haut, le pire cas peut dépasser le plafond : lire la console (Lazar, point 1).
- **Entrée estimée à 4 caractères par jeton** ; l'enveloppe passe `--compter-jetons` (compte exact, gratuit) pour fermer ce trou.
- **Garde de la passe 2 sous la v43** : sans provision (CL43-02) ; la commande borne elle-même la sortie au reste du plafond
  (`maxOutputTokens`), donc une passe ne dépasse plus son plafond déclaré, mais une sortie tronquée (`MAX_TOKENS`) est une erreur
  nommée qui arrête la course : risque si Argon « pense » longtemps. Fiches d'Argon au-delà de ≈ 8 000 caractères : sortie
  au bord du plafond.
- **Témoins** : longueurs servies 1 303 à 4 517 caractères (vrai 4 517, jumeau 4 324 au-dessus de la fourchette 1 500–3 500 du
  devis v5 ; injecteurs 1 303 et 1 474 au-dessous) — dans la fourchette des fiches réelles relevées par CL8 (3 000 à 5 000),
  mais L0 doit le dire (R4).
- **Erreurs HTTP 4xx** comptées au plancher 1e-6 (requête refusée avant génération : non facturée, SUPPOSÉ) ; 5xx et coupures
  après envoi comptées au pire cas.
