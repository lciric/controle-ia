# Consigne — consigne de l'audit des fuites de T0.7, brouillon 2 — v1

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
Rédacteur neuf. Tu n'as écrit ni T0.7, ni ses contre-lectures, ni le module `src/controle_ia/t07/`, ni T0.6, ni P3-bis. Ayant lu T0.7, tu es exclu ensuite de tout rôle de lecteur de P3-bis et de tout rôle d'auditeur de l'audit que tu décris.

## Objet
Le brouillon 1 de la consigne de l'audit des fuites a été **interrompu** par la fin du quota (non scellé, non contre-lu, journal des questions perdu) : `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon1.md` (+ `INTERROMPU-LISEZ-MOI.txt`). Écris le **brouillon 2 complet**, en reprenant ce qui tient du brouillon 1 et en le vérifiant contre les sources ; le brouillon 1 n'est pas modifié.

## À lire
1. `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon1.md` (en entier).
2. `brouillons/T0.7-sondes-v0-v1-brouillon21.md` (`f7dcb226…`, vérifie l'empreinte) : lignes `AUDIT-FUITES-T07` et `CONSIGNE-AUDIT-FUITES-T07` (≈ l. 2086-2087), plan point 4 ter (entrée F), lignes L6 et L1b de la grille, et tout passage qui cite l'audit des fuites (cherche par `grep -n` dans ce seul fichier).
3. `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` (`2638558e…`), § 2e (chemin le plus fragile) et ce qu'il dit de l'audit.
4. Au besoin, la configuration et le texte scellés de T0.6 : `prereg/T0.6-organismes-v0-v1.md`, `prereg/T0.6-organismes-config-7b-v1.json` (construction des conditions seulement ; aucun résultat).
5. Registre : `registres/decisions.md` lignes R-2166, R-2171, R-2177 (par `grep -n '^| R-21\(66\|71\|77\) '`).

## À écrire (seuls chemins permis)
- `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon2.md` : consigne complète, opérationnelle pour un auditeur neuf (entrées, définition gelée recopiée à l'octet depuis T0.7, procédure par jeu `saboteur`, `S25`, `S50`, `S75`, `S100` contre `honnete`, sans aucun score de sonde, critère « séparation ≥ 0,70 » tel que gelé, format exact du fichier d'audit, gardes R5 avec cas sain et artefact, liste d'arrêt, marqueur `<<RAPPORT_CONTRE_LECTURE_CONSIGNE>>`). Là où T0.7 laisse un choix, écris la recommandation et dis-le (« réglage Qn »).
- `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon2-journal-v1.md` : sources lues avec empreintes, questions Q1… pour la mère avec recommandation, écarts au brouillon 1.
- Scelle les deux (compagnons `.sha256`). Aucun commit (la mère committe).

## Rapport final à la mère
Chemins, empreintes, verdict en une ligne (« prêt pour contre-lecture » ou non), questions ouvertes, et toute ligne de T0.7 qui te semble contradictoire.
