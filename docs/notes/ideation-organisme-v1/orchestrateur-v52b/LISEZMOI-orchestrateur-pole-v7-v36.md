# Orchestrateur du pôle, version 0.7.0 — prise « idéation » : v36 — Argon à poids égal (juge) et à égalité (proposeur) ; réponse à la relecture CL3 de la v35 — LISEZMOI v36

Lignée conv-audit (instance de reprise du 28 octobre 2026, Fable 5.1), écrit après le relevé `date -u` de **21:40 UTC** ;
v1 à v35 gardées (R12). Répond : (i) aux **décisions de Lazar** du 28 octobre (21:05 UTC : « je veux que Argon pèse à
poids égal aux autres modèles dans le jugement » ; 21:20 UTC : « Argon propose aussi, à égalité avec Opus et Fable »),
transmises par session-depot (messages n° 118 et 119) ; (ii) à la relecture ciblée v34 → v35 de session-depot
(`docs/notes/ideation-organisme-v1/contre-lecture-v35-cl3.md` sur `main`, « lançable après corrections », message n° 117 :
CL35-01 à 04 majeurs, 05 à 14 mineurs). **v36 n'est pas contre-lue : relecture ciblée v35 → v36 par un modèle ≠ Fable
annoncée chez session-depot, avant tout lancement** (R2).

## Argon à poids égal et à égalité (n° 118, n° 119)

| point | ce que fait la v36 | fichiers |
|---|---|---|
| **Proposeur Argon dans la course** | `--proposeur-externe argon=gemini-argon --commande-externe "…"` : `AdaptateurCommandeExterne` (ex-`AdaptateurJugeExterne`, nom gardé en alias) joue `proposeur_ideation` et `juge_ideation` ; même consigne, mêmes pièces, même nombre, même garde et quarantaine, mêmes témoins de longueur ; il ne voit **jamais** les fiches des autres proposeurs (la passe 2 ne sert que les siennes) ; **sa passe 2 exige `--attestation-materiau`** (JSON scellé `{lecteur, lu_le, materiau_sha256: {nom: …}}`, empreintes vérifiées) sinon la course refuse **avant tout appel** ; plafond **externe séparé** (`--budget-externe-usd`, défaut 4 ; sessions 1 par passe) ; `cout_externe_usd` au journal | `pole/ideation.py`, `pole/adaptateurs.py`, lanceur |
| **Juge Argon à poids égal, différé** | la course avec `--juge-externe` écrit sa consigne en attente scellée et **aucun classement ni agrégat** (`lecture-course.json` : témoins et auto-préférence par juge Claude seulement, quarantaine, longueurs ; `noyau/modeles.json`) ; `executer_bras_differe` (ex-`executer_bras_rapporte`, alias gardé) joue Argon après l'attestation puis écrit le **classement à trois juges** : médiane par critère (`nom_agregat: mediane`), porte sur l'agrégat, unanimité, **accords de rang par paire**, témoins lus chez les trois et chez Argon seul, auto-préférence des trois | `pole/ideation.py` (`_classer`) |
| **Aucun repli silencieux** | Argon en panne, au-delà du plafond, notes invalides → `SansJugeExterne` : `classement-sans-bras.json` à deux juges marqué « sans juge externe, illisible au sens du devis », `lecture-sans-bras.json`, manifeste du bras avec l'erreur, **code de sortie 5** ; témoins échoués chez Argon → classement à trois juges écrit, illisible, code 4 | `pole/ideation.py`, lanceur |

## Relecture CL3 de la v35, constat par constat

