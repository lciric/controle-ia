# Brief de reprise — nouvelle session mère, autre compte — 8 novembre 2026 — v1

Écrit par la session mère `session_01Qi7Gr6NLmhhAcdmnACBC7G` le 8 novembre 2026 vers 06:14 UTC (`date -u`), sur demande de Lazar (« fais la passation et brief pour nouvelle instance autre compte qui reprenne exactement au même endroit »). Tu ne connais rien de la conversation précédente : tout ce qu'il faut est ici et dans les fichiers cités. **La continuité vit dans les fichiers.** Lis aussi `CLAUDE.md`, puis la passation `registres/passations/2026-11-08-0614.md`.

## 0. Où on en est, en trois lignes
1. **Épreuve de l'étiqueteur, phase 1** : générée, déposée chez le tiers (05:54:40Z), essai de format fait et conforme. La lecture principale est **à lancer**, section 4.2 de l'ordre scellé. C'est **ta première action**, après la mise en place et la restauration (§ 2 et § 3). Lazar veut des résultats vite (« accelere je veux des resultats »).
2. **E3 bis de T0.6** : elle tourne sur Vast (instance 59671807), menée par la fille 6 de l'ancien compte, qui pousse ses comptes rendus sur la branche `rapports/fille-6-e3bis-v1`.
3. **Fille 10** (ancien compte) : bras B v4 (tolérance 0,3, lecture stricte), addendum v3, puis candidat 12 de T0.6. **Organisme** : code v65 confié à un développeur neuf dans le conteneur de l'ancienne mère (voir § 5).

## 1. Mise en place sur le nouveau compte
- **Dépôts** à rattacher : `lciric/controle-ia-travail` (privé ; `main` = dépôt de travail), `lciric/ideation-organism` (public). **Ne jamais pousser le dépôt de travail vers `lciric/controle-ia`.**
- **Variables d'environnement, par leur nom seulement** (jamais lire, afficher ni recopier une valeur) :
  - `GEMINI_API_KEY_2` : Argon, **réservée à l'épreuve de l'étiqueteur** (R-1754) ;
  - `KIMI_API_KEY` : Kimi, par le relais local ;
  - `OSF_TOKEN` ;
  - `VAST_API_KEY` ;
  - `HF_TOKEN` ;
  - `CONTROLE_IA_GITHUB_TOKEN_2` ;
  - `GEMINI_API_KEY` : autres usages d'Argon.

  Vérifie leur présence par le nom : `[ -n "${NOM:-}" ] && echo présente`.
- **Réseau** : `generativelanguage.googleapis.com`, `api.moonshot.ai`, `api.osf.io`, Vast, Hugging Face, GitHub.
- **Python** : `cd /home/user/controle-ia-travail && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt`. Le chemin `/home/user/controle-ia-travail/.venv/bin/python` est **écrit dans l'ordre** : clone le dépôt de travail exactement à `/home/user/controle-ia-travail`. Ici tournaient Python 3.13.18 et numpy 2.4.6 ; il faut numpy ≥ 1.25.
- **Mot de Lazar dans ta session** : le contrôle de permissions refuse une dépense sans le mot de Lazar écrit dans la session qui l'engage. Avant 4.3, demande-lui une phrase du type « go lecture principale de l'étiqueteur sous GO-2026-11-07-07 et GO-2026-11-08-03 ». Les deux GO sont déjà au registre.

## 2. Routine de reprise (R14)
`cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` ; lire `registres/etat.md` (section du 8 novembre, 06:14 UTC) et la passation. Pas de suite complète de pytest avant la lecture principale : les essais propres à l'épreuve sont rejoués en 1.4 ; lance la suite complète pendant que la lecture tourne.

## 3. Priorité 1 — lecture principale de l'étiqueteur (commandes exactes)

**Fait foi** : l'ordre scellé `docs/procedures/ordre-execution-phase1-epreuve-etiqueteur-v1.md` (`30f265a9a1c49a6af734c71a69cdc444989f9ec1c6e294525f43035a28705f18`) et le texte scellé `prereg/preenregistrement-epreuve-etiqueteur-v1.md` (`f73455b8…`).
- Tu deviens « la session mère » **et** l'exécutante (R-1756).
- Règles de l'exécutante, valables pour toi :
  - aucune réponse des lecteurs ouverte, aucun item, aucune clé, aucun tirage, aucun résultat ;
  - seulement des codes, des comptes, des empreintes et les champs nommés par l'ordre ;
  - arrêts par numéro de processus ;
  - on n'écrase jamais.
