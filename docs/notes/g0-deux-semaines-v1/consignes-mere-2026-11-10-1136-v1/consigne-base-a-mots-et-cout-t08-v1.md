# Consigne — texte court préenregistré de la base (A) « mots et coût » (T0.8), brouillon 1 — v1

- **Session mère** : nouvelle instance (reprise du 2026-11-10, brief `registres/passations/brief-successeur-mere-2026-11-10-v1.md`, passation `registres/passations/2026-11-10-1113.md` `64d321cf…`). Tu es un sous-agent **neuf**. Dépôt : `/home/user/controle-ia-travail` (branche `main`), `PYTHONPATH=src`, interpréteur `/home/user/controle-ia-travail/.venv/bin/python`. Sceller un fichier : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN` (compagnon `.sha256`).
- Français, presque aucun sigle. Toute heure écrite est relevée par `date -u` dans la même commande. Bac à sable temporaire : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/` (crée-le), `TMPDIR` et `--basetemp` dedans.
- **Interdits communs, recopiés mot pour mot ci-dessous (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)** — ils priment sur toute autre phrase de cette consigne, sauf les exceptions écrites expressément à la section « Exceptions ».

# Interdits communs aux sous-agents de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (10 novembre 2026, v2)

Écrit le 2026-11-09 vers 22:00 UTC (heure relevée par `date -u`). Recopié mot pour mot dans chaque consigne de cette série.

**v2** (R-2086) : v1 recopiée à l'identique (`851028fc…`), plus la règle 9 ; écrite après deux accès mécaniques par recherche récursive (R-2064, R-2086).


1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) :
   - `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` (DT-4 : rien avant le verdict scellé de P3-bis) ;
   - la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` (R-2041, R-2048) ;
   - tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3`, sauf permission écrite dans la consigne ;
   - `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` (le bras d'attaque n'est pas le mandat de la mère : N-056, R-2045, R-2047) ;
   - les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
2. **Secrets** : ne jamais lire, afficher ni copier une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`, même avec la sortie jetée.
3. **Aucun appel** de modèle ni d'interface externe (Argon, Claude, autres), aucune location d'instance, aucun `vastai`, aucune dépense.
4. **Git** : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; les autres commits se lisent par `git show <commit>:<chemin>` seulement (ils sont déjà dans le clone local). Rien n'est écrit hors des chemins de sortie nommés dans la consigne.
5. **Essais** : ne pas lancer la suite complète (la session mère la fait tourner) ; des essais ciblés sont permis.
6. **Refus** : si un contrôle de permissions ou un classifieur refuse une action ou une réponse, s'arrêter sur ce point et le rapporter tel quel ; ni contournement, ni reformulation, ni transfert.
7. **Heures** : toute heure écrite est relevée par `date -u` et dite telle.
8. **Rapport final à la mère** : chemins écrits, empreintes sha256, verdict en une ligne, points ouverts ; **aucune valeur numérique tirée d'une sonde de 7a** (il ne doit d'ailleurs y en avoir aucune sous vos yeux).
9. **Recherches et parcours** : aucune recherche récursive (`grep -r`, `rg`, `find … -exec`, motif `**` ou `*/` développé par l'interpréteur) sur un dossier qui contient un chemin interdit sans l'exclure explicitement ; en pratique, chercher avec `git grep` et des exclusions de chemins (`git grep -n MOTIF -- . ':(exclude)docs/notes/bras-attaque' ':(exclude)scripts/extraire_mesures_epreuve_t06_v1.py' ':(exclude)diag' ':(exclude)runs'`) ou dans une liste de fichiers nommés ; `verifier-arbre` et tout outil qui hache un arbre entier ne se lancent que sur un arbre où `docs/notes/bras-attaque/` n'est pas extrait.


## Rôle
Rédacteur neuf. Tu n'as écrit ni T0.8, ni T0.6, ni T0.7, ni P3-bis, ni leurs contre-lectures. Tu ne lis pas T0.7 (pour rester éligible ailleurs).

## Objet
Décision de Lazar D-2 (a) (R-2175) : la base (A) « mots et coût » de T0.8 est **scellée à part, avant la création de la course de confirmation 7b** (DB8-1 (a)), au **coût brut** ; c'est elle qui rend le barreau 3 lisible vers le 18. N-063 (v2) : le critère 3 de G0 (sondes) n'est jugé qu'aux doses où la base « mots et coût » de T0.6 échoue selon son propre critère, « sans objet » si aucune. Rien n'a été écrit avant l'arrêt du quota : écris le **brouillon 1** d'un préenregistrement court, complet au sens de R1 (hypothèse, prédiction chiffrée avec signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt), sur le gabarit `prereg/gabarit-preregistrement-v1.md`.

## À lire
1. `docs/decisions/decision-N-063-v2.md` ; R-2175, R-2171, R-2186 dans `registres/decisions.md` (par `grep -n`).
2. `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon1.md` (`ca26763a…`) : la base (A) et ce qui la touche ; sa contre-lecture `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon1-cl1.md` (`21499f7c…`) : les couples qui concernent la base (A).
3. `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` (`2638558e…`), barreau 3 et décisions D-1 à D-4.
4. `prereg/T0.6-organismes-v0-v1.md` et `prereg/T0.6-organismes-config-7b-v1.json` : doses, conditions, traits du texte, coût (construction seulement ; aucun résultat ; rien sous `diag/`, `runs/`, `donnees/`).

## À écrire
- `brouillons/T0.8-base-A-mots-et-cout-v1/T0.8-base-A-mots-et-cout-v1-brouillon1.md` et `…-brouillon1-journal-v1.md` (sources et empreintes, choix faits et pourquoi, questions pour la mère avec recommandation, tout point qui toucherait H1, G1 ou le mode tenu à l'écart signalé comme **nœud**). Marqueurs `<<…>>` permis pour ce qui ne peut être fixé qu'au scellement (entropie, commit). Aucun chiffre sans chemin et empreinte (R6).
- Scelle les deux. Aucun commit.

## Rapport final à la mère
Chemins, empreintes, verdict en une ligne, questions et nœuds.