| constat | correction |
|---|---|
| **CL35-01** coût NaN accepté, manifeste absent | coût **obligatoire, fini, strictement positif** (NaN, ∞, 0, négatif, absent → `erreur`) ; le manifeste du bras est écrit **avant** les fichiers de lecture ; essais inverses |
| **CL35-02** coût perdu sur une sortie ≠ 0 | la dernière ligne est lue même sur un échec ou un délai : coût imprimé compté ; sinon **plafond de session compté**, `cout_inconnu` marqué (`Resultat.cout_inconnu`, journal) |
| **CL35-03** commande non consignée | `AdaptateurCommandeExterne.description()` (commande, empreintes des arguments-fichiers, variables transmises, délai) dans le manifeste de départ (proposeur) et dans celui du bras (juge) ; essai |
| **CL35-04** bras simulé sur course réelle | le bras relit `moteur` et `juges_externes` du manifeste de départ : course réelle → seule une commande externe joue ; étiquettes et modèles doivent être ceux de la course ; `cout_fictif` au journal du bras ; même règle pour un proposeur externe simulé dans une course réelle ; essais |
| CL35-05 plafond du bras | plafond **externe** séparé relu dans le manifeste de départ (`budget_externe_usd`) moins le coût externe de la course ; vérifié **avant** l'appel de contrôle (contrôles + sessions) ; `PLAFOND_SESSION_USD` et `ROLE_POLE` passés à la commande |
| CL35-06 appel direct | `executer_ideation` refuse un adaptateur principal « commande-externe » (ou `.reel` d'un mixte) ; moteur « claude-sdk » exige l'adaptateur du kit et des modèles permis ; essai |
| CL35-07 devis contre lanceur | `--commande-externe` sans proposeur externe ni bras → refusé ; `--variable-transmise NOM` (répétable, nom de clé refusé) ; devis v6 |
| CL35-08 code 1 | `principal` enveloppé après l'analyse des arguments : toute exception → 2 |
| CL35-09 réglages du kit | `reglages_kit_par_role()` ({rôle : tools, effort}) et `delai_session_s` au manifeste de départ ; `--delai-session-s` ≤ 0 refusé |
| CL35-10 version de l'outil | `_find_cli()` du kit interrogé d'abord, PATH en repli |
| CL35-11 affirmations | réécrites (effort, aide de l'attestation, « déjà écrit », docstrings) |
| CL35-12 essais | coûts NaN / ∞ / 0 / négatif / sortie ≠ 0 avec coût ; bras simulé sur course réelle ; commande consignée ; **sous-processus qui pend avec un petit-enfant** |
| CL35-13 petit-enfant survivant | `Popen(start_new_session=True)` et `os.killpg` au délai ; essai qui vérifie la mort du petit-enfant |
| CL35-14 attestation | `verifier_scelle` sur toute attestation ; consigne lue **une fois** en octets, empreintée et envoyée telle quelle |

**Non corrigé, assumé** : le juge simulé reconnaît les témoins de l'exemple à leur nom (simulation seulement) ; le délai du
kit (`asyncio.wait_for`) n'est testé que sur un faux kit sans sous-processus (CL35-12, premier point : l'outil en ligne de
commande n'est pas lancé dans ce dépôt) — le petit-enfant est testé sur la commande externe seulement.

**317 essais passent** (312 + 5 : commande externe à coûts dégénérés, délai et groupe de processus, proposeur externe dans la
course avec attestation du matériau, bras à poids égal avec classement à trois juges et refus avant appel, panne d'Argon →
classement sans bras, bras simulé sur course réelle refusé, adaptateur principal externe refusé). Course simulée de bout en
bout avec proposeur et juge externes (15 fiches, aucun classement avant le bras) puis bras différé simulé (trois juges,
médiane, accords par paire, retenues) ; rejeu refusé ; options refusées (`--commande-externe` seul, moteur réel non armé → 2).

## Commandes

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -B -m unittest discover -s essais -t . -p 'test_*.py'                              # 317 essais
$PY -I -B demonstrations/ideation_v1.py SORTIE --liste-blanche L.json --question Q.md --piece … --temoins T.json \
    --piece-juge … --materiau M.md --seconde-passe --attestation-materiau ATT-M.json \
    --proposeur-externe argon=gemini-argon --commande-externe "…" --juge-externe argon-juge=gemini-argon   # course
$PY -I -B demonstrations/ideation_v1.py SORTIE --bras-rapporte-differe --juge-externe argon-juge=gemini-argon \
    --commande-externe "…" --attestation-lecture-humaine ATT.json                      # bras : classement à trois juges
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v36.txt
```

Lancement réel : `../ideation-organisme-approches-v1/devis-ideation-v6.md`. Le reste : LISEZMOI v35 à v1.
