"""Brouillon 9 de l'addendum n° 1 de SPARKS-EXP7-NUL, écrit par script (consigne de la mère, 5 novembre 2026 ≈ 08:24 UTC,
complétée à 08:26 UTC par le résultat du tir 4).

brouillon 9 = brouillon 8 (`def17de7…`) + couples B9-1 à B9-16, appliqués dans l'ordre, chaque « ancien » unique au moment
de son application. Les « anciens » des blocs remplis au brouillon 8 sont lus dans les couples du brouillon 8
(`couples-brouillon8-v1.json`, `fb122334…`), à l'identique. Contenu calculé ici, jamais saisi à la main :
- liste fermée des fichiers changés : `git diff --name-status --no-renames 55399606..78671d93`, comparée à l'égalité exacte
  au fichier de la liste au commit du code (v12) ; empreintes lues au commit (`git show`) ;
- comptes : lignes de résultat lues dans les sorties brutes des essais, des bancs et des répétitions (chemin et empreinte) ;
  le banc complet v12, s'il n'est pas fini, reçoit le seul marqueur « À REMPLIR » de ce brouillon ;
- contrôles finaux : marqueurs restants comptés, `controle_ia.prereg.problemes` rend `[]` une fois les marqueurs remplis
  pour simulation.

    /home/user/controle-ia-travail/.venv/bin/python -I -B appliquer-couples-addendum-1-brouillon9-v1.py > sortie-appliquer-couples-addendum-1-brouillon9-v1.txt
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RACINE / "src"))
from controle_ia.prereg import problemes  # noqa: E402

ICI = Path(__file__).resolve().parent
B8 = RACINE / "prereg" / "SPARKS-EXP7-NUL-addendum-1-brouillon8.md"
B9 = RACINE / "prereg" / "SPARKS-EXP7-NUL-addendum-1-brouillon9.md"
SHA_B8 = "def17de79019847a397c96e1fc8d8312ab0c2f596c10275678d65d2c96fa3fa7"
C8 = ICI / "couples-brouillon8-v1.json"
SHA_C8 = "fb122334377e1132102a09163356957ba745720a91a04ff80ff67f42a7ac0da0"
BASE = "55399606f268713bc1d52a9d18ef1e37c681028d"
CODE = "78671d9362c82a3ef02312bcf80c076a19069d42"
LISTE = "src/controle_ia/sparks_exp7_nul_v12/liste-fermee-v1.txt"
COUPLES = ICI / "couples-brouillon9-v1.json"
MARQUE = "À REMPLIR"
ORDRE_V3 = RACINE / "docs" / "procedures" / "ordre-fille-sparks-exp7-nul-lancement-reel-v3.md"
BANC_V12 = ICI / "essais-et-banc-sparks-v12" / "banc-78671d93.txt"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(*a: str) -> bytes:
    return subprocess.run(["git", "-C", str(RACINE), *a], check=True, capture_output=True).stdout


def rel(p: Path) -> str:
    return str(p.relative_to(RACINE))


def liste_fermee() -> tuple[list[tuple[str, str]], str]:
    diff = [l.split("\t") for l in git("diff", "--name-status", "--no-renames", f"{BASE}..{CODE}").decode().splitlines() if l]
    assert {s for s, *_ in diff} == {"A"}
    changes = sorted(p[-1] for p in diff)
    texte = git("show", f"{CODE}:{LISTE}")
    liste = [l.strip() for l in texte.decode().splitlines() if l.strip() and not l.lstrip().startswith("#")]
    assert len(set(liste)) == len(liste) and sorted(liste) == changes, "différence ≠ liste fermée"
    return [(p, sha(git("show", f"{CODE}:{p}"))) for p in changes], sha(texte)


def ligne_resultat(p: Path) -> str:
    lignes = [l.strip() for l in p.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    code = next((l for l in reversed(lignes) if re.fullmatch(r"code -?\d+", l)), None)
    if p.name.startswith("banc") and "seul" in p.name:
        r = next((l for l in reversed(lignes) if l.startswith("mutations v")), "aucune ligne de synthèse")
        r += f" ; {sum(1 for l in lignes if l.startswith('TUÉE'))} tuées"
    elif p.name.startswith("banc"):
        r = next((l for l in reversed(lignes) if "tuées" in l), "aucune ligne de synthèse")
    else:
        r = next((l for l in reversed(lignes) if re.search(r"\d+ (passed|failed)", l)), "aucune ligne de synthèse")
    return r + (f" ; {code}" if code else "")


def comptes() -> tuple[str, bool]:
    lignes = []
    dossiers = []
    for d in sorted(ICI.glob("essais-et-banc-sparks-v*"), key=lambda d: int(d.name.rsplit("v", 1)[1])):
        dossiers.append(d)
        dossiers += sorted(x for x in d.glob("commit-*") if x.is_dir())
    for d in dossiers:
        for f in sorted(d.glob("*.txt")):
            if f.name.startswith(("essais", "essai-", "banc")):
                lignes.append(f"| `{rel(f)}` | `{sha(f.read_bytes())}` | {ligne_resultat(f)} |")
    fini = BANC_V12.exists() and any(re.fullmatch(r"code -?\d+", l.strip()) for l in BANC_V12.read_text(encoding="utf-8").splitlines())
    rep = []
    for d in sorted(ICI.glob("repetition-jouet-v*")):
        f = (d / "attendus.txt") if (d / "attendus.txt").exists() else next(iter(sorted(d.glob("sortie-repetition-*.txt"))), None)
        if f is None:
            f = d / "00-commit.txt"
            rep.append(f"| `{rel(d)}/` | `{sha(f.read_bytes())}` (`00-commit.txt`) | interrompue avant la création (redémarrage du conteneur) |")
            continue
        t = f.read_text(encoding="utf-8", errors="replace")
        rep.append(f"| `{rel(f)}` | `{sha(f.read_bytes())}` | {len(re.findall(r'^\s+OK\s', t, re.M))} « OK », {len(re.findall('ÉCART', t))} « ÉCART » |")
    v12 = ("" if fini else
           f"\n\n**Banc complet v12** (commit `78671d93`, 265 mutations, 11 témoins ; `essais-et-banc-sparks-v12/banc-78671d93.txt`) : {MARQUE}.")
    texte = (
        "au commit final `78671d93` (v12) : essais (v1 à v4 et v12) à la tête, « "
        + ligne_resultat(ICI / "essais-et-banc-sparks-v12" / "essais-tete-78671d93.txt") + " », et sur un commit enfant qui porte "
        "l'addendum factice (`COMMIT_CODE` posé), « " + ligne_resultat(ICI / "essais-et-banc-sparks-v12" / "essais-enfant-be84eb4d.txt")
        + " » ; mutations v12 seules : « " + ligne_resultat(ICI / "essais-et-banc-sparks-v12" / "banc-v12-seul-78671d93.txt") + " » ; "
        "bancs complets achevés : v10 (245/245) et v11 (258/258), 0 défaut (première table). Tous les runs versés, par version "
        "(sortie brute, empreinte, ligne de résultat lue par script ; les runs joués pendant l'écriture, sur des fichiers non "
        "committés, et les runs interrompus sont comptés dans les additifs v2 à v12, section des comptes) :\n\n"
        "| Sortie | sha256 | Résultat |\n|---|---|---|\n" + "\n".join(lignes) + "\n\n"
        "Répétitions jouet des scripts d'instance (`MODE=jouet`), toutes comptées (R4 ; v4 à v8 jouées par la mère avec le "
        "dépôt distant, v9 jouées en local par le rédacteur-développeur, sans réseau ; aucune répétition complète des codes "
        "v10 à v12, R-1534 : les tirs réels en tiennent lieu, section « Tirs réels ») :\n\n"
        "| Sortie | sha256 | Attendus |\n|---|---|---|\n" + "\n".join(rep) + "\n\n"
        "Les bancs à 49 sur 50 (`ee91412d`), à 29 sur 30 (`96aae619`) et à 12 sur 13 mutations v11 (`da7116b9`) sont dans la "
        "première table ; leurs survivantes ont été tuées par des essais renforcés (additifs v2, v4 et v11)." + v12)
    return texte, fini


def couples(b8: list[dict], fichiers, sha_liste, texte_comptes, fini, heure) -> list[dict]:
    n8 = {c["n"]: c["nouveau"] for c in b8}
    table = "\n".join(f"| `{p}` | `{h}` |" for p, h in fichiers)
    ad = {v: sha((ICI / f"rapport-developpeur-addendum-1-v{v}.md").read_bytes()) for v in (9, 10, 11, 12)}
    tirs = (
        "**Tirs réels** (R-1477 ; tous rapportés, R4 ; sous GO-2026-11-05-02, puis l'enveloppe commune de 5 USD de "
        "GO-2026-11-05-05 ; cumul des quatre tirs ≈ 0,050 USD) :\n\n"
        "| Tir | Code lancé | Instance | Résultat | Dépense | Source |\n|---|---|---|---|---|---|\n"
        "| 1 | v9 `4d07d2a6` (commit de tir `e1542f4a`) | 59219396 | **boucle** : image sans `curl` ; l'amorce v9 sortait sur « curl "
        "absent » avant sa minuterie ; plus de 110 relances par Vast de 06:27:17 à 06:35:02Z ; `journal-amorce` v9 aveugle à ce cas "
        "(REDEMARRAGES=0) ; détruite par son identifiant (`-y`) à 06:35:18Z | ≈ 0,0095 USD | R-1537 ; rapport de la fille "
        "`canal/fille-2026-11-04` `06a602a7`, `a51942b1…` |\n"
        "| 2 | v10 `3196884f` (commit de tir `b80b91c6`) | 59227134 | **conforme** : « AMORCE V10 DEMARRAGE 1 », installation de "
        "ca-certificates, curl et git (code 0), refus à la garde du code (aucun addendum), attente de 300 s, **destruction par "
        "l'instance elle-même** ; DEMARRAGES=1, BOUCLE=non ; absente à 07:31:03Z | ≤ 0,0107 USD | R-1544 ; `de25c88d`, `69960f19…` |\n"
        "| 3 | v11 `cabc06e5`, jouet sur machine (commit de tir `934e4824`) | 59231131 | **arrêt obtenu sur Vast** : « ARRÊT OBTENU "
        "(état voulu « stopped », HTTP 200) » à 07:59:50Z ; « exited » / `cur_state` « stopped » à 08:02:41 et 08:05:43Z ; aucune "
        "relance ; DEMARRAGES=1 ; verdict du script « boucle », **artefactuel** (inventaire de 07:59:39Z, antérieur à l'arrêt ; le "
        "conteneur n'avait démarré qu'à 07:58:17Z, environ 4 min après la création ; corrigé en v12) ; détruite par son identifiant "
        "par la fille à 08:06:14Z ; ordre « fin », `start` et destruction par l'amorce non éprouvés | ≤ 0,0124 USD | R-1547 ; "
        "`69cfe34e`, `e475db53…` |\n"
        "| 4 | v11 `cabc06e5`, jouet sur machine (commit de tir `934e4824` réutilisé du tir 3, écart déclaré) | 59232437 (T0 "
        "08:08:20Z) | **conforme sur toute la chaîne** : « ARRÊT OBTENU (HTTP 200) » à 08:13:09Z ; `cur_state` « stopped » à "
        "08:13:59, 08:17:01 et 08:20:02Z ; verdict « arretee » (inventaires pris seulement après « ARRÊT OBTENU » : écart de "
        "pilotage ordonné, que le verdict v12 fait de lui-même) ; ordre « fin » `28fbd7a0` sur "
        "`ordres/sparks-exp7-nul-v5-934e4824a36d` ; `start` à 08:20:33Z ; DEMARRAGES=2 (08:20:35Z), BOUCLE=non ; **destruction par "
        "l'amorce** (absente à 08:24:21Z) | ≤ 0,0172 USD | rapport `4aff1047`, "
        "`rapport-tir-sparks-exp7-nul-v11-quatrieme-2026-11-05-0826.md`, `bc9ee3da…` |\n\n"
        "Le tir 4 a joué l'amorce v11 ; l'amorce v12 lui est égale aux chemins de version près (essai à l'octet, additif v12). Restent "
        "non éprouvés sur Vast : la copie de lots (`vastai copy`) et la phase causale réelle (risques déclarés, section « Minuterie »).\n\n"
        "**Nom définitif et commit de lancement.** L'addendum scellé est `prereg/SPARKS-EXP7-NUL-addendum-1.md` (nom lu par "
        "`garde_code` et `plan.CHEMIN_ADDENDUM`), avec son compagnon `.sha256`. Le commit de lancement est un **enfant du commit "
        "du code `78671d93…`** sur `prep/sparks-exp7-nul-v12`, qui ajoute ces deux fichiers **et `registres/go.md` de `main`** "
        "(ligne d'extension de GO-2026-11-04-04 à 40 USD ; sans elle, le lanceur et l'amorce refusent), et rien d'autre (la garde "
        "refuse toute différence sous `src/`, `tests/` ou `scripts/`). Ordre de lancement : "
        f"`docs/procedures/ordre-fille-sparks-exp7-nul-lancement-reel-v3.md` (`{sha(ORDRE_V3.read_bytes())}`).\n\n"
        "**Puissance de M5** : section « Seuil » ci-dessous.")
    v1012 = (
        "**Compléments à la liste (tirs réels v9 à v11 : R-1537, R-1542, R-1547).** Codes neufs, chacun descendant du précédent, "
        "fichiers neufs seulement : **v10** (`prep/sparks-exp7-nul-v10`, `3196884f`) : l'amorce ne dépend plus d'aucun outil absent "
        "de l'image (premier geste en bash seul, une ligne de démarrage « AMORCE V10 DEMARRAGE <n> » à compteur gardé sur le disque ; "
        "outils exigés installés par `apt-get` sous `timeout` ; destruction de secours par `python3` si `curl` manque) ; **tout refus "
        "avant l'ordre consommé détruit l'instance** au lieu de sortir (une sortie fait relancer le conteneur par Vast) ; destruction "
        "non obtenue : `sleep infinity`, dit au journal ; `journal-amorce` compte les démarrages et rend la boucle ; **v11** "
        "(`prep/sparks-exp7-nul-v11`, `da7116b9` puis `cabc06e5`) : **en fin normale de phase** (fabrication, fenêtre de copie, "
        "phase causale sans destruction), **l'amorce met l'instance à l'état voulu « stopped » par l'interface de Vast** (`PUT "
        "/instances/<id>/`, clé du conteneur), exige HTTP 2xx et `\"success\": true`, puis sort ; arrêt non obtenu : destruction "
        "(perdues : les couches des modèles et du départ) ; mode jouet sur machine réelle pour les tirs (`MODE=jouet`, "
        "`JOUET_MACHINE=1`, addendum factice marqué) ; **v12** (`prep/sparks-exp7-nul-v12`, `78671d93`) : **verdict de boucle sur "
        "les seuls inventaires postérieurs à la ligne « ARRÊT OBTENU »** (heure lue au journal ; sinon création + 900 s) ; amorce "
        "v12 égale à la v11 aux chemins de version près. La liste fermée v12 (`src/controle_ia/sparks_exp7_nul_v12/liste-fermee-v1.txt`) "
        "compte les fichiers v2 à v12 ; la garde de lancement (amorce v12) lit celle-ci. Fonction par fonction : additifs "
        f"`docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v10.md` (`{ad[10]}`), `-v11.md` (`{ad[11]}`) et "
        f"`-v12.md` (`{ad[12]}`). **Codes v9 à v12 non contre-lus** (R-1534) : section « Contre-lecture ».\n")
    marq_reste = ("le compte du banc complet v12 (section 2, marqueur)" if not fini else "aucun")
    return [
        {"n": "B9-1", "ancien": "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 8\n",
         "nouveau": "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 9\n"},
        {"n": "B9-2", "ancien": "toujours avant toute donnée. Brouillon 8 écrit par script le 5 novembre 2026 à 06:26 UTC (`date -u`), toujours avant toute donnée.",
         "nouveau": "toujours avant toute donnée. Brouillon 8 écrit par script le 5 novembre 2026 à 06:26 UTC (`date -u`), toujours avant toute "
                    f"donnée. Brouillon 9 écrit par script le 5 novembre 2026 à {heure} UTC (`date -u`), toujours avant toute donnée (les tirs "
                    "réels n'entraînent aucun modèle et ne lisent aucune donnée de l'expérience)."},
        {"n": "B9-3", "ancien": n8["B8-3"].split("\n")[1] + "\n",
         "nouveau": n8["B8-3"].split("\n")[1] + "\n- Brouillon 9 : brouillon 8 (`def17de7…`) + les couples B9-1 à B9-16 du même rédacteur-développeur, "
                    "appliqués par script (`docs/notes/weight-space-programming-v1/appliquer-couples-addendum-1-brouillon9-v1.py`, couples "
                    "`couples-brouillon9-v1.json` et sortie `sortie-appliquer-couples-addendum-1-brouillon9-v1.txt`, même dossier), demandés "
                    "par la mère le 5 novembre 2026 vers 08:24 UTC : code final v12, liste fermée et comptes, compléments v10 à v12, tirs "
                    "réels 1 à 4, jeton GitHub, nom définitif et commit de lancement (section 00000000). **Aucun sous-agent neuf n'a relu "
                    "ce brouillon** (R-1534).\n"},
        {"n": "B9-4", "ancien": "## 0000000. Changements du brouillon 7 au brouillon 8 (avant → après ; raison ; source)\n",
         "nouveau": "## 00000000. Changements du brouillon 8 au brouillon 9 (avant → après ; raison ; source)\n\n"
                    "Brouillon 9 : couples B9-1 à B9-16 du rédacteur-développeur, appliqués dans l'ordre par script, chacun unique au "
                    "moment de son application ; aucune contre-lecture (R-1534) : réserve.\n\n"
                    "| N° | Avant → après | Raison | Source |\n|---|---|---|---|\n"
                    "| B9-1 à B9-4 | titre, en-tête, journal au brouillon 8 → brouillon 9 ; cette section | exactitude | consigne de la mère |\n"
                    "| B9-5 | compléments jusqu'à la v9 → plus les compléments v10 à v12 | codes v10 à v12 | additifs v10 à v12 |\n"
                    "| B9-6 à B9-8 | commit final v9 `4d07d2a6`, liste fermée v9 (188), comptes au commit v9 → commit final v12 `78671d93`, liste fermée v12 (240, égalité vérifiée par script), comptes des essais et des bancs v10 à v12 | code final v12 | consigne de la mère |\n"
                    "| B9-9 | résultat du tir réel à remplir → tirs 1 à 4 rapportés (R4), nom définitif et commit de lancement | tirs réels | rapports de la fille ; R-1537, R-1544, R-1547 |\n"
                    "| B9-10 à B9-12 | (iv) code v9 → codes v9 à v12, plus (v) arrêt en fin de phase et destruction sur tout refus précoce ; noms gardés par les codes v5 à v12 | codes v10 à v12 | additifs v10 et v11 |\n"
                    "| B9-13 | — → jeton GitHub de l'instance : échéance au moins le 18 novembre exigée avant la création | le jeton actuel expire le 5 novembre à 10:00:36 UTC | consigne de la mère |\n"
                    "| B9-14 | épreuves : répétitions de la v9 → plus les tirs réels pour les codes v10 à v12 | état | tirs 1 à 4 |\n"
                    "| B9-15, B9-16 | contre-lecture et pied : code v9 et brouillon 8 non relus → codes v9 à v12 et brouillons 8 et 9 non relus ; reste avant scellement | R-1534 | mot de Lazar |\n\n"
                    "## 0000000. Changements du brouillon 7 au brouillon 8 (avant → après ; raison ; source)\n"},
        {"n": "B9-5", "ancien": "**Code v9 non contre-lu** (R-1534) : section « Contre-lecture ».\n",
         "nouveau": "**Code v9 non contre-lu** (R-1534) : section « Contre-lecture ».\n\n" + v1012},
        {"n": "B9-6", "ancien": n8["B8-6a"],
         "nouveau": f"descendant de `55399606`) : `{CODE}` (branche `prep/sparks-exp7-nul-v12` ; version de code citée dans ce texte : "
                    "v12, amorce `scripts/amorce_instance_sparks_exp7_nul_v12.sh`, lanceur v12). **Dernière version, non contre-lue** "
                    "(R-1534, mot de Lazar) : la dernière version contre-lue est la v8 (`4fd10407`, « Contre-lecture 5 »)."},
        {"n": "B9-7", "ancien": n8["B8-6b"],
         "nouveau": f"contrôlé par script au scellement) : **{len(fichiers)} fichiers**, tous ajoutés (`git diff --name-status --no-renames "
                    f"55399606..78671d93` : {len(fichiers)} « A », aucun autre statut), égaux, à l'égalité exacte, au fichier de la liste au "
                    f"commit du code (`{LISTE}`, sha256 `{sha_liste}`), contrôle fait par "
                    "`docs/notes/weight-space-programming-v1/appliquer-couples-addendum-1-brouillon9-v1.py` ; empreintes lues au commit "
                    "`78671d93` (`git show`) :\n\n| Fichier | sha256 |\n|---|---|\n" + table + "\n"},
        {"n": "B9-8", "ancien": n8["B8-6c"], "nouveau": "et le banc à 49 sur 50 du commit `ee91412d`) : " + texte_comptes + "\n"},
        {"n": "B9-9", "ancien": n8["B8-7"], "nouveau": tirs},
        {"n": "B9-10", "ancien": "(iv) **code v9** : à tout redémarrage sans ordre neuf",
         "nouveau": "(iv) **codes v9 à v12** : à tout redémarrage sans ordre neuf"},
        {"n": "B9-11", "ancien": "(la dépense est protégée plutôt que les modèles).",
         "nouveau": "(la dépense est protégée plutôt que les modèles) ; (v) **codes v10 à v12** : **tout refus avant l'ordre consommé**, "
                    "création comprise, détruit l'instance au lieu de la laisser sortir (une sortie fait relancer le conteneur par Vast, "
                    "tir 1) ; une destruction non obtenue laisse le conteneur en attente (`sleep infinity`), sans boucler ; **en fin normale "
                    "de phase** (fabrication, fenêtre de copie, phase causale sans destruction), l'amorce met l'instance à l'état voulu "
                    "« stopped » par l'interface de Vast, vérifié (HTTP 2xx et « success » vrai), puis sort ; arrêt non obtenu : "
                    "destruction, perdues les couches restées sur le disque (obtenu sur Vast aux tirs 3 et 4)."},
        {"n": "B9-12a", "ancien": "(`sparks-v5-detruire` pour les amorces v5 à v9, qui gardent les noms de la v5)",
         "nouveau": "(`sparks-v5-detruire` pour les amorces v5 à v12, qui gardent les noms de la v5)"},
        {"n": "B9-12b", "ancien": "(nom gardé par les codes v5 à v9 ;", "nouveau": "(nom gardé par les codes v5 à v12 ;"},
        {"n": "B9-13", "ancien": "Le tir réel n'exécute aucun code tiers (arrêt à la garde du code, avant toute installation).\n",
         "nouveau": "Le tir réel n'exécute aucun code tiers (arrêt à la garde du code, avant toute installation).\n"
                    "- **Jeton GitHub de l'instance.** Passé à la création (`GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN`), il est fixé pour toute "
                    "la vie de l'instance : il sert au clone, à la lecture des ordres à chaque redémarrage et aux poussées. **Un jeton dont "
                    "l'échéance est au moins le 18 novembre 2026 est exigé avant la création** ; le jeton actuel expire le 5 novembre 2026 "
                    "à 10:00:36 UTC, et un jeton neuf est attendu de Lazar. Un jeton expiré rend les ordres illisibles au redémarrage, ce qui "
                    "est une boucle présumée, donc une destruction avec les modèles ; en fin de phase, il fait échouer la poussée.\n"},
        {"n": "B9-14", "ancien": "la différence `a655bbfa..4d07d2a6` se limite à `nouvel_id`, éprouvé par essais et banc.",
         "nouveau": "la différence `a655bbfa..4d07d2a6` se limite à `nouvel_id`, éprouvé par essais et banc. **Codes v10 à v12** (R-1534 : "
                    "aller vite) : aucune répétition jouet complète ; éprouvés sur processeur (essais et bancs, section 2) et par les tirs "
                    "réels (section 2, « Tirs réels ») : un conteneur qui sort **est relancé par Vast** (tir 1) ; la destruction par "
                    "l'instance elle-même sur un refus précoce est obtenue (tir 2) ; l'arrêt de l'instance par l'interface en fin de phase "
                    "est obtenu, puis, après l'ordre « fin » et le `start`, la destruction par l'amorce (tirs 3 et 4)."},
        {"n": "B9-15", "ancien": n8["B8-11a"],
         "nouveau": ". Codes v9 à v12 faits (`4d07d2a6`, `3196884f`, `cabc06e5`, `78671d93` ; additifs v9 à v12). **Aucune contre-lecture "
                    "neuve n'a relu les codes v9 à v12 (`git diff 4fd10407..78671d93`) ni les brouillons 8 et 9** : mot de Lazar, R-1534 "
                    "(aller vite). R2 est tenue par les contre-lectures 1 à 5 ci-dessus, qui ont relu le texte jusqu'au brouillon 6 et le "
                    "code jusqu'à `4fd10407` ; les codes v9 à v12 et les couples des brouillons 8 et 9 ne sont relus par personne : "
                    "**réserve**. Les tirs réels 1 à 4 (section 2) ont éprouvé sur Vast ce que les essais ne pouvaient pas éprouver."},
        {"n": "B9-16a", "ancien": n8["B8-11b"],
         "nouveau": "Brouillon 9 (5 novembre 2026, couples du même rédacteur-développeur, appliqués par script, sans contre-lecture : "
                    "R-1534), sur le b" + n8["B8-11b"][1:]},
        {"n": "B9-16b", "ancien": n8["B8-11c"],
         "nouveau": f"Reste avant scellement : {marq_reste}. Les éléments de la section 2 (commit final v12, liste fermée et empreintes, "
                    "comptes rejoués, tirs réels 1 à 4, nom définitif et commit de lancement) sont remplis par script au brouillon 9."},
    ]


def main() -> int:
    heure = datetime.now(timezone.utc).strftime("%H:%M")
    t8 = B8.read_bytes()
    assert sha(t8) == SHA_B8, "brouillon 8 altéré"
    assert sha(C8.read_bytes()) == SHA_C8, "couples du brouillon 8 altérés"
    assert not B9.exists() and not COUPLES.exists(), "brouillon 9 ou ses couples existent déjà (R12)"
    fichiers, sha_liste = liste_fermee()
    texte_comptes, fini = comptes()
    c = couples(json.loads(C8.read_text(encoding="utf-8")), fichiers, sha_liste, texte_comptes, fini, heure)
    COUPLES.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    t = t8.decode("utf-8")
    assert t.count(MARQUE) == 1, t.count(MARQUE)
    for k in c:
        n = t.count(k["ancien"])
        assert n == 1, f"{k['n']} : « ancien » trouvé {n} fois"
        t = t.replace(k["ancien"], k["nouveau"])
        print(f"{k['n']} appliqué (ancien unique)")
    attendus = 0 if fini else 1
    assert t.count(MARQUE) == attendus, (t.count(MARQUE), attendus)
    B9.write_text(t, encoding="utf-8")
    p = problemes(B9)
    with tempfile.TemporaryDirectory() as d:
        s = Path(d) / "b9-rempli.md"
        s.write_text(t.replace(MARQUE, "rempli pour simulation"), encoding="utf-8")
        p_rempli = problemes(s)
    print(f"brouillon 8 : {rel(B8)} {SHA_B8}")
    print(f"couples : {rel(COUPLES)} {sha(COUPLES.read_bytes())} ({len(c)} couples)")
    print(f"brouillon 9 : {rel(B9)} {sha(B9.read_bytes())} (écrit à {heure} UTC)")
    print(f"liste fermée : {len(fichiers)} fichiers, égale au fichier {LISTE} au commit {CODE} (sha256 {sha_liste})")
    print(f"banc complet v12 fini : {fini}")
    print(f"marqueurs « {MARQUE} » restants : {t.count(MARQUE)}" + ("" if fini else " (compte du banc complet v12)"))
    print(f"prereg.problemes(brouillon 9) : {p}")
    print(f"prereg.problemes(brouillon 9, marqueurs remplis pour simulation) : {p_rempli}")
    assert p_rempli == [], p_rempli
    assert p == ([] if fini else ["marqueur À REMPLIR restant hors des sections exigées"]), p
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
