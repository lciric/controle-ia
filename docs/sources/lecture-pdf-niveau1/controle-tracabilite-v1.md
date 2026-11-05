# Contrôle de traçabilité du rapport consolidé (état de l'art vérifié niveau 1 et décisions v2), avant corrections — v1

Rapport d'un sous-agent lecteur neuf (il n'a rien écrit de ce qu'il vérifie), rendu le 2026-10-04 (UTC).
PDF lus : les 13 PDF de niveau 1 et les six rapports de lecture.
Texte extrait **mot pour mot** du journal du sous-agent par `extraire_rapport.py`, sans aucune modification.
Les chiffres marqués « calcul » ou « mon calcul » sont des reconstructions du lecteur, pas des chiffres des auteurs.

---

# Contrôle de traçabilité : état de l'art vérifié niveau 1 v1 et décisions v2

## 0. Méthode

- **Empreintes.** Les 13 PDF correspondent à leur fichier compagnon et à `provenance-niveau1-v1.md`, nombres de pages compris. Les 7 rapports, les 5 archives de travail et les 5 fichiers de `TRACE-AcMAS/` sont aussi conformes. Ces 5 derniers sont identiques aux empreintes données dans le rapport brut.
- **Contrôle sur PDF.** J'ai cherché chaque chiffre des sections 2 et 4 dans le PDF, à la page citée (`pdftotext -layout`). J'ai relu en image les figures qui portent des chiffres : Za fig. 2 à 5, Terekhov fig. 3 et 5, Gao fig. 6b, Botas fig. 1.
- **Recalculs indépendants.**
  - TRACE, à partir des tableaux 1 et 5.
  - Moyennes ajustées de Za, à partir des étiquettes des fig. 2 à 4.
  - Plages TRANSFER de NARCBench (tableaux 2 à 5).
  - Comptes 23/…/7 de Hwang (tableau 2).
  - La fuite de Monitor A : je l'ai réimplémentée en Python pur, car numpy et scipy sont absents.
  - Les faits « de code » de 2606.10456 : relus dans le dépôt local, au commit b35f238 consigné dans `ressources-code-v1.md`.
- **Fichiers de travail.** Ils sont dans `/tmp/claude-0/-home-user-cplt-run-2026-09-03/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/controle-tracabilite/` : `mon_calcul_trace.py`, `fuite_pur_python.py`, `fuite_pur_python.out`, `fuite_pur_python_40k.out`, ainsi que les dossiers `pages/` et `img/`.
- **Aucune modification.** Je n'ai rien modifié dans `controle-ia`, `brouillon-edav` ni `ressources`. Trois fichiers de `controle-ia/registres/` apparaissent modifiés dans git. Ils l'ont été à 04:41:22 UTC, avant mon intervention, et je n'y ai pas touché.

## 1. Table de contrôle

### 1a. Section 4, table des chiffres vérifiés (20 lignes)

