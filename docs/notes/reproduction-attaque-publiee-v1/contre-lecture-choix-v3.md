# Contre-lecture (R2) de « Choix de l'attaque publiée à reproduire et antériorité — v1, brouillon 3 »

- **Statut.** Contre-lecture, 10 novembre 2026. Sous-agent neuf (même lignée que la contre-lecture du brouillon 2, `contre-lecture-choix-v2.md`, `5ea95fa7`). Non scellée.
- **Note relue.** `docs/notes/reproduction-attaque-publiee-v1/choix-et-anteriorite-v1-brouillon3.md` (commit `d0c51e84`, lue sur disque, non modifiée, R12).
- **Mandat.** Vérifier que le brouillon 3 corrige **réellement** les deux majeurs (MA1, MA2) et les deux mineurs (MI1, MI2) de `contre-lecture-choix-v2.md`, et qu'aucune erreur neuve n'est introduite. Je recoupe chaque point sur source primaire.
- **Fichiers lus pour vérifier** (explicitement) : la note ci-dessus ; `contre-lecture-choix-v2.md` ; `choix-et-anteriorite-v1-brouillon2.md` ; **les PDF empreintés** `2609.36490v1.pdf` (candidat 2, `eb6d5bbe…`) et `bailey-2025-obfuscated-activations-2412.09565.pdf` (`9c23a613…`), extraits par `pdftotext` ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (l. 95, 113, 122) ; `docs/programme-controle-ia-v2.md` (l. 95, 249) ; `docs/sources/lecture-pdf-niveau2/rapport-lot3-Cc-evasion-quorum-v1.md` (l. 85) ; `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` (l. 11, 78, 99).
- **Portée.** Aucun contenu du coffre, aucune valeur de clé. Niveau infrastructure et antériorité.

## 0. Verdict

**Scellable en l'état.**

Les quatre points de la contre-lecture du brouillon 2 sont corrigés, vérifié point par point sur source primaire. Aucune erreur neuve n'est introduite : les deux libellés que le brouillon 3 ajoute (« boucle §3.5 » et « lemme L ») sont justes sur le PDF de Bailey et sur la nomenclature du programme. Les trois bloquants du brouillon 1 et les corrections du brouillon 2 déjà validées sont conservés sans régression.

Une seule observation **cosmétique, non bloquante** (ne change pas le verdict) : §3, cellule (b) du tableau l. 87, garde « déjà des coûts publiés (Bailey p. 26 ; candidat 2) » sans l'étiquette « OAT » ; la recommandation en prose juste en dessous (l. 90) nomme pourtant l'expérience et la distingue de la boucle. Pas une contradiction, pas un fait faux ; polissage facultatif.

## 1. État des quatre points de la contre-lecture du brouillon 2

### MA1 — Modèle du candidat 2 : **corrigé**

- **Attendu.** « llama-3.1-8b-instruct, exactement le modèle du banc », cohérent entre §0, §2, §7, citation PDF p. 4, « variante non pinée » retiré.
- **Vérifié dans le brouillon 3.** §0 l. 11 : « le candidat 2 … tourne sur **llama-3.1-8b-instruct**, soit **exactement le modèle du banc** ». §2 tableau l. 58 : « **llama-3.1-8b-instruct** (PDF p. 4 : « We primarily study llama-3.1-8b-instruct » ; confirmé p. 5, légende, et tableau p. 20) — **exactement le modèle du banc** ». §2 avantage 1 l. 67 : « Même modèle exact que le banc (llama-3.1-8b-instruct, PDF p. 4) ». §7 l. 131 : « **modèle 3.1-8B-Instruct, exactement le nôtre** ». Les trois sections concordent ; « variante non pinée » **absent** (grep : nul).
- **Confirmé sur source primaire.** PDF candidat 2 p. 4 : « We primarily study llama-3.1-8b-instruct » ; p. 5 (légende) ; p. 20 (tableau « llama-3.1-8b-instruct 24 32 100 »). Banc = Llama-3.1-8B-Instruct (`programme-controle-ia-v2.md` l. 249). **La citation est exacte.**

### MA2 — Chiffres p. 26 de Bailey rattachés à l'OAT : **corrigé**

