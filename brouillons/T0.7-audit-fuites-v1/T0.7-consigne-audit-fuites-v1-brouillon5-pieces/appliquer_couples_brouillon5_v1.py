#!/usr/bin/env python3
"""Brouillon 5 de la consigne de l'audit des fuites de T0.7 : couples appliqués au brouillon 4 (v1).

Écrit le 2026-11-11 à partir de 13:47 UTC (heure relevée par `date -u`) par l'agent du brouillon 4 (Claude Opus 5.5),
sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sous la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-audit-fuites-t07-brouillon4-v1.md`
(`df38829a…`) et les décisions de la mère sur Q-B4-1 à Q-B4-5 (R-2348).

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python <ce script> essais
    PYTHONPATH=src .venv/bin/python <ce script> appliquer
    PYTHONPATH=src .venv/bin/python <ce script> appliquer --a-blanc <dossier>

Réutilise, après contrôle de son empreinte, les fonctions du script scellé du brouillon 4 (`appliquer`, `defaire`,
`verifier_decoupeur`, `git_show`, `ecrire_sans_ecraser`, et ses 19 essais sur jouets). Git : `git show <commit>:<chemin>`
seulement. Chaque « ancien » présent une fois au moment de son remplacement ; défaire les couples, du dernier au premier,
doit redonner le brouillon 4 à l'octet, sinon rien n'est écrit ; aucun fichier différent n'est écrasé (R12).
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

DOSSIER = "brouillons/T0.7-audit-fuites-v1"
B4 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon4.md"
SCRIPT_B4 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon4-pieces/appliquer_couples_brouillon4_v1.py"
B5 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon5.md"
PIECES = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon5-pieces"
FICHIER_COUPLES = f"{PIECES}/couples-brouillon4-vers-brouillon5-v1.json"
JOURNAL_B5 = f"{PIECES}/journal-brouillon5-v1.md"
SCRIPT = f"{PIECES}/appliquer_couples_brouillon5_v1.py"
RECEPTION = "docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/etape-E-reception-r1-v4-v1.md"
DECISIONS = "registres/decisions.md"

ATTENDUS = {
    B4: "f9f4bd380a3066371c88d39ede0ef60bde77070311cd2cd9ca221cf8f3f194c5",
    SCRIPT_B4: "7539b4779e9def222791fafa5165915e00ab85a7bca12693c85101ccd41dd037",
    RECEPTION: "bb6652f2cdd914f2ba0b3cd70c8af37ee6dd40fb0da0db8e289133ed6f5e79e1",
}
COMMIT_DEC = "c7484c43657a2ce22d76af33efd06aaa11a6aafa"
DOSSIER_DEC = "donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1"
EMPREINTES_DEC = {  # R-2238
    "tokenizer.json": "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4",
    "tokenizer_config.json": "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424",
    "special_tokens_map.json": "6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec",
}
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")


class Arret(Exception):
    pass


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire(chemin: str) -> bytes:
    octets = Path(chemin).read_bytes()
    h = sha(octets)
    if h != ATTENDUS[chemin]:
        raise Arret(f"empreinte de {chemin} : {h} ≠ {ATTENDUS[chemin]}")
    hc = Path(chemin + ".sha256").read_text(encoding="utf-8").split()[0]
    if hc != h:
        raise Arret(f"compagnon de {chemin} : {hc} ≠ {h}")
    return octets


def module_b4():
    lire(SCRIPT_B4)
    spec = importlib.util.spec_from_file_location("couples_b4", SCRIPT_B4)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def texte_decoupeur(dec: dict[str, str]) -> str:
    emp = " ; ".join(f"`{n}`\n`{h}`" for n, h in dec.items())
    return (
        "la mère donne au lancement\n"
        f"le **commit** `{COMMIT_DEC}` et le **dossier**\n"
        f"`{DOSSIER_DEC}/` (branche de données privée\n"
        f"`{DOSSIER_DEC}`, orpheline, jamais fusionnée dans `main` ; R-2238 ; commit\n"
        "présent dans le clone local, R-2348) — les fichiers du découpeur de `config.agent` à la révision citée\n"
        "(`tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`) et le sha256 de chacun : "
        + emp
        + "\n(R-2238 ; égaux à la réception R1 v4, "
        f"`{RECEPTION}` l. 70-72,\n`{ATTENDUS[RECEPTION][:8]}…` ; recalculés par `git show` au brouillon 5 et égaux aux "
        "compagnons du commit). L'auditeur\n"
        "écrit chacun des trois fichiers dans un dossier neuf de son bac à sable (hors du dépôt, comme `TMPDIR`, § 7) par\n"
        f"`git show {COMMIT_DEC}:{DOSSIER_DEC}/<fichier> > <dossier>/<fichier>`\n"
        "(règle 4 des interdits, annexe A : lecture par `git show <commit>:<chemin>` seulement ; ni `git archive`, ni `fetch` ;\n"
        "R-2348) ; il vérifie les trois empreintes **avant** de charger le découpeur, puis le charge par\n"
        "`transformers.AutoTokenizer.from_pretrained(<dossier>, local_files_only=True)`"
    )


def couples(dec: dict[str, str]) -> list[dict]:
    C: list[dict] = []

    def ajoute(ident, motif, anc, nou):
        C.append({"id": ident, "motif": motif, "ancien": anc, "nouveau": nou})

    ajoute("D00", "statut : titre du brouillon 5",
           "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 4\n",
           "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 5\n")
    ajoute("D01", "statut du brouillon 5 en tête (qui, quand, d'où) ; l'ancien statut devient « Brouillon 4 (historique) »",
           "- **Statut** : **brouillon 4**, non scellé sous son nom définitif, écrit le 2026-11-11 à partir de 13:28 UTC (heure "
           "relevée\n",
           "- **Statut** : **brouillon 5**, non scellé sous son nom définitif, écrit le 2026-11-11 à partir de 13:47 UTC (heure "
           "relevée\n"
           "  par `date -u`) par l'agent du brouillon 4 (Claude Opus 5.5, `claude-opus-5-5`, sous-agent de la session mère\n"
           "  `session_01VJdZpSMxSdk2SJ1ScmdfNv`), sous la même consigne (`df38829a…`, R-2346) et les décisions de la mère sur\n"
           "  les questions du brouillon 4 (Q-B4-1 à Q-B4-5, R-2348). Auteur des brouillons 4 et 5, cet agent est exclu de la\n"
           "  contre-lecture des écarts (§ 14.2). **Brouillon 5 = brouillon 4**\n"
           f"  (`{B4}`,\n"
           f"  `{ATTENDUS[B4]}`, scellé, gardé intact) **+ les couples « ancien → nouveau »** du fichier\n"
           f"  `{FICHIER_COUPLES}`,\n"
           "  appliqués chacun une fois par le script `appliquer_couples_brouillon5_v1.py` du même dossier ; défaire les "
           "couples\n"
           "  redonne le brouillon 4 à l'octet (vérifié par le script). Sources, contrôles et questions au journal\n"
           f"  `{JOURNAL_B5}`.\n"
           "- **Brouillon 4** (historique) : écrit le 2026-11-11 à partir de 13:28 UTC (heure relevée\n")
    ajoute("D02", "état des marqueurs : `CHEMIN_DECOUPEUR` rempli",
           "; **restent à remplir\n  avant le scellement** : `CHEMIN_DECOUPEUR` (§ 6.1 ; le commit du découpeur n'est pas dans "
           "le clone local, couple\n  prêt au fichier des couples, journal du brouillon 4, § 5) et `RAPPORT_CONTRE_LECTURE_2` "
           "(§ 14.2, contre-lecture des\n  écarts commandée par la mère).",
           "; `CHEMIN_DECOUPEUR`\n  (§ 6.1) **rempli au brouillon 5** (commit amené dans le clone local par la mère, "
           "R-2348 ; trois empreintes\n  recalculées par `git show`) ; **reste à remplir avant le scellement** : "
           "`RAPPORT_CONTRE_LECTURE_2` (§ 14.2,\n  contre-lecture des écarts commandée par la mère).")
    ajoute("D03", "ordre des opérations",
           "  puis remplissage de `CHEMIN_DECOUPEUR`, contre-lecture des écarts (§ 14.2) et scellement de cette consigne.",
           "  puis remplissage de `CHEMIN_DECOUPEUR` (brouillon 5), puis contre-lecture des écarts (§ 14.2), puis scellement "
           "de\n  cette consigne.")
    ajoute("D04", "Q-B4-5 : calendrier visé du § 4 (R-2348)",
           "- **Calendrier visé** (R-2177 ; contre-lecture 1, Q10) : brouillon 22 de T0.7, puis cette consigne remplie et "
           "scellée,\n  le 12 novembre au soir, au plus tard le 13 ; audit dès la poussée vérifiée des sorties de 7b ; ligne "
           "`AUDIT-FUITES-T07`\n  avant l'étape B. Durée au § 13.",
           "- **Calendrier visé** (R-2177 ; contre-lecture 1, Q10 ; mis à jour au brouillon 5, R-2348) : T0.7 scellé le "
           "2026-11-11\n  (R-2321) ; cette consigne remplie, contre-lue (§ 14.2) et scellée **avant l'audit** ; l'audit "
           "relève de l'étape B de\n  T0.7 (ligne `AUDIT-FUITES-T07` exigée à l'étape B) : il se fait après la poussée "
           "vérifiée des sorties de la course\n  7b et avant l'exécution de l'étape B (fenêtre ci-dessus). Aucune autre date "
           "n'est fixée ici. Durée au § 13.")
    ajoute("D05", "Q-B4-1 : `CHEMIN_DECOUPEUR` rempli ; fichiers écrits par `git show`, empreintes vérifiées avant chargement "
           "(R-2238, R-2348)",
           "la mère donne au lancement\n`<<CHEMIN_DECOUPEUR>>` — le chemin exact du dossier des fichiers du découpeur de "
           "`config.agent` à la révision citée\n(`tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`), et le "
           "sha256 de chacun ; l'auditeur vérifie ces\nempreintes, charge le découpeur par "
           "`transformers.AutoTokenizer.from_pretrained(<chemin>, local_files_only=True)`",
           texte_decoupeur(dec))
    ajoute("D06", "Q-B4-2 : objet du § 14.2 étendu au différentiel du brouillon 2 au brouillon 5 (R-2348)",
           "objet : le **différentiel du brouillon 3 au brouillon 4** (couples du fichier des couples, rejoués : défaire les\n"
           "couples redonne le brouillon 3 à l'octet)",
           "objet : le **différentiel du brouillon 2 au brouillon 5** (du brouillon 2 au brouillon 3 : corrections de la\n"
           "contre-lecture 1 et décisions de la mère, § 0 et § 14.1, journal du brouillon 3 ; du brouillon 3 au brouillon 4, "
           "puis\ndu brouillon 4 au brouillon 5 : couples des deux fichiers de couples, rejoués, défaire chaque série redonnant "
           "le\nbrouillon précédent à l'octet ; R-2348)")
    ajoute("D07", "§ 14.2 : contrôle du remplissage de `CHEMIN_DECOUPEUR`",
           "`CHEMIN_DECOUPEUR` (commit, dossier et trois empreintes contre R-2238 et les compagnons du commit)",
           "`CHEMIN_DECOUPEUR` (commit, dossier, écriture des fichiers par `git show`, trois empreintes contre R-2238 et les\n"
           "compagnons du commit)")
    ajoute("D08", "§ 14.2 : fichiers à donner (brouillons 2 à 5)",
           "fichiers à lui donner : ce brouillon,\nses pièces (fichier des couples, script, sortie du script, journal du "
           "brouillon 4), le brouillon 3 et son journal, la\ncontre-lecture 1,",
           "fichiers à lui donner : ce brouillon\net ses pièces (fichier des couples, script, sortie du script, journal du "
           "brouillon 5), le brouillon 4 et ses pièces\n(mêmes noms, journal du brouillon 4), le brouillon 3 et son journal, le "
           "brouillon 2 et son journal, la contre-lecture 1,")
    return C


def essais_b5(m) -> list[str]:
    sortie = list(m.essais())  # 19 essais du brouillon 4 (arrêt si l'un échoue)
    # Essai propre au brouillon 5 : le texte rempli ne porte aucun marqueur et cite les trois empreintes données.
    jouet = {"a.json": "0" * 64, "b.json": "1" * 64}
    t = texte_decoupeur(jouet)
    ok = not MARQUEUR.findall(t) and all(f"`{h}`" in t for h in jouet.values()) and "git archive" not in t.replace(
        "ni `git archive`", "")
    sortie.append(f"essai B5-1 texte du découpeur (sans marqueur, empreintes citées, aucun `git archive` prescrit) : "
                  f"{'sain, conforme' if ok else 'ÉCHEC'}")
    if not ok:
        raise Arret("essai B5-1 en échec")
    return sortie


def principal(argv: list[str]) -> int:
    a_blanc = None
    if len(argv) == 3 and argv[0] == "appliquer" and argv[1] == "--a-blanc":
        a_blanc, argv = Path(argv[2]), argv[:1]
    if argv not in (["essais"], ["appliquer"]):
        print(__doc__)
        return 2
    if not (Path(SCRIPT).is_file() and Path(B4).is_file()):
        print("ARRÊT : à lancer depuis la racine du dépôt")
        return 1
    try:
        m = module_b4()
        print(f"script du brouillon 4 : {SCRIPT_B4} — sha256 {ATTENDUS[SCRIPT_B4]} (égal à l'attendu et au compagnon)")
        for l in essais_b5(m):
            print(l)
        if argv == ["essais"]:
            return 0
        b4 = lire(B4)
        print(f"entrée {B4} : sha256 {ATTENDUS[B4]} (égale à l'attendu et au compagnon)")
        rec = lire(RECEPTION).decode("utf-8")
        r2238 = [l for l in Path(DECISIONS).read_text(encoding="utf-8").split("\n") if l.startswith("| R-2238 |")]
        if len(r2238) != 1 or COMMIT_DEC not in r2238[0] or DOSSIER_DEC not in r2238[0]:
            raise Arret("R-2238 : ligne, commit ou dossier introuvable")
        for n, h in EMPREINTES_DEC.items():
            if h not in r2238[0] or f"`{h}`" not in rec:
                raise Arret(f"empreinte de {n} absente de R-2238 ou de la réception R1 v4")
        print("R-2238 : commit, dossier et trois empreintes présents ; réception R1 v4 : trois empreintes présentes")
        try:
            dec = m.verifier_decoupeur(m.git_show, COMMIT_DEC, DOSSIER_DEC, EMPREINTES_DEC)
        except m.Arret as e:
            raise Arret(f"découpeur non vérifié : {e}")
        for n, h in dec.items():
            print(f"découpeur {n} : sha256 recalculé par `git show {COMMIT_DEC}:{DOSSIER_DEC}/{n}` = {h} ; "
                  "= R-2238 ; = compagnon du commit")
        C = couples(dec)
        t4 = b4.decode("utf-8")
        try:
            t5 = m.appliquer(t4, [(c["ancien"], c["nouveau"]) for c in C])
            retour = m.defaire(t5, [(c["ancien"], c["nouveau"]) for c in C])
        except m.Arret as e:
            raise Arret(str(e))
        if retour.encode("utf-8") != b4:
            raise Arret("défaire les couples ne redonne pas le brouillon 4 à l'octet")
        print(f"couples : {len(C)} appliqués, chacun une fois ; défaits du dernier au premier : brouillon 4 à l'octet")
        restants = sorted(set(MARQUEUR.findall(t5)))
        for mq in restants:
            print(f"marqueur restant : {mq} ({t5.count(mq)} fois)")
        if restants != ["<<RAPPORT_CONTRE_LECTURE_2>>"] or t5.count("<<RAPPORT_CONTRE_LECTURE_2>>") != 1:
            raise Arret(f"marqueurs restants inattendus : {restants}")
        o_couples = (json.dumps({
            "de": {"chemin": B4, "sha256": ATTENDUS[B4]},
            "vers": {"chemin": B5, "sha256": sha(t5.encode("utf-8"))},
            "regle": "appliqués dans l'ordre, chaque « ancien » présent une fois au moment de son remplacement ; défaits du "
                     "dernier au premier (« nouveau » → « ancien », chaque « nouveau » présent une fois), ils redonnent le "
                     "brouillon 4 à l'octet",
            "decoupeur": {"commit": COMMIT_DEC, "dossier": DOSSIER_DEC, "empreintes_recalculees": dec},
            "couples": C,
        }, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        c5, cc = B5, FICHIER_COUPLES
        if a_blanc is not None:
            print(f"À BLANC : sorties écrites sous {a_blanc}, aucune sous {DOSSIER}")
            c5, cc = str(a_blanc / Path(B5).name), str(a_blanc / Path(FICHIER_COUPLES).name)
        print(f"brouillon 5 : {c5} — {m.ecrire_sans_ecraser(c5, t5.encode('utf-8'))} — sha256 {sha(t5.encode('utf-8'))}")
        print(f"couples : {cc} — {m.ecrire_sans_ecraser(cc, o_couples)} — sha256 {sha(o_couples)}")
        return 0
    except Exception as e:  # Arret de ce script ou du script du brouillon 4
        if type(e).__name__ != "Arret":
            raise
        print(f"ARRÊT : {e}")
        return 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
