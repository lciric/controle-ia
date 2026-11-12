# Contre-lecture neuve du lanceur T0.6 v2 et du brouillon 5 de T0.6 (R2, lignée Opus 5.5) — v2

**Verdict : lançable après corrections.**
Les deux bloquants de la première contre-lecture sont fermés (états de sonde hors de toute sortie relayée ou poussée ; morceaux de moins de 90 Mo). C01 à C16 sont portées. 143 essais et banc 41/41 rejoués, E1 rejouée.
Restent avant le 11 novembre trois corrections de code (C-V3-1 à C-V3-3) et sept couples de texte. Deux nœuds de Lazar sont à trancher (Mahalanobis, et L04, L05, L11). E2 et E3 doivent passer avant le lancement (liste au point 9).

- Contre-lecteur neuf (fille 9, session de contre-lectures, lignée Claude Opus 5.5), 5 novembre 2026, de 21:00 à 21:14 UTC (`date -u`), sur la consigne `docs/notes/g0-deux-semaines-v1/consigne-contre-lecture-lanceur-T0.6-v2-v1.md` (`adaef7bcec55bf69…`, compagnon vérifié, `main` `07218b36`). Je n'ai écrit ni le lanceur v1 ou v2, ni les brouillons 4 et 5, ni la première contre-lecture.
- Pièces, empreintes recalculées et égales :
  - première contre-lecture `5e359565…` ; brouillon 5 `e95d4d48…` ; brouillon 4 `8df90b8b…` ; devis `6da6decf…` ;
  - branche `prep/t06-lanceur-v2` à `0d48103b`, rapport v2 `48f3a74a1635fb68…` ;
  - registre des GO de `main`, ligne 216 : GO-2026-11-02-28, 200 USD, échéance 2026-11-16.
- Ce que je n'ai pas fait : aucune location, aucun modèle, aucune clé, rien sous `donnees/` ni `diag/`, aucun `.sha256`, rien d'existant modifié.
- Essais : `--basetemp` dans le bloc-notes, puis supprimé (44 Mo) ; `TMPDIR` du banc dans le bloc-notes, supprimé.

## Points (une ligne chacun ; gravité)

1. **Bloquant 1 — fermé (note).**
   - Côté lanceur : `lanceur_v2` n'écrit dans `PROGRES` que des étapes, des comptes et des durées. `resume_imprimable` retire `ligne_A`, `ligne_B` et `ligne_C` de `run.json`. Les jeux passent par `jeu_ou_echec`, dont le message d'échec reste dans le résultat scellé et n'apparaît jamais sur la sortie d'erreur.
   - Côté amorce : elle ne relaie que les lignes `PROGRES` bien formées et sans mot interdit.
   - Rejeu d'E1 (code 0) : j'ai cherché les noms des familles, `sens1`/`sens2`, « aire », « AUC », `ligne_`, `table_`, « plancher », « au-dessus », « interpr » et « échec ». Dans le journal, `run.err`, `run.json` et les 8 fichiers de traces poussés, les seules occurrences sont `couple=<famille>-c<k>` et le « aire » de « lineaire ».
   - Réserves : `run.err` est copié tel quel dans les traces, si bien que la défense repose sur le code seul. Et `duree_s` par couple trahit faiblement un « échec » (un jeu en échec finit plus vite) : note.
2. **Bloquant 2 — fermé, mais une correction de code est nécessaire (à corriger, C-V3-1 ci-dessous).**
   - En place : morceaux de moins de 90 Mo avec manifeste scellé ; `refuser_gros` avant chaque commit ; données légères dans un commit à part, poussé avant les morceaux ; artefact éprouvé (fichier de 90 000 001 octets retiré).
   - **Défaut** : le remplissage compte les octets des tableaux, puis le lanceur lève `GardeArret` si le fichier `.npz` dépasse 90 Mo. L'enveloppe du format pèse **≈ 17 ko par morceau** (mesure : 49 actions de 222 × 4 096 en demi-précision, 16 636 octets).
   - Un morceau rempli à moins de 17 ko de la borne arrête donc toute la course, **après les épisodes et avant la lecture du coût**. La probabilité est d'environ 0,5 à 1,7 % par morceau plein, soit ≈ 5 à 15 % pour ≈ 12 morceaux.
