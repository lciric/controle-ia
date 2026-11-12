# Ordre à la fille — tours du collisionneur v9 des mentors du soir (Ibrahim Q1, Scheurer) — v1

Écrit par session-depot le 3 novembre 2026 à 11:40 UTC (heure relevée par `date -u` à 11:38:32). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mots directs de Lazar : « go direct à session-depot pour les deux tours, entre 20 et 35 USD
chacun » ; « go trois tours et course Ibrahim ; pas de plafond ». Dépôt Pivotal ce soir 23:00 UTC : à lancer **tout de suite, en
parallèle** de la course Kirchner (qui garde Argon) et de la suite D + E du tour Kirchner. Le troisième tour (Colognese et Ward Q2)
suivra par un message, avec le même gabarit.

## 1. Deux tours, variante SANS ARGON (C absente, déclarée ; contrôle ABDE ; clé Gemini factice)
| Tour | GO | Branche, commit | Lanceur | `PLAFOND_USD` | Port Kimi |
|---|---|---|---|---|---|
| Ibrahim Q1 | GO-2026-11-03-06 (35 USD) | `donnees/collisionneur-v9-ibrahim-q1-v1` `437c4d5e` | `lancer-tour-ibrahim-q1-v9-sans-argon-v1.sh` (`6293da64…`) | 27 | 8814 |
| Scheurer | GO-2026-11-03-07 (35 USD) | `donnees/collisionneur-v9-scheurer-v1` `f9fd47b7` | `lancer-tour-scheurer-v9-sans-argon-v1.sh` (`bd23fc0c…`) | 26 | 8815 |

Pour chacun : `main` tiré (lignes GO-06 et GO-07 au registre) ; branche extraite par `git archive` sans toucher à l'index ;
`sha256sum -c` de tous ses compagnons ; lis son LISEZMOI (commande exacte en quatre lignes, garde R12 **au premier plan**) ;
`PY_COLLISIONNEUR=/home/user/venv-relais-claude/bin/python` ; ports 8814 et 8815 libres ; lanceur détaché, PID réel au journal ;
attente suivie par ton harnais pour chacun. Aucun appel à Argon (garde du port 8805 : la course Kirchner l'occupe, c'est attendu — la
variante sans Argon ne doit pas la refuser pour cela ; si elle refuse, dis-le-moi au lieu de contourner).

## 2. Après chaque tour
`verifier` sur le run (attendu 12 cellules valides, C absente acceptée) ; scellement avant toute lecture ; branche neuve
`<branche>-run` partie du commit du tour ; contrôle des motifs de clé ; rapport scellé (commit, empreintes, code, durée, dépense par
espèce) ; message à session-depot **dès chaque tour fini** (je copie au canal tout de suite) ; aucun relais restant.
