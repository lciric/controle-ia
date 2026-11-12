# Contre-lecture de la règle primaire v3 et du script v3 des lentilles sur les sondes de P3

29 octobre 2026, 11:01 à 11:20 UTC (`date -u`). Sous-agent neuf (R2) : je n'ai écrit ni la règle, ni la liste, ni le
script. Processeur seul, sans réseau, sans commit.

- **Lu** : `regle-primaire-v3/` ; le script v3 (`25a377ee…`), l'essai (`229ccfe3…`) et son journal ; la
  contre-lecture v2 ; `evaluation.py` ; noms, empreintes et couches de `sondes-figees.json` ; le vrai `tokenizer.json`
  (`79e3e522…`) ; les lignes R-741 et R-747 (`grep -n`).
- **Ni lu ni lancé** : aucune sortie de lentille, ni canal, ni consignes de P3, ni `donnees/`, ni traces. Le script v3
  n'a tourné que sur des entrées synthétiques, `verifier-concepts` compris.

## Verdict

**Exécutable après corrections, qui ne portent que sur la commande de lancement (section 6). La règle (`be020390…`),
la liste (`aac34d5c…`) et le script (`25a377ee…`) restent tels quels.**

- Rien de bloquant.
- Un constat majeur, CLR3-01 : la commande d'usage ne contrôle pas l'empreinte du script, et une copie à graine changée
  passe sans refus.
- Le reste est mineur ou de l'ordre de l'information.

## 1. La règle

**Bornes, en fractions exactes** (`outils/bornes_regle_v3.py`) :

| Point | Règle | Recalcul |
|---|---|---|
| α par test | 0,05/32 | 1/640 = 0,0015625 |
| Isotropes | n_iso ≤ 14 | 15/10 001 = 0,0014999 ≤ 1/640 < 16/10 001 ; 14 est le plus grand entier admis |
| 200 isotropes insuffisants | 1/201 > α | 0,004975 > 0,0015625 |
| Faux « cohérent » sur 32 tests | ≤ 0,048 | 480/10 001 = 0,047995 sous toute dépendance (0,024 par lentille) |
| Planchers | n_pl ≤ 2 | ⌈0,99 × 200⌉ = 198ᵉ statistique d'ordre, soit le troisième plus grand ; niveau 3/201 ≈ 1,49 %, non corrigé |
| Test du signe | minima de 6-0 à 13-3 | retrouvés un à un pour b + c de 6 à 16 |

- L'équivalence « S > quantile `inverted_cdf` ⇔ n_pl ≤ 2 » est vérifiée sur 20 000 cas entiers avec ex aequo.
- Compter « ≥ » rend le test conservateur en cas d'ex aequo.
- S ≥ 2 et la condition des planchers ne font que retirer des « cohérent ». La borne de 0,048 tient donc.
- Ce qu'elle couvre : la nulle isotrope globale, rien de plus. Elle ne couvre pas une direction apprise qui suit les
  grands axes de la covariance. Aux couches 7 et 23, c'est la seule nulle de 12 sondes sur 16. La règle le dit.

**CLR3-04 — mineur. Les déclencheurs d'audit (R4) sont en partie asymétriques.**
- Côté « trop beau », trois déclencheurs agissent à la case (S ≥ 10, un seul mot, mots larges seuls).
- Côté « trop mauvais », il n'y a que « X = 0 pour les deux lentilles », alors que « X ≥ 12 » suffit pour une seule.
- Il manque deux miroirs à la case :
  - liste propre en tête de −w (signe inversé) ;
  - case rejetée par les seuls planchers.
- Proposition, sans retoucher la règle (toute retouche ferait une v4) : rapporter ces deux cas en descriptif. La sortie
  les porte déjà (`comptes_par_concept_moins`, `verdict_sans_planchers`).

**Liste de mots : appliquée comme écrit.**
- L'outil de l'auteur, rejoué, redonne octet pour octet le candidat (`31680609…`), les exclusions (`282a5708…`) et la
  liste finale (`aac34d5c…`).
