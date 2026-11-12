# Contre-lecture des corrections du rejeu v2 des juges (R2)

Contre-lecteur neuf : auteur ni du code ni de la première contre-lecture. 29 octobre 2026, 09:05 à 09:35 UTC
(`date -u`). Aucune dépense, aucune clé, aucune instance. Le dépôt n'a pas été modifié. Travail sur deux copies
légères (`copie/` = `5f13293a`, `copie-ancien/` = même arbre avec le module de `cff3d90a`).

## Verdict

**Lançable.** Pas de constat bloquant ni majeur.
- Le diagnostic des fins de tour du 3B est **exact**. La correction est juste et ne laisse passer aucun vrai écart
  d'encodage. Il reste un trou théorique sur les fins elles-mêmes (CLC-02, mineur).
- Le 8B n'est pas exposé au même défaut.
- CLR2-01 et CLR2-06 sont corrigés comme demandé. Suite ciblée : **226 réussis**, le nombre cité par la fiche.
- Cinq constats mineurs. Aucun n'est exigé avant le lancement ; CLC-02 et CLC-03 sont recommandés. Si on les applique,
  il faut recompter « Tests attendus » avant le scellement.

## Brouillon relu (commit `5f13293a`, sha256)

| fichier | sha256 |
|---|---|
| src/controle_ia/environnements/noter_rejeu_juges_v2.py | `d1758f6eae8fd8bb3ceb0e5e5663707dc00d68a2a1a687bca04a5cfe9073da0a` |
| tests/test_noter_rejeu_juges_v2.py | `89728c54954ee8a6c070c319175cb1a800cde5dbdc8264376606e9af5dbe9c52` |
| scripts/rejeu_juges_instance_v2.sh | `967427c697cc07b34accc66cfa5935ac97fd89957bc71bb494334f96a4747aec` |
| docs/procedures/rejeu-juges-v2/lancer_rejeu_juges_v2.sh | `e38e46446844905b68cdd0ce70521253e0a7244599e62a056f07c6eb33424157` |
| …/rejeu-juges-v2/fiche-lancement-rejeu-juges-v2.md | `fb5518154898376c663292115381101b395569ef5dacd41a7bcab01332786f30` |
| …/rejeu-juges-v2/devis-rejeu-juges-v2.md | `f2d13eefbfbc0041565a06c08d439029073558ce0f040e26db293a345cd791ca` |

Le rapport R2 versé sous `contre-lecture-v1/` a la même empreinte que l'original (`b156da9f…`).

## Priorité 1 — fins de tour du 3B

### Diagnostic : exact (démontré)

Outil : `outils/fins_3b_vrai_tokeniseur.py` ; sortie : `sortie-fins-3b.txt`.

Données :
- tokeniseur réel du 3B (`tok-llama32/` de la contre-lecture R2 ; copie publique, non empreintée contre la
  révision `0cb88a4f`) ;
- `generation_config.json` public de `unsloth/Llama-3.2-3B-Instruct` (téléchargé sans frais, `hf/` ; copie non vérifiée
  contre la révision ; la page `meta-llama` répond 401). Ses `eos_token_id` valent `[128001, 128008, 128009]`, comme
  ceux du 8B que le dépôt a observés au réel (verdict T0.4 : « 128001, 128008 ou 128009 »).

Résultats :
- Format du début du run (`charger_format_seul` : `FormatChat` sans `fins`) : fins `{128009}` (fin du tokeniseur,
  `<|eot_id|>`).
- Format du 3B chargé (`charger_modele_et_format` : `fins_du_modele` plus le premier jeton de clôture) : fins
  `{128001, 128008, 128009}`.
- `controler_format` est égal sur les deux formats : `verifier_format` ne dépend pas des fins.
- **Ancienne garde : arrêt.** Les terminaux diffèrent (`<|end_of_text|>` et `<|eom_id|>` en plus), et donc aussi
  `encodage["terminaux"]`. Le chargement du 3B se fait avant toute phase. La phase décisive du 8B, première dans la
  configuration, était donc perdue aussi.
- **Nouvelle garde : passe.** Les jetons de saut sont égaux entre les deux formats.
- Comptes réels, identiques pour les deux tokeniseurs : 201 jetons de fin de ligne (vocabulaire seul), 202 avec la fin
  du tokeniseur, 204 avec les trois fins.

Banc jouet :
- l'essai de l'auteur `test_3b_recharge_avec_les_fins_du_modele_cas_sain` **échoue sur le module `cff3d90a`** (« jouet-3B :
  encodage chargé hors ligne ≠ … ») ;
- il **passe sur `5f13293a`**.

L'affirmation de l'auteur tient.

### Le 8B n'est pas exposé

- Le 8B est l'agent. Son format au début du run vient déjà de `charger_modele_et_format`, avec les fins du modèle, et
  il n'est jamais rechargé : rien n'est comparé.
