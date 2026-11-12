# Provenance des pièces — antériorité de POPPER, E-valuator et de leurs voisins pour l'organisme d'idéation — v1

Récupération par un sous-agent (Opus 5.5) de la session mère, le 9 novembre 2026, de 09:33 à 09:50 UTC (horloge du
conteneur, `date -u`). Suite de R-1990, point (a), et de R-1992 (`registres/decisions.md`). Aucune inscription, aucune
clé, aucun appel de modèle payant. Outil : `curl`, par le mandataire HTTPS du conteneur, redirections suivies, en-tête
User-Agent « Mozilla/5.0 (X11; Linux x86_64) controle-ia-corpus/1.0 ». Note de lecture qui s'appuie sur ces pièces :
`docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-popper-evaluator-v1.md`.

## 1. Pièces versées ou déjà au dépôt

| n° | pièce | fichier (sous `docs/sources/pdf/`) | pages | octets | SHA-256 | adresse, code, heure | licence relevée |
|---|---|---|---|---|---|---|---|
| 1 | Huang, Jin, Li, Li, Candès, Leskovec, « Automated Hypothesis Validation with Agentic Sequential Falsifications », Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:25372-25437, 2025 (version publiée, PDF créé le 3 juin 2025) | `huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 66 | 1 867 721 | `a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998` | `https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf`, 200, `application/octet-stream`, 09:34:30 | « Copyright 2025 by the author(s) » (p. 1) |
| 2 | Même article, prépublication arXiv 2502.09858 v1, 14 février 2025 (seule version au 9 novembre 2026) | `huang-2025-arxiv-2502.09858v1-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 65 | 2 345 399 | `0df7ebac15ec1a3084a00ecedac1f1051f765634f202d1bce84a1fec9b18b27a` | `https://arxiv.org/pdf/2502.09858v1`, 200, `application/pdf`, 09:34:11 | Creative Commons Attribution 4.0 (page arXiv) |
| 3 | Sadhuka, Prinster, Fannjiang, Scalia, Berger, Regev, Wang, « E-valuator: Reliable Agent Verifiers with Sequential Hypothesis Testing », arXiv 2512.03109 v2, 28 mai 2026 (dernière de deux versions au 9 novembre 2026) | `2512.03109v2.pdf` (**déjà au dépôt**, compagnon vérifié `OK` par `sha256sum -c` à 09:50 ; empreinte égale déjà relevée à 09:32) | 27 | 1 992 724 | `b7a46e4cf781aec0c5730196b9f6a2ea1e42c3ec63f1e5260dff223dfafe3828` | non retéléchargé ; page arXiv lue à 09:35:27 (200) | Creative Commons Attribution 4.0 (page arXiv) |
| 4 | Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, « Generalization in Adaptive Data Analysis and Holdout Reuse », arXiv 1506.02629 v2, 25 septembre 2015 (dernière de deux versions) | `anteriorite-P-041-v2/c8/1506.02629.pdf` (**déjà au dépôt**, non recopié ; compagnon vérifié `OK`) | 29 | 705 052 | `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71` | retéléchargé `https://arxiv.org/pdf/1506.02629v2`, 200, 09:37:10 : octet pour octet identique (R11) | arXiv, licence non exclusive de distribution 1.0 |
| 5 | Blum, Hardt, « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », arXiv 1502.04585 v1, 16 février 2015 (seule version) | `anteriorite-P-041-v2/c8/1502.04585.pdf` (**déjà au dépôt**, non recopié ; compagnon vérifié `OK`) | 16 | 308 155 | `957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe` | retéléchargé `https://arxiv.org/pdf/1502.04585v1`, 200, 09:37:14 : identique (R11) | arXiv, licence non exclusive 1.0 |
| 6 | Gao, Schulman, Hilton, « Scaling Laws for Reward Model Overoptimization », arXiv 2210.10760 v1, 19 octobre 2022 (seule version ; « Preprint. Under review. », p. 1) | `gao-schulman-hilton-2022-arxiv-2210.10760v1-scaling-laws-reward-model-overoptimization.pdf` | 28 | 3 186 215 | `c793c551a1b027402f758cce0fbf6b400cf66d0df57d2875d275e73cfd58bfc9` | `https://arxiv.org/pdf/2210.10760v1`, 200, `application/pdf`, 09:37:18 | arXiv, licence non exclusive 1.0 |
| 7 | Miyai, Toyooka, Otonari, Zhao, Aizawa, « Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper », arXiv 2511.04583 v4, 11 mars 2026 (dernière de quatre versions) ; « Published in Transactions on Machine Learning Research (02/2026) » (p. 1) | `miyai-2026-tmlr-arxiv-2511.04583v4-jr-ai-scientist-risk-report.pdf` | 76 | 6 193 688 | `dbd31ea61ff83eda142bbcb961faeda4c0c01075dc74c1bde12dc8540aa8393a` | `https://arxiv.org/pdf/2511.04583v4`, 200, `application/pdf`, 09:37:23 | arXiv, licence non exclusive 1.0 |

Chaque fichier versé (n° 1, 2, 6, 7) a son compagnon `.sha256` écrit par `python -m controle_ia.scellement sceller`
(R6). Les pièces 4 et 5 ne sont pas recopiées : la copie existante est identique à ce que sert arXiv ce jour.

## 2. Identités recoupées (R11)

