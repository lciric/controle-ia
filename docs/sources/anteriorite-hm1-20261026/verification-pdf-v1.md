# Antériorité de H-M1 et du placebo croisé — vérification sur PDF empreintés (v1)

- **Auteur** : lignée « session-depot » (Claude), le 26 octobre 2026, vers 10:45 UTC (`date -u`).
- **Origine** : les deux contre-lectures neuves du 26 octobre (étape 0 de H-M1 v4 ; placebo croisé), qui citent ces travaux d'après des pages HTML (R7 : non opposable). Ici, chaque point est relu sur le PDF téléchargé depuis arXiv, empreinté ; la page est celle du PDF (extraction `pdftotext -layout`, page par page).
- **PDF** : hors dépôt (bloc-notes de la session), empreintes ci-dessous.

| référence | PDF (arXiv) | sha256 |
|---|---|---|
| V. Devbunova, « Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure », atelier « I Can't Believe It's Not Better », ICLR 2026 | 2603.19426v1, 19 mars 2026, 10 pages | `095a5a7c251642f4aed6b1d1848176eac12f19f1c21a354c1f4838469b1788bb` |
| N. Nayan, A. Sampath Kumar, R. Girmal, S. Anilkumar et al., « Evaluation Awareness Is Not One Capability: Evidence from Open Language Models » | 2606.23583, 25 pages | `598da3b4385230032fee5eb9ae43622c889008a8610554aecc4a700ad05257e7` |
| N. Singh, M. Chaudhary, « Evaluation Awareness Shifts from Format to Context with Model Scale » | 2609.22119v1, 20 août 2026, 20 pages | `02ee7b4cc98578688d47c83eb580a38a39f7bb6d149672cdef4eedd76ce97c96` |

## Ce que disent les PDF (vérifié)

- **Devbunova (2026)** :
  - plan 2 × 2 qui croise le format (banc d'essai, libre) et le contexte d'usage (évaluation, déploiement) : p. 2 (figure) et p. 3 (tableau 1) ;
  - cellule « Bench-Deploy » : des requêtes ShareGPT réécrites au format des bancs d'essai, « adversarial control » ; « Casual-Eval » tiré de MuTual : p. 3 ;
  - modèle `meta-llama/Llama-3.1-8B-Instruct`, `bfloat16`, une A100 de 80 Go, couches 8 à 31, graine fixe 42 : p. 3 et p. 5 ;
  - sonde apprise sur le seul contraste habituel : Bench-Deploy classé « évaluation » à 94,5 % ; sonde apprise sur les paires décorrélées : 7,2 % (tableau, p. 4) ;
  - limite déclarée : sondes linéaires seulement, un seul modèle : p. 4.
- **Nayan et al. (2026)** : reprennent le plan 2 × 2 (5 733 prompts) ; pour Llama-3.1-8B-Instruct, aire sous la courbe de 0,644 à 0,491 une fois format et contexte décorrélés (annexe A.6, p. 12) ; détection comportementale sans corrélation avec la détection robuste au format (p. 13 et p. 24).
- **Singh et Chaudhary (2026)** : selon le résumé, les petits modèles s'appuient surtout sur le format pour détecter l'évaluation, les plus grands sur le contexte ; un « Llama-3 8B » figure parmi les modèles étudiés (p. 1). Le reste du papier n'est pas encore lu.

## Lecture (R8)

- La zone « le signal de conscience d'évaluation de Llama-3.1-8B-Instruct suit le format de banc d'essai plutôt que le contexte, par un plan croisé » est **occupée** : Devbunova (2026), reprise par Nayan et al. (2026).
- Elle recouvre le placebo croisé (cellule « réel avec marqueurs » comprise) et le cœur de H-M1 (familiarité du format de banc d'essai, sur ce modèle). Ce qui pourrait rester, sous réserve d'une lecture complète : contenu strictement apparié dans les quatre bras, faux marqueurs, instruments certifiés à l'aveugle, tests d'équivalence, et la séparation format / style de consigne propre à H-M1.
- C'est un nœud de décision pour Lazar (« zone revendiquée trouvée occupée »).