- La garde préalable (`--controle-encodage`) prend le tokeniseur seul pour les deux juges. Elle ne se compare à rien
  dans le run, donc elle ne peut pas causer de faux arrêt.

### La correction n'ouvre aucun trou sur l'encodage

- Comme avant, elle compare le contrôle d'encodage entier (garde v1, sondes, 94 valeurs), sauf le résumé des
  terminaux.
- Elle compare aussi la liste des jetons de fin de ligne du vocabulaire, qui suffit à repérer tout changement de
  vocabulaire sur les fins de ligne.
- Un tokeniseur rechargé qui découpe autrement s'arrête donc comme avant :
  - l'essai d'artefact R2 versé (`valeurs_controlees_v2` faussé) arrête toujours, sans aucune phase ;
  - mon essai (CLC-03) sur la branche « fins de ligne » arrête aussi.
- La seule chose qui passe désormais sans contrôle est une différence de **fins** (CLC-02).
- Effet sur la lecture : le 3B lit maintenant avec les mêmes 204 terminaux que le 8B (symétrie). La seule masse en plus
  est celle d'une valeur suivie de `<|end_of_text|>` ou de `<|eom_id|>`, négligeable après « NOM: v ».

## Constats

**CLC-01 — information — Le diagnostic et la correction du 3B sont vérifiés.**
- **Preuve.** Voir la priorité 1. Ancienne garde : arrêt. Nouvelle garde : passage. Essai de l'auteur : rouge sur
  `cff3d90a`, vert sur `5f13293a`.
- **Correction.** Aucune.

**CLC-02 — mineur — La garde corrigée ne borne pas les fins ajoutées au rechargement.**
- **Preuve.** Les terminaux de la lecture deviennent `nouveaux` sans aucune relation exigée avec ceux du début. Seules
  les fins de ligne du vocabulaire et l'encodage sont comparés. Banc jouet (`outils/test_fins_3b_complementaires.py`,
  `test_trou_fin_du_modele_sur_un_chiffre_passe`) : avec une « fin du modèle » égale au jeton « 0 », le run continue et
  écrit les deux phases. Le chiffre entre alors dans les terminaux de la lecture du 3B, et P(« 2 » puis fin) avalerait
  P(« 20 »).
  - Au réel, le risque est très faible : la configuration de génération vient de la révision figée.
  - `jetons_de_saut` est aussi repris du tokeniseur rechargé sans comparaison. Il est égal au réel (démontré).
- **Correction (trois lignes).**
  - Exiger `set(nouveaux) >= set(terminaux_debut)`.
  - Exiger que `set(nouveaux) - set(terminaux_debut)` soit inclus dans `fmt_j.fins ∩ set(fmt_j.tok.all_special_ids
    or [])`, ou que chaque ajout se décode en « <|…|> ».
  - Exiger `jetons_de_saut(fmt_j.tok) == sauts[j]`.
  - Consigner la liste des fins ajoutées dans `etat`.

**CLC-03 — mineur (R5) — La branche « fins de ligne du vocabulaire » de la nouvelle garde n'a pas d'essai sur artefact.**
- **Preuve.** Les essais du dépôt prouvent :
  - le cas sain (fins du modèle en plus) ;
  - l'artefact d'encodage (`valeurs_controlees_v2`).

  Aucun ne fait échouer la comparaison `jetons_terminaux(fmt_j.tok, set()) != fins_de_ligne[…]`.
  `test_artefact_fins_de_ligne_du_3b_recharge_differentes` (même outil) fausse le 3e appel à fins vides : arrêt « encodage
  chargé hors ligne », `arret.json` à phases vides. Il réussit.
- **Correction.** Verser cet essai, avec ceux de CLC-02 si on les adopte. « Tests attendus » passerait alors de 226 à
  227 ou plus : recompter avant le scellement.

**CLC-04 — mineur — Garde préalable : elle se fait après l'installation lourde, pas avant.**
- **Preuve.** La docstring de `controle_prealable_encodage` dit « avant l'installation lourde et la suite de tests ».
  Or le script la lance après `pip install -r requirements-gpu.txt` et le contrôle de la carte, juste avant les tests.
  Le devis dit qu'un échec « coûterait ≈ 3 minutes au lieu de ≈ 25 ».
  - Le coût perdu en cas d'échec est en fait démarrage + clonage + installation complète, plus près de 10 minutes que
    de 3 (non mesuré).
  - Le gain réel est la durée de la suite ciblée : ici, 651 s sur processeur. Il reste réel.
- **Correction.** Corriger la docstring et la ligne du devis : « avant la suite de tests ; un échec coûte le démarrage
  et l'installation ». On peut garder l'ordre. L'arrêt est propre et consigné : `ETAPE`, trois lignes de stderr au
  journal, `consigner_arret`, sortie 1.
- **Démontré en jouet.**
  - Configuration saine : code 0, JSON des deux juges (94 valeurs chacun).
  - Configuration sans `phases` : code 1, « ARRÊT : configuration du rejeu v2 incomplète : ['phases'] ».

