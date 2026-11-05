# Orchestrateur du pôle, version 0.7.0 — prise « idéation » : v35, réponse à la contre-lecture CL2 de la v34 (« lançable après corrections ») — LISEZMOI v35

Lignée conv-audit (instance de reprise du 28 octobre 2026, Fable 5.1), écrit après le relevé `date -u` de **20:24 UTC** ;
v1 à v34 gardées (R12). Répond à la contre-lecture CL2 de session-depot (`docs/notes/ideation-organisme-v1/contre-lecture-v34-cl2.md`
sur `main`, sous-agent neuf d'un autre modèle ; message n° 114 : « une v35 courte (CL34-01 à 05) »). **v35 n'est pas
contre-lue : le différentiel v34 → v35 doit être relu par un sous-agent d'un autre modèle que Fable avant tout lancement
réel** (R2) ; session-depot l'a annoncé (relecture ciblée chez lui).

## Ce qui change, constat par constat

| constat | correction | fichiers |
|---|---|---|
| **CL34-01** bloquant : Argon pouvait lire les fiches pendant la course | le bras rapporté est **toujours différé** : `executer_ideation` n'appelle jamais un juge externe (il n'a plus d'adaptateur dans la course), écrit sa consigne en attente **scellée** et son empreinte dans la lecture ; `attestation_lecture_humaine` donné à la course → `CourseInterrompue` avant tout appel ; le lanceur refuse `--attestation-lecture-humaine` sans `--bras-rapporte-differe` ; l'essai « bras joué dans la course » est devenu un artefact R5 (refus attendu) | `pole/ideation.py`, `demonstrations/ideation_v1.py`, `essais/test_v7_ideation.py` |
| **CL34-02** majeur : « aucun outil » non appliqué par le kit | `construire_options` rend `tools=[]` pour `proposeur_ideation` et `juge_ideation` (`None` = défaut du kit pour les autres rôles) ; `AdaptateurClaudeSDK.options_sdk` le transmet (`--tools ''`) ; essai qui construit la ligne de commande du kit (jamais exécutée, `cli_path=/bin/true`) et exige `--tools ''` sans `--allowedTools` ; affirmations corrigées | `pole/adaptateurs.py`, essais |
| **CL34-03** majeur : coût manquant lu comme 0 | `"cout_usd" not in objet` → statut `erreur` ; essai inversé | `pole/adaptateurs.py` |
| **CL34-04** majeur : bras différé sans contrôle, plafond, témoins, sceau, rejouable | `executer_bras_rapporte` : refus si `manifeste-bras-rapporte.json` ou `traces-<juge>/reponse.md` existe (jamais rejoué après dépense) ; sceaux vérifiés (fiches, classement, clés, témoins servis, manifestes, consigne en attente) ; l'attestation doit porter `consignes_en_attente_sha256` {étiquette : empreinte} en plus de `fiches_validees_sha256`, `lecteur`, `lu_le` ; **appel de contrôle** de chaque adaptateur externe sur ce chemin (retiré de la course) ; plafond total relu dans le manifeste de départ moins le coût compté au manifeste de fin, vérifié avant chaque session ; témoins relus depuis `noyau/temoins-servis.json` (écrit scellé par la course) et lus chez le juge externe par `lecture_temoins` (critère gelé) ; manifeste du bras écrit sur tous les chemins ; course arrêtée en erreur → aucun bras | `pole/ideation.py`, lanceur |
| **CL34-05** majeur : aucune borne de temps | `AdaptateurClaudeSDK(delai_s=1800)` : la session entière sous `asyncio.wait_for` ; dépassée → statut `erreur`, motif « délai de session dépassé », donc arrêt dur ; `--delai-session-s` ; essai avec un faux kit qui pend | `pole/adaptateurs.py`, lanceur |
| CL34-06 mineur | `--racine-depot` (défaut : `git rev-parse --show-toplevel` depuis le code, repli cinq niveaux, origine consignée) ; `SORTIE-controle` ajouté aux lectures interdites ; interdits consignés au manifeste de départ | lanceur, `pole/ideation.py` |
| CL34-07 mineur | défaut `--budget-total-usd 17` ; coût des appels de contrôle sommé et passé à la course (`cout_deja_engage_usd`), compté au journal (`cout_appels_de_controle_usd`) et dans le plafond total | lanceur, `pole/ideation.py` |
| CL34-08 mineur | `EFFORT_PAR_ROLE` (proposeur `high`, juge `medium`) transmis au kit (`--effort`) et présent dans les options | `pole/adaptateurs.py` |
| CL34-09 mineur | manifeste de départ : commande du juge externe et empreinte de ses arguments-fichiers, version de l'outil en ligne de commande (`claude --version`, sinon « inconnue »), lectures interdites ; `AdaptateurJugeExterne` passe à la commande un **environnement explicite et minimal** (PATH, HOME, LANG, LC_ALL, TMPDIR + `variables_transmises`, jamais un nom de clé), le même que celui qui est vérifié ; `ProxyHandler({})` pour `/relais/etat` ; **toute exception** écrit le manifeste de fin (course et bras) puis remonte ; le lanceur rend 2 sur toute exception | `pole/adaptateurs.py`, `pole/ideation.py`, lanceur |
| CL34-10 mineur | pluriels dans la garde (étapes, injections, portes dérobées, exécuter les scripts…) ; taux de quarantaine par proposeur dans la lecture (L1) ; le signal reste assumé (faux positifs admis, la lecture humaine est la barrière) | `pole/ideation.py` |
| CL34-11 mineur | `nombre_par_proposeur` ∉ [1, 12] refusé (noyau et lanceur) | `pole/ideation.py`, lanceur |
| CL34-12 mineur | longueur des témoins rapportée contre la fourchette des fiches (`longueur_temoins_contre_fiches`, témoins hors fourchette listés) ; consigne au tiers dans le devis v5 (noms neutres, injecteur classé `faux_falsifiabilite`) | `pole/ideation.py`, devis v5 |
| CL34-13 mineur | `lecture["complet"]` (toujours vrai) remplacé par `juges_rendus` ; code de sortie 3 (inatteignable) retiré ; docstrings « v33 », « juge non Claude impossible », « aucun outil » réécrits | tous |
| CL34-14 (lot) | lot **v2** avec les deux antériorités manquantes (`anteriorite-coevolution-et-boite-blanche-v1.md`, `anteriorite-universalite-metriques-v1.md`) | `livrables/lot-ideation-tournoi-v35-v1.zip` |

**Non corrigé, assumé** : la garde lexicale signale et ne décide pas (CL34-10) ; le juge simulé reconnaît les témoins de
l'exemple à leur nom (c'est la simulation, pas la course : les témoins réels du tiers ont des noms neutres, devis v5).

