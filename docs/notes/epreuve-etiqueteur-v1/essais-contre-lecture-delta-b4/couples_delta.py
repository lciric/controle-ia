"""Construit et vérifie les couples de la contre-lecture du delta (chaque « ancien » présent exactement n fois dans le
brouillon 4, sans chevauchement). Arguments : brouillon 4, sortie JSON, empreinte du rapport, heure de fin."""
import json, sys, hashlib
b4p, sortie, emp_rapport, fin = sys.argv[1:5]
b4 = open(b4p, encoding="utf-8").read()
assert hashlib.sha256(b4.encode()).hexdigest() == "4f186d8e9e435d64598d9f0b2b39a646e46934913cb27f39d7dc92a447687db5"
C = []
def c(i, ancien, nouveau, n=1, code=None):
    C.append({"id": i, "n": n, "ancien": ancien, "nouveau": nouveau})

c("CD-01-statut",
  "**non contre-lu dans cet état** (une contre-lecture du delta est requise), **non scellé**.",
  "**contre-lu dans cet état par la contre-lecture du delta** (non scellable en l'état : bloquants D1 et D2, correctifs de code ; B1 à B8 levés ; voir la section « Contre-lecture »), **non scellé**.")
c("CD-02-D1-table-masquage",
  "avant toute troncature, partout ; tout fragment de 6 caractères de la clé masqué |",
  "avant toute troncature, partout, sortie d'erreur du script comprise ; tout fragment de 6 caractères de la clé masqué ; nom de la variable de la clé contrôlé avant tout appel et toute écriture, jamais recopié s'il est refusé (contre-lecture du delta, D1) |",
  code="D1 : lire_items_phase1 en version nouvelle")
c("CD-03-D1-nom-de-variable",
  "la clé est lue **par le nom de sa variable seulement** (`--variable-cle-gemini`, par défaut `GEMINI_API_KEY`)",
  "la clé est lue **par le nom de sa variable seulement** (`--variable-cle-gemini`, par défaut `GEMINI_API_KEY`) ; un nom hors de la forme `[A-Z_][A-Z0-9_]*` (une valeur de clé passée par mégarde à la place du nom, par exemple) est refusé avant tout appel et toute écriture, sans être recopié ; la sortie d'erreur du script passe elle aussi par le masquage (contre-lecture du delta, D1 : au brouillon 4, une valeur de clé passée comme nom s'écrivait en clair sur la sortie d'erreur en mode réel et au manifeste en mode simulé)",
  code="D1 : lire_items_phase1 en version nouvelle")
c("CD-04-D2-analyse-complete",
  "il refuse de rendre un verdict si plus de 2 % des items d'un lecteur sont illisibles.",
  "il refuse de rendre un verdict si plus de 2 % des items d'un lecteur sont illisibles, **un item sans ligne de réponse comptant illisible** ; il refuse aussi, sans verdict, un fichier de réponses incomplet ou en double (pour chaque lecteur : une ligne « principale » par item des 396 et une ligne « relecture » par jumeau de la liste, ni plus ni moins) (contre-lecture du delta, D2 : au brouillon 4, des lignes absentes échappaient à la règle des 2 %, et un fichier vide rendait « étiqueteur non validé », qui brûle les items).",
  code="D2 : analyser_phase1 en version nouvelle")
c("CD-05-D2-liste-d-arret",
  "| plus de 2 % d'items illisibles pour un lecteur | pas de verdict (script d'analyse) ;",
  "| plus de 2 % d'items illisibles pour un lecteur (un item sans ligne de réponse compte illisible) ; fichier de réponses incomplet ou en double | pas de verdict (script d'analyse ; contre-lecture du delta, D2) ;",
  code="D2 : analyser_phase1 en version nouvelle")