- **Écart déjà tranché** : le contrôle des factures (3 bis) a été levé par Lazar (GO-2026-11-08-03, « pas la peine on avance »). Le feu vert de la lecture principale est déjà écrit au compte rendu.

**3.1 Restaurer l'état** (archive scellée, branche `prep/etiqueteur-phase1-reprise-v1`, commit `f8b5ab72c0610456cc07185e0596e1140e0bace8`) :
```bash
cd /home/user/controle-ia-travail
git fetch origin refs/heads/prep/etiqueteur-phase1-reprise-v1:refs/remotes/origin/prep/etiqueteur-phase1-reprise-v1
A=diag/etiqueteur-phase1-v1/etat-etiqueteur-phase1-avant-lecture-principale-v1.tar
git show f8b5ab72c0610456cc07185e0596e1140e0bace8:$A > /tmp/etat-etiqueteur-v1.tar
echo "201e1295e0e820498b44e766e74a62e5a567f8903f3d63f96974e5e074ccc56e  /tmp/etat-etiqueteur-v1.tar" | sha256sum -c -
test ! -e /home/user/epreuve-etiqueteur-phase1-v1 && tar -xf /tmp/etat-etiqueteur-v1.tar -C /home/user
```
L'archive contient la racine telle qu'elle était à 06:10Z. Elle exclut l'arbre du code, les journaux de console et le relais annulé. Elle **contient la clé de construction** (`generation/cle-epreuve-v2.jsonl`) : ne l'ouvre jamais.