- **POPPER = arXiv 2502.09858** : métadonnées de la page arXiv (titre, six auteurs, date 2025/02/14 ; lue à 09:34:01) ;
  index des actes, `https://proceedings.mlr.press/v267/` (200, 09:34:20) : même titre, mêmes auteurs, « PMLR
  267:25372-25437 », fiche `huang25n`, forum OpenReview `iTevNo8PzG`, code `github.com/snap-stanford/POPPER` ; référence 8
  d'E-valuator (p. 11 du PDF n° 3) : même titre, mêmes auteurs, « pages 25372–25437. PMLR, 2025 ». Le doute de la note
  Co-Scientist (§ 5, dernière puce) est levé. Le titre « POPPER: A Framework for Rigorous Hypothesis Validation with LLM
  Agents » (réponse de Kimi) n'est ni celui d'arXiv ni celui des actes.
- **« The reusable holdout » (Science) n'est ni 1411.2664 ni 1506.02629.** Notice PubMed 26250683 (E-utilities, 200,
  09:45:55) : « The reusable holdout: Preserving validity in adaptive data analysis », Science, vol. 349, n° 6248,
  p. 636-638, 7 août 2015, DOI `10.1126/science.aaa9375`, mêmes six auteurs ; aucun identifiant arXiv dans cette notice
  ni dans celle de Semantic Scholar (identifiants externes : MAG, DOI, CorpusId, PubMed). 1411.2664 = « Preserving
  Statistical Validity in Adaptive Data Analysis » (page arXiv lue à 09:35:11 ; v1 du 10 novembre 2014, v3 du 2 mars
  2016), que le PDF n° 4 cite comme « CoRR, abs/1411.2664, 2014. Extended abstract in STOC 2015 » (p. 23).
  1506.02629 = l'article technique du holdout réutilisable (Thresholdout), qui ne cite pas l'article de Science.
  La suspicion de `docs/notes/reponses-especes-seules-2026-11-01-v1/lecture-verifiee-selection-generations-v2.md`
  (l. 53) est donc fondée pour le couple « Science, 1411.2664 » ; le couple « Science, 1506.02629 » est aussi inexact.

## 3. Pièce non obtenue

- **Article de Science** (DOI `10.1126/science.aaa9375`) : accès fermé selon Semantic Scholar (`openAccessPdf.status` =
  « CLOSED », 09:36:50 ; réponse enregistrée à 09:49:03) ; `https://www.science.org/doi/10.1126/science.aaa9375` rend 403
  (page de contrôle « Just a moment... », 09:36:50) ; la page de l'auteur `https://www.cis.upenn.edu/~aaroth/reusable.html`
  échoue en TLS (« unable to get local issuer certificate », code 60 de curl), avec et sans le paquet d'autorités du
  mandataire (09:35:59, 09:36:22) ; l'état du mandataire ne signale aucun échec de relais. Seuls la notice et le résumé
  PubMed sont lus : non opposables pour un chiffre (R7) ; aucun chiffre n'en est tiré.
- **arXiv 1411.2664** : page lue (identité), PDF non téléchargé.

## 4. Extraction du texte

Deux sorties par PDF, page par page, pour p de 1 au nombre de pages donné par `pdfinfo` :

```
printf '======== PAGE %d ========\n' p
pdftotext -layout -enc UTF-8 -f p -l p FICHIER.pdf - | tr -d '\f'      # sortie « -pages.txt » (mise en page)
pdftotext -enc UTF-8 -f p -l p FICHIER.pdf - | tr -d '\f'              # sortie « -pages-lecture.txt » (ordre de lecture)
printf '\n'
```

`pdftotext` version 24.02.0 (poppler). La sortie avec `-layout` (demandée) entrelace ligne à ligne les deux colonnes des
PDF à deux colonnes (POPPER, actes d'ICML) ; les citations de la note sont donc contrôlées sur la sortie « ordre de
lecture ». Le séparateur porte le numéro de page du PDF ; pour toutes les pages citées, ce numéro égale le numéro imprimé
(contrôle par programme ; seules les pages 40 à 76 de Jr. AI Scientist, qui reproduisent les articles générés avec leur
propre numérotation de lignes, diffèrent). Contrôle : nombre de séparateurs égal au nombre de pages de `pdfinfo` pour les
sept PDF (66, 65, 27, 29, 16, 28, 76).

## 5. Archive des fichiers de travail

`docs/sources/lecture-pdf-niveau2/fichiers-de-travail-anteriorite-popper-evaluator-v1.tar`, 2 918 400 octets, SHA-256
`45c19344e31bee2a36a29c236ae6cecf736645d64e840f305c083b2b44e88892` (compagnon `.sha256`). Archive reproductible (noms
triés, date fixée au 2026-11-09 09:50:00Z, propriétaire 0). Contenu, sous `fichiers-de-travail-anteriorite-popper-evaluator-v1/` :
`extractions/` (les quatorze sorties du § 4), `scripts/` (`extraire_pages.sh`, `extraire_pages_lecture.sh`, `lire.sh`),
`pages-lues/` (les sept pages arXiv lues, la notice PubMed, la réponse de Semantic Scholar, l'extrait de l'index des actes
PMLR 267) et `SHA256SUMS.txt` (27 lignes). Empreintes des extractions les plus citées : POPPER, actes, ordre de lecture
`4bd38d2d48862d1e…` ; E-valuator, ordre de lecture `87f34d5f1ca076f6…`.

L'archive est rangée dans `docs/sources/lecture-pdf-niveau2/` parce que le script de copie expurgée en retire
`docs/sources/lecture-pdf-niveau2/*.tar` (`scripts/depot_expurge_v5.py`, l. 44) ; des fichiers texte posés à côté des
PDF dans `docs/sources/pdf/` ne seraient pas retirés (seuls `*.pdf` le sont, l. 41-42), et le texte intégral d'articles
sous licence arXiv non exclusive passerait dans la copie publique.

Version 1 ; jamais réécrite (R12).
