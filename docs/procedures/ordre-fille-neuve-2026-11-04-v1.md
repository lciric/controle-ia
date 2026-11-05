# Ordre de la session mère (instance fusionnée) à la fille neuve, 4 novembre 2026 — v1

Écrit le 4 novembre 2026 vers 01:35 UTC (`date -u`) par la session mère `session_01Qi7Gr6NLmhhAcdmnACBC7G` (rôles conv-audit et
session-depot fusionnés, R-1450). Destinataire : la fille neuve créée juste après, porteuse des clés que Lazar a posées dans
l'environnement (mot de Lazar, 01:22 UTC : « tu as toutes les cles … lannce une session fillle neuve »). Cet ordre **complète**, sans
les remplacer : `docs/procedures/creation-session-fille-v2.md` (§ 2 et § 4 : brief et installation) et
`docs/procedures/ordre-fille-a1-v3-seconde-v1.md` (`8236b9ea…`, avec l'ordre v1 qu'il cite). Partout où ces textes disent
« session-depot », lis « la session mère ». Aucune clé affichée ni écrite ; arrêts par identifiant de processus seulement (R10) ;
aucune lecture d'une sortie avant son scellement ; tout écart à un ordre : rien ne part, tu me le dis.

## 0. Communication
- Tu m'écris par `send_message` à `session_01Qi7Gr6NLmhhAcdmnACBC7G` (court : ce qui est fait, commit, empreintes, dépense) ; chaque
  rapport complet est aussi un fichier scellé poussé (voir chaque tâche).
- Commits : `-c user.name="Lazar Ciric" -c user.email="lciric@ens-paris-saclay.fr"`, avec les lignes d'attribution de ton
  environnement ; avant chaque poussée, la garde des secrets du brief vaut 0, sinon pas de commit.
- Branches neuves seulement (`donnees/…` pour les sorties) ; tu ne pousses jamais sur `main` ni sur `canal/conv-audit-n04`.

## 1. Installation (sans dépense)
Comme `creation-session-fille-v2.md` § 2, points 2 à 4 : présence de chaque clé **par son nom** (`env | grep -o '^NOM='`) et rapport
(noms présents, noms absents) ; clone de `main` dans `/home/user/controle-ia-travail` si ton environnement ne l'a pas déjà ; branches
d'outils par refspec explicite seulement (jamais `donnees/bras-attaque*` ni `donnees/mode-tenu-a-l-ecart*` ; compte des refs
`donnees` au journal) ; relais et commandes sous `env -i`, chacun éprouvé par l'appel de contrôle (« Réponds seulement par le mot
OK », plafond 0,05 USD), modèle servi égal au modèle demandé.

## 2. Tâche A — appel unique à Astra (GO-2026-11-04-01, 3 USD)
- Pièces sur `main` : `docs/notes/weight-space-programming-v1/question-astra-sparks-v1.md` (`ac88944d…`), `piece-1-billet.txt`
  (`49b2db7e…`), `piece-2-nos-resultats.md` (`d6fa8011…`) : `sha256sum -c` de leurs compagnons ; tout écart : rien ne part.
- Prompt servi, dans cet ordre : le texte de la section « Question (servie telle quelle) » (de la ligne qui suit son titre jusqu'à la
  ligne qui précède « ## Pièces jointes »), puis `=== Pièce 1 : billet ===` et le fichier entier, puis `=== Pièce 2 : nos résultats
  publics ===` et le fichier entier. Écris ce prompt dans un fichier, scelle-le avant l'appel.
- Appel : commande Astra 8807 (`outils/commandes-a1-bis-v1`), modèle `gpt-6-astra`, effort de raisonnement le plus haut que la
  commande offre, plafond de session 3 USD, **un appel** (une relance au plus sur panne déclarée du fournisseur) ; modèle servi
  vérifié.
- Sortie : réponse brute, jetons et dépense au journal ; scellement (`EMPREINTES-appel-astra-sparks-v1.txt`) avant toute lecture ;
  branche neuve `donnees/appel-astra-sparks-v1` partie de `main` ; garde des secrets à 0 ; message à la mère (commit, empreintes,
  dépense). Tu ne commentes pas la réponse.

## 3. Tâche B — seconde course d'A1-v3 (GO-2026-11-03-01, 400 USD)
- Suis `ordre-fille-a1-v3-seconde-v1.md` à la lettre, avec l'ordre v1 qu'il cite pour ce que tu dois remettre en place (pièces de
  la mini-course, commande Argon et relais 8805, registre de dépense, `collisionneur_v7.py`), empreintes contrôlées.
- **Le « lance » est donné par cet ordre** : mot direct de Lazar « go seconde course A1-v3 » (GO-2026-11-03-01), go permanent R-1059
  et ses cinq conditions, mots de Lazar de cette nuit (01:20 UTC « avance en autonomie pendant 12h sur les programmes controle ia et
  organisme » ; 01:22 UTC, la fille neuve). Il ne vaut **qu'après** : l'installation faite, la vérification
  (`--verifier-seulement`) en code 0, la garde de session éprouvée sur un processus factice (§ 1 de l'ordre). Envoie-moi la sortie de
  la vérification avant le départ, puis pars sans attendre de réponse si tout est conforme.
- Registre des GO servi au lanceur : `registres/go.md` de `canal/conv-audit-n04` (tête `7a4e5a56` ou plus récente).
- Pendant la course : **aucun autre usage d'Argon** (relais monofil). Ta session reste active jusqu'à la fin (attente suivie par ton
  harnais, relevés au journal toutes les 2 minutes au plus).
- Fin : comme le § 5 de l'ordre (branche `donnees/attaque-goodhart-v3-a1v3-seconde-v1`, rapport scellé, message à la mère).

## 4. Ensuite
Le tour du collisionneur (GO-2026-11-04-02) aura son ordre propre, sans Argon tant qu'A1-v3 court. Rien d'autre sans ordre écrit.
