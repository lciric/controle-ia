# Consigne : préparer la chaîne v14 de T0.6 (lanceur et amorce qui lisent le GO de la configuration), sans l'adopter — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un **développeur neuf** (Opus), qui n'a écrit ni la chaîne de T0.6, ni T0.6, ni T0.7, ni P3-bis, ni leurs contre-lectures. Cadre : **option (c) de Lazar** (R-2079) : T0.6 est scellé sur la chaîne v13 (S `935262b1`, R-2082) ; la v14 est une **assurance**, préparée et éprouvée, **jamais adoptée sans décision** (bascule décidée le 13 novembre à 12:00 UTC si T0.7 n'est pas scellé ; elle demanderait une version neuve de T0.6, nœud de Lazar).

## Pourquoi

La chaîne v13 écrit `GO_ID=GO-2026-11-02-28` en dur en mode course (`scripts/lancer_t06_v13.sh` l. 83, contrôles l. 123 et l. 197 ; `scripts/amorce_instance_t06_v11.sh` l. 60 et l. 372 ; `src/controle_ia/t06/configuration.py` l. 14 ; `session.verifier_go` par défaut) et refuse ce GO après le 16 novembre. Lazar a prolongé le GO jusqu'au 23 par la ligne neuve **`GO-2026-11-10-01`** (200 USD non cumulés, R-2077). La v14 doit permettre une course de confirmation sous cette ligne, création au plus tard le 22, sans rien changer d'autre.

## Lieu

Arbre lié à créer par toi, partant de S, en extraction partielle (le dossier sous embargo et `docs/sources/` ne sont jamais extraits) :
```
git -C /home/user/controle-ia-travail worktree add --no-checkout -b prep/t06-chaine-v14-v1 /home/user/wt-t06-v14 935262b17ca95894a882b02f1526ee39d1738652
git -C /home/user/wt-t06-v14 sparse-checkout set --no-cone '/*' '!/docs/sources/' '!/docs/notes/bras-attaque/'
git -C /home/user/wt-t06-v14 checkout prep/t06-chaine-v14-v1
test ! -e /home/user/wt-t06-v14/docs/notes/bras-attaque && echo embargo-absent
```
Tu n'écris que là ; commits locaux sur `prep/t06-chaine-v14-v1`, un par jalon ; jamais `fetch`, `push`, ni action sur `main`, sur `/home/user/controle-ia-travail` (sauf son interpréteur `.venv/bin/python`) ni sur les autres arbres (`wt-t07`, `wt-t07-jouet`, `wt-t07-cl`, `wt-p3bis`, `wt-p3bis-lanceur`). `df -h /home/user` avant chaque passage d'essais ; sous 3 Go libres, arrête et rapporte.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier, sauf les commits locaux sur ta branche. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json`, ni celui d'un run jouet ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; **jamais `scripts/extraire_mesures_epreuve_t06_v1.py`**. Aucun `vastai` réel, aucune création d'instance, aucune dépense, aucun appel externe. Ne modifie ni `.claude/hooks/garde_calcul.py` ni `registres/go.md` (un registre temporaire pour les essais). Si la garde de calcul ou un classifieur refuse une commande : arrêt sur ce point, rapport tel quel. Garde des secrets à 0 avant chaque commit.

## Mandat

1. **Noms neufs (R12)** ; aucun fichier existant modifié : `scripts/lancer_t06_v14.sh` (copie de v13 : en mode course, la ligne de GO vient de la configuration (`go_id`), doit égaler `GO_ID` de l'environnement, est lue et vérifiée au registre par `session_v12.ligne_go_calcul` (type calcul, Lazar, non échue, non révoquée), et le plafond de la configuration ne dépasse pas celui de la ligne ; plus aucun identifiant en dur ; calendrier vérifié contre cette ligne) ; `scripts/amorce_instance_t06_v12.sh` (copie de v11 : même règle, GO reçu du lanceur et relu au registre du commit cloné ; fin du GO tirée de la configuration) ; module de session neuf si un module doit changer ; liste ciblée neuve `scripts/tests-cibles-t06-v4.txt` (v3 + tes essais) et liste des exclus si besoin ; essais neufs `tests/test_t06_v14_*.py` (cas sain et artefact pour chaque garde neuve : GO de la configuration ≠ `GO_ID`, ligne absente, échue, révoquée, plafond de la configuration > plafond de la ligne, ancienne valeur GO-28 en dur absente du code v14, calendrier au-delà de l'échéance de la ligne).
2. **Configuration de 7b, version 2, brouillon** (non adoptée) : `docs/notes/g0-deux-semaines-v1/t06-chaine-v14/config-t06-7b-v2-brouillon1.json`, copie de `prereg/T0.6-organismes-config-7b-v1.json` où changent seulement `go_id` → `GO-2026-11-10-01`, `calendrier.dernier_jour_creation` → `2026-11-22`, `calendrier.fin_go_utc` → `2026-11-24T00:00:00Z` ; empreinte canonique par `controle_ia.t06.lanceur.empreinte_config` ; scellée.
3. **Essais** : la liste ciblée v4 entière sur ton arbre (≈ 50 min ; `--basetemp` neuf sous ton arbre, effacé ensuite par son chemin) ; les trois échecs `pypandoc` connus sont attendus.
4. **Essai à blanc de la bascule**, hors ligne, sans rien pousser : texte factice (copie de `prereg/T0.6-organismes-v0-v1.md` dont seules les citations de code, d'amorce, de configuration et de calendrier changent, marquées FACTICE) dans un commit S″ de ta branche ; `controles` de v14 joué hors ligne (sans `fetch` ni jetons, comme l'essai à blanc de la voie B, `docs/notes/g0-deux-semaines-v1/integration-t06-v13-main-v1/rapport-essai-blanc-S-voie-b-v1.md`, § 3) pour les jours 16, 22 et 23 novembre avec le registre de `main` lu en lecture seule (`git -C /home/user/controle-ia-travail show main:registres/go.md` copié en temporaire) : conforme les 16 et 22, refus le 23 ; artefacts.
5. **Ce qu'une version neuve de T0.6 devrait changer** si Lazar bascule : liste des passages du texte scellé à changer (section, ligne, ancien, nouveau proposé), en couples JSON prêts à relire ; sans rien écrire dans `prereg/`.

## Sorties

Commits locaux sur `prep/t06-chaine-v14-v1` ; rapport `docs/notes/g0-deux-semaines-v1/t06-chaine-v14/rapport-preparation-chaine-v14-v1.md` dans ton arbre, scellé (fichiers et empreintes, différentiel v13 → v14 commenté, essais avec comptes, durées et heures `date -u`, essai à blanc, couples proposés, temps estimé d'une bascule complète). Réponse courte à la mère : commits, comptes d'essais, ce qui reste.
