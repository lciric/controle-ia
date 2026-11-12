# Contre-lecture (R2) de « Choix de l'attaque publiée à reproduire et antériorité — v1, brouillon 2 »

- **Statut.** Contre-lecture, 10 novembre 2026. Sous-agent neuf, qui n'a écrit ni le brouillon 1, ni le brouillon 2, ni la contre-lecture du brouillon 1 (R2). Non scellée.
- **Note relue.** `docs/notes/reproduction-attaque-publiee-v1/choix-et-anteriorite-v1-brouillon2.md` (commit `54a731b2`, lue sur disque, non modifiée, R12).
- **Mandat.** Vérifier que les trois bloquants et les cinq majeurs de la contre-lecture du brouillon 1 sont corrigés **réellement** (pas seulement reformulés) et chercher tout défaut neuf. Je ne fais confiance à aucune affirmation de la note sans la recouper sur source primaire.
- **Fichiers lus pour vérifier** (explicitement) : la note ci-dessus ; `contre-lecture-choix-v1.md` ; `choix-et-anteriorite-v1-brouillon1.md` ; `docs/notes/anteriorite-P-041-v1/bailey-depot-public-parametres-v1.md` et son `erratum-bailey-depot-public-parametres-v1.md` ; `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` ; `docs/sources/lecture-pdf-niveau2/rapport-lot3-Cc-evasion-quorum-v1.md` ; `docs/programme-controle-ia-v2.md` (l. 249) ; la ligne GO-2026-10-31-05 de `registres/go.md` (l. 170) ; `docs/notes/anteriorite-P-041-v1/devis-P-041-gpu-et-collisionneur-protocelles-v1.md` ; `docs/decisions/decision-N-053-v1.md` ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` ; `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon1.md` (l. 56) ; **les PDF empreintés eux-mêmes** : `2609.36490v1.pdf` (candidat 2, `eb6d5bbe…`, extrait par `pdftotext`) et `bailey-2025-obfuscated-activations-2412.09565.pdf` (`9c23a613…`, extrait par `pdftotext`).
- **Portée.** Je n'ai lu aucun contenu du coffre (`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`) ni aucune valeur de clé. Niveau infrastructure et antériorité, comme la note relue.

## 0. Verdict

**Scellable après corrections ; aucun bloquant.**

Les **trois bloquants** du brouillon 1 sont corrigés **réellement**, et je l'ai vérifié sur les sources primaires, pas sur la parole de la note : le modèle n'est plus inversé (candidat 2 = version mineure 3.1, Bailey = 3.0, programme = 3.1-Instruct) ; le document empreinté du candidat 2 est reconnu (empreinte recalculée par moi, conforme) ; la carte A100 80 Go est traitée comme provenant du dépôt public, non opposable, non empreinte, avec renvoi à l'erratum. Les cinq majeurs du brouillon 1 sont eux aussi corrigés (R7 des deux candidats remis à l'endroit, « point de coût » et non « taxe », licence en réserve de choix, GO en tête du reste à faire, chiffres de figure marqués non opposables).

Pour l'équilibre (R4) : la correction n'est pas qu'une reformulation — les faits ont changé dans le bon sens et tiennent à la vérification. Mais une correction « trop propre » se vérifie deux fois : j'ai trouvé **deux majeurs** (une contradiction interne sur le modèle du candidat 2, qui en plus **sous-estime** la source primaire ; et un **mélange d'expériences** de Bailey pour la prédiction chiffrée) et **deux mineurs**. Aucun ne falsifie le choix (Bailey) ; les deux majeurs doivent être corrigés avant scellement parce qu'ils touchent l'axe du nœud soumis à Lazar et la future prédiction du préenregistrement.

Décompte : **0 bloquant, 2 majeurs, 2 mineurs.**

## 1. Points bloquants

Aucun. Voir en section 4 l'état détaillé des trois bloquants du brouillon 1 (tous corrigés).

## 2. Points majeurs

### MA1 — Contradiction interne sur le modèle du candidat 2, qui sous-estime la source primaire

- **Passages visés.** §2 tableau l. 58 : « llama-3.1-8b ([C89] p. 20, [C66] p. 23) … **la variante exacte (Instruct) n'est pas pinée dans les lignes citées** ». Contre §0 l. 13 : « ancrer sur **notre modèle exact** (candidat 2) » ; §7 l. 127 : « Candidat 2 : **modèle 3.1 (le nôtre)** », « le candidat 2 (**modèle exact du banc**) », « (b) Candidat 2 : **colle au modèle exact** ».
- **Fait vérifié sur source primaire.** Le PDF empreinté du candidat 2 (`2609.36490v1.pdf`, `eb6d5bbe…`) nomme le modèle en toutes lettres, **page 4** : « We primarily study **llama-3.1-8b-instruct** (Grattafiori et al., 2024) » ; confirmé en **page 5** (légende : « Numbers and figures are for llama-3.1-8b-instruct with mean-pooled logistic ») et en annexe (tableau p. 20 : « llama-3.1-8b-instruct 24 32 100 »). C'est donc **la variante Instruct**, soit **exactement le modèle du banc** (Llama-3.1-8B-Instruct, `programme-controle-ia-v2.md` l. 249, vérifié). La prudence de §2 (« variante non pinée ») est vraie pour les **deux lignes courtes** que le rapport lot3 a citées, mais le PDF, lui, la pine clairement : la note aurait dû aller à la source primaire, désormais sur disque et empreinte.
- **Pourquoi c'est majeur.** La note se contredit (§2 hésite, §0 et §7 affirment) sur le seul critère qui distingue le candidat 2, et c'est l'axe même du nœud soumis à Lazar (« ancrer sur l'effet le mieux outillé, Bailey, ou sur notre modèle exact, candidat 2 »). Le sens de l'erreur est **conservateur** (elle affaiblit un candidat écarté, elle ne gonfle pas le choix) — ce n'est donc pas un bloquant — mais une note qui fait foi ne peut pas être scellée avec une contradiction interne et une imprécision évitable sur une source empreinte.
- **Correction attendue.** En §2, citer le PDF p. 4 et écrire « llama-3.1-8b-**instruct** (PDF p. 4), soit exactement le modèle du banc » ; retirer le « non pinée ». Aligner §0 et §7 (déjà exacts) sur cette formulation. Garder, comme le fait §0 l. 11, que c'est Bailey (3.0) qui diffère du banc.

### MA2 — Les chiffres opposables de Bailey (p. 26) décrivent une autre expérience que le test (a)

- **Passages visés.** §3 l. 90 : « Bailey donne un couple de coûts p. 26 (16 384 pas / 35 % contre 256 pas / 95 %) … Préférer, pour le chiffre cité au jury, les chiffres de texte de Bailey (p. 26) » ; §4 l. 96–97 (mêmes chiffres cochés « Oui », opposables) ; §1 l. 31 (« ≈ 10 h sur une carte » pour 16 384 pas) ; **§5 point 5 l. 110 : « prédiction chiffrée (chiffres de texte de Bailey p. 26) »**.
- **Fait vérifié sur source primaire.** Dans le PDF empreinté de Bailey, ces chiffres viennent de l'expérience **OAT (Obfuscated Adversarial Training, durcissement du modèle, §6.2)** : « we introduce Obfuscated Adversarial Training (OAT) … we finetune the model (Llama-3-8B-Instruct) … an obfuscation attack with … (1% FPR) after **16,384 gradient steps** (about 10 hours on a single GPU). In comparison, against Llama-3-8B-Instruct **without OAT**, the same obfuscation attack achieves a **95% jailbreak rate** and zero recall after only **256 gradient steps** » (PDF, p. 26, bloc OAT). Or le test (a) reproduit **la boucle itérée sonde-contre-attaquant** (§0 l. 9 : « le protocole qui est la boucle adverse sonde-contre-attaquant » ; §1 l. 29 : « Recette de sonde réentraînée dans la boucle » ; `bailey-depot…` : `attack_defense_epochs: 100`, « over 70 epochs »), **dont les chiffres phares sont lus sur figure** (figures 8a/8b ; oscillation 100/0 %, évasion ≈ 85-90 %), **non opposables** — ce que §4 l. 98 marque correctement par ailleurs.
- **Pourquoi c'est majeur.** La note désigne les chiffres de **l'expérience OAT** comme référence de coût, comme chiffre d'entretien **et comme prédiction chiffrée du préenregistrement**, alors que le test (a) reproduit **une autre expérience** (la boucle, §3.5). R1 exige que la prédiction chiffrée porte sur l'expérience réellement conduite ; R7 exige de dire **de quelle expérience** vient chaque chiffre opposable. La note ne dit nulle part que p. 26 = OAT ≠ boucle : ce n'est pas un fait faux (les chiffres **sont** p. 26), mais une confusion d'expérience qui se propagerait au préenregistrement. (Note : la réserve du §1 l. 31 sur la durée est bien vue, mais ne nomme pas la provenance OAT.)
- **Correction attendue.** Distinguer explicitement les deux expériences de Bailey : (i) la boucle itérée (§3.5, figures 8a/8b, chiffres **de figure, non opposables**), que le test (a) reproduit ; (ii) l'OAT (§6.2, p. 26, chiffres **de texte, opposables** : 16 384 / 35 %, 256 / 95 %, ≈ 10 h). Puis dire laquelle le préenregistrement prédit : soit reproduire/prédire l'OAT, soit prédire la boucle avec une fourchette lue sur figure, marquée comme telle. Ne pas présenter les chiffres OAT comme la prédiction chiffrée d'une reproduction de la boucle.

## 3. Points mineurs

- **MI1 — Étiquette d'énoncé fausse : « L l. 122 ».** §2 l. 63 : « `niveau2-v1/anteriorite-v1.md` : HC5 l. 14, H7/H5 l. 20, **L l. 122**, transposition jeton→action l. 138 ». Vérifié : la **ligne 122** de ce fichier est sous l'en-tête « **## T — théorème négatif (N-003)** » (l. 113) ; c'est l'énoncé **T** (« voisin, pour le seul volet attaquant adaptatif »), **pas L**. De plus le candidat 2 **ne touche pas L** (`rapport-lot3` l. 85 : « HC1, HC3, H1, H3, H4′, **L**, statistique de population (papier B) | **ne touche pas** »). La revendication d'ensemble (antériorité établie au niveau 2) **tient** : le candidat 2 y figure sous HC5 (l. 14), H5/H7 (l. 20), T (l. 122), Tr/transposition (l. 138), plus HC2, HC2b, H6, H8, HC6 dans le rapport lot3 ; seule l'étiquette est fausse. *Correction* : remplacer « L l. 122 » par « T (théorème négatif) l. 122 » ; ne pas citer L. (Erreur héritée telle quelle de `contre-lecture-choix-v1.md` l. 30, non corrigée.)
- **MI2 — « ICLR 2026 » non vérifié sur le PDF empreinté.** §1 tableau l. 21 et §0 l. 9 donnent la référence « arXiv 2412.09565v2, **ICLR 2026** ». La note de vérification (`verification-bailey…` l. 11, 78) relève « aucune mention … d'ICLR dans le PDF » et « venue ICLR 2026 non lue sur le PDF ». Per R7, la venue est non opposable sur la source empreinte. *Correction* : marquer « ICLR 2026 » comme non vérifié sur le PDF (ou le retirer), ou le sourcer à part. (Mineur : c'est une venue, pas un chiffre ; présent aussi au brouillon 1.)

### Ce qui, vérifié, ne pose PAS de problème (R4, pour l'équilibre)

- **Code du candidat 2 « non confirmé » — exact.** PDF p. 10, Reproducibility Statement : « We **intend to** make our code, the generated concept data, and the trained model organisms available. » Intention, pas publication confirmée : « non confirmé » est juste.
- **Candidat 2 écarté pour « méthode à réglage fin des poids … bras d'attaque déclaré (N-053 point 5) » — exact.** `decision-N-053-v1.md` l. 42–44 : invariant « aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection de l'agent, **hors bras d'attaque déclaré** » ; la méthode du candidat 2 (LoRA de rang 1 dont la perte traverse les sondes, sortie imposée : `rapport-lot3` [C20], [C25], [C26], [C93]) met bien un score de sonde dans l'entraînement de l'agent. Les « échelons 5-6 de l'échelle d'accès » sont définis et cohérents (`regle-du-jeu-et-integration-v1-brouillon1.md` l. 56 : « Les échelons 5 et 6 mettent la note d'une sonde dans un signal d'entraînement. N-053 ne le permet qu'à un bras d'attaque déclaré »).
- **Choix justifié honnêtement.** §0 l. 9–11 ancre « sur le modèle de Bailey » et dit le transfert vers 3.1-8B-Instruct « étape séparée » ; aucun « même modèle que nous » n'est réintroduit dans les avantages de Bailey (§1 avantages l. 37–41, vérifié). Le GO (plafond 210 / test (a) 75 / expiration 14 nov / A100 80 Go / conditions, `registres/go.md` l. 170), le devis (31 / 74 / 75, carte 40 Go, `devis-…-v1.md` l. 15, 19, 23, 94) et les quatre préalables au scellement (GO renouvelé §5.1 ; licence §5.2 ; PDF de StrongREJECT §5.3 ; devis 40→80 §5.4) sont tous présents et exacts.

## 4. État des trois bloquants du brouillon 1

| Bloquant du brouillon 1 | État | Vérification |
|---|---|---|
| **B1 — modèle inversé entre les deux candidats** | **Corrigé** | Programme = Llama-3.1-8B-Instruct (l. 249, lu) ; Bailey = Llama-3-8B-Instruct / 3.0 (`verification-bailey` l. 26 ; PDF Bailey « finetune the model (Llama-3-8B-Instruct) ») ; candidat 2 = 3.1, en fait **llama-3.1-8b-instruct** (PDF p. 4). « Modèle identique au nôtre » retiré des avantages de Bailey ; ancrage honnête sur le modèle de Bailey, transfert vers 3.1 en étape séparée. *Résidu* : contradiction §2 vs §0/§7 → **MA1** (affinage, pas réapparition de l'inversion). |
| **B2 — document du candidat 2 déclaré absent** | **Corrigé** | PDF présent en deux copies, empreinte `eb6d5bbe…` **recalculée par moi**, conforme aux compagnons ; reconnu « lu en entier » (§2 l. 57). Écartement **refondé** sur des motifs exacts et vérifiés (code non confirmé ; coût non chiffré ; réglage fin des poids / échelons 5-6 → bras déclaré, N-053). R11 respectée ; les deux motifs faux (document absent, chiffre non opposable) explicitement retirés (§2 l. 78). |
| **B3 — « A100 80 Go » attribué à la p. 26 et coché « vérifié »** | **Corrigé** | Carte attribuée au **dépôt public** (README l. 96, `evaluate_defenses.sh` l. 7), marquée **non opposable seule, non empreinte**, erratum cité, « le papier ne nomme aucune carte » (§1 l. 30 ; §4 l. 99). Conforme à `erratum-bailey-depot-public-parametres-v1.md`. |

## 5. Renvois vérifiés par moi-même sur source primaire

**16 renvois vérifiés sur la source primaire ou le fichier cité :**

1. Modèle du programme = Llama-3.1-8B-Instruct — `programme-controle-ia-v2.md` l. 249.
2. Candidat 2 présent en deux copies, empreinte `eb6d5bbe9bfaff0ac4fbac948a7bd9937721721fc558655fdf606d254421a088` recalculée, conforme aux compagnons — `2609.36490v1.pdf` et `anteriorite-P-041-v2/c3/evade-from-feedback-…`.
3. Modèle du candidat 2 = **llama-3.1-8b-instruct** (variante Instruct, = banc) — PDF candidat 2 p. 4, p. 5 (légende), p. 20 (tableau).
4. Code du candidat 2 = intention, non confirmé — PDF candidat 2 p. 10 (« We intend to make our code … available »).
5. Candidat 2 : coût non chiffré ; méthode = LoRA rang 1, sortie imposée — `rapport-lot3` [C15]/[C56]-[C59], [C20], [C25], [C26], [C93].
6. Bailey = Llama-3-8B-Instruct (3.0) — `verification-bailey` l. 26 ; PDF Bailey (bloc OAT, « finetune the model (Llama-3-8B-Instruct) »).
7. Chiffres p. 26 de Bailey (16 384/35 %, 256/95 %, ≈ 10 h) = expérience **OAT (§6.2)**, distincte de la boucle §3.5 — PDF Bailey, bloc OAT p. 26.
8. Boucle §3.5 : chiffres phares lus sur figure, non opposables — `verification-bailey` l. 99.
9. A100 80 Go : non nommée par le papier, source = dépôt — `erratum-bailey-depot-public-parametres-v1.md`.
10. GO-2026-10-31-05 : plafond 210, test (a) 75, expiration 14 nov, A100 80 Go, conditions — `registres/go.md` l. 170.
11. Devis test (a) : 31 attendu / 74 pire cas / plafond 75 ; carte A100 40 Go — `devis-…-v1.md` l. 15, 19, 23, 94.
12. N-053 point 5 contient « hors bras d'attaque déclaré » — `decision-N-053-v1.md` l. 42–44.
13. Échelons 5-6 de l'échelle d'accès définis et liés à N-053 — `regle-du-jeu-et-integration-v1-brouillon1.md` l. 56.
14. Niveau 2 : l. 122 est sous l'en-tête « T — théorème négatif » (l. 113), pas L ; candidat 2 « ne touche pas L » — `niveau2-v1/anteriorite-v1.md` l. 113, 122 ; `rapport-lot3` l. 85.
15. Niveau 2 : candidat 2 sous HC5 (l. 14), H5/H7 (l. 20), transposition jeton→action (l. 138) — `niveau2-v1/anteriorite-v1.md`.
16. Candidat 2 : 96 % = 1 − 0,040, chiffres de texte [C32] p. 6 / [C10] p. 1 — `rapport-lot3` l. 47, 60, 94.

**Non vérifiable dans cette session :** la licence du dépôt `LukeBailey181/obfuscated-activations` (dépôt non présent, accès non disponible ici) — déjà porté par la note en préalable au verrouillage du choix (§1 l. 26, §5.2).
