# Orchestrateur du pôle, v7 — version 52 : mode « juges seulement » (R-805)

Lignée conv-audit (sous-agent ingénieur), 30 octobre 2026. Base : la v51 (`EMPREINTES-orchestrateur-pole-v7-v51.txt`, `8044fa5c…`,
branche `origin/canal/session-depot-reprise-n55`), sans l'étage de tests de mort (inutile ici, refusé dans ce mode). **v52 n'est pas
contre-lue** (R2 : à faire par un sous-agent neuf, avant tout lancement réel). **Aucun appel payant, aucune clé, aucun réseau** : tout
est essayé avec les moteurs simulés, de faux adaptateurs, un faux kit et un amont factice local.

Décision du directeur R-805 (≈ 08:00 UTC) : les 29 fiches validées de la course 1, tentative 2 (arrêtée à 07:44 UTC sur un refus du
juge Fable 5.1), sont notées par **Opus 5.5 et Argon, sans Fable** ; si Opus 5.5 refuse, le même juge est relancé sur
`claude-opus-4-6` — **bascule déclarée**, par une option explicite, jamais automatique, modèle servi consigné ; toute autre bascule
reste un arrêt (R-764).

## R12

Aucun fichier de la v51 n'est modifié : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v51.txt` passe **en entier** sur l'arbre v52.
Fichiers nouveaux :

| fichier nouveau (v52) | rôle | version précédente gardée |
|---|---|---|
| `pole/juges_seulement_v1.py` | cœur du mode (préparation sans appel, exécution, bascule déclarée) | — (module nouveau) |
| `pole/adaptateurs_v2.py` | `AdaptateurClaudeSDKBascule` : l'adaptateur du kit qui accepte aussi un modèle de repli **déclaré et autorisé** (`BASCULES_AUTORISEES` : seulement `claude-opus-5-5` → `claude-opus-4-6`, R-805) | `pole/adaptateurs.py` |
| `pole/relais_reel_v2.py` | relais Claude, version 0.7.0 | `pole/relais_reel.py` |
| `demonstrations/ideation_v3.py` | lanceur : sans `--juges-seulement`, rend la main à la v2 (mêmes sorties) | `demonstrations/ideation_v2.py`, `ideation_v1.py` |
| `essais/test_v52_juges_seulement.py` | 30 essais | — |

Les empreintes sont dans `EMPREINTES-orchestrateur-pole-v7-v52.txt` ; le code dans `CODE-orchestrateur-pole-v7-v52.zip` (125 fichiers :
les 120 de la v51 et les cinq ci-dessus).

## Le mode

```
python -I -B demonstrations/ideation_v3.py SORTIE_NEUVE --juges-seulement COURSE_ARRETEE \
    --empreinte-manifeste-fin SHA256 --empreinte-fiches-validees SHA256 \
    --liste-blanche … --question … --temoins … --piece-juge … (mêmes fichiers, même ordre que la course) \
    --juge juge-opus=claude-opus-5-5 --juge-externe argon-juge=gemini-4-argon \
    --bascule-declaree claude-opus-5-5=claude-opus-4-6 \
    --budget 'juge_ideation|claude-opus-5-5=4' --budget 'juge_ideation|claude-opus-4-6=4' --budget 'juge_ideation|gemini-4-argon=3.5' \
    --budget-total-usd 10 --budget-externe-usd 4 [--budget-controle-usd 0.2] \
    [--verifier-seulement | --moteur simule | --moteur claude-sdk --url-relais … --confirmer-moteur-reel --commande-externe "…" \
     --attestation-lecture-humaine ATTEST.json]
```

**Avant tout appel et toute écriture** (`preparer_juges_seulement`) :
1. course intacte : sceaux de `manifeste-depart.json`, `manifeste-fin.json`, `fiches-validees.json` ; empreintes du manifeste de fin
   et des fiches **égales à celles données** (fixées dans le lanceur) ; course arrêtée en erreur, sans classement ; pas de dossier
   fermé, de moisson ni d'étage (consigne des juges différente : refusé) ;