| Emplacement | Ce qui est écrit | Rapport / PDF (page) | Verdict | Correction proposée |
|---|---|---|---|---|
| §4 l.1 | 24,4 % → 33,9 % (+ 9,5 points), p. 5 | p. 5 : « 24.4% … 33.9% … by 9.5% ». Recalcul sur les fig. 2 à 4 : 24,44 et 33,88, moyennes non pondérées de 9 cellules | conforme | — |
| §4 l.2 | 95,5/97,5/98,8 ; 7,5/5,0/1,3, p. 4 | Tableau 1, p. 4 : identique | conforme | — |
| §4 l.3 | 40 tâches, 4 domaines, p. 3–4 | p. 3 : 40 tâches et 4 domaines énumérés. « 4 » est écrit en toutes lettres p. 2 et 10 | conforme | — |
| §4 l.4 | « ≈ 35 points », baisse avec un vérificateur d'une autre famille, p. 6 | Le texte p. 6 dit « approximately 35% », sans unité. Les points viennent de la fig. 5, p. 8 : je lis ≈ 0,405 → ≈ 0,058. Testé seulement avec l'agent GPT-4.1 et avec CoT. Pour le moniteur Claude, le vérificateur « autre famille » est GPT-4.1, c'est-à-dire le modèle de l'agent (rapport C) | à nuancer | Écrire « ≈ 35 points, lecture de la fig. 5 (le texte dit "35%") ; agent GPT-4.1, avec CoT, moyenne des 3 moniteurs ; pour Claude, vérificateur = agent ». Pages 6 et 8 |
| §4 l.5 | 14 juges ; 7 techniques ; échelle 0–5 | p. 4, 5, 12, 19 | conforme | — |
| §4 l.6 | 23/22/20/18/16/11/7 sur 24, p. 5 | Exact : recompté sur le tableau 2, p. 6. Les 24 cas valent **4 juges** (Qwen 2.5 14B et 72B, GPT-3.5, GPT-4o) × 6 bancs. Un « succès » est toute hausse, sans seuil de bruit | conforme | Ajouter « 4 juges × 6 bancs ; toute hausse compte » (la ligne précédente, « 14 juges », peut induire en erreur) |
| §4 l.7 | 18 modèles ; 349 propositions ; 11 172 invites | p. 1, 2, 5, 24 | conforme | — |
| §4 l.8 | 137,9/138, τ = 0,97 | p. 32 ; tableau 4, p. 33 ; aussi p. 10 | conforme | Option : 138 paires significatives sur 153 ; l'ordre exact ne revient que dans 6 % des tirages (p. 32) |
| §4 l.9 | AUROC 1,00 (CORE, meilleure méthode) ; TRANSFER 0,73–0,93 (Llama) | p. 15 ; tableau 3, p. 25 : exact. Mais CORE ne compte que 36 épisodes collusifs et 50 témoins, en validation par domaine exclu sur 17 domaines (p. 12, 32), soit ≈ 5 épisodes par pli. Le rapport B (alerte 3) dit que ce ne sont « pas des bases à battre » | à nuancer (R4) | Ajouter la réserve d'effectif |
| §4 l.10 | Rappel 0,38 à 1 % de FP (TRANSFER) ; 1,00 (STEGO) | p. 15. Le 0,38 est celui de Deception Split, le 1,00 celui d'Activation Alignment. La fig. 4 donne les ROC de Llama-3.1-70B | conforme | Préciser la méthode et le modèle. Le rapport B demande que le programme le recalcule lui-même |
| §4 l.11 | « r = 0,55 global, **0,14–0,46** par générateur » | Fig. 3, p. 4, relue en image : r par générateur = **0,00** (GPT-5.4), 0,01, 0,05, 0,07, 0,14 (Opus 4.6), 0,15 (Haiku 4.5), 0,25, 0,27, 0,38, 0,46 (GPT-OSS-20B). Le rapport ne donnait que 3 exemples, pas une plage | **à corriger** : borne basse fausse, flatteuse pour le juge faible | « r par générateur de 0,00 (GPT-5.4) à 0,46 (GPT-OSS-20B) ; 0,14 pour Opus 4.6 » |
| §4 l.12 | g = 34,7 à w = 85,3 contre 70,7 | p. 2, 5, 6 : exact. Mais la fig. 5 (p. 6) donne 67,6 pour l'Opus bénin, incohérence interne relevée par le lecteur | à nuancer | Signaler l'écart 70,7 / 67,6 |
| §4 l.13 | F1 0,713 ; rappel 0,844 (moyennes par tâche, seuil ≥ 4), p. 2, 17 | Exact : mes moyennes donnent 0,7128 et 0,8441. Le seuil ≥ 4 est p. 4 | conforme | Pages 2, 4, 17 |
| §4 l.14 | 189 / 274 / 463, p. 5–6 | p. 6 | conforme | — |
| §4 l.15 | ≈ 75 % de faux positifs ; « tout signaler » F1 0,744 (calcul) | Mon recalcul : 142/189 = 75,1 %. « Tout signaler » donne 0,744 en agrégation poolée et **0,755 en moyenne par tâche**. TRACE poolé donne 0,716. `recon_trace.py`, rejoué, redonne les mêmes valeurs | conforme | Comparer 0,755 au 0,713 publié, qui est une moyenne par tâche (la conclusion se renforce) |
| §4 l.16 | AcMAS F1 0,93–0,95 / 0,92–0,94 ; FP 0,04–0,07 | Tableau 1, p. 6 : exact | à nuancer | Ajouter : seuil choisi en maximisant le F1 ; 100 % de faux positifs sans trace bénigne du domaine cible (p. 20) |
| §4 l.17 | 60,2 % et 54,9 % de tokens économisés à 90 % de rappel | p. 1 : « **The strongest settings** reduce… ». Ce sont les meilleures cellules (TextCraft avec Qwen-2.5-7B, WebShop avec Qwen3-1.7B). Les autres cellules donnent 34,7 et 47,3 %, puis 35,9 et 24,7 % (tableau 1, p. 5). Le scoreur est « stacking » (sonde + traits de surface) | **à corriger** : chiffre trop propre, qualificatif des auteurs supprimé | « Meilleurs réglages… ; sur 3 modèles : 34,7–60,2 % et 24,7–54,9 % » |
| §4 l.18 | 94,44 / 49,96 / 60,11 | Tableau 1, p. 5 : exact, ligne « Template-Based », nocivité sur WildGuardTest. Les auteurs parlent de « diagnostic upper bound » (p. 4) | conforme | Préciser le régime d'entraînement |
| §4 l.19 | Citation de la Proposition 1, p. 3 | Tronquée : la phrase finit par « **against any zero-stealth-budget attack** » | à nuancer | Citer la phrase entière : c'est la condition ε = 0 qui rend l'énoncé vide |
| §4 l.20 | Puissance de la moyenne 0,168 ; AUC du max 0,302 (calcul, « reproduit par l'orchestrateur ») | Le rapport donne les mêmes valeurs. **Ma réimplémentation indépendante donne 0,173/0,303 (20 000 + 20 000 trajectoires) et 0,172/0,300 (40 000 + 40 000)**, donc confirmé. Trois réserves : (i) aucune sortie de la reproduction « par l'orchestrateur » n'est archivée ; (ii) c'est une simulation de la construction du dépôt (marginale Beta), pas « une reconstruction à partir des tables du papier » ; (iii) l'AUC de la moyenne vaut ≈ 0,50 : la fuite passe par la variance (écart-type multiplié par 2,49) | à nuancer | Archiver la sortie. Préciser « simulation » et « puissance unilatérale ». Ajouter la ligne δφ = 0,09 (0,019–0,021 ; AUC du max 0,486), qui porte le « ≈ 2α » du §1.12 et de N-003 |

### 1b. Section 2, tableau des corrections (20 lignes)

| Ligne | Rapport / PDF | Verdict | Correction |
|---|---|---|---|
| 1. Auteurs de NARCBench | p. 1 : 6 auteurs, Oxford / ELLIS / UCL, v3 du 1er octobre 2026, pas de NYU | conforme | — |
| 2. Cadrage | p. 2, 12, 14 | conforme | — |
| 3. Deception Split | p. 13, équation 6 | conforme | — |
| 4. Transfert | Tableaux 2 à 5 recalculés : les 4 plages sont exactes ; « 0,60–0,86 » est absent de la v3 | conforme | Pour GPT-OSS, la plage porte sur 3 familles seulement |
| 5. Juge textuel | p. 41, citation exacte | conforme | Ce juge était aussi *informé* de la menace ; essai sur 20 + 20 parties |
| 6. 2609.03035 | p. 1, 3, 14, 15 : mixte ≤ 0,80 ; rappel 0,95 → 0,41 et 0,96 → 0,55 ; ni « construct », ni « intent », ni « incrimin » | conforme | — |
| 7. Cinq stratégies | p. 14 (annexes A.1 et A.2), p. 7 | conforme | — |
| 8. 45 % / 6 % | p. 1, 2 ; fig. 5, p. 8 | conforme | — |
| 9. + 9,5 % | p. 5, 14 ; 9 cellules recalculées | conforme | Étiqueter « 9 cellules » comme reconstruction du lecteur |
| 10. LASR / « Persuade Me » | Introuvables dans le PDF | conforme | — |
| 11. EMNLP | Introuvable dans le PDF | conforme | — |
| 12. TRACE | p. 2, 3, 4, 17 | conforme | — |
| 13. E-valuator | p. 1, 4–6 | conforme | « Any type » est p. **3** ; l'échec de Ville est p. 7–8 |
| 14. TRACES | p. 9, 4 | conforme | Modèles nommés p. 5 ; lecture hors ligne p. 8 |
| 15. Probe Trajectories | p. 3–5 | conforme | « Le max ne se justifie qu'à l'intérieur d'une action » est une analyse du lecteur, à étiqueter |
| 16. 2606.10456, identité | p. 1 : exact. Le titre du README vient du dépôt. La réserve « horizon fixe » ne vaut que pour 2(b) ; 2(c) est correcte pour l'autocorrélation sur échelle gaussienne | à nuancer | Corriger la portée de 2(b) et 2(c) |
| 17. Traces réelles | Le PDF dit « **120 benign goals** » (p. 8) et présente la fig. 7c comme une concaténation d'épisodes réels (p. 10). « 16 objectifs », « 7 valeurs » et « remontée synthétique » viennent du **dépôt** : je les ai vérifiés (`gpu/gen_real_traces.py`, `gpu/results/real_traces.json`, `exp_realdata_detect.py` l. 116–125). « Puissance → 1 » est la Prop. 2(c), p. **4** | **à corriger** (attribution de source) | Source : « dépôt b35f238 » pour les faits de code ; p. 4 pour 2(c) ; mentionner que le PDF dit 120 |
| 18. 0,688 ; H ; 0,62 → 0,86 | p. 7 : H absent. Le tableau 3 (p. 8) porte « H = 2.0 », origine probable de l'erreur. Le PDF annonce « 500 bootstrap replications » (p. 5) : « un seul tirage », « ≈ 0,53 » et « H = 1,5 » viennent donc du code et du calcul. La courbe de la fig. 6b donne bien ≈ 0,635 → ≈ 0,847, comme le JSON, mais sa **légende (p. 9) dit 0,62 → 0,86** | à nuancer | Préciser « d'après le code ». Écrire « courbe et JSON contre texte p. 7 et légende p. 9 » |
| 19. Monitor A | p. 6 ; tableau 2, p. 7 : a_mean = 0,048, a_max = 0. « ≈ 2α » vaut à δφ = 0,09 : 0,021 chez moi, et 0,0204 analytiquement avec la marginale N(0,1) du PDF | conforme | Préciser δφ ; la fuite croît avec δφ (0,047 puis 0,168) |
| 20. Environnement (a) | p. 2, 3, 4, 55, 11, 13 | conforme | — |

### 1c. Autres sections de l'état de l'art (écarts seulement)

| Emplacement | Écrit | Source | Verdict | Correction |
|---|---|---|---|---|
| Statut | « Chaque verdict cite la page et une citation exacte » | Les verdicts « introuvable » et les calculs n'ont ni page ni citation | à nuancer | « … hors verdicts d'absence » |
| Statut | « calcul » = reconstruction par script à partir des tables du papier | Faux pour `fuite_monitor_A.py` (simulation). Des lectures de figure ne sont pas marquées (≈ 35 points, 45/6, « 9 cellules ») | à nuancer | Marquer chaque chiffre selon sa nature |
| §1.1 | Doomed : « garantie globale … (Clopper-Pearson par porte) » | p. 4 : la garantie exacte vient d'un **certificat indépendant optionnel**. Horizon figé à 6 portes. Sans certificat, jusqu'à 4 graines sur 20 sous la cible (p. 13) | à nuancer | Réécrire en conséquence |
| §1.1 | Régime « sous le seuil par action » libre | Le rapport H2 cite Yueh-Han et al. 2025 (2506.10949) en priorité 2, pour ce régime précis | à nuancer | « Libre dans les sources lues » ; ajouter la référence en §5 |
| §1.2 et N-005 | Nul de régression vers la moyenne et verdict par jeton « libres » | PARROT et BASIL menacent ces deux points ; ils ne sont pas lus (rapport C §5) | à nuancer | « Sous réserve de PARROT et BASIL » |
| §1.4 | Contre-déférence d'Opus et de Sonnet 4.6 | −3 et −4 (p. 33) sont des estimations ponctuelles, sans intervalle publié | à nuancer | « Significativité non établie » |
| §1.6 | « b* est publié » | L'invite est publiée ; **les poids ne le sont pas** (vérifié p. 48–49 et 68–71). b* a été trouvé avec le proxy de vérité | à nuancer | Préciser les deux points |
| §1.11 | « AcMAS est la première détection par activations en multi-agents » | p. 10 : « To the best of our knowledge … first framework to address adversarial compromise » (auto-revendication). NARCBench p. 3 cite **Golechha & Garriga-Alonso, NeurIPS 2025**, qui détectent la tromperie dans un jeu multi-agents avec des détecteurs boîte blanche par agent | **à corriger** | « AcMAS *se dit* premier ; contredit par Golechha 2025 et NARCBench » |
| §1.12 | « ≈ 2α » juxtaposé à « 0,168 à δφ = 0,40 » | Ce sont deux points différents : δφ = 0,09 et δφ = 0,40 (≈ 17α) | à nuancer | Préciser les δφ |
| §3, 2606.08892 | « 72 sur 73 confirmées » | La 73e citation est confirmée sur l'image de la page | à nuancer | « 73 sur 73 » |
| §5 l.6 | Les auteurs s'appuient sur ces 5 travaux | p. 2 : seulement Hebbar 2025, Gasteiger 2025 et Gan 2026 (= ASMR-Bench) | à nuancer | Restreindre la liste ; ajouter Hebbar, et Benton 2024 (2410.21514) |

### 1d. `decisions-v2.md`

| Emplacement | Écrit | Source | Verdict | Correction |
|---|---|---|---|---|
| N-003, enjeu | « tout moniteur … est aveugle », entre guillemets | C'est une paraphrase, pas une citation (Prop. 1 p. 3 ; « provably blind » p. 9) | à nuancer | Citer la Prop. 1 |
| N-003, enjeu | « moyenne ≈ 2α, max < α » | Vrai à δφ = 0,09, mais absent de la §4 (R7) | à nuancer | Ajouter la ligne à la §4 |
| N-003 (a) | « Avantage : vrai » | Seul T1 est corroboré par les sources ; T2 et T3 viennent de la note mathématique, que personne n'a contrôlée | à nuancer | Limiter « vrai » à T1 |
| N-003 (c) | « la version correcte est libre » | Le rapport classe l'énoncé par invariance « **adjacent** » (remarque « multiset » p. 1), et seulement vis-à-vis de ce papier | **à corriger** | « Adjacente ; libre vis-à-vis de 2606.10456 seulement » |
| N-005 (a) | « originalité ≈ 0,5 » | Le rapport C dit seulement « revoir 0,75 » | à nuancer | Marquer comme estimation de l'auteur |
| N-005 (b) | « zones libres » | HC4 est libre, HC6 est adjacent | à nuancer | Corriger HC6 |
| N-007 | Confiance haute ; « 0,35 » | Le rapport B demande de lire **Kulkarni 2026 avant toute revendication H2**. Padhi et FIPER sont en priorité 1. « 0,35 » n'a pas de source | **à corriger** | Conditionner (a) à ces lectures ; confiance moyenne d'ici là |
| N-008 | — | Conforme au rapport TRACE-AcMAS et à mes recalculs | conforme | Voir la remarque en section 3 |
| P-003 | — | Conforme aux sources | à nuancer | Ajouter : poids de b* non publiés ; revalidation sur juge 8B/3B (rapport 08892) |
| P-004 | Liste « ce qui manque » ; « plan B armé » | Le rapport liste aussi les poids de b* et le code MO-ASHA ; il dit « reste pertinent » | à nuancer | Compléter la liste |
| P-005 | « La sonde doit réussir sur (i-a) » | Une réussite sur (i-a) peut venir de la lecture de l'instruction (AcMAS : 100 % de faux positifs hors domaine ; sondes NARCBench apprises sur des rôles instruits) | à nuancer (omission) | Ajouter un témoin « instruit sans sabotage » |

## 2. Omissions importantes

1. **Kulkarni 2026 comme préalable à H2.** Le rapport B l'exige avant toute revendication H2, Tr ou spatio-temporelle. N-007 recommande pourtant en « confiance haute ».
2. **Lecture de l'instruction plutôt que de l'intention.** Les rapports AcMAS et NARCBench signalent ce risque (100 % de faux positifs hors domaine pour AcMAS ; sondes apprises sur des agents instruits). Il est absent des sections 1, 3 et 4 et de P-005, et touche H8 et P-005.
3. **Primauté d'AcMAS.** Elle est affirmée comme un fait, alors que Golechha & Garriga-Alonso 2025 et NARCBench la contredisent.
4. **Garantie de Doomed.** Elle dépend d'un certificat optionnel, sur un horizon figé ; jusqu'à 4 graines sur 20 tombent sous la cible sans certificat.
5. **Chiffres NARCBench.** Le 1,00 repose sur ≈ 5 épisodes par pli, et le code ne correspond pas à la v3 : ce ne sont pas des bases à battre (rapport B, alerte 3).
6. **b\*.** Ses poids ne sont pas publiés et il a été sélectionné avec le proxy de vérité. Cela touche P-003 et P-004.
7. **Références menaçantes absentes de la §5.**
   - Yueh-Han et al. 2025, pour le régime « chaque pas bénin ».
   - Pour H3 : Pang et al. 2026 (Codetta), Schroeder de Witt 2026 (2606.09931), Vaikuntanathan & Zamir 2026.
   - Golechha & Garriga-Alonso 2025.
   - Benton et al. 2024.
   - Pour HC3, HC4, HC5 : Liu (2403.04957), Greshake (2302.12173), Baker (2503.11926), Wataoka (2410.21819), Li (2502.01534).
8. **2609.03035.** La « revendication interdite » de la §5 de l'état de l'art v1 n'a plus de source (rapport B, alerte 2).
9. **Incohérences internes de 2606.08892.** Le lecteur en relève sept et demande de ne pas reprendre ces chiffres sans précaution ; or 70,7 est repris en §4.
10. **Probe Trajectories, annexe I.** Des variantes autres que « Pool » atteignent une AUROC ≈ 0,95 (p. 28) ; cela fragilise la règle « max, jamais la moyenne » (rapport H2, alerte 3).
11. **`ressources-code-v1.md`, ligne 15.** Ce document hors périmètre répète « en concaténant les épisodes », l'erreur que la §2 corrige pour l'état de l'art. Il n'est pas listé à corriger.

## 3. Cohérence interne des décisions

- **N-003, N-005, N-008, P-003, P-004 et P-005** découlent bien des faits rapportés.
- **N-007** va au-delà des sources : confiance haute alors qu'une référence non lue (Kulkarni) est signalée comme bloquante, et probabilité de 0,35 sans source.
- **N-003 (c)** et **N-005 (b)** qualifient de « libre » ce que les rapports classent « adjacent ».
- **Probabilités d'originalité (0,5 et 0,35).** Ces chiffres ne sont traçables à aucune source (R6).
- **Remarque d'analyse sur N-008 (a).** À taux de faux positifs égal et prévalence fixée, le F1 est une fonction strictement croissante du rappel. L'option (a) ramène donc le bras F1 à une comparaison de rappels : la disjonction est surtout nominale, et les « + 5 points » dépendent de la prévalence. Le plancher « tout signaler » est un plancher de F1, puisque son taux de faux positifs vaut 100 %.

## 4. Verdict global

**Publiable après les corrections listées.**
- **Sources.** Toutes les empreintes sont conformes.
- **Section 4.** 12 lignes sur 20 sont conformes, 6 sont à nuancer et 2 à corriger : l.11 (chiffre faux) et l.17 (chiffre trop propre).
- **Section 2.** 17 lignes sur 20 sont conformes, 2 sont à nuancer et 1 à corriger : la ligne 17, où des faits de code sont attribués à des pages du PDF.
- **Recalculs.** Les chiffres « calcul » de TRACE et de la fuite de Monitor A tiennent sous mes recalculs indépendants.
- **Conclusions.** Aucune erreur n'inverse une conclusion principale.
- **Corrections obligatoires avant usage (R6, R7).** Les deux corrections de la §4 (l.11, l.17) et celle de la §2 (ligne 17), la primauté d'AcMAS (§1.11), le conditionnement de N-007 et la qualification de N-003 (c).
