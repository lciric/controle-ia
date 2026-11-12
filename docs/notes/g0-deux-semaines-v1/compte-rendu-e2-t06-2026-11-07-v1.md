# Compte rendu d'E2 (T0.6, lanceur v7, amorce v5) — fille 6, 7 novembre 2026

Ordre : `docs/procedures/ordre-fille-6-t06-e2-v4.md` (sceau 4c1113cd…, main 395b85aa) ; commit d'épreuve 0e52603c ; GO-2026-11-06-01 ; autorisation de location de Lazar (R-1655). Aucune valeur de clé, aucun résultat de sonde.

## Écarts acceptés (R-1667, R-1669, R-1683)
- Jeton : `CONTROLE_IA_GITHUB_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` sous `env -i` (valeur jamais lue).
- Arbre `git worktree` détaché à 0e52603c (au lieu d'un clone) ; branche A relue par `git worktree` (au lieu d'un clone complet).
- Environnement `/home/user/venv-depot` : numpy 2.4.6, Python 3.13.18.
- `verifier-arbre` à 0e52603c : 118 problèmes, aucun sur une pièce de l'épreuve (R-1669).
- vastai 1.8.3, VAST=/home/user/venv-vastai/bin/vastai ; W=/tmp/tmp.cTV7VcRAjd ; REGGO = registres/go.md de main 395b85aa.

## Tentatives antérieures (comptées dans le plafond)
- 59555071 (matin, lanceur v6, amorce v4) : silencieuse 39 min, disparue 11:18Z sans poussée ; facture 0,149.
- 59589344 (v7, 04d89122) : run mort sur « empreinte compagnon taches-evaluation.json.sha256 absente » ; détruite par moi ; facture 0,019.

## Instances de la troisième tentative
| | A | B | C |
|---|---|---|---|
| identifiant | 59590613 | 59598117 | 59601024 |
| offre / machine | 55214435 / 21042 | 59418319 / 17704 | 54486048 / 110506 |
| carte + stockage relevés (USD/h) | 0,3617 + 0,0417 | 0,4139 + 0,0472 | 0,4156 + 0,0556 |
| création | 15:23:09Z | 16:40:30Z | 17:09:01Z |
| fin | détruite par moi 16:39:29Z (minuterie absente au cas 2) | détruite par la minuterie ≤ 17:08:02Z | détruite à l'échéance ≈ 17:18:42Z |
| code de l'amorce | 0 | run interrompu (refus au redémarrage) | aucun run (échéance pendant l'installation) |
| branche / dernier commit | essai/t06-e2-v3-a f5be441f | essai/t06-e2-v3-b c4e865a9 | essai/t06-e2-v3-c 0e52603c (poussée initiale seule) |
| facture (USD) | 0,099 | 0,289 | 0,044 |