2. fiches traitées comme des données : chacune est revalidée au gabarit depuis sa vue servie, à l'ordre canonique des champs (le
   fichier scellé les trie), et son empreinte recalculée doit être celle de la course ; **seules les fiches validées** sont servies ;
3. mêmes témoins, pièces des juges (noms, empreintes, ordre), question, liste blanche, graine : empreintes du manifeste de départ ;
   juges : mêmes étiquettes et modèles que la course (l'anonymisation dépend de l'étiquette) ; liste **explicite** (`--juge`,
   `--juge-externe`), aucun juge par défaut ;
4. **mêmes consignes** : toute consigne de juge écrite par la course (y compris mise à l'écart) doit avoir l'empreinte exacte de sa
   reconstruction ; au moins une, sinon refus ;
5. budgets par rôle, total Claude (contrôles, juges, session de repli déclarée) et total externe : somme des plafonds ≤ total ;
6. bascules : seulement les paires de `BASCULES_AUTORISEES`, sur le modèle d'un juge Claude ; jamais pour un juge externe ;
7. moteur réel : relais Claude lisible, modèles permis **exactement** les modèles Claude du mode, relais **v2** dès qu'une bascule est
   déclarée, plafond − réserve − dépense ≥ somme Claude ; attestation de lecture humaine scellée pour le juge externe (fiches
   validées et consigne du juge externe, même contrat que le bras différé) ; garde de taille de la consigne d'Argon.

**Puis** : dossier de sortie **neuf** (provisoire puis renommé ; jamais écrasé ; jamais dans la course) ; `manifeste-depart-juges.json`
avant tout appel ; appels de contrôle courts (Argon d'abord, puis chaque modèle Claude, repli déclaré compris) ; juges Claude, puis
juges externes. Sur un refus : si c'est un refus **dit par le modèle déclaré** (`stop_reason = refusal`, modèle servi = demandé) et
qu'une bascule est déclarée pour ce modèle, la session est mise à l'écart (`A-L-ECART-modele-non-autorise/`, coût compté) et une
session **neuve** du même juge (même étiquette, même consigne — empreinte vérifiée —, même clé d'anonymisation) est ouverte sur le
modèle de repli (`juges-bascule/`) ; refus initial, bascule, autorisation (R-805) et modèle servi sont consignés (manifeste de fin,
`noyau/modeles.json`, bilan). **Arrêt** sinon : refus sans bascule déclarée, refus du modèle de repli, refus d'Argon, événement de
repli du kit, modèle servi différent — même quand c'est le modèle de repli servi en silence dans la session d'Opus 5.5. Enfin notes,
témoins lus chez chaque juge (critère gelé), classement (moyenne à deux juges), `manifeste-fin-juges.json` (écrit sur tout chemin,
notes partielles scellées à part), `empreintes-sortie.txt` : tout scellé.

Codes : 0 lisible ; 4 témoin mal classé chez un juge (classement écrit, illisible) ; 2 refus ou arrêt.
`--verifier-seulement` : aucun appel, aucune écriture ; imprime reconstruction, empreintes et tailles des consignes, sommes et les
empreintes à porter dans l'attestation ; jamais le contenu d'une fiche.

## Relais Claude, version 2

`--modeles-permis claude-opus-5-5,claude-opus-4-6` était déjà accepté par la v1 (noms exacts ; tout autre modèle : 403 sans dépense) —
vérifié en processus par l'essai `test_relais_v2_en_processus`. **Adapté** : le barème du modèle inconnu comptait la lecture de cache à
0,25 USD par million de jetons, plus bas que 10 % d'une entrée à 5 USD : une borne **basse** pour `claude-opus-4-6`, hors barème. La v2
prend 1,00 (chaque composante du barème inconnu est une borne haute) ; `claude-opus-4-6` n'est pas ajouté au barème (prix non lu sur la
page officielle, aucun réseau ici) : il est compté au barème inconnu (10 / 50 / 12,5 / 1,0), plus cher que son prix réel — le
plafond du relais s'use plus vite, jamais moins. `/relais/etat` porte `version_relais` (0.7.0) et `bareme_modeles_permis` ; le mode
les exige quand une bascule est déclarée.

## Sur la vraie course (sans appel)

`--verifier-seulement` sur `/root/ideation-v1/sortie-course-v2` (fiches jamais ouvertes par l'opérateur du code) : code 0 ; **29 fiches**
servies, 6 témoins ; **reconstruction identique** de la consigne du juge Fable mise à l'écart (`336b0327a8d835c4…`, 824 298
caractères) ; consignes : `juge-opus` `7b55c2c4ae374194…`, `argon-juge` `6fd2277d1e9d2e4a…` (824 298 caractères chacune) ; garde de
taille d'Argon 1 336 746 caractères (passe). Essai à blanc au moteur simulé sur les vraies fiches, sans commande externe : code 4
(attendu : des juges simulés ne reconnaissent pas les témoins réels), 29 fiches notées, sortie scellée (`sha256sum -c` passe) ;
sortie de l'essai retirée ensuite (elle contenait les consignes).

## Essais

`env -i PATH=/usr/bin:/bin HOME=/tmp LANG=C.UTF-8 python3 -B -m unittest discover -t . -s essais -p 'test_*.py'`, deux exécutions
complètes sur l'arbre v52 (copies de la livraison) : **547 essais, 547 OK, 0 échec, 0 erreur, 0 ignoré**, chaque fois (≈ 360 s) — les
517 de la v51 (essais réels sous le vrai `bwrap` compris, joués) et 30 nouveaux. Témoin : la v51 seule, même machine, 517 OK. Les 30
essais nouveaux (`essais/test_v52_juges_seulement.py`) : course d'essai
arrêtée comme la course 1 (vraie course v51, refus du juge Fable) ; cas sain (lanceur v3, moteur simulé, code 0, quarantaine jamais
servie, course intacte, sortie entièrement scellée) ; `--verifier-seulement` sans écriture ; lanceur v3 = v2 sans le mode ; fiches
altérées (sceau faux ; rescellées ; empreinte attendue mise à jour mais fiche qui ne repasse pas le gabarit à son empreinte ;
manifeste de fin) ; consigne de la course altérée (sceau faux, puis rescellée : reconstruction différente) ; juges et pièces hors de la
course ; témoin mal classé (code 4) ; refus d'Opus avec bascule déclarée (repli consigné, même consigne, session refusée mise à
l'écart et comptée, contrôles des deux modèles) ; sans bascule (arrêt) ; repli du kit vers un autre modèle (arrêt) ; modèle servi
autre, y compris Opus 4.6 servi en silence (arrêt) ; refus du repli (arrêt) ; paires non autorisées (refus avant tout) ; refus d'Argon
(arrêt, notes partielles scellées) ; sommes des plafonds ; plafond total atteint avant la session de repli ; options de course
refusées ; attestation exigée et vérifiée ; relais (modèles permis exacts, v2 exigé avec bascule, champs finis) ; modèle servi non lu
(arrêt) ; adaptateur simulé refusé sur moteur réel ; adaptateur de bascule (noms exacts, jamais par préfixe ; faux kit de bout en bout :
refus d'Opus puis session sur 4.6, `fallback_model=None` ; repli du kit dans la session : arrêt) ; relais v2 en processus (4.6 permis,
autre modèle 403 sans atteindre l'amont, barème borné).

## Lanceur réel préparé (non lancé)

`/root/ideation-v1/lancer-juges-course-v2.sh` : gardes sans dépense (GO_ID, clés, root, arbre v52 à son empreinte, course, relais Gemini,
commande d'Argon, ports, R12) ; `--verifier-seulement` ; essai à blanc simulé sur les vraies fiches (sans commande externe) ;
attestation exigée avant les relais ; relais Claude v2 (plafond 20, réserve 4, `--modeles-permis claude-opus-5-5,claude-opus-4-6`),
relais Gemini (8 appels) ; clés par variable sous `env -i` ; mode réel ; arrêt des relais par PID (piège sur toute sortie) ; scellement.
Arbre installé dans `/root/ideation-v1/orchestrateur-v52/arbre/`. Sortie : `/root/ideation-v1/sortie-juges-course-v2/`.

**Devis** (plafonds, pire cas) : Claude 2 × 0,2 (contrôles Opus 5.5 et 4.6) + 4,0 (juge Opus 5.5) + 4,0 (repli Opus 4.6, sur refus
seulement) = 8,4, total du mode 10 (marge pour une session refusée comptée un peu au-delà de son plafond : 7,51 pour 7 chez Fable) ;
Argon 0,2 + 3,5 = 3,7, total 4. **Pire cas ≈ 12,1 USD.** Attendu (SUPPOSÉ) ≈ 3,5 à 4,5 USD sans refus ; ≈ 8 à 9 avec refus et
bascule.

## Réserves

- **Non contre-lue (R2).** Un sous-agent neuf doit lire `pole/juges_seulement_v1.py`, `pole/adaptateurs_v2.py`, `pole/relais_reel_v2.py`,
  `demonstrations/ideation_v3.py` et le lanceur avant tout GO.
- **Attestation de lecture humaine** gardée pour Argon (contrat du bras différé) : le lanceur s'arrête sans elle, avant les relais.
  À signer par Lazar (ou son lecteur) sur les empreintes imprimées par `--verifier-seulement` ; si le directeur veut l'ôter, c'est une
  décision et une nouvelle version.
- **Appel de contrôle d'Opus 4.6 dès le départ** (quelques centimes), même sans refus : il éprouve la route (relais, modèle servi)
  avant toute dépense de juge ; ce n'est pas une bascule (consigne « OK », jamais les fiches).
- **Barème d'Opus 4.6** non lu sur la page officielle : compté au barème inconnu (borne haute) par le relais ; le coût compté par le
  noyau (le plus grand du coût déclaré et de l'écart au relais) peut donc dépasser le coût facturé pour la session de repli.
- Effet réel des variables « sans repli » du kit : SUPPOSÉ (comme en v47) ; les barrières du noyau et du relais le couvrent.
- Deux juges : l'agrégat est une **moyenne** (règle gelée : médiane au-delà de deux) — à dire à la lecture du classement.
- La quarantaine (3 fiches) n'est jamais servie ; une relecture de quarantaine est hors de ce mode.
- **Relais de la course 1, tentative 2, encore vivants** (constaté ≈ 08:30 UTC) : `relais_reel.py` (PID 24293, port 8787, clé
  `RR_ANTHROPIC_API_KEY_3`, plafond 40) et `relais_gemini_v1.py` (PID 24295, port 8788), lancés à 07:25:16. `lancer-course-v2.sh` a
  arrêté 24291 et 24292 : les processus `setsid`, qui avaient fourché ; les relais python ont survécu (R10 non tenu par ce lanceur).
  Non touchés ici (pas les processus de ce sous-agent) : à arrêter **par leur PID** par la session, et à consigner dans
  `registres/arrets.md`. Tant qu'ils vivent, le lanceur des juges s'arrête (« port 8787 déjà pris »), sans rien payer. Le nouveau
  lanceur lance ses relais sans `setsid`, vérifie le PID par `/proc/PID/cmdline` et vérifie l'arrêt.
- GO : R-805 autorise la dépense « sous GO-2026-10-30-02, avec une ligne de GO et un devis » ; R-807 borne ce GO à ≈ 09:15 UTC. Le
  lanceur exige `GO_ID` ; la ligne de GO reste à inscrire par la session.
