# Orchestrateur du pôle, version 0.7.0 — v40 : réponse à la relecture CL6 de la v39 (« pas lançable en l'état ») — LISEZMOI v40

Lignée conv-audit (instance de reprise, Fable 5.1), écrit après le relevé `date -u` de **02:11 UTC** le 29 octobre 2026 ;
v1 à v39 gardées (R12). Répond à la relecture ciblée v37 → v39 de session-depot (`docs/notes/ideation-organisme-v1/
contre-lecture-v39-cl6.md` sur `main`, `4e701178…`, message n° 139 : CL39-01 bloquant de lancement, 02 à 04 majeurs, 05 à 12
mineurs, 21 défauts réintroduits survivants). Décision de Lazar (chez session-depot, ≈ 01:48 UTC) : **Argon 11,6**, total
idéation 51,6. **v40 n'est pas contre-lue** : relecture ciblée v39 → v40 annoncée chez session-depot (R2).

| constat | correction |
|---|---|
| **CL39-01** somme d'Argon fausse (contrôle à taille réelle 2,5, contrôle du bras omis) | la somme externe compte le contrôle à taille réelle **et** le contrôle du bras (`budget_controle_bras_usd`), dans `verifier_reglages` et au cœur ; défauts du lanceur : **Claude 40, Argon 11,6** (mot de Lazar) ; tout réglable |
| **CL39-02** contrôle refusé non consigné, relances illimitées | toute exception après le premier contrôle écrit `SORTIE-controle/tentative-N.json` scellé (lectures, coûts Claude et externe, plafond si coût inconnu) ; au lancement, les tentatives sont lues, leurs coûts imputés aux totaux, **au plus trois** ; essai (trois tentatives à 0,15 puis refus) |
| **CL39-03** garde du relais sans la dépense faite | `verifier_relais` : plafond − réserve − **dépense** ≥ total − plus petit juge ; état consigné au manifeste ; essai (réserve 10 refusée, relance après 0,4 refusée) |
| **CL39-04** bras interrompu après envoi scellé « rien envoyé » et rejouable | `consigne_envoyee` marqué avant `lancer` ; tout échec ensuite compte le **plafond** de la session, écrit le manifeste du bras et **verrouille** ; essai |
| CL39-05 SIGTERM | gestionnaires SIGTERM et SIGHUP → `KeyboardInterrupt` dans le lanceur ; une session interrompue (course ou bras) est comptée au plafond, statut `interrompue`, manifeste de fin écrit ; essai en sous-processus réel (SIGTERM pendant la session d'Argon : code 2, manifeste, petit-enfant mort) |
| CL39-06 contrôle à la passe 1 seulement | le contrôle d'Argon reçoit la **plus grosse consigne** qu'il recevra : pièces + matériau s'il est attesté + marge pour ses fiches (`texte_controle_externe`) ; taille de chaque consigne au journal |
| CL39-07 refus après les contrôles | SORTIE existante, `max_tours` > 2 : refusés avant tout contrôle (`verifier_reglages(max_tours=…)`) ; essai |
| CL39-08 régression du simulé | consigne de contrôle reconnue par préfixe ; essai (répétition simulée avec proposeur externe sans commande : code 0) |
| **CL39-09** valeurs non finies ailleurs dans le juge | `pari_apparie` : `_fini`, `_exiger_fini`, `_exiger_valeur` ; refus nommé (`ContrasteInvalide`) sur la constante et les coefficients (`verifier_coefficients`, `contraste`, `contraste_plafonne`), `log_e` (`ebh_pondere`), trajectoires (`Course.ajouter_trajectoire`), valeurs (`sans_remise`, `borne_basse`, borne [−1 ; 1]), α et m (`evaluer`, `borne_basse`) ; cas sains et artefacts (`TestValeursNonFiniesV40`) ; statistique inchangée sur entrées finies |
| CL39-10 garde PACE sans cas sain | régime **« honnête avec garde »** dans `simuler_suite`, la démonstration et l'essai ; la **puissance de la garde est rapportée** à côté du refus du tricheur ; essais M34 (gain non fini), M35 (e-BH contre seuil par candidat), M36 (δ vérifié) |
| CL39-11 écrits, code mort | définition morte de `executer_ideation` supprimée ; docstrings (agrégation, ordre des passes, versions, défauts, « relance permise ») réécrits |
| CL39-12 essais | le kit est déchargé après l'essai de la ligne de commande (ordre `test_v7_ideation` → `test_adaptateurs` sain) ; sceau faux : motif vérifié ; essai du délai borné (< 10 s) |
| 21 réintroductions survivantes | un essai chacune : M07, M09, M12 à M19, M20, M21, M22, M26, M28 à M31, M34 à M36 (`TestV40`, `TestLanceurV37`, `TestCommandeExterne`, essais de PACE) |

**Ce que la v40 rapporte, sans l'avoir cherché (R4)** : dans le monde synthétique de la porte PACE, **notre garde δ = 0,05 n'a
presque aucune puissance** aux tailles du pilote — un témoin honnête n'est validé que dans ≈ 1 % des suites à 120 unités,
7 % à 400, ≈ 42 % à 1 000 : la marge δ − E[g] = 0,05 est petite devant l'écart-type de l'écart (0,45 par unité, bruit ±1), et
même sans bruit le facteur par unité ne dépasse pas 1,045, donc m/α = 400 n'est pas atteignable avant ≈ 166 unités.
**Ce n'est pas une mesure de la garde de production** (ses écarts sont des fractions de scores, moins bruités, et δ = 0,10
dans les décisions D-S), mais c'est une alerte pour le préenregistrement de G1 : simuler la puissance de la garde avec le
bruit réel des écarts avant de la sceller. Détail dans la docstring de `pole/porte_pace.py`.

**363 essais passent** (363 = 340 + 23). Relecture ciblée v39 → v40 chez session-depot avant tout lancement.

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v40.txt
```
