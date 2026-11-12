# Consigne : corriger le code de P3-bis d'après sa contre-lecture (CP-01 à CP-17) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 vers 05:25 UTC (`date -u`). Destinataire : un **développeur neuf** (Opus), qui n'a écrit ni le code de P3-bis v1, ni ses brouillons, ni ses contre-lectures, ni T0.6, ni T0.7, ni le lanceur de P3-bis (un autre développeur l'écrit en parallèle).

## Lieu

Arbre à créer par toi : `git -C /home/user/controle-ia-travail worktree add -b prep/p3bis-code-v2 /home/user/wt-p3bis main`. Tu n'écris que là ; commits locaux sur `prep/p3bis-code-v2` seulement, **un commit par jalon** (le conteneur a redémarré deux fois cette nuit) ; jamais `fetch`, `push`, ni action sur `main`, sur `/home/user/controle-ia-travail` (sauf son interpréteur `.venv/bin/python`), `/home/user/wt-t07`, `/home/user/integ-t06` ni `/home/user/wt-p3bis-lanceur`. Regarde `df -h /home/user` avant chaque passage d'essais ; sous 3 Go libres, arrête et rapporte.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier, sauf les commits locaux sur ta branche. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. **T0.7** : un seul fichier de T0.7 t'est permis, `src/controle_ia/t07/registre_v1.py` de `main`, et seulement pour recopier la chaîne de motifs de CP-15 (commit et empreinte écrits) ; aucun autre fichier de T0.7, aucun brouillon de T0.7. Aucun appel externe, aucun `vastai`, aucune dépense. Aucun nettoyage hors de tes propres dossiers temporaires, effacés par leur chemin exact. Refus d'un contrôle ou d'un classifieur : arrêt sur ce point, rapport tel quel. Garde des secrets à 0 avant chaque commit (`git diff --cached | grep -c -E 'sk-ant-api03-[A-Za-z0-9_-]{40,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE[ ]KEY|sk[-]proj-|AIza[0-9A-Za-z_-]{35}|sk[-][A-Za-z0-9]{40,}'`).

## À lire

- Contre-lecture du code : `brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md` (`7a074ad1…`) — **ta liste de travail** (table CP-01 à CP-17, points 1 à 6).
- Texte qui fait foi : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md` (`eb65773f…`) ; décision `docs/decisions/decision-N-066-v1.md` (`21e83ed5…`).
- Code v1 et compte rendu du développeur v1 (`977d84c1…`).
- Noms : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/noms-communs-p3bis-v2.md` (fait foi pour les noms et l'interface).

## Mandat

1. **Bloquants** : CP-01 (trois décisions, modes `pleine`, `reduite`, `pleine-anticipee`, refus nommés, une seule « ouvrir pleinement » après une ouverture réduite lue au journal), CP-02 (journal au format exact du texte, l. 668 à 695 ; relu à chaque tentative ; `deja-ouverte` ; codes de motif de la liste fermée ; essais du texte), CP-03 (au moins quatre passages par issue, règle des 16 octets sur les plages, contrôle positif « 4 096 zéros de bourre »).
2. **À corriger** : CP-04 à CP-10. Pour CP-10, inscrire `run_v2.py::executer` (son appel à `charger_invite`) au dictionnaire `REGISTRE` de `tests/test_cibles_invisibles_v1.py`, avec sa raison, **sans toucher aucune fonction d'essai** ; c'est le mécanisme voulu par cet essai ; le déclarer au rapport.
3. **Mineurs** : CP-11, CP-12, CP-14 à CP-17 si chacun reste court ; CP-13 est côté texte : le lister seulement.
4. Le **journal** écrit par la v2 doit être lu tel quel par T0.7 ; ne lis pas le lecteur de T0.7 : suis la lettre du texte, la mère fera l'essai de concordance entre les deux.
5. Chaque garde neuve ou corrigée : un cas sain et un artefact (R5) ; graines par `SeedSequence` dérivées (R9) ; aucun essai existant modifié pour passer (sauf l'inscription de CP-10, qui n'est pas une fonction d'essai).
6. **Essais** : liste ciblée v2 (v1 plus tes fichiers neufs) avec `--basetemp` neuf sous ton arbre ; l'essai de fermeture v2 une fois à la fin (sortie écrite sous `brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v1.txt`, scellée) ; pas la suite complète.
7. Ne pas écrire dans le brouillon 9 ni dans la configuration.

## Sorties

Commits locaux sur `prep/p3bis-code-v2` ; compte rendu `brouillons/P3-bis-temoin-positif-v1/compte-rendu-developpeur-code-p3bis-v2.md` dans ton arbre, scellé : défaut par défaut (fait, fichier, ligne, essai), écarts déclarés, ce qui va au texte (écarts 3, 4, 5, 7, 9, 10 du développeur v1, CP-13, taille réelle du second paquet), valeurs proposées pour `COMMIT_CODE_P3BIS`, `EMPREINTES_CODE_P3BIS` (avec l'essai de fermeture), `IDENTITE_CODE_P3BIS`, `TESTS_ATTENDUS_P3BIS` (provisoire), `ESSAI_FERMETURE_P3BIS`. Réponse courte à la mère : commits, comptes d'essais, défauts réglés ou non, écarts.
