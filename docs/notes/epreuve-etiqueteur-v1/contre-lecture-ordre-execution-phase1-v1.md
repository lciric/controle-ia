# Contre-lecture — ordre d'exécution de la phase 1 de l'épreuve de l'étiqueteur, brouillon v1

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf. Je n'ai écrit ni le préenregistrement, ni ses scripts, ni cet ordre, ni aucune contre-lecture antérieure.
- **Heures** (temps universel, `date -u`) : 8 novembre 2026, de 00:35:20 à 00:49:30.
- **Objet** : `docs/notes/epreuve-etiqueteur-v1/ordre-execution-phase1-v1-brouillon.md`, empreinte `63f2de9529d3947eb8afbae0e571e57d8012a5f18ac93fd8fe214e8e64a8636b` (égale à son `.sha256`), arbre `/home/user/wt-etiqueteur`, branche `prep/epreuve-etiqueteur-v1`, commit `dd3b912605f4a2cdf4b387bfbcf108fe8126a9b3`. Arbre propre avant et après (seuls ajouts : ce rapport et le fichier de couples).
- **Fait foi, vérifié** : texte scellé `prereg/preenregistrement-epreuve-etiqueteur-v1.md` = `f73455b8…40fa` (sur disque et au commit `d858b66f9`, présent sur `origin/main`) ; scripts au commit du code `64e67cbd…` : les huit empreintes de la section 1.3 de l'ordre, celle du relais (`67f36951…`) et celles des deux entrées du générateur sont exactes et égales à l'annexe C du texte scellé ; registre des GO : GO-2026-11-07-05, 06, 07 (calcul, 300 dollars, échéance 2026-11-30) et 10 lus ; GO-2026-11-07-07 présent au registre du commit scellé (1 ligne), **absent** de celui du commit du code (0 ligne) : le choix `--registre-go "$ENTREES/go-d858b66f9.md"` de l'ordre est nécessaire (rejoué : registre par défaut, code 2, « GO absent du registre »).

## Verdict

**Scellable après couples.** 16 couples (`couples-contre-lecture-ordre-execution-phase1-v1.json`, empreinte `706d244c…e2f4`), chacun trouvé une seule fois dans le brouillon ; appliqués dans l'ordre à une copie du bloc-notes : 22 blocs, syntaxe correcte (`bash -n`), blocs modifiés rejoués en mode simulé. Sept sont **bloquants** : sans eux, la lecture principale serait tuée par l'outil de commande au bout de deux heures au plus, la reprise serait mal chiffrée, et le premier temps du contrôle du prix d'Argon, écrit au texte scellé, manquerait. Aucun couple ne touche au texte scellé ni aux scripts ; aucun n'appelle de nœud du directeur.

## Ce que j'ai rejoué (bloc-notes, sans réseau, sans clé, graine d'essai 20261107)

Code du commit `64e67cbd…` extrait par `git archive` (chemins nécessaires seulement), texte scellé et registre extraits du commit `d858b66f9` ; variables de clé **factices et absentes** (`VARIABLE_FACTICE_ARGON_ABSENTE`, `VARIABLE_FACTICE_KIMI_ABSENTE`) ; aucune variable réelle lue.

