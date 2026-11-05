# Contre-lecture du mode sonde de l'hôte durable d'A1-v3, v3

Je suis un contre-lecteur neuf. Je n'ai écrit aucune des pièces, ni les contre-lectures de la v1 et de la v2. J'ai travaillé le
4 novembre 2026, de 13:04 à 13:11 UTC (`date -u`), en lecture seule : aucun réseau, aucune location, aucune clé, aucune dépense,
aucun commit.

**Verdict : lançable après corrections.** Trois corrections courtes (M-1, m-1, m-2), dont deux démontrées hors des essais du rédacteur :
- un délai dépassé de `vastai create` imprime le jeton GitHub dans le terminal de la session et ne pose aucun marqueur de
  création incertaine (M-1, m-1) ;
- si l'amorce se bloque et que les `DELETE` sont refusés, le conteneur vit au-delà de sa fin de vie, sans borne (m-2).

Les points des contre-lectures v1 et v2 sont corrigés dans le code. La borne de la commande recommandée (tir de la minuterie,
1 200 s) vaut 0,33 USD, et au plus 0,37 USD en comptant l'attente finale ; elle reste donc sous 0,43 USD. Elle n'est pas
mécanique dans le cas « jamais démarrée, pilote coupé », ce qui est déclaré.

## Empreintes vérifiées (compagnons, depuis le dossier de chaque fichier ; `HEAD` = `05edcac1`)

