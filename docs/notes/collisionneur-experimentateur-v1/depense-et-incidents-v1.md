# Tour du collisionneur sur le choix de l'expérimentateur : dépense et incidents — v1

Écrit le 11 novembre 2026 à 16:13 UTC (heure relevée par `date -u`) par l'opérateur neuf (Claude Opus 5.5) de la session
mère, sous **GO-2026-11-11-03** (plafond 15 USD). Aucune lecture du contenu des cellules (la synthèse revient à un autre
lecteur) ; seuls les statuts, les jetons et les coûts du journal sont relevés ici.

## 1. Déroulé (heures de la console, UTC)

- 15:41:50 : relais Kimi `relais_kimi_v4.py` lancé (processus 3741, port 8789, plafond 3 USD, au plus 8 appels) ; état :
  variable de clé effacée de l'environnement du processus.
- 15:42:03 → 15:49:34 : premier lancement de l'étage III (`console-run-e3-v1-masque-v1.log`) : A, B, C de III.1 valides ;
  **D (Kimi) en échec**, HTTP 429 de Moonshot, « suspended due to insufficient balance » (`exceeded_current_quota_error`),
  arrêt du script (code 5), aucun autre modèle essayé. Même incident que le 9 novembre (R-2019).
- 15:49:53 : état du relais relevé (`relais-v1/etat-apres-v1.json` : un appel, statut 429) ; **relais arrêté par son numéro
  de processus, 3741, à 15:49:58** (R10).
- 15:50:09 → 16:12:46 : même run relancé avec **absence acceptée des trois cellules de D** (`E3-T1-conception-D`,
  `E3-T2-critique-croisee-D`, `E3-T3-reponse-D`), Kimi ne pouvant servir sans recharge du compte
  (`console-run-e3-v1-relance1.log`) ; étage III fini, code 0.
- 16:12:53 : `verifier run-e3-v1` (hors réseau) : **« tout tient »** (`verification-run-e3-v1.txt`).

## 2. Cellules

12 cellules valides sur 15 : A (`claude-fable-5-1`), B (`claude-opus-4-6`), C (`gemini-4-argon`) et E (`gpt-6-astra`),
chacune aux trois tours ; un seul essai chacune, fin normale, marqueur de fin présent, modèle servi égal au modèle demandé ;
**aucun refus, aucune troncature, aucune relance**. Absentes, acceptées : les trois cellules de D (Kimi), pour la raison
ci-dessus.

## 3. Dépense relevée par espèce (journal du run, `run-e3-v1/journal-masque-v1.jsonl`)

| espèce | modèle | essais (OK) | jetons d'entrée | jetons de sortie | coût au barème du script, USD |
|---|---|---|---|---|---|
| A | `claude-fable-5-1` | 3 (3) | 89 934 | 42 097 | 3,0043 |
| B | `claude-opus-4-6` | 3 (3) | 71 249 | 20 121 | 2,5778 |
| C | `gemini-4-argon` | 3 (3) | 56 996 | 19 928 | 1,5664 |
| D | `kimi-k3.1-pro` | 1 (0) | 0 | 0 | 0,0000 |
| E | `gpt-6-astra` | 3 (3) | 56 825 | 15 853 | 1,3609 |
| **total** | | 13 (12) | | | **8,5094** |

Lecture des barèmes : Fable 5.1 à 10/50 USD par million (égal au tarif public lu dans la référence de l'interface mise en
cache le 3 novembre 2026) ; Opus 4.6 à 15/75, alors que le tarif public est 5/25 : au tarif public, B coûte environ
0,8593 USD (calcul sur les jetons du journal) ; Argon et Astra à 10/50, barème supposé haut, non lu ; la sortie d'Astra
compte 14 780 jetons visibles plus 1 073 de réflexion ajoutés par le script (double compte possible si l'interface les
inclut déjà). **Kimi** : aucune facture (appel refusé par l'amont) ; le relais impute à son propre compte une réserve de
0,364024 USD à l'appel refusé (`etat-apres-v1.json`), qui n'est pas une dépense.

Sur les crédits de la clé `RR_ANTHROPIC_API_KEY_RIGAUD` : 5,5821 USD au barème du script (A + B), environ 3,8636 au tarif
public (calcul). Hors crédits : Argon 1,5664 et Astra 1,3609, soit 2,9273 au barème.

## 4. Fichiers d'origine non versés

Deux fichiers portaient en clair l'identifiant d'organisation et l'identifiant de clé du compte Moonshot (message d'erreur
du fournisseur ; non secret, mais sensible) : le journal du run et la console du premier lancement. Comme le 9 novembre,
**des copies masquées sont versées** (`run-e3-v1/journal-masque-v1.jsonl`, `console-run-e3-v1-masque-v1.log` : un
remplacement de chaque identifiant, rien d'autre ne change) ; les originaux sont gardés hors du dépôt, dans le bac à sable de
l'opérateur, avec leurs empreintes : `journal.jsonl` `91aeb030d97f1bcb4ec8522d876a434fbc9db3df663fa7cfd23557edf7f927d4`,
`console-run-e3-v1.log` `1e78563d5f48a60ec5c79e023854175326314618ad165926f1dc54ce598b51f7`. La vérification (`verifier`)
a été jouée avant ce déplacement.

## 5. Conséquence

Sans recharge du compte Moonshot qui porte la clé `KIMI_API_KEY` de cet environnement, Kimi ne peut servir ni au collisionneur
ni à aucun autre usage qui passe par ce compte (constat, sans proposition).