c("CD-06-lancement-repris",
  "part avec le plafond diminué de la dépense déjà engagée |",
  "part avec le plafond diminué de la dépense déjà engagée ; la dépense déjà engagée est le champ `depense_estimee_dollars` du manifeste du lancement précédent ou, pour un lancement arrêté par son numéro de processus (sans manifeste), la somme des `cout_estime` de son journal écrit au fil ; le second lancement de la phase passe le même `--plafond-dollars` que l'essai de format, et une `--depense-engagee` au moins égale à la dépense de son manifeste (le script ne le vérifie pas : contre-lecture du delta) |\n| lancement de lecture principale repris, ou plusieurs lancements | l'analyse lit les seuls fichiers finals du dernier lancement « principale+relecture » allé à son terme ; les réponses des lancements interrompus sont gardées et rapportées, jamais mêlées ni choisies après coup |")
c("CD-07-limite-11",
  "mais son excès peut porter la dépense au-delà du plafond, une fois par lecteur en vol ;",
  "mais son excès peut porter la dépense au-delà du plafond, une fois par appel en vol : le script tourne avec un seul groupe de fils commun aux deux lecteurs (`--fils-par-lecteur 1`, valeur gelée, soit deux fils), si bien que deux appels du même lecteur peuvent être en vol ensemble (essai de la contre-lecture du delta) ; l'entrée, réservée à 3 caractères par jeton, n'est pas contrôlée après coup et peut aussi dépasser sa réserve ;")
c("CD-08-temperature-documentee-table",
  "températures envoyée et servie écrites au manifeste et au journal |",
  "températures envoyée et documentée écrites au manifeste et au journal (le champ `temperature_servie` porte la valeur que documente le fournisseur ; aucune des deux réponses ne la rend : elle n'est pas vérifiée) |")
c("CD-09-temperature-documentee-sorties",
  "températures envoyée et servie)",
  "températures envoyée et documentée, la seconde non rendue par les fournisseurs)")
c("CD-10-reglages-geles",
  "toute autre valeur arrête le script",
  "constantes du script scellé, non modifiables en ligne de commande ; leur empreinte est écrite au manifeste, et la lecture principale refuse de partir si elle diffère de celle de l'essai de format",
  n=2)
c("CD-11-relais",
  "le plafond du relais est réglé à la part de Kimi du plafond de la phase.",
  "le relais (version 4) est lancé, pour chaque lancement de lecture, avec `--modeles-permis kimi-k3.1-pro`, `--plafond-usd` égal au reste du plafond de la phase (filet : la garde du script reste la borne) et `--max-appels` au moins égal au nombre de tentatives possibles (cinq par item au plus : quatre erreurs de transport et deux demandes, compteurs communs à l'item), soit 100 pour l'essai de format et 2 280 pour la lecture principale et la relecture ; son défaut (64 appels) ferait échouer la lecture principale dès le 65e appel (réponse 429, reprise, puis « illisible ») ; ses réponses 402 (plafond) et 429 (appels) rendent l'item illisible sans arrêter le lecteur (arrêt du lecteur recommandé au code par la contre-lecture du delta).")
c("CD-12-cle-invalide-400",
  "| clé refusée par un fournisseur (codes 401 ou 403) |",
  "| clé refusée par un fournisseur (codes 401 ou 403 ; l'interface d'Argon peut rendre une clé invalide en 400, raison `API_KEY_INVALID`, comportement connu de l'interface Gemini, non vérifié ici : le script la traite alors en « illisible », sans arrêt général, et l'essai de format passe au rouge ; arrêt général sur ce motif recommandé au code par la contre-lecture du delta) |")
c("CD-13-exception-imprevue",
  "autre erreur : « illisible » aussitôt.",
  "autre erreur du fournisseur : « illisible » aussitôt ; une exception imprévue (réponse que le protocole ne peut lire, par exemple) est traitée comme une erreur de transport (quatre tentatives au plus).")
c("CD-14-T5-devis",
  "sans humains, le coût dépend des appels (275 dollars au plus prudent) : la variante à 312 items n'épargnerait qu'une quarantaine de dollars",
  "sans humains, le coût dépend des appels (devis v3 : 185 dollars au centre, 600 au plus prudent ; le devis v2 disait 275) : la variante à 312 items n'en épargnerait qu'environ un cinquième de la lecture principale (au prorata des items : de l'ordre de 35 dollars au centre et de 110 à 120 au plus prudent ; estimation de la contre-lecture du delta, non opposable)")