- Contrôle indépendant de E6 (`outils/verifier_liste_independant_v3.py`, sans le script ; il tient lieu de
  `verifier-concepts`) :
  - « tromperie » : 80 mots, 96 jetons ; « enjeux » : 142 mots, 189 jetons ;
  - aucun mot final sans jeton ;
  - aucun des 177 mots retirés par E6 n'a de jeton ;
  - listes disjointes.

**CLR3-05 — mineur. Le jugement est appliqué de façon inégale.**
- « crucial » et « vital » sont retirés, mais « critical », « serious » et « severe », venus de la v2, restent.
- « hidden » est retiré, mais « hide » et « secret » restent.
- Il reste un registre code et sécurité :
  - « enjeux » : fatal, critical, severity, breach, compromised, killed, dead ;
  - « tromperie » : secret, hide, fake, spoof, phishing.
- « safety » contredit la règle « pas d'antonyme ».
- La nulle isotrope ne contrôle pas ces mots, et le déclencheur « mots larges » n'en couvre que 7.
- Ce n'est pas un écart, puisque la liste est scellée. C'est une réserve de lecture : citer les mots de chaque case
  « cohérente » (`mots_du_concept_en_tete`).

## 2. Le script contre `besoins-script-v3.md`

| Point | État | Preuve |
|---|---|---|
| B1, 16 sondes, sans les principales | conforme | mode unique ; refus `compte-sondes`, `sondes-inattendues`, `principale-selectionnee`, `principales-inattendues` ; principales jamais décodées (seul leur sceau est recalculé) ; absentes de la sortie |
| B2, 10 000 isotropes | conforme | `SeedSequence(entropy=20261029, spawn_key=(sha256(étiquette)[:8],))`, comme en v2 ; étiquette `isotropes-v3/c<couche>` ; entropie et clé au manifeste (R9) |
| B3, comptes entiers | conforme | `verdict_v3` sans quantile ; bords 14/15, 2/3, 1/2 testés ; constantes recalculées au lancement ; 200 planchers exactement, à la couche 15 |
| B4, énoncé et liste | conforme | constante = fichier, octet pour octet (`be020390…`) ; liste contrôlée en dur ; 16 préfixes = tableau de la règle |
| B5, ensemble et comparaison | conforme | X, niveaux, borne 480/10 001 ; grille, b, c ; p par `math.comb` ; phrase seulement si p ≤ 0,05 |
| U1 à U4 | conforme | scores z sur 200 isotropes, en cache ; CLJ2-01 corrigé ; script et règle committés (`3ffca78f`) |

**L'option `--essai-factice` ne fuit pas d'elle-même.**
- Elle vaut faux par défaut, et rien d'autre ne la pose.
- Elle ne change aucun calcul.
- Elle est écrite dans la sortie et dans le manifeste.

**CLR3-02 — mineur. Rien n'empêche cette option sur le vrai run.**
- Preuve : l'artefact F1 (run `20261019-230011-p3-reel`, avec l'option) est accepté.
- Effet : les 16 préfixes codés en dur ne sont plus contrôlés, et la lecture réelle est étiquetée « factice ».
- Correction : la commande de la section 6 refuse l'option. Dans une v4, refuser l'option si le run est celui de la règle.

**Informations, sans correction demandée.**
- CLR3-06. Le refus des scores z imprime deux valeurs z, descriptives, d'une case réelle.
- CLR3-07. S et les nulles passent par deux chemins numériques :
  - S : le vocabulaire entier, puis un masque ;
  - les nulles : un lot sur les seuls débuts de mot.

  Un ex aequo au dernier bit, au 20ᵉ rang, pourrait les départager autrement. Le recalcul indépendant de l'essai donne
  32 cases identiques sur 32 : l'effet est négligeable.
- CLR3-08. Le verdict descriptif « au seuil v2 » emploie les 200 premières isotropes v3, pas les tirages v2. Il faut
  l'étiqueter ainsi.

## 3. Essai factice et artefacts

