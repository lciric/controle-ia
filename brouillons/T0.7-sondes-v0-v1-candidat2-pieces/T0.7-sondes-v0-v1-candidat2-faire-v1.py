"""T0.7 sondes v0, candidat 2 : application des couples du candidat 2 au candidat 1 (remède (a'), 800 directions, plancher neuf
des sondes figées de P3) et vérifications, dont « tout le reste de l'empan gelé égal à l'octet » (v1).

Rédacteur neuf du candidat 2 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 11 novembre
2026 ; consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-candidat2-v1.md`
(`d29c7858…`) ; méthode du script du candidat 1 (`brouillons/T0.7-sondes-v0-v1-candidat1-pieces/T0.7-sondes-v0-v1-candidat1-faire-v1.py`,
`2e74a1b4…`). Bibliothèque standard, plus `controle_ia.prereg` du dépôt (RACINE/src) et `git` en lecture (`git show <commit>:<chemin>`,
`git ls-tree`) ; le module au commit `0d0c5da4` est recopié par `git show` dans le dossier temporaire pour rejouer
`lecture_v4 empreinte-config` ; aucun réseau ; aucune écriture hors du candidat 2 et du dossier temporaire.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie les empreintes de ses entrées (candidat 1, couples, vérification courte du candidat 1, ordre d'exécution brouillon 6,
   configuration v5 et v7, puissance et sa sortie, rapport chiffré et verdict de l'audit de P3, note v3, rapport du code) ;
2. configuration : v7 = v5 plus `methode_plancher`, `n_plancher` (800) et `plancher_figees`, rien d'autre ; `lecture_v4
   empreinte-config` (module recopié au commit `0d0c5da4`) rend `4ff92c8e…` ; `lecture_v2` la refuse ;
3. applique les couples dans l'ordre ; chaque « ancien » présent exactement une fois au moment de son application et différent de
   son « nouveau » ; clés exactement `id`, `section`, `motif`, `gelee`, `ancien`, `nouveau` ; **un couple touche l'empan gelé
   (« Hypothèse » à « Liste d'arrêt ») si et seulement si son champ `gelee` le déclare, et seulement dans la section déclarée** ;
   sinon arrêt (code 1), rien n'est écrit ; VC1-A et VC1-B égaux à ceux du fichier de la vérification courte ;
4. écrit `brouillons/T0.7-sondes-v0-v1-candidat2.md` (R12) ;
5. vérifie : (1) titre et premier statut ; (2) **chaque section de l'empan gelé, ses couples gelés défaits dans l'ordre inverse,
   égale octet pour octet celle du candidat 1** ; liste des couples gelés égale à celle du mandat (G2-01 à G2-17) ; (3) sections
   neuves (une), disparues (aucune) ; (4) marqueurs : un seul restant, une occurrence ; les remplis absents ; (5) `problemes`
   réduit à la ligne de ce marqueur, vide à valeur factice ; (6) règle (a) citée telle que l'écrit la docstring de
   `plancher_v2.py` au commit `0d0c5da4` ; (7) vingt-six modules : huit neufs à leur empreinte au commit et cités, dix-huit de
   `CODE-T07-v1.json` cités ; (8) devis égaux à ceux de l'ordre, brouillon 6 ; (9) puissance : nombres cités présents dans la
   sortie versée ; (10) réserves de P3 jointes (forme du registre et forme de l'audit) ; (11) phrases exigées présentes, passages
   retirés absents ; (12) différentiel compté.
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

COMMIT = "0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07"
C1 = "brouillons/T0.7-sondes-v0-v1-candidat1.md"
C2 = "brouillons/T0.7-sondes-v0-v1-candidat2.md"
P = "brouillons/T0.7-sondes-v0-v1-candidat2-pieces/"
COUPLES = P + "T0.7-sondes-v0-v1-candidat2-couples-v1.json"
VC = "prereg/contre-lectures/T0.7-sondes-v0-v1-candidat1-verification-courte-v1.md"
ORDRE6 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md"
V5 = "brouillons/T0.7-sondes-v0-v1-candidat1-pieces/configuration-t07-v5.json"
V7 = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v7.json"
PUISS, PUISS_TXT = P + "puissance_regle_a_t07_v1.py", P + "puissance-regle-a-t07-v1.txt"
AUDIT = "docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md"
CODE_V1 = "registres/code-t07/CODE-T07-v1.json"
SHA_ENTREES = {
    C1: "1718f2a047195c8553f01cd937b24a061d1dc3a54e865775449abaf0cfc93913",
    COUPLES: "beb5ecfb210978a188a749b6c4420757a0106a523d72189e146971f09f39daea",
    VC: "ef3431a1a45c5e1fe8a83369fefb5ca9b5ba0cb1b69dc61ae5a23d9fd5e5e138",
    ORDRE6: "92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca",
    V5: "4be50447d1063015aa8ad99970d7e803765d85964d2b58010f5731bcd8c4ff46",
    V7: "3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab",
    PUISS: "4523a480f8560089f5c34e63b0e29ac65d90689ed8ffc87f1aab584916447146",
    PUISS_TXT: "af73498e757d4ab33e2804a30b375a815340d6fa9b63d34f3bec8682630a83dd",
    AUDIT: "57f16378d0bf15e5d95cb771cbc181cc41c610cb947a22f33c6a16746e08997e",
    "docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/rapport-p3-v1.json":
        "bdd5f6d5895d294edae4a429585e38f17093066bc4a497916131e7db88d772f8",
    "docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md":
        "760a562c15991421e6c1eca2b8f65072d82976a956482c599fdeb0cc1c46b602",
    "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md":
        "cb31edc844c6bc4ee285219a819d2943fd140bf9d70f56d1da2e9e031520db92",
    CODE_V1: "9ef4ede751fcceb51eda1e622deaa62552326e395fdbd647c6989ad32353701f",
}
CANON_V7 = "4ff92c8ef07943e093793c218967be36621410714be9634ccccc3c27811d2b38"
TITRE = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — candidat 2"
MARQ = "<<C7_ET_CODE_T07_26_MODULES>>"
REMPLIS = ["<<MOT_LAZAR_P064>>", "<<MOT_LAZAR_P065>>", "<<ENTROPIE_T07>>", "<<EMPREINTE_CONFIG_T07>>",
           "<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>", "<<GO_ETAPE_A_T07>>", "<<ESSAI_CLC04_T07>>"]
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
GELES_MANDAT = {"G2-01": "Hypothèse", "G2-02": "Prédiction chiffrée et signe attendu", "G2-03": "Métrique", "G2-04": "Métrique",
                "G2-05": "Seuil", "G2-06": "Seuil", "G2-07": "Seuil", "G2-08": "Seuil", "G2-09": "Plan d'analyse",
                "G2-10": "Plan d'analyse", "G2-11": "Plan d'analyse", "G2-12": "Plan d'analyse", "G2-13": "Plan d'analyse",
                "G2-14": "Critères de lecture gelés", "G2-15": "Critères de lecture gelés", "G2-16": "Critères de lecture gelés",
                "G2-17": "Liste d'arrêt"}
NEUVES = ["Table « ce qui change du candidat 1 au candidat 2 »"]
NEUFS = {"plancher_v2.py": "a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796",
         "lecture_v3.py": "ac3666e4003b55629600c4d21db9e9b35086c37325c4f63e6417bca1864c921a",
         "lectures_t07_v2.py": "1f523c07273ae11359ca199056eadbf68cf1448c93e9c43eb2bf4a8a600b5271",
         "plancher_v3.py": "c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8",
         "reextraction_p3_v1.py": "fe9b48e3bdd83e83da29d79947748346ca56be535a8be401ad8f290f553ee8a1",
         "lecture_v4.py": "5cb4c44872472b94d995c9ace11530655539cfc68ec06874e0f6b6d005ae7d19",
         "passe_blanc_v2.py": "66d1b5151c5dd6eb463f37d5f4987abb097afc50f64e2aa9e0adb2b5b40ba974",
         "repli_etapes_v2.py": "70f587da4c68c90f6dcb7970cc4bd4d26d2a41dfdd1475aac255075404c91476"}
DEVIS = ["3,2 à 4,7", "8,6 à 11,6", "5,5 à 7,4", "12,5 à 16,4", "`ANT0` ≤ 3,6 USD", "41 616 s = 11,56 h", "0,45 h"]
PUISSANCE = [("0,6408", "0.6408"), ("0,6058", "0.6058"), ("0,5815", "0.5815"), ("0,6658", "0.6658"), ("0,6387", "0.6387"),
             ("0,6036", "0.6036"), ("0,5793", "0.5793"), ("0,6636", "0.6636"), ("0,6355", "0.6355"), ("0,6004", "0.6004"),
             ("0,6638", "0.6638"), ("0,6292", "0.6292"), ("0,6047", "0.6047"), ("0,6890", "0.6890"),
             ("0,000 / 0,010 / 0,129 / 0,531 / 0,901", "0.000 (0.000) | 0.010 (0.010) | 0.129 (0.161) | 0.531 (0.633) | 0.901"),
             ("0,035 / 0,266 / 0,714 / 0,960 / 0,998", "0.035 (0.040) | 0.266 (0.329) | 0.714 (0.805) | 0.960 (0.985) | 0.998"),
             ("+0,0592", "+0.0592"), ("+0,0942", "+0.0942"), ("+0,0342", "+0.0342"), ("+0,1185", "+0.1185"),
             ("+0,0092", "+0.0092"), ("+0,0442", "+0.0442"), ("−0,0158", "-0.0158"),
             ("0,510 pour k = 2, 0,260 pour k = 4", "| enjeux élevés (figée, P3) | 2 | 0.001 | 0.071 | 0.510"),
             ("0,282 et 0,080", "| tromperie (figée, P3) | 4 | 0.000 | 0.000 | 0.000 | 0.080"),
             ("**0,70 à 0,71**", "0.704"), ("0,047901", "0.047901"), ("0,048676", "0.048676")]
PHRASES = (
    "- **« Au-dessus du plancher »** (**candidat 2** : **règle (a)**", "**800 sondes linéaires aléatoires**",
    "1 bis. **réextraction des jetons d'entraînement des deux sondes figées de P3 et plancher neuf**",
    "**T7-P1 n'est plus une réplication de P3 pour cette sonde**", "« plancher neuf de la sonde figée non établi »",
    "`garde_principale` = « rapportee »", "défaut appliqué le 10 novembre 2026 à 17:13 UTC (R-1902) : oui — constaté par R-2269",
    "défaut appliqué le 10 novembre 2026 à 17:13 UTC (R-1902) : déclarer sans étendre — constaté par R-2269",
    "**chemin final `prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json`**", f"`{CANON_V7}`",
    f"`{ORDRE6}`, sha256 `92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca`", "1 nonies. **Candidat 2",
    "## Table « ce qui change du candidat 1 au candidat 2 »", "reste 1,4 à 1,8 fois le nominal", "**non établi**",
    "**hors de la règle (a), déclarés** : **T4**", "`ENTROPIE_T07` inchangée", "**Candidat 2** : **à contre-lire par une "
    "vérification courte neuve**", "141327499974890102043551261780374423878",
)
ABSENTES = (
    "- Statut : **candidat 1**", "- **« Au-dessus du plancher »** : borne basse de l'intervalle de la sonde",
    "T7-P1, réplication de P3-P3, garde **les mêmes 200 directions que P3**",
    "jeu (`plancher_apparie` pour tirer les 200 directions et les noter à l'étape A)",
    "- **« Non au-dessus »** : borne basse inférieure ou égale au quantile 0,95 du plancher ;",
)


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def plat(s: str) -> str:
    return " ".join(s.split())


def sections(texte: str) -> dict:
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {titre.strip(): corps for titre, corps in zip(morceaux[1::2], morceaux[2::2])}


def section_de(texte: str, debut: int, fin: int) -> set:
    """Sections que touche l'empan [debut, fin) du texte (la section où il commence et celles dont il franchit l'en-tête)."""
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


def ecrire_r12(chemin: Path, octets: bytes, racine: Path) -> bool:
    if chemin.exists():
        if chemin.read_bytes() != octets:
            print(f"ARRÊT (R12) : {chemin.relative_to(racine)} existe et diffère : rien n'est écrasé")
            return False
        print(f"{chemin.relative_to(racine)} déjà écrit, identique")
        return True
    chemin.write_bytes(octets)
    print(f"écrit : {chemin.relative_to(racine)}")
    return True


def vc1(vc: str, ident: str, constat: str) -> tuple:
    m = re.search(rf"\*\*{ident}\*\* \({constat}\)\n\n- ancien : `(.*)`\n- nouveau : `(.*)`\n", vc)
    return m.group(1), m.group(2)


def main(argv: list) -> int:
    if not 1 <= len(argv) <= 2:
        print("usage : RACINE [DOSSIER_TEMPORAIRE]", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    dossier = (Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-c2-"))).resolve()
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

    # ------------------------------------------------------------------------------------------------------ configuration
    print("\n# configuration v7")
    c5 = json.loads((racine / V5).read_text(encoding="utf-8"))
    c7 = json.loads((racine / V7).read_text(encoding="utf-8"))
    diff_cles = sorted(k for k in set(c5) | set(c7) if c5.get(k, "∅") != c7.get(k, "∅"))
    attendu_pf = {"methode": "reextraction_p3_v1", "n_p3": 200,
                  "tolerances": {"processeur": 1e-06, "carte_sonde": 0.01, "carte_directions": 0.1}, "garde_principale": "rapportee"}
    ok = (diff_cles == ["methode_plancher", "n_plancher", "plancher_figees"] and c7["n_plancher"] == 800 and c5["n_plancher"] == 200
          and c7["methode_plancher"] == "difference_appariee_percentile" and c7["plancher_figees"] == attendu_pf
          and c7["entropie"] == c5["entropie"] == 141327499974890102043551261780374423878)
    print(f"clés qui changent de la v5 à la v7 : {diff_cles} ; n_plancher {c5['n_plancher']} → {c7['n_plancher']} ; entropie "
          f"inchangée : {c7['entropie'] == c5['entropie']} : {ok}")
    if not ok:
        defauts.append("configuration v7 ≠ v5 plus les trois clés")
    copie = dossier / "src-0d0c5da4"
    noms = git(racine, "ls-tree", "-r", "--name-only", COMMIT, "src").stdout.decode().split()
    for nom in noms:
        cible = copie / nom
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_bytes(git(racine, "show", f"{COMMIT}:{nom}").stdout)
    env = dict(os.environ, PYTHONPATH=str(copie / "src"), PYTHONDONTWRITEBYTECODE="1")
    r4 = subprocess.run([sys.executable, "-B", "-m", "controle_ia.t07.lecture_v4", "empreinte-config", str(racine / V7)],
                        capture_output=True, env=env, cwd=str(copie))
    r2 = subprocess.run([sys.executable, "-B", "-m", "controle_ia.t07.lecture_v2", "empreinte-config", str(racine / V7)],
                        capture_output=True, env=env, cwd=str(copie))
    s4 = r4.stdout.decode().strip()
    ok = r4.returncode == 0 and s4 == CANON_V7 and "800" in r2.stdout.decode() + r2.stderr.decode() and s4 not in r2.stdout.decode()
    print(f"module recopié au commit {COMMIT[:8]} ({len(noms)} fichiers) ; `lecture_v4 empreinte-config` : code {r4.returncode}, {s4} ; "
          f"`lecture_v2 empreinte-config` : code {r2.returncode}, « {(r2.stdout.decode() + r2.stderr.decode()).strip()[:60]} » : {ok}")
    if not ok:
        defauts.append("empreinte canonique de la v7 ou refus de la v2")

    # ------------------------------------------------------------------------------------------------------ couples
    texte1 = (racine / C1).read_bytes().decode("utf-8")
    couples = json.loads((racine / COUPLES).read_text(encoding="utf-8"))
    vc = (racine / VC).read_text(encoding="utf-8")
    mien = {c["id"]: c for c in couples}
    for ident, constat in (("VC1-A", "VC1-07"), ("VC1-B", "VC1-08")):
        a, n = vc1(vc, ident, constat)
        ok = ident in mien and (mien[ident]["ancien"], mien[ident]["nouveau"]) == (a, n)
        print(f"{ident} tel qu'écrit dans la vérification courte : {ok}")
        if not ok:
            defauts.append(f"{ident} différent de la vérification courte")
    ids = [c["id"] for c in couples]
    if len(set(ids)) != len(ids):
        print("ARRÊT : identifiants en double")
        return 1
    print(f"\n# application ({len(couples)} couples) (id ; ligne ; sections touchées ; gelée)")
    t = texte1
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
    texte2 = t
    geles_faits = {c["id"]: c["gelee"] for c in couples if c["gelee"] is not None}
    print(f"couples gelés : {len(geles_faits)} ; égaux au mandat (G2-01 à G2-17, sections déclarées) : {geles_faits == GELES_MANDAT}")
    if geles_faits != GELES_MANDAT:
        defauts.append("couples gelés ≠ mandat")
    octets = texte2.encode("utf-8")
    print()
    if not ecrire_r12(racine / C2, octets, racine):
        return 1
    print(f"candidat 2 : {sha(octets)} ; {texte2.count(chr(10))} lignes")

    # ------------------------------------------------------------------------------------------------------ vérifications
    print("\n# vérifications")
    statut = next(l for l in texte2.split("\n") if l.startswith("- Statut :"))
    ok = texte2.split("\n", 1)[0] == TITRE and statut.startswith("- Statut : **candidat 2**")
    print(f"(1) titre et premier statut : {ok}")
    if not ok:
        defauts.append("titre ou statut")
    s1, s2 = sections(texte1), sections(texte2)
    print("(2) empan gelé (couples gelés défaits dans l'ordre inverse, section par section) :")
    for k in s1:
        if not gelee(k):
            continue
        x = s2.get(k)
        if x is None:
            defauts.append(f"section gelée « {k} » disparue")
            continue
        miens = [c for c in couples if c["gelee"] is not None and k.startswith(c["gelee"])]
        for c in reversed(miens):
            if x.count(c["nouveau"]) != 1:
                defauts.append(f"{c['id']} : « nouveau » présent {x.count(c['nouveau'])} fois dans « {k[:30]} »")
            x = x.replace(c["nouveau"], c["ancien"], 1)
        egal = x == s1[k]
        d = lignes_diff(s1[k], s2[k])
        print(f"    « {k[:48]} » : couples {[c['id'] for c in miens]} ; {len(d)} lignes de différence ; égale au candidat 1 une fois "
              f"défaite : {egal}")
        if not egal:
            defauts.append(f"section gelée « {k[:40]} » changée hors des couples déclarés")
    neuves = [k for k in s2 if k not in s1]
    disparues = [k for k in s1 if k not in s2]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues}")
    if neuves != NEUVES or disparues:
        defauts.append("sections neuves ou disparues inattendues")
    restes = {m: texte2.count(m) for m in sorted(set(GABARIT.findall(texte2)))}
    presents = [m for m in REMPLIS if m in texte2]
    print(f"(4) marqueurs restants : {restes} ; remplis encore présents : {presents}")
    if restes != {MARQ: 1} or presents:
        defauts.append("marqueurs")
    pb = problemes(racine / C2)
    attendu = [f"marqueurs de gabarit restants : {MARQ}"]
    factice = dossier / "T0.7-sondes-v0-v1-candidat2-valeur-factice.md"
    factice.write_text(texte2.replace(MARQ, "valeur-factice-c7-et-code-t07"), encoding="utf-8")
    pf = problemes(factice)
    print(f"(5) controle_ia.prereg.problemes(candidat 2) : {pb} ; à valeur factice : {pf}")
    if pb != attendu or pf:
        defauts.append("problemes")
    doc = git(racine, "show", f"{COMMIT}:src/controle_ia/t07/plancher_v2.py").stdout.decode("utf-8")
    regle = plat(re.search(r"\*\*Règle \(a\)\*\* : (.*?de D\*\.)", doc, re.S).group(1))
    ok = sha(doc.encode("utf-8")) == NEUFS["plancher_v2.py"] and f"« {regle} »" in plat(texte2)
    print(f"(6) règle (a) citée telle que l'écrit plancher_v2.py au commit {COMMIT[:8]} : {ok}")
    if not ok:
        defauts.append("règle (a) non citée telle quelle")
    manq = []
    for nom, h in NEUFS.items():
        if sha(git(racine, "show", f"{COMMIT}:src/controle_ia/t07/{nom}").stdout) != h or f"`src/controle_ia/t07/{nom}` `{h}`" not in texte2:
            manq.append(nom)
    v1 = json.loads((racine / CODE_V1).read_text(encoding="utf-8"))["fichiers"]
    for f, h in v1.items():
        if f"`{f}` `{h}`" not in texte2 or sha(git(racine, "show", f"{COMMIT}:{f}").stdout) != h:
            manq.append(f)
    n_mod = len([x for x in git(racine, "ls-tree", "--name-only", COMMIT, "src/controle_ia/t07/").stdout.decode().split() if x.endswith(".py")])
    print(f"(7) module au commit {COMMIT[:8]} : {n_mod} fichiers ; huit neufs et dix-huit anciens à leur empreinte et cités : "
          f"{not manq}{' ; manquants : ' + repr(manq) if manq else ''}")
    if manq or n_mod != 26:
        defauts.append("vingt-six modules")
    ordre = (racine / ORDRE6).read_text(encoding="utf-8")
    manq = [x for x in DEVIS if x not in texte2 or x not in ordre]
    print(f"(8) devis communs au candidat 2 et à l'ordre, brouillon 6 : {not manq}{' ; manquants : ' + repr(manq) if manq else ''}")
    if manq:
        defauts.append("devis")
    sortie = (racine / PUISS_TXT).read_text(encoding="utf-8")
    manq = [(a, b) for a, b in PUISSANCE if a not in texte2 or b not in sortie]
    print(f"(9) puissance : {len(PUISSANCE) - len(manq)} nombres sur {len(PUISSANCE)} cités et présents dans la sortie versée"
          f"{' ; manquants : ' + repr(manq) if manq else ''}")
    if manq:
        defauts.append("puissance")
    reg = (racine / "registres/decisions.md").read_text(encoding="utf-8")
    l2299 = next(l for l in reg.split("\n") if l.startswith("| R-2299 |"))
    res = re.search(r"\*\*Réserves\*\* : (.*? des aires un peu plus hautes)\.", l2299).group(1)
    audit = (racine / AUDIT).read_text(encoding="utf-8")
    s7 = audit[audit.index("## 7. Réserves"):audit.index("## 8.")]
    r1 = plat(re.search(r"\*\*Réserve d'audit 1 — niveau de la règle de P3-P3\*\* : « (.*?) »\.", s7, re.S).group(1))
    r2_ = plat(re.search(r"\*\*Réserve d'audit 2 — puissance du nul\*\* : « (.*?) »\.", s7, re.S).group(1))
    n_res = texte2.count(f"« {res} »")
    ok = n_res == 4 and r1 in plat(texte2) and r2_ in plat(texte2)
    print(f"(10) réserves de P3 : forme du registre (R-2299) jointe {n_res} fois (Hypothèse, Prédiction, L4, Puissance) ; forme de "
          f"l'audit (réserves 1 et 2) en « Puissance » : {ok}")
    if not ok:
        defauts.append("réserves de P3")
    plat2 = plat(texte2)
    manquantes = [ph for ph in PHRASES if plat(ph) not in plat2]
    presentes = [ph for ph in ABSENTES if ph in texte2]
    print(f"(11) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)}{' ; manquantes : ' + repr(manquantes) if manquantes else ''} ; "
          f"passages retirés encore présents : {presentes}")
    if manquantes or presentes:
        defauts.append("phrases")
    d = lignes_diff(texte1, texte2)
    print(f"(12) différentiel candidat 1 → candidat 2 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées ; {len(couples)} couples, dont {len(geles_faits)} gelés")
    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
