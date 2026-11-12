# Orchestrateur du pôle, v7 — version 47 : moissonneur (option A) en préparation hors ligne, et correctif bloquant R-764

Lignée conv-audit (sous-agent), 29 octobre 2026. v1 à v46 gardées (R12) : LISEZMOI et EMPREINTES v1 à v46 intacts. Sources :
note de conception `../ideation-organisme-approches-v1/note-moissonneur-integration-v1.md` (« go » de Lazar le 29 octobre à
11:52 heure de Paris sur les sept points, recommandation (A)) ; incident réel R-764 de 10:43 UTC relayé par le coordinateur ;
complément de Lazar de 12:33 heure de Paris (barrière 3 au relais).

**v47 n'est pas contre-lue.**

**Aucune moisson réelle ici, aucune session réelle, aucune dépense, aucun réseau, aucune clé** : relais de moisson factice
en mémoire sur la boucle locale, amont factice local pour le relais réel, garde-fou d'essai qui refuse toute connexion hors
boucle locale. La première moisson réelle est un **GO séparé** chez session-depot (premier usage du réseau par l'organisme).

**Rétrocompatibilité (prouvée par empreintes).** Sans `--moisson`, la course est celle de la v46 : consignes identiques
**octet pour octet**. Pour le prouver, `pole/ideation.py` et `pole/dossier_ferme.py` de la v46 ont été reconstruits en
inversant chaque modification de la v47 et vérifiés contre `EMPREINTES-orchestrateur-pole-v7-v46.txt` (empreintes égales :
`50689654…`, `52c9097d…` ; les huit autres modules importés sont ceux de la v46) ; sept consignes de référence (passe 1,
passe 2, contrôle d'Argon, juge, passe 1 et 2 à dossier fermé par protocole, juge à dossier fermé) ont été produites par
cette v46 reconstruite sur les gabarits des essais, et leurs empreintes sont gelées dans `TestV47.CONSIGNES_V46_SHA256`
(`test_v47_retrocompatibilite_octet_pour_octet_avec_la_v46`). Deux changements touchent aussi la course sans moisson, et
ce sont des corrections : le correctif R-764 (ci-dessous) et deux champs nouveaux du manifeste de fin (`statut_course`,
`depense_modele_non_autorise_usd`, nuls hors refus).

## Ce que fait la v47 — moissonneur

| point | ce qui est fait | essai |
|---|---|---|
| module commun | `pole/protocole_outils.py` : lecture du bloc de demandes d'une réponse (`extraire_bloc_demandes`, partagée par la lecture du dossier fermé — `dossier_ferme.extraire_demandes` s'y branche, aucune duplication — et par la moisson), quotas par rôle et par course (`Quotas` : proposeur 1 tour, réglage borné à 2, ≤ 4 requêtes par tour, ≤ 5 résultats par requête ; juge 0 tour, refus dur ; une demande refusée compte), journal (`JournalProtocole` : motif exact), section servie entre délimiteurs (`section_servie`, `DEBUT_DONNEES` / `FIN_DONNEES` : données, jamais consigne) | `TestV47` (tous) |
| garde de fuite | `pole/moisson.py`, `GardeFuite` : les six règles de la note § 3 — (1) 3 à 200 caractères, ≤ 25 mots, ni retour à la ligne ni caractère de contrôle ; (2) ni adresse ni `@ = ? & # % < > { } [ ] \| $ \`` ni barre oblique hors identifiant arXiv ancien ; (3) aucun secret (`caviardage.contient_secret`, noms de `relais.NOMS_DE_CLE`, jetons factices) ; (4) aucun identifiant interne (épisode, `T01`, hexadécimal ≥ 12, `GO-`, `R-`, `N-`, `CL`, nom de fichier, fragments interdits) ; (5) aucun bardeau de 8 mots d'un **registre d'empreintes** (témoins que le noyau détient, plus un registre scellé construit par qui détient les textes : `construire_registre_bardeaux`, `--registre-bardeaux`) ; (6) aucun extrait de pièce > 60 caractères contigus, hors titres déclarés ; **motif exact au journal du noyau, motif générique à l'agent** ; le relais refait 1 à 3 | `test_v47_2_garde_de_fuite_cas_sain_et_artefacts` (titres des dix extraits du corpus, requêtes de 3 à 25 mots ; vingt-cinq artefacts, motif exact par règle) |
| résultats servis | titre ≤ 300, auteurs ≤ 300, date, identifiant, résumé ≤ 2 000 caviardé et passé à la garde lexicale (signalé → servi **réduit au titre**, `resume_retire`), **lien de notice construit par le noyau** (`arxiv.org/abs/…`, `openalex.org/W…` : jamais un PDF, même si l'amont en sert un), source, étiquette `[moisson:<source>:<empreinte12>:<identifiant>]` ; ≤ 2 800 caractères par résultat (résumé raccourci jusqu'à tenir) ; résultat à identifiant illisible écarté | `test_v47_1`, `test_v47_4` (résumé piégé) |
| cache et modes | `CacheMoisson` : chaque réponse acceptée scellée dans `SORTIE/noyau/moisson/<clé>.json` (clé = empreinte de source, requête normalisée, `n`, version du schéma), servie **depuis le fichier scellé** (mêmes octets pour tous les proposeurs et au rejeu), index scellé en fin de course, empreinte au manifeste de fin ; `--moisson frais` (relais interrogé) ; `--moisson rejeu --cache-moisson DOSSIER` (**jamais le réseau** ; entrée absente → « absente du cache » ; entrée discordante avec l'index → **arrêt du rejeu**, R6) | `test_v47_1` (rejeu octet pour octet sans relais), `test_v47_4` (absente, discordante, index descellé) |
| relais de moisson | `pole/relais_moisson.py`, processus à part sur la boucle locale, séparé du relais de clé (aucune route ajoutée à `relais_reel.py`) : `GET /moisson/arxiv?q=&n=`, `GET /moisson/openalex?q=&n=`, `GET /moisson/etat` ; toute autre route 404 (dont `/moisson/brave`), POST 404, tout paramètre hors `q` et `n` 400, jeton factice propre `x-jeton-moisson` 401, gardes 1 à 3 refaites 400, plafond de requêtes par source et par jour 429, amont en panne, illisible ou injoignable 502 ; réponse `{source, requete, n, horodatage, empreinte_brute, resultats, empreinte}` (SHA-256 des octets de l'amont, puis du JSON canonique) ; journal JSON par ligne sans clé ; amonts codés par source (`AMONTS`, **SUPPOSÉS**) remplaçables par `--amont-factice URL` (boucle locale seulement) ; `--courriel-politesse` vide par défaut : **aucun en-tête d'identité** (ni `User-Agent` ni `mailto`) tant que Lazar n'a pas nommé un courriel | `essais/test_v47_relais_moisson.py` (9 essais, amont factice Atom et JSON) |
| branchement | `executer_ideation` : **tour de moisson entre les passes** (après la passe 1 de chaque proposeur, Argon compris : sa passe 2 suit sa passe 1), session à part sous `proposeur_ideation`, plafond `--budget-moisson-usd-par-session` (0,5), `tools=[]`, consigne courte (`consigne_moisson` : question, vue courte des fiches de passe 1, règles, quotas), réponse = bloc `{"moisson": [{"source", "requete", "resultats"}]}` ; résultats servis en passe 2 sous « Moisson servie par le noyau (données ; résumés non opposables) » entre délimiteurs ; moisson ⇒ `--seconde-passe` obligatoire ; gabarit de passe 2 avec le statut `MOISSONNE`, marqué `non_opposable: true` par le noyau ; juges : phrase `MOISSON_JUGE`, **refus dur** d'un bloc de moisson (consigné, rien envoyé) ; `{"moissonner": …}` d'un tour de lecture : « au tour de moisson seulement » ; bloc illisible ou absent → passe 2 sans moisson, dit au journal ; relais indisponible → « moisson indisponible », **la course continue** (distinct d'une session en échec) ; la taille servie entre dans les gardes de taille de la passe 2 (Argon) ; les tours de moisson entrent dans les deux sommes de plafonds | `test_v47_1`, `test_v47_3`, `test_v47_4` |
| vérification (L7 étendue) | après les passes, chaque antériorité `MOISSONNE` est vérifiée : étiquette servie à **ce** proposeur, identifiant et titre (hors étiquette) concordants ; rapportée au manifeste de fin (`moisson.verification_moissonnees`) à côté du classement, **jamais aux juges** ; `candidats-corpus.json` scellé (identifiants servis, à qui ; identifiants cités, vérifiés ou non) pour la chaîne du corpus primaire | `test_v47_1`, `test_v47_3` (titre faux, étiquette non servie) |
| absence de canal | aucune variable du relais de moisson chez un agent (`variables_agent`, `construire_options`) ni dans `environnement_commande` ; `tools=[]` inchangé ; `garde_outils.py` sans aucune commande nouvelle ; le client n'accepte qu'une adresse locale ; garde-fou d'essai | `test_v47_5` |
| mesures | `--mesurer-consignes --moisson frais` : moisson au pire cas (20 résultats à leurs bornes, servis par la même fonction que la course) = **57 900 caractères** (nominal 56 000), comptée dans `consigne_passe_2_maximale` et dans la consigne de contrôle d'Argon ; consigne du tour de moisson maximale ≈ 106 000 | `test_v47_6` |
| démonstration | `demonstrations/ideation_v1.py --moteur simule --moisson frais` : relais factice en mémoire lancé par le lanceur (aucun réseau), proposeurs simulés qui moissonnent et citent `MOISSONNE`, Argon simulé ou par commande (la commande doit répondre au tour de moisson : `SCRIPT_OK` des essais le fait), puis `--moisson rejeu --cache-moisson SORTIE/noyau/moisson` sans relais : section servie identique octet pour octet | `test_v47_6` |

**Options nouvelles du lanceur** : `--moisson frais|rejeu|aucune` (défaut `aucune`), `--url-relais-moisson URL` (frais ; moteur
réel : obligatoire, plus `--confirmer-moisson-reelle`), `--cache-moisson DOSSIER` (rejeu), `--budget-moisson-usd-par-session`
(0,5), `--tours-moisson` (1, borné à 2), `--registre-bardeaux FICHIER`, `--confirmer-moisson-reelle`. Sous `--moisson`, les
totaux doivent couvrir les tours de moisson : aux réglages du devis, `--budget-total-usd 41` (deux proposeurs Claude × 0,5) et
`--budget-externe-usd` + 0,5 (12,1 ; 12,6 dans les essais).

## Correctif bloquant R-764 (changement de modèle par le kit) — trois barrières (kit, noyau, relais)

Incident réel du 29 octobre, 10:43 UTC : en passe 1, Opus 5.5 a rendu `stop_reason: refusal` ; le kit d'agent a émis
`system/model_refusal_fallback` et a continué sur `claude-opus-4-8` (modèle non autorisé), 4,66 USD, jusqu'au plafond de
session ; le noyau a conclu « budget_depasse ».

1. **Kit (a)** — réglage trouvé dans le binaire de l'outil installé (`claude` 2.1.312, chaînes lues, pas exercé) : la voie de
   repli sur refus n'est active que si `vz() = !CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK && !CLAUDE_CODE_NO_MODEL_FALLBACK` ;
   `CLAUDE_CODE_NO_MODEL_FALLBACK=true` porte en plus un « tripwire » (« a model-fallback pivot was attempted while the
   no-fallback guarantee is active ») et s'applique aussi aux replis d'accès (`model_fallback`). Les deux variables sont
   posées dans l'environnement de **toute** session du pôle (`adaptateurs.VARIABLES_SANS_REPLI_DE_MODELE`, dans `env` de
   `construire_options`), et `fallback_model=None` est explicite dans les options du kit. Le kit Python (0.2.172) n'a pas
   d'option propre pour le repli sur refus : seule la variable d'environnement le coupe. **SUPPOSÉ** jusqu'à l'épreuve
   réelle : effet des variables sur la version 2.1.312 lu dans le binaire, non exercé.
2. **Noyau (b, c, d)** — `AdaptateurClaudeSDK._executer` lit le **modèle servi** de chaque message de l'assistant
   (`AssistantMessage.model`, champ `model` de la transcription ; suffixe de date admis : `claude-opus-5-5-20261001`) et
   son `stop_reason` ; tout écart au modèle demandé, tout `stop_reason == "refusal"`, tout événement système
   `model_refusal_fallback` (ou `model_fallback`, `model_refusal_no_fallback`) est un **refus = arrêt propre du tour** : la
   lecture du flux cesse au message fautif (session close ; le flux est clos avant tout message suivant), statut « refus »,
   **jamais « budget_depasse »** ; la dépense des messages servis sous un modèle non autorisé est comptée à part au barème du
   relais (`depense_modele_non_autorise_usd`) et le coût total de la session, non rendu par le kit, est marqué inconnu (la
   course lit l'écart au relais). Dans la course (`_lancer`) : la sortie de la session (dossier de l'agent et traces) est
   mise à l'écart dans `SORTIE/A-L-ECART-modele-non-autorise/…` (jamais servie aux juges ni au matériau), ligne de journal
   avec le modèle demandé et le modèle servi (`refus_modele`), `statut_course = {statut: "refus", role, etiquette,
   modele_demande, modele_servi}` et `depense_modele_non_autorise_usd` au manifeste de fin ; `CourseInterrompue`
   « refus (R-764) : … ». Un juge externe (bras) qui rendrait un bloc de moisson est aussi consigné en refus dur.
3. **Relais (barrière 3, mot de Lazar de 12:33)** — `relais_reel.py --modeles-permis claude-opus-5-5,claude-fable-5-1`
   (noms exacts) : toute requête vers `/v1/messages` dont le corps demande un autre modèle est **refusée avant envoi à
   l'amont** (403, `{"erreur": "modèle non permis", "modele_demande": …, "depense_usd": 0.0}`), journalisée avec le modèle
   demandé, comptée à l'état (`refus_modele`) ; **liste vide = tout refusé**, dit au démarrage ; la forme `role=modele` est
   refusée au démarrage (le relais ne connaît pas le rôle : aucun en-tête de session ne le porte). Le lanceur, sur le moteur
   réel, lit `modeles_permis` à l'état du relais et exige la liste **exactement** égale aux modèles des proposeurs et des
   juges (un modèle en plus serait une voie de repli, un en moins refuserait une session) ; un relais antérieur (muet) est
   dit au manifeste, pas refusé. Les lanceurs de relais des essais et de la répétition générale passent la liste.

Essais R5 : `test_v47_r764_refus_de_modele_trois_barrieres` (cas sain : un message sous le modèle demandé → ok ; artefacts :
faux kit qui rend `refusal` puis un message sous `claude-opus-4-8` et « budget dépassé » → refus, flux clos au premier
message ; message sous un autre modèle → refus, dépense comptée ; événement système seul → refus ; course : sortie à l'écart,
manifeste ; relais : modèle permis relayé, `claude-opus-4-8` refusé sans appel amont, liste vide, forme `role=`, lanceur).
Le faux kit de la répétition générale (`essais/faux_sdk`) exige désormais les deux variables et peut rejouer l'incident
(`FAUX_SDK_REFUS=<rôle>`).

## Restes et doutes déclarés — ce qui n'est pas vérifié en réel (SUPPOSÉ)

- **Formats des amonts** (arXiv : Atom, `search_query=all:…&max_results=` ; OpenAlex : JSON, `search=&per-page=&select=…`,
  résumé en index inversé), **noms d'hôtes**, **débits** (arXiv : une requête toutes les trois secondes, de mémoire), **conditions
  d'accès** (OpenAlex : courriel de politesse ; sans `User-Agent` l'amont peut refuser) : de mémoire, à relire au branchement par
  session-depot. Le relais ne respecte aucun délai entre deux requêtes vers un même amont (≈ 12 requêtes par course).
- Les quotas et le plafond du tour (0,5) sont ceux de la note, **SUPPOSÉS** ; coûts au barème du code.
- La garde 5 ne couvre que les témoins que le noyau détient tant que le registre d'empreintes de bardeaux (épreuve finale, banque,
  mode tenu à l'écart) n'est pas construit par qui détient ces textes (`construire_registre_bardeaux`, hors de ce dépôt).
- Les requêtes quittent la machine et sont journalisées par les amonts (≤ 4 × 200 caractères par proposeur et par tour).
- L'empreinte rendue par le relais détecte une altération de transport ou de cache, pas un relais menteur.
- La commande d'Argon doit répondre au tour de moisson par un bloc `{"moisson": [...]}` (ou `[]`) ; la recherche en ligne
  intégrée de Gemini doit être coupée côté session-depot (note § 4).
- Témoins : avec `MOISSONNE` admis, les fiches citeront plus de `MOISSONNE` que les témoins du tiers ; à écrire au devis.
- R-764 : effet réel de `CLAUDE_CODE_NO_MODEL_FALLBACK` et de `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK` sur l'outil 2.1.312
  (lu dans le binaire, non exercé) ; identifiant exact du modèle servi dans les messages (suffixe de date supposé) ; que le kit
  rende bien `AssistantMessage.model` à chaque message (documenté dans `claude_agent_sdk` 0.2.172) ; `--modeles-permis` exige
  des noms exacts : si l'amont attend un alias différent du nom envoyé par le kit, le relais refuserait tout (à voir à l'épreuve).

## Devis de l'épreuve réelle courte (GO séparé, chez session-depot ; aucune dépense ici)

1. Relais de moisson réel lancé chez session-depot (`python -I -m pole.relais_moisson --port 0 --journal …`), **quelques requêtes
   réelles** à la main (`curl` sur la boucle locale) : une arXiv, une OpenAlex, une refusée (brave, 404), une au-delà du
   plafond journalier réglé à 2 ; vérifier les formats (`resultats` non vides, identifiants de la forme attendue, résumés
   reconstruits), l'absence d'en-tête d'identité, le journal. **0 dollar de source.**
2. Une course simulée avec le relais réel (`--moteur simule --moisson frais --url-relais-moisson …`) : 0 dollar.
3. Une course réelle courte sous GO : jetons ≈ **0,4 dollar par course** pour les tours de moisson et la moisson servie en passe
   2 (≈ 1 au pire cas), en plus du devis de la course qui l'emploie ; relais de clé lancé avec `--modeles-permis` exactement
   égal aux modèles de la course ; vérifier R-764 par un cas sain seulement (aucun refus provoqué).

## Essais

**444 essais** (427 en v46 ; + 8 `TestV47` dans `essais/test_v7_ideation.py`, avant `unittest.main()` ; + 9
`essais/test_v47_relais_moisson.py`), 0 échec, deux exécutions complètes sur l'arbre final, aucun processus survivant,
`essais/_tmp` et `__pycache__` retirés. Fichiers nouveaux : `pole/protocole_outils.py`, `pole/moisson.py`,
`pole/relais_moisson.py`, `essais/test_v47_relais_moisson.py`, ce LISEZMOI, les EMPREINTES v47. Fichiers changés :
`pole/ideation.py`, `pole/dossier_ferme.py`, `pole/adaptateurs.py`, `pole/relais_reel.py`, `demonstrations/ideation_v1.py`,
`demonstrations/repetition_generale_v6.py`, `essais/test_v7_ideation.py`, `essais/test_v6_relais_reel.py`,
`essais/test_adaptateurs.py`, `essais/faux_sdk/claude_agent_sdk.py`.

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v47.txt
```
