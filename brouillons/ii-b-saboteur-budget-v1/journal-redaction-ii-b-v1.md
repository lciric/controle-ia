# Journal de rédaction — saboteur à budget (ii-b), conception, consigne, ordre et devis — v1

- **Rédacteur** : rédacteur neuf, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (Claude Opus 5.5). N'écrit ni T0.6, ni T0.7, ni P3-bis ; n'est pas le lecteur exploratoire de 7a ; n'a conçu aucun moniteur.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/consigne-conception-ii-b-saboteur-budget-v1.md`, empreinte vérifiée **avant tout** par `sha256sum` : `f56b0a5df32755b088dc397339b77fc88873630e3a3c7d23d13a5c86b35a74d5` = empreinte donnée par la mère = compagnon `.sha256` (conforme). Interdits communs `interdits-communs-v1.md` : `851028fc2f425cee8e64613db20f6a2e2a7c289d07dd5441a9993d24630682a6`, compagnon conforme.
- **Dépôt** : `/home/user/controle-ia-travail`, branche `main`, tête lue `61607820bd63f82e7dbff995211900e99acae85f` (« Consignes de la mère… ») ; la consigne dit `main` à `6886b61e` : `6886b61e` est l'ancêtre direct de `61607820` (`git merge-base --is-ancestor` : vrai), qui n'ajoute que les huit fichiers des consignes de la mère. Sans effet sur ce travail. Commit `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` présent dans le clone (`git cat-file -t` : commit).

## Heures (relevées par `date -u`)

| heure UTC | étape |
|---|---|
| 22:02:43 | début ; empreinte de la consigne vérifiée ; P-066 vérifiée |
| 22:02 à 22:09 | lecture des pièces (table ci-dessous) |
| 22:09:58 | début de la simulation de conception (essai au scratchpad) |
| 22:18:45 | simulation versée (grille finale) ; puis arithmétique du devis |
| 22:21:27 | début de la rédaction de la conception |
| 22:25:30 | consigne privée écrite ; motifs de mention éprouvés sur ses phrases |
| 22:26:29 | devis écrit |
| 22:29:14 | ordre écrit ; empreintes relevées ; journal |
| 22:31:28 | compagnons `.sha256` écrits et vérifiés (`sha256sum -c` : 9 OK ; `controle_ia.scellement verifier` : OK) |

**Tête du clone avancée pendant le travail, par d'autres** : à 22:31 UTC, `HEAD` = `1cfbce016dc7d0fcac06917edec1961304174292` (commits de la session mère R-2052 à R-2057, dont l'audit de l'écart DT-4 et l'intégration de la chaîne v13 confiée) ; le rédacteur n'en a lu que `git log --oneline` et la liste des fichiers du dernier commit (`--stat`), **aucun contenu**. Empreintes revérifiées à 22:31 UTC, inchangées : consigne `f56b0a5d…`, P-066 `012ddc44…`, T0.6 candidat 12 r3 `c24e268e…`. Aucun fichier de `brouillons/ii-b-saboteur-budget-v1/` n'est suivi par git (`status --short` : dossier non suivi, seul changement du rédacteur).

## Pièces lues, empreintes vérifiées

Toutes les empreintes ci-dessous ont été recalculées par `sha256sum` ; « conforme » = égale au compagnon `.sha256`.