| bloc | résultat |
|---|---|
| 1.3 | douze « OK », `code sha256sum=0`, GO : 1, entropie 17812956677980471985 (égale à l'ordre), python 3.13.18, numpy 2.4.6 |
| 1.4 (commande exacte, `env -i`) | 24, 6, 79, 12 passés, codes 0 |
| 2.1 à 2.4 | codes 0 ; 396, 396, 20, 20, 80, 60 lignes ; items `f11ba273…` (égale à l'annexe C pour la graine d'essai) |
| 3.2 en `--simule` (filtre de l'environnement compris) | code 0, feu vert, 20 « ok » par lecteur |
| 3.3, impression du manifeste de 3.4, 3 bis | nombres seulement ; tous les champs lus existent dans le manifeste et le journal |
| 4.2 (calculs) | `DEP` 1.042356, plafond du relais 298.95 |
| 4.3 en `--simule`, `--depense-engagee "$DEP"` | code 0, 456 « ok » par lecteur, `depense_engagee_avant` = `DEP` ; manifeste cumulatif (26.68) |
| 4.5 | empreintes égales au manifeste, A et B différentes |
| 5 (analyse, code seulement) | code 0, résultat écrit ; contenu non lu |
| 3.2 en `--reel`, variable factice absente | code 2, « variable … absente : aucun appel », aucun dossier créé |

Le relais et le bloc d'état n'ont **pas** été lancés (appel réseau local interdit à cette contre-lecture) : relus dans le code (`relais_kimi_v4.py`, `analyseur`, `etat`, `do_GET`).

## 1. Commandes, options, sorties

Conformes au texte scellé et aux scripts : `--plafond-dollars 300` aux deux lancements (le script refuse tout autre plafond et un plafond différent de l'essai) ; `--depense-engagee 0` puis la valeur exacte du manifeste de l'essai (`repr` d'un flottant : égalité exacte, contrôlée par le script) ; `--relais-max-appels` 100 puis 2 280, égal au `--max-appels` du relais et au minimum du script (5 × 20, 5 × 456) ; `--registre-go` justifié ; dossiers de sortie neufs, refus d'un dossier existant par le script (R12) ; options entières (la lecture refuse l'abréviation ; relais, générateur et analyse l'admettraient, mais l'ordre n'en abrège aucune) ; réglages du relais conformes au texte scellé (« Points ouverts », point 3) et au LISEZMOI cité (`--modeles-permis kimi-k3.1-pro --prix-entree 2 --prix-sortie 10 --prix-cache 2`, instance neuve par lancement, état avant et après, arrêt par numéro).

Écarts trouvés :
- **Comptes du manifeste de génération non contrôlés** (moyen, CO-08, CO-09). La liste d'arrêt scellée dit « comptes du manifeste ou du tirage différents de ce texte » ; l'ordre ne compte que des lignes. Le générateur écrit `$GEN/manifeste-generation-v2.json` (pas dans la console, contrairement à ce que dit le brouillon) avec 24 par case plantée, 20 par sorte et dose de placebo, 60 jumeaux, 60 tâches. Programme ajouté (nombres seulement), essayé sur le cas sain (« comptes conformes ») et sur un artefact (une case à 23 : « ARRET »).
- **Bloc d'état du relais** (mineur, CO-11, CO-12) : la liste gardée cite `prix_entree`, `prix_sortie`, `prix_cache`, mais le relais rend `prix_entree_usd_par_million`, etc. : les prix, réglage exigé, ne s'impriment pas. Noms corrigés ; ajout de `reserve_par_appel_usd` et `recherche_officielle` (attendu « inactive »).
- **Relais pas encore prêt** (mineur, CO-13) : l'état est lu dans l'appel qui suit le lancement, sans attendre ; une lecture vide ferait échouer `json.load` et, à la lettre, arrêter. Attente bornée à 20 secondes ajoutée.
- **1.2 sans « Attendu »** (mineur, CO-15).

## 2. Ordre des étapes

Génération → arrêt et dépôt chez le tiers (2.5) → essai de format → contrôle de la facture par le directeur (3 bis) → feu vert écrit de la session mère (4.1) → lecture principale et relecture → analyse par un lecteur neuf : conforme au texte scellé (« Ordre des opérations », points 3 à 6), chaque passage gardé par un arrêt écrit.

Écarts :
- **Premier temps du contrôle du prix d'Argon absent** (bloquant, CO-07). Le texte scellé (« Points ouverts », point 4) prévoit, **avant l'essai de format**, le relevé du prix public de Google (par le directeur, ou par un réseau permis sur sa décision), un prix au-dessus de 10 et 50 dollars par million arrêtant l'épreuve avant tout appel ; il demande aussi « clé ou projet dédié à l'épreuve » pour isoler le relevé. Le brouillon n'a que le second temps (facture, 3 bis) et une garantie d'usage exclusif « avant le lancement 3.2 » sans porte écrite. Couple : les deux conditions entrent dans le message de feu vert de 2.5 ; sans elles, aucun lancement.
- **`<<GENERATION_PAR>>`, variante « session mère » inexécutable telle qu'écrite** (moyen, CO-10) : l'exécutante devrait « recevoir » `$GEN` et `$TIRAGE`, mais 1.1 s'arrête si la racine existe, et rien n'est écrit pour une exécutante sur une autre machine. Le brouillon attribue en outre au point 3 de « Ordre des opérations » ce qu'il ne dit pas : le texte scellé ne nomme la session mère que pour la liste des relectures (« Scripts de la phase 1 »). Couple : attribution corrigée ; variante « session mère » = la mère exécute 1.1 à 2.4 sur la machine et dans la racine de l'exécutante, l'exécutante refait 1.3, 1.4, 2.4 et compare ; autre machine : arrêt. Le choix reste celui de la mère (point ouvert 2 du brouillon) ; à la lettre du texte scellé, la variante « session mère » est la plus sûre.

## 3. L'exécutante ne lit ni réponse ni résultat

Tenu. Les programmes de l'ordre ne lisent que les champs nommés (`lecture`, `statut`, `cout_estime`, jetons, modèles, heures, champs du manifeste) et n'impriment que des nombres, des statuts, des motifs écrits par le script et des empreintes ; consoles, réponses, clé, tirage et résultat ne sont jamais ouverts ; l'analyse est laissée à un lecteur neuf. Remarque : le journal porte `reponse_brute` pour les tentatives au format faux ; les programmes ne lisent pas ce champ. Le contrôle scellé « champ `lecteur` de chaque ligne égal au lecteur du fichier » n'avait pas de commande : ajouté en 4.5 (mineur, CO-16), comptes seulement, essayé sain (« conforme ») et sur l'artefact « même fichier pour A et B » (456 lignes d'un autre lecteur, « ARRET »).

## 4. Clés

Tenu : présence vérifiée par le nom seul (`${!n:-}` dans un test, jamais imprimé ; nom contrôlé par une forme avant l'expansion) ; aucun `echo` de valeur, `env` complet, `printenv`, `set -x` ni journal de commande ; `env -i` n'est employé qu'avec un programme ; les filtres de 3.1, 3.2, 4.2 et 4.3 ne listent que des noms (`compgen -e`) et ne gardent que la clé du processus concerné (le relais n'a pas celle d'Argon, la lecture n'a pas celle de Kimi) ; essayés en mode simulé. Limite connue, écrite dans le relais : le bloc initial `/proc/<pid>/environ` du relais et de la lecture garde la clé tant qu'ils vivent ; la règle 1 de l'ordre en interdit la lecture.

**Marqueurs** : `<<VARIABLE_CLE_ARGON>>` est bien placé (seule occurrence active : `NOM_CLE_ARGON='…'` dans le fichier de variables de 1.1, entre apostrophes d'un document littéral ; le garde de 1.5 arrête s'il reste `<<`). `<<GENERATION_PAR>>` est bien placé (section 2, en prose ; non rempli : arrêt), sous réserve du couple CO-10.

## 5. Durée, reprise, dépense engagée

- **Bloquant (CO-01 à CO-04)** : 3.2 et 4.3 lancent la lecture avec `run_in_background` et une enveloppe qui attend (`wait`). Or l'outil arrête une telle commande à sa limite : 30 minutes au défaut, 2 heures au plus. **Constaté ici** sur un processus factice (`sleep`, limite de 60 secondes) : à la limite, le processus attendu meurt et l'enveloppe n'écrit **pas** son code de fin. La lecture principale (456 items par lecteur, deux fils, Kimi à raisonnement long, jusqu'à 1 800 secondes par appel) dépasse très probablement deux heures ; même l'essai de format peut dépasser 30 minutes. Elle mourrait sans manifeste, sans code de fin, items restants non lus. Aussi constaté : un processus détaché par `&` survit à la fin de l'appel qui l'a lancé (appel ordinaire comme appel en arrière-plan), et une enveloppe détachée écrit bien son code de fin. Couple : enveloppe détachée (`) > /dev/null 2>&1 &`) lancée par un appel ordinaire, puis un « guet » en `run_in_background`, qui rend la main toutes les 9 minutes (essai de format) ou 14 minutes (lecture principale), sans jamais toucher la lecture, pour les surveillances de 3.3 et 4.4 (règle des 45 minutes comprise). Rejoué en mode simulé : lancement, guet « lecture finie, code 0 », suite des blocs ; guet sur un processus disparu sans code de fin : « ARRET : lecture disparue ».
- **Bloquant (CO-05, CO-06)** : le brouillon ne traite pas le **lancement disparu** (conteneur redémarré — le rédacteur en a vécu un à 00:25 —, session fermée, limite de l'outil), et sa règle de reprise est ambiguë. « La dépense déjà engagée (somme des `cout_estime` du journal) et un plafond diminué d'autant » omet la dépense de l'essai de format, ne dit pas « les deux journaux », et peut se lire comme `--plafond-dollars` diminué, que le script refuse (code 2). Couple : cas écrit (arrêt, relais relevé puis arrêté, comptes et sommes des deux journaux, empreintes, aucune relance, nœud du directeur) ; règle de reprise explicite : `--plafond-dollars 300` inchangé ; `--depense-engagee` = `depense_estimee_dollars` du manifeste précédent s'il existe (il est cumulatif, vérifié), sinon `DEP` plus les `cout_estime` des journaux A et B (texte scellé, liste d'arrêt) ; relais à 300 moins cette somme. Réserve écrite : une tentative en vol à la mort (deux au plus) n'a pas de ligne au journal ; son coût (moins d'un dollar chacune au pire cas) échappe à cette somme. La session mère la compare aux relevés des fournisseurs (le texte scellé, ligne « exception imprévue », prévoit déjà ce recours).

## Couples (détail au fichier JSON)

| repère | gravité | objet |
|---|---|---|
| CO-01, CO-02 | bloquant | essai de format : enveloppe détachée et guet |
| CO-03, CO-04 | bloquant | lecture principale : enveloppe détachée et guet |
| CO-05 | bloquant | lancement disparu ; règle de reprise et dépense engagée explicites |
| CO-06 | bloquant | ligne « lecture disparue » dans la table des arrêts |
| CO-07 | bloquant | prix public d'Argon avant l'essai de format ; clés ou projets sans autre usage |
| CO-08, CO-09 | moyen | comptes du manifeste de génération ; attendu de 2.4 |
| CO-10 | moyen | qui génère : attribution exacte, variante « session mère » exécutable |
| CO-11, CO-12 | mineur | noms des champs de prix dans l'état du relais ; attendu |
| CO-13 | mineur | attente du relais avant l'état |
| CO-14 | mineur | 3 bis : `jetons_sortie` comprend déjà la pensée (Argon et Kimi, vérifié dans `appeler_gemini` et `appeler_kimi`) ; pas de double compte face à la facture |
| CO-15 | mineur | attendu de 1.2 |
| CO-16 | mineur | contrôle du champ `lecteur` avant l'analyse |

## Remarques sans couple

1. Le `git worktree add` de 1.2 dépose tout l'arbre du commit du code, y compris des dossiers que le programme tient à l'écart des autres travaux. Je ne les ai ni listés ni lus. Une extraction limitée aux chemins nécessaires (`git archive` des deux dossiers de scripts et des deux fichiers d'entrée) suffit : les 121 essais y passent. Elle changerait les contrôles de 1.2 (plus de `rev-parse`) : au choix de la session mère.
2. GO-2026-11-07-07 a pour échéance le 30 novembre 2026 : une reprise tardive doit passer avant, ce que l'ordre ne vérifie pas.
3. La branche locale `main` de `/home/user/controle-ia-travail` est en retard (sans GO-07 ni le commit scellé) ; `origin/main` les porte. L'ordre fait `fetch` puis travaille par numéros de commit : sans effet.
4. Le relevé de facturation des fournisseurs peut arriver avec retard ; l'ordre ne borne pas l'attente entre 3 bis et 4.1, ce qui est prudent.

## Interdits tenus

Aucune référence ouverte ni listée sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; aucune clé ni variable de clé lue (seuls des noms factices absents) ; aucun appel réseau (pas de relais lancé, pas de requête locale) ; aucun commit, aucune poussée, aucun `.sha256` ; aucun fichier existant modifié. Les processus factices des essais (`sleep`) ont été arrêtés par leur numéro ou sont morts d'eux-mêmes ; aucun ne reste. Script des couples et copie appliquée : bloc-notes de la session (`outils/couples.py`, `237533fd…` ; `ordre-applique.md`, `ab07632e…`).
