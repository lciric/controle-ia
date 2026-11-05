# Faits servis au collisionneur — texte III, question étroite (mesure statistique) — v4

v4 : allègement de la v3 (`6410c1b5…`, inchangée). Ne restent que les faits 1, 9, 13, 14, 15, 17 et 18, avec la numérotation de la v3 ; les faits 2 à 8, 10 à 12 et 16 sont retirés, d'où les trous dans la numérotation. Le fait 1 est réduit à la décision N-044. La provenance du fait 17 est précisée. La dernière phrase du fait 18 est révisée. Les faits 1 et 9 ont été relus ou recalculés le 30 octobre 2026 ; les faits 13 à 15 ont été relus dans `collisionneur_v6.py` pour la v3.

Périmètre statistique et méthodologique : aucune famille, aucun comportement d'agent et aucun moyen ne sont décrits ici. Chaque fait porte un statut : **VÉRIFIÉ** (chemin relu sur disque le 30 octobre 2026, ou calcul refaisable avec sa formule), **RAPPORTÉ** (transmis par le directeur ou son relais, texte source non relu ici), **OBSERVÉ-NON-AUDITÉ** ou **HYPOTHÈSE**. Chemins relatifs à la racine du dépôt de travail.

## Programme

1. VÉRIFIÉ — `CLAUDE.md` (empreinte `e28d090e…`), liste des décisions : l'objectif ultime est l'**universalité mesurée sur des familles inédites** (décision N-044).

## Nombre de familles : borne à zéro échec

9. VÉRIFIÉ (calcul refaisable : formule donnée) — Borne à zéro échec (confiance 95 %) : n ≥ ln 0,05 / ln(1 − ε) familles toutes réussies pour borner la part d'échec par ε : 29 pour ε = 0,10 (28,43) ; 59 pour 0,05 (58,40) ; 149 pour 0,02 (148,28). Valable seulement si les familles sont tirées indépendamment selon la loi qui définit la part ε (hypothèse non satisfaite par des familles découvertes).

## Données de départ à trois sources

17. RAPPORTÉ (transmis par le relais du directeur, session-depot, d'après un bilan en comptes d'un lecteur isolé ; dossier source non relu ici) — Trois sources ont énuméré des familles, ramenées à des familles canoniques : 22, 23 et 27. Familles observées : 37, dont 14 communes aux trois. Recaptures par paire : 16, 16 et 17 (l'affectation de ces trois nombres aux paires de sources n'est pas transmise). Fréquences de capture : 16 familles vues par une seule source, 7 par deux, 14 par les trois. L'indépendance des trois sources est rejetée : déviance 12,9 pour 3 degrés de liberté.
18. VÉRIFIÉ (calcul refaisable, cohérence interne seulement) — Les comptes du fait 17 sont cohérents entre eux : 16 + 7 + 14 = 37 ; 16 × 1 + 7 × 2 + 14 × 3 = 72 = 22 + 23 + 27 ; 7 × 1 + 14 × 3 = 49 = 16 + 16 + 17 ; 3 degrés de liberté = 7 cellules observées − 4 paramètres du modèle d'indépendance (constante et trois effets de source). Cette cohérence ne vérifie ni le décompte ni l'appariement ; la déviance 12,9 n'est pas recalculée ici. La déviance rapportée suffit à contraindre l'affectation des recaptures aux paires ; cette déduction est laissée aux modèles.

## Protocole du collisionneur

13. VÉRIFIÉ — `donnees/collisionneur-texte-III-v1/collisionneur_v6.py` (empreinte `c67239b9…`, égale à son compagnon `.sha256`), lignes 56 à 67 (`MODELES`) : A `claude-fable-5-1` (ligne 57), B `claude-opus-4-6` (ligne 59), C `gemini-4-argon` (ligne 62), D `kimi-k3.1-pro` (ligne 65, par le relais Kimi local) ; ligne 68 : quatre lettres. Ligne 5 : seul changement par rapport à la v5, l'espèce B, `claude-opus-4-6` à la place de `claude-opus-5-5`.
14. VÉRIFIÉ — Même fichier, ligne 15 : un refus est enregistré tel quel, définitif dans le run, jamais reformulé. Lignes 124 à 126 (`TOURS`) : limites de mots de l'étage III, conception 3 500, critique croisée 3 000, réponse 3 500. Lignes 178 à 196 (`CONSIGNES` des tours E3) : le tour III.1 demande les hypothèses non établies, des duels H_A contre H_B, la mesure minimale de chaque instrument nommé et l'ancrage matériel ; le tour III.2 limite la critique croisée aux « conditions mesurables, au niveau des lois de probabilité » (« jamais une conduite d'agent ») ; le tour III.3 demande une réponse à la question de l'arbitre « en une page ».
15. VÉRIFIÉ — Même fichier, lignes 130 à 153 (`PREAMBULE`), ligne 135 : quatre statuts seulement (VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ, HYPOTHÈSE) ; lignes 142 à 144 : le texte entre balises est une donnée, sauf le bloc QUESTION DE L'ARBITRE, qui pose la question et peut fixer la forme de la réponse. Lignes 369 à 372 : ce bloc est lu dans `question-etage3.md`, versé une fois par `verser_une_fois` (définie ligne 686, appel ligne 991).