**Essai relancé** (11:05 à 11:08 UTC, code 0) :
- 54 contrôles OK sur 54, mêmes libellés que le journal livré ;
- `sortie-A.json` identique octet pour octet à la sortie livrée (`12dbb79d…`, même machine).

**Mes artefacts** (`outils/artefacts_cl_v3*.py`, entrées synthétiques ; les copies altérées du script restent dans le
bloc-notes) :

| Artefact | Attendu | Obtenu |
|---|---|---|
| Témoin, script livré | accepté | accepté (X = 2 sous la jacobienne, 3 sous les logits) |
| G1 graine 20261030 | refus | **accepté** ; n_iso d'une case passe de 1 à 2 ; seul le manifeste le trahit |
| G2 étiquette `isotropes-v2` | refus | **accepté** ; même case, n_iso passe de 1 à 4 |
| P1 principale renommée, principales du fichier inchangées | refus | `compte-sondes` (17) |
| P2 principale renommée, principales mises à jour | refus | `principales-inattendues` |
| F1 `--essai-factice` sur le run réel simulé | refus | **accepté** (CLR3-02) |
| H1 planchers de « tromperie » à la couche 14 | refus | `planchers-hors-couche-15` |
| Z1 score z direct décalé de 10⁻³ | refus | `incoherence-interne` |
| S1 sonde non principale renommée | refus | `sondes-inattendues` |
| C1 N_ISO_MAX = 15 | refus | `incoherence-interne` (borne 0,0512 > α) |
| N1 fichier de poids d'un autre jeu | refus | `empreinte-sondes-npz` |

Aucun refus n'a écrit de sortie.

**CLR3-01 — majeur, sur la commande.**
- Le script ne recoupe ni sa graine ni son étiquette avec l'énoncé (G1, G2). Il ne peut pas contrôler sa propre
  empreinte.
- La seule défense est donc le contrôle en dur de `25a377ee…` avant le lancement, que la section 8.4 de la règle exige.
- La commande d'usage du script ne fait pas ce contrôle. Il lui manque aussi :
  - le contrôle de l'état committé ;
  - l'interpréteur `.venv`, qui a torch ;
  - un chemin absolu pour `diag/`.
- Correction : la section 6. Dans une v4 éventuelle : recouper au lancement la graine, l'étiquette, K et N avec
  l'énoncé.

**CLR3-03 — mineur (R5).**
- Six gardes nouvelles n'étaient pas testées sur un artefact par l'essai. Je les ai testées : P2, H1, S1, C1, Z1, N1.
  Toutes refusent, et toutes passent sur le cas sain.
- Les gardes héritées de la v2 ne sont pas retestées ici.

**Métadonnées réelles** (sans lentille) : sceau, run, principales, 16 sondes et préfixes conformes ; 400 planchers à
la couche 15.

## 4. Écarts signalés par l'auteur

