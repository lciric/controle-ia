"""Formes écrites après les deux-points dans les blocs du rejeu v1 (« verdict d'abord ») ; lecture stricte v2 rejouée
sur ces textes (contrefactuel descriptif : le texte v2 sera généré sous une autre consigne)."""
import json, sys, collections, re
from controle_ia.environnements import noter_rejeu_juges_v2 as v2
from controle_ia.environnements.rubrique import CRITERES
for f in sys.argv[1:]:
    d = json.load(open(f))["resultat"]["notations"]
    formes = collections.Counter(); strict_ok = 0; v1_ok = 0; blocs = 0; sans_espace = 0; lignes = 0
    for r in d:
        bloc = v2.bloc_des_notes_v2(r["reponse"], CRITERES)
        v1_ok += r["proba"]["score"] is not None
        if bloc is None:
            continue
        blocs += 1
        e = v2.lecture_ecrite_v2(bloc, CRITERES)
        strict_ok += e["score"] is not None
        for nom, m in v2._dernieres_lignes(bloc, CRITERES).items():
            lignes += 1
            b = m["brut"]
            forme = re.sub(r"\d", "9", b)
            formes[forme] += 1
            sans_espace += not b.startswith(" ")
    print(f.rsplit("/",1)[-1], "notations", len(d), "blocs", blocs, "finis et appuyés v1", v1_ok,
          "écrits stricts v2", strict_ok, "lignes", lignes, "lignes sans espace après les deux-points", sans_espace)
    print("   formes :", formes.most_common(12))
