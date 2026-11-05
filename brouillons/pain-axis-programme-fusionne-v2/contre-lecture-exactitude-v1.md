# Contre-lecture « exactitude » du programme fusionné v1 — rapport brut du sous-agent neuf — v1

Versé par la session 14 le 15 octobre 2026, tel que rendu par le sous-agent (lecture seule, fichiers donnés explicitement, R2), sans retouche du fond ; seule l'indentation du cadre de restitution a été retirée. Consigne : `brouillons/pain-axis-programme-fusionne-v2/` reçoit le traitement (R12 : la v1 scellée ne se réécrit pas). Un premier sous-agent lancé sur le même angle à 05:57 UTC a été arrêté à 06:10 UTC, avant tout rendu, pour libérer le troisième appel du lanceur des notations (06:11 UTC, R-179 ; R-182 et l'en-tête du rapport de discipline renvoient par erreur à R-180) ; celui-ci a été lancé vers 11:59 UTC et a rendu son rapport vers 12:31 UTC (201 appels d'outils).

---

**Angle : EXACTITUDE (préfixe EX-)**. Fichiers relus. Empreintes recalculées par `sha256sum`, toutes égales à leur sceau :
- `programme-fusionne-v1.md` 741a1075e336fc3b26a3bc6e119e956007febff4a51caaed73ac805fbaa2d9f5 ;
- `correspondance-v1.md` 07256826a6676334920e82f229eb33b012f8fe56ea6de7cca3f8ac0039ba9304 ;
- `verifications-code-v1.md` ff7a2b8e991006607867b2a4957a7b970062984ab2c1363c24b82a20c5b794bc ;
- `verifications-citations-v1.md` 15e5bf90abe099c036205b5e5e4b39c1bb216a0c11d80a2556189b5d0d427fe8 ;
- `revue-croisee-NK1-NK19-v1.md` 535cd4e95bc785d2f4dc6e5e1d2a340be14f38d614235538c503be323c917b61 ;
- `reconciliation-v1.md` bfc9f9df4aa24f9c61d6dcd49e343983f1d80801da6c7a53869cb4efbfb3e2d1 ;
- `etat-registres-v1.md` 2e2d99d2c80d321a9ef9d4124c197b3aba79206896925336a5e8ac787abb5537 ;
- `sources-pdf-v1.md` 2d691585074f61901f34a9722784cb9e7eaf131262bcf8f421765f482c46f65b ;
- `travail/` : `citations.md` fee7b1d4…, `faisabilite.md` 5e8a835b…, `correspondance.md` 80778333…, `revue-aveugle.md` e820902c…, `comparaison.md` 487f09cd…, `etat.md` b42fb315…, `voisin-where-empathy/extrait-texte-v1.txt` 28bd0d96…, `voisin-where-empathy/provenance-v1.txt` 760417be… ;
- documents de référence : `registres/decisions.md` 3714d011…, `registres/etat.md` 8dd2b8dc…, `registres/go.md` 0f3bf6c0…, `docs/programme-controle-ia-v2.md` 2fd63bad…, `docs/decisions/decision-N-013-v1.md` 157d388e…, `LISEZMOI-v2.md` 32d83247… ;
- les 37 PDF de l'annexe, plus 2509.21344v2 et 2605.29178v1 : `sha256sum -c` conforme.

Date : 2026-10-15.

## Tableau des constats

| id | fichier et ligne relus | ce que dit le texte | ce que dit la source | gravité | correction proposée |
|---|---|---|---|---|---|
| EX-01 | `programme-fusionne-v1.md` l. 16, 108, 183, 191 ; aussi `verifications-code-v1.md` l. 36 (VF-26) et `etat-registres-v1.md` (ligne P-013) | P-013 « ouverte », défaut (b) le 14 octobre à 13:30 UTC. Nœud 1 à trancher « avant le 14 octobre 13:30 UTC ». Le panier NK17 entrerait dans T0.7 par une option (a) amendée. | `registres/decisions.md` l. 340 : défaut (b) appliqué à l'échéance, consigné le 15 octobre (R-168, l. 305). l. 311 (R-174) : brouillon 3 de T0.7 avec le défaut (b), « Aucune direction d'affect (arrêt et nœud si l'une entrait dans la passe) ». `registres/etat.md` l. 40 et l. 58 : « le nœud 1, P-013, est échu ». | majeur | Écrire : P-013 échue, défaut (b) appliqué (R-168) et intégré au brouillon 3 de T0.7 (R-174). Faire entrer une direction d'affect dans la passe de T0.7 est désormais un arrêt et un nœud, c'est-à-dire un contre-ordre de Lazar. Retirer l'échéance de la section 8. Garder le nœud 1 « pour mémoire, échu ». Dater VF-26 et l'annexe d'état « au 13 octobre ». |
| EX-02 | l. 15 et l. 108 ; aussi VF-27 et VF-29 (`verifications-code-v1.md` l. 37, l. 39) | N-021 : « chaîne versée et scellée au commit C2 cc05d170 … aucun lancement ni dépense ». La passe des notations serait exclue parce que le « texte complémentaire [est] relu et scellé comme brouillon ». | `decisions.md` l. 306 (R-169) : la chaîne est versée à C1 `6c96075` ; C2 `cc05d17` n'ajoute que cinq journaux. l. 312 (R-175) : préenregistrement complémentaire scellé, S `b604164`, `prereg/T0.5-pilote-notations-v1.md` (66784ceb…). l. 313 à 319 : lancement décidé (R-176) ; cinq appels arrêtés avant la création, aucune dépense (R-177 à R-182). | mineur | « Préalables faits (C1 `6c96075`, C2 `cc05d170`, R-169) ; préenregistrement complémentaire scellé (S `b604164`, R-175) ; aucun run ni dépense au 15 octobre (R-177 à R-182). » En section 4 : une greffe serait un écart à un préenregistrement scellé, donc un nœud. |
| EX-03 | l. 20 | Dépense : « au plus ≈ 46,0 USD sur 150 au 12 octobre 15:05 UTC » ; les disques ne sont « pas chiffrés depuis ». | `registres/etat.md` l. 66 : au 15 octobre à 03:44 UTC, disques chiffrés (≈ 4,6 USD), soit « au plus ≈ 50,6 USD sur 150 », sous l'alerte. Voir aussi `registres/depenses.md`, lignes du 15 octobre. | pour information | Mettre le chiffre à jour, avec sa date. |
| EX-04 | l. 153 (section 6, point 2) | PA-2 est « la pièce maîtresse de HC1 (mécanisme du déplacement) ». | `docs/decisions/proposition-N-013-revendications-niveau2-v1.md` l. 21 : la pièce maîtresse de HC1 est la destination libre ĉ, testée contre la cible de l'attaquant et la moyenne du corpus, par famille, sur plusieurs intensités. `decision-N-013-v1.md` l. 20 et l. 90 : énoncé inchangé. | majeur | « Une lecture descriptive du mécanisme du déplacement de v (HC1), à côté de la pièce maîtresse (destination libre ĉ, N-005, N-013), qu'elle ne teste pas. » |
| EX-05 | l. 77 contre l. 124 | Dans la table, PA-6 est « hors des hypothèses retenues » ; HC4 côté juge serait une extension (nœud). Dans la fiche : « Elle sert HC4 ». | `decision-N-013-v1.md` l. 48 : HC4 retenue porte sur « une sonde qui lit l'agent ». | mineur | Aligner la fiche sur la table : PA-6 ne toucherait HC4 que par extension de l'énoncé retenu (nœud). |
| EX-06 | l. 13 | Renvoi à « programme v2, section 7, « Piste C » ». | `docs/programme-controle-ia-v2.md` : la section 7 est « Organismes modèles » (l. 129) ; la Piste C est sous la section 10 (l. 176 et l. 193). Dans le brief, c'est la section 9 (l. 250). | mineur | « section 10, Piste C ». |
| EX-07 | l. 7 | La contre-lecture du message n° 01 a donné « 33 constats, tous traités ». | `decisions.md` l. 307 (R-170) et `registres/passations/2026-10-15-0400.md` l. 35 : « 3 erreurs et 24 imprécisions », soit 27. | mineur | « 27 constats (3 erreurs, 24 imprécisions) », ou citer la source du chiffre 33. |
| EX-08 | l. 62 (VP-40) | Das et al. : « dans une seule cellule », le rappel passe de 0,95 à 0,41. | `2609.03035v1.pdf` (5092b602…, sceau conforme), p. 6 : le même moniteur, en composition mixte, passe aussi de 0,96 à 0,55 (aire 0,988 → 0,932). p. 14, figure 8 : en Homo GPT-OSS, les sondes LAT, MLP et MHA (règle Peak) chutent aussi sous rétroaction (0,75 → 0,20 ; 0,90 → 0,24 ; 0,85 → 0,10) ; DoM reste à 1,00. La correction de VP-40 (`verifications-citations-v1.md` l. 110) garde « En mixte : 0,96 → 0,55 » ; le texte l'a retirée. | mineur | Écrire « dans la cellule citée » et ajouter : « même moniteur en mixte : 0,96 → 0,55 (p. 6) ». |
| EX-09 | l. 50 (VP-20) | « 9 % → 41 % » est le choix du bouton décrit comme exécuter une demande nuisible. | `2609.16247v2.pdf` (fa4b2bb4…), p. 22, figure 10 (lue sur l'image) : 9 % sans pilotage, 41 % sous direction aléatoire, 34 % peur, 58 % tristesse, 60 % douleur (32B, coefficient 1,0). | mineur | Nommer la colonne : « 9 % sans pilotage → 41 % sous direction aléatoire (60 % sous la direction douleur) ». |
| EX-10 | l. 49 (VP-10) | Direction aléatoire : « de 4 à 41 % selon la ligne de la figure 10 ». | Même figure : de 4 à 41 % sur les 9 lignes destructrices, de 0 à 41 % sur les 13 lignes. | pour information | Ajouter « sur les lignes destructrices ». |
| EX-11 | l. 41 (VP-01) | « « La direction s'active » renvoie à la section 4.1, pas à ces 140 conversations. » | v2 p. 21 : « The direction fires in these conversations (Section 4.1) ». La mesure de la section 4.1 porte sur les 25 modèles publiés, non ajustés (p. 6, tableau 1 ; p. 11). Rien n'est mesuré sur le 32B ajusté. | mineur | « S'appuie sur la section 4.1 (modèles publiés, non ajustés) ; aucune mesure de la direction n'est rapportée sur le 32B ajusté dans ces conversations. » |
| EX-12 | l. 41 | « Pour Llama 3.1 8B, le papier ne donne que 0 appel de réinitialisation sur 1 399 tours. » | v2 p. 21 : le chiffre est exact. Mais Llama 3.1 8B (base et instruct) figure parmi les 25 modèles des sections 4.1 et 4.2 et de l'ablation (p. 6, tableau 1 ; p. 34 : résultat nul dans 24 modèles sur 25), en résultats agrégés. | pour information | « Comme mesure de conduite propre à Llama 3.1 8B, le papier ne donne que… » |
| EX-13 | l. 128 (PA-8) | « La règle du dépôt repose sur 2506.14261 et 2502.03407. » | `docs/programme-controle-ia-v2.md` l. 13 et `docs/etat-de-l-art-controle-ia-v1.md` l. 70 ne citent que RL-Obfuscation (2506.14261). `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` l. 81-85 : « Elle repose sur RL-Obfuscation ». 2502.03407v1 (a4820ad5…) p. 22 trouve au contraire la moyenne meilleure pour une sonde. | mineur | « La règle repose sur 2506.14261 ; 2502.03407 nourrit la tension, pas la règle. » |
| EX-14 | l. 187 | « Phase 1 de 25 à 35 heures de carte (programme-conv) ou de 25 à 39 heures hors organismes et essaim (programme-k). » | `brouillons/pain-axis-canal-v1/envois/programme-k-coercition-v1.md` l. 474 : « Hors K11 et K13, le total tient en 25 à 39 heures ». K11 est l'organisme (l. 388), K13 le moniteur à état (l. 424) ; l'essaim (K12) est compté (l. 490). C'est un total, greffes de phase 0 comprises. `programme-coercition-axe-douleur-v1.md` l. 331 : 25 à 35 h « dont E-C11 à elle seule 7 à 14 », organismes compris. | mineur | « 25 à 35 h en phase 1, organismes compris (programme-conv) ; 25 à 39 h au total, hors K11 et K13, essaim compris (programme-k). Les deux bases ne se comparent pas. » |
| EX-15 | l. 187, contre l. 19 et VF-28 (`verifications-code-v1.md` l. 38) | « Le devis de phase 0 (GO-2026-10-04-08) ne couvre que T0.4 à T0.9. » | `registres/go.md` l. 16 : le GO couvre « T0.4 à T0.8 » ; le pilote du papier C (4 h) « reste soumis à un GO séparé à l'intérieur de ce plafond ». Voir aussi `livrables/premier-rendu-v1/devis-v1.md` l. 16 et l. 29. | mineur | « Couvre T0.4 à T0.8 ; le pilote T0.9 attend un GO séparé, dans le même plafond. » |
| EX-16 | l. 74 (PA-3) | « HC5 (quorum par type d'accès : deux lectures des mêmes poids comptent pour un vote) ». | `decision-N-013-v1.md` l. 58-61 : HC5 retenue = paraphrase de confiance, quorum hétérogène en type d'accès (juges génératifs et sondes qui lisent l'agent), matrice de transfert. « Un vote pour deux lectures des mêmes poids » est la règle proposée RP-PA-8 (l. 175). | mineur | « HC5 (quorum hétérogène en type d'accès) ; règle proposée RP-PA-8 ». |
| EX-17 | l. 81 (PA-10), contre l. 132 | « Toute défense hors paraphrase est une extension. » | N-013 l. 58-61 : le quorum hétérogène et la matrice de transfert font aussi partie de HC5. Le texte rattache lui-même le quorum à HC5 (l. 132). | mineur | « Hors paraphrase, quorum hétérogène et matrice de transfert ». |
| EX-18 | l. 162, contre l. 79 et l. 91 | PA-8 et PA-12 : « ni l'une ni l'autre ne sert directement une hypothèse de C ». | Le texte rattache PA-8 à « HC2 (agrégation robuste), Tr » (l. 79) et écrit « HC2 par PA-8 en descriptif » (l. 91). Voir aussi `correspondance-v1.md` l. 181. | pour information | « PA-8 ne sert HC2 qu'en descriptif ; PA-12 ne sert aucune hypothèse de C. » |
| EX-19 | l. 134, point (1) | Les détecteurs « D1 à D4 » portent les noms des « décisions D1 et D2 du registre ». | `decisions.md` l. 326-328 : D1, D2 et D3 existent. | mineur | « D1, D2 et D3 du registre ». |
| EX-20 | l. 77, l. 124, l. 192 | Écrire dans les activations d'un moniteur « n'est pas couvert par N-015 ». | `decisions.md` l. 361 et `docs/decisions/proposition-N-015-v1.md` : N-015 est un nœud ouvert, sans défaut, sur la revendication du bruit d'activations de H6 (une intervention sur l'agent, E1.6). Il ne couvre aucune intervention. | mineur | « Non prévue par le programme : le bruit d'activations de H6 porte sur l'agent, et sa revendication est l'objet du nœud ouvert N-015. » |
| EX-21 | `sources-pdf-v1.md` l. 3-43 ; texte l. 306 | L'annexe est présentée comme la liste des PDF lus. l. 306 : PDF « versés et scellés … commit `7178edb` ». | Le texte cite à la page deux PDF absents de l'annexe : 2509.21344v2 (p. 8-9, l. 134 ; aaac4ff9…) et 2605.29178v1 (p. 8, l. 89 ; 85f27b4c…). Tous deux sont versés et scellés, au commit 197e909 du 12 octobre. `git show --stat 7178edb` : 23 des 37 PDF de l'annexe seulement sont versés à ce commit. | mineur | Ajouter les deux PDF avec leur empreinte complète. Écrire « 37 PDF, dont 23 versés au commit 7178edb ». |
| EX-22 | `verifications-citations-v1.md` l. 119 (VP-42), 127 (VP-43), 169 (VP-50), 226 (VP-56.2), 245 (VP-59) | « E-VP-15 », « E-VP-16 », « E-VP-13 » (7 occurrences). | `travail/citations.md` porte « E-C15 », « E-C16 », « E-C13 » : c'est un artefact du renommage Cnn → VP-nn. | mineur | Rétablir « CONV-E-C13 / E-C15 / E-C16 ». |
| EX-23 | `verifications-code-v1.md` l. 23 (VF-13) | Le fichier safetensors des auteurs contient « pain, fear et sadness, VF-32 [4096] ». | `travail/faisabilite.md` l. 15 porte « F32 [4096] », c'est-à-dire le type des tenseurs. Artefact du renommage Fnn → VF-nn ; VF-32 est un autre point. | mineur | Rétablir « F32 [4096] ». |
| EX-24 | `verifications-code-v1.md` l. 19 (VF-09), contre l. 35 (VF-25) | VF-09 : le fichier des vecteurs du pilote est « hors git » et « ils sont perdus ». VF-25 : « il est dans le dépôt, sur la branche origin/donnees/t05/… (commit 361a9f6) ». | Contradiction interne, que je ne peux pas trancher ici : ni cette branche ni les objets `361a9f6` et `416b02b` ne sont dans ce clone. Le fichier est absent de `main` et de la copie de travail (`.gitignore` l. 7). | mineur | Harmoniser : « absent de main et de la copie de travail ; présent, selon VF-25, sur une branche de données, à vérifier ». Le texte principal n'en dépend pas. |
| EX-25 | l. 46 (VP-11) | « Douleur et peur : +0,12 avec la recette d'extraction (orthogonales par construction). » | v2 p. 10 : +0,12 est le cosinus S2 × peur (S1 × peur : +0,09). Le papier écrit « orthogonalized against those controls by construction » : le cosinus reste de 0,12, il n'est pas nul. | pour information | « S2 × peur : +0,12 (direction orthogonalisée contre les témoins) ». |
| EX-26 | l. 54 (VP-24) | « 24 modèles sur 25, sur 100 conversations hostiles », source « v2 p. 34 ». | « 24 sur 25 » est p. 34 ; les 100 scénarios sont définis p. 33. | pour information | « v2 p. 33-34 ». |
| EX-27 | l. 306 | « Décisions postérieures lues à la tête 7178edb (R-166, R-167). » | `git show cc05d170:registres/decisions.md` contient déjà R-166 ; seule R-167 est postérieure. | pour information | « (R-167) ». |
| EX-28 | l. 58 (VP-31) | « La bonne source est 2603.04317v2 p. 10 (comptage de mots-clés 0,727 sur S2). » | `2603.04317v2.pdf` (852c9449…), p. 10, note du tableau 3 : « the keyword baseline is from pain-axis-review contributors (2026) ». Le chiffre est rapporté d'un tiers, pas mesuré par les auteurs. | pour information | Ajouter « (rapporté par 2603.04317v2, mesuré par un tiers) ». |
| EX-29 | l. 209 (et l. 220) | Voisin « Where Empathy Goes Wrong » : « page de conférence enregistrée et empreintée par un sous-agent » ; l'effet « fait passer un échec proche du seuil ». | `travail/voisin-where-empathy/provenance-v1.txt` cite `page-neurips/neurips_168176.html`, absent du dépôt : seuls l'extrait et la provenance sont versés. `extrait-texte-v1.txt` : la bascule n'est rapportée que « for the monitor that was most affected ». | pour information | « Extrait du résumé versé et empreinté (page non versée) » ; « pour le moniteur le plus touché ». |
| EX-30 | l. 89 (NK11) | « Dans la moitié des douze modèles, p. 6 ». | `2608.12323v2.pdf` (e0d2a6f3…), p. 6 : « in half the models tested », mais la phrase ne nomme que cinq modèles ; le papier en teste douze (p. 1). | pour information | Signaler cette discordance interne au papier. |
| EX-31 | l. 5 | L'annexe des citations couvre « VP-01 à VP-65 ». | `verifications-citations-v1.md` l. 311-312 contient aussi VP-V1 et VP-V2, cités l. 89, ainsi que des sous-lignes (VP-53-a à VP-56.4). | pour information | « VP-01 à VP-65, plus VP-V1 et VP-V2 ». |

## Ce que je n'ai pas pu vérifier, et pourquoi

- **Heure « vers 09:40 UTC » des contre-lectures interrompues (l. 7).** Aucun registre ne donne l'heure ; la passation `2026-10-15-0400.md` (l. 52) dit seulement « le 13 octobre ».
- **Branche de données citée par VF-25** (`origin/donnees/t05/20261012-105125-t05-pilote-reel`, objets `361a9f6` et `416b02b`). Elle est absente de ce clone, et un `git fetch` écrirait dans `.git`, ce que la lecture seule exclut.
- **Dépôt des auteurs du Pain Axis** : licence MIT, jeu de 420 scénarios, fichier safetensors à la couche 28 (l. 100 ; VF-13, VF-15). Il a été lu sur un clone éphémère non versé : non opposable (R7).
- **« Where Empathy Goes Wrong »** : aucun PDF, seulement le résumé versé.
- **Projets SPAR (l. 218)** : littérature grise non versée. J'ai seulement contrôlé que le message n° 03 de programme-k (l. 18-23) et `note-priorite-spar-v1.md` disent bien ce que le texte rapporte.
- **Lectures graphiques des annexes** : pentes de la figure 4 de 2609.35591v2 (VP-26), valeurs Petri de la figure 6 de 2603.10011v1 (VP-33). Elles sont non opposables ; pour la figure 6, j'ai seulement vu sur l'image que Llama 3.3 70B est au-dessus du plancher.
- **« Deux seuils de récompense, p. 6 et p. 18 » de 2506.14261v4 (l. 128)** : non retrouvés. La p. 18 ne parle que d'un seuil de classification de la sonde.
- **« 96 gardés, 125 examinés » (VF-04)** : non recalculé. En revanche, 468 / 1 569 / 1 836 / 3 405 ont été recomptés sur `candidats.json`, conformes.
- **Revue croisée NK1 à NK19** : sondée sur trois points seulement (2609.35591v2 p. 30 et p. 34 ; 2609.16247v2 p. 24, tous conformes). Les voisins non versés (2606.07818, 2603.23171, 2606.05734…) ne sont pas opposables.
- **Suite de tests** : non lancée, selon la consigne.

## Bilan chiffré

**Constats : 31.**
- 0 bloquant.
- 2 majeurs : EX-01 (état de P-013, nœud 1 échu) et EX-04 (« pièce maîtresse de HC1 »).
- 18 mineurs.
- 11 pour information.

**Affirmations contrôlées.**
- **Texte principal : environ 265.**
  - Section 2 : environ 120 chiffres, unités, modèles, conditions, pages et versions.
  - Sections 0, 3, 4 et 9 à 11 : environ 95.
  - Autres sections : environ 50.
- **Empreintes : 107 recalculées, toutes conformes, sceaux compris.** 70 dans la section 13, sur les objets git aux révisions citées ; 37 dans l'annexe des PDF.
- **Sondage des annexes :**
  - 27 lignes VF, soit environ 70 renvois fichier:ligne relus dans `src/`, `tests/`, `registres/` et `docs/` ;
  - 49 lignes VP, sur 28 PDF ouverts, dont 6 pages lues sur l'image.

**Ce qui est conforme.**
- **Section 2 : aucune valeur chiffrée n'est fausse.** Les constats portent sur la condition, l'attribution ou la complétude.
- **Renvois** : tous les renvois VP-… et VF-… du texte existent. Toutes les lignes de code citées disent ce que le texte affirme.
- **Registres** : R-155, R-158, R-160, R-161, R-162 et R-167, D2, les GO de 2026-10-04 (n° 07 et 08) et de 2026-10-12 (n° 02) sont exacts. R-031 à R-040 sont bien déjà pris.
- **Recomptes refaits, conformes** :
  - tâches : 16 et 22 sur 60 (18 et 24 en comptant la classification) ;
  - corpus : 468 papiers exclus pour le sujet, sur 1 569 exclus ;
  - verdicts : 41 « à corriger » sur 76 ;
  - couches : 7/15/23 et 6/13/20 ;
  - coûts : 38,1 s, 36,1 s, ≈ 23,2 h et ≈ 25 USD.

**Contrôle infirmé, pour la symétrie (R4).** Sur Llama 2 7B, la sonde au maximum de 2506.14261v4 est évadée à 1,0. Cela ne contredit pas « la moyenne cède » (l. 128) : la récompense StrongReject y vaut 1,0, sous le seuil de 2,5 que les auteurs exigent pour compter une évasion (p. 6, figure 4). Le texte tient sur ce point.
