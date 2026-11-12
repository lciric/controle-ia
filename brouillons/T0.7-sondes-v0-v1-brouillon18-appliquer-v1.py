"""T0.7 sondes v0, brouillon 18 : application des couples au brouillon 17 et vérifications (v1).

Rédacteur du brouillon 18 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), 10 novembre 2026 ;
consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/consigne-redaction-t07-brouillon18-v1.md` (`f4fd33fc…`).
Bibliothèque standard, plus `controle_ia.prereg` du dépôt (lu dans RACINE/src) ; aucun réseau, aucune clé, aucun appel externe.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie l'empreinte du brouillon 17 (`65efe32f…`) ;
2. applique dans l'ordre les couples de `brouillons/T0.7-sondes-v0-v1-brouillon18-couples-v1.json` : chaque « ancien » doit être
   présent exactement une fois dans le texte au moment de son application, sinon arrêt (code 1), rien n'est écrit ;
3. écrit `brouillons/T0.7-sondes-v0-v1-brouillon18.md` (R12 : refuse d'écraser un fichier différent ; un fichier identique est
   accepté) ;
4. vérifie : sections (a) à (d) de « Écrits exigés par P3-bis » égales octet pour octet au brouillon 17 ; sections de l'empan
   « Hypothèse » à « Liste d'arrêt » inchangées, sauf « Règle « mots et coût » de T0.6 », touchée par le seul couple déclaré
   (B18-09) ; marqueurs restants = les sept laissés ; `controle_ia.prereg.problemes` réduit à la ligne de ces marqueurs ; liste
   vide à valeurs factices (copie dans DOSSIER_TEMPORAIRE, ou un dossier temporaire neuf) ; phrases de la déclaration de
   l'écart DT-4 présentes ; ancienne affirmation en gras absente.
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

SHA_B17 = "65efe32f933d35bfc2c1415e382264327d6797912a1c02d8e753f6465d7c9275"
LAISSES = ["<<EMPREINTE_CONFIG_T07>>", "<<EMPREINTE_PREREG_T06>>", "<<ENTROPIE_T07>>", "<<GO_ETAPE_A_T07>>",
           "<<MOT_LAZAR_P064>>", "<<MOT_LAZAR_P065>>", "<<NIVEAU_BASE_T06>>"]
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
TOUCHEE_DECLAREE = "Règle « mots et coût »"
PHRASES_DT4 = (
    "la chaîne de 7a a calculé des sondes sur l'instance",
    "le lecteur exploratoire de 7a en a vu des valeurs par accident",
    "ce lecteur est **exclu de T0.6, T0.7, P3-bis et G0**",
    "**sa lecture B est en quarantaine**",
    "**audit et complément : « aucune trace trouvée »**",
    "**ouvre le fichier des sondes**",
    "il **reste interdit** sur les arbres de 7a et de 7b **jusqu'au verdict scellé de P3-bis**",
    "**aucune lecture de T0.7 ne porte sur les sondes de 7a**",
)
ANCIENNE_AFFIRMATION = "**aucune sonde de ce texte ni aucune sonde figée de P3 n'est passée sur les activations de 7a**"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sections(texte: str) -> dict:
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {titre.strip(): corps for titre, corps in zip(morceaux[1::2], morceaux[2::2])}


def bloc_ecrits(texte: str) -> str:
    i = texte.index("### (a) Périmètre fermé des clés")
    j = texte.index("### (e) Grille de lecture")
    return texte[i:j]


def section_de(texte: str, position: int) -> str:
    titres = [(m.start(), m.group(1)) for m in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M)]
    nom = "(avant la première section)"
    for p, t in titres:
        if p <= position:
            nom = t
    return nom[:70]


def main(argv: list) -> int:
    if not 1 <= len(argv) <= 2:
        print("usage : RACINE [DOSSIER_TEMPORAIRE]", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # noqa: E402

    b17 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon17.md"
    couples_chemin = racine / "brouillons/T0.7-sondes-v0-v1-brouillon18-couples-v1.json"
    b18 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon18.md"
    defauts = []

    brut = b17.read_bytes()
    if sha(brut) != SHA_B17:
        print(f"ARRÊT : empreinte du brouillon 17 {sha(brut)} ≠ {SHA_B17}")
        return 1
    print(f"brouillon 17 : {b17.relative_to(racine)} {SHA_B17} (égale)")
    texte17 = brut.decode("utf-8")
    cbrut = couples_chemin.read_bytes()
    couples = json.loads(cbrut.decode("utf-8"))
    print(f"couples : {couples_chemin.relative_to(racine)} {sha(cbrut)} ({len(couples)} couples)")

    # 2. application
    t = texte17
    print("\n# application (id ; occurrences de l'« ancien » ; ligne d'application dans le texte courant ; section ; gelée)")
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1:
            print(f"ARRÊT : {c['id']} : « ancien » présent {n} fois (1 attendu) ; rien n'est écrit")
            return 1
        if c["ancien"] == c["nouveau"]:
            print(f"ARRÊT : {c['id']} : « nouveau » égal à « ancien »")
            return 1
        p = t.index(c["ancien"])
        print(f"{c['id']} ; 1 ; l. {t.count(chr(10), 0, p) + 1} ; {section_de(t, p)} ; {'oui' if c['section_gelee'] else 'non'}")
        t = t.replace(c["ancien"], c["nouveau"], 1)
    texte18 = t

    # 3. écriture (R12)
    octets18 = texte18.encode("utf-8")
    if b18.exists():
        if b18.read_bytes() != octets18:
            print(f"ARRÊT (R12) : {b18.relative_to(racine)} existe et diffère : rien n'est écrasé")
            return 1
        print(f"\n{b18.relative_to(racine)} déjà écrit, identique")
    else:
        b18.write_bytes(octets18)
        print(f"\nécrit : {b18.relative_to(racine)}")
    print(f"brouillon 18 : {sha(octets18)} ; {texte18.count(chr(10))} lignes")

    # 4. vérifications
    print("\n# vérifications")
    if bloc_ecrits(texte17) == bloc_ecrits(texte18):
        print("(1) sections (a) à (d) de « Écrits exigés par P3-bis » : égales octet pour octet au brouillon 17")
    else:
        defauts.append("sections (a) à (d) changées")
    s17, s18 = sections(texte17), sections(texte18)
    neuves = [k for k in s18 if k not in s17]
    disparues = [k for k in s17 if k not in s18]
    changees = [k for k in s17 if k in s18 and s17[k] != s18[k]]
    print(f"(2) sections neuves : {neuves} ; disparues : {disparues}")
    print(f"    sections changées ({len(changees)}) :")
    for k in changees:
        gele = any(k.startswith(g) for g in EMPAN_GELE)
        print(f"      - {k[:90]}{'  [EMPAN GELÉ]' if gele else ''}")
    geles_touchees = [k for k in changees if any(k.startswith(g) for g in EMPAN_GELE)]
    if [k for k in geles_touchees if not k.startswith(TOUCHEE_DECLAREE)]:
        defauts.append(f"section de l'empan gelé touchée hors déclaration : {geles_touchees}")
    for k in geles_touchees:
        diff = [l for l in difflib.unified_diff(s17[k].split("\n"), s18[k].split("\n"), lineterm="", n=0)
                if l[:1] in "+-" and not l.startswith(("+++", "---"))]
        print(f"    empan gelé, « {k[:40]}… » : {len(diff)} lignes de différence (couple B18-09, substitution du marqueur) :")
        for l in diff:
            print(f"      {l}")
    if neuves != ["Table « ce qui change du 17 au 18 »"] or disparues:
        defauts.append("sections neuves ou disparues inattendues")
    restes = sorted(set(GABARIT.findall(texte18)))
    comptes = {m: texte18.count(m) for m in restes}
    print(f"(3) marqueurs restants : {len(restes)} : {comptes}")
    if restes != sorted(LAISSES):
        defauts.append(f"marqueurs restants {restes} ≠ {sorted(LAISSES)}")
    p = problemes(b18)
    attendu = [f"marqueurs de gabarit restants : {', '.join(sorted(LAISSES))}"]
    print(f"(4) controle_ia.prereg.problemes(brouillon 18) : {p}")
    if p != attendu:
        defauts.append("problemes ≠ la seule ligne des marqueurs laissés")
    dossier = Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-b18-factice-"))
    dossier.mkdir(parents=True, exist_ok=True)
    factice = texte18
    for m in LAISSES:
        factice = factice.replace(m, "valeur-factice-" + m.strip("<>").lower())
    copie = dossier / "T0.7-sondes-v0-v1-brouillon18-valeurs-factices.md"
    copie.write_text(factice, encoding="utf-8")
    pf = problemes(copie)
    print(f"(5) à valeurs factices ({copie}) : problemes = {pf}")
    if pf:
        defauts.append("problemes non vide à valeurs factices")
    plat = " ".join(texte18.split())
    manquantes = [ph for ph in PHRASES_DT4 if ph not in plat]
    print(f"(6) déclaration de l'écart DT-4 : {len(PHRASES_DT4) - len(manquantes)} phrases sur {len(PHRASES_DT4)} présentes"
          f"{' ; manquantes : ' + repr(manquantes) if manquantes else ''}")
    if manquantes:
        defauts.append("phrases de la déclaration DT-4 manquantes")
    if ANCIENNE_AFFIRMATION in plat:
        defauts.append("ancienne affirmation en gras encore présente")
    print(f"    ancienne affirmation en gras présente : {ANCIENNE_AFFIRMATION in plat}")
    diff = [l for l in difflib.unified_diff(texte17.split("\n"), texte18.split("\n"), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    print(f"(7) différentiel 17 → 18 : {sum(1 for l in diff if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in diff if l[0] == '+')} lignes ajoutées")

    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
