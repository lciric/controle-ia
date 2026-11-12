"""T0.7 sondes v0, candidat 1 : configuration v5, application des couples du candidat 1 au brouillon 22, et vérifications (v1).

Rédacteur du candidat 1 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 10 novembre 2026 ;
consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-candidat1-v1.md` (`017361bd…`),
méthode du script du brouillon 22 (`brouillons/T0.7-sondes-v0-v1-brouillon22-faire-v1.py`, `e586bf36…`). Bibliothèque standard,
plus `controle_ia.prereg`, `controle_ia.t07.lecture_v2` et `controle_ia.t07.registre_v1` du dépôt (lus dans RACINE/src) et `git` en
lecture (`git show`, `git rev-parse`, `git merge-base --is-ancestor`, `git diff --quiet` entre deux commits) ; aucun réseau ; aucune
écriture hors du candidat, de la configuration v5 et du dossier temporaire.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie les empreintes de ses entrées (brouillon 22, contre-lecture orchestrée et ses couples, ordre d'exécution brouillon 5 et la
   contre-lecture de son brouillon 4, configuration v4, couples du candidat 1) ;
2. écrit la configuration v5 (v4, seule la clé `entropie` remplie ; R12 : refuse d'écraser un fichier différent), la passe à
   `lecture_v2.exiger_configuration`, compare son empreinte canonique et celle du fichier aux valeurs écrites, rejoue
   `lecture_v2 empreinte-config` ;
3. contrôle que CLO-01, CLO-02 et CLO-04 à CLO-10 sont ceux du fichier de la contre-lecture (« ancien » et « nouveau » égaux) et que
   CLO-03 n'est pas appliqué ;
4. applique les couples dans l'ordre ; chaque « ancien » présent exactement une fois au moment de son application et différent de son
   « nouveau », clés exactement `id`, `section`, `motif`, `ancien`, `nouveau` ; sinon arrêt (code 1), rien n'est écrit ; seul CLO-08
   peut toucher l'empan gelé « Hypothèse » à « Liste d'arrêt » (et seulement la « Liste d'arrêt ») ;
5. écrit `brouillons/T0.7-sondes-v0-v1-candidat1.md` (R12) ;
6. vérifie : (1) titre et premier statut ; (2) empan gelé égal octet pour octet au brouillon 22, hors de la « Liste d'arrêt », égale
   une fois CLO-08 défait ; (3) sections neuves (une), disparues (aucune) ; (4) deux marqueurs restants, une occurrence chacun ;
   marqueurs remplis absents, valeurs présentes ; (5) `problemes` réduit à la ligne des deux marqueurs, vide à valeurs factices ;
   (6) essais (empreintes aux commits cités et à la tête, ancêtres, arbres de la mesure, `src` égal à `37485ce5`) ; (7) devis : table
   du § 6 de l'ordre relue, nombres présents dans le candidat ; (8) cellules `AUDIT-FUITES-T07` et `CONSIGNE-AUDIT-FUITES-T07`
   inchangées ; dix-huit empreintes du code présentes ; (9) registre et classement de `GEL-T08` ; (10) phrases exigées présentes,
   passages retirés absents ; (11) différentiel compté.
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

SHA_ENTREES = {
    "brouillons/T0.7-sondes-v0-v1-brouillon22.md": "8b84cba5bd527e10a3b835ebc0caa7e7da0e31af503904e51621d752d65f0a37",
    "prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md":
        "47537dfa7d4f97d0266f72eb3d791996d2ea0aa8f35a098a721c1d72ab251a60",
    "prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1-couples.json":
        "4c9407146be479f202ed48d0e7962085162f25c751ce701d7d30eea6ab14da7c",
    "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md": "d0b75d161e80efbd4b1e5e6ca8f2cc49476bf90801cae57617b2cc553a92108b",
    "prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md":
        "88ea9f0661e07a7840b10c060f1488a479efa9d01e82bbdbb643b72329c74704",
    "brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json":
        "3d19b08cbeda6f30c36303896de5e2e8e692b6f9ba0d3b54d62955a38f2c4c9b",
    "brouillons/T0.7-sondes-v0-v1-candidat1-pieces/T0.7-sondes-v0-v1-candidat1-couples-v1.json": "f73c58820559d5ebdffc02835d13879af92a48b7499fe67dba4ded38ca7b513e",
    "registres/code-t07/CODE-T07-v1.json": "9ef4ede751fcceb51eda1e622deaa62552326e395fdbd647c6989ad32353701f",
}
B22 = "brouillons/T0.7-sondes-v0-v1-brouillon22.md"
CLO_JSON = "prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1-couples.json"
ORDRE = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md"
V4 = "brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json"
COUPLES = "brouillons/T0.7-sondes-v0-v1-candidat1-pieces/T0.7-sondes-v0-v1-candidat1-couples-v1.json"
V5 = "brouillons/T0.7-sondes-v0-v1-candidat1-pieces/configuration-t07-v5.json"
CANDIDAT = "brouillons/T0.7-sondes-v0-v1-candidat1.md"
CODE_V1 = "registres/code-t07/CODE-T07-v1.json"

ENTROPIE = 141327499974890102043551261780374423878
CANON_V4 = "f1e3133b9733039ad3473a732dcdfee6375c4f2d9a310f0d8ca11505560cfb61"
CANON_V5 = "9d138bf3a635dbc0207a6bcf5cf7e436c34d3af8ce2866f96025a594cc04c681"
FICHIER_V5 = "4be50447d1063015aa8ad99970d7e803765d85964d2b58010f5731bcd8c4ff46"
CHEMIN_FINAL = "prereg/T0.7-sondes-v0-v1-configuration-t07-v5.json"
SIX_CHEMINS = ["diag/20261019-230011-p3-reel/sondes-figees.json", "donnees/20261007-082440-t05-extraction/taches-entrainement.json",
               "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz", "donnees/T0.7-faits-repe-v1/facts_true_false.csv",
               "donnees/T0.7-models-under-pressure-v1/training/train.jsonl", "runs/20261019-230011-p3-reel/manifeste.json"]

TITRE = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — candidat 1"
RESTANTS = ["<<MOT_LAZAR_P064>>", "<<MOT_LAZAR_P065>>"]
REMPLIS = ["<<ENTROPIE_T07>>", "<<EMPREINTE_CONFIG_T07>>", "<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>", "<<GO_ETAPE_A_T07>>",
           "<<ESSAI_CLC04_T07>>"]
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
TOUCHES_GELEES = {"CLO-08": "Liste d'arrêt"}
CLO_APPLIQUES = ["CLO-01", "CLO-02", "CLO-04", "CLO-05", "CLO-06", "CLO-07", "CLO-08", "CLO-09", "CLO-10"]
NEUVES = ["Table « ce qui change du 22 au candidat 1 »"]

C37 = "37485ce50601b7d7ff9035bc34c734ec689ca731"
ESSAIS = [  # (commit de l'essai, fusion dans main, fichier, sha256)
    ("31b55c92393173d01153e4c8a5a9f0d69365ce81", "24697e9be4f6e85dc2f989403944ccb35c8fe2b9",
     "tests/test_t07_ouvrir_reel_concepts_v1.py", "6192a821773a661d9fc983d65bca03b7321e4be607d852e5ead1567b4e67505d"),
    ("2c8ab779ca6df361d562e120ba34045be675853a", "9e128befc2dea336370d50cb872f03e1889322ee",
     "tests/test_t07_tirages_degeneres_v1.py", "c68fd68fc9e747aa34ed0853e1da6c8e0124ec0c3197287c40faa2ae746c5140"),
]
ARBRES = {"tests": "79230a584e8675f1771fd4f0a9315de71c2bcbdc", "src": "744a9e16f1635ff402e798b4ac868a57311e44b8"}
ATT = "346 passed, 2 skipped, 4 xfailed"
DEVIS_ORDRE = [("0,10", "0,30"), ("0,10", "0,45"), ("0,15", "0,50"), ("0,25", "0,60"), ("0,01", "0,05"), ("0,10", "1,00"),
               ("0,10", "0,40"), ("0,10", "0,20"), ("2,00 à 3,50", "4,00 à 7,00"), ("0,10", "0,40"),
               ("**3,0 à 4,5**", "**7,9 à 10,9**")]
DEVIS_TEXTE = ["0,10 h, 0,30 au pire", "0,10, 0,45", "0,15, 0,50", "0,25, 0,60", "0,01, 0,05", "0,10, 1,00", "0,10, 0,40",
               "0,10, 0,20", "2,00 à 3,50, 4,00 à 7,00", "3,0 à 4,5 h attendues, 7,9 à 10,9 h au pire"]
DEVIS_COMMUNS = ["3,9 à 5,9 USD", "10,3 à 14,2 USD", "24 Go × 0,05 USD", "5,2 à 7,1 USD", "11,6 à 15,5 USD", "716,0 s",
                 "`ANT0` ≤ 4,5 USD", "3,2 USD", "1,1 h", "≤ 0,08 USD de l'heure", "`20 − ANT0 − 1,30`"]
MINUTERIE_COMMUNS = ["39 240 s", "10,9 h", "HMAX"]
CELLULES = {"AUDIT-FUITES-T07": "381a72d5b52c1534d116c81b71568dd4728d1a4d90a22a25e99109508e30fede",
            "CONSIGNE-AUDIT-FUITES-T07": "95c8b659c54f218a903e1d0359a5a4a9ca9bd2e81072741803861a4bb4fa1121"}
REGISTRE_ATTENDU = [
    "| SCELLEMENT-JEUX-T07-JD | 2026-11-10T08:22:50Z | donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl | 32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228 |",
    "| SCELLEMENT-JEUX-T07-JA | 2026-11-10T08:22:50Z | donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl | 5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf |",
    "| SCELLEMENT-T08-BASE-A | 2026-11-10T12:21:55Z | prereg/T0.8-base-A-mots-et-cout-v1.md | 72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d |",
    "| GEL-T08 | 2026-11-10T14:57:57Z | brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md | 7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5 |",
]
PHRASES = (
    "au plus 12 h, bornée par la dépense", "**Réserve CLE-12, déclarée**", "**détruit une étape ouverte**",
    "n'a jamais été mesurée", "**CLO-03 non appliqué**", "21. **Essais versés avant C7 (candidat 1", f"`{ATT}`",
    f"`{ENTROPIE}`", f"`{CANON_V5}`", f"**chemin final `{CHEMIN_FINAL}`**", FICHIER_V5,
    "`docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md`, sha256 `d0b75d161e80efbd4b1e5e6ca8f2cc49476bf90801cae57617b2cc553a92108b`",
    "`GO-2026-11-10-06` (extension de `GO-2026-11-10-04` à la variante B, voie nominale ; 20 USD au total sous les deux lignes)",
    "`31b55c92393173d01153e4c8a5a9f0d69365ce81`", "`24697e9be4f6e85dc2f989403944ccb35c8fe2b9`",
    "`6192a821773a661d9fc983d65bca03b7321e4be607d852e5ead1567b4e67505d`", "`2c8ab779ca6df361d562e120ba34045be675853a`",
    "`c68fd68fc9e747aa34ed0853e1da6c8e0124ec0c3197287c40faa2ae746c5140`", "retrouvée sous Python 3.11.17**", "Python 3.13.16",
    "`79230a584e8675f1771fd4f0a9315de71c2bcbdc`", "`744a9e16f1635ff402e798b4ac868a57311e44b8`", "1 octies. **Candidat 1",
    "**Clés présentes au candidat 1**", "- **Contre-lectures orchestrées du brouillon 22**",
    "- **Contre-lecture R2 de l'ordre d'exécution de l'étape A, brouillon 4**", "**C7 n'est pas fixé ici**",
    "**état au candidat 1** : brouillon 5", "CLE-04, majeur",
)
ABSENTES = (
    "destruction par son identifiant à la création + 12 h",
    "la minuterie (création + 12 h) ne la détruisant",
    "**Devis** (ordre d'exécution, brouillon 3",
    "instance du programme déjà sur le compte, carte H200",
    "à trancher dans l'ordre d'exécution.",
    "**brouillon 22, écart déclaré**",
    "les quatorze fichiers `tests/test_t07_*.py` du commit cité par `CODE-T07`",
    "de la ligne `AUDIT-FUITES-T07` du brouillon 22 (cellule et empreinte)",
)


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sections(texte: str) -> dict:
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {titre.strip(): corps for titre, corps in zip(morceaux[1::2], morceaux[2::2])}


def section_de(texte: str, position: int) -> str:
    nom = "(avant la première section)"
    for m in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M):
        if m.start() <= position:
            nom = m.group(1)
    return nom


def gelee(nom: str) -> bool:
    return any(nom.startswith(g) for g in EMPAN_GELE)


def lignes_diff(a: str, b: str) -> list:
    return [l for l in difflib.unified_diff(a.split("\n"), b.split("\n"), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]


def cellule(texte: str, cle: str) -> str:
    ls = [l for l in texte.split("\n") if l.startswith(f"| `{cle}`")]
    if len(ls) != 1:
        raise ValueError(f"ligne {cle} : {len(ls)} occurrences")
    c = re.split(r"(?<!\\)\|", ls[0])[1:-1]
    if len(c) != 4:
        raise ValueError(f"ligne {cle} : {len(c)} cellules")
    return c[1].strip()


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


def appliquer(t: str, couples: list) -> tuple[str | None, list]:
    print(f"\n# application, candidat 1 ({len(couples)} couples) (id ; occurrences de l'« ancien » ; ligne ; section ; empan gelé)")
    gelees = []
    for c in couples:
        if sorted(c) != ["ancien", "id", "motif", "nouveau", "section"]:
            print(f"ARRÊT : {c.get('id')} : clés {sorted(c)}")
            return None, gelees
        n = t.count(c["ancien"])
        if n != 1 or c["ancien"] == c["nouveau"]:
            print(f"ARRÊT : {c['id']} : « ancien » présent {n} fois (1 attendu), ou égal au « nouveau » ; rien n'est écrit")
            return None, gelees
        p = t.index(c["ancien"])
        sec = section_de(t, p)
        g = gelee(sec)
        if g:
            gelees.append(c["id"])
            if c["id"] not in TOUCHES_GELEES or not sec.startswith(TOUCHES_GELEES[c["id"]]):
                print(f"ARRÊT : {c['id']} touche la section gelée « {sec[:60]} » sans déclaration")
                return None, gelees
        print(f"{c['id']} ; 1 ; l. {t.count(chr(10), 0, p) + 1} ; {sec[:70]} ; {'OUI' if g else 'non'}")
        t = t.replace(c["ancien"], c["nouveau"], 1)
    return t, gelees


def main(argv: list) -> int:
    if not 1 <= len(argv) <= 2:
        print("usage : RACINE [DOSSIER_TEMPORAIRE]", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # noqa: E402
    from controle_ia.t07 import lecture_v2 as l2  # noqa: E402
    from controle_ia.t07 import registre_v1 as rg  # noqa: E402

    defauts = []
    for rel, attendu in SHA_ENTREES.items():
        e = sha((racine / rel).read_bytes())
        if e != attendu:
            print(f"ARRÊT : empreinte de {rel} {e} ≠ {attendu}")
            return 1
        print(f"{rel} : {e} (égale)")

    # ------------------------------------------------------------------------------------------------- configuration v5
    print("\n# configuration v5")
    b4 = (racine / V4).read_bytes()
    ancien_cfg, nouveau_cfg = b'"entropie": null,', f'"entropie": {ENTROPIE},'.encode("utf-8")
    if b4.count(ancien_cfg) != 1:
        print("ARRÊT : la v4 ne porte pas exactement une fois « \"entropie\": null, »")
        return 1
    b5 = b4.replace(ancien_cfg, nouveau_cfg, 1)
    c4, c5 = json.loads(b4.decode("utf-8")), json.loads(b5.decode("utf-8"))
    diff_cles = sorted(k for k in set(c4) | set(c5) if c4.get(k, "∅") != c5.get(k, "∅"))
    print(f"clés qui changent de la v4 à la v5 : {diff_cles} ; entropie = {c5['entropie']} ({type(c5['entropie']).__name__})")
    if diff_cles != ["entropie"] or c5["entropie"] != ENTROPIE or list(c4) != list(c5):
        defauts.append("configuration : autre chose que l'entropie change")
    try:
        l2.exiger_configuration(c4)
        print("v4 : exiger_configuration passe (inattendu)")
        defauts.append("v4 acceptée")
    except Exception as err:  # noqa: BLE001
        print(f"v4 : refusée par exiger_configuration ({type(err).__name__} : {str(err)[:90]}…) (attendu)")
    try:
        l2.exiger_configuration(c5)
        print("v5 : exiger_configuration passe")
    except Exception as err:  # noqa: BLE001
        print(f"v5 : REFUS {type(err).__name__} : {err}")
        defauts.append("v5 refusée")
    k4, k5, f5 = l2.empreinte_canonique(c4), l2.empreinte_canonique(c5), sha(b5)
    print(f"empreinte canonique v4 {k4} (attendue {CANON_V4[:8]}…) ; v5 {k5} (attendue {CANON_V5[:8]}…) ; fichier v5 {f5} "
          f"(attendu {FICHIER_V5[:8]}…)")
    if (k4, k5, f5) != (CANON_V4, CANON_V5, FICHIER_V5):
        defauts.append("empreintes de la configuration")
    chemins = sorted({v["chemin"] for v in _dicts(c5) if isinstance(v.get("chemin"), str)})
    print(f"chemins cités par la v5 (préalable P12 de l'ordre) : {len(chemins)} ; égaux aux six de la v4 : {chemins == SIX_CHEMINS}")
    if chemins != SIX_CHEMINS or c5["code_t07_exige"] is not True or c5["preenregistrement"] != "prereg/T0.7-sondes-v0-v1.md":
        defauts.append("chemins cités, code_t07_exige ou preenregistrement")
    if not ecrire_r12(racine / V5, b5, racine):
        return 1
    env = dict(os.environ, PYTHONPATH=str(racine / "src"), PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "-B", "-m", "controle_ia.t07.lecture_v2", "empreinte-config", str(racine / V5)],
                       capture_output=True, env=env, cwd=str(racine / "src"))
    sortie_cli = r.stdout.decode().strip()
    print(f"`lecture_v2 empreinte-config {V5}` : code {r.returncode}, {sortie_cli}")
    if r.returncode != 0 or sortie_cli != CANON_V5:
        defauts.append("sous-commande empreinte-config")

    # --------------------------------------------------------------------------------------------- couples, application
    texte22 = (racine / B22).read_bytes().decode("utf-8")
    couples = json.loads((racine / COUPLES).read_text(encoding="utf-8"))
    clo = {c["id"]: c for c in json.loads((racine / CLO_JSON).read_text(encoding="utf-8"))}
    ids = [c["id"] for c in couples]
    mien = {c["id"]: c for c in couples}
    ecarts_clo = [i for i in CLO_APPLIQUES if i not in mien or (mien[i]["ancien"], mien[i]["nouveau"]) !=
                  (clo[i]["ancien"], clo[i]["nouveau"])]
    print(f"\nCLO appliqués tels qu'écrits : {[i for i in CLO_APPLIQUES if i not in ecarts_clo]} ; écarts : {ecarts_clo} ; "
          f"CLO-03 dans les couples : {'CLO-03' in ids} ; ids uniques : {len(set(ids)) == len(ids)}")
    if ecarts_clo or "CLO-03" in ids or len(set(ids)) != len(ids):
        defauts.append("couples CLO")
    texte_c1, gelees = appliquer(texte22, couples)
    if texte_c1 is None:
        return 1
    print(f"couples qui touchent l'empan gelé : {gelees} (déclarés : {sorted(TOUCHES_GELEES)})")
    if sorted(gelees) != sorted(TOUCHES_GELEES):
        defauts.append("touches de l'empan gelé ≠ celles déclarées")
    octets = texte_c1.encode("utf-8")
    print()
    if not ecrire_r12(racine / CANDIDAT, octets, racine):
        return 1
    print(f"candidat 1 : {sha(octets)} ; {texte_c1.count(chr(10))} lignes")

    # ------------------------------------------------------------------------------------------------------ vérifications
    print("\n# vérifications")
    premiere = texte_c1.split("\n", 1)[0]
    statut = next(l for l in texte_c1.split("\n") if l.startswith("- Statut :"))
    ok = premiere == TITRE and statut.startswith("- Statut : **candidat 1**")
    print(f"(1) titre et premier statut au candidat 1 : {ok}")
    if not ok:
        defauts.append("titre ou statut")

    s22, s1 = sections(texte22), sections(texte_c1)
    neuves = [k for k in s1 if k not in s22]
    disparues = [k for k in s22 if k not in s1]
    changees = [k for k in s22 if k in s1 and s22[k] != s1[k]]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues}")
    if neuves != NEUVES or disparues:
        defauts.append("sections neuves ou disparues inattendues")
    print(f"    sections changées ({len(changees)}) :")
    for k in changees:
        print(f"      - {k[:90]}{'  [EMPAN GELÉ]' if gelee(k) else ''}")
    print("(2) empan gelé :")
    for k in s22:
        if not gelee(k):
            continue
        x1 = s1[k]
        for ident, prefixe in TOUCHES_GELEES.items():
            if k.startswith(prefixe):
                x1 = x1.replace(mien[ident]["nouveau"], mien[ident]["ancien"], 1)
        egal = x1 == s22[k]
        d = lignes_diff(s22[k], s1[k])
        print(f"    « {k[:45]} » : {len(d)} lignes de différence ; égale au brouillon 22 (CLO-08 défait s'il y a lieu) : {egal}")
        for l in d:
            print(f"      {l[:260]}{' […]' if len(l) > 260 else ''}")
        if not egal or (d and not k.startswith("Liste d'arrêt")):
            defauts.append(f"empan gelé « {k[:40]} » changé hors du couple déclaré")

    restes = {m: texte_c1.count(m) for m in sorted(set(GABARIT.findall(texte_c1)))}
    print(f"(4) marqueurs restants : {len(restes)} : {restes}")
    if sorted(restes) != RESTANTS or any(v != 1 for v in restes.values()):
        defauts.append(f"marqueurs restants {restes} ≠ {RESTANTS}, une occurrence chacun")
    absents = [m for m in REMPLIS if m in texte_c1]
    print(f"    marqueurs remplis encore présents entre chevrons : {absents}")
    if absents:
        defauts.append("marqueurs remplis encore présents")

    p = problemes(racine / CANDIDAT)
    attendu = [f"marqueurs de gabarit restants : {', '.join(RESTANTS)}"]
    print(f"(5) controle_ia.prereg.problemes(candidat 1) : {p}")
    if p != attendu:
        defauts.append("problemes ≠ la seule ligne des deux marqueurs")
    dossier = Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-c1-factice-"))
    dossier.mkdir(parents=True, exist_ok=True)
    factice = texte_c1
    for m in RESTANTS:
        factice = factice.replace(m, "valeur-factice-" + m.strip("<>").lower())
    copie = dossier / "T0.7-sondes-v0-v1-candidat1-valeurs-factices.md"
    copie.write_text(factice, encoding="utf-8")
    pf = problemes(copie)
    print(f"    à valeurs factices ({copie}) : problemes = {pf}")
    if pf:
        defauts.append("problemes non vide à valeurs factices")

    print("(6) essais versés avant C7 :")
    for commit, fusion, chemin, attendu_sha in ESSAIS:
        h_c = sha(git(racine, "show", f"{commit}:{chemin}").stdout)
        h_t = sha(git(racine, "show", f"HEAD:{chemin}").stdout)
        anc = [git(racine, "merge-base", "--is-ancestor", x, "HEAD").returncode == 0 for x in (commit, fusion)]
        parent = git(racine, "rev-parse", f"{fusion}^2").stdout.decode().strip() == commit
        ok = h_c == h_t == attendu_sha and all(anc) and parent
        print(f"    {chemin} : au commit {commit[:8]} {h_c[:8]}…, à la tête {h_t[:8]}… (attendu {attendu_sha[:8]}…) ; commit et "
              f"fusion {fusion[:8]} ancêtres de la tête : {anc} ; fusion de ce commit : {parent} : {ok}")
        if not ok:
            defauts.append(f"essai {chemin}")
    tete = git(racine, "rev-parse", "HEAD").stdout.decode().strip()
    arbres = {k: git(racine, "rev-parse", f"HEAD:{k}").stdout.decode().strip() for k in ARBRES}
    src_egal = git(racine, "diff", "--quiet", C37, "HEAD", "--", "src").returncode == 0
    n_t07 = sum(1 for l in git(racine, "ls-tree", "--name-only", "HEAD", "tests/").stdout.decode().split("\n")
                if l.startswith("tests/test_t07_"))
    print(f"    tête {tete[:8]} : arbres {arbres} (mesure : {ARBRES}) : {arbres == ARBRES} ; `src` égal à {C37[:8]} : {src_egal} ; "
          f"fichiers tests/test_t07_* : {n_t07} (dix-sept attendus)")
    if arbres != ARBRES or not src_egal or n_t07 != 17:
        defauts.append("arbres, src ou compte des essais à la tête")

    ordre = (racine / ORDRE).read_text(encoding="utf-8")
    s6 = ordre[ordre.index("## 6. Devis"):ordre.index("## 7. Arrêts")]
    rangs = [tuple(x.strip() for x in l.split("|")[2:4]) for l in s6.split("\n") if l.startswith("| ") and "---" not in l][1:]
    i0 = texte_c1.index("**Devis** (**candidat 1**, CLE-09")
    devis = texte_c1[i0:texte_c1.index("aucune règle de ce texte ne change.", i0)]
    manq_t = [x for x in DEVIS_TEXTE if x not in devis]
    manq_c = [x for x in DEVIS_COMMUNS if x not in devis or x not in ordre]
    i1 = texte_c1.index("**minuterie** : destruction par son identifiant à `ECH`")
    minuterie = texte_c1[i1:texte_c1.index("tant que le conteneur tourne", i1)]
    manq_c += [x for x in MINUTERIE_COMMUNS if x not in minuterie or x not in ordre]
    print(f"(7) devis : table du § 6 de l'ordre relue ({len(rangs)} lignes) égale à celle recopiée : {rangs == DEVIS_ORDRE} ; "
          f"nombres par phase présents dans le candidat : {not manq_t}{' ; manquants : ' + repr(manq_t) if manq_t else ''} ; nombres "
          f"communs à l'ordre et au candidat (devis et minuterie) : {not manq_c}{' ; manquants : ' + repr(manq_c) if manq_c else ''}")
    if rangs != DEVIS_ORDRE or manq_t or manq_c:
        defauts.append("devis")

    for cle, attendu_c in CELLULES.items():
        h22, h1 = sha(cellule(texte22, cle).encode("utf-8")), sha(cellule(texte_c1, cle).encode("utf-8"))
        ok = h22 == h1 == attendu_c
        print(f"(8) cellule {cle} : brouillon 22 {h22[:8]}…, candidat 1 {h1[:8]}… (attendu {attendu_c[:8]}…) : {ok}")
        if not ok:
            defauts.append(f"cellule {cle}")
    fichiers_v1 = json.loads((racine / CODE_V1).read_text(encoding="utf-8"))["fichiers"]
    manq = [f for f, h in fichiers_v1.items() if f"`{f}` `{h}`" not in texte_c1]
    print(f"    dix-huit empreintes du code ({len(fichiers_v1)} dans {CODE_V1}) présentes au candidat : {not manq}"
          f"{' ; manquantes : ' + repr(manq) if manq else ''}")
    if manq or len(fichiers_v1) != 18:
        defauts.append("empreintes du code")

    reg = (racine / "registres/scellements-v1.md").read_text(encoding="utf-8").split("\n")
    lignes = [l for l in reg if l.startswith("| ")]
    classe = rg.classer_cle_inconnue("GEL-T08", ("T06", "T08", "P3BIS", "NARC"))[0]
    ok = lignes == REGISTRE_ATTENDU and classe == "ignoree"
    print(f"(9) registre : {len(lignes)} lignes, égales aux quatre citées : {lignes == REGISTRE_ATTENDU} ; GEL-T08 classée "
          f"« {classe} » : {ok}")
    if not ok:
        defauts.append("registre ou classement")

    plat = " ".join(texte_c1.split())
    manquantes = [ph for ph in PHRASES if " ".join(ph.split()) not in plat]
    print(f"(10) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)} présentes"
          f"{' ; manquantes : ' + repr(manquantes) if manquantes else ''}")
    if manquantes:
        defauts.append("phrases exigées manquantes")
    presentes = [ph for ph in ABSENTES if ph in texte_c1]
    print(f"     passages retirés encore présents : {presentes}")
    if presentes:
        defauts.append("passages retirés encore présents")

    d = lignes_diff(texte22, texte_c1)
    print(f"(11) différentiel 22 → candidat 1 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées ; {len(couples)} couples")

    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


def _dicts(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from _dicts(v)
    elif isinstance(x, list):
        for v in x:
            yield from _dicts(v)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
