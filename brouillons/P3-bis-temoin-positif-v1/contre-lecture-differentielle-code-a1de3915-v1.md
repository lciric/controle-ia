# Contre-lecture différentielle du code de P3-bis — commit proposé `a1de3915` — v1

- **Contre-lecteur** : agent neuf, Claude Fable 5.2 (`claude-fable-5-2`). Je n'ai écrit ni le code, ni la chaîne, ni le préenregistrement, ni les contre-lectures précédentes.
- **Objet** : différentiel du code de `02217f1c` (commit du code lu par la contre-lecture différentielle précédente, `01194253…`, vérifiée ; sa chaîne : `776b26cb`) à `a1de3915` (branche `prep/p3bis-lanceur-v1`, tête `614fd5da`). Ce que le différentiel doit faire : R-2103 et R-2113 de `registres/decisions.md`.
- **Méthode** : consigne `…/consigne-contre-lecture-differentielle-p3bis-code-v2-chaine-v1.md` (`62916a28…`, vérifiée) ; interdits communs v2 (`1ee3b370…`, vérifiés), règle 9 comprise.
- **Heures** (toutes relevées par `date -u`, le 2026-11-10) : début 10:04:05 UTC ; arbre détaché créé à 10:04:18 ; essais de 10:06:20 à 10:36:02 ; arbre retiré à 10:36:19 ; rapport écrit ensuite.
- **Lieu** : `/home/user/wt-p3bis-cl3`, détaché à `a1de3915`, extraction partielle prescrite (`docs/sources/` et `docs/notes/bras-attaque/` non extraits, absence vérifiée) ; retiré à la fin par `git worktree remove` (chemin exact), dossiers d'essai effacés.
- **Lu** : différentiel entier de `ouverture_p3bis_v2.py` et de son essai ; les deux fichiers d'essais neufs ; du module, les fonctions touchées et leurs appelants (lecteur de ligne, format, inscription, registres, garde d'ouverture, `ouvrir`) ; différentiel `776b26cb` → `a1de3915` du lanceur, du module commun et de leurs bancs (borne du 18) ; sortie v3 de l'essai de fermeture (`57d3467c…`, vérifiée par `git show` au commit `8ad29273`) ; ligne D-3 du rapport de concordance (`c867a1b2…`).
- **Empreintes** : `ouverture_p3bis_v2.py` à `a1de3915` = `1361382e…`, égale à son compagnon et à celle qu'imprime l'essai de fermeture ; compagnons des trois fichiers d'essais conformes. `src/`, `tests/`, `scripts/` : seuls ces quatre fichiers (et leurs compagnons) changent depuis `02217f1c` ; aucun script de l'instance, aucune liste, aucun fichier de P3 touché ; aucune empreinte périmée du module trouvée dans `src`, `scripts`, `tests` ni la chaîne.
- **Interdits tenus** : aucun fichier interdit ouvert ; aucun fichier ni module de T0.7 lu ; aucune recherche récursive hors `git grep` avec exclusions ; aucun appel externe, aucune dépense ; un processus d'essais à la fois. Écritures git : les seules commandes d'arbre prescrites. **Aucun refus de permissions ni de classifieur.**
- **Écarts du contre-lecteur, déclarés** : (1) pour que la liste ciblée se compte (défaut relevé par la contre-lecture précédente), le seul dossier `docs/sources/invites-2606.08892-v1` (68 fichiers) a été extrait dans mon arbre par `git archive a1de3915 … | tar -x` ; le reste de `docs/sources/` est resté absent. (2) La consigne demande la suite du code proposé, que la règle 5 des interdits réserve à la mère : j'ai suivi la consigne, en jouant la liste ciblée v2 entière et les deux fichiers d'essais neufs, pas tout `tests/`. (3) Une sonde à moi a créé un dossier temporaire dans mon arbre (journaux fabriqués), effacé aussitôt.
- **Non vérifié, déclaré** : la concordance avec le lecteur de T0.7 (non lu ; je m'appuie sur R-2113 pour le rejeu) ; le reste du différentiel de la chaîne (CD-04, CD-05 : hors de l'objet) ; les bancs autres que ceux du module commun et du lanceur ; la répétition jouet.