**CLC-05 — mineur — Les terminaux de la garde préalable et ceux du run diffèrent, ce qui peut se lire comme une
anomalie.**
- **Preuve.** Au réel, `encodage.json` (tokeniseurs seuls) donnera `terminaux.n = 202` pour les deux juges. Le run
  (`resume.json`, `rejeu-*-verdict-echelles.json`) et la fiche (« 204 jetons de fin de ligne ou de fin de tour »)
  diront 204. Comptes sur les vrais tokeniseurs ci-dessus.
- **Correction.** Une phrase dans la fiche, à la « Liste d'arrêt » : « la garde préalable ne porte que la fin du
  tokeniseur (202) ; le run, celles du modèle (204) ». Ou retirer `terminaux` de la sortie préalable.

**CLC-06 — mineur — Second réveil : marge de 2 à 3 minutes sous le plafond.**
- **Preuve.** Session perdue, arrêt au second réveil : (150 + 2) min = 2,533 h × 1,43 + 0,32 = **3,94 USD**. La marge
  sous 4 USD est de 0,06 USD, soit ≈ 2,4 minutes. Or un réveil attend la fin du tour en cours de la session.
  - Les heures sont cohérentes : lanceur `CREATION + 8100` et `+ 9000`, messages « + 135 et + 150 min », fiche et devis.
  - Les autres chiffres tiennent aussi : pire facturé 140 min ≈ 3,66 USD ; seuil de 45 minutes ⇔ 58 minutes avant le
    plafond (`RESTE = reste − 8 − 5`).
- **Correction.** Second réveil à + 145 min, ce qui laisse ≈ 3,8 USD. Ou consigner que la session ne garde aucun tour
  long ouvert entre + 135 et + 150 min.

**CLC-07 — information — CLR2-01 est conforme.**
- **Preuve.**
  - Mêmes chemins que `validation_reelle.CHEMINS_GELES`, dans le même ordre : « . » et onze exclusions, `CLAUDE.md`
    compris.
  - Même comparaison commit à commit (`git diff --quiet A B`). Le module compare le commit cité à HEAD, et HEAD vaut
    COMMIT sur l'instance.
  - Le contrôle est dans un `if` (`set -e`, `trap ERR`), avant toute création.
  - Rejoué sur les vrais commits du dépôt :
    - `cff3d90a..5f13293a` : refusé (module, essais, script) ;
    - `244d1525..37fe5c97` (165 fichiers sous `docs/`, 4 sous `brouillons/`, 1 sous `registres/`) : accepté ;
    - un commit inconnu : refusé, avec un message qui dit « modifié » alors qu'il s'agit d'une erreur de git
      (cosmétique ; l'ascendance l'a déjà écarté).
- **À savoir.** D'autres sessions committent souvent dans `src/` et `tests/` : 68 et 43 fichiers en trois jours. Tout
  commit de code entre le commit du code et le scellement fera refuser le lancement. C'est voulu. Le remède est de
  re-citer le commit et de resceller.

**CLC-08 — information — « Tests attendus : 226 » est confirmé.**
- **Preuve.** Suite ciblée telle que la liste la fiche (sept fichiers, `-p no:cacheprovider`), sur une copie de
  `5f13293a`. Il a fallu y ajouter `docs/sources/invites-2606.08892-v1/`, que les essais lisent. Dernière ligne :
  `226 passed in 651.45s (0:10:51)`. Elle est conforme au motif du script (suffixe « (h:mm:ss) » admis). Sortie :
  `pytest-cible.txt`.

## Non vérifié

- La configuration de génération et le tokeniseur du 3B **à la révision figée `0cb88a4f`** : seules des copies
  publiques ont été lues. R-068 (même `tokenizer.json` que le 8B) n'a pas été revérifié.
  - Si les vraies fins étaient `{128009}` seulement, l'ancienne garde n'aurait pas arrêté.
  - La garde corrigée reste juste dans les deux cas.
- Le banc complet du lanceur devant le faux `vastai` après correction (fiche non scellée et `garde_calcul.py` liée
  aux registres) : seul le fragment `git diff` a été rejoué, sur les vrais commits.
- La chaîne de l'instance en jouet de bout en bout avec l'étape préalable : seule la commande `--controle-encodage` a
  été rejouée, avec ses codes de sortie.
- Les durées d'installation sur l'instance (CLC-04).

## Fichiers (dossier `relecture-rejeu-v2-corrections/`)

- `outils/fins_3b_vrai_tokeniseur.py`, `sortie-fins-3b.txt` : diagnostic du 3B sur les vrais tokeniseurs.
- `outils/test_fins_3b_complementaires.py` : CLC-02 et CLC-03, 2 réussis.
- `pytest-cible.txt` : 226 réussis.
- `hf/` : configurations de génération publiques (données seules).
- `copie/`, `copie-ancien/` : copies légères, jetables.
