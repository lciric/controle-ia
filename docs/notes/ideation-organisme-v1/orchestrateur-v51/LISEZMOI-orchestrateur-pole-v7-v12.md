# Orchestrateur du pôle, version 0.7.0 — la clé du relais hors de l'environnement (fichier à lecture unique), contrôle de /proc — LISEZMOI v12

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v12 écrite à partir de 19:30 UTC (heure lue sur
`date -u` : 19:29:55) ; v1 à v11 gardées (R12). Suite du constat F-C7 de la contre-lecture du code et du **message n° 92 de
session-depot** (19:26 UTC) : en (a) et (a) bis, le relais et les agents tournaient **sous le même utilisateur (root), dans
le même conteneur**, et la clé restait lisible dans `/proc/<pid du relais>/environ` (l'effacement de `os.environ` ne touche
pas le bloc initial) — le n° 117 de conv-audit disait à tort « sous un autre utilisateur, comme en (a) bis » (erreur de
conv-audit : une recommandation du LISEZMOI v5 prise pour un fait). Réserve de sûreté consignée par session-depot (R-589),
rotation de la clé recommandée à Lazar.

| changement | fichiers |
|---|---|
| **`--fichier-cle`** : le relais lit la clé dans un fichier **à lecture unique** (fichier ordinaire, mode sans droits de groupe ni d'autrui, une ligne), puis le supprime ; la clé n'entre jamais dans son environnement, donc jamais dans `/proc/<pid>/environ`, même pour root ; refus si la variable d'environnement est aussi présente (la clé n'est qu'à un seul endroit) ; `--variable-cle` reste pour compatibilité, avec sa limite écrite | `pole/relais_reel.py` (`lire_cle_fichier`, `principal`) |
| **contrôle de /proc** : `demonstrations/verification_cle_proc_v7.py --pid PID` dit si une variable de clé figure, **par son nom** (jamais la valeur), dans `/proc/PID/environ` (cas sain : aucune ; illisible = autre utilisateur, cas sain aussi) ; `--demonstration` joue les deux cas sur des processus factices à clé FACTICE (R5 : cas sain tenu, artefact tenu ; vérifié ici, code 0) | `demonstrations/verification_cle_proc_v7.py` (nouveau) |
| essais : lecture unique et mode du fichier (lisible par d'autres : refusé ; supprimé après lecture ; seconde lecture refusée) ; la démonstration /proc comme essai | `essais/test_v7_v11.py` (+2) |

**220 essais passent.**

## Ce que le duel attend de session-depot (commande exacte, à adapter aux chemins)

```bash
# 1. Dans la session de session-depot seulement : la clé dans un fichier à lecture unique, puis la variable retirée.
umask 077 && printf '%s\n' "$RR_ANTHROPIC_API_KEY_LUC" > /chemin/prive/cle-relais && unset RR_ANTHROPIC_API_KEY_LUC
# 2. Le relais, sans aucune variable de clé dans son environnement (env -i), lit le fichier et le supprime.
env -i PATH="$PATH" HOME="$HOME" /opt/venv/bin/python -I -B -m pole.relais_reel --fichier-cle /chemin/prive/cle-relais \
    --plafond-usd 100 --port 0 --journal /chemin/journal-relais.jsonl --reserve-par-appel 0.40 &
# 3. Contrôle (cas sain attendu : « aucune variable de clé : cas sain ») — à verser avec la course.
python -I -B demonstrations/verification_cle_proc_v7.py --pid <pid du relais>
# 4. Les agents : bac à sable du kit avec un /proc neuf (ne PAS régler enableWeakerNestedSandbox ; v11 exige le bac à
#    sable, failIfUnavailable) ; si bubblewrap ne peut pas monter /proc dans le conteneur, la course s'arrête d'elle-même :
#    il faut alors des agents sous un utilisateur non root, distinct de celui du relais.
# 5. Le duel : demonstrations/duel_proposeurs_v7.py DOSSIER --moteur claude-sdk --url-relais http://127.0.0.1:<port>/v1
```

Même avec le fichier à lecture unique, la clé vit dans la **mémoire** du relais : un agent root dans le même espace de
noms pourrait en principe la lire (`/proc/<pid>/mem`) ; seul un autre utilisateur ou un espace de noms propre ferme cela.

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v12.txt
$PY -I -B -m unittest                                                              # 220 essais
$PY -I -B demonstrations/verification_cle_proc_v7.py --demonstration               # code 0 attendu
```

Le reste : LISEZMOI v11.
