# Ordre de session-depot à la fille — seconde course d'A1-v3 (GO-2026-11-03-01), v1

Écrit le 3 novembre 2026 à 10:10 UTC (heure relevée par `date -u` à 10:08:51) par session-depot (`session_01XJ6MgmmBhNGj5VaXDwJTP4`),
pour la fille (`session_01XJ6Mgq5AWikCJZKnsMkbRZ`). Course payante, Argon seul, plafond 400 USD (3,9 h attendues, 36 h au pire, 72 h
de garde). **Elle ne part qu'après la fin du tour et de la course Kirchner Q2 et l'arrêt de leur relais Argon par son identifiant
(ordre voulu par Lazar), et sur mon « lance ».** Aucun autre usage d'Argon pendant la course. Aucune clé affichée ni écrite ; aucune
lecture de la sortie avant son scellement ; arrêts par identifiant de processus seulement (R10). Reprend l'ordre de la première course
(`docs/procedures/ordre-fille-a1-v3-v1.md`, `35d72a3c…`) ; seuls changent les points ci-dessous.

## 0. Cinq conditions de R-1059 (sources)
1. Texte scellé : dépôt public `ideation-organism`, `main`, commit **`4848ad97967f2116b3a76cf8497d2d36c9d123cf`**,
   `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v2.md`, sha256 **`2a29f59353ce776f92d17799de25f8b75741f1c60dcc5edfbc427bf0ae3a8bb1`**
   (= compagnon) ; contre-lecture courte n° 3 « scellable après couples ».
2. Ligne **GO-2026-11-03-01** (calcul, 400 USD, échéance 2026-11-17) sur `main` et sur `canal/conv-audit-n04`.
3. Commande exacte : n° 410 de conv-audit (`aecff64b43feff03…` = compagnon), § 1, point 5.
4. `--verifier-seulement` en code 0 chez toi.
5. Sortie scellée avant toute lecture.

## 1. Garde de session, d'abord à coût nul (texte, section 13, point 7 bis ; audit A9)
Avant tout relais : une attente **suivie par ton harnais** sur un processus factice (`sleep 900` détaché, PID lu au processus), avec
un relevé d'activité daté au journal **toutes les 2 minutes au plus** (nettement sous 5 min), réarmée avant son délai de 2 h. Une fois
ce témoin passé (relevés datés au journal), la même garde sert pour le lanceur, jusqu'à sa fin. `guetteur.pid` = PID réel du guetteur
(l'audit a vu 1403 au lieu de 1405).

## 2. Code, registre et dossier
- Clone public au commit `4848ad97` (`checkout --detach`), `git status --porcelain` vide au journal.
- Dossier neuf hors du clone : `/home/user/hors-clone-a1-v3-seconde-v1/` ; journal `journal-lancement-a1-v3-seconde-v1.log`.
- `registre-go.md` = `registres/go.md` de **`canal/conv-audit-n04` à `46062b4e` ou plus récent** (celui de `main` est refusé par le
  lecteur du lanceur : seize doublons) ; commit, empreinte et `grep -n GO-2026-11-03-01` des deux registres (la copie et `main`) au journal.
- Configuration `…/nuit/configuration-mini-course-kimi-argon-v3.json` (`e5306c47…`) et ses six pièces, commande Argon `221df610…`,
  registre de dépense `8ba92066…`, `collisionneur_v7.py` `c9725f02…` : empreintes au journal (déjà en place depuis la première course).

## 3. Relais Argon 8805 neuf
Comme la première course (§ 4 de l'ordre v1), journal `/home/user/hors-clone-a1-v3-seconde-v1/relais-argon-journal-a1-v3-seconde.jsonl`,
`--plafond-usd 410 --max-appels 9000` ; identifiants et heures au journal ; vérifie qu'aucun autre relais d'Argon ne vit (port 8805 libre
avant).

## 4. Vérification puis course (depuis `orchestrator/` du clone, environnement sans clé)
```
nice -n 10 python3 -I -B demonstrations/attaque_goodhart_v3.py /home/user/hors-clone-a1-v3-seconde-v1/sortie-attaque-goodhart-v3 \
    --preenregistrement prereg/preenregistrement-attaque-goodhart-v3-v2.md \
    --configuration /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/configuration-mini-course-kimi-argon-v3.json \
    --moteur reel --confirmer-moteur-reel \
    --registre-go /home/user/hors-clone-a1-v3-seconde-v1/registre-go.md --go GO-2026-11-03-01
```
D'abord avec `--verifier-seulement` (code 0 exigé, sortie au journal, message à session-depot) ; puis, **sur mon « lance »**, sans,
détachée (`nohup setsid … &`), PID réel et heure au journal, et la garde de session du § 1 sur ce PID.

## 5. Pendant, fin, scellement
Guetteur et alerte comme l'ordre v1 (§ 6), sans relève horaire comme seule garde. Fin : relais arrêté par son PID ; liste
`EMPREINTES-sortie-a1-v3-seconde-v1.txt` ; branche neuve `donnees/attaque-goodhart-v3-a1v3-seconde-v1` partie de `main` ; contrôle des
clés à 0 ; rapport scellé ; message à session-depot (commit, empreintes, code, durée, dépense, incidents).
