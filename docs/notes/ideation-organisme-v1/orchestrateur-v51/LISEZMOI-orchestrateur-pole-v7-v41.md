# Orchestrateur du pôle, version 0.7.0 — v41 : réponse courte à la relecture CL7 de la v40 (« lançable ; aucune relance avant corrections ») — LISEZMOI v41

Lignée conv-audit (instance de reprise, Opus 5.5), écrit après le relevé `date -u` de **03:40 UTC** le 29 octobre 2026 ; v1 à v40
gardées (R12). Répond à la contre-lecture CL7 de la v40 (Opus 5.5, `contre-lecture-v40-cl7.md` : aucun bloquant de
lancement, CL40-01 à 03 majeurs, 04 à 09 mineurs, 10 défauts réintroduits survivants) dans le périmètre de la v41 courte
demandée par session-depot (message n° 146). **CL40-01 reste une décision de Lazar** : la politique n'est pas changée
(aucune marge ajoutée, contrôles réussis rejoués) ; seul le calcul de `relancable` l'est. **v41 n'est pas contre-lue**.

| constat | correction | essai qui le démontre (échoue sur la v40, passe sur la v41) |
|---|---|---|
| **CL40-02** contrôle interrompu scellé à 0 | `appel_de_controle` : toute exception pendant la session de contrôle compte son **plafond** (`cout_compte_usd`, `cout_inconnu`, statut « interrompue ») ; la lecture accumulée (modèles déjà contrôlés compris) est jointe à l'exception ; une interruption remonte telle quelle (le lanceur rend 2), une autre exception devient `ControleRefuse` ; seule `CleDansEnvironnement` (avant tout lancement) compte 0 ; le bras capte toute exception de son contrôle ; message du lanceur réécrit | `TestV41.test_controle_interrompu_compte_le_plafond_et_garde_les_lectures` ; `test_sigterm_pendant_le_controle_de_la_course` (SIGTERM réel : tentative à **2,5**, commande et petit-enfant morts) ; `test_sigterm_pendant_le_controle_du_bras` (bras-tentative à **0,2**) |
| **CL40-03** lanceur et cœur, contrôle du bras ; refus du cœur après contrôles | le lanceur passe `budget_controle_bras_usd` au cœur (même valeur que `verifier_reglages`) ; la capture des tentatives s'étend jusqu'au manifeste de départ du cœur : tout refus avant lui écrit `tentative-N.json` scellé avec les coûts, borné comme les autres ; **en plus** : le bras, lancé sans `--budget-controle-usd`, prend le contrôle que la course a compté (manifeste de départ) — rejouer S9 montrait qu'il reprenait 0,2 et refusait | `TestV41.test_s9_meme_controle_du_bras_et_refus_du_coeur_scelle` (S9 : course et bras passent, Argon 11,1 ; refus du cœur → tentative scellée, relance refusée avant tout contrôle) |
| **CL40-04** marge de la passe 2, consigne du juge | le contrôle d'Argon porte **sa consigne de passe 2 elle-même** au maximum (`consigne_proposeur` avec `nombre` × `fiche_maximale()` : chaque champ à son maximum permis, et matériau s'il est servi ; aussi sans matériau) ; **la passe 2 d'Argon est jouée juste après sa passe 1, avant toute passe Claude** (ordre des fiches écrites inchangé) ; le contrôle du bras envoie la consigne réelle du juge (pièces de juge et fiches comprises) | `TestV41.test_controle_a_la_taille_reelle_de_la_passe_2_et_ordre_d_argon` ; `test_controle_du_bras_porte_la_consigne_du_juge` |
| point 4 : `relancable` promis | `relancable` **calculé** dans `tentative-N.json` (moins de trois tentatives ; somme Claude et somme externe de la relance, coûts de la tentative imputés ; relais si lu) et dans `bras-tentative-N.json` / `manifeste-bras-non-joue-N.json` (tentatives ; plafond externe de la relance) ; motifs scellés et imprimés ; « bornée à trois » retiré du lanceur | `TestV41.test_relancable_calcule_avec_un_controle_claude_paye` ; `test_bras_tentative_relancable_calcule` |
| point 5 : une tolérance pour deux sommes | `--tolerer-somme-plafonds-claude` et `--tolerer-somme-plafonds-externe` (cœur : `tolerer_somme_claude`, `tolerer_somme_externe`) ; l'ancienne option vaut les deux, consignée au manifeste (`versions.tolerances`) | `TestV41.test_tolerances_separees` |
| point 6 : essai avec un contrôle Claude payé | moteur simulé au contrôle payé (0,01 puis 0,2 par modèle), réglages du devis v7 quinquies : la tentative porte 0,02 (0,4) et 0,15 ; `relancable` **faux** (somme de la relance 40,02 ; 40,40) ; aucune relance (Argon non rappelé) ; total relevé à 41 : deux relances, puis la borne | `TestV41.test_relancable_calcule_avec_un_controle_claude_paye` |
| **CL40-05** chemin de l'argent | `budget_controle_bras_usd` (réglages, cœur) et `budget_controle_usd` (bras) : réel fini ≥ 0, ni booléen ; `verifier_relais` : `depense_usd`, `plafond_usd`, `reserve_par_appel_usd` présents → finis, ≥ 0, non booléens ; `lire_tentatives_controle` : sceau vérifié (refus si absent ou faux), coûts finis ≥ 0, numérotation continue, aucun dossier `tentative-K` sans sa tentative scellée (fichier retiré, ou arrêt brutal au coût inconnu) ; **en plus** : les `bras-tentative-N.json` lus sceau vérifié | `TestV41.test_chemin_de_l_argent_valeurs_non_finies` |
| **CL40-06** juge apparié | `ebh_pondere` : α fini dans ]0 ; 1[ ; `trajectoire_log_richesse` : `_exiger_valeur` ; parts de `contraste` : `_exiger_fini` ; `_fini` seul prédicat (`verifier_coefficients`, garde) ; `ponderation_plafonnee` refuse un booléen | `test_v7_pari_apparie.TestV41` (4 essais) |
| **CL40-08** bras verrouillé sans classement | tout échec **après envoi** (interruption comprise) écrit `classement-sans-bras.json` à deux juges, marqué « sans juge externe, illisible » ; l'interruption remonte ; bras verrouillé | `TestV41.test_bras_interrompu_apres_envoi_ecrit_le_classement_sans_bras` |
| **CL40-07** M07 survivante | essai qui la tue : contrôle du bras où un processus est parti sans coût compté (exception à plafond nul ; « KO » gratuit) → tentative payée, jamais « non joué » | `TestV41.test_m07_controle_du_bras_a_cout_nul_processus_parti` (passe sur la v40, qui a la bonne condition ; **tue M07** réintroduite) |
| **CL40-09** écrits | « devis v7 bis / ter / quater » → « devis v7 quinquies » ; message d'interruption vrai pour les contrôles | `TestV41.test_ecrits_du_lanceur` |

**Défauts réintroduits (ma vérification, sur copie)** : 17, dont M07 et N03 de CL7 et un par correction (contrôle interrompu
compté 0, lectures perdues, marge d'une fiche, marge sans matériau, ordre d'Argon, contrôle du bras court, `relancable`
promis côté lanceur et côté bras, contrôle du bras repris à 0,2 par défaut, tolérances liées, sceau non vérifié, contrôle du bras non vérifié, classement sans bras
seulement pour `CourseInterrompue`, α d'e-BH) : **17 tuées** par les modules `test_v7_ideation` et `test_v7_pari_apparie`.

**Rejoué avec les outils de CL7** (`argon_factice.py`, `lanceur_pire.py`, sur l'arbre v41) : S1 (réglages du devis, tout au
plafond) : Claude 40,0, Argon course 7,5 puis bras 11,2, classement à trois juges ; S2 (Argon « KO », contrôle Claude 0,2 ou
0,01) : une seule tentative, `relancable` faux avec ses motifs, relances refusées sans rappeler Argon ; S5 (8 fiches d'Argon
aux champs de 3 000) : passe 2 réelle 328 829 caractères ≤ contrôle 389 751 ; Argon qui casse sous la taille du contrôle :
arrêt après 0,4 de contrôles Claude seulement ; S9 : course et bras passent, Argon 11,1.

## Restes déclarés

- **CL40-01** (décision de Lazar) : aux réglages du devis, toute relance après un contrôle payé est refusée ; la v41 le dit
  (`relancable` faux, motifs) au lieu de le promettre. Politique inchangée.
- **Plafond du contrôle du bras** : il envoie désormais la consigne réelle du juge (≈ 22 000 caractères en S1, jusqu'à
  ≈ 243 000 dans le S6 de CL7) sous le plafond de 0,2 du devis ; au barème réel d'Argon (inconnu), il peut dépasser ce plafond et être
  refusé (« budget_depasse »), tentative payée comptée. À trancher au devis (plafond séparé du contrôle du bras).
- **Marge de la passe 2** : les listes `questions_servies` et `anteriorite` n'ont pas de borne au gabarit (comptées à 9 et
  12 éléments) et l'échappement JSON n'est pas compté ; au-delà, la marge est dépassée — la passe 2 d'Argon, jouée
  juste après sa passe 1, fait alors tomber l'échec avant toute passe Claude (0,4 de contrôles Claude perdus, plus Argon).
- **CL40-08** : pas de sous-commande `--ecrire-classement-sans-bras` ; un bras verrouillé par la v40 (sans classement) ou
  un échec du classement de repli lui-même reste sans outil.
- Arrêt brutal (SIGKILL, coupure) pendant un contrôle : rien n'est scellé ; la relance est **refusée** (dossier de contrôle
  sans tentative), mot de Lazar requis — ni compté ni rejouable automatiquement.
- Non vérifié : vraie commande d'Argon, kit réel sous SIGTERM, relais réel (comme CL7, § 7).

**Essais** : un essai v40 corrigé sans changer ce qu'il démontre — `TestV40.test_interruption_arrete_le_groupe_et_compte`
simule `os.killpg`, et la commande lente qu'il lance survivait à la suite ; il l'arrête désormais lui-même (zéro processus
survivant après la suite, vérifié par `ps`).

**380 essais passent** (380 = 363 + 17 : `TestV41`, 13 dans `test_v7_ideation` et 4 dans `test_v7_pari_apparie`) ; trois
exécutions complètes, 169 s, 177 s et 178 s, aucun essai instable.

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v41.txt
```