3. **C01 à C16 — portées comme écrites (note), sauf C13 et C12 (à corriger).**
   - Correctes, chacune avec un cas sain et un artefact au banc ou aux essais : C03 (demi-précision et garde de disque avant les épisodes) ; C04 (clés exactes, nuls exigés) ; C05 (128 × 10⁹ octets et 128 000 Mo d'offre) ; C06 ; C07 ; C08 (cumul antérieur + forfait + instance, heure d'épuisement à l'amorce) ; C09 ; C10 ; C11 ; C14 ; C15 (prix maximal par carte, H200 en configuration) ; C16.
   - **C13 incomplète (C-V3-2)** : l'amorce teste « démarrage après l'heure de dépense épuisée → `detruire` » *avant* la branche du second démarrage. Un redémarrage après une dépense épuisée détruit donc l'instance sans pousser. La branche « `t06-depense-epuisee` → consigner » n'est jamais atteinte, et l'essai qui croit l'éprouver pose cette heure dans 10⁶ s.
   - **C12 (C-V3-3)** : `vastai search offers` est appelé sans `--storage`. `storage_total_cost` et `dph_total` sont donc lus au disque par défaut, pas aux 150 Go demandés, et la borne de 0,03 USD/h sur le stockage n'est pas éprouvée. L'heure d'épuisement est sous-estimée d'environ 0,03 USD/h.
4. **L04, L05, L10, L11 en configuration — conformes (note).**
   - `distillation.pas_declares` 480 est vérifié avant le manifeste. `lecture.non_interpretable_si_au_dessus_seulement` est vrai. `carte.relance` H200 NVL est à 4,70 USD/h.
   - Calendrier : dernier jour 2026-11-15 ; fin du GO 2026-11-17T00:00:00Z, recalculée contre `registres/go.md` (échéance 2026-11-16, ligne 216).
   - DT-6 (A100 SXM4 à 1,30, relance H200) et doses : texte, configuration et code concordent. DT-1 à DT-5 n'ont pas d'effet de code au-delà de la configuration.
   - L04, L05 et L11 restent des choix de fond : `<<MOT_LAZAR_DT>>`.
5. **Essais et banc — conformes (note).**
   - **143 passed** en 156,95 s (21:01 → 21:04 UTC). Banc v2 : **41 mutations, 41 tuées**, 4 témoins verts (21:06 → 21:12 UTC).
   - Les deux échecs « disque de l'hôte » de la v1 sont levés : `controles` est éprouvé avec un `df` factice.
6. **E0 et E1 (note).**
   - E0 au 1/64 et au 1/256 : durées et pics de mémoire probants pour l'ordre de grandeur (pentes linéaires en jetons), pas pour la taille réelle. Ce n'est pas une épreuve de la tendance statistique : la première contre-lecture l'avait contrôlée par simulation.
   - E1 rejouée : vrai lanceur sous la vraie amorce, dépôt nu, trois commits (résultats et données légères, morceaux, traces), `t06-fin-normale`.
   - Restent pour E2 et E3 : l'interface de Vast et la carte (point 9).
7. **Texte contre code (à corriger ; couples 1 à 6).**
   - Le plan daté du brouillon 5 écrit `surveillance <ID> <CREATION_S> <DOSSIER>`, ce qui est faux : la signature est `surveillance ID DOSSIER [FACTURE_USD]`. Il omet aussi `[JOUR]`, `[ECHEANCE_UTC_S]`, les valeurs de CARTE et `apres-creation`.
   - **La ligne 661 décrit les citations dans la forme exacte que la chaîne compte.** Au candidat, « Tests attendus : `N` » (et les quatre « Chemin … : `…` ») compteraient deux fois. Sur l'instance, `lire_unique` de l'amorce refuserait alors après l'installation, et `controles` refuserait les chemins.
   - « Tests attendus » n'a aucun marqueur ni procédure. L'amorce n'admet que « N passed » éventuellement suivi d'avertissements : un essai sauté sous l'image de l'instance arrêterait la course. Le nombre doit venir de la suite complète rejouée sous l'image (E3).
   - Procédure des empreintes du code (`<<EMPREINTES_CODE_T06>>`), forme de la citation de l'amorce (L13) : couple 6.
8. **Coût de Mahalanobis (nœud de Lazar ; évalué, non tranché).**
   - Mesure rejouée (bloc-notes, données synthétiques, 4 cœurs) : `SondeMahalanobis.scores_par_jeton` du paquet gelé coûte **21,2 ms/jeton à 1 000 jetons et 18,4 ms/jeton à 4 000**. La pente du rédacteur (26 ms sur une machine chargée) est confirmée, et l'extrapolation linéaire (≈ 7 à 9 h par couche à 1,28 million de jetons) tient.
   - **Cause** : `np.einsum("nd,de,ne->n")` sans `optimize`, qui contourne les produits matriciels. La même quantité calculée par `((z @ P) * z).sum(1)` coûte 0,18 à 0,23 ms/jeton (**80 à 120 fois** moins), avec un écart relatif de 5–6·10⁻¹⁵.
   - Le texte classe Mahalanobis parmi les quatorze couples **descriptifs** (point 6) : aucune décision n'en dépend. Les options :
     - (a) la retirer de la course : simple et sans surcoût, mais trois lignes descriptives perdues ; c'est un changement du texte.
     - (b) la lire hors ligne après coup : seul le sous-ensemble de 10 % de la couche 15 est poussé, donc pas les couches 7 et 23, ni les mêmes jetons. Ce n'est plus la même lecture, à moins de garder le disque et de payer la relecture.
     - (c) sous-échantillonner les jetons : cela change l'estimateur (le maximum par action exige tous les jetons) ; à écarter.
     - (d) option neuve : une version neuve du calcul (R12), même formule par produit matriciel, éprouvée égale à 10⁻¹² près contre le paquet gelé sur un échantillon. Elle garde la lecture et coûte ≈ 5 à 15 min par couche, mais touche l'usage d'un paquet gelé de T0.7 (nœud).
   - Je ne tranche pas.
9. **Interface de Vast et gardes de l'instance : ce qu'E2 (≤ 1 USD) et E3 (≤ 3 USD) doivent prouver avant le 11 novembre (GO à part).**
   - **E2, interface de Vast** :
     - lire une offre brute A100 SXM4 et une offre H200 et vérifier les clés réellement servies : `gpu_name` exact ; `gpu_ram` et `cpu_ram` en Mo ; `cpu_cores_effective` ; `disk_space` en Go ; `dph_total`, `storage_total_cost` et `inet_down_cost` **avec `--storage 150`** ; `rentable` ;
     - `vastai show instances --raw` filtré par étiquette ;
     - création sous l'amorce en `MODE=jouet` sur le dépôt réel : clone partiel avec le jeton, blobs paresseux lus, poussée initiale et finale sur une branche d'essai ;
     - PUT « stopped » par `CONTAINER_API_KEY`, corps `"success": true` ;
     - redémarrage réel dans les trois cas de C13, dont un redémarrage après l'heure de dépense épuisée (C-V3-2) ;
     - DELETE de la minuterie ; facture relue ;
     - `MemTotal` de l'instance contre 128 × 10⁹.
   - **E3, carte** :
     - `python3.11 -m venv` et `requirements-gpu.txt` sur l'image `python:3.11-bookworm` ;
     - **suite complète rejouée sous l'image, dernière ligne relevée** (nombre exact, aucun essai sauté) pour « Tests attendus » ;
     - mémoire et secondes par pas de la distillation sur ≈ 4 400 jetons ; `use_deterministic_algorithms` en rétropropagation ;
     - identité à dose 0 sur le vrai modèle ; un lot à dose 1 avec la garde au 99e centile ;
     - débit d'écriture des activations ; durée d'un couple descriptif sur 16 cœurs.
   - **Aucun bloquant qui ne puisse attendre E2 et E3**, à condition que C-V3-1 et C-V3-2 soient corrigées avant E2 et que les sept couples soient portés au candidat.
10. **Ce qui peut encore faire perdre la course ou l'argent.**
    - (i) C-V3-1 (morceaux) : perte de la course après les épisodes, ≈ 5 à 15 % de risque.
    - (ii) C-V3-2 : destruction sans poussée au redémarrage après une dépense épuisée.
    - (iii) Citation « Tests attendus » doublée par la ligne 661, ou nombre faux à cause d'un essai sauté : refus sur l'instance, après l'installation.
    - (iv) Durée de Mahalanobis : 8 à 30 h de carte, sous le plafond (A100, ≈ 1,3 USD/h) mais hors devis.
    - (v) Stockage lu à 5 Go et non à 150 Go : cumul légèrement sous-estimé.
    - (vi) Dépense antérieure donnée à la main à la relance H200 : seule valeur manuelle, à relire au registre.
    - (vii) Le résultat scellé des sondes est poussé fermé mais lisible par tout lecteur du dépôt privé : conception du texte, déclarée.
    - La minuterie (échéance et dépense), la destruction par l'identifiant, la poussée en trois essais et le refus d'une branche existante sont conformes et éprouvés en local.

## Fichiers du rendu

- `couples-brouillon5-vers-candidat1-T0.6-v1.json` : 7 couples, chaque « ancien » unique dans le brouillon 5 (`e95d4d48…`), appliqués dans l'ordre et vérifiés par script. Après application, aucune clé lue par la chaîne n'est suivie d'un accent grave hors des vraies citations (assertion du script).
- `corrections-code-lanceur-T0.6-v3.md` : C-V3-1 à C-V3-4 (versions neuves, R12).
- `outils/mesure_mahalanobis_v1.py` et ses deux sorties : mesure rejouée du point 8.