## Verdict

**`a1de3915` est citable au scellement comme commit du code** : chaque point de R-2103 et R-2113 est fait, avec cas sain et artefact, sans repli silencieux ; suite rejouée sans échec ; essai de fermeture v2 rejoué **CONFORME**. **Aucun constat bloquant, aucun « à corriger » dans le code** ; six constats mineurs, dont quatre à porter au texte (brouillon 11).

## Points demandés

| point | fait | cas sain | artefact | repli silencieux |
|---|---|---|---|---|
| **CD-01** `exclure_localement` | oui : refus si la racine git n'est pas la racine donnée, si `.git` n'est pas un dossier (arbre lié), si le fichier d'exclusion n'est pas sous `<racine>/.git/` ; `fermer_run` appelle la garde avant toute écriture | racine d'un clone, motif écrit une fois | sous-dossier (deux profondeurs), arbre lié, hors dépôt, `fermer_run` sur un sous-dossier : rien d'écrit | aucun |
| **D-1** horloge en arrière | oui : `exiger_horloge` dans `ouvrir`, avant toute lecture des registres, et de nouveau dans `inscrire` ; `HorlogeEnArriere`, code 2 en ligne de commande, aucune ligne, rien d'extrait ; dates non décroissantes exigées du journal lu | même seconde permise ; journal absent ou à en-tête seul | une seconde avant ; horloge réelle en arrière par la ligne de commande ; après une ouverture ; journal qui recule | aucun (C-2) |
| **D-2** `pleine-anticipee` | oui : refusée dès que `SCORES-T07` et `SONDES-T07` sont inscrites et conformes, avec ou sans décision ; refus journalisé, code `ni-scores-ni-ouvrir`, motif écrit | permise sous « ouvrir pleinement » sans ces lignes ; `pleine` ouvre | croisement avec « ouvrir pleinement », sans décision, complément après la réduite | aucun ; lecture littérale (lignes inscrites non conformes : permise) éprouvée et acceptée par la mère (R-2113) |
| **D-3** fichier vide | oui : hors format (`ligne-mal-formee`) ; `inscrire` n'écrit plus d'en-tête dans un fichier vide, qui reste donc hors format | journal absent : en-tête écrit, ouverture | fichier vide avant et après une ouverture ; seize formes du tableau du rapport | aucun |
| **D-4** chemin de T0.7 | oui : `SCELLEMENT-T07` et la garde adaptée doivent citer `prereg/T0.7-sondes-v0-v1.md`, sinon `garde-adaptee-absente` | réduite ouverte | autre chemin (même empreinte) sur l'une, l'autre, les deux | aucun (C-4) |
| **Clé de rendez-vous** | oui : `RENDEZ-VOUS-P3BIS-([1-9][0-9]*)` au registre ; l'appui du journal avait déjà ce motif | `-1`, `-9`, `-10`, `-123` | `-01`, `-0` : `cle-inconnue` ; `-007`, vide, `-1a` | aucun |
| **Borne du 18 novembre** | oui : `BORNE_CREATION` au lanceur (rejouée avant chaque essai d'offre) et au module commun, en plus de l'échéance du GO ; constante et phrase du texte liées par les contrôles | le 18 | le 19, le 23, date qui passe pendant les offres, borne à 17, phrase retirée du texte | aucun |

## Essais rejoués

Interpréteur `/home/user/controle-ia-travail/.venv/bin/python` (Python 3.13.18), `PYTHONPATH=src`, `-p no:cacheprovider`.

| essai | heures (UTC) | résultat |
|---|---|---|
| trois fichiers d'essais de l'ouverture v2 (v2, journal, exclusion) | 10:06:20 – 10:06:57 | **111 passés** (73, 33, 5), 36,90 s, code 0 |
| essai de fermeture v2 (`scripts/essai_fermeture_p3bis_v2.py`) | 10:06:57 – 10:14:00 | code 0, dernière ligne « ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME » ; 18 constats conformes, 0 non conforme ; mêmes quatre empreintes de fichiers essayés que la sortie v3 versée (`57d3467c…`) ; plage totale 10 octets, plus grande plage d'une issue 8 (marge 16) ; plus grand écart de durée 2,3 s (seuil 30 s) |
| liste ciblée v2 (30 fichiers) | 10:14:00 – 10:35:13 | **531 passés, 0 échec, 0 erreur**, 1 271,21 s, code 0 (compte de R-2113 retrouvé) |
| banc du module commun (pytest) | 10:35:23 – 10:35:35 | 144 passés |
| banc du lanceur | 10:35:41 – 10:36:02 | 58 cas, 0 non conforme ; L06, L06b, L06c, L06d, L07 conformes |

Sonde à moi (journaux fabriqués, fonctions du module) : LF et CRLF admis ; fichier d'une espace ou d'un seul saut de ligne, marque d'ordre d'octets, journal qui recule : refusés ; voir C-1 et C-2.

Fichier commun `/home/user/controle-ia-travail/.git/info/exclude` : 244 octets, daté 05:42:07, empreinte `44292ee3…` inchangée avant et après mes essais, joués pourtant depuis un arbre lié (la ligne `/x/` de l'incident y est toujours : à retirer par une personne).

## Constats

| # | gravité | lieu | constat | suite proposée |
|---|---|---|---|---|
| C-1 | mineur, au texte | `lire_journal`, `instant_de_la_derniere_ligne` ; en-tête du module et des essais (« CRLF seul admis ») | La phrase est inexacte : par `read_text`, un retour chariot seul et des fins de ligne mêlées sont admis aussi (sonde). Le rapport de concordance dit que le lecteur lit de même ; je ne l'ai pas vérifié. L'écrivain n'écrit jamais ces formes. | Écrire le prédicat exact au brouillon 11 et au brouillon 21 ; ajouter « retour chariot seul » au rejeu de concordance sur les commits finaux. |
| C-2 | mineur, au texte | `instant_de_la_derniere_ligne` | « Dernière ligne hors format tenue pour antérieure » : si une ligne bien formée plus haute est plus tardive que l'horloge, le refus `ligne-mal-formee` est écrit daté avant elle (sonde). Sens prudent : le journal est déjà hors format et le reste ; mais après réparation à la main de la ligne fautive, le recul demeure et tout reste refusé jusqu'à une seconde réparation. | Le dire au texte (toute réparation du journal est un nœud), ou comparer l'horloge à la plus tardive des lignes lisibles : changerait le commit, non nécessaire. |
| C-3 | mineur, au texte | `garde_ouverture` | D-2 ne porte que sur `pleine-anticipee` : sous « ouvrir », `reduite` reste permise quand `SCORES-T07` et `SONDES-T07` sont conformes (lecture du code ; conforme à la lettre de R-2103, et la réduite ouvre moins que la pleine). | Une phrase au brouillon 11. |
| C-4 | mineur | `garde_adaptee_en_vigueur` | D-4 n'est appliquée que dans la branche 1 (dernière décision « ouvrir ») ; ailleurs le chemin de `SCELLEMENT-T07` n'est pas jugé, la ligne n'y étant pas employée. Conforme à R-2103. | Aucune. |
| C-5 | mineur | `exclure_localement` | Un `.git` lien symbolique vers un dossier extérieur passerait les trois gardes (lecture, non éprouvé). Le chemin réel (clone neuf de la récupération) n'est pas concerné. | Aucune avant le scellement. |
| C-6 | mineur | `ouverture_p3bis_v1.py` l. 115 ; liste v2 | Le module v1 garde le motif `[0-9]+` (inchangé, R12) et la liste v2 joue encore ses essais ; la chaîne ne l'emploie pas. Liste v2 gardée par décision de la mère (R-2113). | Aucune. |

## Ce qui reste, hors de ce commit

- Le compte de 531 vaut sous Python 3.13 ; `TESTS_ATTENDUS_P3BIS` reste à compter sous Python 3.11 (CD-02 de la contre-lecture précédente).
- Les 38 essais neufs (33 du journal, 5 de l'exclusion) ne sont pas dans la liste v2 : joués localement, non sur l'instance (accepté par R-2113).
- Brouillon 11 : règles D-1 à D-4, lecture littérale de D-2, C-1 à C-3.
- Concordance du journal à rejouer sur les commits finaux des deux côtés (R-2103).