**312 essais passent** (305 + 7 : artefact attestation en course, bras différé complet avec refus avant appel, rejeu
refusé, sceau faux, plafond total, témoins lus chez le juge externe ; environnement minimal de la commande ; `tools=[]`
et ligne de commande du kit ; borne de temps ; pluriels ; `nombre` borné et contrôles comptés ; manifeste de fin sur
`OSError`). Course simulée de bout en bout puis bras différé simulé : attestation absente → arrêt ; attestation juste →
contrôle fait, témoins conformes chez le juge externe, accord de rang rapporté ; second lancement → refus ; options
refusées par le lanceur (`--attestation-lecture-humaine` sans `--bras-rapporte-differe`, `--nombre 13`).

## Commandes

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -B -m unittest discover -s essais -t . -p 'test_*.py'                              # 312 essais
$PY -I -B demonstrations/ideation_v1.py LISTE.json --construire-liste-blanche Q.md P1.md … TEMOINS.json
$PY -I -B demonstrations/ideation_v1.py SORTIE --liste-blanche LISTE.json --question Q.md --piece P1.md … \
    --temoins TEMOINS.json --piece-juge A1.md … --juge-externe argon=gemini-argon        # course ; Argon différé
$PY -I -B demonstrations/ideation_v1.py SORTIE --bras-rapporte-differe --juge-externe argon=gemini-argon \
    --commande-juge-externe "…" --attestation-lecture-humaine ATTEST.json               # après lecture humaine
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v35.txt
```

Attestation : `{"lecteur": "…", "lu_le": "…", "fiches_validees_sha256": "…", "consignes_en_attente_sha256": {"argon": "…"}}`,
écrite par le lecteur nommé après lecture des réponses brutes, de la quarantaine, de **toutes** les fiches validées et de
la consigne en attente ; scellée. Lancement réel : `../ideation-organisme-approches-v1/devis-ideation-v5.md`. Le reste :
LISEZMOI v34 à v1.
