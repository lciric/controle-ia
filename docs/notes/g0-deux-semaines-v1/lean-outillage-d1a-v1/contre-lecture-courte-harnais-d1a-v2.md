# Essai Lean, outillage D-1a — contre-lecture courte et différentielle du harnais v2

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, puis Lazar.
- **Écrit par** : sous-agent neuf, second contre-lecteur ; **modèle déclaré : Claude Fable 5.2 (`claude-fable-5-2`)**. Je n'ai
  écrit ni le harnais, ni ses corrections, ni la première contre-lecture. L'auteur du harnais est Opus 5.5 ; la première
  contre-lecture est d'une autre instance de Fable 5.2 (même modèle que moi : à compter comme une seule lignée de relecture).
- **Date** : 11 novembre 2026, vers 01:30 UTC. Processeur seulement : aucune dépense, aucun serveur, aucun appel à Hetzner ni à
  une interface payante, aucune connexion SSH, aucun appel de modèle. Aucun commit, aucune poussée.
- **Lu, empreintes vérifiées par `sha256sum -c` avant lecture** : `contre-lecture-harnais-d1a-v1.md` (`2077ae26…`),
  `rapport-corrections-harnais-d1a-v2.md` (`a68b8cca…`), `journal-essais-r5-v2.txt`, `journal-mutations-harnais-v2.json`.
  Code : différence `558bcf97…..99192fd2…` (49 fichiers ajoutés, aucun modifié : R12 tenue), dans un arbre clairsemé à moi.
  Empreintes des modules v2 égales à celles du rapport (`6a5ad5e7…`, `8d9a7986…`, `3f5d44d6…`, `fc68b0d5…`).
- **Limite** : aucune chaîne Lean ici. « (éprouvé) » = exécuté en Python sur le code du commit, import tracé vers mon arbre.
  « (Lean, non éprouvé) » = raisonné sur la grammaire et les interfaces de Lean, à confirmer sur la machine.

## Verdict

**Défauts bloquants : CLC2-01, CLC2-02 (gardes encore contournables) et CLC2-04 (serveur créé sans minuterie si la réponse de
la création se perd).**

- CLC2-01 et CLC2-02 bloquent le scellement de la pièce HARNAIS-ET-ISOLEMENT et tout usage des gardes en D-1b. Ils ne créent
  aucun risque pendant l'installation de D-1a (aucun code d'agent n'y tourne).
- CLC2-04 est à corriger **avant toute création de serveur**, avec CLC2-03.
- Des quinze défauts de la première contre-lecture : **neuf levés** (CLL-02, 03, 07, 08, 10, 11, 12, 14, 15), **six partiels**
  (CLL-01, 04, 05, 06, 09, 13), aucun « non levé ». Les attaques citées par la première contre-lecture échouent toutes contre
  la v2 ; ce qui reste ouvert, ce sont les **classes** dont ces attaques étaient des exemples.
- Essais : `169 passed` (101 de la v2, 68 de la v1), commande de la consigne. Mutations neuves : 24, dont 15 tuées, 9
  survivantes (CLC2-08).

## Les quinze défauts, un par un

