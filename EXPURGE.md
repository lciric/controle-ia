# What this copy omits

Copy of the private repository `controle-ia` at commit `1ac93de794d94f8c1ab2297382d4aed5f537b659`, made for evaluators by `scripts/depot_expurge.py` (same commit). Third-party texts that the code does not need are omitted, together with an application to another funder, the working registers (`registres/`, which quote private messages) and the texts of another application. Their SHA-256 hashes remain (companion `.sha256` files, and the table below), so anyone holding the originals can check them. Before writing the copy, the script checked that no omitted file survives inside a kept archive (53 files in zip, tar or git bundle format, Word and NumPy files included, searched at any depth, by hash and by path).

`python -m controle_ia.scellement verifier-arbre .` reports each omitted sealed file as an orphan hash; that is expected. The README's paragraph on third-party material was adapted for this copy.

- Files kept: 2099. Files omitted: 263 (394.8 MB).
- Kept on purpose: the prompt texts transcribed from arXiv 2606.08892 (`docs/sources/invites-2606.08892-v1/invites/`) and from arXiv 2606.07054 (`docs/sources/invites-2606.07054-v1/invites/`), and the templates adapted from the latter (`docs/sources/invites-2606.07054-v1/derivees/`): the code and its tests load them after checking their hashes.

## arXiv papers whose PDF copies are omitted

