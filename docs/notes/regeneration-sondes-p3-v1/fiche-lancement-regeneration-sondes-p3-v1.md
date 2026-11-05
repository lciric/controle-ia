# Fiche de lancement — régénération du fichier complet des sondes figées de P3 — v1

Écrite par la lignée « session-depot » (instance 2), le 28 octobre 2026 vers 22:15 UTC. Complète le devis
`devis-regeneration-sondes-p3-v1.md` (`9c85bb5e…`, non réécrit, R12) ; GO-2026-10-28-11 et son extension « par
anticipation, en autonomie » (R-664). Le **critère d'acceptation du devis (§ 3) est repris tel quel** et appliqué par le
code (`scripts/regenerer_sondes_p3_v1.py`, fonction `verdict`), tolérance = `tolerance_identite` de la configuration de
P3 (1e-6).

## 1. Correction du devis
- § 2, « point non consigné par P3 » : **faux**. P3 a consigné `fils_entrainement_effectifs` = **30**, avec
  `coeurs` = {affinité 128, quota du groupe de contrôle 30,72} (`diag/20261019-230011-p3-reel/sondes-figees.json`,
  champ `resultat`). La chaîne borne donc le processus à 30 cœurs (`taskset -c 0-29`) sur une machine d'au moins 31 cœurs
  effectifs, de même processeur (AMD EPYC 7513) : `min(32, 30, quota ≥ 31)` = 30.

- **Fils de l'algèbre linéaire de numpy** (contre-lecture R2, CLR-01) : OpenBLAS (livrée avec numpy 2.4.6, compilée avec
  `MAX_THREADS=64`) prend autant de fils que l'affinité du processus, plafond 64, sans voir le quota. P3 tournait sans
  borne d'affinité (128) : **64 fils, inféré, non consigné par P3**. `np.linalg.inv` (Mahalanobis) et `cholesky`
  (planchers) changent au bit près selon ce nombre (mesuré par le contre-lecteur). Le script fixe donc OpenBLAS à **64**
  par appel explicite (`scipy_openblas_set_num_threads64_`), le relit (arrêt s'il diffère) et consigne la configuration ;
  `taskset` ne borne que torch. Si l'inférence est fausse, le palier 1 échoue et le palier 2 décide (devis § 3).
- **Fils de torch gardés avant calcul** (CLR-02) : le script exige `fils_effectifs(32)` = 30 (valeur de P3) avant tout
  calcul, sinon arrêt ; la chaîne prend les 30 premiers cœurs de l'affinité réelle du conteneur.
- **Graines confrontées** (CLR-09) : les graines des étapes 1 à 5 du manifeste régénéré doivent égaler celles du manifeste
  de P3 ; sinon `refuse`.

## 2. Méthode retenue
- L'instance clone le dépôt, **extrait le commit de P3** (`97dd82900cb120d5ce7328f8569d514fe987cc3c`, joignable par
  `calcul/p3-reel-v1`), lit le préenregistrement de P3 comme `p3_instance.sh` (tests attendus, configuration, tâches,
  consignes, sceaux), installe `requirements-gpu.txt`, passe la suite des tests au nombre attendu, puis lance
  `regenerer_sondes_p3_v1.py` **copié hors de l'arbre** : l'arbre reste propre et égal au commit cité (garde
  `exiger_code_cite`), et les graines sont celles de P3 (entropie citée par le préenregistrement).
- Le script appelle `controle_ia.premier_test_ia.run.executer` **sans changer une ligne** ; il enveloppe la fonction de
  progression et lève un arrêt volontaire juste après `etape=sondes-figees` : aucun épisode, aucun juge. Le lanceur de
  P3 consigne cet arrêt (`diag/<run>/arret.json`, étape « sondes figées », motif « arrêt volontaire … régénération »).
- Ce run réutilise le préenregistrement de P3 pour ses gardes ; il n'en est pas une nouvelle exécution : aucune lecture
  de P3 n'est refaite (devis § 6).

## 3. Versement
Branche `calcul/regeneration-sondes-p3-v1` : manifeste et résultats du run, fichier léger régénéré, sceau du fichier
complet, verdict scellé, traces (machine, tests, journal). Dès que le fichier complet existe et que son sceau est conforme,
**quel que soit le verdict** (CLR-04 : un refus doit rester examinable) : fichier complet (≈ 820 Mo : six
matrices de Mahalanobis 4 096 × 4 096 en double précision) en morceaux de 90 Mio, chacun scellé, liste scellée ; la
couche 2 le reconstitue par concaténation et vérifie le sceau.

## 4. Épreuves (R5), sans dépense
- `tests/test_regenerer_sondes_p3_v1.py`, mode jouet : cas sain (arrêt avant tout épisode, `accepte-identique`) ; niveau 2
  (`accepte-avec-declaration`) ; écart sous la tolérance accepté ; artefacts refusés : tableau écarté, aire écartée, sonde
  manquante, référence au sceau faux, référence ≠ sceau attendu, sortie existante, mode réel sans préenregistrement,
  lanceur qui ne passe pas par les sondes figées.
- Banc de la chaîne (dépôt distant local, `scratchpad/banc-regen/`) : A (vrai script, mode jouet, verdict `refuse`, poussée
  sans morceaux, code 0) ; B (bouchon accepté, fichier de 100 Mio versé en deux morceaux, reconstitué au sceau près) ;
  C1 branche existante (code 2) ; C2 référence au sceau faux (code 2) ; C3 plus de fils que de cœurs (code 1) ; C4 mode
  réel sans carte (arrêt avant les tests).

## 5. Bornes
Plafond 6 USD (une instance ; une seconde seulement si la première est perdue par l'hôte avant tout calcul). Amorce bornée
à 240 minutes, run à 150. Surveillance de la session ; arrêt par identifiant (R10) dès le versement lu ; réveils programmés
de la session à la création + 3 h et + 4 h (CLR-06 : une instance oubliée dépasserait le plafond vers 4 h). Contre-lecture
R2 : `contre-lecture-regeneration-sondes-p3-v1.md` (même dossier), « lançable après corrections » ; CLR-01 à 07, 09, 10
corrigés ; CLR-08 (comparaison au fichier léger, critère du devis), CLR-11 (poids), CLR-12 (banc du mode réel sur
processeur) notés.
