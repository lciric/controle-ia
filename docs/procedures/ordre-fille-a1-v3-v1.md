# Ordre de session-depot à la fille — lancement d'A1-v3 (GO-2026-11-02-21), v1

Écrit le 3 novembre 2026 à 06:13 UTC (heure relevée par `date -u`) par session-depot (`session_01XJ6MgmmBhNGj5VaXDwJTP4`), pour la
fille (`session_01XJ6Mgq5AWikCJZKnsMkbRZ`). Course payante, Argon seul, plafond 400 USD (devis : au plus ≈ 190 USD ; durée haute
≈ 25 h, pire ≈ 36 h). **Aucun autre usage d'Argon pendant la course.** Aucune clé affichée ni écrite ; aucune lecture de la sortie
avant son scellement ; arrêts par identifiant de processus seulement (R10).

## 0. Vérifie d'abord les cinq conditions du go permanent R-1059 (sources, pas ce message)
1. Texte scellé et contre-lu : dépôt public `lciric/ideation-organism`, commit **`ba4edfe103102ddbda921baa50b5356aea5887b5`**,
   `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v1.md`, sha256 **`898d5be414f1472dc5beb9c9e8d377698c6b1744e9b95bd188de5a157426a23e`**
   (= compagnon) ; contre-lecture n° 2 « scellable après couples » (public `d54b85c`).
2. Ligne `GO-2026-11-02-21` sur `main` du dépôt privé (`registres/go.md`) : calcul, 400 USD, échéance 2026-11-16, aucune révocation.
3. Commande exacte transmise par conv-audit : message n° 393, `canal/conv-audit-n04`, fichier
   `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-11-03_n393.md`, sha256 `49f5a8d1f0c0d7d010fdf2c1ddaffea064da677ec5f624278f0e8a428ae4e234`
   (= compagnon), § 1 ; c'est le bloc « Commande exacte » de la section 4 du texte scellé, avec N = 1.
4. `--verifier-seulement` rend 0 chez toi (point 5 ci-dessous).
5. Sortie scellée avant toute lecture (point 8).
Si l'une manque : rien ne part, dis-le à session-depot.

