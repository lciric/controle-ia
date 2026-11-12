"""Remplace la table des empreintes du brouillon 2 (copies versées au dépôt seulement) et contrôle la présence des couples."""
import hashlib, re, subprocess, sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, "brouillons/couche4-essai-preuve-formelle-v1/calculs-v2")
from appliquer_couples_cl1_v1 import lire_couples

D = "brouillons/couche4-essai-preuve-formelle-v1"
F = Path(f"{D}/essai-preuve-formelle-devis-v1-brouillon2.md")
CL = "prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md"
T = F.read_text(encoding="utf-8")
lignes = [
 ("docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-devis-essai-preuve-formelle-couche4-v1.md", "consigne ; lue en entier"),
 ("docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md", "interdits communs v2, recopiés dans la consigne"),
 (CL, "contre-lecture 1 (Fable 5.2) ; lue en entier ; source des 14 couples"),
 (f"{D}/essai-preuve-formelle-devis-v1-brouillon1.md", "brouillon 1, intact ; texte de départ des couples"),
 (f"{D}/essai-preuve-formelle-devis-v1-journal-v1.md", "journal du brouillon 1, intact"),
 ("docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md", "synthèse du tour 2 ; lue en entier (brouillon 1)"),
 ("docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-v2.md", "synthèse v2 ; lue en entier (brouillon 1)"),
 ("docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v2.md", "programme complet v2 ; parties lues (brouillon 1)"),
 ("docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py", "table des prix, l. 60–95"),
 ("brouillons/entretien-taif-v3/programme-entretien-taif-v16.md", "l. 384–388, 436–440, 800–810 (carte des hypothèses v1)"),
 ("brouillons/P3-chaine-v1-brouillon4/lancer_p3_v1.sh", "l. 44 : prix horaire de borne haute (1,30 USD l'heure)"),
 ("registres/decisions.md", "registre vivant : R-920, R-946, R-957, R-959, R-2199 à R-2226 (lus pour le brouillon 1)"),
]
for p in sorted(Path(f"{D}/calculs-v1").glob("*")):
    if p.suffix != ".sha256":
        lignes.append((str(p), "copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine)"))
for p in sorted(Path(f"{D}/calculs-v2").glob("*")):
    if p.suffix != ".sha256" and p.name != "__pycache__":
        lignes.append((str(p), "brouillon 2 : " + ("calculs v4 (C04, CLP-06, CLP-09, CLP-10)" if "calculs_devis" in p.name else
                       "sortie des calculs v4" if "sortie-calculs" in p.name else
                       "application programmatique des 14 couples" if p.name.startswith("appliquer") else
                       "sortie de l'application des couples")))
lignes.append(("/tmp/claude-0/bundled-skills/2.1.322/3f5d19faa48e8729fa23bef895bf9c5b/claude-api/shared/models.md",
               "référence locale de prix de l'outil `claude-api` (hors dépôt, non un fichier du rédacteur), l. 78, 80, 83, 89"))
out = ["## Table des empreintes (SHA-256, calculées par script à l'assemblage ; aucune valeur retapée)", "",
       "| Fichier | Rôle | SHA-256 | Compagnon |", "|---|---|---|---|"]
for chemin, role in lignes:
    p = Path(chemin)
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    c = Path(chemin + ".sha256")
    etat = ("égale au compagnon" if c.read_text().split()[0] == h else "**DIFFÉRENTE du compagnon**") if c.exists() else \
           ("pas de compagnon (registre vivant)" if chemin.startswith("registres/") else "pas de compagnon")
    out.append(f"| `{chemin}` | {role} | `{h}` | {etat} |")
date = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
out += ["", f"Table assemblée par script le {date} (horloge du système, UTC). L'empreinte du présent brouillon est celle de son "
        "compagnon `.sha256`. Aucun fichier du bac à sable du rédacteur n'est cité : les calculs et jalons du brouillon 1 le sont "
        "par leurs copies sous `calculs-v1/` (mêmes empreintes) ; les instantanés de jalon du brouillon 2 sont décrits au journal v2.", ""]
i = T.index("\n---\n\n## Table des empreintes")
T = T[:i] + "\n---\n\n" + "\n".join(out)
F.write_text(T, encoding="utf-8")
assert "scratchpad" not in T, "le bac à sable est encore cité"

# contrôle des couples
norm = lambda s: " ".join(s.split())
NT = norm(T)
couples = lire_couples(Path(CL).read_text(encoding="utf-8"))
MODIFS = {"C08": ("**Lignes absentes du tableau, comprises dans le plafond**",
                  "**Lignes absentes du tableau du brouillon 1, comprises dans le plafond** (estimation de la contre-lecture, reprise telle quelle ; le tableau ci-dessus les chiffre par le script v4)"),
          "C10": ("192 à 300 aux effectifs du devis)", "150 à 300 aux scénarios du devis v4)")}
for nom, constat, ancien, nouveau in couples:
    if nom == "C08":   # seul le paragraphe ajouté compte ; la phrase d'origine reprise par C08 (plafond 450) est remplacée (R42)
        nouveau = nouveau.split("\n\n")[0]
    attendu = norm(nouveau)
    if nom in MODIFS:
        a, b = MODIFS[nom]
        attendu = attendu.replace(norm(a), norm(b))
    n = NT.count(attendu)
    print(f"{nom} ({constat}) : texte du couple présent {n} fois" + (" (retouche documentée au journal)" if nom in MODIFS else ""))
    assert n == 1, nom
print("couples : 14 présents une fois ; table : ", len(lignes), "fichiers")
