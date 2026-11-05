# Chiffres et venues introuvables — lectures sur PDF de niveau 2 (lots 1 à 3) — v1

Compilation par un compilateur neuf, sans lecture de PDF (format de document portable). « Introuvable » veut dire : absent du PDF empreinté que le lecteur a lu, après la recherche indiquée ; ce n'est pas une preuve que le chiffre ou la venue soit faux. Tant qu'une source primaire n'est pas lue et empreintée, le chiffre ou la venue n'est pas opposable (R7). Rapports : « lot2-X » = `docs/sources/lecture-pdf-niveau2/rapport-lot2-X-….md`, de même pour les lots 1 et 3.

Sigles des venues et des termes de recherche, recopiés tels quels : ICML (International Conference on Machine Learning), ICLR (International Conference on Learning Representations), NeurIPS (Conference on Neural Information Processing Systems), ACL, EMNLP et NAACL (conférences de l'Association for Computational Linguistics et de ses chapitres), PMLR (Proceedings of Machine Learning Research), FPR (taux de faux positifs), DAI (International Conference on Distributed Artificial Intelligence).

## 1. Documents du programme

| document | ligne | chiffre ou venue | ce que les lecteurs ont cherché | rapport |
|---|---|---|---|---|
| docs/etat-de-l-art-controle-ia-v1.md | 33 | venue « ICML 2025 » de 2502.03407 (Goldowsky-Dill et al.) | « ICML », « NeurIPS », « ICLR », « conference », « proceedings », « PMLR », « workshop », « accepted », « preprint », dans les 35 pages de la v1 et dans les métadonnées : aucune occurrence ; la v1 du 5 février 2025 n'imprime aucune venue | lot2-A2b (item 3.2, l. 184) |
| docs/etat-de-l-art-controle-ia-v1.md | 47 | venue « ACL 2026 » de 2605.27958 (Kumar) | « ACL », « EMNLP », « NAACL », « Proceedings », « conference », « workshop », « accepted », « submitted », « under review », dans les 18 pages : présents seulement dans la bibliographie ; le PDF ne porte que le tampon arXiv | lot2-A2b (item 2.3, l. 112) |
| docs/etat-de-l-art-controle-ia-v1.md | 91 | venue « ICLR 2026 » de 2510.09462 (Terekhov, Panfilov et al.) | « ICLR », « International Conference on Learning Representations », « Published as », « Under review », « conference », dans les 52 pages ; en-tête de la page 1 examiné sur image ; métadonnées sans venue ; seule attestation tierce : Hasan, 2604.13301v1, p. 8 | lot2-A4 (item 1.3, l. 57) |
| docs/etat-de-l-art-controle-ia-v1.md | 102 | chiffres du billet d'Anthropic de mars 2025 : « Claude 3.7 Sonnet » ramené « au niveau d'un modèle plus faible » ; précision des juges « d'environ 70 % à 20–35 % » | « 70 % », « 20–35 », « Claude 3.7 », « weaker model », dans les sept PDF du lot ; trois PDF citent le billet (Gasteiger et al. 2025, « Automated Researchers Can Subtly Sandbag ») sans en reproduire les chiffres ; source primaire non lue | lot2-A3 (n° 17, l. 219) |
| docs/etat-de-l-art-controle-ia-v1.md | 134 | venue « ICLR 2026 » de 2412.09565 (Bailey et al.) | « ICLR », « conference », « published », « under review », « proceedings », sur les 51 pages de la v2 (8 février 2025), qui n'imprime aucune venue ; attestation secondaire seulement, dans la bibliographie de 2602.15515v2, p. 10 | lot2-A2a (item 2.2, l. 95) |
| docs/etat-de-l-art-controle-ia-v1.md | 138 | chiffres de CaMeL : « attaques réussies quasi nulles sur AgentDojo », « utilité de 77 % contre 84 % », « environ 2,8 fois plus de tokens » | dans 2505.22852v1 : 77, 84, 2,8, « times », « tokens », « attack success », « AgentDojo » (divergence : 67 %, d'une référence erronée) ; dans 2601.09923v3 : 77, 84, 2,8, « tokens », « AgentDojo », annexe F des coûts (le 1,88× porte sur un autre cadre et « ne doit pas être substitué ») ; à vérifier sur le PDF de CaMeL lui-même (arXiv 2503.18813, version à préciser) | lot2-C3b (S3 n° 3, l. 148 ; S4 n° 5, l. 183 ; l. 156, 225) |

Autres éléments introuvables dans les documents du programme, qui ne sont ni des chiffres ni des venues (détail dans `corrections.md`) :
- programme v2, l. 59 : l'attribution « Koning & Grünwald » de 2208.07610 — « Koning » n'apparaît nulle part dans les 31 pages ; quatre auteurs : Pérez-Ortiz, Lardy, de Heide et Grünwald (lot1-lemme, l. 20, 39) ;
- état de l'art v1, l. 138 : « Google DeepMind » comme affiliation de CaMeL — introuvable dans 2505.22852v1 et 2601.09923v3 (seul indice : code officiel sous google-research) (lot2-C3b, l. 147, 182) ;
- état de l'art v1, l. 194 : le code de 2605.31593 — « github », « code (is/will) », « release », « available », « open source » cherchés dans les 17 pages : aucun lien ni annonce (lot2-B1, item 1.9, l. 60) ;
- brief v2, l. 133 : la licence de FakeLab (2607.07368) — « licen » cherché dans les 81 pages : seules occurrences dans la liste de contrôle NeurIPS, aucune licence de FakeLab (lot2-B1, item 3.12, l. 179).

## 2. Rapports de recherche affirmative

| document | ligne | chiffre ou venue | ce que les lecteurs ont cherché | rapport |
|---|---|---|---|---|
| docs/sources/recherche-affirmative-20261006/rapport-papier-A-v1.md | 75 | venue « ICLR 2025 » de 2411.17693 (Wen, Hebbar et al.) | « ICLR », « Conference on Learning » et toute mention de venue dans les 44 pages ; chaque page porte l'en-tête « Preprint » | lot3-Aa (n° 2, l. 128) |
| docs/sources/recherche-affirmative-20261006/rapport-papier-A-v1.md | 79 | version d'atelier NeurIPS 2024 « Sandbag Detection Through Model Impairment » de 2412.01784 | « workshop », « Impairment », « Sandbag Detection », dans la v3 (2 décembre 2025, NeurIPS 2025 selon le pied de page) | lot3-Ac (item 8.1, l. 127) |
| docs/sources/recherche-affirmative-20261006/rapport-papier-A-v1.md | 85 | billet d'Anthropic « SLEIGHT-Bench: Finding Blind Spots in AI Monitors » (titre et lieu de diffusion) | « Finding Blind » et « blog » dans les 42 pages de 2605.16626v2 : aucune page | lot3-Cd (SLEIGHT-Bench, 3 (A), l. 124) |
| docs/sources/recherche-affirmative-20261006/rapport-papier-A-v1.md | 119 | venue « ICLR 2026 » de 2508.19461 (Kale et al.) | « ICLR », « Conference on Learning », « under review », dans les 50 pages de la v1 : aucune occurrence ; version des actes non fournie | lot3-Ca (A.1, l. 129 ; l. 113) |
| docs/sources/recherche-affirmative-20261006/rapport-papiers-C-B-v1.md | 88 | « publié à ICLR 2026 » pour 2508.19461 | même recherche que ci-dessus | lot3-Ca (A4.1, l. 122 ; l. 113) |
| docs/sources/recherche-affirmative-20261006/rapport-papiers-C-B-v1.md | 91 | « Détection par activations au-dessus de 86 % sous obfuscation » (2608.19161) | `obfusc`, `evas`, `adaptiv`, `adversar`, `robust`, `86`, par expressions régulières sans tenir compte de la casse, sur les 12 pages : aucune occurrence ; aucune évaluation sous obfuscation (le plus proche : aire 0,854 en paires hétérogènes, sans obfuscation) | lot3-Be (A7-4, l. 33) |

Autres éléments des rapports de recherche affirmative, introuvables ou corrigés sans être des chiffres introuvables :
- rapport A, l. 84 : l'annonce d'une agrégation séquentielle des sondes ou d'une calibration de trajectoire par 2607.13087 — introuvable (« probe », « linear », « aggregat », « cumulat », « sequential », « calibrat », « false positive », « FPR », « threshold », « per-action », « per action », « trajectory-level ») (lot3-Ac, 13.8, l. 185) ;
- rapport A, l. 98 : la source 2607.24893 elle-même — non citée par 2607.11751 (« 24893 », « characteriz », « early detection ») et absente du dépôt (vérifié sur disque, R11) (lot3-Ab, B9, l. 177) ;
- chiffres présents mais mal situés, donc corrigés et non introuvables : « accepté à DAI 2026 » (rapport A, l. 72 : venue imprimée comme format de référence, acceptation non énoncée ; lot3-Aa) ; « Selon le résumé : 0,908 et 7,9 % » (rapport A, l. 73 : absents du résumé, présents p. 7 ; lot3-Ab) ; « jusqu'à 98,85 % » (rapport A, l. 82 : ligne SWiM et non SC-TopK ; lot3-Ab).

## Bilan

- Documents du programme : 6 lignes de chiffres ou de venues introuvables (4 venues, 2 groupes de chiffres), plus 4 éléments introuvables d'autre nature.
- Rapports de recherche affirmative : 6 lignes (4 venues ou versions, 1 billet, 1 chiffre), plus 2 éléments introuvables d'autre nature.
