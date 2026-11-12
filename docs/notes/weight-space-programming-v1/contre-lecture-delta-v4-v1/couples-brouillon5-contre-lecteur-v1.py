"""Couples L1 à L8 de la contre-lecture du delta v4 de SPARKS-EXP7-NUL (brouillon 4 → brouillon 5). Écrit le fichier des
couples s'il est absent (jamais d'écrasement), vérifie le brouillon 4 par empreinte, puis applique les couples dans l'ordre
sur une copie en mémoire (chaque « ancien » présent exactement une fois au moment de son application), exige les trois
marqueurs « À REMPLIR » et imprime l'empreinte du texte d'essai (non versé).

    python3 -I -B couples-brouillon5-contre-lecteur-v1.py RACINE_DU_DEPOT
"""
import hashlib
import json
import sys
from pathlib import Path

SHA_B4 = "925c11fe58fe157e2343d5d36b816aacbdeb0f677d63afa50a1c0818323d5f29"
B4 = "prereg/SPARKS-EXP7-NUL-addendum-1-brouillon4.md"
SORTIE = "docs/notes/weight-space-programming-v1/contre-lecture-delta-v4-v1/couples-brouillon5-v1.json"
COUPLES = [
    {"id": "L1", "raison": "nom resté de la v3 ; le code lancé est celui de la section 2 (point 2)",
     "ancien": "donc l'amorce (`scripts/amorce_instance_sparks_exp7_nul_v3.sh`)",
     "nouveau": "donc l'amorce de la version du code citée en section 2 (`scripts/amorce_instance_sparks_exp7_nul_v<N>.sh`, "
                "<N> étant le numéro de cette version)"},
    {"id": "L2", "raison": "nom de fichier resté de la v3 (le code v4 pose `sparks-v4-detruire`) (point 2)",
     "ancien": "dès que la machine pose le fichier `sparks-v3-detruire`",
     "nouveau": "dès que la machine pose le fichier `sparks-v<N>-detruire` (même numéro que l'amorce)"},
    {"id": "L3", "raison": "idem (point 2)",
     "ancien": "**Qui pose `sparks-v3-detruire`.**",
     "nouveau": "**Qui pose `sparks-v<N>-detruire`.**"},
    {"id": "L4", "raison": "clé de Vast retirée par `env -i` ; refus rendus avec le code 0 (R-1506) (points 14 et 15)",
     "ancien": "tout code non nul ou délai dépassé pose un marqueur de création incertaine",
     "nouveau": "l'environnement de `vastai` garde, par leur nom, la clé `VAST_API_KEY` (que `vastai` lit, R-032) et les "
                "variables du mandataire (R-1497) ; tout code non nul, tout délai dépassé et toute sortie sans identifiant "
                "rendu avec « success » vrai, code 0 compris (`vastai` 1.8.3 rend ses refus avec le code 0, R-1506), pose "
                "un marqueur de création incertaine"},
    {"id": "L5", "raison": "un code 0 de `vastai start` ou `vastai destroy` ne prouve rien (R-1506) (point 16)",
     "ancien": "aucune seconde création avant un inventaire sans sortie brute.",
     "nouveau": "aucune seconde création avant un inventaire sans sortie brute. Un redémarrage ou une destruction par la "
                "session ne sont tenus pour faits qu'après un inventaire filtré (état lu, ou instance introuvable), jamais "
                "sur le seul code de retour de `vastai`."},
    {"id": "L6", "raison": "plafonds consignés jamais remplacés par la durée réelle : phase causale refusée au coin haut du "
                           "devis (point 9)",
     "ancien": "somme des plafonds des démarrages consignés sur son disque × prix de la carte, plus la durée depuis la "
               "création × prix du stockage",
     "nouveau": "somme, pour chaque démarrage consigné sur son disque, de sa durée réelle consignée à sa fin par l'amorce, "
                "ou de son plafond consigné avant le lancement si aucune fin n'est consignée, × prix de la carte, plus la "
                "durée depuis la création × prix du stockage"},
    {"id": "L7", "raison": "le tir n'a pas de commande, et le lanceur refuse sans addendum scellé ; répétition à rejouer, "
                           "chaque démarrage isolé (points 19 à 22)",
     "ancien": " et la répétition jouet complète (création, redémarrage de copie, phase causale) par la session reliée au "
               "dépôt distant.",
     "nouveau": ", joué par une commande écrite d'avance (mode « tir » du lanceur : échéance courte, étiquette de tir, "
                "création arrêtée à la garde du code, puis ordre « fin ») et sous un GO qui le couvre ; et la répétition "
                "jouet complète (création, redémarrage de copie, phase causale) par la session reliée au dépôt distant, "
                "sur la version du code citée en section 2, chaque démarrage dans son propre espace de processus "
                "(`unshare -pf`)."},
    {"id": "L8", "raison": "branche restée de la v2 (point 3)",
     "ancien": "(branche `prep/sparks-exp7-nul-v2`, descendant de `55399606`) : À REMPLIR.",
     "nouveau": "(branche `prep/sparks-exp7-nul-v<N>` de la dernière version contre-lue, descendant de `55399606`) : "
                "À REMPLIR."},
]


def main(racine: Path) -> int:
    b4 = (racine / B4).read_bytes()
    if hashlib.sha256(b4).hexdigest() != SHA_B4:
        raise SystemExit("REFUS : brouillon 4 différent")
    sortie = racine / SORTIE
    donnees = (json.dumps(COUPLES, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    if sortie.exists():
        if sortie.read_bytes() != donnees:
            raise SystemExit("REFUS : fichier des couples présent et différent (R12)")
    else:
        sortie.write_bytes(donnees)
    texte = b4.decode("utf-8")
    for c in COUPLES:
        n = texte.count(c["ancien"])
        if n != 1:
            raise SystemExit(f"REFUS {c['id']} : « ancien » trouvé {n} fois")
        texte = texte.replace(c["ancien"], c["nouveau"])
        print(f"OK {c['id']} : 1 occurrence, {len(c['ancien'])} → {len(c['nouveau'])} caractères")
    if texte.count("À REMPLIR") != 3:
        raise SystemExit("REFUS : marqueurs")
    print(f"couples : {SORTIE} {hashlib.sha256(donnees).hexdigest()}")
    print(f"marqueurs « À REMPLIR » : 3 ; texte d'essai (non versé) : {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1])))
