# Journal — barreau 6, candidat 3 — v1

Même rédacteur (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; même consigne (`f86a6834ccf0d0f8b53d3821c2a52495c711837e07563633059170a4765da7c2`), mêmes interdits ; aucun commit, aucun appel de modèle, aucune dépense ; candidats 1 (`b8bbea6a…`) et 2 (`0716d3d5…`) intacts. Je n'ai ouvert ni le verdict ni aucune sortie de `agregation-r1-v4`, ni aucune sortie de T0.7 ou de P3-bis, ni la ligne R-2273. Heures relevées par `date -u`.

## 1. Entrées et vérifications (21:13:08 UTC)

- Message de la mère (R-2278, R-2279) : `COMMIT_CODE_ACCB6` = `6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625` ; énumération v2 ; compteurs ; deux couples de VB6-3 ; rendu de « non interprétable » ; « Reste avant le scellement » (contre-lecture du code par un autre modèle, VB6-4 ; fusion après le scellement de T0.7 ; fichier et ligne `CODE-ACCB6` au commit final, entropie de R-2274).
- Complément 3 du développeur, lu entier : `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v1-complement3-v1.md`, `23c758e7e2813998c223e5723511386f2b1d111598b6ca0a35a43746043ece29`, égal à son compagnon.
- Vérification courte du candidat 2 : `prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md`, `d35055ff1ac72264e94a6a83228f49963d4e7b227a7d7853733b281989f2d5dd`, égale à son compagnon ; lus : titres, § 6 (VB6-3 à VB6-7) et § 7.
- Au commit `6c98ea20…`, par `git show` (aucun `checkout`) : `5ee8a4ac…` en est l'ancêtre ; `scripts/enumeration_etats_accb6_v2.py` `a6dbfdd85ba2ff0e92fd905ff3f144f5397f7f97990411e0786f1c38605d31d9` et `scripts/enumeration-etats-accb6-v2.txt` `00088af568388a4fbe381b7d80b97883b242013d99c7c5893bde54b9e741873e` (2 152 lignes), égaux au complément 3 ; `garde_v1.py` `5b91bfaa…` et `phrases_v1.py` `961ea2b3…`, égaux au complément 3 ; gabarit de la phrase « non interprétable » dans `phrases_v1.py` : « non interprétable : un prédicteur trivial d'épisode, nommé, sépare au moins autant ({triviaux}) ».

## 2. Couples C3-01 à C3-16

| couple | où | quoi | section du préenregistrement ? |
|---|---|---|---|
| C3-01 | titre | « candidat 3 » | non |
| C3-02 | en-tête, date | heure du candidat 3, journal | non |
| C3-03 | en-tête, statut | candidat 3 = candidat 2 + C3-01 à C3-16 ; sections touchées déclarées | non |
| C3-04 | en-tête, commit du code | `6c98ea20…` (parent `5ee8a4ac…`) | non |
| C3-05 | en-tête, documents | complément 3, vérification courte, commit | non |
| C3-06 | « Ce que les auteurs savaient » | lectures du candidat 3 | non |
| C3-07 | section « Code », « État » | commit `6c98ea20…`, 171 essais (dont l'essai des 1 188 phrases), 71 mutations sur 71, phrases de (i) alignées (VB6-1, VB6-2), garde de non-relance (`garde_v1.py` `5b91bfaa…`, logique inchangée) | non |
| C3-08 | section « Code », énumération | script v2 `a6dbfdd8…`, sortie v2 `00088af5…` au commit cité ; la v1 reste versée | non |
| C3-09 | « Reste », pas 2 | VB6-3, premier couple, tel qu'écrit (entropie : `ecrire_fichier_code(…, entropie=…)`, R-2277) | non |
| **C3-10** | **Plan d'analyse, point 6** | **VB6-3, second couple, tel qu'écrit** : « tirée une fois par la session mère avant l'inscription de `CODE-ACCB6` (R-2274) » au lieu de « tirée à l'inscription » | **oui, déclaré** : formulation de l'origine de l'entropie ; aucun signe, seuil, niveau ni règle d'état |
| **C3-11** | **Critères de lecture gelés, table des phrases, dernière ligne** | « … sépare au moins autant ([prédicteurs nommés]) » : le code écrit les prédicteurs nommés entre parenthèses (R-2279) | **oui, déclaré** : rendu de la phrase ; le mot « nommé » y était déjà ; aucun état ni condition changés |
| C3-12 | « Reste », en-tête | « au candidat 3 » | non |
| C3-13 | « Reste », pas 1 | contre-lecture du code par un autre modèle que son développeur, avant la ligne `CODE-ACCB6` (VB6-4) | non |
| C3-14 | « Reste », pas 2 | fichier `CODE-ACCB6` au commit final (`6c98ea20…` au candidat 3 ; il suit un commit neuf éventuel) ; une seule ligne | non |
| C3-15 | « Reste », pas 4 | fusion au commit final après le scellement de T0.7 (raison écrite) | non |
| C3-16 | « Reste », pas 5 | vérification courte du candidat 3 ; VB6-6 ouvert, non demandé | non |

Citations de `5ee8a4ac…` gardées à dessein (statut du candidat 2, lectures du candidat 2, parent du commit, origine de la garde, notes du pas 2) : le script les imprime.

## 3. Exécution

- Constructeur des couples : bac à sable, `…/c3/construire_couples_c3.py` (`10c473aac9cfcab31ae454ab6c785c893a16b91ec55c107146c717af405dbaaf`, non versé) ; il applique les couples en mémoire et vérifie chaque « ancien » une fois.
- Script `accumulation-barreau6-v1-candidat3-faire-v1.py` (dérivé du script du candidat 2, remplacements contrôlés un par un) essayé sur une copie du bac à sable, puis lancé dans le dossier du brouillon (21:15 UTC) : « 16 couples appliqués ; marqueurs restants : `REVERIFICATION_T07_SCELLE` ; TOUT PASSE ; candidat 3 : `d48fb8a3…` ». `controle_ia.prereg.problemes` : seul `REVERIFICATION_T07_SCELLE`.

## 4. Ouvert

- VB6-6 (lignes B6-D3b et B6-D4 de la table des prédictions, « pour une sonde en A ») : non demandé à ce candidat, écrit au pas 5 de « Reste ».

## 5. Fichiers rendus (dossier `brouillons/accumulation-barreau6-v1/`, chacun avec compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `accumulation-barreau6-v1-candidat3.md` | `d48fb8a36c960e85416dfe42b2a9d77824067333b543a9f16540766e02ff1dfb` |
| `accumulation-barreau6-v1-candidat3-couples-v1.json` | `2057a5a99b78a6f6b1e68fcbec180e1e5507e4da4fa96c75c36843b38687bd7b` |
| `accumulation-barreau6-v1-candidat3-faire-v1.py` | `89d227c18985260018b5de45b89dc5a48f815b4e39d1464e8822ad750a40f764` |
| ce journal | compagnon écrit au scellement |