- [2005.07821v1](https://arxiv.org/abs/2005.07821v1)
- [2208.07610v2](https://arxiv.org/abs/2208.07610v2)
- [2302.12173v2](https://arxiv.org/abs/2302.12173v2)
- [2309.17012v3](https://arxiv.org/abs/2309.17012v3)
- [2402.10669v5](https://arxiv.org/abs/2402.10669v5)
- [2402.14016v2](https://arxiv.org/abs/2402.14016v2)
- [2403.04957v1](https://arxiv.org/abs/2403.04957v1)
- [2403.17710v5](https://arxiv.org/abs/2403.17710v5)
- [2404.13076v1](https://arxiv.org/abs/2404.13076v1)
- [2405.05466v2](https://arxiv.org/abs/2405.05466v2)
- [2410.02736v2](https://arxiv.org/abs/2410.02736v2)
- [2410.14746v1](https://arxiv.org/abs/2410.14746v1)
- [2410.21514v1](https://arxiv.org/abs/2410.21514v1)
- [2410.21819v2](https://arxiv.org/abs/2410.21819v2)
- [2411.03336v2](https://arxiv.org/abs/2411.03336v2)
- [2411.17693v1](https://arxiv.org/abs/2411.17693v1)
- [2412.01784v3](https://arxiv.org/abs/2412.01784v3)
- [2412.09565v2](https://arxiv.org/abs/2412.09565v2)
- [2502.01534v3](https://arxiv.org/abs/2502.01534v3)
- [2502.03052v2](https://arxiv.org/abs/2502.03052v2)
- [2502.03407v1](https://arxiv.org/abs/2502.03407v1)
- [2503.11926v1](https://arxiv.org/abs/2503.11926v1)
- [2503.18813v2](https://arxiv.org/abs/2503.18813v2)
- [2504.05259v1](https://arxiv.org/abs/2504.05259v1)
- [2504.10374v1](https://arxiv.org/abs/2504.10374v1)
- [2504.18333v1](https://arxiv.org/abs/2504.18333v1)
- [2504.20271v1](https://arxiv.org/abs/2504.20271v1)
- [2505.06311v2](https://arxiv.org/abs/2505.06311v2)
- [2505.13348v1](https://arxiv.org/abs/2505.13348v1)
- [2505.22852v1](https://arxiv.org/abs/2505.22852v1)
- [2505.23575v3](https://arxiv.org/abs/2505.23575v3)
- [2506.10805v4](https://arxiv.org/abs/2506.10805v4)
- [2506.10949v2](https://arxiv.org/abs/2506.10949v2)
- [2506.14261v4](https://arxiv.org/abs/2506.14261v4)
- [2507.12691v3](https://arxiv.org/abs/2507.12691v3)
- [2508.05625v1](https://arxiv.org/abs/2508.05625v1)
- [2508.07805v1](https://arxiv.org/abs/2508.07805v1)
- [2508.09759v1](https://arxiv.org/abs/2508.09759v1)
- [2508.16846v6](https://arxiv.org/abs/2508.16846v6)
- [2508.19461v1](https://arxiv.org/abs/2508.19461v1)
- [2509.16533v1](https://arxiv.org/abs/2509.16533v1)
- [2509.21344v2](https://arxiv.org/abs/2509.21344v2)
- [2509.26072v2](https://arxiv.org/abs/2509.26072v2)
- [2509.26238v4](https://arxiv.org/abs/2509.26238v4)
- [2510.07192v1](https://arxiv.org/abs/2510.07192v1)
- [2510.09459v2](https://arxiv.org/abs/2510.09459v2)
- [2510.09462v2](https://arxiv.org/abs/2510.09462v2)
- [2511.00554v1](https://arxiv.org/abs/2511.00554v1)
- [2511.09904v2](https://arxiv.org/abs/2511.09904v2)
- [2511.17220v2](https://arxiv.org/abs/2511.17220v2)
- [2512.03109v2](https://arxiv.org/abs/2512.03109v2)
- [2512.07810v1](https://arxiv.org/abs/2512.07810v1)
- [2512.11949v1](https://arxiv.org/abs/2512.11949v1)
- [2601.09923v3](https://arxiv.org/abs/2601.09923v3)
- [2601.11516v4](https://arxiv.org/abs/2601.11516v4)
- [2601.13433v4](https://arxiv.org/abs/2601.13433v4)
- [2601.20022v2](https://arxiv.org/abs/2601.20022v2)
- [2602.14161v2](https://arxiv.org/abs/2602.14161v2)
- [2602.15222v1](https://arxiv.org/abs/2602.15222v1)
- [2602.15515v2](https://arxiv.org/abs/2602.15515v2)
- [2602.20628v2](https://arxiv.org/abs/2602.20628v2)
- [2602.22303v1](https://arxiv.org/abs/2602.22303v1)
- [2603.02798v1](https://arxiv.org/abs/2603.02798v1)
- [2603.12277v6](https://arxiv.org/abs/2603.12277v6)
- [2603.13791v1](https://arxiv.org/abs/2603.13791v1)
- [2603.15809v1](https://arxiv.org/abs/2603.15809v1)
- [2603.29403v2](https://arxiv.org/abs/2603.29403v2)
- [2604.01151v3](https://arxiv.org/abs/2604.01151v3)
- [2604.03968v1](https://arxiv.org/abs/2604.03968v1)
- [2604.13301v1](https://arxiv.org/abs/2604.13301v1)
- [2604.14865v1](https://arxiv.org/abs/2604.14865v1)
- [2604.16286v2](https://arxiv.org/abs/2604.16286v2)
- [2604.16824v1](https://arxiv.org/abs/2604.16824v1)
- [2604.19775v2](https://arxiv.org/abs/2604.19775v2)
- [2604.21564v2](https://arxiv.org/abs/2604.21564v2)
- [2604.22082v2](https://arxiv.org/abs/2604.22082v2)
- [2604.22888v1](https://arxiv.org/abs/2604.22888v1)
- [2604.28129v1](https://arxiv.org/abs/2604.28129v1)
- [2605.06455v2](https://arxiv.org/abs/2605.06455v2)
- [2605.09684v1](https://arxiv.org/abs/2605.09684v1)
- [2605.15377v2](https://arxiv.org/abs/2605.15377v2)
- [2605.16626v2](https://arxiv.org/abs/2605.16626v2)
- [2605.18549v1](https://arxiv.org/abs/2605.18549v1)
- [2605.18918v1](https://arxiv.org/abs/2605.18918v1)
- [2605.23970v1](https://arxiv.org/abs/2605.23970v1)
- [2605.26047v2](https://arxiv.org/abs/2605.26047v2)
- [2605.27690v2](https://arxiv.org/abs/2605.27690v2)
- [2605.27958v1](https://arxiv.org/abs/2605.27958v1)
- [2605.29178v1](https://arxiv.org/abs/2605.29178v1)
- [2605.31593v1](https://arxiv.org/abs/2605.31593v1)
- [2606.06223v2](https://arxiv.org/abs/2606.06223v2)
- [2606.07054v1](https://arxiv.org/abs/2606.07054v1)
- [2606.07612v1](https://arxiv.org/abs/2606.07612v1)
- [2606.07897v2](https://arxiv.org/abs/2606.07897v2)
- [2606.08892v2](https://arxiv.org/abs/2606.08892v2)
- [2606.09931v1](https://arxiv.org/abs/2606.09931v1)
- [2606.10456v2](https://arxiv.org/abs/2606.10456v2)
- [2606.14037v1](https://arxiv.org/abs/2606.14037v1)
- [2606.17478v1](https://arxiv.org/abs/2606.17478v1)
- [2606.18276v1](https://arxiv.org/abs/2606.18276v1)
- [2606.22864v1](https://arxiv.org/abs/2606.22864v1)
- [2607.02510v1](https://arxiv.org/abs/2607.02510v1)
- [2607.02514v2](https://arxiv.org/abs/2607.02514v2)
- [2607.06503v2](https://arxiv.org/abs/2607.06503v2)
- [2607.06596v3](https://arxiv.org/abs/2607.06596v3)
- [2607.06807v1](https://arxiv.org/abs/2607.06807v1)
- [2607.07368v1](https://arxiv.org/abs/2607.07368v1)
- [2607.08066v1](https://arxiv.org/abs/2607.08066v1)
- [2607.11751v1](https://arxiv.org/abs/2607.11751v1)
- [2607.13087v1](https://arxiv.org/abs/2607.13087v1)
- [2608.02657v2](https://arxiv.org/abs/2608.02657v2)
- [2608.02698v1](https://arxiv.org/abs/2608.02698v1)
- [2608.16190v1](https://arxiv.org/abs/2608.16190v1)
- [2608.19161v1](https://arxiv.org/abs/2608.19161v1)
- [2608.25869v1](https://arxiv.org/abs/2608.25869v1)
- [2609.03035v1](https://arxiv.org/abs/2609.03035v1)
- [2609.24967v2](https://arxiv.org/abs/2609.24967v2)
- [2609.36490v1](https://arxiv.org/abs/2609.36490v1)
- [2610.04575v1](https://arxiv.org/abs/2610.04575v1)

## Omitted files

| path | SHA-256 | reason (in French) |
|---|---|---|
| `docs/procedures/T0.5-extraction-v1/contre-lecture/fichiers-de-travail-contre-lecture-1-v1.tar` | `6a5520b43c59f9d72904d60a5866587bda357f61f928985bdfd84b8488502d78` | fichiers de travail des relecteurs de l'extraction |
| `docs/procedures/T0.5-extraction-v1/contre-lecture/fichiers-de-travail-contre-lecture-2-v1.tar` | `2d3e07db38496f22743008c5218eea06d8f1a87aad74e83ff9bc1926af10a27d` | fichiers de travail des relecteurs de l'extraction |
| `docs/procedures/T0.5-extraction-v1/contre-lecture/fichiers-de-travail-contre-lecture-3-v1.tar` | `8b0950a374fe08d5e4f0fcc34781d924e9d1ab54788227b775f1e15bcc11cd60` | fichiers de travail des relecteurs de l'extraction |
| `docs/procedures/T0.5-extraction-v1/contre-lecture/fichiers-de-travail-verification-4-v1.tar` | `b1eaa3ff7f25ca9bfaec9e164562cc885a70a3277f0e383764ffbd420081886c` | fichiers de travail des relecteurs de l'extraction |
| `docs/sources/cartes-modeles-20261006/huggingface-meta-llama-Llama-3.1-8B-Instruct.html` | `466678423ace08372a1a0d78e0cfa723c66b92efafe07d8f6b49bc33d33d0410` | page d'une carte de modèle (site tiers) |
| `docs/sources/cartes-modeles-20261006/huggingface-meta-llama-Llama-3.2-3B-Instruct.html` | `203accf5cfefe82a2e0f7c2502d094d3c9f2b3da5fe8b651f1317e8b89102774` | page d'une carte de modèle (site tiers) |
| `docs/sources/invites-2606.07054-v1/derivees/contre-verification-v1/fichiers-de-travail-differentiel-v1.tar` | `10af4c542e2fcbe1d3f6f85c8efd57d6432dff2ecf6fcf47a843743af5a26bfa` | fichiers de travail d'une contre-vérification : texte extrait d'un papier de tiers |
| `docs/sources/invites-2606.07054-v1/derivees/contre-verification-v1/fichiers-de-travail-v1.tar` | `49a6657c94bc7c16535bf626b12952e21eb5c741a158a1d88aaf34f48c6726cc` | fichiers de travail d'une contre-vérification : texte extrait d'un papier de tiers |
| `docs/sources/invites-2606.07054-v1/extrait.tar` | `80005a4068a79e9d8833afb46ceecb49bdbc0af10ec5db18fc0dd69e7a5c4b31` | texte extrait d'un papier de tiers |
| `docs/sources/invites-2606.08892-v1/extrait.tar` | `0717692754eb9d5a3fe8c011a36a929966201e75030ccea4cb37020349c315f5` | texte complet extrait d'un papier de tiers |
| `docs/sources/lecture-pdf-niveau1/fichiers-de-travail-2606.08892-v1.tar` | `cb9d3c820ee0ae379ea4ca145193d5bf235b5c68c266c120217d48a9f68c1cf8` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau1/fichiers-de-travail-2606.10456-v1.tar` | `6cfaaf848b0f14af563b894622fb3f45bee693aff706f7ef9176afcc18fc5bef` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau1/fichiers-de-travail-H2-voisins-v1.tar` | `591002de002896597700c13382317e509a8e2f3192af40e2dfc7d4602d4d47d0` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau1/fichiers-de-travail-controle-tracabilite-v1.tar` | `28a22c5debbd349dfdcbb2107539745e41f8e8e7cfd6cd23ba306909fb8489d5` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau1/fichiers-de-travail-papierB-NARCBench-Das-v1.tar` | `c97630233236caa9958356372bd83fe04d1453e676567e69e27d1b90cf50fca4` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau1/fichiers-de-travail-papierC-v1.tar` | `79f5bc2f7461c18069181b60d7c5f45369d649dab626e0abc8d4d9a44231db28` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-GC-reseaux-v1.tar` | `56b4639669e446f694f9189cae58ac03664afa7ecedb286fcfef750951f27cc3` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-H2-voisins-v1.tar` | `fd7cf4aa39a3d4a0c3ec87d4d05ea37900e84f81d0392cfcc0fea01b06ce5518` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-HC1-voisins-v1.tar` | `b5d2829d8ac6197c93abb5af0faac68edc967dca94233a47dfccca6cc6f5e8f1` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lemme-v1.tar` | `760829b29bfcdef4b3327b9698ff1216c12c7bcbbd7b0ed121534a13f866d0e4` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-A1-bases-sequentielles-v1.tar` | `566800d28d19e963f0fee7a061adeca9e251adef352f4770e453e1c8aea4056a` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-A2a-evasion-sondes-v1.tar` | `b420d3eaffc0b9ba07a31fb5dad44a904481c1c23f226366f07abd0dee878826` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-A2b-validite-sondes-v1.tar` | `fa57e8f3dbf8d3cee1436321f1df69cd86caa58cacb0da5cf007531aba602d92` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-A3-sabotage-recherche-v1.tar` | `130dab2b81594a8894ed8354d32ede39d095cd9b6db5dfe327144cfa36740b07` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-A4-protocoles-controle-v1.tar` | `a71bf67b8587af8caccbe65b5605dc0e2eb6c986570631e875ca802bafb1ab68` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-B1-multi-agents-v1.tar` | `b68221c7976a2db702e7922c884b04d0e57eeba30392653ab285ef0e8029dff2` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-C1a-juges-biais-v1.tar` | `f5fc72563968b2a46db0606a574f00d0e42b998d43565bf292a535bd8879538c` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-C1b-persuasion-v1.tar` | `99b19120b1d41ddbba521d098f46efc44814822479a68c8004c18afbfe512280` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-C2a-deplacement-juges-v1.tar` | `b812e5e6719184115d827f88f2991f00ac16410449c2abb10fa017e522184d50` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-C2b-suffixes-v1.tar` | `a75e5f0d52cd2ddc4d3a43ca4f822b07d1e97ed7549dc0bc7d314c3e763edad6` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-C3a-injection-etats-internes-v1.tar` | `33163891db94ac6b2b4f062549fe6a3bab5ba58ac978045b92a9e7a2ab245d3f` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot2-C3b-separation-controle-donnees-v1.tar` | `bebb445933e0b0ed166d1ea9835e1642ef532bd7386159945fc51b1c635327d8` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Aa-H2-trajectoire-v1.tar` | `d9b651acbd13d28516ca114d40ce84ec9edcb4c05e0d7658aa6f38f725a06b41` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Ab-accumulation-agregation-v1.tar` | `986e33ff7b60d561d585927ff25aab0d04e0454e895467a04af83c57a65e01cf` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Ac-blanc-noir-interventions-feuille-v1.tar` | `20d7d7dacf8a88b192686d75a38e8d380a99a2edcff63ededc6b6be4b67959e3` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Be-essaim-auto-signalement-v1.tar` | `04b92af7462671924198f3cba0b6d4f4bdae8c5c4b94297a06af3a88901d3de1` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Ca-juges-ancrage-v1.tar` | `cc32f36844235bc906afdc14d95ec374be9e067a90e5b0e2ad3309a929fee34b` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Cb-sondes-texte-persuasion-v1.tar` | `923eb95b3f099ac9391167a2abfdbc5ea59e0f91bed71f1446057e8d498ec3a9` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Cc-evasion-quorum-v1.tar` | `de8890e8c3bbefcb49ee1a1fd04423482731bc577ee83ecd7997b0e7a41d1bc7` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot3-Cd-bancs-attaque-v1.tar` | `e498077f6968d588ab11605b753983420c80742a95e94c47bd76ec53bab6e8da` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot5-camel-et-pistes-v1.tar` | `46ed47fca68ffc2e61d69a61f11acd75011bbd1f78f779915654a16a8a0ec69f` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-lot6-pistes-v1.tar` | `7bc5777416255fb21adaf7e0852a4a3b4092a2231b499f7fac768bfc7d218533` | fichiers de travail d'un lecteur : pages extraites des PDF de tiers |
| `docs/sources/pdf/2005.07821v1.pdf` | `e1532df64652fa114c7ebda2f9111e6547750537509f5ecd2d7d1d214eb53c14` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2208.07610v2.pdf` | `e9e5fd4e0096e3be7e7b07d083fd73818791feafd69a65676c289c0f63db6223` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2302.12173v2.pdf` | `428e23e8c7e4f89310e113e38d082b3f65548a8b887188ebc536099061800e81` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2309.17012v3.pdf` | `8dc98f733b0318aa31acb5b5df36131e835b87e2183579d6c0c51a64f81259b5` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2402.10669v5.pdf` | `47ae7d76edd51093525fd0a868987b626e46f891f065607b568057439de8b41f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2402.14016v2.pdf` | `d10f97ce404e460004a35cd0ca4093f7bbd547230986280be1f5f4460fac9b12` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2403.04957v1.pdf` | `c7cca74230ac03c1f10b39c287e84b0b51ccfbfb89f3daa369583f91be4fc6ba` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2403.17710v5.pdf` | `7bea71368aec667cdbae6d096ff39a18ca11f7c39d53cab65f999771d7869cc3` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2404.13076v1.pdf` | `e1466f5ade6144599fda01deafdd737b4623eaae273d71e4a0099d55b33189d3` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2405.05466v2.pdf` | `aa781893236e877a8f63e22249e77f454c8df6e2d82018fff3ca99456ad782c4` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2410.02736v2.pdf` | `d67bb6157df77fadb8e64187fbb81f1a2d4b85dfe89135b30b81b3439e6ad579` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2410.14746v1.pdf` | `179c42fb5a26ee7bffcc5448937de67f1aad30366710695f13ce9c0b96d56ba8` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2410.21514v1.pdf` | `67f35893f1ebacb83407db92caf44c9b86d24da222ea5caee3f23184949cbb4f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2410.21819v2.pdf` | `d1e6b1c9cceb62f095d99c36da314d8e3d4302573e6226b56f101ab120af7f0d` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2411.03336v2.pdf` | `46b4901a0f0c2a63ae90247b611b619fc9ca22d4129bdfdf5608e9148c4bca7e` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2411.17693v1.pdf` | `13a93a48dcb373595709da1096984d308cd3cd17c3bf00602944a24abcc2c627` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2412.01784v3.pdf` | `7fbe44ec6d764951f76d94f8d52cfcb7db89f1a130526462c46afc3f626d11a2` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2412.09565v2.pdf` | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2502.01534v3.pdf` | `f1204432f553296541ad2bd97b2f557b40c5235e2adc2d13810e618ffb2116c3` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2502.03052v2.pdf` | `a32e75e21540af2648782ce14c371863cb572fa2b4b39df389035483a8384a90` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2502.03407v1.pdf` | `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2503.11926v1.pdf` | `2547162c549d70e02beca2687903a8fce75fd950269a3ee479d5b8ebbb53ff38` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2503.18813v2.pdf` | `c3719f6ce73eecf45e3764debef8a3d8ff8c9233b37d128c558b694ec3790cc7` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2504.05259v1.pdf` | `6c433161e5d3bfdf85ddd262083e711e5ff7d0c2b3d232f1ecd35c94e7130a24` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2504.10374v1.pdf` | `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2504.18333v1.pdf` | `96d398709fcb5ff38bb2568249f7a68997b0bac96e1afc7f0b72bf0e63038df7` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2504.20271v1.pdf` | `a496a833574e00b8a62fe382a32e37f9a91cd58ba66a5a7744759609ac9d222a` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2505.06311v2.pdf` | `dc3e7d954f9eb6144b5cb9505aeb9683d37eacc500e6fe4a69a170fd1ba558ba` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2505.13348v1.pdf` | `980c51a243fc8f94f80faed83e1c84784d4193a497966731919fd11286209714` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2505.22852v1.pdf` | `640fa777c59491256c02059f385c117a7b0d2c346ceb075dfca24d9a146f77e8` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2505.23575v3.pdf` | `04c44d4ac7c4d2c145609324994cb2f58e1c10f65874ee3a5622541a631996e1` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2506.10805v4.pdf` | `54bf555501b831d2505b05a0104d59cc0ab46dbb55516e6c0b7548e11db2b7d6` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2506.10949v2.pdf` | `ce51b7f5e263e2a78cb934b4d7cc135ba18335b713fe0b716f781738d67ead66` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2506.14261v4.pdf` | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2507.12691v3.pdf` | `0c00a77b0c07bb9a8cd2feb748d65fe9ac01ee7bee9746ebb9cbc0d1ca8ebb00` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2508.05625v1.pdf` | `c7629e20810194a8df90ba0781bcf87082e50aef5088f39a98e88c51a4c3ea72` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2508.07805v1.pdf` | `4cc15dcde9a22a797718c28fc47f8ef7da4e344624885cd4bc7a4ad0fd3a8a2f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2508.09759v1.pdf` | `11e49565e0e8e0a96f2f606c97d5c78fe3cffd3687c71ecbcde8783612584c7b` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2508.16846v6.pdf` | `8fc54c534171bc4e734e93d23baf4e8146d44264d74464e7915bf46393a271e9` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2508.19461v1.pdf` | `24365928b67324f9f16123637ff88a8857594621903b0f14d412f8eb113e740a` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2509.16533v1.pdf` | `b08468d81268b6705dd99c8e2ce76ba1ad0d6487494ddc84b2aa3a5008cc33d4` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2509.21344v2.pdf` | `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2509.26072v2.pdf` | `c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2509.26238v4.pdf` | `7cd297e7eb2500980caa23d88410a20f0d6c10b90e787b28070afa14e891a962` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2510.07192v1.pdf` | `8b8c5e05deedff10c93be7d49555d9c41028e18bc902dad428da759ad3358f5a` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2510.09459v2.pdf` | `df815e61dc535ff248b020b151c7b94d7921fa8cca21e5041899a7a165e8a597` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2510.09462v2.pdf` | `96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2511.00554v1.pdf` | `17708292f357ddeea469f1157c1ab72c77471b70293d17c2f00409b11aabc75f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2511.09904v2.pdf` | `afff193dcf3dd1384e70939c5b2c6277e8c9255b79fefd0643485de2a7e3c396` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2511.17220v2.pdf` | `65524c725e837c4a9ed95506eefb3641a799265f7f5407c19b9752cfc7286b45` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2512.03109v2.pdf` | `b7a46e4cf781aec0c5730196b9f6a2ea1e42c3ec63f1e5260dff223dfafe3828` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2512.07810v1.pdf` | `77e64bcd88754f506890ee99dc5672284145a8705d27c5a63e4fc47330d28c8f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2512.11949v1.pdf` | `e0f8ddfff6e75d835995886a630a5d077ed871c28599f710b41c96efc949e3ee` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2601.09923v3.pdf` | `ca9b8cc895d22590f1e9fe031b5eac52c3bd22a1ab3aadc2034c4bcd0adedca1` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2601.11516v4.pdf` | `c4a36db54c9d679a718a0e35b9cad09fa628d81f6174bb6e1d8c6b26a063d8bf` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2601.13433v4.pdf` | `e4991aa9e346cbb536fc6c03817138b56fea77ed8379dc62f3cad0eaedef877f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2601.20022v2.pdf` | `8d090f3171ef76cad597ab263a2de9df49de1d1accf78a8afff55ceb82881b42` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2602.14161v2.pdf` | `7831c848841eca32bcbb1e18cd35f644cfe5a8af8f0f003623c4e1bdd6e03c00` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2602.15222v1.pdf` | `e516b3fc78ece6ffc6383edfa6ceb2ee6e025cafb2efd4fed67716d78c7bcde9` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2602.15515v2.pdf` | `f6547ec830104abf8ceca353e46e32ee78453f6470fd1c03053e13834ebc54cb` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2602.20628v2.pdf` | `b7d4663ace86c1cf9f730509c39ef0138022ccf4b72ae7242892b3a7e5f9d0bf` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2602.22303v1.pdf` | `739ee7747236c1886131b6e33cc2f6833d3d7eb99b34f34732d79dc61aebaccc` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2603.02798v1.pdf` | `1ee9bf721494de9ef78cb06ef396583de90cef8bb8093b18e6d8b9c71e291ff6` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2603.12277v6.pdf` | `609332fdfaae35838e5c82c0ef9a9b7d23aac7ac24000452917c47a56d4f29e0` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2603.13791v1.pdf` | `0b2b155024d67bae9fa3f46044b978b3e9a76eec717a6e9171feeeeb1f114308` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2603.15809v1.pdf` | `29316c29e444175fe1436aad6773a1d44b422d693db8eb10b2e7538c70d53529` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2603.29403v2.pdf` | `7141fad8e02f81bd4e09fec1c810a549e80892db8bc10211a8082b060153f2d2` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.01151v3.pdf` | `bde99a620dbbb4064fcfd9a010ac4e92b17b619c5995ae0696911afdbed7686b` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.03968v1.pdf` | `eb49aa426debb55164675881d6af91c26e438e408d460f2d28428c022e9c1c27` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.13301v1.pdf` | `fc09ad6f0202284a8e99009252da573274393c69fcc22b9022ba8fdd07ef5cd3` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.14865v1.pdf` | `4ff711e178125b20ea8749d052d7598b7a4644ae6a7fd04f79979afb7680f5f9` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.16286v2.pdf` | `833a48e6c63b0e1b36af9d7e1952878752379115c49f72bc2c9e3e7af3161cc0` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.16824v1.pdf` | `ad860956062a13a0a236d12b861c83bef08242ff69304efcadc7220f77f4b74d` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.19775v2.pdf` | `f3abefb4be525c80df9bdf78992ba4f7591819db22952e21b57438069cfd37ac` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.21564v2.pdf` | `c2a2f1e28e258628c775de38cf424a571f42747764c0c232c160b386247cf3b3` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.22082v2.pdf` | `f27f3c399084f2abf8127969ac10a9ed3a4c5b859f5c23048b488d9872da3c05` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.22888v1.pdf` | `9b840e2ac022ed5d2a6e81f397daf390a1c013f1cc10c078885604ef974f82bb` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2604.28129v1.pdf` | `f656c9b7e7fbd5d6c70555f825f67cd89b08b0fa746ec0efa895dd64e0f81cb5` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.06455v2.pdf` | `4a7533a04ae0c41d1d6ee1b66aa90ab7bbbf5099bf38193f9fdaf61a54477e6c` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.09684v1.pdf` | `35bb09b49f85578e4cfddeec16c9ae101a51b5d618196a4b29a1722b89b831f5` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.15377v2.pdf` | `fe591700228b29dc3287130efe6f877c5eeada84169dcbf1e526f6dc2e401712` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.16626v2.pdf` | `1ba418227095eeea98881f61a606c9974f4f3a8758d6a6292c6a9cd8bbd76751` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.18549v1.pdf` | `fe2e3a6936199a59adb440d026a2f6988361fdf8b21670669c33f475f25e0b0a` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.18918v1.pdf` | `b808b44783e4864f0bb0e1b3e68772ec97547683c72a0df14352f68b0580b5a2` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.23970v1.pdf` | `42867a39af4afd2a8c29d2bc8e023cb9df69924f7cac6de7f12b2e2487a39a1a` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.26047v2.pdf` | `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.27690v2.pdf` | `ebcbb371a78f3d4a5d3fe0db4c1eb87e8e4883e49e5785277bd612fe00b6abe4` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.27958v1.pdf` | `43f55118822b378d950255b10aa68379fdb24a1431bba7e8721aacaf44d856e0` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.29178v1.pdf` | `85f27b4c7aa7d606e0c12cd2094b0c3b45378a75f4750a99e947707082dfe477` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2605.31593v1.pdf` | `037f653703ec0da12dfaaf83a50d576355e7ac19985cd109426a90567eb8b0f0` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.06223v2.pdf` | `a95da1d590044f0ac7a5b7f707186b1241aece0e3546d0fb924d8ec355e562c3` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.07054v1.pdf` | `9e169bb5eced6fb2079c14804efcda54ad5e4a4ab9392b6c3b148c4ea6405fee` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.07612v1.pdf` | `3cc173e5688dbd88d51e091cb9bafcaabe62e2a87349ae67f3aa27223b0ff7d1` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.07897v2.pdf` | `e025464dba714bb5406222bca2a55447cea3e1272ed50bf8819890cc7a02f844` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.08892v2.pdf` | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.09931v1.pdf` | `538e8488bdcc09fcb1d58ff5c88f101d6da0232c73b095aa6e6519e3f3c19232` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.10456v2.pdf` | `aaeedd1e7a88203e47bf4400829dc4fdaa49eeb35bfb0da0cf999e2a7a3b2ba2` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.14037v1.pdf` | `682a2dad52698d06ecf1aa6515e90f5264b02c6fe7b97fe09d7672d1a4d533ac` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.17478v1.pdf` | `deda43a6f6bafe307ac50323169ed47e118802045a25a925819250e9dab56221` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.18276v1.pdf` | `8332adc89c0d75f89aaa3b94584a9f7a85a9301a2dfe12b2b2adaa47c349a44b` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2606.22864v1.pdf` | `f81c73e22f301541c96a94aa7e5e33f00734af5d80b9acc0ec0712d91046102f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.02510v1.pdf` | `eefdaeaec17c3b1683b0398d2bfd8aced1d7e9a342870172982e5c0b4ac2ebb1` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.02514v2.pdf` | `9baceea4719a5ff2d63c3278d425a0c3b9feeb2d447a19a3cd7a6b62d3339c22` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.06503v2.pdf` | `ae2a2d307373c145392fa7381d9d0523b37c4b5b3a85b9c7b460e89e0e1408fc` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.06596v3.pdf` | `63181efe25f4115bdb8652aad12f6bdeade2f9e27f3c61811161e9278b885c8e` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.06807v1.pdf` | `bf5093088fa8a3f6d167a63b0430b44e2d7a2864de52561867e58b0531968a67` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.07368v1.pdf` | `d72cae4337e824e4af9eb84759775f6c5dc704f157a0d302df1b44538eb159cd` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.08066v1.pdf` | `f22075f04c845a5062e51bfe8ee56150a3cad92eaef0bc2ed2c0e42ada2269a9` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.11751v1.pdf` | `eef30ef62b965b954d871d873f4d5920ed4482823b84b2204cabe41ac66b97f1` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2607.13087v1.pdf` | `291a0cd72b0b6a0f08882db7080bba9f8a24ee196ae2f69f5063314cbfddeb55` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2608.02657v2.pdf` | `415e1b9b26a6d218b6a6219d84a7ab1549e1ae8f74d953a9254a68c42dd6b14d` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2608.02698v1.pdf` | `452ae117a6814f004e65e161606dba52ae73bf645c1b5e49f7788c4df58531ce` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2608.16190v1.pdf` | `8fdb6141aac64fe6bf9f741336befe58b255e8588294d11ca708c6e8a2c857f5` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2608.19161v1.pdf` | `c094ebf48b9e3bde1547daa101d475d74e8cc279ab02b834cccdcdba0a99879f` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2608.25869v1.pdf` | `f54d19a56474a4821b8e66df88e71bcb0d012e950363cdc38bdff6d468100599` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2609.03035v1.pdf` | `5092b602b687f8efb76ede8983794e6686a82b139bdc7bcb04bc43fd8d56090d` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2609.24967v2.pdf` | `95127141d5d92c720d5e95b7cd151b72e3a760b3283b5681f9fc1c4676d5d37b` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2609.36490v1.pdf` | `eb6d5bbe9bfaff0ac4fbac948a7bd9937721721fc558655fdf606d254421a088` | copie d'un PDF d'arXiv de tiers |
| `docs/sources/pdf/2610.04575v1.pdf` | `ef50ec541464c3ee8e3f2fda9251684668238377575b2530341319f474dce12c` | copie d'un PDF d'arXiv de tiers |
| `donnees/20261007-082440-t05-extraction/details-validation-tentative-1.json` | `0082c3d59bd3ee46694e05b99f4017327948dd8316524e254b657804e1ae1cfb` | sortie de l'extraction : texte dérivé de papiers de tiers |
| `donnees/20261007-082440-t05-extraction/details-validation-tentative-1.json.sha256` | `622a3c69d28fe10c29a9006e8a28d75078193353434669e79d0542caa567b3a6` | sortie de l'extraction : texte dérivé de papiers de tiers |
| `donnees/20261007-082440-t05-extraction/retours-tentative-1.json` | `112c270747d0da24561a6428b5f4ce365dbce7c29302cf647668109228847094` | sortie de l'extraction : texte dérivé de papiers de tiers |
| `donnees/20261007-082440-t05-extraction/sorties-tentative-1.tar` | `aad99ad785744250c0ccfa81c7e44c4e987e2e5271addfabc663ef70eecbfe67` | sortie de l'extraction : texte dérivé de papiers de tiers |
| `donnees/20261007-082440-t05-extraction/sorties-tentative-1.tar.sha256` | `aaf701e6af469538c0164670ffce949936403c6eaf5de8c72f6bc0b7a2e020d2` | sortie de l'extraction : texte dérivé de papiers de tiers |
| `livrables/anteriorite-niveau1-v1.zip` | `c3f66df0452951b05ac9a1513a8a4db97db1330814e325020bee9f45d520c182` | archive qui contient les registres de travail (R-116) |
| `livrables/anteriorite-niveau1-v1/decisions-v2.md` | `ad9aad4afe330675cd326d0c15c1fc1dc6755e0fc2e495f702add46ed1392900` | copie du registre des décisions (R-116) |
| `livrables/candidature-ea-funds-v1.zip` | `8811d9c7ea91dea5e642066e677b043f74b1d8695a9310976a13168482cd6b2b` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1.zip.sha256` | `d0b74a8794e84d62636ef142a8895d949ee4d41a8edd57dc936b6c315c7743b0` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v1.csv` | `f42cf79b7ddb299627c07c6375f800d9aa3b76d90eccfc6fb6829431859c0c50` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v1.csv.sha256` | `01e3ea54312a95a83348cc9dc3ab3f561fff3ab73620536a1dd7f2bee07c23f6` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v1.md` | `08bc74c33f469947ae106d851746d37f477fa5206bd8683a162b28eccf654643` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v1.md.sha256` | `c4a679e12d5d0dd7ebc20b9aea1468a36fa36813133e6c2355980eb3b80853b7` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v2.csv` | `02a7ee2e0e85190dd07e5a223e5fde0387b5dad1cd8ea2d733bb194d2e45692f` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v2.csv.sha256` | `d20c09e63f8904a84e2ad0e42c347d305d60672a8f2b3f3f9dc2226ad9905dc8` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v2.md` | `c5be140254367f34f9e7c88f2f0a10768cc13b305dd5eda4ef511800f4072271` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/budget-v2.md.sha256` | `d209ecfc712f09cdaa92ffaee4484a72b6b290ccd9ce0c9ae3e016e303afd200` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/candidature-v1.md` | `5df54a2731d19c5e9a35237c58f7f8e954350600fded0e53fac8acd85d29a960` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/candidature-v1.md.sha256` | `f280fc4839b222b9299f1db41ed24cbfc54d0a47cdab4af36ce2072ab8bdb356` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/candidature-v2.md` | `dbe24ac05bb17474f1f5e039ba43dae30e7e06729a2380d7c384172fe328f638` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/candidature-v2.md.sha256` | `329888bfac5eb20d5e36ea72c60838476e0064405091dc6b821451deb3ba6e46` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.css` | `10ed0d2f4734128e136855c42e5e491cb8908ea19194ff2cb5fda4bb851d76af` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.css.sha256` | `ae45cf271ded963f68f7882a3eec5a6c8acabae72605ffc46627d7a32082bcd4` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.docx` | `62f19f7b91a82fa1de6bfeaf08b984a4a827d342a58a3eca4bc0630d694d4759` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.docx.sha256` | `7bf472af51dbabc825f65ae97212799016d8f99ebcef8f03023ec220a089187f` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.md` | `2f1e0864110f5f747347da40c9e9f89174119de5a3a14875b0371ae78c57e2c7` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.md.sha256` | `86447669d1f25015f5c5b1e0c45ae6b0fc1e3de99b5a4f4fe5107f0ca2322ef1` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.pdf` | `35226dfdf7bf1e36931a3b9ca9a056c5b69fce0a5e1b36b127d8eb883efccb36` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/proposal-v1.pdf.sha256` | `acb7bc438d3cae258921712d03ae2c1aeb57529c73f0d7435141f9b17c5b795a` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/relecture-proposal-v1.md` | `60c37fc9574be30c3ad5f2e524cf7ec9395572b7af12f88aeae5ff3409350cbe` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/relecture-proposal-v1.md.sha256` | `aeaa81cf882fce8b729b30d88a122c6ef758fe9861a5511a6938b02f70d38220` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/tracabilite-proposal-v1.md` | `3dfe04ec279ff5c4aa08a9f3879d292b9c910f25a59ac6e6e51db069cccea8ed` | candidature à un autre fonds, confidentielle |
| `livrables/candidature-ea-funds-v1/tracabilite-proposal-v1.md.sha256` | `9a061187b51f278c095b1d1f70806009e128a24ca4abbd015d6eb4634b3ea633` | candidature à un autre fonds, confidentielle |
| `livrables/controle-ia-v1.bundle` | `66d72be4739f3d93ed716ac5e4f028a328afe66c97a57141d827a784b35fafb5` | paquet git qui contient les registres de travail (R-116) |
| `livrables/premier-rendu-v1.zip` | `e35bf97b992298b13b7fbfc4e93c3c2ef482c888cd4cdea12b12df6f32e67d35` | archive qui contient les registres de travail (R-116) |
| `livrables/premier-rendu-v1/decisions-v1.md` | `2191f7fbd5803a4f1dac9dfafd4b3881e157b1dd96d74af6f628a574e1bf8ea8` | copie du registre des décisions (R-116) |
| `livrables/reponse-amitie-v1.zip` | `b58c1333c0145e8329d5526debf7091da9d4fc851145162c3c86baf92bd55c40` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1.zip.sha256` | `03119a5c2306839ef3cc2c4bf804c192f555d21641d64106fe448719aa66d4ac` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/LISEZMOI-v1.md` | `2962fcd549390f959dd169a1e2ef4829a3ba660dfb57b1e8826f4590ea82829b` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/LISEZMOI-v1.md.sha256` | `ab5aab63374df15a48748cd531822cb5faf46a72fe78447e3153f30a89e3c168` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/fiche-argument-amitie-v2.md` | `d84a5f912ca7bf0624464b1181f32efcdeafbae53015c0bfb5ab70915d1cf792` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/fiche-argument-amitie-v2.md.sha256` | `5c3da744d4d4f88599b579a3d2f3d0af421702aece7eec61cdeee4fd4eea399b` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/fusion-v1.md` | `edd42491933aec7382f5296a2cfd4774e013751b049afc9cbf2ca52e3625d3d0` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/fusion-v1.md.sha256` | `989b64b37252052d331f9c116e46363fbfe2a506412def27b3fa78a2d3baea01` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/reponse-amitie-en-v1.md` | `d8faa9c74ae626887c925035efefd7d96d08883e843a33f653f7b254a5606e83` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/reponse-amitie-en-v1.md.sha256` | `1769d78153ee001e7fdc41b79fff3121c256a4ff7f11503f1d8e40a9d2562c8a` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/reponse-amitie-en-v2-essai.md` | `f333f51ecee93190d2aa6cae3219f5ca99acffd749c9f4f8762d2a352107b2a9` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/reponse-amitie-en-v2-essai.md.sha256` | `6a5ebdf87f82338641165555e45c52089ba761046d4abb0a3ac956ae2e659a42` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/reponse-amitie-fr-v1.md` | `543496ca0eb01577f3ef85d5d118017ab1f8f7c24606fe9197a37cde41abcd75` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/reponse-amitie-fr-v1.md.sha256` | `71d6be2b0bb2c3120d40955e063c11e978a458eb838873ac9e4c340c7196c194` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/version-lazar-recue-v1.md` | `50a05a9a6f6fcdbe36275a113a08727d95c4e42093ecb19463916a9dc21823a8` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `livrables/reponse-amitie-v1/version-lazar-recue-v1.md.sha256` | `59c89de06d7c287fdf92ad27437fed3ca15fa82cf67e3c8d63a76de720a97e55` | textes d'une candidature (séminaire AFFINE), privés (R-116) |
| `prereg/contre-lectures/T0.5-pilote-contre-lecture-1-verifications-v1.tar` | `a9738d5ab5d671f1e5fc3e75ff805edac2663484692487391754efb455dc5640` | fichiers de travail d'un relecteur : pages extraites d'un PDF de tiers |
| `registres/arrets.md` | `2f7da299264d5c33f6c3ead5ab426ca0ce29b2548510aa7465be54d640bd244d` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/decisions.md` | `fd96fa167d120fa50fbad12055ebef6e569ba4eaf5b5c09fba211bedb6cf9510` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/depenses.md` | `f5dc9bc2834325bf88e37f94b00463507d9f4765174ed3bce3c020715a3db850` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/etat.md` | `3bf8cf3f59e97cb152faaaa1f1f83cd2519652dfbfe5c08491ab8d0a03caceef` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/go.md` | `1cd03cf1a3eb920204785b02c28d5c18447c3477baa51f07c676fc8c1bcdd7fd` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/.gitkeep` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-0346.md` | `bb367c23d3e06444f877e2601cf5c74f5e725e7b7163199a76ca60fc37fda71f` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-0346.md.sha256` | `b39a986f04fc4c304fef1d051dfd07bdfb2c5b3f3b22e18696b5a19774dfdff9` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-0820.md` | `f6e0582917146179cf8c584a579cfb557bf1f9c5ae36e72ed9472509beafe820` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-0820.md.sha256` | `cf1a4c4d7f7ac8b8a2cffdd03fa1efc5667e3e35f70654620ec0b063a4abb0a5` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-1044.md` | `7808f942479f989fdf7abc48350948d8728817398130875a0025e4c939de41fe` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-1044.md.sha256` | `056cd7a729f3e05a092d49364918d760da9de9e87a96f47fecc2e182a1aea8a9` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-1647.md` | `0da566884f6180a2115f6451cec98446a775b4a89497d45b1b77ba37326598ad` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-1647.md.sha256` | `a8268aed9a91671fd78b4263e3372fe90910c2bebcea53309460341a296f6dc3` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-1818.md` | `53ec581a61257a038dfcdb705bc85da08d31a751f6f3c65bda472e9d8e30ebc6` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-04-1818.md.sha256` | `de430d607999b2d66bfbc4afb78e3531acc7be04f2f45f8fd988255d63b32cdd` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-0833.md` | `d15671209510e387ca47d4db2bf179e9d6cec7dde4f40e50e11e0d53d0bcabe0` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-0833.md.sha256` | `d6f3bf2ce6863116bf65d5322781aeb26f7a7cbe31b0a33c7cf057dcfe8baf3f` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-1101.md` | `d8e365e21c859814120325c0aba863307d7af98080bf8b1acccca8f76b983728` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-1101.md.sha256` | `43dd04b0243d0de7e1dced1ccac668841e4fabe73cb50ba4304be3cf7bf985ed` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-1250.md` | `803e9641de18b591a282b2f7530b8552cfe321ebb83d970e79f73d99b461f4be` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-1250.md.sha256` | `274ece4d81ceb643abd7d00bba79fc47df173f05539297b13363e801b6b635de` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-1535.md` | `4ebd3ea0ff9275d13c47e78b3cc7992e74652e534a53dbcf64b773bfd106bc07` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-05-1535.md.sha256` | `c7a777dfd5c0a33f10f53d6c2c3d1d536b68172cbf8f1c88c0f6fb46bded7ba6` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1249.md` | `36cced89ec7a1c6428afbd24642c988cf9a49be6b2ee94e836440a9a0df0cdcb` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1249.md.sha256` | `0187dc96a3fd594da7ed5e7023396fb3def8952c99238ed08cf04c18101ef466` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1415.md` | `dbcf952b975cbb262e335ad206d43cfdf255b316c6588ec7d3f0a2b5f766003a` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1415.md.sha256` | `780b2944b6b533fd84cadd4a00824b727bb8ff1b2e62b0a797f520e5eef195b3` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1725.md` | `8dfe420273136e90a2350446c35c150600a3dc32f69684b61f973e7ad06aec73` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1725.md.sha256` | `1d243840d84dd9a5b39e6eddcdf2ed8be11f1462fb391c873c851d1a1859b11e` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1840.md` | `7c67f6648b4e5127b0d25e0252922a3bfbb06da2b2c63c9c05925447de4e1257` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-1840.md.sha256` | `22341747c952863e61390ba1feb225052b930ad4bfde5fced661e7c19170da41` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-2013.md` | `ac2ce1e123024af3e774f0bc43d198ad349f4d03a0ef07a0e04871b51ef6b56e` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-06-2013.md.sha256` | `53f04d1455caebb8feb86f1d521ec3f356124ab233ae2463bb09dfd0186ed6bb` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-0802.md` | `2ad43362cf4ec61cb55e9e847f330e92ed28b346e192efd2d4004794a3e17a44` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-0802.md.sha256` | `cc75708abc1173007fcdb997eb8315d2db52715a9a2ea722b47c8b79560954b3` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-1122.md` | `e938ed08d8c70aec5ef4060566033dd5071f0dcabc9b7af3cdedd1573e90042f` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-1122.md.sha256` | `efeb2cbabce4dcc2cc84ff02c83aa788214d84437a561e342762a81856102cce` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-1405.md` | `d8e478fc9d8b98e09514720fb834a79685de982c1638901248b068fec9b37ed4` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-1405.md.sha256` | `1294c9ef8c90c29ecf1796f200f667746a3618a78df4b45ed994efe1f640bc69` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-1613.md` | `dd11b3689c84560bee17b5a73e93d4d985a78989262548cf3ec4eebf2baeb6bf` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-07-1613.md.sha256` | `a32b5de557da561d3893bf1738969af69655f7e9802a7c196417afd5bade3b99` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-08-0310.md` | `77748a64335ec1f139224b927ac38dd6124681f2c628b392c77d995aa12919a8` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-08-0310.md.sha256` | `e07469ef978f5a8b6d3ed2206e91ef3fadd26dfbfcbe5bac765b400d431ad7f2` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-08-2350.md` | `8f583cd14df4e96666dfc4de1f2d6821de530d571d1b302d15db145111c16424` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-08-2350.md.sha256` | `91c115ff614d829939251fda40443c923087080bf2bd7bee423acb21359f4443` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-09-0742.md` | `8fe9f3bf637cf305b3dd2ba14516104070835ca08ccb849d2bbaad98840e65b6` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/passations/2026-10-09-0742.md.sha256` | `5d602e707414adac966b0ac161392a9c9d26e18c2c07ef443ec0c1529a7a8c88` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
| `registres/veille.md` | `336da8badc562720eb901716351e363f0edf698535f1fd2c7eb0f99c79adfc83` | registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116) |
