"""Ordre d'exécution de l'étape A de T0.7, variante B, brouillon 9 : application au brouillon 8 des couples VF4-A à VF4-E de la
vérification finale, tels qu'écrits (P14 : nombre de lignes, un entier, aucune colonne lue ; R-2314 (4), R-2315), puis des
mentions d'état (`a621dcd3` dernier commit contre-lu ; brouillon 8 contre-lu ; VF4-06), puis vérifications, dont « tout le reste
égal à l'octet au brouillon 8 » (v1).

Rédacteur des brouillons 6 à 8 et des candidats 2 à 4 de T0.7 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`,
Claude Opus 5.5), 11 novembre 2026, sur le message de la mère qui suit R-2315 (mêmes interdits et chemins que la consigne
`d29c7858…`, aux noms près). Bibliothèque standard et `bash -n` seulement ; aucun réseau, aucune clé, aucun `git`, aucun `vastai`.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

1. vérifie les empreintes du brouillon 8 (`24dc8df6…`) et de la vérification finale (`26efc4df…`) ;
2. lit les couples du bloc JSON du § 4 de la vérification finale ; applique **d'abord et seuls** ceux dont la cible est l'ordre
   (VF4-A à VF4-E), tels qu'écrits, chaque « ancien » présent une fois ; exige l'empreinte calculée par le vérificateur
   (`8413f56e…`) **avant** tout autre couple ; sinon arrêt (code 1) ;
3. applique les couples O9 (mentions d'état ; § 0 sexies) ; chaque « ancien » présent une fois ;
4. **tout le reste égal à l'octet** : défait tous les couples dans l'ordre inverse et exige le brouillon 8 octet pour octet ;
5. vérifie : titre ; douze marqueurs, une occurrence chacun, aucun autre ; P14 sans lecture de colonne ; blocs `bash` (`bash -n`,
   valeurs factices) ; extraits `python3 -I -c '…'` (`ast.parse`) ; choix de l'offre (§ 4.3) sur offres factices ; § 6 (devis)
   égal au brouillon 8 ; phrases exigées présentes ;
6. écrit `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9.md` (R12). Le scellement se fait à part.
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHEMIN_B8, SHA_B8 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md", "24dc8df6555bac03f2ffbe8440c3c1a7b9bf2aeaf9eab3c651306a6a73fc116e"
CHEMIN_B9 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9.md"
VF, SHA_VF = ("prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md",
              "26efc4dfb4924e6a2d6ddfaf7fdb37a6dae453946b1a114df2ec76ec014ad257")
SHA_VF_SEULS = "8413f56e8f14090718149a9bd8078e8dd4e59a2339015ea21408afa92ecd4759"
SHA_SCRIPT_V4 = "4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6"
COMMIT = "a621dcd3b929ce3ebd615fa852d4a7f5c103071d"
TITRE_B9 = "# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 9"
IDS_VF_ORDRE = ["VF4-A", "VF4-B", "VF4-C", "VF4-D", "VF4-E"]
MARQUEURS = ["<<ID_SESSION_FILLE>>", "<<EMPREINTE_CONFIG_T07>>", "<<LIGNE_SCELLEMENT_T07>>", "<<DEPENSE_ANTERIEURE_USD>>",
             "<<RUN_T06_7B>>", "<<BRANCHE_7B>>", "<<COMMIT_CODE_T07>>", "<<COMMIT_SCELLEMENT_T07>>", "<<CHEMIN_CONFIG_T07>>",
             "<<PERIMETRE_T07>>", "<<COMMIT_SRC_CONTRE_LU_T07>>", "<<ATT_C7_T07>>"]
FACTICES = {"<<DEPENSE_ANTERIEURE_USD>>": "0", "<<RUN_T06_7B>>": "20261112-000000-t06-reel",
            "<<BRANCHE_7B>>": "calcul/t06-confirmation-7b-v1", "<<COMMIT_CODE_T07>>": "0" * 40,
            "<<COMMIT_SCELLEMENT_T07>>": "1" * 40, "<<CHEMIN_CONFIG_T07>>": "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json",
            "<<PERIMETRE_T07>>": "JD,JA", "<<COMMIT_SRC_CONTRE_LU_T07>>": "3" * 40,
            "<<ATT_C7_T07>>": "530 passed, 23 skipped, 3 xfailed"}
VF_CITE = (f"vérification finale, `{VF}` (`{SHA_VF}`, Claude Fable 5.2, R-2315 : texte et ordre « après corrections », aucun "
           "nœud ; code `7e23a554..a621dcd3` « sans défaut bloquant »)")

COUPLES_O9 = [
    ("O9-01", "titre", "activations recalculées) — v1, brouillon 8\n", "activations recalculées) — v1, brouillon 9\n"),
    ("O9-02", "encadré et statut du brouillon 9",
     "couples VC3-C et VC3-D.\n\n- **Statut** : **brouillon 8**, écrit le 2026-11-11 à partir de 04:59 UTC",
     "couples VC3-C et VC3-D.\n"
     "> **Brouillon 9 (R-2315)** : couples VF4-A à VF4-E de la vérification finale, tels qu'écrits (P14 : le seul nombre de lignes\n"
     "> des mesures de 7b, un entier ; aucune colonne lue ; R-2314 (4)) ; `a621dcd3` est le dernier commit contre-lu (P13 (iii), `SRC7`).\n"
     "\n"
     "- **Statut** : **brouillon 9**, écrit le 2026-11-11 à partir de 05:39 UTC (`date -u`) par le rédacteur des brouillons 6 à 8\n"
     "  (Claude Opus 5.5, `claude-opus-5-5`, même sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; exclu de tout\n"
     "  rôle de lecteur de P3-bis), sur le message de la mère qui suit R-2315. **Brouillon 9 = brouillon 8**\n"
     f"  (`{SHA_B8}`, gardé tel quel, R12) **+ les couples VF4-A à VF4-E de la vérification\n"
     "  finale, tels qu'écrits** (lus dans son § 4 par le script\n"
     "  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9-appliquer-v1.py` et appliqués d'abord et seuls : ils donnent\n"
     f"  `{SHA_VF_SEULS}`, l'empreinte calculée par le vérificateur, contrôlée par le script avant tout\n"
     "  autre couple) **+ les couples O9-01 à O9-07** (mentions d'état : `a621dcd3` dernier commit contre-lu, brouillon 8 contre-lu,\n"
     "  VF4-06) ; **tout le reste est égal à l'octet au brouillon 8** (vérifié par le script : couples défaits → brouillon 8). Ce\n"
     "  qui change et pourquoi : § 0 sexies. **Contre-lu** : le brouillon 8 et les couples VF4-A à VF4-E, par la " + VF_CITE + " ;\n"
     "  les seules mentions d'état des couples O9 ne sont pas contre-lues ; à sceller avec le candidat 5 de T0.7.\n"
     "- **Brouillon 8** (statut gardé pour mémoire) : **brouillon 8**, écrit le 2026-11-11 à partir de 04:59 UTC"),
    ("O9-03", "statut du brouillon 8 (mention d'état)",
     "**Non\n  contre-lu** : à contre-lire (R2) avec le candidat 4 de T0.7 avant son scellement.",
     "**Non\n  contre-lu** : à contre-lire (R2) avec le candidat 4 de T0.7 avant son scellement (contre-lu depuis, brouillon 9 : "
     f"`{VF}`, `26efc4df…`, R-2315)."),
    ("O9-04", "section neuve « 0 sexies »", "\n## 1. Cadre\n",
     "\n## 0 sexies. Ce qui change depuis le brouillon 8 (brouillon 9 : vérification finale)\n\n"
     f"Source : R-2315 ({VF_CITE}) ; R-2314 (4) (P14 restreint par la mère).\n\n"
     "| Point | Où | Brouillon 8 | Brouillon 9 | Source |\n|---|---|---|---|---|\n"
     "| P14 | encadré ; § 0 quinquies ; § 3, P14 ; § 5 bis ; § 7 | la mère compte les actions notées de 7b, colonne `jetons_notes` "
     "lue | **le seul nombre de lignes** (forme du tableau, lu à son en-tête), un entier ; aucune colonne chargée, aucune valeur, "
     "aucune ventilation ; il majore `n` ; au-delà d'environ 7 378 lignes, aucune création (nœud) : **couples VF4-A à VF4-E tels "
     "qu'écrits** | R-2314 (4) ; R-2315 (VF4-01) |\n"
     "| Dernier commit contre-lu (`SRC7`) | encadré ; § 1 ; § 12 | différentiel `7e23a554..a621dcd3` sans contre-lecture | "
     "**`a621dcd3` dernier commit contre-lu** (vérification finale, mandat B : « sans défaut bloquant ») ; la mère écrit l'égalité "
     "de l'arbre `src/` de `SRC7` avec celui de `a621dcd3` (P13 (iii), VC3-D) | R-2315 |\n"
     "| Contre-lecture de l'ordre | statut | brouillon 8 non contre-lu | brouillon 8 contre-lu, « après corrections », aucun nœud | "
     "R-2315 |\n"
     "| Préchargement de la révision de P3 | § 3, P13, colonne « sinon » | « le v3 précharge » | le v4 de même (VF4-06) | R-2315 |\n\n"
     "Notes de la vérification finale sans geste ici (rien avant le scellement, R-2315) : **VF4-08** (une faute hors de "
     "`FAUTES_DU_BRAS` sort de `lecture_v4 controle-avant-ouverture` en code 1, non 2 ; le script v4 arrête quand même en code 2, "
     "rien d'ouvert) ; **VF4-09** (motif recopié au journal : tête de 600 octets de l'erreur ; le fichier entier reste sur "
     "l'instance) ; **VF4-10** (S-14 à S-16 confirmées). Un script d'un entier pour P14 est proposé au § 4 de la vérification "
     "finale (lecture de l'en-tête du tableau ; non versé). Devis (§ 6), P8, minuterie, script v4, ligne (A) et marqueurs : "
     "inchangés. Tout le reste est égal à l'octet au brouillon 8 (vérifié par programme, statut).\n\n"
     "## 1. Cadre\n"),
    ("O9-05", "§ 1 : code (dernier commit contre-lu)",
     "(brouillon 8 ; `7e23a554…` au brouillon 7), non fusionnée ;",
     "(brouillon 8 ; `7e23a554…` au brouillon 7), non fusionnée ; **dernier commit contre-lu** (brouillon 9 : " + VF_CITE + ") ;"),
    ("O9-06", "§ 3, P13, colonne « sinon » (VF4-06)",
     "autre : écrit au journal, le v3 précharge la révision de P3 (§ 5, étape 8) ;",
     "autre : écrit au journal, le v3 précharge la révision de P3 (§ 5, étape 8 ; brouillon 9 : le v4 de même, VF4-06) ;"),
    ("O9-07", "§ 12 : COMMIT_SRC_CONTRE_LU_T07 (dernier commit contre-lu)",
     "contre-lecture courte des corrections rendue, R-2311 ; la mère écrit l'égalité des arbres `src/`, P13 (iii))",
     "contre-lecture courte des corrections rendue, R-2311 ; la mère écrit l'égalité des arbres `src/`, P13 (iii) ; "
     f"**brouillon 9** : `{COMMIT}` est le dernier commit contre-lu, vérification finale, `26efc4df…`, R-2315)"),
]

EXIGEES = (
    "## 0 sexies. Ce qui change depuis le brouillon 8", "> **Brouillon 9 (R-2315)**", "**dernier commit contre-lu**",
    f"SHA_SCRIPT={SHA_SCRIPT_V4};", "ATT='<<ATT_C7_T07>>';", "`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`",
    "**3,2 à 4,7**", "**`ANT0` ≤ 3,6 USD**", "| P14 |", "**n'imprime qu'un entier**",
)
ABSENTES = ("`jetons_notes` seule", "actions de 7b compté", "la mère compte `n`")


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def echec(motif: str) -> None:
    print(f"ÉCHEC : {motif}")
    sys.exit(1)


def remplacer(texte: str, ident: str, ancien: str, nouveau: str) -> str:
    n = texte.count(ancien)
    if n != 1:
        echec(f"{ident} : « ancien » présent {n} fois (une attendue)")
    if ancien == nouveau:
        echec(f"{ident} : « ancien » égal au « nouveau »")
    return texte.replace(ancien, nouveau)


def blocs_bash(texte: str) -> list[str]:
    return re.findall(r"```bash\n(.*?)```", texte, flags=re.S)


def essai_offre(texte: str) -> None:
    b = next(x for x in blocs_bash(texte) if "vastai search offers" in x)
    extrait = re.search(r"python3 -I -c '([^']*)' \"\$W/offres.json\"", b).group(1)
    base = {"gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "storage_total_cost": 0.05, "inet_down_cost": 0.01,
            "inet_up_cost": 0.01, "machine_id": 1, "cuda_max_good": 13.0}
    cas = [([{**base, "id": 1, "dph_total": 0.9, "cpu_name": "Intel Xeon"}, {**base, "id": 2, "dph_total": 1.2, "cpu_name": "AMD EPYC 7513"},
             {**base, "id": 3, "dph_total": 1.1, "cpu_name": "AMD EPYC 7J13"}], "id=3 "),
           ([{**base, "id": 4, "dph_total": 1.0, "cpu_name": "Intel Xeon"}, {**base, "id": 5, "dph_total": 0.95}], "id=5 "),
           ([], "aucune offre")]
    with tempfile.TemporaryDirectory() as d:
        for offres, attendu in cas:
            p = Path(d) / "offres.json"
            p.write_text(json.dumps({"offers": offres}), encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", "-c", extrait, str(p)], capture_output=True, text=True)
            if r.returncode != 0 or not r.stdout.startswith(attendu):
                echec(f"§ 4.3 : choix de l'offre {r.stdout.strip()!r} (attendu {attendu!r})")
    print("§ 4.3 : choix de l'offre essayé sur trois cas factices : conforme")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        echec("usage : appliquer RACINE")
    racine = Path(argv[0]).resolve()
    for chemin, attendu in ((CHEMIN_B8, SHA_B8), (VF, SHA_VF)):
        e = sha((racine / chemin).read_bytes())
        if e != attendu:
            echec(f"{chemin} : empreinte {e[:16]}… ≠ {attendu[:16]}…")
    print("entrées vérifiées : brouillon 8, vérification finale")
    vf = (racine / VF).read_text(encoding="utf-8")
    s4 = vf[vf.index("## 4. Couples proposés"):vf.index("## 5.")]
    vfs = json.loads(re.search(r"```json\n(.*?)\n```", s4, re.S).group(1))
    ordre_vf = [c for c in vfs if c["cible"] == "ordre, brouillon 8"]
    if [c["id"] for c in ordre_vf] != IDS_VF_ORDRE or any(c["gelee"] is not None for c in ordre_vf):
        echec(f"couples de l'ordre dans la vérification finale : {[c['id'] for c in ordre_vf]}")
    couples = [(c["id"], c["section"], c["ancien"], c["nouveau"]) for c in ordre_vf]
    texte8 = (racine / CHEMIN_B8).read_bytes().decode("utf-8")
    texte = texte8
    for ident, ou, ancien, nouveau in couples:
        texte = remplacer(texte, f"{ident} ({ou})", ancien, nouveau)
    e = sha(texte.encode("utf-8"))
    if e != SHA_VF_SEULS:
        echec(f"VF4-A à VF4-E seuls : {e} ≠ {SHA_VF_SEULS} (empreinte du vérificateur)")
    print(f"VF4-A à VF4-E appliqués seuls, tels qu'écrits : {e} = empreinte calculée par le vérificateur")
    ids = [c[0] for c in COUPLES_O9]
    if ids != [f"O9-{k:02d}" for k in range(1, len(ids) + 1)]:
        echec("identifiants de couples O9")
    for ident, ou, ancien, nouveau in COUPLES_O9:
        texte = remplacer(texte, f"{ident} ({ou})", ancien, nouveau)
    couples += COUPLES_O9
    print(f"{len(COUPLES_O9)} couples O9 appliqués, chacun à une occurrence ; {len(couples)} couples en tout")
    defait = texte
    for ident, ou, ancien, nouveau in reversed(couples):
        n = defait.count(nouveau)
        if n != 1:
            echec(f"défaisage de {ident} : « nouveau » présent {n} fois (une attendue)")
        defait = defait.replace(nouveau, ancien)
    if defait != texte8:
        echec("les couples défaits ne redonnent pas le brouillon 8 octet pour octet")
    print(f"tout le reste égal à l'octet : couples défaits dans l'ordre inverse → brouillon 8 retrouvé "
          f"({texte8.count(chr(10))} → {texte.count(chr(10))} lignes)")
    if texte.split("\n", 1)[0] != TITRE_B9:
        echec("titre du brouillon 9")
    for m in MARQUEURS:
        if texte.count(m) != 1:
            echec(f"marqueur {m} : {texte.count(m)} occurrences (une attendue)")
    autres = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)) - set(MARQUEURS))
    if autres:
        echec(f"marqueurs inattendus : {autres}")
    print(f"marqueurs : {len(MARQUEURS)}, une occurrence chacun, aucun autre")
    for p in EXIGEES:
        if p not in texte:
            echec(f"phrase exigée absente : {p!r}")
    for p in ABSENTES:
        if p in texte:
            echec(f"passage retiré encore présent : {p!r}")
    print(f"phrases exigées : {len(EXIGEES)} présentes ; P14 sans lecture de colonne ({len(ABSENTES)} passages retirés absents)")
    s6 = texte[texte.index("## 6. Devis"):texte.index("## 7. Arrêts")]
    if s6 != texte8[texte8.index("## 6. Devis"):texte8.index("## 7. Arrêts")]:
        echec("§ 6 changé")
    print("§ 6 (devis, plafond, marge) égal à celui du brouillon 8")
    blocs = blocs_bash(texte)
    if len(blocs) != 8 or blocs != blocs_bash(texte8):
        echec(f"{len(blocs)} blocs bash (8 attendus, égaux au brouillon 8)")
    n_py = 0
    with tempfile.TemporaryDirectory() as d:
        for k, b in enumerate(blocs, 1):
            for m, v in FACTICES.items():
                b = b.replace(m, v)
            p = Path(d) / f"bloc-{k}.sh"
            p.write_text(b, encoding="utf-8")
            r = subprocess.run(["bash", "-n", str(p)], capture_output=True, text=True)
            if r.returncode != 0:
                echec(f"bloc bash {k} : bash -n en échec : {r.stderr.strip()[:300]}")
            for extrait in re.findall(r"python3 -I -c '([^']*)'", b):
                try:
                    ast.parse(extrait)
                except SyntaxError as e:
                    echec(f"bloc bash {k} : extrait Python illisible ({e})")
                n_py += 1
    print(f"blocs bash : {len(blocs)}, égaux au brouillon 8, bash -n sans erreur ; extraits Python : {n_py}, ast.parse sans erreur")
    essai_offre(texte)
    sortie = racine / CHEMIN_B9
    octets = texte.encode("utf-8")
    if sortie.exists() and sortie.read_bytes() != octets:
        echec(f"{CHEMIN_B9} existe avec un autre contenu (R12)")
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"écrit : {CHEMIN_B9} ({sha(octets)})")
    print("TOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