## 1. Code public
`git -C /home/user/ideation-organism fetch origin main` puis `git -C /home/user/ideation-organism checkout --detach ba4edfe103102ddbda921baa50b5356aea5887b5` ;
`git status --porcelain` doit être vide (copie sa sortie au journal de lancement). Journal de lancement :
`/home/user/hors-clone-a1-v3/journal-lancement-a1-v3-v1.log` (chaque ligne avec l'heure `date -u`).

## 2. Fichiers aux chemins que gèle la configuration
- Dans `/home/user/controle-ia-travail`, sans toucher à l'index ni à `main` : récupère par refspec explicite
  `donnees/recuperation-collisionneur-v8-v1` (déjà fait) et `canal/session-depot-reprise-n120`, puis extrais par `git archive` :
  `git archive origin/donnees/recuperation-collisionneur-v8-v1 donnees/mini-course-kimi-argon-v1/orchestrateur/nuit donnees/espece-seule-v1/collisionneur_v7.py | tar -x -C /home/user/controle-ia-travail`.
- Place la configuration gelée d'A1 à côté : `git show origin/canal/session-depot-reprise-n120:brouillons/canal-reprise-releve-v1/envois/session-depot/conf-a1-v3/configuration-mini-course-kimi-argon-v3.json > /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/configuration-mini-course-kimi-argon-v3.json`.
- Vérifie par `sha256sum` et écris au journal : configuration **`e5306c47e1b21a5e55b599411dba92c97e88aa98bb6d6fa91fc5d358a2bdde30`** ;
  ses six pièces (`pieces/…`) égales aux empreintes qu'elle déclare ; `commande_argon_v56_nuit_v2.py` **`221df610…622b851`** ;
  `registre_depense_cumulee_v1.py` `8ba92066…578ff` ; `donnees/espece-seule-v1/collisionneur_v7.py` **`c9725f02…98dc`**. Toute autre
  empreinte : pas de course.

## 3. Registre des GO et dossier de sortie, hors de tout dépôt
`mkdir -p /home/user/hors-clone-a1-v3` (vide hors du journal) ; `registre-go.md` = `registres/go.md` de `canal/conv-audit-n04` au
commit `aff188da` (sha256 `53985197d3e9780db9bf9738c050c3e746eea149af3e4024649f41db5cedef0a`, accepté par `verifier_go_v56` pour
GO-21 à 400 USD, vérifié par session-depot) : écris au journal commit, empreinte et la sortie de `grep -n GO-2026-11-02-21`.
La sortie de la course : `/home/user/hors-clone-a1-v3/sortie-attaque-goodhart-v3` (ne la crée pas : le lanceur la crée).

## 4. Relais Argon 8805, neuf, pour cette course seule (texte scellé, section 13, point 7)
- `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" HTTPS_PROXY="$HTTPS_PROXY" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt`
  (plus `https_proxy`, `NO_PROXY`, `no_proxy` **seulement s'ils sont posés** : une variable de mandataire vide en annule une autre),
  `/usr/bin/python3 -I -B /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py servir --port 8805 --plafond-usd 410 --max-appels 9000 --journal /home/user/hors-clone-a1-v3/relais-argon-journal-a1-v3.jsonl`,
  détaché (`nohup setsid … &`) ; PID au journal ; vérifie `/proc/<PID>/cmdline`.
- Avant `--verifier-seulement`, écris au journal : **(a)** plafond propre 410 USD (≥ 400) et 9 000 appels (≥ 8 000) ; **(b)** taille
  de corps admise 4 000 000 octets (la plus longue consigne, 90 363 octets, passe) ; **(c)** aucune reprise dans le relais (une
  tentative ; erreur ou quota de l'interface → code 3 au pire cas ; blocage du prompt → code 5) ; et le relevé `GET /relais/etat`
  (clé présente en booléen seulement, plafond, appels, dépense nulle). Aucun relais Kimi.

## 5. Vérification, puis course (depuis `/home/user/ideation-organism/orchestrator`)
Environnement de l'orchestrateur sans aucune variable de clé : `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/home/user/hors-clone-a1-v3 TMPDIR=/tmp`.
```
nice -n 10 python3 -I -B demonstrations/attaque_goodhart_v3.py /home/user/hors-clone-a1-v3/sortie-attaque-goodhart-v3 \
    --preenregistrement prereg/preenregistrement-attaque-goodhart-v3-v1.md \
    --configuration /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/configuration-mini-course-kimi-argon-v3.json \
    --moteur reel --confirmer-moteur-reel \
    --registre-go /home/user/hors-clone-a1-v3/registre-go.md --go GO-2026-11-02-21
```
D'abord **avec `--verifier-seulement`** : sortie complète gardée au journal ; **si le code n'est pas 0, rien ne part** et tu
envoies la sortie à session-depot. Puis la même commande **sans** `--verifier-seulement`, détachée (`nohup setsid … &`), PID et
heure de départ au journal.

## 6. Pendant la course
- **Guetteur** (script à toi, détaché) : toutes les 5 minutes, il vérifie que le relais (par son PID) vit ; s'il est mort, il le
  **relance** avec exactement les mêmes valeurs et l'écrit au journal avec l'heure ; il n'arrête jamais rien (règle des
  guetteurs, section 8 du texte). Il relève aussi `GET /relais/etat` (compteurs seulement) toutes les heures.
- **Alerte écrite d'avance** (section 13, point 7) : dès qu'une tentative finit « échouée (relais) », lis les statuts du journal du
  relais (statuts et compteurs seulement) et recopie-les au journal de lancement avec l'heure ; si la cause est durable (refus
  400, 403, 411, 413 du relais ; erreur de clé, de facturation, de modèle ; quota 429 qui dure plus d'une tentative), préviens
  session-depot par message ; tu n'arrêtes rien toi-même : Lazar décide.
- Reste active : pose une tâche planifiée liée à ta session, toutes les heures, qui relit le guetteur et l'état du processus.

## 7. Fin
À la fin du processus de la course (code de sortie au journal) : arrête le relais par son PID ; ne lis rien de la sortie.

## 8. Scellement et versement, avant toute lecture
Liste `EMPREINTES-sortie-a1-v3-v1.txt` (`sha256sum` de chaque fichier de la sortie, du registre de dépense, du registre des GO lu,
des journaux de lancement, du relais et du guetteur) ; branche **neuve** `donnees/attaque-goodhart-v3-a1v3-v1` partie de `main` :
commit de ces fichiers sous `donnees/attaque-goodhart-v3-a1v3-v1/` ; contrôle de clés avant la poussée (la commande de motifs du
dépôt rend 0) ; poussée. Puis rapport scellé `brouillons/fille/rapport-a1-v3-v1.md` sur une branche neuve `fille/rapport-a1-v3-v1` :
commit de données, empreintes, code de sortie, durée, dépense (registre de dépense et relevé du relais), incidents. Message à
session-depot : commit, empreinte du rapport, dépense. Pendant la course, un message court à session-depot : après
`--verifier-seulement` (code), au départ (PID, heure), puis à chaque alerte.
