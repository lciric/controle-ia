# Additif 1 au rapport de rédaction v3 (`rapport-redaction-v3-v1.md`, `e8f2729d…`) — sonde d'hôte et variantes « Coût » et « clé »

Même rédacteur-développeur, 4 novembre 2026, de 08:29 à 09:00 UTC (`date -u`). J'ai travaillé sur la suite demandée par le
directeur, puis sur le mot de Lazar de 08:41 UTC qu'il m'a relayé : « on met de cote argon aujoridhui, GO machine ». Cela donne
GO-2026-11-04-09 (calcul, 35 USD, échéance 2026-11-18, `registres/go.md` de `main` au commit `3eacfed4`) pour la machine. La
variante (a) est retenue et la variante (b) est reportée avec Argon. Mêmes interdits : fichiers neufs, aucun commit, aucun
`.sha256`, aucune location, aucun appel, aucune clé lue. J'ai réécrit `couples-variantes-cout-cle-v1.json` par son script après le
mot de Lazar : ton instantané en porte une version antérieure.

**Verdict.**
- Le mode sonde est écrit et ses 19 essais jouets passent. Il ne part que sous **GO-2026-11-04-09** : garde de `main` telle quelle,
  montant exactement 35 USD, et GO-2026-11-04-06 refusé.
- Il ne dépend d'aucune tâche planifiée (R-1477). La machine se détruit seule, après son plafond de durée et le versement. Si elle
  est encore listée, la fille la détruit par son identifiant.
- Reste à lancer la vraie sonde : c'est une dépense d'au plus 0,50 USD sous GO-2026-11-04-09.
- Les couples de la variante (a) sont remplis avec GO-2026-11-04-09 ; ceux de la variante (b) sont gardés. Aucun n'est appliqué.

## 1. Fichiers neufs (sha256 à la remise : section 6)

- `src/controle_ia/sonde_hote_durable_a1_v3.py` : bibliothèque standard seule.
- `scripts/amorce_sonde_hote_durable_a1_v3_v1.sh`.
- `tests/test_sonde_hote_durable_a1_v3.py` : 19 essais.
- `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/couples-variantes-cout-cle-v1.json`.
- Bloc-notes : `…/scratchpad/v3b1/couples_variantes.py`, qui écrit le fichier JSON et le vérifie.

Le lanceur durable rendu (`hote_durable_a1_v3.py`, `5b853fde…`) n'est pas modifié. La sonde reprend sa classe `Machine` :
scellement, contrôle des secrets, versement, poussée vérifiée et destruction sont ceux de la course.

## 2. Le mode sonde

**Partie « louer »**, dans la session de la fille :
- GO-2026-11-04-09 est contrôlé par `verifier_go_sonde` : garde de `main` (`decider`), puis montant exactement 35 USD sur la ligne
  et sur chaque extension.
- L'offre doit être conforme : aucune carte, au plus 0,40 USD/h, mêmes minima que la course. Elle doit aussi être **la moins chère
  des offres conformes** de la réponse brute.
- Plafond de durée : 20 min par défaut, 30 au plus. **Plafond de dépense : 0,50 USD**, calculé comme prix × (durée + 15 min de
  marge), soit au pire 0,40 × 35/60 ≈ 0,23 USD.
- Le corps de création ne porte que `COMMIT_PRIVE`, `GO_ID`, `PRIX_H_USD`, `DUREE_MAX_S`, `DEPOT_URL` et `GH_TOKEN`. Toute clé de
  modèle y est refusée (`CLE_ARGON`, `GEMINI*`, `ANTHROPIC*`, `OPENAI*`, `MOONSHOT*`, `KIMI*`).
- Création par l'outil `vastai`, sous la forme de la course : `python:3.13-bookworm`, `--entrypoint bash --args -c`, sortie
  filtrée.

**Partie « hote »**, sur la machine :
- Refus de partir si une clé de modèle est dans l'environnement. Revérification du prix, du plafond de dépense, puis de
  GO-2026-11-04-09 sur `main`.
- Faits de l'hôte relevés au journal : Python, `/usr/bin/python3`, numpy, git, cœurs, disque, et présence en booléen de
  `CONTAINER_ID` et de `CONTAINER_API_KEY`. Les installations sont chronométrées.