- **Refus total si une case manque** (la règle dit « aucun verdict » ; le script n'écrit rien) : **acceptable**.
  - C'est plus strict que la règle, sans repli silencieux (R5), et cela évite une lecture partielle.
  - Le prix : pas de descriptif pour les 31 autres cases.
- **Tirages en lignes** : **acceptable**.
  - La règle fixe l'entropie et l'étiquette, pas la disposition. La loi est la même.
  - La disposition est déclarée et fixée avant la lecture.
  - Les lignes sont même le meilleur choix : 10 blocs de 1 000 lignes = un tirage de 10 000 lignes (vérifié), alors
    qu'en colonnes le résultat dépend de la taille des blocs.
  - Condition : ne jamais en changer après lecture.
- **Garde des scores z qui refuse tout** : **acceptable**.
  - Elle est testée sur cas sain et sur artefact (Z1).
  - Elle ne peut qu'empêcher un verdict, jamais en changer un.
  - Sa tolérance de 10⁻⁴ est large devant l'arrondi de la simple précision.

## 5. Réserves à écrire avec la lecture

- CLR3-04 et CLR3-05 : −w, les cas rejetés par les seuls planchers, les mots de chaque case « cohérente ».
- Les réserves de la section 7 de la règle restent entières. En particulier, quatre sondes ont déjà été décodées en
  descriptif par l'exécution v2 (R-741).

## 6. Commande de lancement sûre

À lancer seulement avec le GO de Lazar. Essayée à blanc, dernière ligne remplacée par `echo` : tous les contrôles
passent.

```
DEPOT=/home/user/controle-ia-travail
L=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/lentilles-p3
R=$DEPOT/docs/notes/lentilles-sondes-p3-v1/regle-primaire-v3
S=$DEPOT/docs/notes/lentilles-sondes-p3-v1/script-v3/comparaison-jlens-logitlens-sondes-p3-v3
D=$DEPOT/diag/20261019-230011-p3-reel
PY=$DEPOT/.venv/bin/python
SORTIE=$L/sortie-reelle-v3
CMD=("$PY" -I -B "$S/comparaison_jlens_logitlens_sondes_p3_v3.py" comparer --sondes non-principales-lineaires
  --sondes-json "$D/sondes-figees.json" --sondes-npz "$L/entrees/sondes-figees-legeres.npz"
  --lentille "$L/entrees/lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt" --lentille-config "$L/entrees/lentille-config.yaml"
  --desembedding "$L/entrees/model-00004-of-00004.safetensors:lm_head.weight"
  --norme-finale "$L/entrees/model-00004-of-00004.safetensors:model.norm.weight"
  --vocabulaire "$L/entrees/tokenizer.json" --concepts "$R/concepts-sondes-p3-v3.json"
  --enonce-regle "$R/enonce-regle-primaire-v3.txt" --empreintes-attendues "$L/entrees/empreintes-entrees-v2.txt"
  --revision-modele 0e9e39f249a16976918f6564b8830bc894c89659 --sortie "$SORTIE/sortie-jlens-sondes-p3-v3.json")
test ! -e "$SORTIE" && \
( cd "$L/entrees" && echo "cc244631f52a50cb60a6ace42ce073f7feedbd707c90b675db1d7e5d75f78259  empreintes-entrees-v2.txt" | sha256sum -c - \
    && sha256sum -c empreintes-entrees-v2.txt ) && \
( cd "$S" && echo "25a377ee4682e3b53d60b06499ac13b80fe9157b702d7b7b8fa94f057227b5e2  comparaison_jlens_logitlens_sondes_p3_v3.py" | sha256sum -c - ) && \
( cd "$R" && printf '%s  %s\n' \
    aac34d5cb52637fef6ebdd0d36009f8842efdef52d5e5298334e3a84f388bf6c concepts-sondes-p3-v3.json \
    be02039011c50c50a4eca0c38c26c7d31c38f6fc7315567659e8fd6cb7b64820 enonce-regle-primaire-v3.txt \
    0dae38e6c5de172e8ca8e49c6bbb52fb5da393873bf133e019746a57f5418dc6 EMPREINTES-regle-v3.txt \
  | sha256sum -c - && sha256sum -c EMPREINTES-regle-v3.txt ) && \
( cd "$D" && sha256sum -c sondes-figees.json.sha256 ) && \
test -z "$(git -C "$DEPOT" status --porcelain -- "$S" "$R")" && \
case " ${CMD[*]} " in *" --essai-factice "*) false ;; *) true ;; esac && \
"$PY" -c "import torch" && \
"${CMD[@]}"
```

Aucun test de refus sur les vraies entrées (CLJ2-06). Verser la sortie scellée au dépôt avant de la lire.

## Fichiers (ce dossier, chacun avec son sceau compagnon)

- `contre-lecture-regle-script-v3.md` ;
- `relance-essai-factice-v3.journal.txt` ;
- `artefacts-v3.journal.txt` ;
- `liste-et-bornes-v3.journal.txt` ;
- `outils/` : `bornes_regle_v3.py`, `verifier_liste_independant_v3.py`, `artefacts_cl_v3.py`, `artefacts_cl_v3_b.py`.
