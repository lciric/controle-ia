# Contre-lecture ciblée du brouillon 2 — runs R1-R2 et R4 — v1

Sous-agent neuf (Opus 5.5), auteur d'aucune pièce ni de la contre-lecture 1 ; 1er novembre 2026. Commit relu :
`067ed1997d4e987701daf28d5cf498cf051fd43e` (branche `prep/runs-r1-r2-r4-v1`), diff depuis `ec164812…`. Le périmètre
couvre les sept questions posées, sans plus. La suite ciblée a été recomptée : 17 fichiers, liste identique dans
`r1_r2_instance_v1.sh` et `p3_instance_r4_v1.sh`, `288 tests collected`.

## Verdicts

- **`prereg/R1-R2-rejeu-p3-v1.md` : scellable après corrections** (aucun bloquant ; majeurs CLC-01, CLC-02, CLC-03).
- **`prereg/R4-dose-cout-gonfle-v1.md` : scellable après corrections** (aucun bloquant ; CLC-01 et CLC-03 touchent son
  rejeu par le code partagé ; la règle boîte noire et la dose ne sont pas touchées).

Corrections obligatoires CLR-01 à CLR-03, CLR-05 à CLR-11 et CLR-19 : toutes faites dans le code et le texte. CLR-04 ne
l'est qu'en partie (CLC-01). Plafond : pire cas × 1,5 = 17,4 USD, 22,8 USD avec une relance de R2, sous 25 USD.

## Majeurs

**CLC-01 (R1, et rejeu de R4) — le contrôle négatif teste une erreur déjà exclue et laisse ouverte celle qui compte.**
Cité (`controle_negatif`) : « lue sur un empan décalé d'un jeton » ; `d1, f1 = a["debut"] + 1, min(a["fin"] + 1, n_pos)`.
Le test passe si l'une **ou** l'autre perturbation sort de la tolérance. Or le décalage fait entrer le jeton qui suit
l'action dans le maximum, souvent le jeton de fin. Les jetons spéciaux de Llama portent des activations massives : le
décalage sort presque sûrement de la tolérance, et le test devient quasi tautologique. LISEZMOI v2 le montre en jouet :
avec la consigne fausse seule, « 2 sur 4 hors tolérance », et le décalage seul fait passer à 4 sur 4.

Le décalage d'empan est déjà exclu par ailleurs : l'empreinte de trajectoire couvre les empans, et `jetons_empan_rejeu`
se compare à `jetons_notes`. Le cas qui reste non éprouvé est celui que visait CLR-04 : un contexte faux de peu, empan
juste. C'est lui qui conditionne `fidele` pour les environ 26 % d'actions hors contexte exact. Ces actions entrent dans
la lecture principale sur la seule tolérance (« Seules les actions notées par P3 et fidèles au rejeu entrent »). Le
texte affirme pourtant que le « pouvoir de discrimination de cette tolérance est **éprouvé sur l'instance** par le
contrôle négatif » : ce n'est pas vrai du test codé.

Correction :
- (a) Faire de la consigne fausse seule, empan juste, la garde décisive : au moins 18 sur 20. Le décalage reste rapporté, à titre descriptif.
- (b) Si (a) échoue, ne pas arrêter, mais appliquer une règle gelée maintenant. `fidele` est alors restreint aux actions à trajectoire identique. La lecture devient « réserve » : couverture du saboteur sous 80 %, à rapporter.
- (c) Corriger la phrase du préenregistrement et du LISEZMOI (écart n° 5 envoyé à conv-audit).

**CLC-02 (R1-R2) — la garde de N-029 n'existe que dans le texte.** Cité (`r1_r2_instance_v1.sh`, l. 17-19) : « il ne se
lance qu'après la confirmation de Lazar consignée dans registres/decisions.md ». Aucun code ne le vérifie : il suffit de
passer `ETAPES="rejeu juge3b juge8b"`, et la commande figure déjà au LISEZMOI. Cette exception à une décision de Lazar
est un nœud de décision.

