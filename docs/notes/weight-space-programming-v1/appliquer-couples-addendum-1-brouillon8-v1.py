"""Brouillon 8 de l'addendum n° 1 de SPARKS-EXP7-NUL, écrit par script (consigne de la mère, 5 novembre 2026 ≈ 06:22 UTC).

brouillon 8 = brouillon 7 (`357370e7…`) + couples B8-1 à B8-11, appliqués dans l'ordre, chaque « ancien » unique au moment
de son application. Contenu calculé ici, jamais saisi à la main :
- liste fermée des fichiers changés : `git diff --name-status --no-renames 55399606..4d07d2a6`, comparée à l'égalité exacte
  au fichier de la liste au commit du code ; empreintes lues au commit (`git show`) ;
- comptes : lignes de résultat lues dans les sorties brutes des essais, des bancs et des répétitions (chemin et empreinte
  de chaque sortie) ;
- contrôles finaux : un seul marqueur « À REMPLIR » (le résultat du tir réel), et `controle_ia.prereg.problemes` rend `[]`
  une fois ce marqueur rempli pour simulation.

    /home/user/controle-ia-travail/.venv/bin/python -I -B appliquer-couples-addendum-1-brouillon8-v1.py > sortie-appliquer-couples-addendum-1-brouillon8-v1.txt
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
B7 = RACINE / "prereg" / "SPARKS-EXP7-NUL-addendum-1-brouillon7.md"
B8 = RACINE / "prereg" / "SPARKS-EXP7-NUL-addendum-1-brouillon8.md"
SHA_B7 = "357370e711da1389dec05b21a00270b405cdde0391d09dadac0d032ffe265eae"
BASE = "55399606f268713bc1d52a9d18ef1e37c681028d"
CODE = "4d07d2a6830ab09cb91250016284efb5cbe8a91c"
LISTE = "src/controle_ia/sparks_exp7_nul_v9/liste-fermee-v1.txt"
ADDITIF_V9 = ICI / "rapport-developpeur-addendum-1-v9.md"
COUPLES = ICI / "couples-brouillon8-v1.json"
MARQUE = "À REMPLIR"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(*a: str) -> bytes:
    return subprocess.run(["git", "-C", str(RACINE), *a], check=True, capture_output=True).stdout


def rel(p: Path) -> str:
    return str(p.relative_to(RACINE))


# --- liste fermée ------------------------------------------------------------------------------------------------------
def liste_fermee() -> tuple[list[tuple[str, str]], str]:
    diff = [l.split("\t") for l in git("diff", "--name-status", "--no-renames", f"{BASE}..{CODE}").decode().splitlines() if l]
    statuts = {s for s, *_ in diff}
    assert statuts == {"A"}, statuts
    changes = sorted(p[-1] for p in diff)
    texte = git("show", f"{CODE}:{LISTE}")
    liste = [l.strip() for l in texte.decode().splitlines() if l.strip() and not l.lstrip().startswith("#")]
    assert len(set(liste)) == len(liste) and sorted(liste) == changes, "différence ≠ liste fermée"
    return [(p, sha(git("show", f"{CODE}:{p}"))) for p in changes], sha(texte)


# --- comptes -----------------------------------------------------------------------------------------------------------
def ligne_resultat(p: Path) -> str:
    lignes = [l.strip() for l in p.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    code = next((l for l in reversed(lignes) if re.fullmatch(r"code -?\d+", l)), None)
    if p.name.startswith("banc"):
        r = next((l for l in reversed(lignes) if "tuées" in l), "aucune ligne de synthèse")
    else:
        r = next((l for l in reversed(lignes) if re.search(r"\d+ (passed|failed)", l)), "aucune ligne de synthèse")
    return r + (f" ; {code}" if code else "")


def comptes() -> tuple[str, dict]:
    lignes, resume = [], {}
    dossiers = sorted(ICI.glob("essais-et-banc-sparks-v*")) + [ICI / "essais-et-banc-sparks-v9" / "commit-a655bbfa"]
    for d in dossiers:
        for f in sorted(d.glob("*.txt")):
            if f.name.startswith(("essais", "essai-", "banc")):
                lignes.append(f"| `{rel(f)}` | `{sha(f.read_bytes())}` | {ligne_resultat(f)} |")
    rep = []
    for d in sorted(ICI.glob("repetition-jouet-v*")):
        f = next((d / n for n in ("attendus.txt",) if (d / n).exists()), None) or next(iter(sorted(d.glob("sortie-repetition-*.txt"))), None)
        if f is None:
            f = d / "00-commit.txt"
            rep.append(f"| `{rel(d)}/` | `{sha(f.read_bytes())}` (`00-commit.txt`) | interrompue avant la création (redémarrage du conteneur) |")
            continue
        t = f.read_text(encoding="utf-8", errors="replace")
        ok = len(re.findall(r"^\s+OK\s", t, re.M))
        ec = len(re.findall(r"ÉCART", t))
        rep.append(f"| `{rel(f)}` | `{sha(f.read_bytes())}` | {ok} « OK », {ec} « ÉCART » |")
    final = ICI / "essais-et-banc-sparks-v9"
    for n in ("essais-tete-4d07d2a6.txt", "essais-enfant-2cc4bb27.txt", "banc-4d07d2a6.txt"):
        resume[n] = ligne_resultat(final / n)
    texte = (
        "au commit final `4d07d2a6` : essais (v1 à v4 et v9) à la tête, « " + resume["essais-tete-4d07d2a6.txt"] + " », et sur un "
        "commit enfant qui porte l'addendum factice (`COMMIT_CODE` posé), « " + resume["essais-enfant-2cc4bb27.txt"] + " » ; "
        "banc de mutations v9 (bancs v1 à v8 compris), « " + resume["banc-4d07d2a6.txt"] + " », 8 témoins verts. "
        "Tous les runs versés, par version (sortie brute, empreinte, ligne de résultat lue par script ; les runs joués pendant "
        "l'écriture, sur des fichiers non committés, sont comptés dans les additifs v2 à v9, section des comptes) :\n\n"
        "| Sortie | sha256 | Résultat |\n|---|---|---|\n" + "\n".join(lignes) + "\n\n"
        "Répétitions jouet des scripts d'instance (`MODE=jouet`), toutes comptées (R4 ; v4 à v8 jouées par la mère avec le "
        "dépôt distant, v9 jouées en local par le rédacteur-développeur, sans réseau ; causes des écarts : additifs v4 à v9) :\n\n"
        "| Sortie | sha256 | Attendus |\n|---|---|---|\n" + "\n".join(rep) + "\n\n"
        "Le banc à 49 sur 50 du commit `ee91412d` et le banc à 29 sur 30 du commit `96aae619` sont dans la première table ; "
        "leurs survivantes ont été tuées par des essais renforcés (additifs v2 et v4).")
    return texte, resume


# --- couples -------------------------------------------------------------------------------------------------------------
def couples(fichiers: list[tuple[str, str]], sha_liste: str, texte_comptes: str, sha_additif: str, heure: str) -> list[dict]:
    table = "\n".join(f"| `{p}` | `{h}` |" for p, h in fichiers)
    return [
        {"n": "B8-1", "ancien": "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 7\n",
         "nouveau": "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 8\n"},
        {"n": "B8-2", "ancien": "Brouillon 7 écrit après le 5 novembre 2026 à 04:06 UTC, toujours avant toute donnée.",
         "nouveau": f"Brouillon 7 écrit après le 5 novembre 2026 à 04:06 UTC, toujours avant toute donnée. Brouillon 8 écrit par "
                    f"script le 5 novembre 2026 à {heure} UTC (`date -u`), toujours avant toute donnée."},
        {"n": "B8-3", "ancien": "(`docs/notes/weight-space-programming-v1/contre-lecture-delta-v8-v1/contre-lecture-delta-v8-v1.md`, couples `couples-brouillon7-v1.json`, même dossier ; section 000000).\n",
         "nouveau": "(`docs/notes/weight-space-programming-v1/contre-lecture-delta-v8-v1/contre-lecture-delta-v8-v1.md`, couples `couples-brouillon7-v1.json`, même dossier ; section 000000).\n"
                    "- Brouillon 8 : brouillon 7 (`357370e7…`) + les couples B8-1 à B8-11 du même rédacteur-développeur, appliqués "
                    "par script (`docs/notes/weight-space-programming-v1/appliquer-couples-addendum-1-brouillon8-v1.py`, couples "
                    "`couples-brouillon8-v1.json` et sortie `sortie-appliquer-couples-addendum-1-brouillon8-v1.txt`, même dossier), "
                    "demandés par la mère le 5 novembre 2026 vers 06:22 UTC : compléments du code v9 et du tir ; clé d'instance "
                    "(R-1533) ; aucune contre-lecture neuve (R-1534) ; trois marqueurs de la section 2 remplis ; un marqueur neuf "
                    "pour le résultat du tir réel (section 0000000). **Aucun sous-agent neuf n'a relu ce brouillon** (R-1534).\n"},
        {"n": "B8-4", "ancien": "## 000000. Changements du brouillon 5 au brouillon 7 (avant → après ; raison ; source)\n",
         "nouveau": "## 0000000. Changements du brouillon 7 au brouillon 8 (avant → après ; raison ; source)\n\n"
                    "Brouillon 8 : couples B8-1 à B8-11 du rédacteur-développeur, appliqués dans l'ordre par script, chacun unique au "
                    "moment de son application ; aucune contre-lecture (R-1534, mot de Lazar : aller vite) : réserve.\n\n"
                    "| N° | Avant → après | Raison | Source |\n|---|---|---|---|\n"
                    "| B8-1 à B8-3 | titre, en-tête et journal au brouillon 7 → brouillon 8 | exactitude | consigne de la mère |\n"
                    "| B8-4 | — → cette section | journal des changements | idem |\n"
                    "| B8-5 | section 2 : compléments v6 à v8 → plus les compléments v9 (protocole du tir, boucle détectée par l'amorce, identifiants de démarrage) ; liste fermée v9 lue par la garde | exactitude (code v9) | « Contre-lecture 5 », point 31 et question 2 ; additif v9 |\n"
                    "| B8-6 | trois marqueurs de la section 2 → remplis par script (commit final, liste fermée et empreintes, comptes de tous les runs) | état avant scellement | consigne de la mère |\n"
                    "| B8-7 | aucun marqueur pour le tir → un marqueur neuf, à remplir par la mère : résultat du tir réel (verdict, identifiant, dépense) | le tir réel part avant le scellement, sous GO-2026-11-05-02 | consigne de la mère ; R-1534 |\n"
                    "| B8-8 | « Qui pose » : trois cas → plus (iv), boucle présumée au redémarrage sans ordre neuf ; noms gardés par les codes v5 à v9 | code v9 | additif v9, section 1 (b) |\n"
                    "| B8-9 | clé d'instance : nœud de Lazar avant toute création → risque accepté par Lazar et déclaré | mot de Lazar | R-1533 |\n"
                    "| B8-10 | épreuves : répétition complète sur la version citée → v9 : répétitions locales seulement, aucune complète au commit final ni avec le dépôt distant : réserve | aller vite (mot de Lazar) | R-1534 ; additif v9, section 4 |\n"
                    "| B8-11 | contre-lecture : « restent … la contre-lecture neuve de son delta » → aucune contre-lecture neuve du delta v9 ni du brouillon 8 ; R2 tenue par les contre-lectures 1 à 5 ; réserve ; pied : reste le résultat du tir | mot de Lazar | R-1534 |\n\n"
                    "## 000000. Changements du brouillon 5 au brouillon 7 (avant → après ; raison ; source)\n"},
        {"n": "B8-5", "ancien": "La liste fermée v8 (`src/controle_ia/sparks_exp7_nul_v8/liste-fermee-v1.txt`) compte les fichiers v2 à v8 ; la garde de lancement lit celle-ci. Fonction par fonction : additifs `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v6.md` (`2814152f…`), `-v7.md` (`1c69f72b…`) et `-v8.md` (`3752a2d5…`).\n",
         "nouveau": "La liste fermée v8 (`src/controle_ia/sparks_exp7_nul_v8/liste-fermee-v1.txt`) compte les fichiers v2 à v8 ; la garde de lancement lit celle-ci. Fonction par fonction : additifs `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v6.md` (`2814152f…`), `-v7.md` (`1c69f72b…`) et `-v8.md` (`3752a2d5…`).\n\n"
                    "**Compléments à la liste (contre-lecture du delta v5 → v8, « Contre-lecture 5 », points 5, 10 à 19 et 31 ; répétition locale v9).** "
                    "Code **v9** (`prep/sparks-exp7-nul-v9`, deux commits sur `4fd10407` : `a655bbfa`, puis `4d07d2a6`), fichiers neufs seulement : "
                    "(1) **mode « tir » du lanceur v9** : recherche d'offres écrite (`vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw`), "
                    "offres gardées si `resource_type` = « gpu » et `num_gpus` = 1, par prix croissant, au plus 4 ; **prix tirés de l'offre retenue par une règle écrite** "
                    "(`PRIX_CARTE` = `dph_total` ; `PRIX_STOCKAGE` = `storage_cost` × 20 Go ÷ 730 h) ; jeton passé à l'instance écrit dans la commande "
                    "(`GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN`, comme R1 v4) ; inventaire par `vastai show instances --raw`, lu en JSON strict et filtré par "
                    "identifiant entier (`{\"instances\": null}` ou identifiant absent de la liste = « absente » ; toute autre forme = « illisible » ; aucun motif « 404 ») ; "
                    "**verdict de boucle** sur au moins trois inventaires en au moins 5 minutes (« arretee » : trois « exited » avec `cur_state` « stopped » ; "
                    "« absente » ; « indecis » ; sinon « boucle » : destruction par l'identifiant avec `-y`, puis nœud de Lazar) ; lignes de l'amorce lues sans ancre "
                    "dans `vastai logs` (nombre de redémarrages) ; sorties brutes de `vastai` effacées après lecture, jamais versées ; « no_such_ask » sans identifiant "
                    "rendu : refus net, sans marqueur, offre suivante (au plus 4) ; `start` et `destroy` tenus pour envoyés sur « starting instance <ID>. » et "
                    "« destroying instance <ID>. » seulement ; ligne de GO du tir dont le périmètre nomme « SPARKS » et « tir » (`sparks_exp7_nul_v9/tir.py`) ; "
                    "(2) **amorce v9** : boucle de redémarrage détectée par l'amorce elle-même (section « Minuterie de destruction et redémarrages », (iv)) ; "
                    "ordre consigné « fait » et ordre « fin » traités avant la borne ; message exact de la fin causale (code et poussée) ; identifiants de démarrage "
                    "jamais réutilisés (`nouvel_id` : deux démarrages dans la même seconde écrasaient un plafond au registre, trouvé par la répétition locale) ; "
                    "(3) 34 mutations neuves. La liste fermée v9 (`src/controle_ia/sparks_exp7_nul_v9/liste-fermee-v1.txt`) compte les fichiers v2 à v9 ; la garde "
                    f"de lancement (amorce v9) lit celle-ci. Fonction par fonction : additif `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v9.md` (`{sha_additif}`). "
                    "**Code v9 non contre-lu** (R-1534) : section « Contre-lecture ».\n"},
        {"n": "B8-6a", "ancien": "descendant de `55399606`) : À REMPLIR.",
         "nouveau": f"descendant de `55399606`) : `{CODE}` (branche `prep/sparks-exp7-nul-v9`, poussée par la mère ; version de code citée dans ce texte : "
                    "v9, amorce `scripts/amorce_instance_sparks_exp7_nul_v9.sh`, lanceur v9). **Dernière version, non contre-lue** (R-1534, mot de Lazar) : "
                    "la dernière version contre-lue est la v8 (`4fd10407`, « Contre-lecture 5 »)."},
        {"n": "B8-6b", "ancien": "contrôlé par script au scellement) : À REMPLIR.",
         "nouveau": f"contrôlé par script au scellement) : **{len(fichiers)} fichiers**, tous ajoutés (`git diff --name-status --no-renames 55399606..4d07d2a6` : "
                    f"{len(fichiers)} « A », aucun autre statut), égaux, à l'égalité exacte, au fichier de la liste au commit du code "
                    f"(`{LISTE}`, sha256 `{sha_liste}`), contrôle fait par `docs/notes/weight-space-programming-v1/appliquer-couples-addendum-1-brouillon8-v1.py` ; "
                    "empreintes lues au commit `4d07d2a6` (`git show`) :\n\n| Fichier | sha256 |\n|---|---|\n" + table + "\n"},
        {"n": "B8-6c", "ancien": "et le banc à 49 sur 50 du commit `ee91412d`) : À REMPLIR.",
         "nouveau": "et le banc à 49 sur 50 du commit `ee91412d`) : " + texte_comptes + "\n"},
        {"n": "B8-7", "ancien": "**Puissance de M5** : section « Seuil » ci-dessous.",
         "nouveau": "**Résultat du tir réel** (GO-2026-11-05-02 ; code v9 `4d07d2a6` ; mode « tir » du lanceur v9 : verdict de boucle « arretee », "
                    "« boucle » ou « absente », compte `REDEMARRAGES=` du journal, identifiant de l'instance, destruction constatée par l'inventaire, "
                    "dépense relevée ; rapport du tir avec son empreinte) : " + MARQUE + ".\n\n**Puissance de M5** : section « Seuil » ci-dessous."},
        {"n": "B8-8a", "ancien": "(iii) à tout démarrage à partir de l'échéance (aucun calcul).",
         "nouveau": "(iii) à tout démarrage à partir de l'échéance (aucun calcul) ; (iv) **code v9** : à tout redémarrage sans ordre neuf lisible et accepté "
                    "(branche des ordres absente ou illisible, ordre déjà fait ou refusé, ordre mal lu, consignation impossible) et à tout refus qui précède "
                    "l'ordre (identifiant, commit du disque, GO à la date) : **boucle de redémarrage présumée, destruction immédiate**, sans attendre "
                    "l'échéance ; de même pour une création relancée sur un disque où elle a déjà été tentée sans dépôt extrait. Chaque redémarrage est "
                    "consigné au registre des démarrages avant tout le reste (plafond de 5 minutes, puis durée réelle) et compte à la borne de la machine ; "
                    "l'ordre est consigné « fait » avant la borne, si bien qu'un refus après lui ne se rejoue pas. Prix déclaré : un ordre manquant par "
                    "incident de réseau au redémarrage détruit l'instance et ses modèles (la dépense est protégée plutôt que les modèles)."},
        {"n": "B8-8b", "ancien": "(`sparks-v5-detruire` pour les amorces v5 à v8, qui gardent les noms de la v5)",
         "nouveau": "(`sparks-v5-detruire` pour les amorces v5 à v9, qui gardent les noms de la v5)"},
        {"n": "B8-8c", "ancien": "(nom gardé par les codes v5 à v8 ;", "nouveau": "(nom gardé par les codes v5 à v9 ;"},
        {"n": "B8-9a", "ancien": "- **Clé d'instance (R-1527 ; nœud de Lazar, compte).**",
         "nouveau": "- **Clé d'instance (R-1527 ; risque accepté par Lazar et déclaré, R-1533).**"},
        {"n": "B8-9b", "ancien": "Risque déclaré ; aucune création sous ce texte avant la réponse de Lazar à ce nœud.",
         "nouveau": "Risque **accepté par Lazar et déclaré** (R-1533, mot de Lazar, 5 novembre 2026) : la création n'attend plus ce nœud ; "
                    "le risque reste ouvert pour toute la durée de vie de chaque instance."},
        {"n": "B8-10", "ancien": "chaque démarrage dans son propre espace de processus (`unshare -pf`).",
         "nouveau": "chaque démarrage dans son propre espace de processus (`unshare -pf`). **Code v9** (R-1534, mot de Lazar : aller vite) : répétitions "
                    "jouées en local seulement (dépôt nu local qui emprunte les objets du dépôt de travail, `unshare -pf`, sans réseau ; "
                    "`docs/notes/weight-space-programming-v1/repetition-jouet-v9-locale-v1/` à `-v4/`) : run 3 complet au commit `a655bbfa`, tous les "
                    "attendus « OK » (fabrication, copie, phase causale, relance sans ordre neuf détruite, un seul `DELETE`) ; run 4 au commit final "
                    "`4d07d2a6` interrompu par un redémarrage du conteneur avant la création, non rejoué ; **aucune répétition complète au commit final, "
                    "aucune avec le dépôt distant** : réserve ; la différence `a655bbfa..4d07d2a6` se limite à `nouvel_id`, éprouvé par essais et banc."},
        {"n": "B8-11a", "ancien": "; restent le tir réel, le code v9 et la contre-lecture neuve de son delta (`git diff 4fd10407..<commit>`).",
         "nouveau": ". Code v9 fait (`4d07d2a6`, additif v9). **Aucune contre-lecture neuve n'a relu le delta v9 (`git diff 4fd10407..4d07d2a6`) ni "
                    "le brouillon 8** : mot de Lazar, R-1534 (aller vite). R2 est tenue par les contre-lectures 1 à 5 ci-dessus, qui ont relu le texte "
                    "jusqu'au brouillon 6 et le code jusqu'à `4fd10407` ; le code v9 et les couples du brouillon 8 ne sont relus par personne : **réserve**. "
                    "Reste le résultat du tir réel (section 2)."},
        {"n": "B8-11b", "ancien": "Brouillon 7 (5 novembre 2026, couples de la contre-lecture du delta v5 → v8), sur le brouillon 6",
         "nouveau": "Brouillon 8 (5 novembre 2026, couples du même rédacteur-développeur, appliqués par script, sans contre-lecture : R-1534), sur le "
                    "brouillon 7 (5 novembre 2026, couples de la contre-lecture du delta v5 → v8), sur le brouillon 6"},
        {"n": "B8-11c", "ancien": "Reste avant scellement : le tir réel et son rapport ; le code v9 et la contre-lecture neuve de son delta ; les trois éléments de la section 2 (commit final, liste fermée et empreintes, comptes rejoués).",
         "nouveau": "Reste avant scellement : le résultat du tir réel et son rapport (section 2, marqueur rempli par la mère). Les trois éléments de la "
                    "section 2 (commit final, liste fermée et empreintes, comptes rejoués) sont remplis par script au brouillon 8."},
    ]


def main() -> int:
    heure = datetime.now(timezone.utc).strftime("%H:%M")
    t7 = B7.read_bytes()
    assert sha(t7) == SHA_B7, "brouillon 7 altéré"
    assert not B8.exists(), f"{B8} existe déjà (R12)"
    fichiers, sha_liste = liste_fermee()
    texte_comptes, resume = comptes()
    c = couples(fichiers, sha_liste, texte_comptes, sha(ADDITIF_V9.read_bytes()), heure)
    assert not COUPLES.exists(), f"{COUPLES} existe déjà (R12)"
    COUPLES.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    t = t7.decode("utf-8")
    assert t.count(MARQUE) == 3
    for k in c:
        n = t.count(k["ancien"])
        assert n == 1, f"{k['n']} : « ancien » trouvé {n} fois"
        t = t.replace(k["ancien"], k["nouveau"])
        print(f"{k['n']} appliqué (ancien unique)")
    assert t.count(MARQUE) == 1, t.count(MARQUE)
    B8.write_text(t, encoding="utf-8")
    p = problemes(B8)
    with tempfile.TemporaryDirectory() as d:
        s = Path(d) / "b8-rempli.md"
        s.write_text(t.replace(MARQUE, "rempli pour simulation"), encoding="utf-8")
        p_rempli = problemes(s)
    print(f"brouillon 7 : {rel(B7)} {SHA_B7}")
    print(f"couples : {rel(COUPLES)} {sha(COUPLES.read_bytes())} ({len(c)} couples)")
    print(f"brouillon 8 : {rel(B8)} {sha(B8.read_bytes())} (écrit à {heure} UTC)")
    print(f"liste fermée : {len(fichiers)} fichiers, égale au fichier {LISTE} au commit {CODE} (sha256 {sha_liste})")
    print(f"comptes au commit final : {json.dumps(resume, ensure_ascii=False)}")
    print(f"marqueurs « {MARQUE} » restants : {t.count(MARQUE)} (résultat du tir réel)")
    print(f"prereg.problemes(brouillon 8) : {p}")
    print(f"prereg.problemes(brouillon 8, marqueur rempli pour simulation) : {p_rempli}")
    assert p == ["marqueur À REMPLIR restant hors des sections exigées"], p
    assert p_rempli == [], p_rempli
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
