"""Essai ciblé (barreau 6, brouillon 1) : la garde de T0.7 face aux clés candidates du barreau 6. Lecture seule du module de
T0.7 (`src/controle_ia/t07/registre_v1.py`) et de `registres/scellements-v1.md` ; registres jouets écrits dans un dossier
temporaire, effacé à la fin ; aucun fichier du dépôt n'est écrit.
Lancement : `python3 -I -B <chemin absolu de ce script>` (interpréteur du dépôt, `.venv/bin/python`)."""
import sys, hashlib, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.t07 import registre_v1 as rg

_tmp = tempfile.TemporaryDirectory()
ici = Path(_tmp.name)
print("registre_v1.py sha256 :", hashlib.sha256(Path(rg.__file__).read_bytes()).hexdigest())
MARQUES = ("T06", "T08", "P3BIS", "NARC")   # liste fixée par T0.7 (brouillon 18, marqueur CLES_REGISTRE_PARTAGE ; brouillon 22)
for cle in ("SCELLEMENT-ACCB6", "CODE-ACCB6", "LECTURE-ACCB6", "SCELLEMENT-ACCUMULATION-B6", "SCELLEMENT-B6-T07",
            "SCELLEMENT-ACCUMULATION-B6-T08", "SCELLEMENT-ACCUMULATION-B6-T06"):
    print(f"classer_cle_inconnue({cle!r}) ->", rg.classer_cle_inconnue(cle, MARQUES))

# Registre jouet : copie des lignes présentes de registres/scellements-v1.md + une ligne RUN-CONFIRMATION-T06 fictive
source = Path("/home/user/controle-ia-travail/registres/scellements-v1.md").read_text(encoding="utf-8")
fictive = "| RUN-CONFIRMATION-T06 | 2026-11-13T00:00:00Z | runs/jouet/manifeste.json | " + "0" * 64 + " |\n"
sain = ici / "registre-jouet-sain.md"
sain.write_text(source + fictive, encoding="utf-8")
artefact = ici / "registre-jouet-artefact.md"
artefact.write_text(source + fictive + "| SCELLEMENT-ACCB6 | 2026-11-12T00:00:00Z | prereg/accumulation-barreau6-v1.md | " + "1" * 64 + " |\n",
                    encoding="utf-8")
propre = ici / "registre-jouet-accb6.md"
propre.write_text("# Registre propre du barreau 6 (jouet)\n\n| SCELLEMENT-ACCB6 | 2026-11-12T00:00:00Z | prereg/accumulation-barreau6-v1.md | "
                  + "1" * 64 + " |\n", encoding="utf-8")
for nom, reg in (("cas sain (registre partagé, sans clé du barreau 6)", sain),
                 ("artefact (registre partagé + SCELLEMENT-ACCB6)", artefact)):
    for etape, ex, pe, rf in (("A", rg.EXIGEES_ETAPE_A, rg.PERMISES_ETAPE_A, rg.REFUSEES_ETAPE_A),
                              ("B", rg.EXIGEES_ETAPE_B, rg.PERMISES_ETAPE_B, {})):
        try:
            lignes, ignorees = rg.lire_registre_detail(reg, ex, pe, rf, MARQUES)
            print(f"{nom}, étape {etape} : lu sans refus ; clés lues {sorted(lignes)} ; ignorées {ignorees}")
        except rg.RefusRegistre as e:
            print(f"{nom}, étape {etape} : REFUS : {e}")
print("registre propre du barreau 6 : T0.7 ne lit que", rg.REGISTRE_DEFAUT, "; le fichier", propre.name, "n'est lu par aucune fonction de T0.7")
print("registres/scellements-v1.md sha256 au moment de l'essai :",
      hashlib.sha256(Path("/home/user/controle-ia-travail/registres/scellements-v1.md").read_bytes()).hexdigest())
_tmp.cleanup()