- Lecture de la machine par la clé d'instance. C'est une mesure, pas une garde.
- **Course factice détachée** : aucune variable de clé, un battement toutes les 10 s, 3 600 s prévues.
- Relevé de la garde toutes les 30 s. **Au plafond de durée**, la course factice est arrêtée par son identifiant de processus :
  c'est la fin attendue (`plafond_de_duree_de_la_sonde`).
- Liste `EMPREINTES-sonde-hote-durable-a1-v3-v1.txt`, contrôle des secrets, puis versement sur la branche neuve
  **`donnees/sonde-hote-durable-a1-v3-v1`** avec poussée vérifiée.
- **Autodestruction par l'identifiant de la machine**, sans aucune tâche planifiée. Si la poussée n'est pas vérifiée ou si un
  secret est trouvé, la machine est arrêtée, pas détruite.
- Reprise du conteneur : rien n'est relancé ; versement sur `…-interrompue-v1`, puis destruction.

**Ce que la sonde éprouve et que les jouets ne peuvent pas** : offres sans carte, création, image, commande détachée, poussée depuis
la machine, clé d'instance en lecture (au journal versé), puis en destruction (vue par l'inventaire du pilote).

## 3. Essais (`timeout 900 nice -n 10`)

`tests/test_sonde_hote_durable_a1_v3.py` : **19 passés**. Ceux du lanceur durable, rejoués : **49 passés**. Chaque garde est
éprouvée sur un cas sain et sur un artefact.