## Table E2-1 à E2-10
| n° | obtenu | verdict |
|---|---|---|
| E2-1 | neuf clés présentes et de bon type dans les quatre listes ; gpu_name « RTX 4090 », « A100 SXM4 », « H200 NVL » ; fiabilité : `reliability` (= `reliability2`, float, ≥ 0,98 aux rangs 1-3) ; `reliability_mult` existe aussi (non filtrée) | conforme |
| E2-2 | storage_total_cost avec 150 Go 0,041667 > sans 0,001852 ; prédiction R-1660 : rang 1 = machine 21042 = offre choisie. Prix réel : facture A gpu 0,320 + disque 0,042 = 0,362 USD/h = `dph_total` de l'instance (0,3617) ; lanceur : prix_carte + prix_stockage = 0,4034 → écart −10,3 % : **`dph_total` (avec --storage) inclut déjà le stockage ; le lanceur le compte deux fois** (surestimation prudente) | **non conforme** (± 5 %) |
| E2-3 | « commit 0e52603c… » sans clonage impossible ; « CLONAGE mode=jouet secondes=10 octets_git=100336549 octets_arbre=308253499 debit_Mo_s=40.86 motifs=27 » 10 s après commit ; poussée avant installation ; « branche … poussée (résultats, données légères, morceaux et traces) » ; branche A : 3 commits (résultats, morceaux, traces) — la poussée initiale ne crée pas de commit propre | conforme, sauf **3 commits au lieu de 4** |
| E2-4 | « ARRÊT OBTENU (état voulu « stopped », HTTP 200) » 15:27:01Z ; exited/stopped à 15:27:52Z | conforme |
| E2-5 cas 1 | A : DEMARRAGE 2, poussée d'abord, « sommeil (second démarrage après une fin normale, rien ne repart) », aucune ligne `run :` | conforme |
| E2-5 cas 2 | A : start 16:05:17Z mis en file par Vast (« Required resources are currently unavailable »), reparti 16:22:46Z ; poussée **avant** « destruction demandée … l'argent est épuisé » ; **mais aucune destruction par la minuterie** : exited, listée jusqu'à 16:39:15Z → détruite par moi | **attendu manquant isolé** (DELETE absent) |
| E2-5 cas 3 | B arrêtée 17:03:10Z en plein run (phase S50) ; au redémarrage : résultats partiels et morceaux committés, poussés, « refus … résultats partiels consignés, rien ne repart », destruction 180 s plus tard | conforme |
| E2-6 | C : échéance 17:18:42Z (maintenant + 600 s ; la formule donnait + 241 s) atteinte **pendant l'installation** (hôte lent : CLONAGE 125 s à 3,27 Mo/s) ; instance détruite ; **aucune consignation poussée** (branche v3-c = 0e52603c), journal de Vast perdu avec l'instance : lignes « ÉCHÉANCE … (C14) » / « consigné (échéance) » non observées | **non exercé / non observable** |
| E2-7 | « MATERIEL MemTotal_ko=65680708 coeurs=28 flock=oui » ; aucune ligne « outils absents » | conforme |
| E2-8 | 65680708 / (64141 × 1024) = 1,000 | conforme |
| E2-9 | B et C détruites par la minuterie (inventaire) ; A : minuterie sans DELETE au cas 2 ; t06-minuterie.log de A sur la branche : une ligne (« minuterie 54 : échéance …, dépense épuisée … »), pas de DELETE (A s'est arrêtée, pas détruite, au premier run) ; destructions manuelles par identifiant seulement | partiel |
| E2-10 | factures ci-dessous | conforme (≤ 1,5) |

## Montants (factures Vast relevées à 17:19:42Z)
59555071 0,149 ; 59589344 0,019 ; 59590613 0,099 ; 59598117 0,289 ; 59601024 0,044 ; **total E2 = 0,600 USD** (plafond 1,5). Estimations de `surveillance`/lanceur (cumulées passées en dépense antérieure) : 0,168 → 0,688 → 0,978 ; écarts : le repli « prix × durée » surestime (stockage compté deux fois, carte comptée pendant l'arrêt).

## Mesures d'exploitation (A, extraire_mesures_epreuve_t06_v1.py, code 0)
Fichier `$W/mesures-a.txt` (151 lignes) : distillation 5,9 s, adaptateurs float32, dose 0 identique, durées par couple 0,1 à 1,2 s.

## Autres constats
- Pilote CUDA de la machine 21042 trop vieux pour torch cu130 (« found version 12020 », `cuda_max_good` 12,2) : sans effet en jouet, à filtrer pour E3 (v8).
- Surveillance v6 (matin) : « POURSUIVRE » après disparition de l'instance ; v7 : « ARRET mort … absente à deux relevés » correct.
- Une instance arrêtée n'est pas toujours relançable aussitôt (cas 2 : 17 min en file).
- Inventaire final 17:19:26Z : aucune instance t06-e2 (4 instances : les trois R8 et 59288960, toutes arrêtées).