| Défaut | État | Preuve |
|---|---|---|
| **CLL-01** lexique | **partiel** | Les cinq sources de la première contre-lecture sont refusées (éprouvé : `«/-»`, `«a"»`, `«--»`, `'a'r"\"`, `1'"'` ⇒ cinq gardes en échec). Mais la classe reste ouverte par un autre chemin : CLC2-01. |
| **CLL-02** genre et sûreté | **levé** | `etape_1` de genre « definition » ⇒ G-L4 et G-L6 ; « non-sure » ⇒ G-L3 en plus (éprouvé). Réserve : l'interface de Lean qui imprime genre et sûreté n'est pas compilée. |
| **CLL-03** couverture | **levé** | `enonce_item.i definition` non imprimée ⇒ G-L6 (éprouvé). Reste : un nom de la liste fermée sous un nom attendu (`etape_1.match_1`) est couvert sans être imprimé ; il ne s'atteint que par un texte caché (CLC2-01). |
| **CLL-04** sortie du contrôle | **partiel** | (a) levé, éprouvé : marqueur brut au bon nonce ⇒ G-L7 ; code 137 ⇒ G-L7 ; nonce faux ⇒ G-L7 ; contrôle passé par l'entrée standard, sortie écrite par le harnais. (c) levé : artefact `gl7_init_attribut_v2.lean`. (b), la garde de fond, n'est pas écrite (réserve 1 de l'auteur) : CLC2-02 montre qu'elle n'est pas facultative. |
| **CLL-05** minuterie | **partiel** | Erreur passagère à l'échéance : trois 503 puis succès ⇒ détruit au 4ᵉ essai (éprouvé). Mais toute exception autre que `ErreurHetzner` et `OSError` tue encore la minuterie : CLC2-03. |
| **CLL-06** plafond par GO | **partiel** | Commande unique, prix lu dans l'API, devis sur le reste : levés (éprouvé ; `ccx63` refusé avant création, essais de l'auteur). Deux machines sous un même GO : refusée avec le même journal, **acceptée** avec un autre chemin de journal ou avec `--mot-de-lazar x` (éprouvé) : CLC2-07. Réponse de création perdue : CLC2-04. `garde_calcul.py` ne connaît toujours pas Hetzner (hors de la branche, dit par l'auteur). |
| **CLL-07** résidus | **levé** | Plus aucun arrêt par utilisateur ; arrêt par PID dans le groupe de l'unité. Note : avec `--wait --collect`, l'unité n'existe plus au retour de `systemd-run` ; la lecture rend donc toujours une liste vide sur la machine. C'est systemd qui nettoie ; le champ `processus_residuels` ne prouve rien. |
| **CLL-08** `import Lean` | **levé** (texte) | Lignes 1 et 2 du contrôle. (Lean, non éprouvé.) |
| **CLL-09** attributs | **partiel** | Liste fermée des attributs : levée. Éprouvé sur dix formes de plus que celles de l'auteur (`@[ init ]`, `@[simp ←, init]`, `@[simp] @[init]`, `attribute` puis saut de ligne puis `[init]`, `@[reducible, instance]`, etc.) : toutes refusées. Mais les **commandes et tactiques** qui exécutent du code restent une liste de mots ouverte : CLC2-02. |
| **CLL-10** énumération | **levé** (texte) | Aucun `open`, noms `_root_.Lean.…`, pas d'interpolation. Surface d'instances restante dite par l'auteur (réserve 2). (Lean, non éprouvé.) |
| **CLL-11** A12 | **levé** | Égalité avec le GO du pilote fixé ; essais de l'auteur ; mutation n23 tuée. |
| **CLL-12** A7 | **levé** | Verrou autour de « contrôler puis inscrire » ; essai à quatre fils ; mutation n24 tuée. |
| **CLL-13** ordre | **partiel** | Sonde exigée par le bac : levé (mutation n19 tuée). Lecture du pare-feu du nuage : incomplète et sans commande (CLC2-06). Tampon de la sonde jamais périmé pendant un même démarrage (note 3). |
| **CLL-14** survivantes | **levé** | Les neuf sont tuées (journal de l'auteur, 45 sur 45). D'autres lignes restent sans essai : CLC2-08. |
| **CLL-15** pannes du bac | **levé**, avec un trou neuf | Classement correct (essais de l'auteur). Mais la panne « bwrap » se lit dans un texte que l'agent écrit : CLC2-05. |

## Défauts neufs

### CLC2-01 — bloquant — le lexique lit `/-` et `--` au milieu d'un lexème de Lean

- **Où** : `gardes_lean_v2.py`, `masquer`, l. 87 et l. 93 : le début de commentaire est cherché à **chaque** position.
- **Chemin (éprouvé côté Python ; Lean, non éprouvé)** : Lean ne cherche un commentaire qu'après un lexème complet, et lit le
  lexème le plus long. Dans `{ x : Int //-x = 0 }`, Lean lit `//` puis `-x` ; `masquer` lit `/` puis un commentaire de bloc
  ouvert. Une ligne `-- -/` plus bas le referme pour `masquer` ; pour Lean, c'est un commentaire de ligne. Tout ce qui est
  entre les deux est invisible des gardes textuelles et lu par Lean. Trois variantes passent :
  1. `def T := { x : Int //-x = 0 }` … `-- -/` (plusieurs lignes cachées) ;
  2. `theorem t (x : Int) (p : Prop) (h : p) : p \/-1 = x := Or.inl h` … `-- -/` (`\/` puis `-1`) ;
  3. `def f : Id Int := do let x <--(1 : Int); pure x  @[init] def …` (`<-` puis `-` : le reste de la ligne est caché).
- **Mesure** : dans le bloc caché, `notation`, `macro`, `@[init] def etape_1.match_1 : IO Unit`, `initialize`, `#eval`,
  `run_cmd`, `instance enonce_item.match_1 : LE Nat := ⟨fun _ _ => True⟩`, `attribute [instance] foo`,
  `set_option debug.skipKernelTC true` : **aucun motif sur aucune garde textuelle**. Avec une énumération qui rend
  `etape_1.match_1 definition sure` et `enonce_item.match_1 definition sure` (noms de la liste fermée sous un nom attendu),
  `evaluer` rend **`accepte_gardes = True`**, rien n'est imprimé pour le relecteur.
- **Portée** : rouvre CLL-03 (instance qui change le sens de `≤`, non imprimée), CLL-04 (initialiseur par `@[init]`), CLL-09,
  et laisse passer `set_option debug.skipKernelTC` (preuve non vérifiée par le noyau).
- **Correction** : n'admettre un début de commentaire ou de littéral qu'en début de fichier, après un blanc, après un
  identifiant ou après `(`, `[`, `{`, `,` ; tout autre voisinage ⇒ `ErreurLexicale`. Ajouter les trois sources aux artefacts
  R5 (textuels et Lean). Classer comme identifiant tout caractère que Lean tient pour une lettre (par exemple `℘`, U+2118 :
  `isalpha` le refuse, Lean l'admet ; mes essais sur ce caractère échouent fermés, je ne l'ai pas tourné en attaque).

### CLC2-02 — bloquant — du code de l'agent tourne encore à la compilation, sans aucun mot interdit (Lean, non éprouvé)

- **Où** : `gardes_lean_v2.py`, `MOTS_GL3_SUPPL`, l. 38-39 : liste de mots ; la liste fermée de la v2 ne porte que sur les
  attributs.
- **Chemins (éprouvé pour le texte : aucun motif ; Lean, non éprouvé pour l'effet)** :
  1. `simproc nom (motif) := fun e => do …` (et `dsimproc`, `simproc_decl`, `dsimproc_decl`), puis `by simp [nom]` : le corps
     est du code `SimpM`, donc `MetaM` et `IO`, exécuté pendant la compilation du fichier.
  2. `def monTac : Lean.Elab.Tactic.TacticM Unit := do …` puis `by aesop (add safe tactic monTac)` : Aesop (import permis)
     évalue la constante nommée. La définition est imprimée pour le relecteur, mais aucune garde mécanique n'échoue.
  3. À vérifier sur la chaîne : `by_elabq` et `run_cmdq` de Qq, si la version installée les porte (les motifs `by_elab` et
     `run_cmd` ne les couvrent pas : la lettre suivante empêche la correspondance).
- **Pourquoi c'est grave** : du code `MetaM` peut ajouter une déclaration sans passer par le noyau
  (`debug.skipKernelTC` posé par programme, `addDeclWithoutChecking`), sous un nom `etape_1._proof_1` de genre théorème. Le
  théorème attendu s'y réfère, le noyau l'accepte, `#print axioms` ne liste rien, l'énumération rend « theoreme sure » :
  toutes les gardes passent sur un énoncé non prouvé, sans forger la sortie du contrôle. Le même code peut aussi écrire
  `/item/Item.olean` lui-même puis quitter avec le code 0, ou poser `/item/Lean.olean` (voir note 2).
- **Correction** : la garde de fond de CLL-04 (b), que l'auteur a laissée en réserve 1 : rejouer `Item.olean` dans le noyau
  par un outil du harnais qui n'exécute pas le code de l'agent (`lean4checker` ou équivalent), et en faire une garde exigée.
  Une liste de mots ne fermera pas cette classe. En attendant, ajouter `simproc`, `dsimproc`, `simproc_decl`,
  `dsimproc_decl`, les formes `add … tactic` d'Aesop, et un artefact R5 Lean par chemin, avec « observer » pour établir le
  fait sur la machine.
- **À établir en premier sur la machine** : les chemins 1 et 2 exécutent-ils bien le code dans le fichier qui le déclare ?
  Si non pour les deux, ce défaut tombe à « à corriger ».

### CLC2-03 — à corriger avant toute création de serveur — la minuterie meurt encore sur une réponse mal formée

- **Où** : `minuterie_v2.py` l. 111 (`except (ErreurHetzner, OSError)`) et l. 134 (`except ErreurHetzner`) ;
  `hetzner_v1.py` l. 89 (`d["server"]`) ; `hetzner_v2.py` l. 33 (`decode("utf-8")`).
- **Chemins (éprouvés)** :
  - statut 200 avec un corps JSON sans « server » : `KeyError` à la destruction, après **un seul appel**, aucun DELETE ;
  - corps non UTF-8 : `UnicodeDecodeError` (ni `OSError` ni `JSONDecodeError`), même issue ;
  - le même 200 mal formé **avant** l'échéance, dans `veiller` : `KeyError`, minuterie morte, serveur allumé ;
  - un seul 404 suffit à conclure « absent » (jeton d'un autre projet, par exemple) : la minuterie s'arrête, « destruction
    confirmée » au journal.
- **Boucle sans fin si l'API ment** : oui, et c'est voulu. DELETE accepté et serveur toujours présent : 4 essais = 4 DELETE,
  pauses 5, 10, 20 s (plafond 300 s), une ligne de journal par essai, aucune sortie. Aucune alerte hors du journal.
  Refus de nom à l'échéance : `GardeArret`, aucun DELETE (R10 tenue), mais **aucune ligne de journal**.
- **Correction** : dans la boucle de destruction et dans la lecture de `veiller`, attraper `Exception` sauf `GardeArret` ;
  exiger deux lectures « absent » de suite, dont une par l'inventaire ; journaliser le refus de nom.

### CLC2-04 — bloquant avant toute création de serveur — réponse de création perdue : serveur allumé, ni minuterie ni journal

- **Où** : `minuterie_v2.py`, `creer_et_veiller`, l. 159-162 : l'appel de création et la lecture de `reponse["server"]["id"]`
  sont **hors** du bloc qui détruit en cas d'erreur ; rien n'est écrit au journal avant l'appel.
- **Chemin (éprouvé)** : le serveur est créé côté Hetzner, la réponse se perd (délai) : `ErreurHetzner` remonte, le journal des
  créations n'existe pas, aucun DELETE n'est envoyé, aucune minuterie ne tourne. La relance refuse (« existe déjà ») : c'est
  le seul signal.
- **Correction** : écrire une ligne d'intention au journal avant l'appel ; sur toute exception de l'appel, chercher le nom
  dans l'inventaire et, s'il y est, veiller ou détruire par son identifiant ; mettre la lecture de la réponse dans le bloc.

### CLC2-05 — à corriger avant D-1b — trou ouvert par la correction de CLL-15 : l'agent peut arrêter l'exécuteur

- **Où** : `executeur_bac_v2.py`, `classer_execution`, l. 141-142, appelée sur la sortie d'erreur de l'item.
- **Chemin (éprouvé)** : un code Python d'agent qui écrit `bwrap: bonjour` sur sa sortie d'erreur lève `ErreurBac`, même avec
  un résultat « success ». Arrêt franc, non silencieux, mais déclenché par l'agent : il coupe la course au lieu d'être compté.
  Côté Lean : toute écriture de l'agent sur la sortie d'erreur (`dbgTrace` sous `native_decide`, par exemple).
- **Correction** : établir « le bac n'a pas démarré » par un canal que l'agent n'écrit pas (`bwrap --json-status-fd` vers un
  descripteur du harnais), jamais par un préfixe de ligne.

### CLC2-06 — à corriger — lecture du pare-feu du nuage : un seul pare-feu lu, aucune commande

- **Où** : `hetzner_v2.py`, `verifier_coupure_nuage`, l. 72-83 ; `piloter_poste_v2.sh` l. 8-9.
- **Chemins** : (éprouvé) un seul appel, `GET /firewalls/N`. Les autres pare-feux du serveur ne sont pas lus ; or les règles de
  plusieurs pare-feux s'ajoutent : un second pare-feu avec une sortie permise rouvre la sortie. L'état d'application
  (« applied » ou en attente) n'est pas lu. Aucune commande n'appelle la fonction (appel à la main, entre deux phases).
- **Ce qui tient** : `nftables` et sa sonde ; le bac n'a aucune interface.
- **Correction** : lire `GET /servers/N`, exiger que ses pare-feux soient exactement celui attendu, à l'état appliqué ; une
  commande `verifier-coupure` qui écrit le relevé au journal.

### CLC2-07 — à corriger avant toute création de serveur — le plafond par GO dépend encore de deux déclarations

- **Où** : `minuterie_v2.py`, `machines_anterieures` l. 82-95, `deja_depense_go` l. 60-79, `lire_montant` l. 53-57.
- **Chemins (éprouvés)** :
  - seconde machine **acceptée** si `--journal-creations` désigne un autre fichier et que le registre des dépenses n'est pas
    encore tenu (il l'est à la passation) ;
  - `--mot-de-lazar x` : toute chaîne non vide suffit ; le déjà-dépensé retenu reste **0,00** : le journal des créations ne
    sert pas au calcul. Deux fois 62,40 USD restent possibles ;
  - `lire_montant("18.52")` rend 18,0 et `"1.96"` rend 1,0 : le registre réel porte ces deux cellules à point décimal
    (`registres/depenses.md`) ; le déjà-dépensé est sous-compté. Un montant négatif est soustrait.
- **Correction** : chemin du journal fixé dans le code ; déjà-dépensé = le plus haut entre le registre et la somme « heures
  entamées × prix » des machines du journal ; mot de Lazar = identifiant d'une ligne de `registres/go.md` ou de
  `docs/decisions/`, vérifié ; point décimal lu, montant négatif refusé.

### CLC2-08 — à corriger — lignes sans essai, vues par mutation

24 mutations neuves sur des copies (import depuis la copie, sans `PYTHONPATH` hérité) : 15 tuées, 9 survivent.

1. n09 `set_option` suivi de plusieurs blancs, et le mot `skipKernelTC` seul (`gardes_lean_v2.py` l. 168) ;
2. n10 imports hors liste (l. 244) : aucun essai v2 ;
3. n12 plafond de 300 s de la pause (`minuterie_v2.py` l. 117) ;
4. n15 lecture en échec avant l'échéance, dans `veiller` (l. 134) ;
5. n17 filtre « ipv4 » du prix de l'adresse (`hetzner_v2.py` l. 61) ;
6. n20 `IPAddressDeny=any` retiré de la commande (`executeur_bac_v2.py` l. 181) ;
7. n21 `--unshare-all` retiré (l. 186) ;
8. n02 `»` seul admis et n04 « commande sans réponse » retirée : redondantes avec d'autres motifs, sans gravité.

Les lignes 6 et 7 sont les deux cloisons du bac : un essai sur le texte de la commande ne coûte rien ; l'épreuve sur la
machine les couvre par ailleurs.

## Réponses aux trois questions

1. **Levé ou contourné par l'essai ?** Les attaques citées sont arrêtées par le code, pas par l'essai : je les ai rejouées avec
   mes propres sources. Mais quatre corrections ferment l'exemple et non la classe : lexique (CLC2-01), code exécuté
   (CLC2-02), exceptions de la minuterie (CLC2-03), seconde machine (CLC2-07).
2. **Trous neufs des corrections** :
   - contrôle par l'entrée standard et nonce : aucun trou trouvé hors du code d'agent exécuté (CLC2-01, CLC2-02) ;
   - liste fermée d'attributs : tient ; la faiblesse est à côté (commandes et tactiques) ;
   - `creer-et-veiller` : CLC2-04, CLC2-07 ;
   - retentatives sans fin : voulues, bornées en cadence ; la minuterie meurt encore par ailleurs (CLC2-03) ;
   - lecture du pare-feu : CLC2-06 ; classement des pannes : CLC2-05.
3. **Essais** : `169 passed` ; mutations en CLC2-08.

## Notes

1. Cas sains refusés par le lexique v2, arrêt franc, à écrire dans les consignes des bras : `f '' s` (image d'un ensemble),
   `f ⁻¹' s` (image réciproque), `s!"…"`, tout identifiant `«…»`.
2. Le dossier `/item` entre dans `LEAN_PATH` du contrôle et n'est pas inventorié après la compilation : seuls `Item.lean`,
   `Item.olean`, `Item.ilean` devraient y être ; tout autre fichier devrait faire échouer G-L7.
3. Le tampon « réseau fermé » vaut pour tout le démarrage courant : une réouverture de `nftables` après la sonde n'est pas vue.
   Sans effet sur le bac (aucune interface), mais la mention « éprouvé fermé » devient fausse.
4. En mode tube, la sortie du contrôle est lue en mémoire sans borne avant la troncature à 16 Mio ; `text=True` lève sur une
   sortie non UTF-8 (arrêt franc).
5. `attribute [simp] a [init] b` passe la garde textuelle (seul le premier crochet est lu) ; ce n'est pas du Lean valide, donc
   sans effet ; un refus net serait plus sûr.
6. La devise rendue par `/pricing` n'est pas comparée à « EUR » ; `/server_types` est lu sans pagination (échec fermé).

## Ce que j'ai lancé

- Essais : commande de la consigne depuis mon arbre, import tracé vers
  `…/scratchpad/cl2-lean-d1a/arbre/src/controle_ia/lean_essai/gardes_lean_v2.py` : `169 passed`.
- Trois scripts de démonstration et un script de mutations, dans mon bac à sable, non versés ; chaque chemin « (éprouvé) » se
  rejoue avec les sources citées dans le texte du défaut.
- `registres/depenses.md` : en-tête, ligne de GO-2026-11-10-13 et colonne des coûts seulement, en lecture.
- Rien lu de `diag/`, `runs/`, du bras d'attaque, du mode tenu à l'écart, de T0.6, T0.7 ni de P3-bis. Arbre retiré à la fin.