| garde | cas sain | artefacts |
|---|---|---|
| GO de la machine | ligne factice ; registre réel de `main` (GO-2026-11-04-09, échéance 2026-11-18) | GO-2026-11-04-06 ; ligne absente ; 36 USD ; après la validité ; autre type |
| plafond de dépense et de durée | 0,40 USD/h à 20 et à 30 min | 0, 31 et −1 min ; plafond de 0,10 USD |
| offre la moins chère | la moins chère des offres conformes (une offre avec carte moins chère n'est pas comptée) | offre plus chère ; offre avec carte |
| corps sans clé de modèle | variables exactes, `DUREE_MAX_S` 1200, amorce de la sonde dans le script | jeton absent ; `CLE_ARGON` ajoutée, refusée par l'outil |
| location jouet | une machine créée, journal sans jeton | offre plus chère, 45 min, GO-2026-11-04-06, 400 USD sur -09, ligne -09 absente, jeton absent : code 2, rien créé |
| machine, cas sain | GO, faits, clé d'instance « vue », course factice détachée, plafond de durée (1,5 s), arrêt par identifiant, battements versés, course factice sans variable de clé, liste juste, aucun secret, détruite | — |
| fin avant le plafond | versée, détruite | — |
| refus sur la machine | — | `CLE_ARGON`, `GEMINI_API_KEY_2`, GO-2026-11-04-06, 0,5 USD/h, jeton absent, 60 min : rien lancé, état versé, détruite, aucune valeur interdite au journal |
| reprise du conteneur | — | aucune relance, branche « interrompue », détruite |
| fuite d'un secret | — | jeton dans un fichier : rien versé, machine arrêtée |
| amorce | — | jeton absent, `CLE_ARGON` présente, GO-2026-11-04-06 : code 2, jeton jamais affiché |

## 4. Variantes : `couples-variantes-cout-cle-v1.json`, non appliquées

**(a) GO à part pour la machine — RETENUE.**
- 4 couples de texte : section 0.7, ligne 22 ; section 8, « Création » ; section 12 ; section 13, point 3. Le texte nomme
  GO-2026-11-04-09 (35 USD : machine et sonde) et GO-2026-11-04-06 (400 USD, Argon seul) : aucun montant ne peut plus être dépassé.
  Aucun marqueur neuf.
- 7 couples de code : `MONTANT_GO_MACHINE_USD`, `verifier_go_machine`, son appel dans `louer`, `--go-machine`, et des essais
  (ligne factice de -09, cas sain et artefacts).

**(b) Clé d'Argon dédiée — REPORTÉE avec Argon.**
- 3 couples de texte : section 0.7, ligne 23 (22 si (b) seule) ; section 8, « Création » et point (4).
- 4 couples de code : lecture de la clé **par son nom**, celui que donne `--variable-cle-argon` (par exemple
  `GEMINI_API_KEY_A1V3`, à fixer) ; nom contrôlé ; valeur masquée au journal et jamais développée sur une ligne de commande.

**Vérification.** Chaque « ancien » est présent une seule fois au moment de son application : (a) seule, (b) seule, puis (a) et
(b). Chaque texte résultant ne porte que les deux marqueurs du brouillon et le bloc du plan est intact. Le code et les essais
résultants sont joués dans des copies du bloc-notes : (a) 50 passés, (b) 49 passés, (a) puis (b) 50 passés.
Les essais de la variante (a) emploient un GO factice, GO-2026-11-04-90, parce que l'essai de révocation existant se sert
déjà de l'identifiant -09 ; le texte et la commande, eux, nomment le vrai GO-2026-11-04-09.

## 5. Commande exacte de la sonde, pour la fille

Elle se lance après le commit de la sonde sur `main` du dépôt privé (`COMMIT_PRIVE`, hash complet donné par le directeur). Coût au
plus 0,50 USD sous **GO-2026-11-04-09**. Aucune tâche planifiée n'intervient : la fille lance, puis vérifie elle-même.
`OFFRE` est la moins chère des offres conformes de `offres.json`, sinon la sonde la refuse.

```
D=/home/user/hors-clone-sonde-a1-v3-v1; mkdir "$D"                 # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main
git show origin/main:registres/go.md > "$D/registre-go-main.md"
git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py"
for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py; do git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f"; done
timeout 300 vastai search offers 'num_gpus=0 rentable=true verified=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --raw > "$D/offres.json"
for V in "--verifier-seulement" ""; do
  env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" timeout 900 nice -n 10 \
    python3 -I -B "$D/sonde_hote_durable_a1_v3.py" louer --go GO-2026-11-04-09 \
      --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
      --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-min 20 --journal-local "$D/journal-location-sonde-v1.log" $V || break
done
```

`env -i` ne laisse aucune clé de modèle dans le processus ; `vastai` garde sa clé dans `HOME`. L'identifiant de la machine est dans
`$D/journal-location-sonde-v1.log.identifiant`.

Environ 35 min plus tard, la fille vérifie elle-même dans sa session :
- `git ls-remote origin refs/heads/donnees/sonde-hote-durable-a1-v3-v1` montre la branche ;
- le `journal-sonde-a1-v3-v1.log` versé porte « nature de la fin : plafond_de_duree_de_la_sonde », « versé » et « clé d'instance :
  lecture faite … vue » ;
- `python3 -I -B "$D/hote_durable_a1_v3.py" inventaire` ne montre plus la machine.

Si la machine est encore listée, l'autodestruction par la clé d'instance a été refusée. La fille la **détruit alors par son
identifiant** (`vastai destroy instance <ID>`, R10), le consigne dans `registres/arrets.md`, et la fin de la course est revue avant
tout lancement. La sonde n'est pas une sortie de course : on peut la lire.

## 6. Empreintes à la remise

Empreintes relevées le 4 novembre 2026 à 10:23 UTC. Le bloc-notes est
`/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/`.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3.py` | `f7c7f79ba974dd1e38743265caf88f09ce7d4d96ea4676f6d66e75cc9ebca69d` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v1.sh` | `3fb62bd19e1e8f53c55a6721beef08bbdf8bfca83389335286c9b3cc7d8b6d37` |
| `tests/test_sonde_hote_durable_a1_v3.py` | `a5d41158c2ae4ae901c0007282f0defa2eb18da7e47eaaf2fb79c9759e911866` |
| `…/a1-v3-troisieme-course/couples-variantes-cout-cle-v1.json` | `1a74f6c285d817864a49e32ce297b06639c0c47e9c367d365154c3931936e4ec` |
| bloc-notes `couples_variantes.py` | `573974b1270d4670574ee7a461ee91ae5d62e4edb709dbddacd5227bc24ee3f8` |
| bloc-notes `sorties/essais-sonde.txt` (19 passés) | `31bd86e912e2691a656dcd8077e3208963f8b38b32b9d9a118ba62418e5e0ad4` |
| bloc-notes `sorties/essais-variantes-final.txt` (50, 49, 50 passés) | `34fb3c56d7fdc671b6ee1f40dc0f9941f1e215fcc160a767b1dca6f5a427dd21` |
| bloc-notes `sorties/couples-variantes.txt` (vérification des couples) | `5aab27d052062dd8a883a90d129984176b72138bf270d36718106aa4c0d3412d` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés que tu as committés pendant le
travail sont intermédiaires ; les fichiers rendus sont ceux qui portent les empreintes ci-dessus.
