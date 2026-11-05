# Orchestrateur du pôle, version 0.7.0 — corrections du premier lancement réel, pari à fraction — LISEZMOI v5

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5 pour cette version), v5 écrite à partir de 15:28 UTC
(heure lue sur `date -u`) ; v1 à v4 gardées telles quelles (R12). Ce qui change en v5 : **les huit défauts de plomberie du
premier lancement réel (a)** (lecture : `../premier-lancement-reel/lecture-lancement-reel-a-v1.md`, `9305a3b4…`), et le
**pari à fraction** (levier de puissance du juge, garantie inchangée). Rien d'autre ne change.

## Pourquoi la génération 1 de (a) a été perdue

La synthèse de la génération 0 a écrit la leçon « toujours écrire reponse.txt » (d'après la plainte d'un vérificateur) ;
injectée dans la consigne de chaque expérimentateur de la génération 1, elle leur a fait écrire le fichier que
l'orchestrateur se réservait ; l'écriture de l'orchestrateur, qui n'écrase jamais, a échoué cinq fois sur cinq. Les
invariants de l'orchestrateur dépendaient de l'obéissance des agents : ce n'est plus le cas.

## Ce qui change en v5

| défaut de (a) | correction | fichiers |
|---|---|---|
| 1. noms de fichiers partagés avec l'agent | toutes les traces de l'orchestrateur (consignes, réponses, leçons) vont dans un **dossier voisin** `traces-<dossier de l'agent>`, hors de portée de l'agent (garde et bac à sable) ; consignes : « ta réponse est ton dernier message » ; la synthèse écrit sur la science, jamais sur la plomberie | `pole/outils.py` (`dossier_traces`), `pole/cycle.py`, `pole/pole.py`, `pole/proposeur.py`, `pole/recombinaison.py` |
| 2. une erreur compte comme un essai | une erreur de l'orchestrateur laisse la fiche **indécise et rejouable** (`erreur_orchestrateur`), jamais retirée ; **arrêt du pôle** si la moitié au moins des fiches lancées d'une génération sont en erreur (au moins deux) | `pole/cycle.py`, `pole/pole.py` |
| 3. mesure de qualité flatteuse | nouvelles clés : témoins **jugés** par le pari, **vraies promues** (puissance), témoins **en erreur**, non jugés ; `etat_dents` ∈ {« dents », « pas de dents », « dents non mesurées »} ; « pas de dents » = témoins vrais jugés, aucun promu ; promotions étiquetées `sans_dents` ou `dents_non_mesurees` ; les clés historiques (« testés » = servis) restent pour les lecteurs existants | `pole/cycle.py` |
| 4. double règlement du budget | l'issue garde ses coûts même en erreur ; une réservation n'est réglée qu'une fois | `pole/cycle.py` |
| 5. consigne du vérificateur ambiguë, empreintes orphelines | sous le pari : « aucun verdict chiffré à confirmer » ; les compagnons `.sha256` des fichiers exclus du rejeu sont exclus aussi | `pole/cycle.py` |
| 6. faux positifs de la garde | la garde **sépare le code du shell** : corps des redirections `<<FIN` destinés à un interpréteur ou à `cat`/`tee`, arguments de `python -c` (`node -e`…) = code, où seuls les littéraux de chaîne sont des chemins (premier composant existant) ; corps destinés à un shell ou à une commande inconnue = shell (strict) ; redirection sans fin refusée ; substitutions `$(…)` lues comme du shell | `pole/garde_outils.py` |
| 7. bac à sable inactif | **moteur réel refusé** si `bwrap` ou `socat` manque, ou si `bwrap --ro-bind / / --dev /dev --unshare-net true` échoue ; exception seulement par `--accepter-sans-bac-a-sable --motif-sans-bac-a-sable "…"`, **jamais sous root** ; faux moteur de la répétition générale reconnu (`EST_FAUX_SDK`) ; état consigné au manifeste et au bilan | `pole/adaptateurs.py`, `pole/pole.py`, `essais/faux_sdk/claude_agent_sdk.py` |
| 8. réserve du relais sous le coût d'un appel | réserve par défaut **0,40 USD** par appel (0,266 au plus vu en (a)) ; dépassements de réserve comptés (`appels_au_dessus_de_la_reserve`, `depassement_max_usd`) et journalisés par appel | `pole/relais_reel.py` |

**Pari à fraction** (`--pari-fraction`, `ConfigGeneration.pari_fraction`) : le numérateur de la richesse devient le
mélange bayésien, sur la grille λ ∈ {0,25 ; 0,5 ; 0,75 ; 1}, des lois λ·p_h + (1 − λ)·m_t, où m_t est la marginale en
ligne (Laplace 0,5) des issues précédentes ; la grille est déclarée dans l'engagement, sous son empreinte. C'est une loi
prévisible : le rapport à tout membre du nul reste une martingale de test (inférence universelle), la garantie de Ville
tient. Prix : au plus log 4 contre la meilleure fraction. `pole/selection_pari.py` (`GRILLE_FRACTIONS`,
`trajectoire_numerateur`), `pole/nul_filles_v2.py`, `pole/cycle.py`, `pole/pole.py`.

## Essais (R5)

