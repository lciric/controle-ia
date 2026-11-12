"""Écrit la version 2 du document « le programme expliqué depuis zéro » à partir de la version 1, des couples de sa
contre-lecture et des couples du rédacteur de la version 2 (v1 de ce script).

Usage (depuis la racine du dépôt) :
  .venv/bin/python -I docs/notes/rapports-directeur/programme-depuis-zero-v2-faire-v1.py \
      [--sortie CHEMIN.html] [--essai-artefact double|absent|chiffre|copie]

Contrôles, dans l'ordre ; le premier qui échoue arrête tout avant la moindre écriture (code 2) :
  1. empreintes : la version 1 et la contre-lecture sont égales aux empreintes écrites dans le fichier de couples ;
  2. copie fidèle : les 47 couples de la contre-lecture sont relus dans son fichier (blocs « Texte actuel » et
     « Texte corrigé ») et doivent être égaux, mot pour mot et dans l'ordre, aux champs « actuel » et
     « corrige_contre_lecture » du fichier de couples ; un couple appliqué autrement que son texte corrigé doit porter
     un « ecart » écrit ;
  3. chaque texte actuel des 47 couples de la contre-lecture apparaît exactement une fois dans la version 1 ;
  4. application dans l'ordre du fichier : au moment de son application, chaque texte actuel (contre-lecture comme
     rédacteur) apparaît exactement une fois dans le texte courant, sinon refus ;
  5. aucun texte actuel d'un couple de la contre-lecture ne subsiste dans la sortie (sauf s'il est contenu dans le
     texte qui le remplace) ;
  6. couples marqués « exemple » : chaque nombre décimal écrit (virgule décimale) doit sortir du script de l'exemple
     chiffré v2, relancé ici, à l'arrondi écrit près, tel quel ou en pourcentage ; ce script doit finir en code 0 (sa
     propre garde vérifie que l'horizon de 200 reproduit la sortie de sa version 1).
La sortie n'est jamais écrite par-dessus un fichier scellé (compagnon .sha256 présent) ; sans --sortie, rien n'est écrit.
--essai-artefact : rejoue les contrôles sur un artefact injecté en mémoire (texte actuel dédoublé, texte actuel absent,
chiffre de l'exemple faussé, couple de la contre-lecture altéré) et attend un refus (règle R5) ; n'écrit rien.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
COUPLES = os.path.join(ICI, "programme-depuis-zero-v2-couples-v1.json")
SCRIPT_EXEMPLE = os.path.join(ICI, "exemple-chiffre-depuis-zero-v2.py")
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", ".."))


class Refus(Exception):
    pass


def sha256(octets):
    return hashlib.sha256(octets).hexdigest()


def lire_couples_contre_lecture(texte):
    """Les couples de la contre-lecture, dans l'ordre : (constat, numéro, actuel, corrigé)."""
    blocs = re.split(r"^### Constat (\d+) — ([^—]+?) — ", texte, flags=re.M)
    sortie = []
    for i in range(1, len(blocs), 3):
        n, corps = int(blocs[i]), blocs[i + 2]
        actuels = re.findall(r"^Texte actuel(?: (\d))? :\n\n```\n(.*?)\n```", corps, flags=re.M | re.S)
        corriges = re.findall(r"^Texte corrigé(?: (\d))? :\n\n```\n(.*?)\n```", corps, flags=re.M | re.S)
        if len(actuels) != len(corriges):
            raise Refus(f"constat {n} : {len(actuels)} textes actuels pour {len(corriges)} textes corrigés")
        for (ka, a), (kc, c) in zip(actuels, corriges):
            if ka != kc:
                raise Refus(f"constat {n} : numéros de couple discordants ({ka!r}, {kc!r})")
            sortie.append((n, int(ka) if ka else 1, a, c))
    return sortie


def nombres_sortie(texte):
    return [float(x) for x in re.findall(r"-?\d+\.\d+", texte)]


def nombre_sort_du_script(ecrit, valeurs):
    """Vrai si le nombre écrit (virgule décimale) est un arrondi d'une valeur du script, telle quelle ou × 100."""
    entier, decimales = ecrit.split(",")
    x = float(f"{entier}.{decimales}")
    demi = 0.5 * 10 ** (-len(decimales)) + 1e-12
    return any(abs(y - x) <= demi or abs(100.0 * y - x) <= demi for y in valeurs)


