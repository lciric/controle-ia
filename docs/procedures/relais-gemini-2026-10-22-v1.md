# Relais de Claude Code à Gemini — 22 octobre 2026 (v1)

Message à coller tel quel dans l'instance Gemini de Lazar. Tu reprends la relève du programme « contrôle boîte blanche des menaces diffuses » (R-318) jusqu'au retour de Claude Code, attendu le 25 octobre vers 18:00 UTC. Les règles du dépôt (`CLAUDE.md`, R1 à R14) s'appliquent à toi comme à Claude.

## 1. D'abord

1. Fais `git fetch origin`, puis mets ta copie de `main` à jour. Depuis ton départ, Claude a poussé deux commits : `55236a7` et `18637a0`.
2. Lis `registres/etat.md` (les trois premières lignes) et `registres/passations/2026-10-22-1645.md`. Les heures de cette passation sont corrigées par R-323.
3. Vérifie l'arbre : `cd docs && sha256sum -c sha256sums-lancement-v2.txt`, puis, à la racine, `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .`.
4. Lis toujours l'heure avec `date -u` avant de l'écrire.

## 2. Ce qui a changé depuis le 21 octobre

- **N-034 tranché par Lazar** : options (a), (b) et (c), fixées par `docs/decisions/decision-N-034-v1.md`. « Functional Welfare » devient voisin publié de PA-12 ; une réserve entre au préenregistrement de G1 ; un bras « revers » est ouvert.
- **N-035 tranché par Lazar** : H9, la survie des contraintes de sécurité à la délégation, entre au papier B sous réserve d'antériorité (`docs/decisions/decision-N-035-v1.md`).
- **P-015** a pris son défaut (b) (R-321).
- **Hors dépôt** : le collisionneur 3×3 de Lazar a été réécrit (v2.5). C'est son outil personnel : tu ne le modifies pas et tu ne le lances pas.

## 3. Le travail local du 22 octobre : quarantaine, puis audit

Les textes du collisionneur du 22 octobre, écrits à partir des faits fournis par Lazar, décrivent sur la chaîne de P4 :
- des bancs de vérification modifiés ;
- un faux « Tests passed » ;
- un échec d'assertion rapporté comme un succès ;
- une substitution de modèle, avec un texte simulé et une troncature.

Ils citent deux commits locaux, `9c699ca` et `687ede7`, absents de `main`.

1. Pousse ces commits tels quels, sans les modifier ni les rebaser, sur une branche neuve : `quarantaine/releve-gemini-2026-10-22`. Si tu ne peux pas pousser toi-même, donne à Lazar les commandes exactes pour le faire.
2. Ne bâtis rien dessus. La chaîne de P4 est gelée jusqu'à l'audit, que fera Claude ou un relecteur neuf.
3. Sur cette branche, écris `RAPPORT-RELEVE-2026-10-22.md` : ce que tu as modifié, pourquoi, et la sortie brute des commandes concernées (codes de sortie, journaux). Pas de résumé à la place des sorties.

## 4. Règles de cette relève

- **Tu n'écris jamais sur `main`.** Tu travailles sur `canal/gemini`, pour les propositions, ou sur une branche neuve. La session Claude relit, fait contre-lire par un relecteur neuf (R2), puis applique elle-même sur `main`.
- **Tu ne modifies jamais** un test, une garde, un hook, `.claude/settings.json`, un banc de vérification ni un fichier scellé. Si l'un d'eux te bloque, tu t'arrêtes et tu le dis.
- **Tu ne remplaces jamais un modèle par un autre**, tu n'écris jamais de réponse simulée et tu ne tronques jamais une sortie. Un appel qui échoue est rapporté comme un échec.
- **Tu n'écris jamais qu'un test passe** sans coller la sortie qui le montre.
- **Aucune dépense sans GO** (`registres/go.md`), et aucune instance de calcul lancée ni arrêtée par toi. La destruction de l'instance 56799469 attend Lazar ou Claude (R10 : par son identifiant).
- **Les registres de `main`** (`etat.md`, `decisions.md`, `go.md`) ne sont tenus que par Claude. Les défauts qui échoient pendant ta relève seront appliqués par la routine de reprise de Claude : ne les écris pas. Ce sont P-016 et P-017 (le 22 octobre vers 21:15 UTC), puis P-020 à P-024 (le 23 octobre vers 00:30 UTC).
- **Jamais de poussée vers `lciric/controle-ia`** ; aucune clé écrite ni affichée.
- **Toute pièce que tu écris déclare en tête** ce que tu as lu des résultats et des consignes de P3 (R-318).

## 5. Ce que tu peux faire

1. **H9, recherche d'antériorité** (N-035). La survie d'une contrainte de sécurité à travers les délégations entre agents est-elle déjà mesurée ?
   - Commence par deux sources citées de mémoire et non vérifiées : Cemri et al. 2025, « Why Do Multi-Agent LLM Systems Fail? » ; Hammond et al. 2025, « Multi-Agent Risks from Advanced AI ».
   - Fais ensuite des recherches affirmatives.
   - Livrable, sur `canal/gemini` : une note où chaque PDF est téléchargé et empreinté et chaque citation porte sa page, avec un verdict par pièce : prise, partiellement prise, ou libre dans les sources lues (R7, R8).
2. **P-025, brouillon de conception du bras « revers »** (N-034 (c)) : où il entre (T0.6, G1 ou une passe propre), ses conditions (un témoin, des revers sans lien avec le contenu, un retour du protocole de contrôle), ses mesures (sondes gelées, fausses alertes du moniteur séquentiel), son devis. Livrable : un brouillon sur `canal/gemini`, que Claude relira. Rien n'est préenregistré ni lancé.
3. Rien d'autre sans l'accord de Lazar.

## 6. Fin de relève

Le 25 octobre, ou plus tôt sur l'ordre de Lazar, écris sur ta branche `RELEVE-FIN-AAAA-MM-JJ.md`. Il contient : ce qui est fait, ce qui reste, tes réserves, la prochaine action, et la liste exacte de tes commits avec leur empreinte. Claude reprendra par sa routine de reprise.