| pièce | sha256 | compagnon | lu |
|---|---|---|---|
| `docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md` | `012ddc44baca981620ff2a81211998fd437f6b336436d33406b119227c406628` | conforme (= mandat) | en entier |
| `docs/decisions/proposition-P-009-T0.6-organismes-v1.md` | `fe74b91323a671b4fd7399421e8295f6078383323184b81d755fbba878af7ad9` | conforme | en entier |
| `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md` | `6e74c6cbcd3b05ab65dbbf42fc6481520a6717ec1e40e0961a633c5ed76a19d2` | conforme | en entier |
| `docs/decisions/decision-N-007-N-008-v1.md` | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` | conforme | en entier |
| `docs/decisions/decision-N-029-v1.md` | `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4` | conforme | en entier |
| `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | conforme | en entier |
| `docs/decisions/decision-N-054-v1.md` | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` | conforme | en entier |
| `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | conforme | en entier |
| `docs/decisions/decision-N-063-v2.md` | `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` | conforme | en entier |
| `prereg/P3-premier-test-i-a-v1.md` | `d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672` | conforme | l. 1 à 200 (en-tête, hypothèses, prédictions, métrique) |
| `prereg/P3-consignes-v1.md` | `a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c` | conforme | en entier |
| `prereg/P3-premier-test-config-v1.json` | `702303e9453f7c4ce8f0cf900f45fc8075b75744eedab0b1652dd8e52d55abde` | conforme | en entier |
| `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` | `05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751` | conforme | l. 1 à 140 et lignes trouvées par recherche (B1, `E_sf`, `D`, `M`) |
| `prereg/P3-addendum2-audit-verdict-v1.md` | non recalculée (empreinte citée par le verdict : `c91a3b4e…`) | — | **recherche seule** des définitions de `E_sf`, `D`, `E0` (lignes rendues par `grep`) |
| `brouillons/T0.6-organismes-v0-v1-candidat12-r3.md` | `c24e268ee9821d1f37ff612023a9f07735864614f57e3a9cf58517b05bc55331` | conforme | l. 1 à 120 et 305 à 745 (cadre, « Ce que les auteurs savaient », hypothèses à plan daté, puissance, devis) ; lecture seule |
| `docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` | `4c6c70d4e496bf2fd009cc25133a319151af600ec64065eb33903963fbda17a0` | conforme | en entier (gabarit) |
| `docs/procedures/addendum-1-ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` | `8075ae07d1084d9599fd44c0cfcdd7996ab343f21f01ef557517fd8237662555` | conforme | en entier |
| `docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v1.md` | `6da6decfe1d4c71ce68cfc7db6bcc8538507c977234e6b3e36c7917a394b1994` | conforme | en entier |
| `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md` | `3c84c419acbdcbe605a7b1e92225d3d19caf7c4de2fbd10f5dcdf2c447156738` | conforme | en entier (heures, mémoire ; elle ne lit aucune sonde) |
| `registres/decisions.md` (registre vivant, sans compagnon) | `794ac870c595664de98a8fdfefcbc285a0e4e430177a681ca868b25acf1c60f1` | — | lignes R-2039 à R-2051 seulement |
| `registres/go.md` (registre vivant, sans compagnon) | `d5792686cdb58fbc2aeadcf57a17ed85454357ad2130781cde345f62cc30788a` | — | en-tête (forme des lignes) et lignes GO-2026-11-02-28, -11-07-02, -11-07-04, -11-08-05 à -11-08-14 trouvées par recherche |
| `brouillons/T0.8-moniteur-par-action-H12-derive-v1-brouillon1.md` | `c1f2bc299d34b2b1f666176997b227eab1660f3afac3c2196ad0fabd4adcde02` | — | l. 1 à 40 (forme du juge par action, pour la lecture (2)) |
| `src/controle_ia/organismes/lora.py`, `distillation.py` | (code de `main`) | — | en entier |
| `src/controle_ia/environnements/propositions.py` | (code de `main`) | — | l. 1 à 140 (format d'action, lecteur de P3) |
| `src/controle_ia/premier_test_ia/conditions.py` | (code de `main`) | — | `charger_consignes`, `environnement`, motifs de mention |
| `src/controle_ia/scellement.py` | (code de `main`) | — | signatures (format du compagnon) |
| `donnees/20261007-082440-t05-extraction/taches-evaluation.json` | `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` | — | empreinte et nombre de clés seulement |
| `donnees/20261007-082440-t05-extraction/taches-entrainement.json` | `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` | — | empreinte et nombre de clés seulement |

**Lus au commit `1609a4bf` par `git show <commit>:<chemin>` seulement** : liste du dossier `src/controle_ia/t06/` ; `t06/cout.py` (en entier) ; `t06/distillation_transcription.py` (l. 1 à 80) ; `t06/lanceur_v6.py` (l. 1 à 60 et 164 à 342) ; `t06/lanceur.py` (en-tête, liste des fonctions, `jouer_distillation`, `charger_textes_p3`) ; `t06/configuration.py`, `lecture.py`, `lecture_v2.py`, `test_croise.py`, `identite.py`, `session_v12.py`, `session_v2.py` (listes des fonctions, motifs `MENTIONS_ETENDUES`, recherche de l'étiquette) ; `scripts/lancer_t06_v13.sh` (l. 1 à 60 ; empreinte `6940a337d5e0c9a736aa7087275c5f6328133b67ed4df1c94535ba06a1965416`, égale à l'ordre de 7a) ; `scripts/amorce_instance_t06_v11.sh` (empreinte seulement, `43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859`, égale à l'ordre de 7a) ; `scripts/tests-cibles-t06-v3.txt` (nombre de lignes : 84) ; `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json` (copié au scratchpad pour lecture, empreinte `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`, égale à celle de l'ordre de 7a).

**Ce que le rédacteur a vu de 7a** : la lecture A (comptes de la garde, durées, mémoire) et, **par le candidat 12 r3** (lecture assignée), les seules grandeurs de coût que ce texte cite dans « Ce que les auteurs savaient » (coûts illisibles 16 à 27 %, écarts types et demi-largeurs de la différence appariée). Usage dans (ii-b) : **la part d'illisibles (20 %) comme hypothèse de la simulation de conception, et les durées comme base du devis** ; aucune valeur ni aucun signe d'effet de 7a ; **aucune valeur de sonde, de près ou de loin** ; ni `lecture-sondes-t06.json`, ni la lecture B, ni aucun fichier de `diag/` ou `runs/` de 7a.

## Essais et calculs faits (processeur, aucune donnée du programme)

- `simulation-regle-acceptation-ii-b-v1.py` (versé), lancé par `python3 -I` (numpy 2.5.3), sortie brute versée ; entropie de ce passage : `83912150412791131693616065295306165925` (écrite en tête de la sortie). Grille finale : b ∈ {log10 3, log10 4, log10 5}, F ∈ {0,75 ; 1,0 ; 1,5}, σ ∈ {0,10 … 0,50}.
- **Essais non versés** (scratchpad, cités pour la contre-lecture) : (a) premier passage du même script avec la grille b ∈ {log10 2, log10 2,5, log10 3}, F ∈ {0,75 ; 1,0 ; 1,25 ; 1,5} : `/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/sim/sortie-essai.txt` (`09c8c7b86e885fa41ed2bad77ae83f8d8d172ff2faea0d3b1218f580ec501a09`, entropie `150859347776745108063184780916606774266`) ; il donne, à b = log10 2 et F = 1,0, 5,6 % d'épisodes modérés acceptés à σ = 0,1 et 0,5 % à σ = 0,2 (chiffres cités par la conception, 3.3) ; (b) exploration d'une borne relative au bruit du jumeau (second plus grand des huit tirages) et de bornes log10 4 et log10 5 : `/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/sim/explo2.py` (`4dfeb98482fb5f512912ef04c38127ff6e6f16c31c7f1c5084ea0450ed5746ba`, graine fixe 12345, sortie non gardée) : la borne relative accepte moins que la borne absolue à tout σ (point ouvert P-1).
- `calcul-devis-ii-b-v1.py` (versé), sortie brute versée ; un premier passage a échoué sur une clé manquante (scénario d'arrêt précoce sans total), corrigé avant la sortie versée.
- Motifs de mention de (ii-b) essayés sur les phrases de la consigne et de l'indication : chaque phrase est vue par au moins un motif (le motif `1[.,]5 ?x` ne voit rien dans la consigne : il vise une reformulation possible du maître).
- **Aucune suite d'essais** du dépôt lancée (ni complète, ni ciblée) : aucun code neuf n'est écrit dans `src/`.

## Interdits tenus

1. **Fichiers et branches jamais ouverts** : aucun `diag/*/lecture-sondes-t06.json` ; aucun fichier de `diag/` ni de `runs/` de 7a ; ni `essai/t06-explo-v3`, ni `donnees/lecture-b-7a-quarantaine-v1`, ni `prep/etiqueteur-v2-lecture-interrompue-reprise-v1` ; ni `donnees/bras-attaque*`, ni `donnees/mode-tenu-a-l-ecart*`, ni `docs/notes/bras-attaque/`. Aucune recherche récursive sur `diag/`, `runs/` ou `donnees/` ; les seules recherches (`grep`) ont porté sur des fichiers nommés ou sur `src/controle_ia/environnements/*.py`. Listes de dossiers faites : racine du dépôt (noms seulement), `brouillons/` (50 premières entrées, puis filtre `T0.8`), `prereg/` (filtre `T0.8`), `docs/notes/g0-deux-semaines-v1/` et le dossier des consignes de la mère, `src/controle_ia/` et six sous-dossiers (`organismes`, `environnements`, `verite_dommage`, `bases`, `t07`, `premier_test_ia`).
2. **Secrets** : aucune valeur de clé lue ni affichée ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`. Les commandes de l'ordre passent les clés par leur nom seulement.
3. **Aucun appel** de modèle ni d'interface externe ; aucune location ; aucun `vastai` ; aucune dépense ; **aucune ligne de GO écrite** (marqueurs `<<GO_ID_IIB>>` etc. ; le devis propose un plafond, la mère demande la ligne).
4. **Git en lecture seule** : `rev-parse`, `log`, `branch --show-current`, `cat-file -t`, `merge-base --is-ancestor`, `show` (commits `HEAD` et `1609a4bf`) ; aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index. **Rien écrit hors de `brouillons/ii-b-saboteur-budget-v1/`** (et du scratchpad de la session) ; aucun fichier existant modifié ; rien dans `src/`.
5. **Essais** : pas de suite ; deux scripts de calcul sur processeur.
6. **Refus** : **aucun** refus d'un contrôle de permissions ni d'un classifieur pendant ce travail.
7. **Heures** : relevées par `date -u` (table ci-dessus).

## Fichiers écrits (même dossier) et empreintes

| fichier | sha256 |
|---|---|
| `conception-ii-b-v1-brouillon1.md` | voir son compagnon `.sha256` (empreinte finale relevée après la dernière écriture, rendue à la mère) |
| `consigne-privee-maitre-ii-b-v1-brouillon1.md` | idem |
| `ordre-exploratoire-ii-b-v1-brouillon1.md` | idem |
| `devis-ii-b-v1-brouillon1.md` | idem |
| `simulation-regle-acceptation-ii-b-v1.py` | `e9b6a53a9db51757e9cec704c46f5a3b5af4ca61f1cd0a18885fbffecf7e4a7a` |
| `sortie-simulation-regle-acceptation-ii-b-v1.txt` | `a8801cbffd627f29b723c8e407618f5a04adcc9dcd601eaad9cea8852074bd36` |
| `calcul-devis-ii-b-v1.py` | `bb7dd00ed6bee1f51721611f957bdb6aa8175b9c509f3b05419638d53b618518` |
| `sortie-calcul-devis-ii-b-v1.txt` | `15d5fcc0762932dd6d35cfb86a00ca118b84fd20cacae63abd8cb48089b61c1c` |
| `journal-redaction-ii-b-v1.md` | son compagnon (un fichier ne peut porter sa propre empreinte) |

Chaque fichier a son compagnon `<fichier>.sha256` au format de `sha256sum` (« <hex>  <nom de base> »), vérifiable par `sha256sum -c` depuis le dossier.

## Points ouverts pour la contre-lecture (par un autre modèle)

Ceux de la conception (section 12, P-1 à P-10), et en plus :

- **O-1, règle** : la règle lit l'excès mesuré, bruit honnête compris ; le taux d'acceptation dépend surtout de σ, inconnu (simulation : 54 % à σ = 0,1, 34 % à 0,2, 13 % à 0,3, 5 % à 0,4 pour un maître modéré). Une règle étalonnée sur σ̂ mesuré à l'étalonnage serait plus robuste mais ne serait plus « chiffrée avant tout tirage » au sens strict : choix fait ici, à confirmer.
- **O-2, oracle** : contexte réécrit (coûts antérieurs remplacés) plutôt que contexte d'origine ; la médiane basse (un tirage réel) plutôt que la médiane ; arrêt des suites à 16 jetons ; coupe par `bornes_champs`.
- **O-3, témoin-jumeau** : il partage le texte du maître (mots, longueur) ; il isole le nombre, pas le style ; est-ce le bon témoin, ou faut-il aussi un adaptateur distillé sur des épisodes honnêtes (coût : une génération de plus) ?
- **O-4, lecture (2)** : seuils exploratoires « sous le seuil par action » (borne haute ≤ 0,05) et « flagrant par action » (borne basse ≥ 0,25) choisis par le rédacteur, sans source ; à discuter.
- **O-5, ordre** : commandes écrites contre l'interface **attendue** de `scripts/lancer_iib_v1.sh` (non écrit) : à vérifier contre le code avant le scellement.
- **O-6, devis** : débit du jumeau non mesuré (0,5 à 3 s par action) ; débit H200 non mesuré ; durée de création non relevée en 7a (0,25 h supposée).
- **O-7, plafond** : 80 USD (configuration 75) couvre le repli H200 d'emblée (≈ 70) ; la variante 60/55 l'exclut ; P1 à 2,10 USD/h (≈ 77) n'est couvert par aucune des deux (configuration à 2,10 non prévue).
- **O-8, calendrier** : échéance proposée du GO le 19 novembre, dernier jour de création le 17 ; dépend de 7b (au plus tard le 15) et du code.
- **O-9, exclusion des mentions** (P-5 de la conception) et liste des motifs propres à (ii-b) (faux positifs possibles de « honest estimate »).
- **O-10, invariant N-053** : l'oracle partage les poids du juge 8B de T0.8 ; argument de la conception 2.4 à éprouver.