def controler(v1, texte_cl, doc, sortie_exemple, journal):
    # 1. Empreintes.
    if sha256(v1.encode("utf-8")) != doc["source"]["sha256"]:
        raise Refus("version 1 : empreinte différente de celle du fichier de couples")
    if sha256(texte_cl.encode("utf-8")) != doc["contre_lecture"]["sha256"]:
        raise Refus("contre-lecture : empreinte différente de celle du fichier de couples")
    journal.append("1. empreintes de la version 1 et de la contre-lecture : conformes")
    # 2. Copie fidèle des 47 couples.
    lus = lire_couples_contre_lecture(texte_cl)
    cl = [c for c in doc["couples"] if c["origine"] == "contre-lecture"]
    if len(lus) != doc["contre_lecture"]["couples"] or len(cl) != len(lus):
        raise Refus(f"nombre de couples : {len(lus)} dans la contre-lecture, {len(cl)} dans le fichier")
    for (n, k, a, c), e in zip(lus, cl):
        if (e["constat"], e["numero"], e["actuel"], e["corrige_contre_lecture"]) != (n, k, a, c):
            raise Refus(f"{e['id']} : différent du couple {n}-{k} de la contre-lecture")
        if e["applique"] != e["corrige_contre_lecture"] and not e.get("ecart"):
            raise Refus(f"{e['id']} : appliqué autrement que son texte corrigé sans écart écrit")
    journal.append(f"2. copie fidèle des {len(lus)} couples de la contre-lecture : conforme")
    # 3. Unicité dans la version 1.
    for e in cl:
        k = v1.count(e["actuel"])
        if k != 1:
            raise Refus(f"{e['id']} : texte actuel présent {k} fois dans la version 1 (exactement une fois exigé)")
    journal.append("3. chaque texte actuel de la contre-lecture présent exactement une fois dans la version 1 : conforme")
    # 4. Application.
    texte = v1
    for e in doc["couples"]:
        k = texte.count(e["actuel"])
        if k != 1:
            raise Refus(f"{e['id']} : texte actuel présent {k} fois au moment de son application")
        texte = texte.replace(e["actuel"], e["applique"], 1)
        etat = "appliqué" if e["applique"] == e.get("corrige_contre_lecture", e["applique"]) else "appliqué, adapté"
        journal.append(f"4. {e['id']} ({e['origine']}) : {etat}")
    # 5. Aucun texte actuel de la contre-lecture ne subsiste.
    for e in cl:
        if e["actuel"] not in e["applique"] and e["actuel"] in texte:
            raise Refus(f"{e['id']} : le texte actuel subsiste dans la sortie")
    journal.append("5. aucun texte actuel de la contre-lecture ne subsiste dans la sortie : conforme")
    # 6. Nombres de l'exemple.
    valeurs = nombres_sortie(sortie_exemple)
    n_verifies = 0
    for e in doc["couples"]:
        if not e.get("exemple"):
            continue
        for ecrit in re.findall(r"\d+,\d+", e["applique"]):
            if not nombre_sort_du_script(ecrit, valeurs):
                raise Refus(f"{e['id']} : le nombre {ecrit} ne sort pas du script de l'exemple chiffré v2")
            n_verifies += 1
    journal.append(f"6. nombres des couples « exemple » : {n_verifies} nombres, tous sortis du script v2 : conforme")
    return texte


def lancer_exemple():
    proc = subprocess.run([sys.executable, "-I", SCRIPT_EXEMPLE], capture_output=True, text=True, cwd=RACINE)
    if proc.returncode != 0:
        raise Refus(f"script de l'exemple chiffré v2 : code {proc.returncode}\n{proc.stdout}\n{proc.stderr}")
    return proc.stdout


def artefact(nature, v1, texte_cl, doc):
    doc = json.loads(json.dumps(doc))
    if nature == "double":
        v1 = v1 + doc["couples"][0]["actuel"]
    elif nature == "absent":
        e = next(c for c in doc["couples"] if c["origine"] != "contre-lecture")
        e["actuel"] = e["actuel"] + " [texte qui n'existe pas]"
    elif nature == "chiffre":
        e = next(c for c in doc["couples"] if c["id"] == "R07")
        e["applique"] = e["applique"].replace("0,2845", "0,2945")
    elif nature == "copie":
        e = doc["couples"][5]
        e["corrige_contre_lecture"] = e["corrige_contre_lecture"] + " "
    return v1, texte_cl, doc


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sortie")
    p.add_argument("--essai-artefact", choices=("double", "absent", "chiffre", "copie"))
    a = p.parse_args()
    with open(COUPLES, "rb") as f:
        octets_couples = f.read()
    doc = json.loads(octets_couples.decode("utf-8"))
    with open(os.path.join(RACINE, doc["source"]["chemin"]), encoding="utf-8", newline="") as f:
        v1 = f.read()
    with open(os.path.join(RACINE, doc["contre_lecture"]["chemin"]), encoding="utf-8", newline="") as f:
        texte_cl = f.read()
    print(f"fichier de couples : {os.path.relpath(COUPLES, RACINE)} sha256 {sha256(octets_couples)}")
    with open(SCRIPT_EXEMPLE, "rb") as f:
        print(f"script de l'exemple : {os.path.relpath(SCRIPT_EXEMPLE, RACINE)} sha256 {sha256(f.read())}")
    sortie_exemple = lancer_exemple()
    journal = []
    if a.essai_artefact:
        v1_a, cl_a, doc_a = artefact(a.essai_artefact, v1, texte_cl, doc)
        if a.essai_artefact == "double":
            doc_a["source"]["sha256"] = sha256(v1_a.encode("utf-8"))
        try:
            controler(v1_a, cl_a, doc_a, sortie_exemple, journal)
        except Refus as r:
            print(f"artefact « {a.essai_artefact} » refusé, comme attendu : {r}")
            return 0
        print(f"artefact « {a.essai_artefact} » NON refusé : garde défaillante")
        return 1
    try:
        texte = controler(v1, texte_cl, doc, sortie_exemple, journal)
    except Refus as r:
        print("REFUS :", r)
        return 2
    for ligne in journal:
        print(ligne)
    n_cl = sum(1 for c in doc["couples"] if c["origine"] == "contre-lecture")
    n_adapt = sum(1 for c in doc["couples"] if c["origine"] == "contre-lecture"
                  and c["applique"] != c["corrige_contre_lecture"])
    n_red = len(doc["couples"]) - n_cl
    print(f"bilan : {n_cl} couples de la contre-lecture appliqués ({n_cl - n_adapt} tels quels, {n_adapt} adaptés, "
          f"0 non appliqué) ; {n_red} couples du rédacteur ; sortie sha256 {sha256(texte.encode('utf-8'))}")
    if a.sortie:
        if os.path.exists(a.sortie + ".sha256"):
            print("REFUS : la sortie est scellée (compagnon .sha256 présent) ; on n'écrase jamais (R12)")
            return 2
        with open(a.sortie, "w", encoding="utf-8", newline="") as f:
            f.write(texte)
        print(f"écrit : {a.sortie}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
