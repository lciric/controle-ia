import json, sys
src, dst = sys.argv[1], sys.argv[2]
o = json.loads(open(src, encoding="utf-8").read())
o["_lisez_moi"] = ("Configuration v8 de la plus petite course réelle de la boucle complète de l'organisme (code v67 ; écart 1 au "
 "texte scellé preenregistrement-boucle-reelle-organisme-v1-v1.md, sha256 46d7545b…, option 2 décidée par le directeur, R-2426, "
 "GO-2026-11-12-06 ; texte neuf preenregistrement-boucle-reelle-organisme-v1-v2.md). Copie de la configuration v7 "
 "(configuration-boucle-reelle-v7.json, sha256 e45f3a7199c5d16428a3b4f2b31f1b18ee82594cabbf2b5ec26a6168b1655df6), elle-même copie de "
 "la v6 (4743ddbe…) avec plafonds_session.proposeur 0.5 → 1.5 et --max-sortie-proposeur de Kimi 65536 → 131072. Ne changent en v8 que : "
 "ce texte ; fournisseurs.kimi.delai_s 1800 → 7200 (délai de l'adaptateur, que le code v67 passe à l'adaptateur ; le code v66 "
 "l'ignorait et gardait 1 800 s) ; --delai-s de la commande de Kimi 1750 → 7150 (la commande s'arrête d'elle-même 50 s avant "
 "l'adaptateur ; garde 24 du code v67) ; arrets.a3_delai_s.kimi 1800 → 7200 (non lu sur le chemin de la course, relevé par "
 "cohérence). Le relais Kimi se lance avec --delai-amont-s 7200 (option de lancement, hors configuration). Argon : délais inchangés "
 "(1 800 et 1 750 s). Plafonds, parts, pièces (pieces/, six pièces de la v4) et commandes v6 (commandes-v6/, mêmes trois fichiers, "
 "mêmes empreintes) inchangés. Aucune valeur n'est un seuil scientifique gelé.")
k = o["fournisseurs"]["kimi"]
assert k["delai_s"] == 1800; k["delai_s"] = 7200
c = k["commande"]; i = c.index("--delai-s"); assert c[i + 1] == "1750"; c[i + 1] = "7150"
assert o["arrets"]["a3_delai_s"]["kimi"] == 1800; o["arrets"]["a3_delai_s"]["kimi"] = 7200
open(dst, "w", encoding="utf-8").write(json.dumps(o, indent=1, ensure_ascii=False) + "\n")