| pièce | sha256 |
|---|---|
| `consigne-contre-lecture-sonde-v3.md` | OK (compagnon) |
| `src/controle_ia/sonde_hote_durable_a1_v3_v3.py` | `39ccc5ed…` OK |
| `scripts/amorce_sonde_hote_durable_a1_v3_v3.sh` | `59eb0067…` OK |
| `tests/test_sonde_hote_durable_a1_v3_v3.py` | `db48ccf9…` OK |
| `rapport-redaction-v3-v1-additif-3.md` | `7c8851c8…` OK |
| `essais-sonde-v3.txt` | `25f9285f…` OK (égale à la section 4 de l'additif) |
| `contre-lecture-sonde-v1.md` | `07ba1356…` OK |
| `contre-lecture-sonde-v2.md` | `a8fc1079…` OK |

## 1. Points des contre-lectures antérieures : état dans le code (lignes du module v3, sauf mention)

| point | état | où |
|---|---|---|
| M-A contrôles | **corrigé** | code 5 l. 381-384 ; contrôles T0 + 40 et T0 + 70 l. 334 ; destruction 10 min après l'échéance l. 379, 386 ; T0 + 70 est au-delà de la borne T0 + 65 (55 min plus 10 min) en mode normal, et de T0 + 50 en tir |
| M-B échéance absolue | **corrigé** (réserve f-2) | calcul l. 317-319 ; dans le corps l. 207 ; minimum l. 170, 173 ; course raccourcie l. 467-473 ; borne l. 93-97 ; « jamais démarrée » déclaré hors borne l. 96 |
| m-a arrêt | **corrigé** | aucun appel à `arreter` dans la v3 ni dans le chemin hérité ; `se_detruire` l. 592-628 ; aucun `PUT` dans la minuterie, `DELETE` répété l. 146-152 |
| m-b reprise tardive | **corrigé** | attente sur le numéro de la minuterie l. 193-195 (au plus 300 s) ; essai `unshare -pf` avec reprise (essais l. 628-649), joué ici |
| m-c `curl` | **corrigé** (réserve f-1) | installation l. 171 ; repli `python3` et alarme l. 122-136 ; refus de l'amorce (amorce l. 23) ; présence écrite au journal l. 179 |
| m-d tir réel | **corrigé** | `--tir-minuterie` l. 312-313, 651 ; aucun geste en tir l. 615-618 ; essais sous `unshare -pf` |
| f-a sorties | **corrigé**, avec un trou neuf (M-1) | `stderr=DEVNULL` l. 237 ; code seul l. 245-246 ; mais le message d'un délai dépassé contient les arguments |
| f-b ligne d'état | **corrigé** | l. 347-351 |
| f-c commande | **corrigé** | additif, section 6 |
| f-d clonage | **corrigé** | `sparse-checkout` l. 185 ; `fetch` et `checkout` sous `timeout 600` l. 186-187 |
| f-e crochets | **corrigé** | l. 165-170 |
| f-f, f-g | **réserves écrites** | additif, section 3, à relever sur la facture et dans `offres.json` |
| v1 M1 minuterie | **corrigé** | l. 118-153, lancée l. 177 avant le clonage |
| v1 M2 `-y` | **corrigé** | l. 270 |
| v1 M3 `VAST_API_KEY` | **corrigé** | exigée l. 225-226 ; passée au seul `vastai` l. 236 ; commande `env -i` |
| v1 m1, m2 dépense | **corrigé**, sauf le cas « jamais démarrée, pilote coupé » | M-B ; `controler` l. 354-394 ; réserve R-1 |
| v1 m3 réponse | **corrigé** | l. 273-290 ; marqueur l. 326-328 (mais voir M-1 et m-1) ; seconde location refusée l. 299-300 |
| v1 m4 commande | **corrigé** | additif, section 6 ; `offre` l. 663-676 |
| v1 m5 clonage | **corrigé** | l. 184-187 ; versements orphelins l. 505-532 |
| v1 m6 jeton | tranché par Lazar (R-1484) | — |
| v1 m7 R5 | **corrigé** pour la liste de la v1 | essais ; restent M-1, m-1 et m-2, hors de cette liste |
| v1 f1 à f8 | **corrigés** | f1 l. 237-247 ; f2 l. 82-83 et amorce l. 18 ; f3 l. 540, 562 ; f4 l. 64-67 ; f5 l. 86, 545-551 ; f6 `--storage 30` dans la commande ; f7 l. 301-302 ; f8 l. 141-143, 610, 373-374 |

## 2. Minuterie

- **Lancée en tout premier, sans Python, détachée.** Oui, sauf un cas : l'installation de `curl` par `apt-get` (l. 171), sans
  `timeout`, passe *avant* elle quand `curl` manque (f-1).
  - Ce cas n'est pas nécessaire, puisque la minuterie a son repli `python3`.
  - Il est improbable, car `python:3.13-bookworm` hérite de `buildpack-deps`, qui contient `curl` (non vérifié hors réseau).
- **Sortie du processus principal.** La minuterie meurt avec lui dans un conteneur, mais le principal l'attend désormais
  (l. 193-195).
  - Rejoué : les deux essais `unshare -pf` passent ici (chemin normal et reprise tardive).
  - Trou neuf (m-2) : le principal n'a aucune borne propre.
  - Si l'amorce, `git`, `apt-get` ou Python se bloquent (l. 182, 190, aucun `timeout`), le principal ne parvient jamais à
    l. 192.
  - Si en plus les `DELETE` sont refusés (403, précisément l'inconnue que le tir éprouve), le conteneur tourne sans fin.
  - Démontré sous `unshare -pf` : fin de vie à + 3 s ; encore en vie à + 40 s, tué par `timeout` (code 124) ; journal
    « DELETE … HTTP 403 », « ALARME ». Démonstration : `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl-sonde-v3/demo2/`.
- **Reprise du conteneur.** L'échéance d'origine est relue (l. 172). Après la fin de vie, il reste un seul essai de
  `DELETE`, que le principal attend.
- **`curl` absent.** Le script de démarrage tente de l'installer. L'amorce refuse de partir (code 2, visible). La minuterie passe par
  `python3 -I` (urllib) et écrit son ALARME. Un essai couvre ce cas.
- **Écart déclaré (destruction quand l'étiquette est illisible).** Il est sûr : aucun chemin ne peut viser une autre instance.
  - La minuterie et la machine ne visent que `CONTAINER_ID`, posé par Vast et absent du corps.
  - Cet identifiant est contrôlé en chiffres, et les instances protégées sont exclues.
  - Les valeurs du corps sont sans espace ni guillemet, ce qui empêche toute injection d'un `-e`.
  - Le pilote ne vise que `new_contract`, après contrôle de l'étiquette.
  - Une étiquette lue différente donne « aucun geste », sans nouvel essai (f-5).

## 3. Borne de dépense

- **Commande recommandée** (tir, 1 200 s, 0,40 USD/h au plus) :
  - échéance absolue = création + 2 400 s, soit **0,27 USD** si la minuterie détruit ;
  - sinon fin de vie à + 3 000 s, soit **0,33 USD** (borne écrite) ;
  - plus l'attente du principal, d'environ 60 s et au plus 300 s non comptées (f-2) : **au plus 0,37 USD ≤ 0,43**.
- **Mode normal à 1 800 s** : 0,50 USD écrits, et jusqu'à 0,53 avec l'attente, au-dessus du plafond de 0,50 que
  `verifier_plafond` accepte (f-2).
- **Démarrage tardif** : borné par l'échéance absolue (essai l. 569).
- **Pas mécanique dans trois cas :**
  - machine qui ne lance jamais son script, avec pilote coupé par la limite d'usage : aucune borne jusqu'à une session.
    C'est déclaré (l. 96, additif). Réserve R-1, à faire accepter par Lazar ;
  - m-2 : principal bloqué et `DELETE` refusés ;
  - f-f : instance « exited » après des `DELETE` refusés (stockage, voire calcul) jusqu'à une session.

## 4. Secrets

- **Ce qui atteint la machine.**
  - `GH_TOKEN` par `--env` : accepté pour la seule sonde (R-1484).
  - `CONTAINER_API_KEY`, posée par Vast : elle ne sert que dans l'en-tête de `curl` ou d'urllib, et dans `ClientVast`.
  - Aucune clé de modèle : la liste est littérale et gardée par le pilote, le corps, l'amorce et la machine.
  - `VAST_API_KEY` n'est passée qu'au sous-processus `vastai`.
- **Masquage.** Les journaux sont masqués (pilote : deux clés ; machine : trois). `fuites` passe avant le versement, journaux du
  démarrage compris. La minuterie jette le corps de son `GET`, qui contient les variables de l'instance, jeton compris
  (R-1480). Rien de tout cela n'est écrit.
- **Sorties de `vastai`.** La sortie d'erreur est jetée, jamais lue. En cas d'échec, seul le code est écrit. **Une exception :**
  un délai dépassé (`subprocess.TimeoutExpired`, 300 s) n'est pas attrapé (l. 237, 342). Son message, imprimé par la trace de
  Python, contient la ligne de commande entière, dont `--env "-e … GH_TOKEN=…"` (M-1).
  - Démontré avec un faux `vastai` lent et le délai raccourci : type `TimeoutExpired`, non attrapé par `louer`, « jeton dans le
    message : True ».
  - Démonstration : `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl-sonde-v3/demo/demo_timeout.py`.

## 5. Essais rejoués (commande exacte de la consigne)

**186 passés** en 301,54 s, code 0. Le décompte par fichier (`--collect-only`) donne 66 + 52 + 19 + 49 = 186. La sortie versée
porte 223 essais, garde de calcul comprise (37) : 223 − 37 = 186, soit des comptes **égaux**. Les essais `unshare -pf` sont joués,
car `unshare -pf true` rend 0 ici. Ma sortie est dans
`/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl-sonde-v3/essais.txt`.

## 6. Commande de l'additif 3

Elle est juste sur les points demandés :
- `COMMIT_PRIVE`, `D` et `OFFRE` sont posés, et `D` est réécrit en clair dans le contrôle ;
- `env -i` passe `GO_ID`, `PATH`, `HOME`, `LANG`, `GH_TOKEN` et `VAST_API_KEY` ;
- `GO_ID=GO-2026-11-04-09` est en tête ;
- `-y` est dans le code (l. 270) ;
- `--verifier-seulement` passe avant la création ;
- `timeout 900 nice -n 10` est mis partout où il faut ;
- les contrôles à T0 + 40 et T0 + 70 sont tirés de `controles_utc`, avec recontrôle toutes les 30 min tant que le code est 5.

Il reste deux manques :
- `vastai` 1.8.3 n'est pas dans les préalables, alors que R-1477 a vu une session sans `vastai` (f-4) ;
- en tir, le contrôle de T0 + 40 tombe à l'instant même du `DELETE` de la minuterie (f-3).

## Points (une ligne chacun)

- **M-1 (majeure, courte) — délai dépassé de `vastai create` : jeton dans le terminal, aucun marqueur.**
  - `TimeoutExpired` n'est pas attrapé (l. 237 ; `louer` n'attrape que `Refus`, `OSError`, `ValueError` et `KeyError`, l. 342).
  - Sa trace affiche les arguments, `GH_TOKEN` compris : c'est la leçon de R-1480.
  - Aucun `.creation-incertaine` n'est écrit, alors qu'une instance a pu naître.
  - Correction : dans `_lancer`, `except subprocess.TimeoutExpired: raise h.Refus("vastai … : délai dépassé") from None` ; dans
    `louer`, marquer incertaine toute création en échec.
- **m-1 (moyenne) — code non nul de `vastai create` : aucun marqueur de création incertaine (l. 326-328).**
  - Une instance acceptée par Vast, mais dont la réponse est perdue, laisse permettre une seconde location, sans `etat.json` ni
    `controler`.
  - Correction : écrire `.creation-incertaine` pour tout `Refus` venu de `creer`, sauf ceux d'avant l'appel.
- **m-2 (moyenne) — principal sans borne propre (l. 182, 190).**
  - Si l'amorce, `git`, `apt-get` ou Python se bloquent, et que les `DELETE` sont refusés, le conteneur ne sort jamais.
  - La borne « sortie 10 min après l'échéance » est alors fausse. Démontré sous `unshare -pf`.
  - Correction : `timeout $(( FINVIE - $(date +%s) ))` sur l'amorce et sur les `apt-get`.
- **f-1 (faible) — `apt-get` sans `timeout` avant la minuterie (l. 171).** Il viole « la minuterie en tout premier » quand `curl`
  manque. Correction : le placer après la l. 177, sous `timeout 120`.
- **f-2 (faible) — attente finale non comptée.** `cout_maximal_usd` omet `ATTENTE_MINUTERIE_S` (au plus 300 s ; environ 60 s en
  pratique), et `verifier_plafond` accepte l'égalité.
  - Commande recommandée : 0,37 USD, ce qui reste sans effet.
  - Mode normal à 1 800 s : 0,53 USD, au-dessus du plafond.
- **f-3 (faible) — en tir, contrôle de T0 + 40 = instant du `DELETE` de la minuterie** (échéance = création + 2 400 s).
  - Le code 0, qui est la preuve du tir, ne se lit qu'à T0 + 70.
  - Sans signe de vie, le pilote détruit à T0 + 40 et devance le tir.
  - Proposition : premier contrôle à T0 + 45 en tir.
- **f-4 (faible) — préalable manquant.** `vastai --version` = 1.8.3 dans la session de la fille (R-1477).
- **f-5 (faible) — minuterie : étiquette lue différente donne une sortie 3, sans nouvel essai, puis « exited ».** C'est le bon sens
  de sécurité. Mais une étiquette vide (`"label": ""`) ou une clé `label` imbriquée lue la première (`head -1`) annulerait le tir.
  De même, `controler` refuse une étiquette `None` : si Vast n'a pas posé l'étiquette, seule la minuterie détruit.
- **f-6 (faible) — `controler` : un délai dépassé de `show instances` ou de `ls-remote` sort en code 1 (trace).** Ce code est
  absent de la table des codes. La trace ne porte aucun secret.
- **R-1 (réserve, nœud de Lazar) — « jamais démarrée, pilote coupé ».** Aucune borne mécanique, comme l'écrivent le code et
  l'additif. Seule une session la borne (R-1481).
- **f-f et f-g (réserves)** — inchangées, à relever par la sonde (additif, section 3).
