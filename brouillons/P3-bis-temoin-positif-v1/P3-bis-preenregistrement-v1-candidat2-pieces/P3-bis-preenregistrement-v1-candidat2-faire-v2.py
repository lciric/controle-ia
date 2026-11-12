"""Candidat 2 du préenregistrement de P3-bis : application des couples C2 et contrôles par programme (v2).

v2 (2026-11-11, vers 13:51 UTC, `date -u`) : copie de la v1 (`1cb33a52…`), gardée telle quelle (R12) et qui ne sert
plus, pour le complément de la session mère (R-2349 : P-9 fait) : couples v2 (C2-01 à C2-22, la ligne P-9 en plus),
script et journal de construction v2, sorties sous des noms v2 ; un contrôle et un artefact de plus (ligne P-9).

Écrit le 2026-11-11 par un rédacteur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère
`session_01VJdZpSMxSdk2SJ1ScmdfNv`, sur la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-p3bis-candidat2-v1.md`
(`85a3d612…`). Aucun appel externe ; aucune écriture git (`git show` en lecture seule) ; aucun fichier de T0.7 ni des
interdits communs v2 ouvert.

Le candidat 2 n'est écrit que par ce script, quand la session mère le lance avec le numéro de la ligne du registre des
décisions qui constate la date tenue (P-11) :
  PYTHONPATH=src .venv/bin/python <ce script> --date-tenue R-NNNN "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
écrit `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2.md` et le journal
`…-candidat2-pieces/P3-bis-preenregistrement-v1-candidat2-journal-v1.md`, chacun scellé (compagnon `.sha256`).
Avec `--date-tenue R-0000` (numéro fictif), il écrit à la place la sortie à blanc
`…-candidat2-pieces/P3-bis-preenregistrement-v1-candidat2-a-blanc.md` et le journal
`…-candidat2-pieces/P3-bis-preenregistrement-v1-candidat2-journal-a-blanc-v1.md` (essai à blanc de la chaîne seulement ;
jamais scellée comme texte de S). `--essai DOSSIER` écrit les mêmes chemins sous DOSSIER au lieu de la racine du dépôt.

Ce que fait le script, dans l'ordre, sans rien écrire tant qu'un contrôle échoue (R5 ; « tout écart : arrête-toi et
écris-le ») :
  1. vérifie ses entrées par leur empreinte et leur compagnon (candidat 1, couples C2, épingles proposées, relecture
     courte, consigne, script de construction) ; numéro de la forme `R-` et quatre chiffres, après R-2345 (sauf R-0000) ;
  2. remplace le jeton `R-NNNN` (une seule fois, couple C2-16) et applique les couples C2 au candidat 1, chacun trouvé
     exactement une fois ;
  3. contrôles par programme sur le texte écrit, chacun aussi éprouvé sur un artefact qui doit échouer :
     (a) défaire les couples, dans l'ordre inverse, redonne le candidat 1 à l'octet ;
     (b) empreintes des sept sections gelées égales à celles du candidat 1, sauf « Plan d'analyse », égale à celle du
         candidat 1 où seul N-1 (C2-11) est appliqué ; chaque autre couple, appliqué seul, ne touche aucune section
         gelée ; titres de niveau 2 : ceux du candidat 1 plus la table neuve ; entrées de « Contre-lecture » inchangées ;
     (c) aucun marqueur `<<…>>` (forme du bloc 4 et de `prereg.GABARIT`), aucun « À REMPLIR », aucun jeton ; la phrase
         « date tenue : défaut échu, R-… » une fois, au numéro donné ;
     (d) `controle_ia.prereg.problemes` vide ;
     (e) `python3 -I verifications_p3bis_v2.py valeurs <texte>` (copie du commit du code, par `git show`) ;
     (f) blocs « textuels » des contrôles avant dépense v2, rejoués par bash sur le texte avec leurs lignes recopiées
         (chacune vérifiée présente, mot pour mot, dans `controles_avant_depense_p3bis_v2.sh` au commit du code) :
         blocs 2 (commit du code cité une fois, égal au code relu), 4 (marqueurs ; « Tâches de P3 »), 6 (sortie de
         l'essai de fermeture citée sous la forme exigée), 7 (longueurs attendues), 11 (amorce et script de l'instance),
         12 (lecture précoce, intitulés une fois, ligne « Lancement »), 14 (chaque rapport attendu, chemin et empreinte),
         avec les valeurs des épingles proposées et les empreintes recalculées au commit du code ;
  4. écrit (R12 : aucune sortie ne doit exister) le texte et le journal, puis les scelle.
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from controle_ia.prereg import GABARIT, MARQUEUR, problemes, sections
from controle_ia.scellement import sceller

DOSSIER = "brouillons/P3-bis-temoin-positif-v1"
PIECES2 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat2-pieces"
C1 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat1.md"
C2 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat2.md"
A_BLANC = f"{PIECES2}/P3-bis-preenregistrement-v1-candidat2-a-blanc-v2.md"
JOURNAL = f"{PIECES2}/P3-bis-preenregistrement-v1-candidat2-journal-v2.md"
JOURNAL_A_BLANC = f"{PIECES2}/P3-bis-preenregistrement-v1-candidat2-journal-a-blanc-v2.md"
COUPLES = f"{PIECES2}/P3-bis-preenregistrement-v1-candidat2-couples-v2.json"
EPINGLES = f"{PIECES2}/P3-bis-epingles-proposees-v1.json"
EMP = {
    C1: "9a56a657b1fad1e23b0cc11e41831f066eed48674159dbc55c2a869aa56c4271",
    COUPLES: "bffe8e381a9a4ca86e56e4e9f88edb69c66ff58f2ad7192d5053c231ef609979",
    EPINGLES: "0fb1443aff22133c8aaaac1616bbc191a53cfd0b2de8c4ffbe8fe53e13240389",
    f"{PIECES2}/P3-bis-preenregistrement-v1-candidat2-construire-couples-v2.py":
        "dc49e0f8b853c8fc282ff7e225408282fa42ed1b848f5c07ae6ca549122b9ba5",
    f"{PIECES2}/P3-bis-preenregistrement-v1-candidat2-construire-journal-v2.txt":
        "11901949c291784b272e904b92b7bd515b5675b0bff3995963f6635b2a8f1df2",
    "docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v2/rapport-concordance-journal-v2.md":
        "01fb3e6551de74b4aaf26aed26e6c5914940f55b2bddc730b95552c4c63652ac",   # P-9 (R-2349) : empreinte seule
    f"{DOSSIER}/P3-bis-candidat1-relecture-courte-v1.md":
        "85ee0b47078d18311bb70872877c0b73c54fc480219e87678e4cc6ae63551eec",
    "docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-p3bis-candidat2-v1.md":
        "85a3d612f441083943d93e5c274e88d3aad58cd84311adc1ef71184bf1a58e58",
}
CODE = "5e4575259478af3611e2c7fb1313342912caf484"
CHAINE = "docs/procedures/P3-bis-temoin-positif-v1"
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
TABLE_NEUVE = "Table « ce qui change du candidat 1 au candidat 2 »"
JETON = "R-NNNN"
N1 = "C2-11"
DATE = "C2-16"
P9 = "| sortie versée : aucune discordance ; une discordance est un nœud ; candidat 2 : **P-9 fait** (R-2349) : rapport "
ENTREE = re.compile(r"^\s*-?\s*\**Contre-lecture (\d+)\**", re.M)    # même motif que prereg.ENTREE

# Blocs « textuels » des contrôles avant dépense v2 : lignes recopiées mot pour mot (vérifiées présentes dans le script
# au commit du code) ; seules changent les valeurs passées en argument (ce qui, dans les contrôles, vient du clone de S
# ou des épingles) et l'absence des parties non textuelles (git show "$S:…", merge-base, essais, pytest).
RECOPIEES = [
    """echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }""",
    """plat() { tr '\\n' ' ' < "$1" | tr -s ' '; }""",
    """NC=$(grep -c "Commit du code d'analyse : \\`" "$P" || true)""",
    """CODE=$(sed -n "s/.*Commit du code d'analyse : \\`\\([0-9a-f]\\{40\\}\\)\\`.*/\\1/p" "$P" | head -1)""",
    """[ "$CODE" = "$CODE_RELU" ] && ok "2 commit du code = code relu épinglé" || ko "2 commit du code $CODE ≠ code relu épinglé $CODE_RELU\"""",
    """MARQ=$(grep -o '<<[A-Z0-9_]\\+>>' "$P" | sort -u | tr '\\n' ' ')""",
    """[ -z "$MARQ" ] && ok "4 texte scellé sans marqueur" || ko "4 marqueurs restants dans le texte : $MARQ\"""",
    """[ "$(grep -c "Tâches de P3 : \\`$ST\\`" "$P")" = 1 ] && ok "4 tâches citées par leur empreinte ($ST)" || ko "4 tâches non citées par leur empreinte\"""",
    """   && plat "$P" | grep -qF "\\`$ESSAI_FERMETURE_CHEMIN\\` (\\`$ESSAI_FERMETURE\\`"; then""",
    """plat "$P" | grep -qF "\\`$LONGUEURS_ATTENDUES_CHEMIN\\` (\\`$LONGUEURS_ATTENDUES\\`" && ok "7 longueurs attendues citées par le texte" || ko "7 longueurs attendues non citées par le texte\"""",
    """a=$(sed -n "s/.*Tests attendus : \\`\\([0-9]*\\)\\`.*/\\1/p" "$P" | head -1)""",
    """        plat "$P" | grep -qF "\\`$f\\` (\\`$e\\`" && ok "11 empreinte de $f citée ($e)" || ko "11 empreinte de $f ($e) non citée\"""",
    """lire_unique() { [ "$(grep -c "$1 : \\`" "$P" || true)" = 1 ] && sed -n "s/.*$1 : \\`\\\\([^\\`]*\\\\)\\`.*/\\\\1/p" "$P"; }""",
    """L_TESTS=$(lire_unique "Tests attendus"); L_CFG=$(lire_unique "Chemin de la configuration de P3")""",
    """L_T=$(lire_unique "Chemin des tâches de P3"); L_C=$(lire_unique "Chemin des consignes de P3")""",
    """[ "$L_TESTS" = "$a" ] && [ "$L_CFG" = "$CFG" ] && [ "$L_T" = "$TACHES" ] && [ "$L_C" = "$CONSIGNES" ] \\""",
    """    && ok "12 lecture précoce : citations uniques, chemins attendus" || ko "12 lecture précoce : citation absente, en double, ou chemin inattendu\"""",
    """INTITULES=("Configuration de P3 (empreinte canonique)" "Tâches de P3" "Commit du code d'analyse" "Entropie" "Tests attendus\"""",
    """           "Chemin de la configuration de P3" "Chemin des tâches de P3" "Chemin des consignes de P3")""",
    """DOUBLES=""; for x in "${INTITULES[@]}"; do [ "$(grep -oF "$x : \\`" "$P" | wc -l)" = 1 ] || DOUBLES="$DOUBLES « $x »"; done""",
    """[ -z "$DOUBLES" ] && ok "12 intitulés lus une fois chacun (${#INTITULES[@]})" || ko "12 intitulés absents ou cités plusieurs fois :$DOUBLES\"""",
    """grep -qF "\\`PREREG=$P\\`, \\`BRANCHE=calcul/p3bis-reel-v1\\`" "$P" && grep -qF "\\`DEPOT_URL=$DEPOT_URL\\`" "$P" \\""",
    """    && ok "12 ligne « Lancement » : PREREG, BRANCHE, DEPOT_URL du dépôt de travail" || ko "12 ligne « Lancement » : PREREG, BRANCHE ou DEPOT_URL autres\"""",
    """        plat "$P" | grep -qF "\\`$f\\`" && plat "$P" | grep -qF "$e" && ok "14 rapport $f présent, scellé, cité" || ko "14 rapport $f présent et scellé, mais non cité par le texte\"""",
]


