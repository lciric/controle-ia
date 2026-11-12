# Consigne : écrire le lanceur de P3-bis et sa chaîne — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 vers 05:25 UTC (`date -u`). Destinataire : un **développeur neuf** (Opus), qui n'a écrit ni le code de P3-bis, ni ses brouillons, ni ses contre-lectures, ni T0.6, ni T0.7 ; un autre développeur corrige le code de P3-bis en parallèle.

## Lieu

Arbre à créer par toi : `git -C /home/user/controle-ia-travail worktree add -b prep/p3bis-lanceur-v1 /home/user/wt-p3bis-lanceur main`. Tu n'écris que là ; commits locaux sur `prep/p3bis-lanceur-v1` seulement, **un commit par jalon** ; jamais `fetch`, `push`, ni action sur `main`, sur `/home/user/controle-ia-travail` (sauf son interpréteur `.venv/bin/python`), `/home/user/wt-t07`, `/home/user/integ-t06` ni `/home/user/wt-p3bis`. Regarde `df -h /home/user` avant chaque passage d'essais ; sous 3 Go libres, arrête et rapporte.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier, sauf les commits locaux sur ta branche. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py` ; **aucun fichier de T0.7**. **Aucun `vastai` réel, aucune création d'instance, aucune dépense, aucun appel externe** : les essais simulent `vastai` par un faux exécutable dans un dossier temporaire, comme ceux de la chaîne de P3. Ne touche jamais aux instances 58936096, 58936099, 58936100 : elles ne figurent que comme constante `ARRETEES_TOLEREES`. Aucun nettoyage hors de tes propres dossiers temporaires, effacés par leur chemin exact. Refus d'un contrôle ou d'un classifieur : arrêt sur ce point, rapport tel quel. Garde des secrets à 0 avant chaque commit (`git diff --cached | grep -c -E 'sk-ant-api03-[A-Za-z0-9_-]{40,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE[ ]KEY|sk[-]proj-|AIza[0-9A-Za-z_-]{35}|sk[-][A-Za-z0-9]{40,}'`).

## À lire

- Texte qui fait foi : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md` (`eb65773f…`), surtout la liste d'arrêt, le devis, la chaîne (`<<CHAINE_P3BIS>>`), l'offre et la récupération.
- Contre-lecture du code, **point 6** (liste des contrôles du lanceur) : `brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md` (`7a074ad1…`).
- Modèle : la chaîne de P3, `docs/procedures/P3-premier-test-v1/` (lanceur, vérifications, contrôles avant dépense, surveillance, récupération, scellement, essais, répétitions jouet et finale) ; garde de calcul `.claude/hooks/garde_calcul.py` (lecture seule ; ne pas la modifier) ; registre `registres/go.md`, ligne `GO-2026-11-02-29` (80 USD, échéance 16 novembre 2026).
- Scripts de l'instance v1 (`scripts/p3bis_instance.sh`, `scripts/amorce_instance_p3bis.sh`) et noms : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/noms-communs-p3bis-v2.md` (fait foi pour les noms et l'interface après correction ; écris contre les noms v2, en constantes en tête de fichier).

## Mandat

1. Écrire la chaîne sous `docs/procedures/P3-bis-temoin-positif-v1/` (noms de la table commune) : tous les contrôles du point 6 de la contre-lecture (GO cité égal à `GO-2026-11-02-29`, aucune révocation, date au plus tard le 16 novembre 2026 en constante ; texte scellé sans marqueur, commit cité égal à l'arbre gelé du commit de scellement ; essai de fermeture conforme au commit du code, sinon aucune création ; longueurs ; compte N des essais ; offre dans les bornes du texte et repli écrit ; crédit ; instances du compte ; `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` ; branche de calcul absente du dépôt distant ; surveillance sans arrêt à durée, alerte à deux heures sans `PROGRES`, arrêts **par identifiant d'instance** (R10), arrêt à 80 USD, code 5 du second paquet = instance gardée ; récupération par clone de la branche de calcul, jamais `main`, `lectures-fermees --prereg --entropie`, commit du seul paquet et de son compagnon).
2. Chaque contrôle : un cas sain et un artefact (R5), dans des essais shell ou Python sous la chaîne et/ou `tests/` (fichiers neufs) ; aucun essai existant modifié.
3. Répétition jouet de la chaîne (faux `vastai`, faux GO dans un registre temporaire, jamais le vrai `registres/go.md` modifié) ; la répétition finale en mode décisif reste écrite mais ne se joue qu'au candidat.
4. Écrire ce que la mère mettra au marqueur `<<CHAINE_P3BIS>>` (fichiers, empreintes) et la liste des écarts au texte.

## Sorties

Commits locaux sur `prep/p3bis-lanceur-v1` ; rapport `docs/procedures/P3-bis-temoin-positif-v1/rapport-developpeur-lanceur-p3bis-v1.md` dans ton arbre, scellé : fichiers et empreintes, contrôles (texte → code → essai), essais (comptes, durées, heures `date -u`), écarts, dépendances envers le code corrigé. Réponse courte à la mère : commits, comptes d'essais, ce qui reste.
