# Rapport d'audit — verdict « agrégateurs sur les scores réels de R1 v4 » — v1

Lecteur neuf (R13) : sous-agent **Claude Opus 5.5 (lignée Opus)**, session `session_01Qi7Gr2gdFYZivRDWLZzkXA`.
Début 13:07:15 UTC, fin 13:16 UTC environ, le 6 novembre 2026 (`date -u`). Verdict :
`docs/verdicts/verdict-agregation-r1-v4-v1.md`.

## 1. Ce qui a été fait

| tâche de la consigne | fait | pièce |
|---|---|---|
| consigne : empreinte et compagnon au commit `b8abaabb` | `67caea0e…0a8` deux fois | `sorties/integrite_agregation_v1.txt` |
| texte égal sur `b8abaabb`, `60ddbedb`, `913a80cc` ; compagnon | `5916e62e…5015` trois fois | idem |
| table de 21 lignes contre `1fcb23d7`, `60ddbedb`, `913a80cc` | 63 égalités sur 63 | idem |
| aucun changement de code entre `1fcb23d7` et `60ddbedb` | seuls `brouillons/` et `prereg/` changent | idem |
| `913a80cc` n'ajoute que la sortie | six fichiers ajoutés (manifeste, sortie, journal, compagnons) | idem |
| un seul manifeste cite le texte | `runs/20261106-130318-agregation-r1-v4/manifeste.json` seul | idem |
| manifeste, sortie, journal : empreintes = compagnons | `f4f152a5…`, `d3c33d1c…`, `43670dd3…` | idem |
| `scores-p3.npz` | manifeste = texte = compagnon `968414fc…04cf` (fichier non extrait) | idem |
| activations | manifeste = `rejeu-activations.json` l. 153-154 (`27b9bd5a…`, `c0c71757`) ; compagnons de réception absents des références locales | idem |
| commande, commit, arbre propre, graines | conformes (verdict, section 2) | `runs/…/manifeste.json` |
| gardes de puissance, de signal, de données | recalculées depuis la sortie, égales à la sortie | `sorties/lecture_verdict_agregation_v1.txt` |
| Holm, table des issues, `lire`, `lire_hag` | recalculés à la main ; code cité importé de l'arbre `913a80cc` (`analyse_v3.py` `75c0d219…`) ; tout égal | idem |
| déclencheurs R4 | recalculés : aucun ; égal à `audit_R4` | idem |
| essais cités | 41 passés (trois fichiers `tests/test_agregation_r1_v4*.py`) | `sorties/essais_agregation_r1_v4.txt` |

## 2. Issues

C1 « non concluant par construction (puissance simulée insuffisante ou signe simulé contraire) » ; C2 « confirmé à cette
puissance » ; C3 « confirmé à cette puissance » ; **H-AG « appuyée à m = 1 seulement »** (a_W = 0,9972). Chiffres : verdict,
section 3, et `sorties/lecture_verdict_agregation_v1.txt`, tous tirés de
`diag/20261106-130318-agregation-r1-v4/agregation-r1-v4-v1.json` (`d3c33d1c2af0decac3d46bf784e63f88fdfe41104eac6cadb6bffb710ad82b25`).

## 3. Audit R4 écrit d'avance

- **Trop propre** : non selon les seuils écrits. |contraste| 0,277 ≤ 0,35 ; C2 dans la plage simulée à a = 0,995 (−0,176 à
  −0,307 sur les quatre cellules, `gardes.porte`) ; aires à m = 1 non saturées (somme 0,701, maximum 0,978). Décomptes de paires
  cohérents (aire × nombre de paires entier ou demi-entier).
- **Plafond** : a_W = 0,9972 ≥ 0,95 → règle appliquée telle qu'écrite ; C3 = Δ_W(10) − Δ_W(1) avec Δ_W(10) = +0,00028 : C3 est
  porté par C2. Réserve.
- **Fuite** : déclencheur écrit (a_W ≥ 0,999) non atteint. Indice descriptif : sous W, 26,7 % des épisodes témoin dépassent
  la troisième valeur honnête (somme et maximum ; nominal 3,3 %) ; la mention, 23 à 57 %. Réserve, sans effet sur l'issue.
  L'audit sur les données prévu par le texte (identité des lignes, plis, réduction, positions des hybrides, aire recalculée à la
  main) n'est pas obligatoire ici et **n'a pas été fait** : il exige les activations, non extraites (consigne de l'appelant).
- **D1** : aucun contraste de Wm, Gt ou Ge entièrement sous 0.

## 4. Écarts et incidents du lecteur

- Rendu sous `/home/user/wt/verdictAG-rendu/`, sans branche, commit, poussée ni message (ordre de l'appelant, contre la
  section « Rendu » de la consigne).
- Les essais ont laissé des dossiers `__pycache__` dans `src/controle_ia/` de l'arbre `/home/user/wt/verdictAG` (créés à
  13:12:40 UTC malgré `PYTHONDONTWRITEBYTECODE=1`), fichiers ignorés par git ; je les ai supprimés aussitôt (les quatre dossiers
  créés après 13:07, rien d'autre). `git status --short --ignored` est vide ensuite.
- Une recherche `git grep` des empreintes d'activations a affiché quatre lignes d'empreintes d'entrée tirées des sorties de
  l'étape F (branche `analyses-r1-v4`) ; aucune valeur de résultat n'a été lue.
- Branche `prep/verdict-etape-F-r1-v4-v1` : absente des références locales vers 13:10 UTC ; aucun accès au dépôt distant.
- Aucune clé, aucune dépense, aucun `vastai`, aucun réseau, aucun `.sha256` écrit.

## 5. Empreintes des pièces de l'audit

| pièce | sha256 |
|---|---|
| `scripts/integrite_agregation_v1.sh` | `7c3e6d3dd4cc78c52fc6ad2656ae0f65d543dffb073b663b7e31957f413d616a` |
| `scripts/lecture_verdict_agregation_v1.py` | `9118045dc4c4d2e352dde81188dcef90194112fcbe5dc7bf32836be50d24f30d` |
| `sorties/integrite_agregation_v1.txt` | `5e0a28925a517ee0d1d8be87ae9adb4800258ae017aaedd3479bfe9870c1db6c` |
| `sorties/lecture_verdict_agregation_v1.txt` | `751132036236a00c640870ccb162622c828dffc5c006b358739a5b16bf0d0aa3` |
| `sorties/essais_agregation_r1_v4.txt` | `fd0c27aef59af375d9dcdb532400338469dd892835973f4248df069f652452d5` |

Les empreintes du verdict et de ce rapport sont dans le message de rendu à l'appelant (un fichier ne peut porter la sienne).