**3.2 Arbre du code et contrôles** (ne rejoue pas 1.1, la racine existe ; de 1.2, seulement l'arbre) :
```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
git -C "$DEPOT" fetch origin refs/heads/main:refs/remotes/origin/main
git -C "$DEPOT" cat-file -e "$COMMIT_CODE^{commit}" && git -C "$DEPOT" worktree add --detach "$CODE" "$COMMIT_CODE"
test "$(git -C "$CODE" rev-parse HEAD)" = "$COMMIT_CODE" && echo "commit du code conforme"
( cd / && sha256sum -c "$CR/empreintes-generation-v1.txt" ) && echo "génération identique au dépôt chez le tiers"
( cd / && sha256sum -c "$CR/empreintes-lecture-format-v1.txt" ) && echo "essai de format identique"
sha256sum "$FORMAT/manifeste-lecture-phase1-v4.json"   # attendu 3a3d868ebc15e995040c9c70807e801589bd02dda4bf7725865c1e22580222a2
```
Puis les blocs 3, 4, 5 et 6 de l'ordre (1.3 empreintes et GO, 1.4 essais, 1.5 variables de clé, 1.6 port libre) :
```bash
cd /home/user/controle-ia-travail; O=docs/procedures/ordre-execution-phase1-epreuve-etiqueteur-v1.md; X=docs/procedures/outils-reprise-etiqueteur-v1
for k in 3 4 5 6; do .venv/bin/python -I $X/extraire_bloc_ordre_etiqueteur_v1.py $O $k /tmp/bloc-$k.sh && bash /tmp/bloc-$k.sh; echo "code bloc $k = $?"; done
```
Attendu (comme le 8 novembre à 05:50Z) : douze « OK » et `code sha256sum=0` ; `1` pour le GO ; `entropie 17812956677980471985` ; 24, 6, 79 et 12 essais passés ; deux « présente » ; « port 8789 libre ». Un seul écart : arrêt, et tu l'écris au compte rendu.

**3.3 Lecture principale** (section 4 de l'ordre ; blocs dérivés scellés sous `docs/procedures/outils-reprise-etiqueteur-v1/`) :
```bash
cd /home/user/controle-ia-travail; O=docs/procedures/ordre-execution-phase1-epreuve-etiqueteur-v1.md; X=docs/procedures/outils-reprise-etiqueteur-v1
for k in 18 19 20; do .venv/bin/python -I $X/extraire_bloc_ordre_etiqueteur_v1.py $O $k /tmp/bloc-$k.sh; done
bash /tmp/bloc-18.sh                                    # 4.2 : relais neuf, plafond 298.83, 2 280 appels
bash $X/bloc-4-2-etat-avant-relais-principale-v1.sh     # attendu : max_appels 2280, plafond_usd 298.83, appels 0, numéro conforme
bash /tmp/bloc-19.sh                                    # 4.3 : lecture détachée ; appel ordinaire, il rend la main aussitôt
```
- Puis le guet : `bash /tmp/bloc-20.sh`, lancé **avec** `run_in_background` et un `timeout` de 7200000. Il rend la main au plus tard après 14 minutes. À chaque « lecture en cours » : `bash $X/bloc-4-4-surveillance-principale-v1.sh` (nombres seulement), puis relancer le guet.
- **Arrêts de 4.4** :
  - 8 items « illisible » ou plus pour un lecteur ;
  - tentatives sans progrès pendant 45 minutes ;
  - dépense estimée cumulée au-delà de 300.
- À la fin : `bash $X/bloc-4-5-apres-fin-principale-v1.sh` (état et arrêt du relais, champs du manifeste, empreintes), puis le bloc 21 de l'ordre (contrôle des empreintes des réponses, sans les ouvrir). Ajoute ensuite le contrôle du champ `lecteur` (couple CO-16, déjà dans le bloc 21).
- **Durée attendue** : environ 3 à 4 heures (essai de format : Argon environ 23 s par item, Kimi environ 29 s ; 456 items par lecteur, un fil par lecteur, valeur gelée).
- **Dépense estimée** : environ 35 USD au barème scellé (Argon compté environ 5 fois au-dessus de son prix public). Inscris l'engagement au registre `registres/depenses.md`.
- Un lancement disparu n'est **jamais** relancé par toi (couple CO-05) : nœud de Lazar.

**3.4 Analyse et verdict** (section 5 de l'ordre) :
1. Un **sous-agent neuf** (ni auteur du texte scellé, des scripts, de l'ordre, ni exécutant) refait le contrôle des empreintes et du champ `lecteur`, puis lance `analyser_phase1_v3.py analyser` (commande exacte au bloc 22).
2. Un **autre sous-agent neuf** prononce le verdict de phase 1 selon les critères gelés (texte scellé, « Critères de lecture gelés », phase 1).
3. Tu scelles le verdict, puis tu le soumets à Lazar.
4. Le résultat dit si l'étiqueteur est « validé contre la construction », « non validé » ou « non tranché ». La phase 2, avec des humains, ne vient qu'après un verdict « validé » et une décision de Lazar.

## 4. E3 bis de T0.6 (fille 6, ancien compte)
- Instance **59671807** (A100 80 Go, 2,069444 USD/h, créée 05:47:22Z), ordre `docs/procedures/ordre-fille-6-t06-e3bis-v3.md` (`1e2e3259…`), commit d'épreuve `c01d29ea` (`prep/t06-v11`), plafond 5,70 USD (GO-2026-11-07-08). La garde de dépense arrête l'instance vers **08:28Z** ; suite ciblée lancée à 05:51:30Z.
- La fille 6 pousse ses comptes rendus sur `rapports/fille-6-e3bis-v1` : lis-les avec `git fetch origin refs/heads/rapports/fille-6-e3bis-v1:refs/remotes/origin/rapports/fille-6-e3bis-v1`. Inscris la facture finale au registre des dépenses.
- **Ce qu'on attend d'E3 bis** : les jalons E3-3 à E3-9, la dernière ligne exacte de la suite ciblée (elle fixe `T06_TESTS_ATTENDUS` pour la course) et le texte exact de `show instance` après destruction.
- **Si la fille 6 se tait** et que l'instance vit encore après 08:35Z :
  - inventorie par identifiant, sans afficher de sortie brute ;
  - si elle tourne sans tâche, détruis-la par son identifiant, avec `-y` (R10) ; il faut d'abord le mot de Lazar dans ta session ;
  - écris l'arrêt dans `registres/arrets.md` ;
  - **ne touche jamais** aux instances 58936096, 58936099, 58936100.
- **Suite de T0.6** : candidat final, puis scellement le 9 ou le 10 novembre, puis **course le 11 novembre** (carte : GO-2026-11-07-02, A100 ≤ 1,30 USD/h pendant 3 heures de recherche, sinon H200 NVL ≤ 4,70 ; plafond 200 USD, GO-2026-11-02-28).

## 5. Autres chantiers en vol
- **Fille 10** (ancien compte, `session_01Qi7Gr6mEgRP9Fa25C4uBjB`, injoignable pour toi) : bras B v4 (`TOLERANCE_SCORE = 0.3`, lecture stricte ; GO-2026-11-08-01), addendum v3 à sceller **avant toute lecture**, puis candidat 12. Elle pousse ses rendus sur des branches `prep/…` et un index sur `rapports/fille-10-v1`. À toi : contre-lire (sous-agent neuf), sceller, intégrer.
- **Organisme, code v65** (GO-2026-11-08-02 : bras réel seul, génération 2 complète, 40 + 5 USD) :
  - un développeur neuf a été lancé vers 05:59Z dans le conteneur de l'ancienne mère ;
  - consigne scellée : `docs/notes/organisme-boucle-reelle-v1/consigne-developpeur-organisme-v65-v1.md` (`2dc207e7…`) ;
  - si son travail n'est pas poussé sur `lciric/ideation-organism`, branche `prep/organisme-v65-boucle-reelle`, relance un développeur neuf avec la même consigne ;
  - ensuite : contre-lecture, machine `bwrap` (pièce M0, plafond machine de 5 USD), préenregistrement scellé, puis la course.
- **T0.7** : réécrire le jeu J-C après la remise à zéro du 10 novembre vers 05:00 UTC (registres).
- **Nœuds anciens de Lazar** : registre `registres/etat.md`, section « GO et nœuds en attente ».

## 6. Règles et interdits (en plus de `CLAUDE.md`)
- Jamais lire, afficher ni demander une valeur de clé ; variables vérifiées par leur nom seulement.
- Garde des secrets à 0 avant tout commit : `git diff --cached | grep -c -E 'sk-ant-api03-[A-Za-z0-9_-]{40,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE[ ]KEY|sk[-]proj-|AIza[0-9A-Za-z_-]{35}'` (les motifs « PRIVATE[ ]KEY » et « sk[-]proj- » sont écrits ainsi pour que ce texte ne déclenche pas la garde ; ils reconnaissent les mêmes chaînes).
- Références `donnees/bras-attaque*` et `donnees/mode-tenu-a-l-ecart*` (et `docs/notes/bras-attaque/`) jamais vues ; branches `calcul/…` interdites à l'écriture sans le mot de Lazar.
- Jamais de `git fetch` sans refspec explicite. Heures par `date -u`, ou aucune heure.
- Aucune dépense sans GO sur devis ; publication, contact, dépôt public : nœuds de Lazar.
- Aucune sortie brute de `vastai` affichée ; destruction par identifiant avec `-y`.
- Ne jamais contourner un refus du contrôle de permissions, ni le faire faire ailleurs.
- Pousser `main` par `git push origin HEAD:main` (avec retentatives à 2, 4, 8 et 16 secondes).

## 7. Empreintes et commits utiles
| objet | chemin ou référence | empreinte ou commit |
|---|---|---|
| ordre de la phase 1 | `docs/procedures/ordre-execution-phase1-epreuve-etiqueteur-v1.md` | `30f265a9…` |
| texte scellé | `prereg/preenregistrement-epreuve-etiqueteur-v1.md` | `f73455b8…`, commit `d858b66f` |
| code de l'épreuve | `docs/notes/epreuve-etiqueteur-v1/` | commit `64e67cbd` (sur `main`) |
| archive de l'état | `prep/etiqueteur-phase1-reprise-v1` | `201e1295…`, commit `f8b5ab72` |
| dépôt chez le tiers | projet privé `dr57c`, `depot-epreuve-etiqueteur-phase1-v1.json` | `ab240b40…`, 2026-11-08T05:54:40.935302Z |
| manifeste de l'essai de format | `lecture-format/manifeste-lecture-phase1-v4.json` | `3a3d868e…`, dépense estimée 1.164904 |
| prix d'Argon | `docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html` | `ad2140dd…` (2 et 10 USD par million jusqu'au 30 novembre) |
| ordre E3 bis v3 | `docs/procedures/ordre-fille-6-t06-e3bis-v3.md` | `1e2e3259…`, commit d'épreuve `c01d29ea` |
| décisions du jour | `registres/decisions.md` | R-1755 à R-1760 ; GO-2026-11-08-01 à 03 |
