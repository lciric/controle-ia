# Rapport du développeur — lanceur de T0.6 v6 (additif aux rapports v1 à v5) — fille 10, Sonnet 5.5, 7 novembre 2026

**Verdict : lanceur v6 prêt pour contre-lecture.** v6 = v5 + `reliability>=0.98` dans le filtre de la recherche de création (R-1660), rien d'autre. 280 essais réussis (suites v1 à v6), banc de mutations 18 sur 18 tuées, épreuve E1 v6 conforme (0 USD). Aucune clé, aucune location, aucune dépense.

## Changement
- `src/controle_ia/t06/session_v5.py` (nom neuf, R12) : `FIABILITE_MIN_OFFRE = 0.98`, et `filtre_recherche` rend `num_gpus=1 rentable=true gpu_name=<carte> reliability>=0.98 cpu_ram>=<Go> cpu_cores_effective>=<n> disk_space>=<Go> dph_total<=<prix max>`. Le reste du module est celui de `session_v4.py`.
- `scripts/lancer_t06_v6.sh` : copie de la v5 qui appelle `session_v5` (en-tête et libellés v6). Amorce inchangée (`amorce_instance_t06_v4.sh`).
- **Une seule source pour les filtres** : le générateur des ordres v3 (`brouillons/ordres-t06-e2-e3-v3/pieces/generer_ordres_v3.py`) lit les filtres dans `session_v5.filtre_recherche` appliquée aux configurations d'épreuve (E2 « course » : carte modeste ; E3 « course » : A100 ; E3 « relance » : H200) et refuse tout filtre de lecture qui n'en est pas un.

## Essais ajoutés (`tests/test_t06_v6_scripts.py`, 6 essais : les 4 de la v5 rejoués avec le lanceur v6 + 2 neufs)
- `test_filtre_de_creation_porte_la_fiabilite_et_le_fake_le_recoit` : la chaîne entière du filtre ; le faux `vastai` reçoit bien `reliability>=0.98` dans l'appel de recherche de `creation auto`.
- `test_filtres_de_lecture_des_ordres_identiques_a_ceux_du_lanceur` : tout filtre `'num_gpus=1 …'` des ordres générés est l'un des filtres du lanceur ; le filtre modeste de l'ordre d'E2 est celui de la configuration d'E2 ; l'ordre d'E3 n'en contient qu'un (A100) ; aucun reste de `lancer_t06_v5`.

## Preuves
- Suites jouées d'un trait : **280 passed in 365,50 s** (`tests/test_t06_*.py`, v1 à v6).
- Banc ciblé `scripts/banc_mutations_t06_v6.py` : 18 mutations (les 14 de la v5 retargetées sur le lanceur v6 + 4 neuves : fiabilité absente du filtre, seuil abaissé, filtre de l'ordre d'E2 non lu dans le lanceur, filtre d'E3 lu sans la fiabilité), 18 tuées, témoin vert (`banc-mutations-t06-v6.{log,json}`).
- E1 v6 (`scripts/epreuve_e1_t06_v6.sh`, `epreuve-e1-t06-v6-journal.md`) : code 0, 73 essais joués par l'amorce, 0 occurrence de mot interdit.

## Écart d'énoncé du texte de T0.6
Le texte de T0.6 ne mentionne pas la fiabilité (constat de la mère, R-1660) ; la valeur 0,98 vient des lectures de l'ordre d'E2 et de `hote_durable_a1_v3.OFFRE_MIN`. Elle est en constante du module, pas en clé de configuration : la changer exige un nouveau module (R12).

## Risques
1. Le filtre n'est pas encore éprouvé contre le vrai `vastai` : l'épreuve E2-1 (lectures, 0 USD) le fait avant toute location ; le contrôle de prédiction (rang 1 lu = rang 1 de `creation auto`, à l'identifiant près) est écrit à l'ordre d'E2 v3.
2. `reliability` est le nom de clé de la recherche ; si Vast le refuse ou le renomme, `creation auto` échoue sans dépense (code 2).
3. Une fiabilité plus stricte réduit la liste filtrée : trois rangs suffiront moins souvent (code 3, arrêt et message).
