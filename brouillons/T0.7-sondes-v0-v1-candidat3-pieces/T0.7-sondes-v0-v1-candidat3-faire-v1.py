"""T0.7 sondes v0, candidat 3 : application des couples du candidat 3 au candidat 2 (configuration v8, code corrigé au commit
`7e23a554`, script v3, ordre brouillon 7) et vérifications, dont « défaire les couples redonne le candidat 2 à l'octet » (v1).

Rédacteur des candidats 2 et 3 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 11 novembre
2026, sur le message de la mère qui suit R-2309 (mêmes interdits et chemins que la consigne `d29c7858…`, aux noms près). Méthode du
script du candidat 2 (`brouillons/T0.7-sondes-v0-v1-candidat2-pieces/T0.7-sondes-v0-v1-candidat2-faire-v1.py`, `42f3ad12…`).
Bibliothèque standard, `controle_ia.prereg` du dépôt (RACINE/src) et `git` en lecture (`git show <commit>:<chemin>`, `git ls-tree`) ;
le module au commit `7e23a554` est recopié par `git show` dans le dossier temporaire pour rejouer `lecture_v4 empreinte-config` ;
aucun réseau ; aucune écriture hors du candidat 3 et du dossier temporaire.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie les empreintes de ses entrées (candidat 2, couples, ordres brouillons 6 et 7, configurations v7 et v8, rapport du code v2,
   `CODE-T07-v1.json`) ;
2. configuration : v8 = v7 aux seules tolérances du palier « carte » près (10⁻³, 10⁻²) ; `lecture_v4 empreinte-config` au commit
   `7e23a554` rend `0f32c6de…` et refuse la v7 ; `TOLERANCES` et `RESERVE_CARTE` du module à ce commit égales à la v8 et au texte ;
3. applique les couples ; chaque « ancien » présent exactement une fois et différent de son « nouveau » ; un couple touche l'empan
   gelé si et seulement si son champ `gelee` le déclare, dans la section déclarée ; sinon arrêt (code 1), rien n'est écrit ;
4. écrit `brouillons/T0.7-sondes-v0-v1-candidat3.md` (R12) ;
5. vérifie : (1) titre et premier statut ; (2) **défaire tous les couples dans l'ordre inverse redonne le candidat 2 octet pour
   octet** ; chaque section gelée, ses couples défaits, égale celle du candidat 2 ; couples gelés = G3-01 (Plan d'analyse) et
   G3-02 (Liste d'arrêt) ; (3) sections neuves (une) et disparues (aucune) ; (4) un seul marqueur restant, une occurrence ;
   (5) `problemes` réduit à sa ligne, vide à valeur factice ; (6) vingt-six modules au commit `7e23a554`, huit neufs et dix-huit
   anciens à leur empreinte et cités ; (7) ordre brouillon 7 cité par chemin et empreinte, son marqueur `ATT_C7_T07` présent et
   `SHA_SCRIPT_V3_T07` rempli ; (8) phrases exigées présentes, passages retirés absents ; (9) différentiel compté.
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

COMMIT = "7e23a554aca040016a08fe510504adec172c6998"
C2 = "brouillons/T0.7-sondes-v0-v1-candidat2.md"
C3 = "brouillons/T0.7-sondes-v0-v1-candidat3.md"
P = "brouillons/T0.7-sondes-v0-v1-candidat3-pieces/"
COUPLES = P + "T0.7-sondes-v0-v1-candidat3-couples-v1.json"
ORDRE6 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md"
ORDRE7 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md"
PIECES = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/"
V7, V8 = PIECES + "configuration-t07-v7.json", PIECES + "configuration-t07-v8.json"
RAP2 = PIECES + "rapport-code-plancher-v3-v2.md"
CODE_V1 = "registres/code-t07/CODE-T07-v1.json"
SHA_ENTREES = {
    C2: "9de13f6a9a40267ff8111a009643a4871eb9e0f91ae23ba89182d3abbc9a3335",
    COUPLES: "4e5fc8b05dbbf688c294bd7f10296c89d742eb8cfb0d7887732f5f2ea364ffed",
    ORDRE6: "92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca",
    ORDRE7: "d799a01bd6008d73794a42dd8b4657c4498ca291bcbd64b771711cf6632a5916",
    V7: "3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab",
    V8: "e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328",
    RAP2: "71cc3b89c2df3c8f511796af0e3597844fb8fd1ec37735f0cbeae21d7b5ca231",
    CODE_V1: "9ef4ede751fcceb51eda1e622deaa62552326e395fdbd647c6989ad32353701f",
}
CANON_V8 = "0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12"
SCRIPT3 = "a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560"
TITRE = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — candidat 3"
MARQ = "<<C7_ET_CODE_T07_26_MODULES>>"
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
GELES_MANDAT = {"G3-01": "Plan d'analyse", "G3-02": "Liste d'arrêt"}
NEUVES = ["Table « ce qui change du candidat 2 au candidat 3 »"]
NEUFS = {"plancher_v2.py": "a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796",
         "lecture_v3.py": "ac3666e4003b55629600c4d21db9e9b35086c37325c4f63e6417bca1864c921a",
         "lectures_t07_v2.py": "1f523c07273ae11359ca199056eadbf68cf1448c93e9c43eb2bf4a8a600b5271",
         "plancher_v3.py": "c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8",
         "reextraction_p3_v1.py": "66b6684cbd816d88968ac7faf9d7df98642bdfee04bddf82507352fdf408b76e",
         "lecture_v4.py": "f193f1b12b6fd3e1194e83e11f299d8da384e5e2975adf03235acb34bb789078",
         "passe_blanc_v2.py": "8e24642fd49c2d57d7f3093f4989a06a5d9110145f7d5574e5b000e48f82dba5",
         "repli_etapes_v2.py": "fe08aaa14de1ca0ac88292f2c7a10ec8d591fee1e83f90c9ae38b32d0c6a2f50"}
PHRASES = (
    "- Statut : **candidat 3**", "« carte » (≤ 10⁻³ pour le témoin, ≤ 10⁻² pour les directions",
    "« écart au palier « carte », cause non établie »", "**la garde n'arrête pas toute faute**",
    f"- Configuration de T0.7 : `{CANON_V8}`", "**chemin final `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`**",
    f"`{ORDRE7}`, sha256 `d799a01bd6008d73794a42dd8b4657c4498ca291bcbd64b771711cf6632a5916`", f"`{SCRIPT3}`",
    "**contrôle avant l'ouverture**, CLP3-03", "**note 05**", "**note 07**", "**note 10**", "**note 06 déclarée**",
    "**toujours vingt-six modules**", "1 decies. **Candidat 3", "## Table « ce qui change du candidat 2 au candidat 3 »",
    "**Candidat 3** : **à contre-lire par une vérification courte neuve**", "commit de `main` qui fusionne la branche finale du code",
)
ABSENTES = ("- Statut : **candidat 2**", "« carte » (≤ 10⁻² pour le témoin, ≤ 10⁻¹ pour les directions :",
            "- Configuration de T0.7 : `4ff92c8e")


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
    dossier = (Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-c3-"))).resolve()
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

    print("\n# configuration v8 et code au commit 7e23a554")
    c7 = json.loads((racine / V7).read_text(encoding="utf-8"))
    c8 = json.loads((racine / V8).read_text(encoding="utf-8"))
    cles = sorted(k for k in set(c7) | set(c8) if c7.get(k) != c8.get(k))
    sous = sorted(k for k in set(c7["plancher_figees"]) | set(c8["plancher_figees"])
                  if c7["plancher_figees"].get(k) != c8["plancher_figees"].get(k))
    tol8 = c8["plancher_figees"]["tolerances"]
    ok = cles == ["plancher_figees"] and sous == ["tolerances"] and tol8 == {"processeur": 1e-06, "carte_sonde": 0.001,
                                                                          "carte_directions": 0.01}
    print(f"v7 → v8 : clés {cles}, sous-clés {sous}, tolérances {tol8} : {ok}")
    if not ok:
        defauts.append("configuration v8 ≠ v7 aux tolérances près")
    copie = dossier / "src-7e23a554"
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
    print(f"module recopié au commit {COMMIT[:8]} ({len(noms)} fichiers) ; `lecture_v4 empreinte-config` v8 : code {r8.returncode}, {s8} ; "
          f"v7 : code {r7.returncode}, « {s7[:70]} » : {ok}")
    if not ok:
        defauts.append("empreinte canonique de la v8 ou refus de la v7")
    rx = git(racine, "show", f"{COMMIT}:src/controle_ia/t07/reextraction_p3_v1.py").stdout.decode("utf-8")
    ok = ('TOLERANCES = {"processeur": 1e-6, "carte_sonde": 1e-3, "carte_directions": 1e-2}' in rx
          and "cause non établie" in rx)
    print(f"reextraction_p3_v1.py au commit : TOLERANCES de la v8 et réserve « cause non établie » : {ok}")
    if not ok:
        defauts.append("TOLERANCES ou RESERVE_CARTE du module")

    texte2 = (racine / C2).read_bytes().decode("utf-8")
    couples = json.loads((racine / COUPLES).read_text(encoding="utf-8"))
    ids = [c["id"] for c in couples]
    if len(set(ids)) != len(ids):
        print("ARRÊT : identifiants en double")
        return 1
    print(f"\n# application ({len(couples)} couples) (id ; ligne ; sections touchées ; gelée)")
    t = texte2
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
    texte3 = t
    geles_faits = {c["id"]: c["gelee"] for c in couples if c["gelee"] is not None}
    print(f"couples gelés : {geles_faits} ; égaux au mandat : {geles_faits == GELES_MANDAT}")
    if geles_faits != GELES_MANDAT:
        defauts.append("couples gelés ≠ mandat")
    octets = texte3.encode("utf-8")
    sortie = racine / C3
    if sortie.exists() and sortie.read_bytes() != octets:
        print(f"ARRÊT (R12) : {C3} existe et diffère : rien n'est écrasé")
        return 1
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"\nécrit : {C3} ({sha(octets)} ; {texte3.count(chr(10))} lignes)")

    print("\n# vérifications")
    statut = next(l for l in texte3.split("\n") if l.startswith("- Statut :"))
    ok = texte3.split("\n", 1)[0] == TITRE and statut.startswith("- Statut : **candidat 3**")
    print(f"(1) titre et premier statut : {ok}")
    if not ok:
        defauts.append("titre ou statut")
    defait = texte3
    for c in reversed(couples):
        if defait.count(c["nouveau"]) != 1:
            defauts.append(f"défaisage de {c['id']} : « nouveau » présent {defait.count(c['nouveau'])} fois")
        defait = defait.replace(c["nouveau"], c["ancien"], 1)
    print(f"(2) couples défaits dans l'ordre inverse → candidat 2 octet pour octet : {defait == texte2}")
    if defait != texte2:
        defauts.append("défaisage ≠ candidat 2")
    s2, s3 = sections(texte2), sections(texte3)
    for k in s2:
        if not gelee(k):
            continue
        x = s3.get(k, "")
        miens = [c for c in couples if c["gelee"] is not None and k.startswith(c["gelee"])]
        for c in reversed(miens):
            x = x.replace(c["nouveau"], c["ancien"], 1)
        egal = x == s2[k]
        print(f"    « {k[:48]} » : couples {[c['id'] for c in miens]} ; {len(lignes_diff(s2[k], s3.get(k, '')))} lignes de "
              f"différence ; égale au candidat 2 une fois défaite : {egal}")
        if not egal:
            defauts.append(f"section gelée « {k[:40]} » changée hors des couples déclarés")
    neuves = [k for k in s3 if k not in s2]
    disparues = [k for k in s2 if k not in s3]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues}")
    if neuves != NEUVES or disparues:
        defauts.append("sections neuves ou disparues")
    restes = {m: texte3.count(m) for m in sorted(set(GABARIT.findall(texte3)))}
    print(f"(4) marqueurs restants : {restes}")
    if restes != {MARQ: 1}:
        defauts.append("marqueurs")
    pb = problemes(racine / C3)
    factice = dossier / "T0.7-sondes-v0-v1-candidat3-valeur-factice.md"
    factice.write_text(texte3.replace(MARQ, "valeur-factice-c7-et-code-t07"), encoding="utf-8")
    pf = problemes(factice)
    print(f"(5) controle_ia.prereg.problemes(candidat 3) : {pb} ; à valeur factice : {pf}")
    if pb != [f"marqueurs de gabarit restants : {MARQ}"] or pf:
        defauts.append("problemes")
    manq = []
    for nom, h in NEUFS.items():
        if sha(git(racine, "show", f"{COMMIT}:src/controle_ia/t07/{nom}").stdout) != h or f"`src/controle_ia/t07/{nom}` `{h}`" not in texte3:
            manq.append(nom)
    v1 = json.loads((racine / CODE_V1).read_text(encoding="utf-8"))["fichiers"]
    for f, h in v1.items():
        if f"`{f}` `{h}`" not in texte3 or sha(git(racine, "show", f"{COMMIT}:{f}").stdout) != h:
            manq.append(f)
    n_mod = len([x for x in git(racine, "ls-tree", "--name-only", COMMIT, "src/controle_ia/t07/").stdout.decode().split() if x.endswith(".py")])
    print(f"(6) module au commit {COMMIT[:8]} : {n_mod} fichiers ; huit neufs et dix-huit anciens à leur empreinte et cités : {not manq}"
          f"{' ; manquants : ' + repr(manq) if manq else ''}")
    if manq or n_mod != 26:
        defauts.append("vingt-six modules")
    o7 = (racine / ORDRE7).read_text(encoding="utf-8")
    ok = (o7.count("<<ATT_C7_T07>>") == 1 and "<<SHA_SCRIPT_V3_T07>>" not in o7 and f"SHA_SCRIPT={SCRIPT3};" in o7
          and "`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`" in o7)
    print(f"(7) ordre, brouillon 7 : `ATT_C7_T07` présent, `SHA_SCRIPT_V3_T07` rempli ({SCRIPT3[:8]}…), chemin final de la v8 : {ok}")
    if not ok:
        defauts.append("ordre, brouillon 7")
    p3 = plat(texte3)
    manquantes = [ph for ph in PHRASES if plat(ph) not in p3]
    presentes = [ph for ph in ABSENTES if ph in texte3]
    print(f"(8) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)}{' ; manquantes : ' + repr(manquantes) if manquantes else ''} ; "
          f"passages retirés encore présents : {presentes}")
    if manquantes or presentes:
        defauts.append("phrases")
    d = lignes_diff(texte2, texte3)
    print(f"(9) différentiel candidat 2 → candidat 3 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées ; {len(couples)} couples, dont {len(geles_faits)} gelés")
    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
