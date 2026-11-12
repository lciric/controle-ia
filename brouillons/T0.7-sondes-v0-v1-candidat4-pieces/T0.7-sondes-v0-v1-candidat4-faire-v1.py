"""T0.7 sondes v0, candidat 4 : application des couples du candidat 4 au candidat 3 (couples VC3-A et VC3-B de la vérification
courte, tels qu'écrits ; code final au commit `a621dcd3` ; script v4 ; CLC-P3-01 et CLC-P3-04 ; réserves de R-2313 ; ordre
brouillon 8) et vérifications, dont « défaire les couples redonne le candidat 3 à l'octet » (v1).

Rédacteur des candidats 2, 3 et 4 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 11 novembre
2026, sur le message de la mère qui suit R-2313 (mêmes interdits et chemins que la consigne `d29c7858…`, aux noms près). Méthode du
script du candidat 3 (`brouillons/T0.7-sondes-v0-v1-candidat3-pieces/T0.7-sondes-v0-v1-candidat3-faire-v1.py`, `b8e3b87a…`).
Bibliothèque standard, `controle_ia.prereg` du dépôt (RACINE/src) et `git` en lecture (`git show <commit>:<chemin>`, `git ls-tree`) ;
`src/` au commit `a621dcd3` est recopié par `git show` dans le dossier temporaire pour rejouer `lecture_v4 empreinte-config` ;
aucun réseau ; aucune écriture hors du candidat 4 et du dossier temporaire.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie les empreintes de ses entrées (candidat 3, couples, ordres brouillons 7 et 8, vérification courte du candidat 3,
   configurations v7 et v8, rapport du code v3, contre-lecture courte des corrections, résumé de la répétition jouet v4,
   `CODE-T07-v1.json`) ;
2. code au commit `a621dcd3` : `lecture_v4 empreinte-config` rend `0f32c6de…` pour la v8 et refuse la v7 ; `TOLERANCES` et
   `RESERVE_CARTE` inchangés ; formes du motif d'un bras arrêté (`<type> : …` ; `réextraction impossible : <type> : …`) et
   `FAUTES_DU_BRAS` tels que G4-03 les décrit ; sous-commande `controle-avant-ouverture` présente ; script v4 à son empreinte et
   qui la joue ; répétition jouet v4 conforme, dix verdicts vrais ;
3. applique les couples ; chaque « ancien » présent exactement une fois et différent de son « nouveau » ; un couple touche l'empan
   gelé si et seulement si son champ `gelee` le déclare, dans la section déclarée ; sinon arrêt (code 1), rien n'est écrit ;
   G4-01 et G4-02 égaux, ancien et nouveau, aux couples VC3-A et VC3-B du § 4 de la vérification courte ;
4. écrit `brouillons/T0.7-sondes-v0-v1-candidat4.md` (R12) ;
5. vérifie : (1) titre et premier statut ; (2) **défaire tous les couples dans l'ordre inverse redonne le candidat 3 octet pour
   octet** ; chaque section gelée, ses couples défaits, égale celle du candidat 3 ; couples gelés = G4-01 (Liste d'arrêt), G4-02
   (Seuil), G4-03 (Liste d'arrêt) ; (3) sections neuves (une) et disparues (aucune) ; (4) un seul marqueur restant, une
   occurrence ; (5) `problemes` réduit à sa ligne, vide à valeur factice ; (6) vingt-six modules au commit `a621dcd3`, huit neufs
   et dix-huit anciens à leur empreinte et cités ; (7) ordre brouillon 8 cité par chemin et empreinte, son marqueur `ATT_C7_T07`
   présent, le script v4 à sa ligne (A), P14, VC3-C et VC3-D tels qu'écrits ; (8) phrases exigées présentes, passages retirés
   absents ; (9) différentiel compté ; mentions « en cours » restantes imprimées.
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

COMMIT = "a621dcd3b929ce3ebd615fa852d4a7f5c103071d"
C3 = "brouillons/T0.7-sondes-v0-v1-candidat3.md"
C4 = "brouillons/T0.7-sondes-v0-v1-candidat4.md"
P = "brouillons/T0.7-sondes-v0-v1-candidat4-pieces/"
COUPLES = P + "T0.7-sondes-v0-v1-candidat4-couples-v1.json"
ORDRE7 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md"
ORDRE8 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md"
VC = "prereg/contre-lectures/T0.7-sondes-v0-v1-candidat3-verification-courte-v1.md"
PIECES = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/"
V7, V8 = PIECES + "configuration-t07-v7.json", PIECES + "configuration-t07-v8.json"
RAP3 = PIECES + "rapport-code-plancher-v3-v3.md"
CLC = PIECES + "contre-lecture-courte-corrections-plancher-v3-v1.md"
REP_R = PIECES + "repetition-jouet-v4-resume.json"
CODE_V1 = "registres/code-t07/CODE-T07-v1.json"
SHA_ENTREES = {
    C3: "1b9b75f0611aab05b9edf61acb49d72f3d606af25024100bda1f0fe75adda4a6",
    COUPLES: "0c74d25a87f253372bb5880a36bbe2413c0896d7ffac57cb8b3fcbeef8143c24",
    ORDRE7: "d799a01bd6008d73794a42dd8b4657c4498ca291bcbd64b771711cf6632a5916",
    ORDRE8: "24dc8df6555bac03f2ffbe8440c3c1a7b9bf2aeaf9eab3c651306a6a73fc116e",
    VC: "cfeeae9c0a3425002f75be94abd9fa32de5e7bd8f7c810d2df4d10410e47aa06",
    V7: "3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab",
    V8: "e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328",
    RAP3: "be2c86e215a1a7a0e41f646e60acaa20a39f0b626c6cd1b0807066348305b159",
    CLC: "6f3769116d2432be4f5b201774307bdfcdbf25cc5b8cb664c61740b8ce0aabf7",
    REP_R: "c36839fe2016ccea200ee5fa28c7a7116f457821d576ee93b88fbfb4d4b4f2e2",
    CODE_V1: "9ef4ede751fcceb51eda1e622deaa62552326e395fdbd647c6989ad32353701f",
}
CANON_V8 = "0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12"
SCRIPT4 = "4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6"
TITRE = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — candidat 4"
MARQ = "<<C7_ET_CODE_T07_26_MODULES>>"
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
GELES_MANDAT = {"G4-01": "Liste d'arrêt", "G4-02": "Seuil", "G4-03": "Liste d'arrêt"}
EGAUX_VC = {"G4-01": "VC3-A", "G4-02": "VC3-B"}
NEUVES = ["Table « ce qui change du candidat 3 au candidat 4 »"]
NEUFS = {"plancher_v2.py": "a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796",
         "lecture_v3.py": "ac3666e4003b55629600c4d21db9e9b35086c37325c4f63e6417bca1864c921a",
         "lectures_t07_v2.py": "1f523c07273ae11359ca199056eadbf68cf1448c93e9c43eb2bf4a8a600b5271",
         "plancher_v3.py": "c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8",
         "reextraction_p3_v1.py": "c32696b82af620e5da07fc4ec5bbb801dc385467cbf8235b799ad28b6471eaf9",
         "lecture_v4.py": "42f60780e6944568e81880887a1ad87c57a520e8c7d54083b36a43c097a06d06",
         "passe_blanc_v2.py": "8e24642fd49c2d57d7f3093f4989a06a5d9110145f7d5574e5b000e48f82dba5",
         "repli_etapes_v2.py": "fe08aaa14de1ca0ac88292f2c7a10ec8d591fee1e83f90c9ae38b32d0c6a2f50"}
PHRASES = (
    "- Statut : **candidat 4**", "**Changements dans l'empan gelé : trois**", "## Table « ce qui change du candidat 3 au candidat 4 »",
    f"`{ORDRE8}`, sha256 `{SHA_ENTREES[ORDRE8]}`", f"`{SCRIPT4}`", f"**`{COMMIT}`**",
    "**`lecture_v4 controle-avant-ouverture RACINE CONFIG [--cache-dir D]`**", "**motif ne commence pas par `GardeArret`**",
    "**arrêt technique**", "**retour à Lazar (nœud, R4) avant toute lecture**", "**à 400 exemples**", "**1 591**", "**1,3 fois**",
    "**0,5 %**", "**palier « carte », avec sa réserve**", "**1 %**", "**10 verdicts sur 10**", "**bash antérieur à 4.4 non éprouvé**",
    "**tronqué non vide**", "**la mère la rejoue entière à C7**", "1 undecies. **Candidat 4",
    "**Candidat 4** : **à contre-lire par une vérification courte neuve**", "**Vérification courte du candidat 3 rendue**",
    "n'est couvert par aucune contre-lecture rendue à ce jour", "N si une autre est au-dessus",
    "c'est la règle dont le niveau n'est pas tenu sous un plancher à signal commun",
)
ABSENTES = ("- Statut : **candidat 3**", "(la plus petite à 4,3 fois le plafond)", "contre-lecture courte différentielle en cours)",
            "(en cours, R-2304)", "(en cours, R-2309)", "contre-lecture courte en cours)",
            "(U si une autre sonde lue est au-dessus et interprétable ; E si toutes")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def plat(s: str) -> str:
    return " ".join(s.split())


def sections(texte: str) -> dict:
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {titre.strip(): corps for titre, corps in zip(morceaux[1::2], morceaux[2::2])}


def section_de(texte: str, debut: int, fin: int) -> set:
    noms, courant = set(), "(avant la première section)"
    for m in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M):
        if m.start() <= debut:
            courant = m.group(1)
        elif m.start() < fin:
            noms.add(m.group(1))
    noms.add(courant)
    return noms


def gelee(nom: str) -> bool:
    return any(nom.startswith(g) for g in EMPAN_GELE)


def lignes_diff(a: str, b: str) -> list:
    return [l for l in difflib.unified_diff(a.split("\n"), b.split("\n"), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]


def git(racine: Path, *args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "--no-optional-locks", "-C", str(racine), *args], capture_output=True)


def main(argv: list) -> int:
    if not 1 <= len(argv) <= 2:
        print("usage : RACINE [DOSSIER_TEMPORAIRE]", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    dossier = (Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-c4-"))).resolve()
    dossier.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # noqa: E402

    defauts = []
    for rel, attendu in SHA_ENTREES.items():
        e = sha((racine / rel).read_bytes())
        if e != attendu:
            print(f"ARRÊT : empreinte de {rel} {e} ≠ {attendu}")
            return 1
        print(f"{rel} : {e[:16]}… (égale)")

    print(f"\n# code au commit {COMMIT[:8]}, script v4, répétition jouet v4")
    copie = dossier / f"src-{COMMIT[:8]}"
    noms = git(racine, "ls-tree", "-r", "--name-only", COMMIT, "src").stdout.decode().split()
    for nom in noms:
        cible = copie / nom
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_bytes(git(racine, "show", f"{COMMIT}:{nom}").stdout)
    env = dict(os.environ, PYTHONPATH=str(copie / "src"), PYTHONDONTWRITEBYTECODE="1")
    r8 = subprocess.run([sys.executable, "-B", "-m", "controle_ia.t07.lecture_v4", "empreinte-config", str(racine / V8)],
                        capture_output=True, env=env, cwd=str(copie))
    r7 = subprocess.run([sys.executable, "-B", "-m", "controle_ia.t07.lecture_v4", "empreinte-config", str(racine / V7)],
                        capture_output=True, env=env, cwd=str(copie))
    s8, s7 = r8.stdout.decode().strip(), (r7.stdout.decode() + r7.stderr.decode()).strip()
    ok = r8.returncode == 0 and s8 == CANON_V8 and r7.returncode == 2 and "REFUS" in s7
    print(f"module recopié ({len(noms)} fichiers) ; `lecture_v4 empreinte-config` v8 : code {r8.returncode}, {s8} ; v7 : code "
          f"{r7.returncode}, « {s7[:70]} » : {ok}")
    if not ok:
        defauts.append("empreinte canonique de la v8 ou refus de la v7")
    rx = git(racine, "show", f"{COMMIT}:src/controle_ia/t07/reextraction_p3_v1.py").stdout.decode("utf-8")
    lv4 = git(racine, "show", f"{COMMIT}:src/controle_ia/t07/lecture_v4.py").stdout.decode("utf-8")
    ok = ('TOLERANCES = {"processeur": 1e-6, "carte_sonde": 1e-3, "carte_directions": 1e-2}' in rx
          and "cause non établie" in rx
          and "FAUTES_DU_BRAS = (GardeArret, OSError, RuntimeError, ValueError, KeyError, MemoryError, TypeError, AttributeError, "
              "IndexError)" in rx
          and 'v["etat"], v["motif"], v["directions"] = "échec", f"{type(e).__name__} : {e}", None' in rx
          and rx.count('echec_global(f"réextraction impossible : {type(e).__name__} : {e}")') == 2
          and '"controle-avant-ouverture"' in lv4)
    print(f"reextraction_p3_v1.py et lecture_v4.py au commit : TOLERANCES de la v8, réserve « cause non établie », FAUTES_DU_BRAS, "
          f"formes du motif (bras seul ; deux bras), sous-commande controle-avant-ouverture : {ok}")
    if not ok:
        defauts.append("code au commit (tolérances, motifs, sous-commande)")
    s4 = git(racine, "show", f"{COMMIT}:scripts/etape_a_t07_variante_b_v4.sh").stdout
    ok = sha(s4) == SCRIPT4 and b"lecture_v4 controle-avant-ouverture" in s4
    print(f"script v4 au commit : empreinte {sha(s4)[:16]}…, joue `lecture_v4 controle-avant-ouverture` : {ok}")
    if not ok:
        defauts.append("script v4")
    rep = json.loads((racine / REP_R).read_text(encoding="utf-8"))
    ok = rep.get("conforme") is True and len(rep.get("verdicts", {})) == 10 and all(v is True for v in rep["verdicts"].values())
    print(f"répétition jouet v4 : conforme {rep.get('conforme')}, {len(rep.get('verdicts', {}))} verdicts, tous vrais : {ok}")
    if not ok:
        defauts.append("répétition jouet v4")

    vc = (racine / VC).read_text(encoding="utf-8")
    s4vc = vc[vc.index("## 4. Couples proposés"):vc.index("## 5.")]
    vcs = {c["id"]: c for c in json.loads(re.search(r"```json\n(.*?)\n```", s4vc, re.S).group(1))}
    texte3 = (racine / C3).read_bytes().decode("utf-8")
    couples = json.loads((racine / COUPLES).read_text(encoding="utf-8"))
    ids = [c["id"] for c in couples]
    if len(set(ids)) != len(ids):
        print("ARRÊT : identifiants en double")
        return 1
    for g, v in EGAUX_VC.items():
        c = next(x for x in couples if x["id"] == g)
        egal = c["ancien"] == vcs[v]["ancien"] and c["nouveau"] == vcs[v]["nouveau"] and c["gelee"] == vcs[v]["gelee"]
        print(f"{g} égal au couple {v} de la vérification courte (ancien, nouveau, section gelée) : {egal}")
        if not egal:
            defauts.append(f"{g} ≠ {v}")
    print(f"\n# application ({len(couples)} couples) (id ; ligne ; sections touchées ; gelée)")
    t = texte3
    for c in couples:
        if sorted(c) != ["ancien", "gelee", "id", "motif", "nouveau", "section"]:
            print(f"ARRÊT : {c.get('id')} : clés {sorted(c)}")
            return 1
        n = t.count(c["ancien"])
        if n != 1 or c["ancien"] == c["nouveau"]:
            print(f"ARRÊT : {c['id']} : « ancien » présent {n} fois (1 attendu), ou égal au « nouveau » ; rien n'est écrit")
            return 1
        p = t.index(c["ancien"])
        touchees = section_de(t, p, p + len(c["ancien"]))
        geles = sorted(s for s in touchees if gelee(s))
        if geles:
            if c["gelee"] is None or len(touchees) != 1 or not geles[0].startswith(c["gelee"]):
                print(f"ARRÊT : {c['id']} touche l'empan gelé ({geles}) sans déclaration exacte (gelee = {c['gelee']!r})")
                return 1
        elif c["gelee"] is not None:
            print(f"ARRÊT : {c['id']} déclaré gelé ({c['gelee']}) mais touche {sorted(touchees)}")
            return 1
        print(f"{c['id']} ; l. {t.count(chr(10), 0, p) + 1} ; {', '.join(s[:40] for s in sorted(touchees))} ; {'OUI' if geles else 'non'}")
        t = t.replace(c["ancien"], c["nouveau"], 1)
    texte4 = t
    geles_faits = {c["id"]: c["gelee"] for c in couples if c["gelee"] is not None}
    print(f"couples gelés : {geles_faits} ; égaux au mandat : {geles_faits == GELES_MANDAT}")
    if geles_faits != GELES_MANDAT:
        defauts.append("couples gelés ≠ mandat")
    octets = texte4.encode("utf-8")
    sortie = racine / C4
    if sortie.exists() and sortie.read_bytes() != octets:
        print(f"ARRÊT (R12) : {C4} existe et diffère : rien n'est écrasé")
        return 1
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"\nécrit : {C4} ({sha(octets)} ; {texte4.count(chr(10))} lignes)")

    print("\n# vérifications")
    statut = next(l for l in texte4.split("\n") if l.startswith("- Statut :"))
    ok = texte4.split("\n", 1)[0] == TITRE and statut.startswith("- Statut : **candidat 4**")
    print(f"(1) titre et premier statut : {ok}")
    if not ok:
        defauts.append("titre ou statut")
    defait = texte4
    for c in reversed(couples):
        if defait.count(c["nouveau"]) != 1:
            defauts.append(f"défaisage de {c['id']} : « nouveau » présent {defait.count(c['nouveau'])} fois")
        defait = defait.replace(c["nouveau"], c["ancien"], 1)
    print(f"(2) couples défaits dans l'ordre inverse → candidat 3 octet pour octet : {defait == texte3}")
    if defait != texte3:
        defauts.append("défaisage ≠ candidat 3")
    s3, s4t = sections(texte3), sections(texte4)
    for k in s3:
        if not gelee(k):
            continue
        x = s4t.get(k, "")
        miens = [c for c in couples if c["gelee"] is not None and k.startswith(c["gelee"])]
        for c in reversed(miens):
            x = x.replace(c["nouveau"], c["ancien"], 1)
        egal = x == s3[k]
        print(f"    « {k[:48]} » : couples {[c['id'] for c in miens]} ; {len(lignes_diff(s3[k], s4t.get(k, '')))} lignes de "
              f"différence ; égale au candidat 3 une fois défaite : {egal}")
        if not egal:
            defauts.append(f"section gelée « {k[:40]} » changée hors des couples déclarés")
    neuves = [k for k in s4t if k not in s3]
    disparues = [k for k in s3 if k not in s4t]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues}")
    if neuves != NEUVES or disparues:
        defauts.append("sections neuves ou disparues")
    restes = {m: texte4.count(m) for m in sorted(set(GABARIT.findall(texte4)))}
    print(f"(4) marqueurs restants : {restes}")
    if restes != {MARQ: 1}:
        defauts.append("marqueurs")
    pb = problemes(racine / C4)
    factice = dossier / "T0.7-sondes-v0-v1-candidat4-valeur-factice.md"
    factice.write_text(texte4.replace(MARQ, "valeur-factice-c7-et-code-t07"), encoding="utf-8")
    pf = problemes(factice)
    print(f"(5) controle_ia.prereg.problemes(candidat 4) : {pb} ; à valeur factice : {pf}")
    if pb != [f"marqueurs de gabarit restants : {MARQ}"] or pf:
        defauts.append("problemes")
    manq = []
    for nom, h in NEUFS.items():
        if sha(git(racine, "show", f"{COMMIT}:src/controle_ia/t07/{nom}").stdout) != h or f"`src/controle_ia/t07/{nom}` `{h}`" not in texte4:
            manq.append(nom)
    v1 = json.loads((racine / CODE_V1).read_text(encoding="utf-8"))["fichiers"]
    for f, h in v1.items():
        if f"`{f}` `{h}`" not in texte4 or sha(git(racine, "show", f"{COMMIT}:{f}").stdout) != h:
            manq.append(f)
    n_mod = len([x for x in git(racine, "ls-tree", "--name-only", COMMIT, "src/controle_ia/t07/").stdout.decode().split() if x.endswith(".py")])
    print(f"(6) module au commit {COMMIT[:8]} : {n_mod} fichiers ; huit neufs et dix-huit anciens à leur empreinte et cités : {not manq}"
          f"{' ; manquants : ' + repr(manq) if manq else ''}")
    if manq or n_mod != 26:
        defauts.append("vingt-six modules")
    o8 = (racine / ORDRE8).read_text(encoding="utf-8")
    ok = (o8.count("<<ATT_C7_T07>>") == 1 and f"SHA_SCRIPT={SCRIPT4};" in o8 and "SHA_SCRIPT=a19c594d" not in o8
          and "| P14 |" in o8 and vcs["VC3-C"]["nouveau"] in o8 and vcs["VC3-D"]["nouveau"] in o8
          and "`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`" in o8)
    print(f"(7) ordre, brouillon 8 : `ATT_C7_T07` présent, script v4 à la ligne (A), P14, VC3-C et VC3-D tels qu'écrits, chemin "
          f"final de la v8 : {ok}")
    if not ok:
        defauts.append("ordre, brouillon 8")
    p4 = plat(texte4)
    manquantes = [ph for ph in PHRASES if plat(ph) not in p4]
    presentes = [ph for ph in ABSENTES if ph in texte4]
    print(f"(8) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)}{' ; manquantes : ' + repr(manquantes) if manquantes else ''} ; "
          f"passages retirés encore présents : {presentes}")
    if manquantes or presentes:
        defauts.append("phrases")
    d = lignes_diff(texte3, texte4)
    restants = [(texte4.count("\n", 0, m.start()) + 1, texte4[max(0, m.start() - 60):m.end() + 10].replace("\n", " "))
                for m in re.finditer(r"en cours", texte4)]
    print(f"(9) différentiel candidat 3 → candidat 4 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées ; {len(couples)} couples, dont {len(geles_faits)} gelés ; "
          f"« en cours » : {len(restants)} occurrences (historiques, imprimées pour relecture)")
    for ligne, ctx in restants:
        print(f"    l. {ligne} : …{ctx}…")
    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