c("CD-15-feu-vert-et-plafond",
  "feu vert de l'essai de format sur extrapolation des jetons mesurés (annexe B, `devis_phase1_v3.py`).",
  "feu vert de l'essai de format sur extrapolation des jetons mesurés (annexe B, `devis_phase1_v3.py`). Avec ce plafond, le feu vert n'est donné que si la lecture principale extrapolée (coût moyen mesuré majoré de 25 %) tient dans le reste : à l'hypothèse haute (lecture principale 316 dollars, essai de format 14), l'extrapolation vaut environ 394 dollars pour 386 restants et le feu est rouge ; le seuil se situe vers 309 dollars de lecture principale mesurée, soit entre l'hypothèse centrale (177) et l'hypothèse haute (estimation de la contre-lecture du delta, non opposable).")
c("CD-16-limite-7",
  "7. Une contre-lecture (brouillon 3) ; les correctifs de code qu'elle demande sont à relire avant le scellement.",
  "7. Deux contre-lectures (brouillon 3 ; delta du brouillon 4) ; les correctifs de code de la seconde (D1, D2) sont à relire avant le scellement.")
c("CD-17-prix-argon",
  "Argon au barème volontairement haut du programme, non vérifié, prudent pour la garde.",
  "Argon au barème volontairement haut du programme, non vérifié, prudent pour la garde ; ce barème est une constante du script scellé : il est à vérifier avant le scellement de préférence, au plus tard avant la décision de dépense ; un prix réel au-dessus de 10 et 50 dollars par million ferait sous-compter la garde (barème corrigé en version nouvelle avant toute lecture, nœud du directeur).")
c("CD-18-relais-empreinte",
  "la version et l'empreinte du relais de Kimi au manifeste.",
  "l'empreinte du relais de Kimi au manifeste, donnée par `--relais-empreinte` (facultative au code, à passer en mode réel ; la version du relais n'est pas écrite par le script).")
c("CD-19-contre-lecture-delta",
  "**Contre-lecture du delta** : à faire par un sous-agent neuf, sur les versions 2, le devis v3, ce brouillon et le journal des couples.",
  "**Contre-lecture du delta** : sous-agent neuf, Claude Opus 5.5 (`claude-opus-5-5`), 7 novembre 2026, de 23:13:48 à " + fin + " (temps universel, `date -u`) ; brouillon relu `4f186d8e9e435d64598d9f0b2b39a646e46934913cb27f39d7dc92a447687db5` ; rapport `docs/notes/epreuve-etiqueteur-v1/contre-lecture-delta-brouillon4-v1.md` (`" + emp_rapport + "`) ; couples `couples-contre-lecture-delta-brouillon4-v1.json` ; verdict : **non scellable en l'état** (bloquants D1 et D2, correctifs de code) ; B1 à B8 levés, chacun prouvé sur un cas sain et sur un artefact ; 38 couples appliqués à l'octet ; une contre-lecture du delta suivante, bornée aux correctifs de D1 et D2 et à l'application de ces couples, est requise avant le scellement.")

pos = []
for x in C:
    k = b4.count(x["ancien"])
    assert k == x["n"], (x["id"], k)
    d = 0
    for _ in range(k):
        i = b4.index(x["ancien"], d); pos.append((i, i + len(x["ancien"]), x["id"])); d = i + 1
pos.sort()
for (a1, b1, i1), (a2, b2, i2) in zip(pos, pos[1:]):
    assert a2 >= b1, ("chevauchement", i1, i2)
t = b4
for x in C:
    t = t.replace(x["ancien"], x["nouveau"])
for x in C:
    assert t.count(x["nouveau"]) >= x["n"], x["id"]
with open(sortie, "x", encoding="utf-8") as f:
    f.write(json.dumps(C, ensure_ascii=False, indent=1) + "\n")
print(len(C), "couples ;", sum(x["n"] for x in C), "occurrences ; brouillon appliqué", hashlib.sha256(t.encode()).hexdigest())
