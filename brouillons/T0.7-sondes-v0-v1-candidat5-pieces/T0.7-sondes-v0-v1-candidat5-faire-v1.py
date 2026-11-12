"""T0.7 sondes v0, candidat 5 : application des couples du candidat 5 au candidat 4 (couples VF4-F à VF4-K de la vérification
finale, tels qu'écrits, d'abord et seuls ; puis mentions d'état et renvois à l'ordre, brouillon 9) et vérifications, dont
« défaire les couples redonne le candidat 4 à l'octet » (v1).

Rédacteur des candidats 2 à 5 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 11 novembre
2026, sur le message de la mère qui suit R-2315 (mêmes interdits et chemins que la consigne `d29c7858…`, aux noms près). Méthode du
script du candidat 4 (`brouillons/T0.7-sondes-v0-v1-candidat4-pieces/T0.7-sondes-v0-v1-candidat4-faire-v1.py`, `65015a26…`).
Bibliothèque standard, `controle_ia.prereg` du dépôt (RACINE/src) et `git` en lecture (`git show <commit>:<chemin>`, `git ls-tree`,
avec `--no-optional-locks`) ; `src/` au commit `a621dcd3` est recopié par `git show` dans le dossier temporaire pour rejouer
`lecture_v4 empreinte-config` ; aucun réseau ; aucune écriture hors du candidat 5 et du dossier temporaire.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie les empreintes de ses entrées (candidat 4, couples, ordres brouillons 8 et 9, vérification finale, configurations v7 et
   v8, `CODE-T07-v1.json`) ;
2. code au commit `a621dcd3` (inchangé depuis le candidat 4) : `lecture_v4 empreinte-config` rend `0f32c6de…` pour la v8 et
   refuse la v7 ;
3. les six premiers couples sont VF4-F à VF4-K, égaux (ancien, nouveau, section gelée) à ceux du § 4 de la vérification finale ;
   appliqués **d'abord et seuls**, ils doivent donner l'empreinte calculée par le vérificateur (`5a3d20a7…`) **avant** tout autre
   couple ; sinon arrêt (code 1), rien n'est écrit ;
4. applique tous les couples ; chaque « ancien » présent exactement une fois et différent de son « nouveau » ; un couple touche
   l'empan gelé si et seulement si son champ `gelee` le déclare, dans la section déclarée ; sinon arrêt, rien n'est écrit ;
5. écrit `brouillons/T0.7-sondes-v0-v1-candidat5.md` (R12) ;
6. vérifie : (1) titre et premier statut ; (2) **défaire tous les couples dans l'ordre inverse redonne le candidat 4 octet pour
   octet** ; chaque section gelée, ses couples défaits, égale celle du candidat 4 ; couples gelés = VF4-H seul (G5-01, Liste
   d'arrêt) ; (3) sections neuves (une) et disparues (aucune) ; (4) un seul marqueur restant, une occurrence ; (5) `problemes`
   réduit à sa ligne, vide à valeur factice ; (6) vingt-six modules au commit `a621dcd3`, huit neufs et dix-huit anciens à leur
   empreinte et cités ; (7) ordre brouillon 9 cité par chemin et empreinte dans les cellules vivantes (« Module », marqueur
   `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07`) ; l'ordre 9 porte ses douze marqueurs, le script v4 à la ligne (A), VF4-A à VF4-E et
   aucune lecture de colonne pour P14 ; (8) phrases exigées présentes, passages retirés absents ; (9) différentiel compté ; mentions
   d'état restantes imprimées.
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
C4 = "brouillons/T0.7-sondes-v0-v1-candidat4.md"
C5 = "brouillons/T0.7-sondes-v0-v1-candidat5.md"
P = "brouillons/T0.7-sondes-v0-v1-candidat5-pieces/"
COUPLES = P + "T0.7-sondes-v0-v1-candidat5-couples-v1.json"
ORDRE8 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md"
ORDRE9 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9.md"
VF = "prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md"
PIECES = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/"
V7, V8 = PIECES + "configuration-t07-v7.json", PIECES + "configuration-t07-v8.json"
CODE_V1 = "registres/code-t07/CODE-T07-v1.json"
SHA_ENTREES = {
    C4: "cad20c1db89397b78c9ba40fa773b3c0396487b0bec4c5cd43a4b7e12d7857d6",
    COUPLES: "531e88898f4072df18c8043d535c3cc0ce0a2dd45d5fad9fd04e8cb194db6458",
    ORDRE8: "24dc8df6555bac03f2ffbe8440c3c1a7b9bf2aeaf9eab3c651306a6a73fc116e",
    ORDRE9: "374332976304d08af7c1b941d8798877d34f9e30b3945ba2be3ac19189740402",
    VF: "26efc4dfb4924e6a2d6ddfaf7fdb37a6dae453946b1a114df2ec76ec014ad257",
    V7: "3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab",
    V8: "e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328",
    CODE_V1: "9ef4ede751fcceb51eda1e622deaa62552326e395fdbd647c6989ad32353701f",
}
SHA_VF_SEULS = "5a3d20a7b3ba2859e5e18933b1474db7d26580d7b53d725e38d1d71a61ab8221"
IDS_VF = ["VF4-F", "VF4-G", "VF4-H", "VF4-I", "VF4-J", "VF4-K"]
IDS_VF_ORDRE = ["VF4-A", "VF4-B", "VF4-C", "VF4-D", "VF4-E"]
CANON_V8 = "0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12"
SCRIPT4 = "4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6"
TITRE = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — candidat 5"
MARQ = "<<C7_ET_CODE_T07_26_MODULES>>"
MARQUEURS_ORDRE = ["<<ID_SESSION_FILLE>>", "<<EMPREINTE_CONFIG_T07>>", "<<LIGNE_SCELLEMENT_T07>>", "<<DEPENSE_ANTERIEURE_USD>>",
                   "<<RUN_T06_7B>>", "<<BRANCHE_7B>>", "<<COMMIT_CODE_T07>>", "<<COMMIT_SCELLEMENT_T07>>",
                   "<<CHEMIN_CONFIG_T07>>", "<<PERIMETRE_T07>>", "<<COMMIT_SRC_CONTRE_LU_T07>>", "<<ATT_C7_T07>>"]
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
GELES_MANDAT = {"VF4-H": "Liste d'arrêt"}
NEUVES = ["Table « ce qui change du candidat 4 au candidat 5 »"]
NEUFS = {"plancher_v2.py": "a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796",
         "lecture_v3.py": "ac3666e4003b55629600c4d21db9e9b35086c37325c4f63e6417bca1864c921a",
         "lectures_t07_v2.py": "1f523c07273ae11359ca199056eadbf68cf1448c93e9c43eb2bf4a8a600b5271",
         "plancher_v3.py": "c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8",
         "reextraction_p3_v1.py": "c32696b82af620e5da07fc4ec5bbb801dc385467cbf8235b799ad28b6471eaf9",
         "lecture_v4.py": "42f60780e6944568e81880887a1ad87c57a520e8c7d54083b36a43c097a06d06",
         "passe_blanc_v2.py": "8e24642fd49c2d57d7f3093f4989a06a5d9110145f7d5574e5b000e48f82dba5",
         "repli_etapes_v2.py": "fe08aaa14de1ca0ac88292f2c7a10ec8d591fee1e83f90c9ae38b32d0c6a2f50"}
PHRASES = (
    "- Statut : **candidat 5**", "**Changement dans l'empan gelé : un**", "## Table « ce qui change du candidat 4 au candidat 5 »",
    f"ordre contre-lu (R2) et scellé, `{ORDRE9}`, sha256 `{SHA_ENTREES[ORDRE9]}` (**candidat 5**",
    f"| **candidat 5** : `{ORDRE9}`, `{SHA_ENTREES[ORDRE9]}`", f"`{SHA_ENTREES[VF]}`",
    "**`a621dcd3` est le dernier commit contre-lu**", "1 duodecies. **Candidat 5", "**Candidat 5** : les couples VF4-F à VF4-K",
    "**VF4-04**", "pour ces bras, cette ligne prime sur la précédente, qui ne vaut seule que pour un bras dont le motif commence par `GardeArret`",
    "`1e08fab15586354d58349624b9fc6090e6549446f8faf6e0e6d6b89db45636a0`", "`b0b1ff695265d2934ca132b8a78cae2479a8d1f58962685fbbea960a827fd703`",
    "nombre de lignes des mesures de 7b", "**état au candidat 5** (R-2315)", "**couvert depuis**",
)
ABSENTES = ("- Statut : **candidat 4**", "nombre d'actions de 7b compté", "jetons_notes` seule) **compté par la mère")


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
    dossier = (Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-c5-"))).resolve()
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

    print(f"\n# code au commit {COMMIT[:8]} (inchangé depuis le candidat 4)")
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
          f"{r7.returncode} : {ok}")
    if not ok:
        defauts.append("empreinte canonique de la v8 ou refus de la v7")

    vf = (racine / VF).read_text(encoding="utf-8")
    vfs = {c["id"]: c for c in json.loads(re.search(r"```json\n(.*?)\n```", vf[vf.index("## 4. Couples proposés"):vf.index("## 5.")],
                                                    re.S).group(1))}
    texte4 = (racine / C4).read_bytes().decode("utf-8")
    couples = json.loads((racine / COUPLES).read_text(encoding="utf-8"))
    ids = [c["id"] for c in couples]
    if len(set(ids)) != len(ids) or ids[:len(IDS_VF)] != IDS_VF or any(i.startswith("VF4-") for i in ids[len(IDS_VF):]):
        print(f"ARRÊT : identifiants ({ids[:8]}…)")
        return 1
    print("\n# couples de la vérification finale, d'abord et seuls")
    t = texte4
    for c in couples[:len(IDS_VF)]:
        v = vfs[c["id"]]
        egal = v["cible"] == "candidat 4" and c["ancien"] == v["ancien"] and c["nouveau"] == v["nouveau"] and c["gelee"] == v["gelee"]
        if not egal or t.count(c["ancien"]) != 1:
            print(f"ARRÊT : {c['id']} différent du couple du vérificateur, ou « ancien » présent {t.count(c['ancien'])} fois")
            return 1
        t = t.replace(c["ancien"], c["nouveau"], 1)
    e = sha(t.encode("utf-8"))
    print(f"{', '.join(IDS_VF)} égaux au § 4 de la vérification finale ; appliqués seuls : {e} ; empreinte du vérificateur : "
          f"{e == SHA_VF_SEULS}")
    if e != SHA_VF_SEULS:
        print("ARRÊT : empreinte des couples du vérificateur appliqués seuls ≠ 5a3d20a7… ; rien n'est écrit")
        return 1
    reste_vf = [x for x in vfs if x not in IDS_VF and x not in IDS_VF_ORDRE]
    if reste_vf:
        defauts.append(f"couples de la vérification finale non répartis : {reste_vf}")

    print(f"\n# application ({len(couples)} couples) (id ; ligne ; sections touchées ; gelée)")
    t = texte4
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
    texte5 = t
    geles_faits = {c["id"]: c["gelee"] for c in couples if c["gelee"] is not None}
    print(f"couples gelés : {geles_faits} (G5-01 = VF4-H) ; égaux au mandat : {geles_faits == GELES_MANDAT}")
    if geles_faits != GELES_MANDAT:
        defauts.append("couples gelés ≠ mandat")
    octets = texte5.encode("utf-8")
    sortie = racine / C5
    if sortie.exists() and sortie.read_bytes() != octets:
        print(f"ARRÊT (R12) : {C5} existe et diffère : rien n'est écrasé")
        return 1
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"\nécrit : {C5} ({sha(octets)} ; {texte5.count(chr(10))} lignes)")

    print("\n# vérifications")
    statut = next(l for l in texte5.split("\n") if l.startswith("- Statut :"))
    ok = texte5.split("\n", 1)[0] == TITRE and statut.startswith("- Statut : **candidat 5**")
    print(f"(1) titre et premier statut : {ok}")
    if not ok:
        defauts.append("titre ou statut")
    defait = texte5
    for c in reversed(couples):
        if defait.count(c["nouveau"]) != 1:
            defauts.append(f"défaisage de {c['id']} : « nouveau » présent {defait.count(c['nouveau'])} fois")
        defait = defait.replace(c["nouveau"], c["ancien"], 1)
    print(f"(2) couples défaits dans l'ordre inverse → candidat 4 octet pour octet : {defait == texte4}")
    if defait != texte4:
        defauts.append("défaisage ≠ candidat 4")
    s4, s5 = sections(texte4), sections(texte5)
    for k in s4:
        if not gelee(k):
            continue
        x = s5.get(k, "")
        miens = [c for c in couples if c["gelee"] is not None and k.startswith(c["gelee"])]
        for c in reversed(miens):
            x = x.replace(c["nouveau"], c["ancien"], 1)
        egal = x == s4[k]
        print(f"    « {k[:48]} » : couples {[c['id'] for c in miens]} ; {len(lignes_diff(s4[k], s5.get(k, '')))} lignes de "
              f"différence ; égale au candidat 4 une fois défaite : {egal}")
        if not egal:
            defauts.append(f"section gelée « {k[:40]} » changée hors des couples déclarés")
    neuves = [k for k in s5 if k not in s4]
    disparues = [k for k in s4 if k not in s5]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues}")
    if neuves != NEUVES or disparues:
        defauts.append("sections neuves ou disparues")
    restes = {m: texte5.count(m) for m in sorted(set(GABARIT.findall(texte5)))}
    print(f"(4) marqueurs restants : {restes}")
    if restes != {MARQ: 1}:
        defauts.append("marqueurs")
    pb = problemes(racine / C5)
    factice = dossier / "T0.7-sondes-v0-v1-candidat5-valeur-factice.md"
    factice.write_text(texte5.replace(MARQ, "valeur-factice-c7-et-code-t07"), encoding="utf-8")
    pf = problemes(factice)
    print(f"(5) controle_ia.prereg.problemes(candidat 5) : {pb} ; à valeur factice : {pf}")
    if pb != [f"marqueurs de gabarit restants : {MARQ}"] or pf:
        defauts.append("problemes")
    manq = []
    for nom, h in NEUFS.items():
        if sha(git(racine, "show", f"{COMMIT}:src/controle_ia/t07/{nom}").stdout) != h or f"`src/controle_ia/t07/{nom}` `{h}`" not in texte5:
            manq.append(nom)
    v1 = json.loads((racine / CODE_V1).read_text(encoding="utf-8"))["fichiers"]
    for f, h in v1.items():
        if f"`{f}` `{h}`" not in texte5 or sha(git(racine, "show", f"{COMMIT}:{f}").stdout) != h:
            manq.append(f)
    n_mod = len([x for x in git(racine, "ls-tree", "--name-only", COMMIT, "src/controle_ia/t07/").stdout.decode().split() if x.endswith(".py")])
    print(f"(6) module au commit {COMMIT[:8]} : {n_mod} fichiers ; huit neufs et dix-huit anciens à leur empreinte et cités : {not manq}"
          f"{' ; manquants : ' + repr(manq) if manq else ''}")
    if manq or n_mod != 26:
        defauts.append("vingt-six modules")
    o9 = (racine / ORDRE9).read_text(encoding="utf-8")
    ok = (all(o9.count(m) == 1 for m in MARQUEURS_ORDRE) and sorted(set(GABARIT.findall(o9))) == sorted(MARQUEURS_ORDRE)
          and f"SHA_SCRIPT={SCRIPT4};" in o9 and all(vfs[i]["nouveau"] in o9 for i in IDS_VF_ORDRE)
          and "`jetons_notes` seule" not in o9 and "## 0 sexies." in o9)
    print(f"(7) ordre, brouillon 9 : douze marqueurs (dont `ATT_C7_T07`, `COMMIT_SRC_CONTRE_LU_T07`), script v4 à la ligne (A), "
          f"VF4-A à VF4-E tels qu'écrits, P14 sans lecture de colonne ; cité par chemin et empreinte au candidat (« Module », "
          f"marqueur) : {ok}")
    if not ok:
        defauts.append("ordre, brouillon 9")
    p5 = plat(texte5)
    manquantes = [ph for ph in PHRASES if plat(ph) not in p5]
    presentes = [ph for ph in ABSENTES if ph in texte5]
    print(f"(8) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)}{' ; manquantes : ' + repr(manquantes) if manquantes else ''} ; "
          f"passages retirés encore présents : {presentes}")
    if manquantes or presentes:
        defauts.append("phrases")
    d = lignes_diff(texte4, texte5)
    print(f"(9) différentiel candidat 4 → candidat 5 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées ; {len(couples)} couples, dont {len(geles_faits)} gelé")
    for motif in (r"aucune contre-lecture", r"non contre-lu à ce jour", r"brouillon8\.md", r"24dc8df6"):
        occ = [(texte5.count("\n", 0, m.start()) + 1, texte5[max(0, m.start() - 50):m.end() + 70].replace("\n", " "))
               for m in re.finditer(motif, texte5)]
        print(f"    « {motif} » : {len(occ)} occurrences (historiques ou annotées, imprimées pour relecture)")
        for ligne, ctx in occ:
            print(f"      l. {ligne} : …{ctx}…")
    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
