# Orchestrateur du pôle, version 0.7.0 — v44 : réponse courte à la contre-lecture CL10 de la v43 — LISEZMOI v44

Lignée conv-audit (instance de reprise, Opus 5.5), écrit après le relevé `date -u` de **09:28 UTC** le 29 octobre 2026
(travail commencé à 09:05 UTC) ; v1 à v43 gardées (R12). Répond à la contre-lecture CL10 de la v43 (Opus 5.5,
`contre-lecture-v43-cl10.md` : voie (β) non lançable telle qu'écrite, CL43-01 ; CL43-02 et CL43-03 majeurs ; CL43-04 à 07
mineurs ; CL43-08 information), dans le **périmètre minimal pour lancer** fixé par session-depot (choix fixés : CL43-01,
02, 03, X01, 05, 08), plus un **ajout de Lazar** relayé en cours de travail (10:09 heure de Paris : mesures de convergence
au manifeste de fin). **v44 n'est pas contre-lue.**

**Entrées et ligne de commande.** La forme des fichiers d'entrée (liste blanche, question, pièces, matériau, témoins,
attestations) **ne change pas**. La ligne de commande gagne **une option** : `--budget-passe-2-externe-usd` (sans elle, la
passe 2 prend le plafond de la passe 1, comme en v43). La ligne (β) du devis ne passe qu'avec elle.

