# Consigne : essai à blanc de la construction du commit de scellement S de T0.6, voie B (R-2062) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-09, après 23:00 UTC (`date -u`). Destinataire : le développeur de l'intégration (R-2054, R-2058, R-2062), qui n'écrit pas T0.6.

## But

Établir, **sans rien pousser ni sceller pour de vrai**, que la voie B fonctionne : un commit S descendant de `1609a4bf`, qui ajoute le texte de T0.6 scellé et ses pièces citées, passe les contrôles du lanceur v13 (`scripts/lancer_t06_v13.sh`, sous-commande `controles`, l. 118-142) et la suite ciblée v3 de l'amorce v11 avec **2 022 passés** ; puis que sa fusion dans `main` laisse S trouvable par `commit_s` (l. 112) et ancêtre de `main`.

## Lieu

Clone temporaire **sous `/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/essai-S/`** (fait par `git clone --no-hardlinks /home/user/controle-ia-travail …` ou depuis `/home/user/integ-t06`, puis distant d'origine retiré). Rien écrit dans `/home/user/controle-ia-travail` ni dans `/home/user/integ-t06`. Aucun `fetch` réseau, aucun `push`. Interpréteur : `/home/user/controle-ia-travail/.venv/bin/python`.

## Interdits

Ceux de `interdits-communs-v1.md` (même dossier), en entier : fichiers et branches sous embargo jamais ouverts (`diag/*/lecture-sondes-t06.json`, nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; `diag/` et `runs/` de 7a et `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; étiqueteur) ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; refus de contrôle ou de classifieur : arrêt et rapport tel quel.

## Travail

1. Dans le clone, branche locale `essai/S-voie-b` partie de `1609a4bf`.
2. **Texte factice** : la r3 (`brouillons/T0.6-organismes-v0-v1-candidat12-r3.md`, `c24e268e…`, lue dans `main`) avec les couples Y1 à Y12 de la contre-lecture 3 appliqués (`prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3-couples-v1.json` ; texte attendu `7d7bfd27…`), puis les dix marqueurs remplis de valeurs **plausibles et marquées factices dans ton rapport** : `COMMIT_CODE_T06` = `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` ; `EMPREINTES_CODE_T06` et `EMPREINTE_AMORCE_T06` = les empreintes réelles au commit `1609a4bf` ; `CHEMIN_CONFIG_T06` = une copie de `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json` (`b7a5c1ba…`) sous `prereg/` (nom à proposer), scellée, et `EMPREINTE_CONFIG_T06` son empreinte ; les autres marqueurs : valeurs factices évidentes. Écrire le texte sous `prereg/T0.6-organismes-v0-v1.md`, le sceller (`controle_ia.scellement sceller`), vérifier `controle_ia.prereg` (aucun problème), committer S′ dans le clone avec les pièces citées absentes de `1609a4bf` (relever lesquelles : config, tâches, consignes de P3, sceaux).
3. **Contrôles du lanceur, hors ligne** : rejouer à la main les lignes 125 à 141 de `controles` contre S′ (sans `fetch`, sans jetons ; le contrôle « ancêtre d'`origin/main` » simulé par une fusion locale de S′ dans une copie de `main`, puis `merge-base --is-ancestor`) : `commit_s` rend-il S′ après la fusion ? les huit citations sont-elles chacune sur une ligne ? fichiers cités et sceaux présents et conformes dans S′ ? calendrier (sous-commande `calendrier` de la session v12) conforme pour un jour du 10 au 14 novembre ? empreinte de l'amorce v11 citée par le texte sous la forme exigée (l. 140) ? `controles` avec `GO_ID` de la course : la ligne GO-2026-11-02-28 lue dans le `registres/go.md` de `main`.
4. **Suite ciblée v3 sur l'arbre de S′**, exactement comme l'amorce v11 (l. 488) : relever passés / échoués / sautés ; attendu 2 022 (hors `test_corpus_arxiv` si `pypandoc` manque : le dire). Si un essai lit `prereg/T0.6-organismes-v0-v1.md` ou les registres et change de résultat parce que le texte existe, le signaler.
5. **Fusion de S′ dans une copie locale de `main`** (tête `d82f89f5` ou plus loin) : conflits et résolutions (mêmes règles que l'intégration et R-2055) ; `git log --diff-filter=A -1 --format=%H -- prereg/T0.6-organismes-v0-v1.md.sha256` depuis la tête fusionnée rend S′ ; `exiger_code_cite` avec commit cité `1609a4bf` et HEAD = S′ : passe.
6. Rien n'est poussé ; le clone reste dans le dossier de travail de la mère.

## Sorties

Rapport `…/scratchpad/essai-S/rapport-essai-blanc-S-voie-b-v1.md` (hors dépôt ; la mère le versera) : chaque contrôle, son résultat, les commandes exactes ; liste des pièces que la r4 et S doivent contenir ; forme exacte des huit lignes citées ; compte des essais ; ce qui ne peut pas être joué hors ligne. Réponse courte à la mère : verdict (voie B jouable ou non), compte des essais, liste des pièces de S, points bloquants.
