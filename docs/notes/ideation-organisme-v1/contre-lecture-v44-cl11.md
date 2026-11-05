# Contre-lecture CL11 du différentiel v43 → v44 — prise « idéation » (orchestrateur du pôle v7) et devis v7 nonies, voie (β)

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (lignée conv-audit), ni CL10, ni la préparation du
lancement. Relevés `date -u` : début **09:39 UTC**, fin **09:49 UTC**, le 29 octobre 2026. Aucun réseau, aucune clé, aucun
appel payant. Argon est joué par deux faux locaux : le faux Argon facturant de CL10 (copié sans changement, ne se borne
jamais) et, pour la vraie commande, un **faux serveur Gemini local** (`outils/faux_gemini_cl11.py`). Claude est le moteur
simulé, mis au pire cas (coût = plafond). Tout a tourné sur des copies (`copie/v44s`). « Démontré » : exécuté par moi ;
« à la lecture » : non exécuté.

## Verdict

**Voie (β) : non lançable sur la v44 telle quelle.** Un seul bloquant, connu et confirmé : les guillemets français
(CL44-01). Avec des témoins à « », la course part, paie, puis s'arrête avant le premier juge. Pire cas démontré sur la v44 :
**Claude 29,0 + Argon 8,7 = 37,7 USD perdus**, aucun classement, code 2.