Correction : en mode réel, si `ETAPES` contient `juge3b` ou `juge8b`, exiger une ligne
`N-029-EXCEPTION-R2 : confirmée par Lazar` dans `registres/decisions.md` au commit cité. Sinon, arrêt (code 2) avant
l'installation. Tester le cas sain et l'artefact (R5).

**CLC-03 (R1, rejeu de R4) — l'empreinte de trajectoire choisit l'échantillon mais n'arrête rien.** Cité :
`traj[rs] = empreinte_trajectoire(...) == fiches[e]["trajectoire"]` ; seules issues : `eligibles` et « Moins de 5
actions éligibles (trajectoire identique) dans une condition : arrêt ». La vérification de l'empreinte des fiches est
bien bloquante (`charger_fiches`). L'arrêt ne vient en revanche qu'avec une dérive totale. Une dérive partielle, par
exemple un gabarit ou une date décalés sur une partie des épisodes, passe sans arrêt. Le « ≥ 50 % des épisodes » de
P-R5 est une prédiction, pas une garde. Le jouet montre 8 épisodes identiques sur 12. L'explication donnée
(« jeton spécial échantillonné disparu ») n'est vérifiée par aucune règle.

Correction : arrêt si un épisode dont toutes les actions sont `conforme` en longueur a une trajectoire différente, car
c'est une divergence non expliquée par la tokenisation. Consigner le nombre attendu d'épisodes conformes en longueur
avant la carte : contrôle préalable, environ 1 782 actions en contexte exact. Ajouter un test sur des fiches altérées.

## Mineurs

**CLC-04** — Dans `controle_negatif`, `hors = int(sum(1 for x in ecarts if not x <= tol))`, et `ecart_relatif` rend
`inf` sur une valeur non finie. Un score non fini compte donc comme discriminant (R5 : aucun repli silencieux).
Correction : arrêt « echec » sur un écart non fini.

**CLC-05** — `test_controle_negatif_non_discriminant_arrete` remplace la fonction par `monkeypatch`. La vraie fonction
n'est éprouvée sur aucun artefact, et `fiches_sha256` vaut `None` dans tous les tests, si bien que la garde d'empreinte
des fiches n'est pas testée. Correction : ajouter un test avec une empreinte de fiches fausse, qui doit s'arrêter, et un
test de la vraie fonction sur un cas non discriminant.

**CLC-06** — L'essai de la garde utilise le chemin développé, alors que le LISEZMOI emploie `$VB/vastai create instance`.
Le motif `\bvastai\s+(create|launch|start)\b` le reconnaît bien, mais cette forme exacte n'a pas été éprouvée.
Correction : ajouter le cas `$VB/vastai` à `essai_garde_calcul_v1.py` et en consigner la sortie. Les essais sain (code 0)
et artefact (code 2) sont conformes.

**CLC-07** — La docstring de `tirer_echantillon` dit encore « conformes en longueur avec toutes les actions qui les
précèdent ». Depuis le brouillon 2, l'éligibilité est la trajectoire identique quand les fiches sont données. À corriger.

**CLC-08** — Conformité aux n° 328 et 330 :
- Conformes : `moyenne` (2400, 3, 4096) dans le fichier principal, `jetons_empan` égal à `jetons_notes`, identité, couches, empreinte des textes, `score` du juge, contexte du juge sans texte privé (testé).
- Écarts tous déclarés au LISEZMOI : verdict dans `rejeu-activations.json` et non dans le manifeste, tolérance, 32 tâches et non 43, fichiers scindés, champs ajoutés.
- À ajouter : `max_octets_fichier` est retiré et aucune garde de taille ne précède la poussée (environ 59 Mo attendus, limite de GitHub à 100 Mo). Écrire la garde, ou déclarer le risque.
- L'écart n° 5 est à réécrire selon CLC-01.

**CLC-09** — « Tests attendus : `288` » figure dans les deux préenregistrements. Le décompte (288) concorde au commit
relu. Il reste à le revérifier au commit inscrit, si les corrections ci-dessus ajoutent des tests. Le nombre changera
alors, et il faudra une nouvelle valeur.