- `essais/test_v7_plomberie.py` (nouveau, 11 essais) : un agent qui écrit `reponse.txt`, `consigne.txt`, `lecons.json`
  dans tous ses dossiers ne casse rien sur deux générations (bras proposeur compris) ; erreur trois générations de suite :
  fiche indécise, zéro essai ; arrêt quand tout est en erreur ; erreur après l'expérimentateur : coût gardé, budget exact ;
  qualité : témoin vrai en erreur → « dents non mesurées », témoin vrai jugé sans agent et promu → « dents » ; copie du
  rejeu sans réponse, consigne ni empreinte orpheline ; garde : 9 commandes saines (dont les cinq faux positifs de (a)) et
  15 interdites ; bac à sable : présent et fonctionnel, dépendance absente, bwrap en échec, exception sans motif, exception
  sous root, exception hors de root, faux moteur ; relais : réserve et dépassements.
- `essais/test_v7_pari_fraction.py` (nouveau, 5 essais) : grille {1} = pari plein au jeton près ; prix borné par log 4 ;
  **puissance** : loi juste mais trop confiante (poids × 4), 40 répétitions de 200 instances : promue **12 fois sur 40**
  au pari plein, **40 sur 40** à fraction (loi bien calibrée : 40 et 40) ; **contrôle fatal** : sous le nul (issues i.i.d.,
  600 répétitions de 120), loi la plus agressive, promotions **4 sur 600** à fraction (0,7 %), 10 sur 600 au pari plein
  (1,7 %), sous α = 5 %.
- Trois essais anciens lisent les traces au nouveau chemin (`test_cycle`, `test_cycle_v3`, `test_recombinaison`).
- **184 essais** au total (voir la section « Lancer »).

## Démonstration : le pari à fraction sur la banque réelle T0.5

`demonstrations/demo_couche1_v7.py`, bras « fraction » ajouté (v3 de la démonstration, lecture F1 à F3 fixée avant
l'exécution, en tête du fichier). Course du 27 octobre, 15:25 UTC, 14 s, bras « aveugle » et « fraction » :
- F1 : aucun témoin faux promu sous « fraction » : **tenu** ;
- F2 : témoins vrais promus : **0 sur 5** sous « fraction » comme sous « aveugle » ;
- F3 : aucune fiche promue par « fraction » seule.

Lecture : le pari à fraction **réduit les pertes** (e-valeurs finales des témoins de −17,4 à −3,1, par exemple) mais ne
monte pas le maximum : le meilleur témoin vrai culmine à log W ≈ 2, loin de log(m/α) ≈ 7,5 qu'exige e-BH. **Le levier ne
suffit pas sur cette banque** : il faut la banque v3 (couche 1 bis). Sortie :
`/tmp/…/scratchpad/demo-couche1-v7-v3-fraction/` (non versée : une seule course, rien de neuf hors de cette lecture).

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v5.txt
$PY -I -B -m unittest                                                   # 184 essais, environ 3 minutes
$PY -I -B demonstrations/demo_couche1_v7.py DOSSIER_NEUF --generations 3 --bras aveugle,fraction   # 14 s
```

**Course de contrôle « (a) bis »** (moteur réel, chez session-depot ; décision et dépense chez lui) : bac à sable actif
exigé ; **`python -I -B pole`** (et non `python -I -m pole`, qui échoue en mode isolé : faux départ de (a)) ; témoins
avec agents (pas de `--temoins-sans-agent`) pour éprouver le vérificateur ; même monde que (a).

```bash
# relais, dans son propre environnement (la clé n'y est lue qu'une fois, puis effacée) :
python -I -B pole/relais_reel.py --port 8787 --plafond-usd 15 --journal RELAIS.jsonl --variable-cle NOM_DE_LA_VARIABLE
# orchestrateur, sans aucune variable de clé :
env -i PATH="$PATH" HOME="$HOME" python -I -B pole --moteur claude-sdk --confirmer-moteur-reel \
  --url-relais http://127.0.0.1:8787 --selection pari --monde-noyau exemples/monde-pari-demo-v1.json --noyau-secret \
  --population exemples/population-pari-demo-4traits-v1.json --temoins exemples/temoins-pari-demo-4traits-v1.json \
  --generations 2 --budget-usd 15 --modele-experimentateur claude-opus-5-5 --modele-verificateur claude-fable-5-1 \
  --modele-recombinaison claude-opus-5-5 --modele-synthese claude-opus-5-5 --sortie DOSSIER_NEUF \
  --horodatage "$(date -u +%H:%M) UTC"
```

À lire après : les questions de la section 1 de la lecture de (a), plus « aucune erreur de l'orchestrateur », « au moins
un témoin vrai jugé », `etat_dents`, `bac_a_sable` du manifeste, `appels_au_dessus_de_la_reserve` du relais.

## Limites connues

- La garde reste une barrière par motifs : un code obscurci (chemin encodé, script écrit par l'outil Write puis exécuté)
  la franchit ; seul le bac à sable borne vraiment le système de fichiers et le réseau. D'où le refus sans bac à sable.
- Dans le code, un chemin absolu dont le premier composant n'existe pas (par exemple `/x.txt`) n'est pas refusé par la
  garde (pour ne pas refuser les expressions régulières et chemins d'URL) ; le bac à sable refuse l'écriture.
- Le pari à fraction n'aide pas sur la banque T0.5 v2 (trop petite) ; son gain ne se lira que sur la banque v3.
- Le reste : LISEZMOI v4.