**Lançable avec une v45 qui ne change que `anonymiser`** (et ses essais), sans autre ligne changée, sous deux réserves dites
au devis (CL44-02 pensées d'Argon, CL44-04 garde de la course à donner). Le reste tient, démontré :
- le lanceur **accepte** les réglages exacts du devis v7 nonies (somme externe 12,4 ≤ 12,8) et refuse sans dépense à 12,3 ;
- pire cas au plafond : **Claude 40,00, Argon 12,4, total 52,4**, classement à trois juges ;
- la vraie commande `commande_argon_v1.py` **borne chaque session à son plafond** ; le coût déclaré est exactement celui que
  le noyau compte.

## 1. Comptes vérifiés (démontré)

- **Empreintes** (09:39) : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v44.txt` → **158 sur 158 conformes**. Liste v44
  `68126ef3…`, LISEZMOI v44 `69d15838…` : ce sont celles du devis. Compagnons conformes. Devis v7 nonies `4b6a7d95…`.
  `commande_argon_v1.py` `f3acf365…` : conforme à `EMPREINTES-lancement-ideation-v1.txt`.
- **Différentiel** : `diff -rq v43 v44` → changent `pole/ideation.py`, `demonstrations/ideation_v1.py`,
  `essais/test_v7_ideation.py` ; s'ajoutent la liste et le LISEZMOI v44. Le patch couvre exactement ces fichiers.
- **Essais** : `env -i PATH=… HOME=… python3 -B -m unittest discover -s essais -t . -p 'test_*.py'` sur une copie :
  **Ran 412 tests in 298,3 s, OK**, code 0 (`sorties/essais-sortie.txt`). Le compte annoncé (412) est exact.
- **Arbres relus intacts** : relevé de 9:39 et de 9:49 identiques (`sorties/empreintes-debut.txt`, `-fin.txt`, `cmp` sans
  écart) ; aucun `__pycache__` dans `v43/` ni `v44/`.

## 2. CL43-01 à 08

| constat | verdict | preuve |
|---|---|---|
| **CL43-01** plafond propre à la passe 2 | **corrigé** | `--budget-passe-2-externe-usd 3.1` : somme 3,1 + 2,5 + 3,1 + 3,5 + 0,2 = **12,40**, acceptée ; à 12,3 : « somme des plafonds externes 12.40 > total externe 12.3 », code 2, avant tout appel, rien payé. La session de passe 2 reçoit bien 3,1 (`PLAFOND_SESSION_USD` lu par la vraie commande, § 4). Option refusée sans `--proposeur-externe` et `--seconde-passe`, ou non finie. Défaut M3 (passe 2 comptée au plafond de passe 1) : tué |
| **CL43-02** garde par passe avec provision | **corrigé** | Sous `--taille-max-consigne-externe 1490000`, passe 1 gardée à min(1 490 000 ; 884 819) **avant tout contrôle** ; passe 2 à 1 173 975 (fiches ≤ 8 000) ou moins (fiches plus grandes). Fiches de 9 066 : passe 2 **refusée avant envoi** (1 175 148 > 1 131 335), Argon 5,33 et non 8,5. Défauts M1, M4, M5 : tués. Réserve de l'auteur exacte : la passe 1 ne peut pas se garder sur ses propres fiches ; la vraie commande la borne (§ 4) |
| **CL43-03** reprise Claude sur relais relancé | **corrigé** | `filtrer_reprises_claude` : dépense lue plus basse → rejoué ; relais illisible ou dépense non lue → rejoué ; égale ou plus haute → repris (sonde). Défaut M2 (jamais rejoué) : tué. Reste un cas (CL44-07) |
| CL43-04 option du bras | **appliqué au devis** | devis et marche : ne pas donner `--taille-max-consigne-externe-bras` ; démontré : garde par défaut du bras avec provision (1 356 746 à 33 fiches servies, 1 206 746 aux réglages réels) |
| CL43-05 trois tentatives | **corrigé (devis et message)** | code inchangé (borne 3) ; le devis le dit ; message du lanceur : « bornée par les sommes ET par 3 tentatives » |
| CL43-06 fichiers changeants dans la commande | **à la charge du lancement, tenu** | la ligne de la marche ne nomme que `setpriv` et l'enveloppe, fixes. Voir CL44-06 (l'inverse) |
| CL43-07 / X01 | **essai ajouté** | `test_x01_fichier_d_entree_change_entre_deux_tentatives` présent et passant ; non muté par moi |
| CL43-08 seuil | **corrigé** | le devis dit 1 493 975 |

## 3. Réglages exacts du devis v7 nonies, pire cas et barème 8,3 (démontré)

Outil : `outils/scenarios_cl11.py` (copie de `scenarios_cl10.py`, réglages du devis v7 nonies : contrôle 3,1, passe 1 à 2,5
(défaut), `--budget-passe-2-externe-usd 3.1`, juge 3,5 (défaut), externe 12,8, garde 1 490 000, prix 8,3 ; bras : prix 8,3,
externe 12,8, **garde par défaut**). Pièce de 750 000, matériau de 350 000, quatre témoins sans guillemets, huit fiches,
seconde passe. Faux Argon facturant (sortie au rapport 5, **hypothèse**).

| scénario | le lanceur accepte ? | contrôle | passe 1 | passe 2 | bras : contrôle ; juge | Claude | Argon | total | issue |
|---|---|---|---|---|---|---|---|---|---|
| **pire cas au plafond** | oui | 3,1 | 2,5 | 3,1 | 0,2 ; 3,5 | **40,00** | **12,4** | **52,4** | trois juges |
| barème 8,3, fiches ≈ 4 500 | oui | 3,02 | 1,94 | 2,74 | 0,0001 ; 0,27 | 40,00 | 7,97 | 47,97 | trois juges |
| barème 8,3, fiches ≈ 7 300 | oui | 3,02 | 2,16 | 3,01 | 0,0001 ; 0,37 | 40,00 | 8,57 | 48,57 | trois juges |
| barème 8,3, fiches ≈ 9 066 | oui | 3,02 | 2,30 | **refusée avant envoi** | — | 0,4 | 5,33 | 5,73 | course perdue, aucun classement, SORTIE écrite |
| barème 8,3, fiches maximales | oui | 3,02 | **5,21 > 2,5** (faux Argon non borné) | — | — | 0,4 | 8,23 | 8,63 | course perdue ; avec la vraie commande : passe tronquée à ≈ 2,5 (§ 4), Argon ≈ 5,5 |
| externe 12,3 | **non** : 12,40 > 12,3, avant tout appel | — | — | — | — | 0 | 0 | 0 | aucun fichier |
| **témoin à « » (v44)** | oui | 3,1 | 2,5 | 3,1 | — | **29,0** | **8,7** | **37,7** | `JSONDecodeError` avant le premier juge, code 2, aucun classement (CL44-01) |

Concordance avec le devis : 12,4 ; 52,4 ; 7,96 (7,97) et ≈ 48 ; 884 819 ; 1 173 975 ; 5,33 ; 8,23 ; 1 493 975 : **tout
concorde**. Le refus et son moment : seul le cas « externe < 12,4 » est refusé au départ ; les fiches trop grandes sont
refusées à la passe 2, **avant son envoi**, après le contrôle et la passe 1 payés.

Mesure v44 sur les **vrais fichiers** (liste v4, sans témoins, `sorties/mesure-v44-*.txt`) : passe 1 **685 992**, passe 2
maximale 1 077 188, contrôle **1 077 663** (2,24 USD à 8,3), juge au maximum 2 755 895 ; garde de passe 1 884 819 (passe) ;
code 0. **Avec les témoins réels : code 2, `JSONDecodeError`** (CL44-01).

## 4. Vraie commande d'Argon, chaîne réelle de l'adaptateur (démontré)

`commande_argon_v1.py` réelle, lancée par l'**`AdaptateurCommandeExterne` de la v44** au travers d'une enveloppe factice
(`commande/enveloppe-factice.sh` : clé factice, mêmes options que la marche — `--compter-jetons --delai-s 1500 --prix-entree
8.3 --prix-sortie 41.5` — plus `--url-base http://127.0.0.1:8799/v1beta`). Le faux serveur rend, par défaut, **la sortie
maximale demandée** (`candidatesTokenCount = maxOutputTokens`), fin « STOP ». Sortie : `commande/essai-commande-sortie.txt`.

| cas | plafond | statut au noyau | coût déclaré = compté |
|---|---|---|---|
| contrôle 1 077 663 caractères, sortie maximale | 3,1 | ok | **3,099975** |
| passe 1 685 992, sortie maximale | 2,5 | ok | **2,499985** |
| passe 2 1 173 975 (garde de la v44), sortie maximale | 3,1 | ok | 3,099959 (16 000 jetons de sortie, soit ≈ 8 × 8 000 caractères : au bord) |
| juge 1 166 746, sortie maximale | 3,5 | ok | 3,499961 |
| compte exact plus dense (3,2 caractères par jeton) | 3,1 | erreur, code 4, **rien envoyé** | 1e-6 |
| entrée seule trop grosse (1 500 000) | 3,1 | erreur, code 4, rien envoyé | 1e-6 |
| sortie tronquée (`MAX_TOKENS`) | 3,1 | erreur, code 5 | 3,099959 (payé, course perdue) |
| **entrée facturée au-dessus du compte** (3,2 contre 4) | 3,1 | `budget_depasse` | **3,709 > 3,1** |
| **pensées facturées en plus de `maxOutputTokens`** (8 000) | 3,1 | `budget_depasse` | **3,432 > 3,1** |

**Course entière avec la vraie commande** (`simulee/C-commande-reelle/`, petites pièces, Claude simulé au plafond, réglages
(β)) : code 0, « en attente du bras ». Contrôle 3,099984 ; passe 1 2,499985 ; passe 2 2,810322 (sortie bornée à 65 536 par
`--max-sortie-jetons`, donc plafond 3,1 bien reçu). Coût calculé sur l'usage rendu par le serveur = coût déclaré par la
commande = `cout_compte_usd` du noyau, à 10⁻⁶ près ; `cout_externe_usd` 8,41 = 3,1 + 2,5 + 2,81.

Lecture. **Oui, la commande s'arrête à son plafond de session**, tant que l'usage facturé suit son estimation : entrée au
compte exact (`countTokens`), pensées comprises dans `maxOutputTokens`. Hors de ces deux hypothèses, elle dépasse
(CL44-02, CL44-03) ; le noyau compte alors le coût déclaré, au-dessus du plafond, et arrête la course. Les 29 essais de
`test_commande_argon_v1.py` ne sont **pas rejoués** : `pytest` absent de cette machine.

## 5. Nœud « relance après contrôles Claude payés : 40,4 > 40 » (démontré)

Sonde `outils/sonde_relance_404_cl11.py` (fonctions de la v44, réglages du devis : total 40, relais 40, réserve 4) :
- **relais relancé** (dépense lue 0) : les deux contrôles Claude sont rejoués ; somme de la relance 0,4 (payés) + 0,4
  (rejoués) + 28,6 (passes) + 11 (juges) = **40,4 > 40** : refusée sans dépense. **Chiffre confirmé.**
- **relais gardé** (dépense lue 0,4) : contrôles repris, somme 40,0 ; mais la garde du relais refuse :
  40 − 4 − 0,4 = 35,6 < 40 − 4.
- Donc, aux réglages du devis, **toute relance après contrôles Claude payés est refusée**, quel que soit le relais.
- Option (a) du devis : elle exige **aussi** `--plafond-usd 40.4` au relais, relancé à neuf (gardé : 36,0 < 36,4, refusé).
  Total au pire 40,4 + 12,4 = **52,8**, soit le GO. À écrire au devis.

## 6. Constats neufs

### CL44-01 — bloquant (connu, non corrigé dans la v44, confirmé) — `anonymiser` normalise la typographie sur le texte JSON

**Endroit.** `pole/ideation.py`, `anonymiser`, l. 588 :
`f = json.loads(normaliser_typographie(json.dumps(vue_servie(fiches[i]), ensure_ascii=False)))`. « » et “ ” deviennent des
`"` non échappés : `JSONDecodeError`.

**Défaut** (démontré sur la v44). Appel direct : fiche à « oui » et “non” → `JSONDecodeError` ; la même fiche sans
guillemets passe. `--mesurer-consignes` avec les témoins réels : code 2. Course (`simulee/G-guillemets/`, un témoin à « »,
réglages (β), pire cas) : le lanceur **accepte** ; le contrôle, les passes Claude et d'Argon sont payés ; arrêt avant le
premier juge. Claude 29,0, Argon 8,7, aucun classement. `verifier_reglages` n'anonymise pas les témoins : rien n'arrête
avant la dépense.

**Où porte le correctif (v45).**
1. Dans `anonymiser` (`pole/ideation.py`, l. 581 à 593) seulement : normaliser **chaque chaîne feuille** de
   `vue_servie(fiches[i])` (copie profonde, parcours récursif des dictionnaires et des listes, clés comprises si l'on veut),
   **jamais le texte JSON**. `normaliser_typographie` reste telle quelle. Elle n'a pas d'autre appel sur du JSON (seul appel :
   l. 588). `mesurer_consignes` (l. 1284), les juges Claude (l. 1649) et le bras (l. 1663) passent tous par là.
2. Garde avant dépense (recommandé) : dans `verifier_reglages`, anonymiser les témoins lus, pour qu'une erreur de cette classe
   arrête la course avant tout appel.
3. Essais : une fiche et un témoin à « » “ ” ‘ ’ servis aux juges ; course simulée jusqu'au classement ; texte servi
   normalisé (« → ") et JSON valide ; `--mesurer-consignes` avec les témoins réels → code 0.

### CL44-02 — majeur (non vérifiable hors ligne) — Les pensées d'Argon ne sont provisionnées nulle part

**Défaut.** La commande borne `maxOutputTokens` au reste du plafond, mais facture `thoughtsTokenCount` en plus. Elle ne pose
aucun `thinkingConfig`.
- Si l'interface ne compte pas les pensées dans `maxOutputTokens` : dépassement (démontré : 3,43 > 3,1 → `budget_depasse`,
  course perdue ; la somme des plafonds ne borne plus la dépense).
- Si elle les compte : les pensées mangent la sortie. La passe 2 à la garde de la v44 n'a que 16 000 jetons de sortie.
  → `MAX_TOKENS`, course perdue après ≈ 3,1 payés.

Avec les vrais fichiers, la marge est large : passe 2 réelle ≈ 0,76 million, ≈ 36 000 jetons libres. Le risque reste réel
si Argon pense longtemps.

**Correction.** Avant le GO : poser un budget de pensée explicite dans la commande, et le compter dans la garde. À défaut :
lire `thoughtsTokenCount` au journal du **premier appel** (le contrôle d'Argon), et arrêter si les pensées sont lourdes. Le
dire au devis.

### CL44-03 — mineur — La borne de la commande vaut « à l'erreur de compte près »

Entrée facturée au-dessus du compte exact : 3,71 > 3,1 (démontré). Le noyau compte le déclaré, sans écart. `--compter-jetons`
est dans l'enveloppe : il ferme le cas courant. Le compte plus dense que 4 caractères par jeton est refusé **sans envoi**
(code 4). Seuil du contrôle réel : ≈ 3,05 caractères par jeton (calcul). Rien à corriger ; à dire.

### CL44-04 — information (marche à suivre) — La garde de la course doit être donnée

Mesure v44 aux réglages du devis, vrais fichiers : **sans** `--taille-max-consigne-externe`, garde par défaut 1 013 975 <
contrôle 1 077 663, « passerait » faux ; la course serait refusée (sans dépense). **Avec** 1 490 000 : passerait vrai. La
ligne de l'étape 9 de la marche doit porter `--taille-max-consigne-externe 1490000` et `--budget-passe-2-externe-usd 3.1`
(au lieu de ses deux marqueurs), comme le devis.

### CL44-05 — mineur — Deux identifiants pour Argon

Le noyau écrit `gemini-argon` aux manifestes. L'enveloppe ne passe pas `--modele` : la commande appelle et vérifie
`gemini-4-argon`. La commande refuse bien un autre modèle servi ; mais aucun manifeste du noyau ne nomme le modèle réel.
**Correction** : consigner la correspondance au registre et au manifeste de run (R9). Ou bien nommer `gemini-4-argon` partout,
budgets compris.

### CL44-06 — mineur — Le script d'Argon n'entre pas dans l'identité de reprise

La ligne de commande nomme `setpriv` et l'enveloppe ; `commande_argon_v1.py` est appelé **dans** l'enveloppe (à la lecture).
`description()` n'en prend donc pas l'empreinte. Un changement du script entre deux tentatives laisserait reprendre le contrôle
d'Argon. Effet faible. **Correction** : ne pas changer le script entre tentatives ; consigner son empreinte au registre
(étape 7 de la marche, déjà prévue).

### CL44-07 — mineur — Reprise Claude jugée sur la dépense : un relais relancé dont la dépense remonte est « repris »

Démontré (`sorties/sonde-reprise-depense-remontee.txt`) : dépense lue 0,45 après relance, contre 0,2 et 0,4 lus après les
contrôles → repris à tort. Sans effet aux réglages du devis : toute relance après contrôles payés est refusée (§ 5). Cela
compte sous l'option (a). **Correction** (CL10) : un identifiant d'instance du relais dans la clé. À défaut : aucun appel
payant au relais relancé avant la relance.

### CL44-08 — information — Défauts réintroduits dans le code neuf

Six défauts, essais de `test_v7_ideation` (94). **Cinq tués** :
- M1 : la taille donnée désarme la provision ;
- M2 : contrôle Claude jamais rejoué ;
- M3 : passe 2 comptée au plafond de passe 1 ;
- M4 : provision de passe 2 sans les grandes fiches ;
- M5 : passe 1 non gardée avant les contrôles.

**Un survit** : M6, « passerait » de la passe 1 toujours vrai dans `--mesurer-consignes` (même trou que X34 en CL10 : sortie
lue par un humain, jamais vérifiée). Sans danger d'argent : la garde réelle refuse avant envoi.

**Compte.** Un bloquant (CL44-01, connu). Un majeur non vérifiable hors ligne (CL44-02). Quatre mineurs (CL44-03, 05, 06,
07). Deux informations (CL44-04, 08).

## 7. Non vérifié

- Le comportement réel de l'interface Gemini : pensées comprises ou non dans `maxOutputTokens` ; facturation de l'entrée
  contre `countTokens` ; prix de sortie (41,5 **supposé**) ; refus HTTP 4xx non facturés (supposé par la commande).
- Les 29 essais de `test_commande_argon_v1.py` (`pytest` absent). L'enveloppe réelle sous l'utilisateur `argon`, `setpriv`,
  le mandataire.
- Le vrai relais et l'en-tête d'espace de travail (réserve de la marche, étape 6.5).
- La taille réelle des fiches d'Argon sans borne.
- Le correctif CL44-01 lui-même (v45) : il demande une relecture ciblée et une mesure avec les témoins réels avant le GO.

## 8. Fichiers produits (sous `relecture-v44/cl11/`)

- `contre-lecture-v44-cl11.md` (ce rapport) et son compagnon `.sha256`.
- `outils/` :
  - neufs : `scenarios_cl11.py` (B-* au devis v7 nonies, G-guillemets, C-commande-reelle), `faux_gemini_cl11.py`,
    `essai_commande_cl11.py`, `sonde_relance_404_cl11.py`, `mutants_cl11.py`, `mesurer_cl11.sh` ;
  - copiés de CL10 sans changement : le reste.
- `sorties/` : `essais-sortie.txt`, `empreintes-debut.txt`, `empreintes-fin.txt`, `mesure-v44-*.txt`,
  `sonde-relance-404.txt`, `sonde-reprise-depense-remontee.txt`.
- `simulee/` : un dossier par scénario (journal d'Argon, `rapport.json`) et un `.log` par scénario.
- `commande/` : enveloppe factice, configuration et journaux du faux serveur, `essai-commande-sortie.txt`.
- `mutants/mutants.json` (copies supprimées) ; `copie/v44s` (copie de travail, à supprimer à volonté).

Aucun processus laissé actif (faux serveur arrêté par PID). Aucun dépôt git créé. Aucun réseau.
