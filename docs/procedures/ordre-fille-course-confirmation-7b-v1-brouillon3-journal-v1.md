# Journal du rédacteur — ordre de la course de confirmation 7b de T0.6, brouillon 3 — v1

- **Qui** : le rédacteur des brouillons 1 et 2 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), sur la correction de la mère après R-2112.
- **Quand** (`date -u`, 10 novembre 2026) : 09:04:53 (lecture de R-2112, début) ; 09:06:25 (contrôles faits, avant ce journal) ; heure de scellement : compte rendu à la mère.
- **Dépôt** : `main` à `469487af` (R-2112). Écritures : le brouillon 3 (copie du brouillon 2, puis corrections) et ce journal, plus leurs compagnons ; le brouillon 2 (`488c2e516347a44d341d8ab3aaf6361b35aa60d348565d0d3aa4385b78fbcb4d`) reste tel quel (R12). Interdits communs v2 (`1ee3b370…`) tenus, règle 9 comprise : aucune recherche récursive dans cette reprise.
- **Source neuve** : `registres/decisions.md`, R-2112 (point bloquant PB-1 : l'étape A ne peut pas tourner sur l'instance de 7b redémarrée, qui tourne en mode « args », sans serveur SSH ; l'amorce v11 pousse puis dort ; `execute` et `copy` sont refusés à la clé ; variante B faisable, l'amorce poussant adaptateurs, mesures, textes des actions et sous-ensemble d'activations, l. 318 à 321). Ces noms de fichiers ont été relus à l'amorce gelée (`git show 1609a4bf:scripts/amorce_instance_t06_v11.sh`, l. 318 à 321, lue au brouillon 1).

## 1. Ce qui change (et seulement cela)

| Demande de la mère | Brouillon 3 |
|---|---|
| retirer le § 4.13 « instance gardée arrêtée pour l'étape A » | ancien § 4.13 (vérification de `GO-ETAPE-A-T07`, garde de l'instance) retiré ; ancien § 4.14 devenu § 4.13 « Destruction » : après une fin normale et un rapatriement vérifié, destruction de l'instance de 7b par son identifiant, sans attendre ; après un arrêt, une fin anormale ou un refus, dès le rapatriement ; écart sur les données : sur le mot de la mère |
| destruction au plus tard le 16 à 23:00Z | gardée, dans tous les cas |
| retirer le marqueur `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07` | retiré (texte et table du § 14) ; cinq marqueurs restent, une occurrence chacun |
| une ligne : l'étape A se joue ailleurs, par la variante B | § 0 ; repris au § 4.13 (une demi-ligne), § 11 et § 12 |
| vérifier au rapatriement, par leurs compagnons, adaptateurs, mesures, textes des actions, sous-ensemble d'activations, sans rien ouvrir d'autre | § 4.12, bloc neuf : comptes par motif de nom (liste de noms tirée des arbres, sans contenu) ; pour chaque fichier, compagnon présent et lu (seul blob extrait), une ligne « empreinte, deux espaces, nom » ; aucune donnée rapatriée, ouverte ni hachée ; attendu 2, 1, 1, 1, au moins 1 morceau ; tout écart : compte rendu à la mère avant toute destruction |

Retouches de cohérence : § 2 points 4 et 5 (seuls les compagnons des données sont lus) ; rapatriement (§ 4.12) ; renvois § 4.14 → § 4.13 (§ 5, § 6, § 8) ; § 9 (mention du redémarrage pour l'étape A retirée ; `start` reste interdit) ; § 10 (compagnons des données au compte rendu) ; § 13 (point 3 sur l'étape A retiré) ; § 4.3 (écriture de `ligne-scellement-t07.txt`, qui ne servait qu'à l'ancien § 4.13, retirée).

## 2. Contrôles faits (lecture seule, aucune écriture hors des sorties)

- 18 blocs `bash` : `bash -n` sans erreur ; extrait Python des gardes : `ast.parse` ; sections 4.0 à 4.13, 0 à 14.
- Marqueurs : `ID_SESSION_FILLE`, `DEPENSE_ANTERIEURE_USD`, `COMMIT_MAIN_REMISE`, `LIGNE_SCELLEMENT_T07`, `LIGNE_REGISTRE_BRAS_B`, une occurrence chacun ; plus aucune mention de `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07` ni de `GO-ETAPE-A-T07`.
- Bloc neuf éprouvé en mémoire (liste factice, `git` remplacé par une fonction qui rend un compagnon bien formé) : cas sain `OK` ; compagnon des textes retiré de la liste → `ÉCART` sur ce seul fichier.
- 62 jetons de garde comparés au brouillon 2 : aucun perdu.
- Taille : 44 501 octets.

## 3. Point ouvert

- Si un fichier de données manque à la branche (par exemple resté sur l'instance au-delà de 90 Mo, amorce C11), la variante B en serait privée : l'ordre suspend la destruction jusqu'au mot de la mère, toujours au plus tard le 16 à 23:00Z ; récupérer un fichier resté sur l'instance n'est pas dans cet ordre (ni `copy` ni `execute` : R-2112).
- Aucun refus de permission ni de classifieur ; aucun appel externe, aucune dépense, aucune écriture git, aucune valeur de clé lue.