- **Attendu.** Chiffres p. 26 partout rattachés à l'OAT (§6.2), distingués de la boucle itérée (§3.5) ; §5 point 5 ne présente aucun chiffre OAT comme prédiction de la boucle.
- **Vérifié dans le brouillon 3.** Toutes les mentions de « p. 26 » portent l'étiquette OAT/§6.2 et la distinction d'avec la boucle §3.5 : §1 l. 31 (Durée), §1 l. 50 (inconvénient 6), §3 l. 90 (recommandation), §4 l. 94 (intro) et §4 l. 98-99 (tableau R7). §4 « Conséquence » l. 106 et **§5 point 5 l. 114** disent que la prédiction chiffrée du test (a) porte sur **la boucle (§3.5), fourchette lue sur figure marquée comme telle**, *ou* bascule **déclarée** vers l'OAT (§6.2), et : « **Ne jamais présenter un chiffre OAT comme la prédiction chiffrée d'une reproduction de la boucle.** » Aucun chiffre OAT n'est présenté comme prédiction de la boucle.
- **Confirmé sur source primaire.** PDF Bailey : en-tête « **3.5 Adversarial Training Against Obfuscation Attacks** » (la boucle ; « even after over 70 epochs… ») ; « **6.2** Training models to be easier to m[onitor] », « using OAT (Algorithm 1) … (§6.2) », « ran the OAT experiments (§6.2) » ; les chiffres 16 384 pas / 35 %, 256 pas / 95 %, ≈ 10 h sont dans le bloc OAT (p. 26). Les chiffres de la boucle (oscillation, ≈ 85-90 %) sont de figure (figures 8a/8b, figure 20), non opposables (`verification-bailey…` l. 99). **La distinction §3.5 / §6.2 est exacte.**

### MI1 — « T — théorème négatif l. 122 » : **corrigé**

- **Attendu.** « T — théorème négatif l. 122 » (plus « L »).
- **Vérifié dans le brouillon 3.** §2 l. 63 : « HC5 l. 14, H7/H5 l. 20, **T — théorème négatif l. 122**, transposition jeton→action l. 138 … le candidat 2 **ne touche pas le lemme L** (`rapport-lot3` l. 85) ». « L l. 122 » **absent** (grep : nul).
- **Confirmé sur source primaire.** `niveau2-v1/anteriorite-v1.md` : la ligne 122 est sous l'en-tête « **## T — théorème négatif (N-003)** » (l. 113) ; « L » est une **autre section**, « ## L — **lemme d'additivité**, énoncé adverse (N-004) » (l. 95). `rapport-lot3` l. 85 liste L parmi « ne touche pas ». **L est bien un lemme** (programme l. 95 : « L — lemme d'additivité ») : le libellé « le lemme L » n'introduit pas d'erreur.

### MI2 — « ICLR 2026 » marqué non vérifié : **corrigé**

- **Attendu.** « ICLR 2026 » retiré ou marqué non vérifié.
- **Vérifié dans le brouillon 3.** §0 l. 9 et §1 tableau l. 21 : « venue ICLR 2026 **non vérifiée sur le PDF empreinté** (R7) », avec renvoi à `verification-bailey…` l. 11, 78. Aucune occurrence de « ICLR 2026 » présentée comme acquise (grep : les deux seules mentions portent la réserve).
- **Confirmé sur source primaire.** `verification-bailey…` l. 11, 78 : « aucune mention … d'ICLR dans le PDF », « venue ICLR 2026 non lue sur le PDF ».

## 2. Erreurs neuves ? Aucune

- **Libellés §3.5 / §6.2** : vérifiés sur le PDF de Bailey (en-têtes de section). Exacts.
- **« le lemme L »** : vérifié (programme l. 95, niveau2 l. 95, decision-N-003-N-004). Nom standard, exact.
- **Ajout §2 l. 61** : « Code public : Non confirmé (PDF p. 10 : « We intend to make our code … available » — intention, pas publication) ». Vérifié sur le PDF candidat 2, p. 10 (Reproducibility Statement). Exact.
- **Sections conservées du brouillon 2** (empreinte `eb6d5bbe…` du candidat 2, A100 80 Go attribuée au dépôt, N-053 point 5 / échelons 5-6, GO, devis 31/74/75, quatre préalables au scellement) : inchangées, déjà validées ; aucune régression.

## 3. Renvois vérifiés par moi-même sur source primaire (ce tour-ci)

**7 renvois vérifiés ou reconfirmés sur source primaire :**

1. Candidat 2 = llama-3.1-8b-instruct — PDF candidat 2 p. 4 (« We primarily study llama-3.1-8b-instruct »), p. 5, p. 20.
2. Boucle itérée = §3.5 — PDF Bailey, en-tête « 3.5 Adversarial Training Against Obfuscation Attacks » ; « even after over 70 epochs ».
3. OAT = §6.2 ; chiffres p. 26 (16 384/35 %, 256/95 %, ≈ 10 h) dans le bloc OAT — PDF Bailey, en-tête « 6.2 », « ran the OAT experiments (§6.2) », bloc p. 26.
4. Chiffres de la boucle lus sur figure, non opposables — `verification-bailey…` l. 99.
5. L = lemme d'additivité, section distincte (l. 95) ; T à l. 113/122 — `niveau2-v1/anteriorite-v1.md` ; `programme-controle-ia-v2.md` l. 95.
6. Candidat 2 « ne touche pas L » — `rapport-lot3` l. 85.
7. Code candidat 2 = intention, non confirmé — PDF candidat 2 p. 10.

**Non vérifiable dans cette session** (inchangé) : la licence du dépôt `LukeBailey181/obfuscated-activations` — déjà portée par la note en préalable au verrouillage du choix (§1 l. 26, §5.2).
