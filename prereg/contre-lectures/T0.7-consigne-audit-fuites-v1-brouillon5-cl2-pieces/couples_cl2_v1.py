"""Couples « ancien → nouveau » proposés par la contre-lecture 2 (brouillon 5 de la consigne de l'audit des fuites de T0.7).
Écrit le fichier JSON des couples et vérifie : chaque « ancien » présent une fois dans le brouillon 5 au moment de son
remplacement ; défaire redonne le brouillon 5 à l'octet. N'écrit aucun brouillon dans le dépôt."""
import hashlib, json, sys
B5 = "brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon5.md"
SHA = "7228ce724d4f2a7c146124ceb70156cf99118b2acebcdc4b3b7d9e5d977d2b67"
C = [
 ("K01", "exigé", "CL2-06 : la ligne CODE-T07 cite un fichier, pas un commit ; ce fichier entre dans la liste fermée",
  "lues comme dit au § 4 (« Lecture du registre »).",
  "lues comme dit au § 4 (« Lecture du registre ») ; si la ligne `CODE-T07` est présente, le fichier qu'elle cite\n"
  "   (`registres/code-t07/CODE-T07-v2.json` le 11 novembre 2026), ouvert par son chemin exact après contrôle de son\n"
  "   empreinte contre la ligne, dont seuls le champ `commit` et l'entrée `fichiers` de\n"
  "   `src/controle_ia/t07/criteres_v1.py` sont lus."),
 ("K02", "exigé", "CL2-06 : d'où vient le commit du validateur",
  "le commit cité par la ligne `CODE-T07` si elle existe, sinon `8ae9fc44`",
  "le commit écrit au champ `commit` du fichier que cite la ligne `CODE-T07` si elle existe (la ligne porte un chemin et\n"
  "   une empreinte, pas un commit : point 2 ; l'empreinte de `criteres_v1.py` doit aussi égaler l'entrée `fichiers` de ce\n"
  "   fichier, sinon arrêt), sinon `8ae9fc44`"),
 ("K03", "exigé", "CL2-07 (Q-B5-3) : écritures hors du dépôt, dans le bac à sable",
  "Aucun autre chemin n'est écrit.",
  "Aucun autre chemin du dépôt n'est écrit ; hors du dépôt, seuls\n"
  "le bac à sable de l'auditeur (`TMPDIR`, § 7 ; les trois fichiers du découpeur, § 6.1) et celui du contre-lecteur du\n"
  "fichier (fichiers de rejeu, § 3) sont écrits, et chacun cite le chemin du sien dans son rapport."),
 ("K14", "exigé", "CL2-05 : numéros de ligne de la réception R1 v4 (les trois empreintes sont aux l. 71-73)",
  "etape-E-reception-r1-v4-v1.md` l. 70-72,", "etape-E-reception-r1-v4-v1.md` l. 71-73,"),
 ("K04", "facultatif", "CL2-08 : le point 8 de la liste fermée dit encore « chemin donné par la mère »",
  "8. Le découpeur du modèle de 7b, au chemin donné par la mère (`CHEMIN_DECOUPEUR`, § 6.1), et rien d'autre de ce dossier.",
  "8. Le découpeur du modèle de 7b : les trois fichiers nommés au § 6.1, lus par `git show` au commit et au dossier écrits\n"
  "   là, puis leurs copies dans le bac à sable ; rien d'autre de ce dossier ni de cette branche."),
 ("K05", "facultatif", "CL2-09 : chemin et empreinte du texte scellé dans la liste fermée",
  "7. T0.7 : les seules lignes recopiées au § 2,",
  "7. T0.7 scellé (`prereg/T0.7-sondes-v0-v1.md`, `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5`, égal à\n"
  "   son compagnon, sinon arrêt) : les seules lignes recopiées au § 2,"),
 ("K06", "facultatif", "CL2-09 : « en vigueur » → texte scellé (§ 7)",
  "cellules du § 2 égales au texte de T0.7 en vigueur", "cellules du § 2 égales au texte scellé de T0.7"),
 ("K07", "facultatif", "CL2-09 : « en vigueur » → texte scellé (§ 10)",
  "Cellules du § 2 différentes au texte de T0.7 en vigueur", "Cellules du § 2 différentes au texte scellé de T0.7"),
 ("K08", "facultatif", "CL2-10 : renvoi aux lignes du brouillon 21, repère du texte scellé",
  "(même contrôle que le module, T0.7 l. 2078)", "(même contrôle que le module, T0.7 l. 2078 au brouillon 21, l. 2199 au texte scellé)"),
 ("K09", "facultatif", "CL2-10 : idem",
  "A, T0.7 l. 2046). Ligne", "A, T0.7 l. 2046 au brouillon 21, l. 2166 au texte scellé ; les renvois de ce § 4 à T0.7 sont en lignes du\n  brouillon 21). Ligne"),
 ("K10", "facultatif", "CL2-10 : idem",
  "l'étape A (T0.7 l. 2046), elle-même", "l'étape A (T0.7 l. 2046 ; texte scellé l. 2166), elle-même"),
 ("K11", "facultatif", "CL2-10 : idem",
  "(garde d'ordre, l. 2047-2050)", "(garde d'ordre, l. 2047-2050 ; texte scellé l. 2167-2170)"),
 ("K12", "facultatif", "CL2-10 : idem",
  "(étape A, l. 1385-1390)", "(étape A, l. 1385-1390 ; texte scellé l. 1527-1532)"),
 ("K13", "facultatif", "CL2-11 : R5, fichier du découpeur absent ou vide",
  "empreinte du découpeur fausse → arrêt ;", "empreinte du découpeur fausse, ou fichier du découpeur absent ou vide (`git show` en échec) → arrêt ;"),
]
h = lambda b: hashlib.sha256(b).hexdigest()
src = open(B5, "rb").read(); assert h(src) == SHA, "brouillon 5 : empreinte"
def jouer(choix):
    t = src.decode("utf-8")
    for i, g, m, a, n in choix:
        k = t.count(a); assert k == 1, (i, "ancien", k); t = t.replace(a, n)
    u = t
    for i, g, m, a, n in reversed(choix):
        k = u.count(n); assert k == 1, (i, "nouveau", k); u = u.replace(n, a)
    assert u.encode() == src, "retour"
    return h(t.encode())
ex = [c for c in C if c[1] == "exigé"]
print("couples exigés seuls :", len(ex), "→ sha256 du texte obtenu (repère, rien d'écrit) :", jouer(ex))
print("tous les couples    :", len(C), "→ sha256 du texte obtenu (repère, rien d'écrit) :", jouer(C))
print("chaque « ancien » présent une fois ; défaire redonne le brouillon 5 à l'octet :", SHA)
out = {"de": {"chemin": B5, "sha256": SHA}, "regle": "appliqués dans l'ordre, chaque « ancien » présent une fois ; défaits du dernier au premier, ils redonnent le brouillon 5 à l'octet",
       "couples": [{"id": i, "statut": g, "motif": m, "ancien": a, "nouveau": n} for i, g, m, a, n in C]}
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1) + "\n"); print("écrit :", sys.argv[1])
