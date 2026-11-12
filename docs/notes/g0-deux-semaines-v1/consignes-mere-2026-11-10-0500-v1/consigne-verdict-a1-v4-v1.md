# Consigne : lecture, audit de symétrie et verdict de la course A1-v4 (attaque de Goodhart contre le nul v9) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **lecteur neuf, modèle Fable** (règle R13 : ni auteur du préenregistrement, de son code, de ses contre-lectures, ni exécutant de la course ; il n'a écrit aucune pièce d'A1). Il applique les **critères gelés** du texte scellé et rien d'autre.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. **Aucun appel d'Argon ni d'aucun modèle** (la lecture et l'audit sont des calculs locaux : le juge v9 est statistique) ; aucune dépense, aucun `vastai`, aucune écriture git, aucune poussée ; rien n'est fusionné dans `main`. Ne jamais lire une valeur de clé.

## Pièces

- **Texte scellé** : `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md`, sha256 `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6` (à vérifier) ; sections 4 (plan), 5, **6 (critères gelés, ordres 2, 6, 1, 3, 4, 5 et 2′, 6′, 1′, 3′, 4′, 5′, suspensions)**, **7 (audit A1 à A9 et vérifications des mondes)**, 11 (code gelé, empreintes).
- **Code gelé** : dépôt public au commit `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0` (texte et compagnon par-dessus le code `b8c1db3add7cdda7fee876944c1e8f692a568e98`), dans le paquet `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/commit-public-code-v5-a1-v4-v2.bundle` (`ac46f313…`, à vérifier) : `git clone` du paquet dans un dossier neuf à toi, `git checkout f39a7f4a…`, empreintes des fichiers gelés comparées au bloc du § 11 avant tout usage.
- **Sortie de la course** : branche `donnees/attaque-goodhart-v4-a1v4-v1` du dépôt privé, tête `773319b7…` (déjà récupérée en `refs/remotes/origin/donnees/attaque-goodhart-v4-a1v4-v1` dans `/home/user/controle-ia-travail`) ; extraction par `git archive` dans un dossier neuf à toi, **intégrité d'abord** (`sha256sum -c EMPREINTES-sortie-a1-v4-v1.txt`), comme le § 7 point 3 de l'ordre `docs/procedures/ordre-course-a1-v4-v9-v1.md`.
- **Écart de la course** : utilisation d'Argon par un tiers pendant la fenêtre (R-2013, R-2014 ; décision (a) de Lazar, R-2043 : course gardée, l'audit lit les erreurs et ralentissements pendant la fenêtre et écrit une réserve s'il y a eu perturbation) ; journaux de la sortie (`relais-argon-journal-a1-v4.jsonl`, `garde-a1-v4.jsonl`, `journal-hote-a1-v4-v1.log`).
- Registre `registres/decisions.md` R-1959 à R-1990, R-2013, R-2014, R-2043, R-2090.

## Mandat

1. **Intégrité** du versement (comptes, empreintes ; tout écart : arrêt et rapport).
2. **Lecture** par les fonctions gelées que le texte nomme (`lire_monde` pour W2, `lire_monde_w2g` pour W2g, code v5), sur la sortie, sans rien changer au code ; sortie brute de la lecture écrite et scellée.
3. **Audit de symétrie** A1 à A9 (§ 7), y compris la vérification du monde W2 au nul v9 et de W2g hors du nul sur les 24 cartes (comptes sur 200, rapportés carte par carte), et **A9 / écart d'Argon** (erreurs, ralentissements, réessais dans la fenêtre de l'usage tiers : réserve écrite s'il y a perturbation).
4. **Verdict** : issue de W2 et issue de W2g selon les ordres gelés, avec les suspensions du § 6 (« tout audit autre que A4 et A8 suspend l'issue jusqu'à l'audit écrit ; A9 sur un monde suspend les deux ; une issue 3 est toujours suspendue par A1 jusqu'à l'audit écrit ») ; qualification exacte (chaînes du code) ; réserves (dont « λ\* à la limite », § 6.2) ; **aucune lecture au-delà des critères** (R8 : aucune revendication neuve).

## Sorties (dossier neuf `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/` dans `/home/user/controle-ia-travail`, rien d'autre écrit)

- `integrite-versement-a1-v4-v1.txt`, `lecture-a1-v4-v1.json` (sortie brute des fonctions gelées), `audit-symetrie-a1-v4-v1.md`, `verdict-a1-v4-v1.md` (en tête : issues de W2 et W2g en une ligne chacune ; puis audit, réserves, ce que le verdict ne dit pas), tous scellés (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`).
- Dossiers temporaires (clone du paquet, extraction de la sortie) sous `/home/user/verdict-a1-v4-tmp/`, effacés à la fin par leur chemin exact.

Réponse courte à la mère : chemins, empreintes, issues de W2 et W2g, suspensions et réserves, refus éventuels.
