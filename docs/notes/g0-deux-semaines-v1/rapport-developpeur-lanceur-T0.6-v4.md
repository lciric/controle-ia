# Rapport du développeur — lanceur de T0.6, v4 (additif aux rapports v1 à v3)

- Statut : rendu le 2026-11-06 (heures par `date -u`) par la fille 10 (session de développement, Claude Sonnet 5.5), qui n'a écrit ni les lanceurs v1 à v3 ni les contre-lectures. Ordre : `docs/procedures/ordre-fille-10-developpement-t06-v1.md`, tâche D1. Rien n'est loué, aucune clé lue, aucun modèle appelé, aucune dépense ; rien d'existant modifié (R12 : tout fichier neuf porte `_v4`, `_v5`, `familles_v3`, `session_v3`, `brouillon4` ou `epreuve`) ; aucun `.sha256` écrit (la mère scelle).
- Branche : `prep/t06-lanceur-v2` (arbre `/home/user/wt/t06-lanceur-v2`), au-dessus de `4f1b402d`. Sources : `corrections-code-lanceur-T0.6-v4.md` (`65259028…`), contre-lecture du lanceur v3 (`b338a812…`), messages de la mère (R-1626 : registre des GO de `main`).

## 1. Traitement

| point | état | où, et comment c'est éprouvé |
|---|---|---|
| **C-V4-1** fin de run sous le verrou | fait | `scripts/amorce_instance_t06_v4.sh` : `prendre_verrou`/`liberer_verrou` (même `flock -w 1500` que `t06-consigner.sh`), pris après la fin du run et du relais, relâché avant `arreter_instance` ; `commit_verifie` rend 0 (fait), 10 (index vide), 1 (échec, réessayé une fois) ; un `git add` en échec est une erreur de chaîne, jamais un index vide ; échec en fin de run → poussée de ce qui existe, `t06-fin-anormale`, code 1 ; `git status --porcelain -- runs diag donnees traces` vide avant `t06-fin-normale` (rattrapage `consigner_partiel "fin de run"`, puis fin anormale) ; fichier retiré pour taille (C11) = fin anormale ; délai de la consignation de la minuterie 900 → 2 400 s (> attente du verrou 1 500 s). Essais : `-k c_v4_1` (cas sain, `index.lock`, crochet de commit refusé une fois / toujours, status non vide rattrapé / non rattrapable, verrou non obtenu, verrou relâché avant l'arrêt, minuterie concurrente sans fichier perdu et ordre des commits gardé, code de sortie 2 de la consignation) |
| **C-V4-2** essai d'égalité sur jetons réels | fait | `sondes/familles_v3.py` (256 jetons réels du sous-ensemble, demi-précision, tolérance 10⁻¹²), `t06/configuration_v4.py` (clé booléenne `egalite_jetons_reels`, sans valeur implicite ; vrai sous le paquet gelé refusé), `t06/lanceur_v4.py` (pool = actions du sous-ensemble, lu dans son manifeste ; essai raté ou pool vide → couple en « échec », jamais l'ensemble ; essais écrits sous `…/reels`) ; configuration réelle du brouillon 4 : `mahalanobis_calcul = produit_matriciel_v2` (R-1624), `egalite_jetons_reels = true`, `familles_descriptives` inchangées |
| **C-V4-3** (non demandé tel quel, nécessaire aux ordres E2/E3) | fait | `t06/session_v3.py` (GO et plafond en arguments, plafond du registre avec commentaire entre parenthèses admis, épuisement simulé), `scripts/lancer_t06_v4.sh controles-epreuve`, GO et plafond lus dans la configuration, branche `essai/` imposée, `T06_EPUISEMENT_SIMULE_S`, `T06_TESTS_ARGS`, amorce `EPREUVE_GO_ID` (sans préenregistrement en mode réel, épreuve jamais décisive), ligne `MATERIEL` (MemTotal, cœurs, `flock`) ; configurations `config-t06-epreuve-e{2,3}-v1.json` (générées par `scripts/ecrire_configs_epreuves_t06_v1.py`), tâches synthétiques `donnees/t06-epreuve-e{2,3}/` (à verser avec `git add -f`) ; extracteur à liste blanche `scripts/extraire_mesures_epreuve_t06_v1.py` (aucune sonde décisive lue) |
| **R-1626** registre des GO de `main` | fait | `T06_REGISTRE_GO` obligatoire pour une épreuve (contrôles et création) ; le registre du commit cloné doit porter le GO aussi (l'amorce le relit) ; cas sain et trois artefacts (`-k registre_des_go_de_main`) |

Signatures de la course inchangées de la v3 (`controles`, `creation`, `apres-creation`, `surveillance`) ; sous-commande ajoutée : `controles-epreuve DOSSIER_NEUF COMMIT CONFIG_CHEMIN [JOUR]`. Branche par défaut de la course : `calcul/t06-reel-v4`.

## 2. Comptes (une suite à la fois, `nice`, `--basetemp` supprimé après)

- Essais neufs v4 : configuration 10, familles 8, extracteur 2, lanceur jouet 12, scripts 53 ; suite `tests/test_t06_*.py` (v1 à v4) : **270 passed** en 316,9 s (6 novembre, après tous les changements).
- **Banc de mutations v4** (`scripts/banc_mutations_t06_v4.py`) : 112 mutations (les 55 de la v3 rejouées sur les fichiers v4, 57 des corrections C-V4-1 à C-V4-3 et R-1626), 8 témoins verts. Passe 1 (`banc-mutations-t06-v4.log`) : 106 tuées, **6 survivantes**. Pour chacune, un essai neuf (message exact du refus, code de sortie 2 de la consignation) ou une mutation mal posée corrigée (registre du commit non relu) ; passe 2 ciblée (`--filtre=`, `banc-mutations-t06-v4-passe2.log`) : **6/6 tuées**. Les 106 premières n'ont pas été rejouées après l'ajout des essais (seuls des essais ont été ajoutés ou précisés).
- **E1 v4** (`scripts/epreuve_e1_t06_v4.sh`, 0 USD, `epreuve-e1-t06-v4-journal.md`) : passe A (paquet gelé) et passe B (`produit_matriciel_v2`, jetons réels) en code 0 ; 73 essais joués par l'amorce (« 73 passed ») ; 0 mot interdit dans journal, `run.err`, `run.json`, traces ; passe B : 24 essais d'égalité dont 12 sur jetons réels, tous égaux, écart relatif maximal 4,4·10⁻¹⁵ ; trois commits poussés ; plus gros fichier 2 Mo ; ligne `MATERIEL` présente.

## 3. Empreintes (sha256 des fichiers au dernier commit de la branche, relevés par `sha256sum`)

| fichier | sha256 |
|---|---|
| `scripts/amorce_instance_t06_v4.sh` | `c4cf05a12e4488338d158bed9ba3efbbc1540be0557b221238cf10d079b1083e` |
| `scripts/lancer_t06_v4.sh` | `6e06ae6b32f2886d8a76d5562728e8af7dc00bf62760c43d1e7b41c79726f01a` |
| `scripts/banc_mutations_t06_v4.py` | `e8805a88a92c5ffa8616386f674f3901bd0bf4205f526b27faf9169c8057cc26` |
| `scripts/epreuve_e1_t06_v4.sh` | `8052a3f214936f98641dc5d7c3285268a4615d583c766e8732dc779b4e0bfdf9` |
| `src/controle_ia/t06/lanceur_v4.py` | `aa290ac5fdd9a4f4451d35be26e767b0090686dd51cb9bbe216b04b92593449e` |
| `src/controle_ia/t06/configuration_v4.py` | `d2cd7c4d610836093ae509aa8f60e38cb3fbb0946d9c21f353f32eb547ff97b6` |
| `src/controle_ia/t06/session_v3.py` | `365d2fde7fe9c4670fd3f2bcb404c3979b1db4e3cc862f0a4a46acf867b4bcf3` |
| `src/controle_ia/sondes/familles_v3.py` | `11a3a3b21e1b73a5fb2230f91adf996b415c41e2fa98c197189c51734f6f9b04` |
| `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json` | `0ffb3c3809fd49c224da741acec4f94e41b643e65a3b82962d507fc5d367c47b` |
| `docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v1.json` | `b599c9a5cf84cbb2ab99340334d6727eb4a769c7d3307dd2ac4641ac36c88459` |
| `docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v1.json` | `98a53db87b740751ac66b32cf33b0af682d047910e8e3abd91b3013544b57545` |

(Les empreintes de ce rapport lui-même et des fichiers modifiés après sa rédaction sont dans le message de la mère ; les configurations d'épreuve et de la course n'ont pas de `.sha256` : la mère les scelle, l'amorce l'exige.)

## 4. Trois risques

1. **Épreuves E2/E3 jamais jouées** : l'interface réelle de Vast (clés, unités, `start instance` après un arrêt, relevé de facture) et la durée de l'installation `requirements-gpu.txt` ne sont éprouvées que par des faux (`vastai`, `curl`, `df`) ; les ordres (brouillons non contre-lus, `brouillons/ordres-t06-e2-e3-v1/`) fixent des offres et des bornes (carte modeste RTX 4090, 0,60 USD/h) à confirmer.
2. **Fin anormale plus stricte** : un fichier retiré pour taille ou un `git status` non vide donne maintenant `t06-fin-anormale` et le code 1 (la v3 finissait « normalement ») ; au second démarrage, une fin anormale suit la voie « run interrompu » (consignation, destruction). À valider par la mère avant la course.
3. **Essai sur jetons réels** : écart relatif sur des jetons proches de μ (score minuscule) pourrait dépasser 10⁻¹² sans erreur réelle ; mesuré seulement sur jouet (4,4·10⁻¹⁵) ; E3 est la première mesure sur activations réelles.