def harnais() -> str:
    r = RECOPIEES
    return "\n".join([
        "set -uo pipefail",
        'T=$1; CODE_RELU=$2; ST=$3; ESSAI_FERMETURE_CHEMIN=$4; ESSAI_FERMETURE=$5; LONGUEURS_ATTENDUES_CHEMIN=$6',
        'LONGUEURS_ATTENDUES=$7; E_AMORCE=$8; E_INSTANCE=$9; RAPPORTS_ATTENDUS=${10}',
        "DEPOT_URL=https://github.com/lciric/controle-ia-travail.git",
        "P=prereg/P3-bis-temoin-positif-v1.md; CFG=prereg/P3-bis-temoin-positif-config-v1.json; "
        "CONSIGNES=prereg/P3-bis-consignes-v1.md",
        "TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json",
        "AMORCE=scripts/amorce_instance_p3bis_v2.sh; INSTANCE=scripts/p3bis_instance_v2.sh",
        # le texte est lu sous le nom de S ($P), dans un dossier de travail (comme dans le clone de S)
        'cd "$(dirname "$T")" && mkdir -p prereg && cp "$T" "$P" || exit 2',
        r[0], r[1],
        "# bloc 2 (l. 108-112 ; partie textuelle)",
        r[2], r[3],
        'if [ "$NC" = 1 ] && [[ "$CODE" =~ ^[0-9a-f]{40}$ ]]; then ok "2 commit du code cité une fois, $CODE"',
        'else ko "2 commit du code cité illisible, cité $NC fois"; fi',
        r[4],
        "# bloc 4 (l. 126-127, 141)",
        r[5], r[6], r[7],
        "# bloc 6 (l. 152 : citation)",
        'if true \\', r[8],
        '    ok "6 essai de fermeture : sortie citée sous la forme exigée"',
        'else ko "6 essai de fermeture : sortie non citée sous la forme exigée"; fi',
        "# bloc 7 (l. 197)",
        r[9],
        "# bloc 8 (l. 200 : N lu)",
        r[10],
        '[[ "$a" =~ ^[0-9]+$ ]] && ok "8 N lu : $a" || ko "8 N illisible"',
        "# bloc 11 (l. 277-278 ; empreintes recalculées au commit du code)",
        'for paire in "$AMORCE=$E_AMORCE" "$INSTANCE=$E_INSTANCE"; do',
        '        f=${paire%%=*}; e=${paire#*=}',
        r[11],
        "done",
        "# bloc 12 (l. 287-297)",
        r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22],
        "# bloc 14 (l. 302-305 ; partie textuelle)",
        "for paire in $RAPPORTS_ATTENDUS; do",
        "    f=${paire%%=*}; e=${paire#*=}",
        r[23],
        "done",
        '[ "$echec" = 0 ] && echo "BLOCS TEXTUELS : TOUS CONFORMES" || echo "BLOCS TEXTUELS : ÉCHEC"',
        '[ "$echec" = 0 ]',
        ""])


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_show(chemin: str) -> bytes:
    r = subprocess.run(["git", "show", f"{CODE}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git show {CODE[:8]}:{chemin} impossible")
    return r.stdout


def tranches(t: str) -> dict:
    """titre de niveau 2 → texte brut, du titre au titre suivant (comme la relecture courte, annexe B)."""
    pos = [(m.start(), m.group(0)[3:].strip()) for m in re.finditer(r"(?m)^## .*$", t)]
    d = {}
    for i, (p, ti) in enumerate(pos):
        if ti in d:
            raise SystemExit(f"titre en double : {ti}")
        d[ti] = t[p:pos[i + 1][0] if i + 1 < len(pos) else len(t)]
    return d


def appliquer(texte: str, couples: list, sens: str = "faire") -> str:
    a, n = ("ancien", "nouveau") if sens == "faire" else ("nouveau", "ancien")
    for x in (couples if sens == "faire" else list(reversed(couples))):
        k = texte.count(x[a])
        if k != 1:
            raise ValueError(f"{x['id']} ({sens}) : « {a} » trouvé {k} fois")
        texte = texte.replace(x[a], x[n], 1)
    return texte


class Controles:
    def __init__(self, t1: str, couples: list, ep: dict, numero: str, tmp: Path):
        self.t1, self.couples, self.ep, self.numero, self.tmp = t1, couples, ep, numero, tmp
        self.s1 = tranches(t1)
        self.n1 = next(x for x in couples if x["id"] == N1)
        self.verif = tmp / "verifications_p3bis_v2.py"
        self.verif.write_bytes(git_show(f"{CHAINE}/verifications_p3bis_v2.py"))
        self.script = tmp / "blocs_textuels.sh"
        self.script.write_text(harnais(), encoding="utf-8")
        self.st = h(git_show("donnees/t05-pilote-v1/taches-pilote-60-v1.json"))
        self.e_am = h(git_show("scripts/amorce_instance_p3bis_v2.sh"))
        self.e_in = h(git_show("scripts/p3bis_instance_v2.sh"))

    def tout(self, t: str) -> list:
        """[(nom, conforme, détail)] pour le texte t."""
        r = []
        # (a) défaire
        try:
            r.append(("a défaire les couples redonne le candidat 1", appliquer(t, self.couples, "defaire") == self.t1,
                      "comparé à l'octet"))
        except ValueError as e:
            r.append(("a défaire les couples redonne le candidat 1", False, str(e)))
        # (b) sections gelées
        s2 = tranches(t)
        plan_n1 = self.s1["Plan d'analyse"].replace(self.n1["ancien"], self.n1["nouveau"], 1)
        for g in GELEES:
            attendu = plan_n1 if g == "Plan d'analyse" else self.s1[g]
            ok = g in s2 and s2[g] == attendu
            r.append((f"b section gelée « {g} »" + (" = candidat 1 + N-1 seul" if g == "Plan d'analyse" else
                                                      " = candidat 1"), ok,
                      f"{h(s2.get(g, '').encode())[:12]} (candidat 1 : {h(self.s1[g].encode())[:12]})"))
        titres1 = list(self.s1)
        i = titres1.index("Table « ce qui change du 12 au candidat 1 »")
        r.append(("b titres : ceux du candidat 1 plus la table neuve, à sa place",
                  list(s2) == titres1[:i] + [TABLE_NEUVE] + titres1[i:], f"{len(s2)} titres"))
        e1 = len(ENTREE.findall(sections(self.t1)["Contre-lecture"]))
        e2 = len(ENTREE.findall(sections(t).get("Contre-lecture", "")))
        r.append(("b entrées « Contre-lecture k » inchangées", e1 == e2, f"{e2} (candidat 1 : {e1})"))
        # (c) marqueurs, jeton, phrase de la date tenue
        r.append(("c aucun marqueur <<…>>", not GABARIT.findall(t) and not re.findall(r"<<[A-Z0-9_]+>>", t),
                  str(sorted(set(GABARIT.findall(t))))))
        r.append(("c aucun « À REMPLIR », aucun jeton R-NNNN", MARQUEUR not in t and JETON not in t, ""))
        phrase = f"date tenue : défaut échu, {self.numero} ("
        r.append(("c phrase « date tenue : défaut échu, R-… » une fois, au numéro donné",
                  t.count(phrase) == 1 and len(re.findall(r"date tenue : défaut échu, R-\d", t)) == 1, phrase))
        r.append(("c ligne P-9 (R-2349) une fois, à la ligne P-9 des « Préalables »",
                  t.count(P9) == 1 and t.count("**P-9 fait** (R-2349)") == 1 and P9 in tranches(t).get(
                      "Préalables vérifiables du scellement (étapes du candidat)", ""), ""))
        # (d) problemes()
        f = self.tmp / "texte.md"
        f.write_text(t, encoding="utf-8")
        p = problemes(f)
        r.append(("d controle_ia.prereg.problemes vide", p == [], str(p)))
        # (e) valeurs (module commun du commit du code)
        v = subprocess.run(["python3", "-I", str(self.verif), "valeurs", str(f)], capture_output=True, text=True)
        r.append(("e verifications_p3bis_v2.py valeurs", v.returncode == 0,
                  (v.stdout + v.stderr).strip().splitlines()[-1] if (v.stdout + v.stderr).strip() else ""))
        # (f) blocs textuels des contrôles
        ec = self.ep["epingles_controles"]
        travail = self.tmp / "s"
        if travail.exists():
            subprocess.run(["rm", "-rf", str(travail)], check=True)
        travail.mkdir()
        (travail / "texte.md").write_text(t, encoding="utf-8")
        b = subprocess.run(["bash", str(self.script), str(travail / "texte.md"), ec["CODE_RELU"], self.st,
                            ec["ESSAI_FERMETURE_CHEMIN"], ec["ESSAI_FERMETURE"], ec["LONGUEURS_ATTENDUES_CHEMIN"],
                            ec["LONGUEURS_ATTENDUES"], self.e_am, self.e_in, ec["RAPPORTS_ATTENDUS"]],
                           capture_output=True, text=True)
        lignes = [x for x in b.stdout.splitlines() if x.strip()]
        for x in lignes[:-1]:
            r.append((f"f bloc {x[4:]}", x.startswith("OK  "), ""))
        r.append(("f " + (lignes[-1] if lignes else "harnais muet"), b.returncode == 0,
                  b.stderr.strip()[:200]))
        self.sortie_harnais = b.stdout
        self.sortie_valeurs = (v.stdout + v.stderr).strip()
        return r


def artefacts(t: str, ep: dict) -> list:
    """(nom, texte artefact, préfixe du contrôle qui doit échouer)."""
    ec = ep["epingles_controles"]
    hyp = "## Hypothèse\n"
    i = t.index(hyp) + len(hyp)
    j = t.index("0,0100 [0,0037 ; 0,0216]")
    lanc = "`BRANCHE=calcul/p3bis-reel-v1`"
    rel = "85ee0b47078d18311bb70872877c0b73c54fc480219e87678e4cc6ae63551eec"
    return [
        ("texte retouché hors couples (une espace ajoutée en fin)", t + " ", "a "),
        ("« Hypothèse » retouchée", t[:i] + "x" + t[i:], "b section gelée « Hypothèse »"),
        ("« Plan d'analyse » retouché à côté de N-1", t[:j] + "0,0101" + t[j + 6:], "b section gelée « Plan d'analyse »"),
        ("marqueur ajouté", t.replace("## Devis\n", "## Devis\n\n<<CHAINE_P3BIS>>\n", 1), "c aucun marqueur"),
        ("marqueur ajouté (problemes)", t.replace("## Devis\n", "## Devis\n\n<<CHAINE_P3BIS>>\n", 1), "d "),
        ("date tenue en double", t.replace("## Devis\n", "## Devis\n\ndate tenue : défaut échu, R-0000 (\n", 1),
         "c phrase"),
        ("valeur « aucun `timeout` » retirée", t.replace("aucun `timeout`", "aucun délai"), "e "),
        ("commit du code cité deux fois",
         t.replace("- Entropie : `", f"- Commit du code d'analyse : `{CODE}`\n- Entropie : `", 1), "f bloc 2 commit du code cité"),
        ("tâches citées par une autre empreinte", t.replace("Tâches de P3 : `287e8348", "Tâches de P3 : `287e8349", 1),
         "f bloc 4 tâches"),
        ("essai de fermeture cité sous une autre empreinte", t.replace(ec["ESSAI_FERMETURE"], "0" * 64),
         "f bloc 6 essai"),
        ("longueurs attendues citées sous une autre empreinte", t.replace(ec["LONGUEURS_ATTENDUES"], "0" * 64),
         "f bloc 7 longueurs"),
        ("amorce citée sous une autre empreinte",
         t.replace("b331e44f763f87744b9669998c8a7aa32308e449d07ba414e6c2bb0bc4ed22f4", "0" * 64),
         "f bloc 11 empreinte de scripts/amorce"),
        ("intitulé « Entropie » en double", t.replace("- Entropie : `", "- Entropie : `1`\n- Entropie : `", 1),
         "f bloc 12 intitulés"),
        ("ligne « Lancement » sans la branche", t.replace(lanc, "`BRANCHE=calcul/autre`"), "f bloc 12 ligne"),
        ("relecture courte non citée par son empreinte", t.replace(rel, "0" * 64),
         "f bloc 14 rapport brouillons/P3-bis-temoin-positif-v1/P3-bis-candidat1-relecture-courte-v1.md"),
        ("titre de niveau 2 ajouté", t.replace("## Devis\n", "## Devis bis\n\nx\n\n## Devis\n", 1), "b titres"),
        ("entrée « Contre-lecture 5 » ajoutée",
         t.replace("## Marqueurs restants", "- **Contre-lecture 5** : x\n\n## Marqueurs restants", 1), "b entrées"),
        ("« À REMPLIR » ajouté", t.replace("## Devis\n", "## Devis\n\nÀ REMPLIR\n", 1), "c aucun « À REMPLIR »"),
        ("marqueur ajouté (bloc 4 des contrôles)", t.replace("## Devis\n", "## Devis\n\n<<CHAINE_P3BIS>>\n", 1),
         "f bloc 4 marqueurs restants"),
        ("commit du code cité autre que le code relu", t.replace(f"Commit du code d'analyse : `{CODE}`",
                                                                 "Commit du code d'analyse : `" + "a" * 40 + "`", 1),
         "f bloc 2 commit du code " + "a" * 40),
        ("tests attendus illisibles", t.replace("Tests attendus : `531`", "Tests attendus : `x531`", 1), "f bloc 8"),
        ("ligne P-9 retirée", t.replace("**P-9 fait** (R-2349)", "**P-9** (R-2349)"), "c ligne P-9"),
    ]


def main(argv: list) -> int:
    args = argv[1:]
    racine = Path(".")
    if "--essai" in args:
        k = args.index("--essai")
        racine = Path(args[k + 1])
        del args[k:k + 2]
    if len(args) != 3 or args[0] != "--date-tenue" or not re.fullmatch(r"R-\d{4}", args[1]) \
            or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", args[2]):
        print("usage : --date-tenue R-NNNN AAAA-MM-JJTHH:MM:SSZ [--essai DOSSIER]", file=sys.stderr)
        return 2
    numero, heure = args[1], args[2]
    a_blanc = numero == "R-0000"
    if not a_blanc and int(numero[2:]) <= 2345:
        print(f"{numero} : la ligne qui constate la date tenue suit R-2345", file=sys.stderr)
        return 2
    texte_sortie, journal_sortie = (A_BLANC, JOURNAL_A_BLANC) if a_blanc else (C2, JOURNAL)
    sorties = [racine / texte_sortie, racine / journal_sortie]
    if any(p.exists() or Path(str(p) + ".sha256").exists() for p in sorties):
        print("une sortie ou son sceau existe déjà (R12) : rien n'est écrit", file=sys.stderr)
        return 2
    j = [f"# Journal du candidat 2 de P3-bis ({'sortie à blanc' if a_blanc else 'texte'}) — v1", "",
         f"- Heure passée en argument (`date -u`) : {heure}", f"- Numéro de la date tenue : {numero}"
         + (" (fictif : sortie à blanc, essai de la chaîne seulement)" if a_blanc else ""),
         f"- Script : `{argv[0]}` ({h(Path(argv[0]).read_bytes())})", f"- Sorties : `{texte_sortie}`, `{journal_sortie}`"]
    echecs = []
    # 1. entrées
    for f, e in EMP.items():
        b = Path(f).read_bytes()
        c = Path(f + ".sha256").read_text(encoding="utf-8").strip() if Path(f + ".sha256").exists() else None
        ok = h(b) == e and c == f"{e}  {Path(f).name}"
        j.append(f"- Entrée `{f}` : {h(b)} {'= épinglée et = compagnon' if ok else 'ÉCART'}")
        if not ok:
            echecs.append(f"entrée {f}")
    sh = subprocess.run(["git", "show", f"{CODE}:{CHAINE}/controles_avant_depense_p3bis_v2.sh"], capture_output=True,
                        text=True).stdout
    manquantes = [x for x in RECOPIEES if x not in sh]
    j.append(f"- Lignes des contrôles recopiées dans le harnais : {len(RECOPIEES)}, toutes présentes mot pour mot au "
             f"commit du code : {'oui' if not manquantes else 'NON ' + repr(manquantes[:2])}")
    if manquantes:
        echecs.append("lignes recopiées absentes des contrôles")
    t1 = Path(C1).read_text(encoding="utf-8")
    brut = Path(COUPLES).read_text(encoding="utf-8")
    couples = json.loads(brut)
    ep = json.loads(Path(EPINGLES).read_text(encoding="utf-8"))
    if brut.count(JETON) != 1 or next(x for x in couples if x["id"] == DATE)["nouveau"].count(JETON) != 1:
        echecs.append("jeton R-NNNN : une occurrence attendue, dans C2-16")
    gelees = [x["id"] for x in couples if x["section_gelee"]]
    j.append(f"- Couples : {len(couples)} ({couples[0]['id']} à {couples[-1]['id']}) ; couples déclarés gelés : {gelees}")
    if gelees != [N1]:
        echecs.append("couples gelés ≠ [C2-11]")
    if echecs:
        print("\n".join(j + ["", "ÉCHEC : " + " ; ".join(echecs)]))
        return 1
    couples = [dict(x, nouveau=x["nouveau"].replace(JETON, numero)) for x in couples]
    # 2. application
    try:
        t2 = appliquer(t1, couples)
    except ValueError as e:
        print("\n".join(j + ["", f"ÉCHEC : {e}"]))
        return 1
    j += [f"- Texte écrit : {h(t2.encode())} ({len(t2.encode())} octets, {t2.count(chr(10))} lignes)", ""]
    # 3. contrôles, puis artefacts
    with tempfile.TemporaryDirectory() as d:
        ctl = Controles(t1, couples, ep, numero, Path(d))
        # couples seuls : aucun ne touche une section gelée, sauf N-1 (Plan d'analyse)
        j.append("## Couples appliqués seuls au candidat 1 (sections gelées touchées)")
        j.append("")
        s1 = tranches(t1)
        for x in couples:
            seul = tranches(t1.replace(x["ancien"], x["nouveau"], 1))
            touchees = [g for g in GELEES if seul.get(g) != s1[g]]
            attendu = ["Plan d'analyse"] if x["id"] == N1 else []
            j.append(f"- {x['id']} : {touchees or 'aucune'}{'' if touchees == attendu else ' — ÉCART'}")
            if touchees != attendu:
                echecs.append(f"{x['id']} touche {touchees}")
        j += ["", "## Contrôles sur le texte écrit", ""]
        res = ctl.tout(t2)
        for nom, ok, det in res:
            j.append(f"- {'OK' if ok else 'KO'} {nom}" + (f" — {det}" if det else ""))
            if not ok:
                echecs.append(nom)
        j += ["", "Sortie du module commun (`valeurs`) : " + ctl.sortie_valeurs, "",
              "Sortie du harnais des blocs textuels (partie textuelle seulement : « présent, scellé » des messages "
              "recopiés du bloc 14 et la présence des pièces à S ne sont pas vérifiés ici — pièces : épingles "
              "proposées et journal de la construction) :", "", "```", ctl.sortie_harnais.rstrip(), "```", "",
              "## Artefacts (R5 : chaque contrôle doit échouer sur son artefact)", ""]
        for nom, ta, prefixe in artefacts(t2, ep):
            ra = ctl.tout(ta)
            vise = [x for x in ra if x[0].startswith(prefixe)]
            ok = bool(vise) and not any(x[1] for x in vise)
            j.append(f"- {'OK' if ok else 'KO'} {nom} : « {prefixe}… » en échec ({len(vise)} contrôle(s) visé(s))")
            if not ok:
                echecs.append(f"artefact non détecté : {nom}")
        j += ["", "## Empreintes des sections gelées (12 premiers caractères)", "",
              "| section | candidat 1 | ce texte |", "|---|---|---|"]
        s2 = tranches(t2)
        for g in GELEES:
            j.append(f"| {g} | `{h(s1[g].encode())[:12]}` | `{h(s2[g].encode())[:12]}` |")
    j.append("")
    if echecs:
        print("\n".join(j + ["ÉCHEC : " + " ; ".join(echecs), "Rien n'est écrit."]))
        return 1
    j.append(f"Empreinte du texte écrit (`{texte_sortie}`) : {h(t2.encode())}"
             + ("" if a_blanc else " — valeur de l'épingle `CANDIDAT_RELU` (P-5), jamais citée par le texte"))
    j.append("CANDIDAT 2 : CONFORME" if not a_blanc else "SORTIE À BLANC : CONFORME")
    for p in sorties:
        p.parent.mkdir(parents=True, exist_ok=True)
    (racine / texte_sortie).write_text(t2, encoding="utf-8")
    (racine / journal_sortie).write_text("\n".join(j) + "\n", encoding="utf-8")
    for p in sorties:
        print(f"{sceller(p)}  {p}")
    print(j[-1])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
