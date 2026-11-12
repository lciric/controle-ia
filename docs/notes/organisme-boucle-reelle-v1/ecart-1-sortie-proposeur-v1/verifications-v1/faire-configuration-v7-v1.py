import json, sys
src, dst = sys.argv[1], sys.argv[2]
o = json.loads(open(src, encoding="utf-8").read())
o["_lisez_moi"] = ("Configuration v7 de la plus petite course réelle de la boucle complète de l'organisme (code v66 inchangé ; "
 "écart 1 au texte scellé preenregistrement-boucle-reelle-organisme-v1-v1.md, sha256 46d7545b…, brouillon "
 "ecart-1-sortie-proposeur-v1/ecart-1-brouillon-1.md, non scellé). Copie de la configuration v6 (configuration-boucle-reelle-v6.json, "
 "sha256 4743ddbe4d294643ac8e1924476dec056b1a08dac9f8010cd647dd1861160b0d) ; ne changent que : ce texte ; "
 "plafonds_session.proposeur 0.5 → 1.5 (budget de session des deux proposeurs, Kimi et Argon) ; dans la commande de Kimi, "
 "--max-sortie-proposeur 65536 → 131072 (valeur par défaut documentée de max_completion_tokens pour kimi-k3.1-pro ; maximum "
 "documenté 1048576). Motif : course 2 du 12 novembre 2026, réponse du proposeur Kimi coupée par sa borne de sortie (46 714 "
 "jetons de sortie dont 46 711 de raisonnement ; max_tokens fixé à 46 714 par le plafond de session de 0,50 USD), rapport "
 "rapport-course-v66-poste-local-v2.md (89b97faf…). Délais inchangés : la commande de Kimi s'arrête à 1 750 s et le code gelé v66 "
 "arrête toute commande externe à 1 800 s (pole/adaptateurs.py, DELAI_COMMANDE_S, que commandes_v64 ne remplace pas) ; la borne "
 "effective d'un appel du proposeur Kimi devient donc sa durée. Plafonds, parts, pièces (pieces/, six pièces de la v4) et "
 "commandes v6 (commandes-v6/, mêmes trois fichiers, mêmes empreintes) inchangés. Aucune valeur n'est un seuil scientifique gelé.")
o["plafonds_session"]["proposeur"] = 1.5
c = o["fournisseurs"]["kimi"]["commande"]
i = c.index("--max-sortie-proposeur"); assert c[i + 1] == "65536"; c[i + 1] = "131072"
open(dst, "w", encoding="utf-8").write(json.dumps(o, indent=1, ensure_ascii=False) + "\n")
