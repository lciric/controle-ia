# Devis du tour du collisionneur sur le choix de l'expérimentateur — v1

Écrit le 11 novembre 2026 à 15:41 UTC (heure relevée par `date -u`), avant tout appel, par l'opérateur neuf (Claude Opus 5.5)
de la session mère, sous **GO-2026-11-11-03** (plafond 15 USD) et la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-collisionneur-experimentateur-v1.md`
(`ef26f7ac305f3c6fd99860b6469a398b6fb127e9961981ef301a43f5cd61a743`, vérifiée). Programme `devis` du script, aucun appel.

## 1. Devis avec le script du tour du 9 novembre, inchangé

`collisionneur_v8.py` (`22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264`) sur `faits-v1.md` et
`question-v1.md` : **étage III, 15 cellules, 38,89 USD au pire cas, sans relance** (sortie complète :
`devis-sortie-v8-inchange-v1.txt`). Le pire cas dépasse 15 USD : la consigne (point 3) demande de retirer une espèce ou de
baisser le plafond de sortie, et de l'écrire.

Pire cas par espèce sur les trois tours (somme des lignes du devis) : A Fable 5.1 10,53 ; B Opus 4.6 15,79 ; C Argon 5,73 ;
D Kimi 1,15 ; E Astra 5,73. **Retirer une seule espèce ne suffit pas** (sans B, la plus chère au barème du script : 23,10) ;
il faudrait descendre à deux espèces (par exemple A et D, 11,68), ce qui ôterait l'essentiel du croisement.

## 2. Choix : baisser le plafond de sortie du premier essai, garder les cinq espèces

Script neuf (R12), `script-v1/collisionneur_v8_plafonds_bas_v1.py`
(`4ad78ccce8228aed2679c854eaec7ee4d2ab8f867098218387024adfeb1e7756`) : copie du v8 où ne changent que `MODELES[…]["max"]`
(plafond de sortie du premier essai) et `MODELES[…]["max_relance"]` de A, B, C et E, plus la ligne `VERSION` et un
commentaire d'en-tête ; aucune autre ligne (différence relue par `diff`). Les prix du script (barème haut) ne changent pas.

| espèce | modèle | plafond v8 (essai / relance) | plafond retenu (essai / relance) | plus grande sortie observée, avec réflexion |
|---|---|---|---|---|
| A | `claude-fable-5-1` | 64 000 / 128 000 | **22 000** / 64 000 | 17 743 (tour du 9 novembre, E3-T3) |
| B | `claude-opus-4-6` | 64 000 / 128 000 | **10 000** / 64 000 | 7 851 (tour du 9 novembre, E3-T1) |
| C | `gemini-4-argon` | 32 000 / 65 536 | **18 000** / 32 000 | 13 618 aux tours d'étage III, 15 423 au plus (journaux du collisionneur du 22-23 octobre, `gemini/01_DONNEES_PRIMAIRES_BRUTES/…/journal.jsonl`) |
| D | `kimi-k3.1-pro` | 32 000 / 65 536 | 32 000 / 65 536 (inchangé) | 20 444 (tour du 9 novembre, E3-T1) |
| E | `gpt-6-astra` | 32 000 / 65 536 | **8 000** / 32 000 | 5 056 (tour du 9 novembre, E3-T3 ; compte du script, réflexion ajoutée) |

Devis avec ce script : **étage III, 15 cellules, 14,74 USD au pire cas, sans relance** (≤ 15 ; sortie complète :
`devis-sortie-v8-plafonds-bas-v1.txt`). Le devis compte quatre pièces croisées par cellule aux tours III.2 et III.3 : il reste
une borne haute si une espèce manque.

**Risque déclaré** : une sortie plus longue que le plafond retenu est « TRONQUE » ; le script relance alors la cellule une
fois au plafond de relance, **si** la dépense consignée plus le pire cas de la relance tient sous le plafond du run ; sinon il
s'arrête (code 4) sans appel, et la cellule est traitée comme une absence, consignée telle quelle.

**Essai hors réseau** (bac à sable, appelants factices, aucune clé, aucun appel) : étage III de bout en bout, 15 cellules,
une troncature simulée de A suivie de sa relance à 64 000, `verifier` sans problème ; plafonds servis conformes au tableau.

## 3. Bornes du tour

- **Plafond du run** : `--plafond-usd 15` (le script vérifie, avant chaque appel, dépense consignée + pire cas de l'appel).
- Dépense consignée par le script au **barème haut** du script : Fable 5.1 10/50 USD par million de jetons (égal au tarif
  public lu dans la référence de l'interface, mise en cache le 3 novembre 2026) ; Opus 4.6 15/75 (tarif public 5/25 : compte
  environ trois fois trop haut) ; Argon 10/50 et Astra 10/50 (supposés hauts, non lus) ; Kimi 2/10. La dépense consignée est
  donc, au plus, une borne haute de la facture des quatre fournisseurs appelés directement.
- **Relais Kimi** (`relais_kimi_v4.py`, `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e`, même relais
  que le 9 novembre) : port 8789, modèle permis `kimi-k3.1-pro`, **plafond 3 USD**, au plus 8 appels, prix 2 / 10 / 2,
  délai 1 800 s, silence 600 s ; il impute aussi une réserve aux appels refusés par l'amont (429), qui n'est pas une
  facture : les deux comptes de Kimi seront rapportés.
- Attendu (estimé, d'après le tour du 9 novembre, à 11 cellules pour 10,89 USD, et des faits cinq fois plus courts) :
  environ 7 à 11 USD consignés.

## 4. Mécanique (celle du 9 novembre, sauf ce qui précède)

- Clés par leur nom, sous `env -i`, jamais affichées : `ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD"` (sans
  `ANTHROPIC_BASE_URL`) ; `GEMINI_API_KEY="$GEMINI_API_KEY"` (jamais `GEMINI_API_KEY_2`, réservée à d'autres usages,
  R-1783) ; `OPENAI_API_KEY="$OPENAI_API_KEY"` ; Kimi par son relais, qui seul reçoit `KIMI_API_KEY`.
- Interpréteurs : relais par `/home/user/controle-ia-travail/.venv/bin/python` (bibliothèque standard) ; collisionneur par un
  environnement Python du bac à sable de l'opérateur (Python 3.13.18, `anthropic` 2.3.0, version des tours précédents), parce
  que `.venv` n'a pas le paquet `anthropic` et que l'opérateur n'écrit pas hors de ses chemins.
- Refus : consigné tel quel, jamais reformulé ; absences par `--accepter-absence`, suite du même run ; relais arrêté par son
  numéro de processus (R10).
