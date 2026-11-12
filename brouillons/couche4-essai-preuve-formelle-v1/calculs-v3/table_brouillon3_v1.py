"""table_brouillon3_v1.py — refait la table des empreintes du brouillon 3 (fichiers du dépôt seulement, plus la référence locale
des prix nommée comme telle) et contrôle quelques invariants. Lancer depuis la racine du dépôt. Aucun appel, aucun réseau."""
import hashlib
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
D = "brouillons/couche4-essai-preuve-formelle-v1"
F = Path(f"{D}/essai-preuve-formelle-devis-v1-brouillon3.md")
T = F.read_text(encoding="utf-8")
lignes = [
    ("docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-devis-essai-preuve-formelle-couche4-v1.md", "consigne ; lue en entier"),
    ("docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md", "interdits communs v2, recopiés dans la consigne"),
    ("prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md", "contre-lecture 1 (Fable 5.2) ; source des 14 couples"),
    ("prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md", "vérification courte du brouillon 2 (Fable 5.2) ; lue en entier ; VL-01 à VL-08"),
    (f"{D}/essai-preuve-formelle-devis-v1-brouillon1.md", "brouillon 1, intact"),
    (f"{D}/essai-preuve-formelle-devis-v1-journal-v1.md", "journal v1, intact"),
    (f"{D}/essai-preuve-formelle-devis-v1-brouillon2.md", "brouillon 2, intact ; texte de départ des retouches S01 à S38"),
    (f"{D}/essai-preuve-formelle-devis-v1-journal-v2.md", "journal v2, intact"),
    ("docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md", "synthèse du tour 2 (brouillon 1)"),
    ("docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-v2.md", "synthèse v2 (brouillon 1)"),
    ("docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v2.md", "programme complet v2 (brouillon 1)"),
    ("docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py", "table des prix, l. 60–95"),
    ("docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html", "page de prix archivée : Gemini 4 Argon, 2 / 10 puis 4 / 20 dès le 1er décembre 2026"),
    ("brouillons/entretien-taif-v3/programme-entretien-taif-v16.md", "carte des hypothèses v1 citée, l. 384–388, 436–440, 800–810"),
    ("brouillons/P3-chaine-v1-brouillon4/lancer_p3_v1.sh", "l. 44 : prix horaire de borne haute (1,30 USD l'heure)"),
    ("prereg/gabarit-preregistrement-v1.md", "convention du marqueur « À REMPLIR » (l. 1–22)"),
    ("registres/decisions.md", "registre vivant (lignes lues pour le brouillon 1)"),
]
for sous in ("calculs-v1", "calculs-v2", "calculs-v3"):
    for p in sorted(Path(f"{D}/{sous}").glob("*")):
        if p.suffix != ".sha256" and p.is_file() and p.name != "sortie-table-brouillon3-v1.txt":
            lignes.append((str(p), {"calculs-v1": "brouillon 1 (copie versée par la mère)",
                                    "calculs-v2": "brouillon 2 (couples, devis v4, retouches R01 à R50, table)",
                                    "calculs-v3": "brouillon 3 (calibrage exact, devis v5, retouches S01 à S38, table)"}[sous]))
lignes.append(("/tmp/claude-0/bundled-skills/2.1.322/3f5d19faa48e8729fa23bef895bf9c5b/claude-api/shared/models.md",
               "référence locale de prix de l'outil `claude-api` (hors dépôt, non un fichier du rédacteur), l. 78, 80, 83, 89"))
out = ["## Table des empreintes (SHA-256, calculées par script à l'assemblage ; aucune valeur retapée)", "",
       "| Fichier | Rôle | SHA-256 | Compagnon |", "|---|---|---|---|"]
for chemin, role in lignes:
    p = Path(chemin)
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    c = Path(chemin + ".sha256")
    etat = (("égale au compagnon" if c.read_text().split()[0] == h else "**DIFFÉRENTE du compagnon**") if c.exists()
            else ("pas de compagnon (registre vivant)" if chemin.startswith("registres/") else "pas de compagnon"))
    out.append(f"| `{chemin}` | {role} | `{h}` | {etat} |")
date = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
out += ["",
        "**Traçabilité du brouillon 2 (VL-08)** : corps du brouillon 2 = jalon 3 (`ff92495600cd094b821652d2a53bab16858e22a2eae2be12463760be25651719`, "
        "reproductible par `calculs-v2/appliquer_couples_cl1_v1.py` depuis le brouillon 1 et la contre-lecture 1) + retouches R01 à R48 "
        "(`calculs-v2/retouches_brouillon2_v1.py`) + R49 (`calculs-v2/deplacer_bloc_c05_v1.py`) + R50 (`calculs-v2/deplacer_scenarios_c10_v1.py`) "
        "+ **R51, retouche faite à la main sans script** (formulation de l'avantage de D-1b : « pilote complet au profil supposé, et d'au moins 48 "
        "graines sur 60 au profil pire réaliste ») ; établi par rejeu par la vérification courte. Sa table des empreintes venait de "
        "`calculs-v2/table_et_controle_brouillon2_v1.py`. La sortie des retouches R01 à R48 (`5fd73ac8…`) est restée dans le bac à sable du rédacteur, "
        "non versée. **Brouillon 3** = brouillon 2 + retouches S01 à S38 (`calculs-v3/retouches_brouillon3_v1.py`) + la présente table.",
        "",
        f"Table assemblée par script le {date} (horloge du système, UTC). L'empreinte du présent brouillon est celle de son compagnon "
        "`.sha256`. Aucun fichier du bac à sable du rédacteur n'est cité.", ""]
i = T.index("\n---\n\n## Table des empreintes")
T = T[:i] + "\n---\n\n" + "\n".join(out)
F.write_text(T, encoding="utf-8")
# contrôles
assert "scratchpad" not in T
assert T.count("<<SOURCE_TANGO>>") >= 3, T.count("<<SOURCE_TANGO>>")
print(f"table : {len(lignes)} fichiers ; marqueurs « À REMPLIR » : {T.count('À REMPLIR')} ; <<SOURCE_TANGO>> : {T.count('<<SOURCE_TANGO>>')} ; "
      f"bac à sable cité : non ; écarts aux compagnons : {T.count('DIFFÉRENTE')}")