| constat | correction | essai qui le démontre (`TestV44`, échoue sur la v43, passe sur la v44, sauf mention) |
|---|---|---|
| **CL43-01** aucun plafond propre à la passe 2 ; (β) somme 13,0 > 12,8 | `--budget-passe-2-externe-usd` (lanceur) et `budget_passe_2_externe_usd` (cœur, `verifier_reglages`) : plafond de la seule passe 2 de chaque proposeur externe, donné à sa session (`PLAFOND_SESSION_USD`) ; défaut : le plafond de sa passe 1 ; somme externe = contrôle + passe 1 + passe 2 + juge + contrôle du bras ; réel fini > 0, avec `--proposeur-externe` et `--seconde-passe` seulement (sinon code 2) ; écrit au manifeste de départ | `test_cl43_01_plafond_de_passe_2_et_somme_externe_de_beta` (pièce 750 000, matériau 350 000 : (β) → somme **12,4** ≤ 12,8, acceptée, passe 1 gardée à 884 819 ; `--budget "proposeur_ideation\|gemini-argon=3.1"` à la place → « 13.00 > total externe 12.8 », code 2, Argon jamais appelé, aucun fichier ; NaN, 0, sans seconde passe : refusés ; v43 : argument inconnu) |
| **CL43-02** sous la garde donnée, passes d'Argon gardées sans provision ni plafond | `garde_passe_externe` : chaque passe d'un proposeur externe est gardée **avant envoi**, sur sa consigne réelle, contre **son propre plafond** (2,5 ; passe 2 : son plafond) / prix (`--prix-entree-usd-par-million-jetons`) **moins la provision de sortie** = `--nombre` fiches × taille de fiche provisionnée × 5 ; la taille donnée **ne désarme plus** cette garde (la plus petite des deux) ; taille de fiche provisionnée : passe 1, `TAILLE_FICHE_PROVISIONNEE_PASSE` = **8 000** ; passe 2, la plus grande de 8 000 et de la **plus grande fiche admise** (servie) du proposeur à sa passe 1 ; la passe 1 (connue d'avance) est en plus gardée **avant tout contrôle** (`verifier_reglages`, `garder_passes_externes`) : refus scellé `refus-taille-K.json`, rien payé ; la passe 2, dans le cœur : refus sans envoi, manifeste de fin scellé en erreur, gardes au journal (`plafond_usd`, `taille_fiche_provisionnee`) | `test_cl43_02_passe_2_refusee_avant_envoi_fiches_de_8950` (sous (β), Argon au barème 8,3 et 41,5, fiches de ≈ 8 950 : contrôle 3,02 et passe 1 2,31 payés, **passe 2 refusée avant envoi** (1 175 148 > 1 493 975 − 40 × taille de fiche), au lieu de 3,18 payés) ; `test_cl43_02_fiches_maximales_et_fiches_courtes` (passe 1 à 1,0 → refus avant tout contrôle, scellé, rien payé ; fiches au maximum par champ : voir la réserve ci-dessous ; au cœur, passe 1 tenue : passe 2 refusée avant envoi, garde 0 ; fiches courtes sous (β) : gardes 884 819 et 1 173 975, bras au barème 8,3, **classement à trois juges** ; `--mesurer-consignes` rapporte les gardes des passes) |
| **CL43-03** reprise d'un contrôle Claude sur un relais relancé | `filtrer_reprises_claude` (lanceur) : un contrôle Claude réussi n'est repris que si la **dépense lue au relais maintenant** n'est pas plus basse que celle lue juste après ce contrôle (`relais_apres.depense_usd` de la tentative) ; plus basse (relais relancé), non lue, ou relais illisible : **rejoué** ; motif écrit au manifeste de départ et au journal du cœur (`motifs_reprise_controles`), à la tentative scellée et sur la sortie d'erreur ; moteur simulé (aucun relais) : repris, comme en v43 | `test_cl43_03_controles_claude_rejoues_si_le_relais_a_ete_relance` (chemin du moteur réel, kit, bac à sable et relais remplacés par des faux locaux, aucun réseau ni clé : relais gardé → contrôles Claude repris, motif « relais non relancé » ; relais relancé à 0 → **rejoués** (v43 : repris), motif « rejoué : relais relancé », coût imputé 0,8) |
| **X01** (CL43-07) fichier changé entre deux tentatives jamais essayé | aucun code : la clé de reprise portait déjà l'empreinte de la consigne de contrôle (et l'identité de la commande ou le moteur et l'adresse du relais) | `test_x01_fichier_d_entree_change_entre_deux_tentatives` (pièce changée, liste blanche refaite : Argon rejoué, empreinte de consigne différente, Claude repris) ; **passe sur la v43** (code juste) ; tue le défaut X01 (clé sans l'empreinte : l'essai échoue, vérifié sur une copie) |
| **CL43-05** « la phrase “trois tentatives” est retirée » faux | la borne est **gardée** (garde-fou) et dite : la relance est bornée **par les sommes ET par `MAX_TENTATIVES_BRAS` = 3** tentatives de contrôle (message du refus de la quatrième, motif de la troisième, docstring) | `test_cl43_05_relance_bornee_par_les_sommes_et_par_trois_tentatives` (v43 : « plus de relance sans un mot de Lazar » seul) |
| **CL43-08** seuil 1 493 976 | aucun code : le code calcule **1 493 975** (3,1 / 2,075 × 10⁻⁶ = 1 493 975,9, tronqué) | — |
| **Ajout de Lazar** mesures de convergence | `mesures_convergence` au **manifeste de fin seulement** (clé `mesures_convergence`, par proposeur → par fiche) : version de passe 2 (même nom, sinon texte le plus proche), distance d'édition (1 − rapport de `difflib.SequenceMatcher` sur les mots), Jaccard des sources citées (`arxiv:NNNN.NNNNN`, `[p.N]`), sources en passe 1 et 2, sources nouvelles en passe 2 (absentes de la passe 1 et des fiches servies), part des pièces servies citées ; `pages_lues` nul, motif « course sans outils de lecture » (forme du tour (c)) ; jamais servies aux juges ni au classement (N-053) ; un échec du calcul est écrit (`erreur`), il n'arrête pas la course | `test_mesures_de_convergence_au_manifeste_de_fin` (fiche modifiée : distance attendue, Jaccard 0,666667, une source nouvelle, pièces citées 0 puis 1 ; fiche identique : 0 ; rien dans le classement, les fiches validées, la lecture, les consignes des juges) |

**Réserve sur CL43-02 (point demandé non tenu tel quel).** « Fiches au maximum par champ → passe 1 refusée avant
envoi » est impossible sans refuser toute course : la passe 1 est gardée **avant** que ses fiches existent. Une provision
de passe 1 à la fiche maximale (8 × 44 259 × 5 = 1 770 360 caractères équivalents, 3,67 dollars à 8,3) donne une garde 0 et
refuse toute passe 1 (v43 l'avait déjà dit) ; même 12 000 (provision de la v43) refuse la passe 1 de (β) (752 440 > 724 819)
et toute passe 2 de (β) (≥ 1 110 020 > 1 013 975). J'ai pris **8 000** (exemple de CL10) : sous (β), la passe 1 part tant
que Argon rend des fiches de moins de ≈ 11 300 caractères en moyenne ; au-delà, si la vraie commande ne s'arrête pas à
`PLAFOND_SESSION_USD`, la passe 1 dépasse son plafond (rejeu D-β-max : 5,21 > 2,5, `budget_depasse`, course arrêtée, passe 2
jamais envoyée). Vérifier avant le GO que la vraie commande d'Argon borne sa sortie (CL10, § 8).

**Gardes prises aux réglages (β)** (prix 8,3 → 2,075 × 10⁻⁶ dollar par caractère ; rapport sortie/entrée 5) :
- course (contrôle d'Argon) : donnée, 1 490 000 (le défaut de la course, inchangé, garde la provision de 12 000) ;
- passe 1 (2,5) : min(1 490 000 ; 1 204 819 − 320 000) = **884 819** ; consigne réelle 752 440 ;
- passe 2 (3,1) : min(1 490 000 ; **1 493 975** − 40 × max(8 000 ; plus grande fiche admise de passe 1)) = **1 173 975**
  pour des fiches ≤ 8 000 ; seuil ≈ **8 100 caractères par fiche d'Argon** (CL10 : dépassement réel au-delà de ≈ 8 000) ;
- bras : défaut 1 166 746 (ne pas donner `--taille-max-consigne-externe-bras 1686000`, CL43-04).

**`--mesurer-consignes`** aux réglages du devis, ligne (β) (pièce 750 000, matériau 350 000, question de 19, témoins de CL10,
sortie redirigée dans mon brouillon, aucun fichier créé, code 0) :

| consigne | caractères | coût d'entrée à 8,3 | avec provision | garde | passe ? |
|---|---|---|---|---|---|
| contrôle d'Argon (course) | 1 457 167 | 3,0236 | — | 1 490 000 (donnée) | oui |
| passe 1 | 752 440 | 1,5613 | 2,2253 (320 000) | 884 819 | oui |
| passe 2, fiches de passe 1 ≤ 8 000 | ≤ 1 173 975 admis | — | (320 000) | 1 173 975 | selon les fiches |
| passe 2 maximale (huit fiches de 44 259) | 1 456 692 | 3,0226 | 6,6961 (1 770 360) | 0 | non |
| juge au maximum (52 fiches de 44 259) | 2 131 096 | 4,422 | — | 1 166 746 (défaut) | non |
| contrôle du bras | 41 | — | — | — | — |

**Rejoué avec les outils de CL10** (`scenarios_cl10.py` copié dans mon brouillon avec deux lignes changées : la ligne
(β) avec `--budget-passe-2-externe-usd 3.1`, le bras sans `-bras 1686000` ; `lanceur_cl10.py`, `argon_factice_cl10.py`
inchangés ; `python3 -I -B` hors de P, environnement propre, copie de l'arbre v44 ; Argon factice qui ne se borne jamais) :

| scénario (pièce 750 000, matériau 350 000, huit fiches, seconde passe) | v43 (CL10) | v44 |
|---|---|---|
| (β) exacte | refus « 13.00 > 12.8 » | acceptée (12,4) |
| **D-β** : barème 8,3, fiches ≈ 8 950 (`g700`, 9 066 servies) | passe 2 3,18 > 3,1 payée, perdue (Claude 0,4, Argon 8,51) | contrôle 3,0236, passe 1 2,3042 ; **passe 2 refusée avant envoi** (1 175 148 > 1 131 335) ; Claude 0,4, Argon **5,33**, total 5,73, aucun classement |
| **D-β-max** : fiches au maximum par champ | passe 1 5,21 > 3,1, perdue (Argon 8,23) | passe 1 gardée à 884 819, partie ; 5,2087 > 2,5, `budget_depasse` ; passe 2 jamais envoyée ; Claude 0,4, Argon 8,23 (réserve ci-dessus) |
| barème 8,3, fiches réelles (≈ 4 500) | passe 2 2,74 > 2,5, perdue (passes à 2,5) | passes 1,9357 et 2,7396 ; bras 0,2584 ; **Claude 40,00, Argon 7,96, total 47,96, trois juges** |
| barème 8,3, petites fiches | — | Claude 40,00, Argon 7,18, total 47,18, trois juges |
| pire cas au plafond, petites fiches | — | Claude 40,00, Argon **12,4** (3,1 + 2,5 + 3,1 + 0,2 + 3,5), total **52,4**, trois juges |

## Ligne de lancement (β)

Relais (clé tenue comme d'habitude par session-depot, inchangé) :
`python3 -I -B pole/relais_reel.py --plafond-usd 40 --reserve-par-appel 4 --port 8787 …`

Course :
```
python3 -I -B demonstrations/ideation_v1.py SORTIE --moteur claude-sdk --confirmer-moteur-reel --url-relais http://127.0.0.1:8787 \
  --liste-blanche LISTE.json --question Q.md --piece P.md … --materiau M.md … --seconde-passe --attestation-materiau ATT.json \
  --temoins TEMOINS.json [--piece-juge …] --proposeur-externe argon=gemini-argon --juge-externe argon=gemini-argon \
  --commande-externe "…" [--variable-transmise …] --horodatage "…" --taille-max-pieces 750000 \
  --budget-controle-externe-usd 3.1 --budget-passe-2-externe-usd 3.1 --budget-externe-usd 12.8 \
  --prix-entree-usd-par-million-jetons 8.3 --taille-max-consigne-externe 1490000
```
Bras (après l'attestation de lecture humaine) :
```
python3 -I -B demonstrations/ideation_v1.py SORTIE --bras-rapporte-differe --attestation-lecture-humaine ATTEST.json \
  --juge-externe argon=gemini-argon --commande-externe "…" --prix-entree-usd-par-million-jetons 8.3 --budget-externe-usd 12.8
```
Proposeurs et juges Claude, plafonds Claude (total 40), délais : défauts. Somme Claude 40,0 ; externe 12,4 ≤ 12,8.

## Restes déclarés

- **CL43-04** (option `-bras 1686000`) : aucun code ; ne pas la donner (défaut 1 166 746).
- **CL43-06** (empreinte de chaque argument fichier de la commande d'Argon) : non traité ; vérifier avant le GO que la vraie
  ligne de commande d'Argon ne nomme aucun fichier qui change.
- **CL43-07 hors X01** : X34 (« passerait » de `--mesurer-consignes`), X15, X16, X30 non traités.
- **CL43-03, conséquence** : aux réglages du devis (relais 40, réserve 4, total Claude 40), une relance après des contrôles
  Claude payés exige de relancer le relais (CL10) ; la v44 rejoue alors ces contrôles : somme Claude 40,4 > 40, relance
  **refusée sans dépense** (mot de Lazar : total 40,4 ou tolérance). Le calcul `relance_relais_relance_a_neuf` de la tentative
  ne compte pas encore ce rejeu (il peut dire « relançable » à tort ; la relance elle-même refuse, sans dépense).
- La garde par défaut de la **course** garde la provision de 12 000 (non demandée) ; seules les gardes des passes prennent
  8 000. Trois essais anciens changent pour la nouvelle provision des passes, chacun dit dans sa docstring :
  `TestV43.test_cl42_01_controle_releve_seul_refuse_sans_depense_et_garde_donnee_passe` (cas sain passé aux réglages (β) :
  au prix 10 et passes à 2,5, la passe 1 serait refusée ; gardes 884 819 et 1 173 975 au lieu de 1 500 000) ;
  `TestV43.test_cl42_01_passe_gardee_contre_son_propre_plafond_avant_envoi` (provision 320 000 au lieu de 480 000 ; 680 000
  au lieu de 520 000) ; `TestV43.test_cl42_03_mesurer_consignes_sans_appel` (680 000 et 320 000).
- Non vérifié : vraie commande d'Argon (barème, sortie, borne à son plafond), sessions Claude réelles, relais réel.

**412 essais passent** (412 = 405 + 7 : `TestV44` dans `test_v7_ideation`) ; deux exécutions complètes sur l'arbre final
(187,2 s et 192,2 s), aucun processus survivant, `essais/_tmp` retiré, aucun `.pyc` suivi réécrit
(empreintes comparées au relevé de début).

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v44.txt
```
