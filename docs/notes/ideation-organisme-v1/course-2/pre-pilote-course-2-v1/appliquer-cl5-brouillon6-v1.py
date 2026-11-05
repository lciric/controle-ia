#!/usr/bin/env python3
"""appliquer-cl5-brouillon6-v1.py — brouillon 6 de l'annexe des paramètres du bras méta, version 1.

Rédacteur : sous-agent neuf Fable 5.1 (reprise du chantier de conv-audit, 1er novembre 2026), qui n'a écrit ni les
brouillons 1 à 5, ni leurs contre-lectures, ni le script de calcul, ni l'erratum. Il traite la contre-lecture 5
(`contre-lecture-annexe-bras-meta-v1-brouillon5.md`, Sonnet 5.5, `156b9c557f9c5a692374db1f991a7e38846fa2e38214735178f5d5eae0911e2e`)
du brouillon 5 (`annexe-bras-meta-v1-brouillon5.md`, `c04ddf15c92c68c33a6770d42ffb6513c66414ee41a7ae76b7bf5bf6d91faf07`).

Ce script lit le brouillon 5, applique chaque substitution exacte de la liste SUBSTITUTIONS (l'ancien texte doit apparaître
exactement une fois, sinon arrêt), calcule l'empreinte du texte hors bloc N4 et celle du bloc de paramètres du brouillon 6
(mêmes définitions que le script de calcul v5 : tout sauf ce qui est strictement entre les deux marqueurs du bloc N4 ;
JSON canonique sans les deux champs libres) et les écrit dans le bloc N4, puis écrit le brouillon 6. Le brouillon 5 n'est
jamais modifié (R12). Aucun réseau, aucun appel de modèle, rien lu sous `donnees/`.

Usage :
    python3 -I appliquer-cl5-brouillon6-v1.py CHEMIN/annexe-bras-meta-v1-brouillon5.md CHEMIN/annexe-bras-meta-v1-brouillon6.md
"""
import hashlib
import json
import re
import sys

if len(sys.argv) != 3:
    sys.exit("usage : appliquer-cl5-brouillon6-v1.py BROUILLON5 BROUILLON6")
SRC, DST = sys.argv[1], sys.argv[2]
SHA5_ATTENDUE = "c04ddf15c92c68c33a6770d42ffb6513c66414ee41a7ae76b7bf5bf6d91faf07"

# Valeurs reportées depuis le rejeu du script v5 sur le brouillon 6 (voir traitement-contre-lecture-5-annexe-bras-meta-v1.md).
SORTIE_B6 = {
    "empreinte": "02d9c99432ec923b63573398f24ed2344243987b4a2b40238254b49e4e311087",
    "lignes": "313",
    "ecart_v5": "cinq",
}

CL5 = "156b9c557f9c5a692374db1f991a7e38846fa2e38214735178f5d5eae0911e2e"

POUR_LAZAR = """## Pour Lazar — ce qu'on te demande et ce que dit l'annexe, en clair (CA5-04 ; nouveau au brouillon 6)

1. **Verdict de la contre-lecture 5** (Sonnet 5.5, 1er novembre 2026, `156b9c55…`) sur le brouillon 5 : « présentable après corrections », aucun bloquant, un constat majeur (collision des noms de niches avec une liste de mots interdits voisine), quatre moyens, sept mineurs ; rejeu du script identique octet pour octet ; recalculs indépendants concordants. Ce brouillon 6 applique ses corrections (section 16) ; il doit être contre-lu à son tour avant tout scellement (R2) : rien n'est gelé ici.
2. **Ce qu'on te demande** (section 9, table 11) : (i) un mot sur DEP10 (les synthèses des questions 4 à 7 valent-elles les verdicts scellés que la condition de gel exige ?) ; (ii) l'option du nœud N4 : garder la bande d'éloignement [2 ; 3] et accepter le repli comme mesure (option (a), accord des quatre espèces du collisionneur, tenu sous conditions au tour 2) ou élargir la bande à [2 ; 4] (option (b1), recommandation de l'annexe, confiance 0,55, que le collisionneur n'a pas vue) ; (iii) si la paire « détection séquentielle – lecture des activations » reste dans le profil (choix de l'annexe) ou en sort (condition des quatre espèces) ; (iv) si les jeux de données comptent comme structure partagée (option A recommandée, écart à ta décision R-638) ; (v) la forme de la relecture du brouillon 6 (entière ou limitée aux passages changés) ; (vi) nouveau au brouillon 6 : que la liste des mots interdits servie au lecteur de niches ne contienne pas les étiquettes de classe `N1` à `N4` (sinon la garde A4 arrête toute lecture de niche), et la lecture de l'issue observée (section 6).
3. **Ce que disent les chiffres, sous une loi des niches que nous supposons (SUPPOSÉ)** : à 10 fiches, un lot sur deux contient une paire du profil sous (a), huit sur dix sous (b1) ; à 6 fiches, un sur quatre et un sur deux. Sous la loi du brouillon 1, celle que le collisionneur a vue, (b1) n'apporte que 0,05 à 0,06. Dans tous les cas, le pré-pilote éprouve la chaîne (lecture des niches, choix d'une paire, fusion, aiguilleur, juges), pas le profil : une seule paire ne réfute rien.
4. **Ce qui change au brouillon 6** : repli et « non produit » comptés sans double compte (à 6 fiches sous (b1) : profil 0,47, repli 0,50, non produit 0,03) ; deux mots-indices retirés de la niche « science de l'évaluation » parce que la question les impose à toutes les fiches ; lecture de l'issue observée et liste d'arrêt réunies en deux tables ; collision des noms de niches avec une liste de mots interdits voisine, reproduite et neutralisée par une condition sur la liste gelée ; citation de Bettencourt et Kaiser vérifiée sur le PDF empreinté ; points de forme. Aucune probabilité de la simulation ne change ; l'empreinte du bloc de paramètres change (indices de n6).
5. **Ce qui ne dépend que de toi** : le champ `approbation_lazar` du bloc de paramètres (un `R-NNN` de `registres/decisions.md`) ; le champ `contre_lecture` reste « À REMPLIR » jusqu'à la contre-lecture du brouillon 6 (le code v55 exige que le rapport cité porte sur le texte scellé lui-même) ; aucune valeur ne prend de défaut à 48 heures.

## Lexique des codes (CA5-04 ; nouveau au brouillon 6)

| Code | Ce qu'il désigne |
|---|---|
| CA1-nn, CA3-nn, CA4-nn, CA5-nn | constats numérotés des contre-lectures des brouillons 1, 3, 4 et 5 de cette annexe (CA1-05 : « le profil est rarement présent » ; CA1-04 : « quelles structures partagées comptent comme fortes ») |
| N4, N5, N11, N1 | nœuds de décision de la question des nœuds posée au collisionneur (v12) : N4 cette annexe ; N5 choix de code ; N11 ponts plantés et reconduction des bras ; N1 monde synthétique |
| tour 1, tour 2 ; espèces A, B, C, D | les deux tours du collisionneur sur la question des nœuds (31 octobre et 1er novembre) ; les quatre modèles lecteurs (A Fable 5.1, B Opus 4.6, C Gemini 4 Argon, D Kimi K3.1 Pro) |
| options (a) à (d2) | réponses possibles à CA1-05 : (a) accepter le repli ; (b1) bande [2 ; 4] ; (b2) bande retirée ; (c1) quinze fiches ; (c2) passes réunies ; (d1) canal faible ≤ 2 ; (d2) changer le profil ; lettres (a) à (h) de N4 et de l'erratum : table de l'erratum v2 |
| options A, B, C | réponses possibles à CA1-04 : A objets et méthodes comptés ; B jeux de données comptés aussi ; C A sans les structures séquentielles |
| (R2), (R3) de la règle des affirmations mixtes | alternatives de cette règle (section 1), sans lien avec les règles R2 et R3 des consignes permanentes |
| n1 à n6 | les six niches de la grille (identifiants complets dans le bloc de paramètres) |
| c, e, s | canal de communication entre deux niches (0 à 3) ; éloignement de contenu (1 à 5) ; nombre de structures comptées partagées par deux fiches |
| m, r | part des fiches mixtes de l'axe 1 ; part de ces fiches rangées en n1 (grille de sensibilité, section 1) |
| P(≥ 1), P(méta) | probabilité qu'un lot contienne au moins une paire du profil ; probabilité que la paire méta retenue soit dans le profil |
| repli, non produit | la paire retenue hors profil quand le profil est vide ; aucun choix possible (aucune paire éligible, niches indistinctes, moins de deux fiches étiquetées) |
| loi par axe, loi du brouillon 1, « n6 fort », « n2 fort » | lois a priori des niches, toutes SUPPOSÉ ; dans la sortie du script, la loi du brouillon 1 s'appelle `annexe-b1` : ce n'est pas l'option (b1) (CA5-12) |
| kappa, Jaccard (S28) | accord des deux lecteurs sur la niche (kappa de Cohen) et sur les structures (indice de Jaccard) ; seuils 0,40 et 0,30 |
| DEP10, D-h, D-e | condition de gel du préenregistrement (annexe écrite après les verdicts des questions 4 à 7) ; décision « le pré-pilote attend l'annexe scellée » ; décision « niche = méthode de l'affirmation centrale » |
| M4, M5, M8, M9 ; P14 ; S18, S22, S23, S24, S28, S29 | mesures, prédiction et seuils du préenregistrement du pré-pilote (brouillon 10) : M9 bras méta ; P14 paires dans le profil ; S28 accord des lecteurs ; S29 (a à f) grille, canal, structures, éloignement, score, repli |
| A4, A9, A20, A21 | arrêts et règles du préenregistrement : A4 étiquette interdite dans une entrée servie ; A9 rien lu sous `donnees/` ; A20 annexe non conforme ⇒ bras méta non produit ; A21 journal ouvert après É9 |
| É0, É2, É7, É7b, É9 | étapes du plan du pré-pilote : É0 contrôles avant lancement ; É2 proposeur ; É7 et É7b lectures d'étiquettes et de niches ; É9 fin des lectures |
| I-1 à I-15 | incompatibilités relevées entre l'annexe et le code (section 10) |
| C12, O15, L3, E1′ | compte des bras non lancés ; question ouverte « grille dégénérée » ; lecture du désaccord ; instrument d'évaluation hors du monde synthétique |
| R1 à R14 ; R-NNN ; GO-AAAA-MM-JJ-NN | règles gelées des consignes permanentes ; décisions de `registres/decisions.md` ; autorisations de dépense de `registres/go.md` |
| R-638, R-637 | décisions du directeur : profil du bras méta (canal faible, structure commune forte, éloignement non extrême, jeu de données nommé) ; carte des chapelles |
| texte I ; pièce B ; pièce 10 ; HELIOS ; Kimi ; Gu-Krenn | la question « défense » servie au proposeur (v5) ; pièce servie au collisionneur sur HELIOS (méthode de référence boîte blanche) ; contre-lecture du brouillon 1 servie au collisionneur ; proposeur du pré-pilote ; bras de fusion fondé sur Gu et Krenn 2024 |
| code v53 à v56 ; `bisociateur`, `course2`, `fiches`, `outils` | versions de l'orchestrateur du pôle et ses modules ; CL21 : contre-lecture du code v56 |
| conv-audit, session-depot | les deux sessions qui tiennent respectivement cette annexe et la question des nœuds |
| SUPPOSÉ | valeur posée sans mesure, à lire comme hypothèse |
| sortie § n | section n de la sortie du script de calcul v5 rejoué sur ce brouillon |

"""

SECTION_16 = """## 16. Ce qui change par rapport au brouillon 5 (contre-lecture 5)

Base : brouillon 5 (`c04ddf15c92c68c33a6770d42ffb6513c66414ee41a7ae76b7bf5bf6d91faf07`), copié puis modifié par les substitutions exactes du script `appliquer-cl5-brouillon6-v1.py` (même dossier ; chaque ancien texte apparaît une fois) ; brouillon 5, script v5, sortie v5, erratum v2 gardés sans modification (R12). Constats : contre-lecture du brouillon 5 (Sonnet 5.5 neuf, `156b9c557f9c5a692374db1f991a7e38846fa2e38214735178f5d5eae0911e2e` ; verdict « présentable après corrections » ; 0 bloquant, 1 majeur, 4 moyens, 7 mineurs). Traitement détaillé, substitutions et chiffres revérifiés : `traitement-contre-lecture-5-annexe-bras-meta-v1.md` (même dossier). **Dix constats acceptés (dont trois en partie), aucun refusé, deux hors du mandat de ce brouillon** (ils touchent le script v5 et l'erratum v2, gardés sans modification).

| Constat | Gravité | Décision | Traitement | Où |
|---|---|---|---|---|
| CA5-01 — `n1_…` à `n6_…` en collision avec les étiquettes de classe `N1` à `N4` de la liste A4 de la consigne de l'aiguilleur | majeur | accepté, voie (ii) | collision reproduite avec `fiches_v53.garde_etiquettes` du code v55 (liste servie : N1 à N4 ; quatre règles : N1, N2 ; `D1` à `D3` trouvés si une liste les contenait) ; condition écrite sur la liste gelée (ni `N1` à `N4`, ni `D1` à `D3`, ni un identifiant de la grille), confirmation du détenteur de la configuration avant É0 ; renommage (voie (i)) non fait : il touche le script et rouvre une relecture entière, alternative posée à Lazar | § 1, § 8, § 9 (étape 4), § 11 |
| CA5-02 — repli 0,53 et non produit 0,028 comptés deux fois | moyen | accepté | trois issues qui font 1, par option, en table 0.2 et au bloc N4 (repli = 1 − P(méta) − P(aucune paire éligible), arithmétique sur la sortie § 3, ± 0,01) ; 0,53 → 0,50 en 0.3 | § 0.2, § 0.3, bloc N4 |
| CA5-03 — ni règle de lecture figée de l'issue observée, ni liste d'arrêt propre | moyen | accepté | table « issue observée → libellé → audit R4 » (aucune issue ne réfute P14) et table des arrêts (condition, action, où), proposées À GELER ; alternative « au préenregistrement brouillon 11 » écrite | § 6, § 0.5, § 11 |
| CA5-04 — codes non développés ; résumé après 16 500 caractères de provenance | moyen | accepté en partie | boîte « Pour Lazar » et lexique des codes en tête ; « pièces lues » et « auteurs » **non déplacés** en fin de document : un déplacement de 16 500 caractères rendrait la relecture limitée (option (ii) de l'étape 3) inutilisable et ne change rien au fond ; à faire au brouillon qui portera l'option choisie si Lazar le demande | en-tête |
| CA5-05 — critère de retrait des indices non appliqué à n6 | moyen | accepté | « transfert » et « famille tenue à l'écart » retirés des indices de n6 (texte I, l. 36 et 52 : définis pour toutes les fiches, imposés à l'axe 1) ; « préenregistrement » gardé avec sa raison ; la définition en une ligne de n6 garde ses mots ; sensibilité « l'axe 1 se range en partie en n6 » non chiffrée (script non modifié) ; **l'empreinte du bloc de paramètres change** | § 1, bloc N4, § 11 |
| CA5-06 — n5 « sans partenaire sous (d1) » faux | mineur | accepté | « sous (a), (c1) et (c2) » (n3–n5 est dans le profil sous (d1), vérifié sur les tables) | § 0.2 bis |
| CA5-07 — Bettencourt et Kaiser : PDF déjà versé ; « cascade » et « branching » absents | mineur | accepté | vérifié sur le PDF empreinté (`2fb9aab0…`, compagnon conforme) : composante géante soutenue (résumé, p. 3) ; cascade et rapport de branchement non attribués à cette source | § 7 (journal 6) |
| CA5-08 — deux gardes sans cas piégé versé | mineur | accepté en partie | section 4 : l'artefact de la garde du désaccord est joué à É0, non par le script ; cas piégé de la garde des marqueurs du script : **hors mandat** (script v5 gardé ; à un script v6) | § 4 |
| CA5-09 — erratum v2 : « contre-lecture à venir » ; 0,12 contre 0,13 pour (d) | mineur | hors mandat | l'erratum v2 est scellé chez conv-audit et n'est pas réécrit ici ; une version 3 de l'erratum le corrigerait ; l'annexe ne porte ni la phrase ni l'écart (elle écrit 0,12 pour (d1), sortie § 17) | — |
| CA5-10 — 0,3 d'erreur-type du kappa sans trace ; effectifs 6 et 10 non expliqués | mineur | accepté en partie | le 0,3 est dit « ordre de grandeur à la main, non calculé par le script » (0,2 à 0,3 selon les marges) ; origine de 6 (S18 du préenregistrement brouillon 10, l. 360) et de 10 (texte I) écrite, n = 8 cité ; calcul dans le script : hors mandat | § 0.1, § 1 |
| CA5-11 — quatre alternatives sans avantage ou sans inconvénient | mineur | accepté | une demi-ligne ajoutée à chacune (poids 0 ; (R3) ; S28 0,50 et 0,40 ; désaccord sur chaque paire) | § 1, § 6, § 11 |
| CA5-12 — libellé `annexe-b1` de la sortie ; « plus de six minutes » | mineur | accepté en partie | lexique : `annexe-b1` = loi du brouillon 1, pas l'option (b1) ; durée « de trois à sept minutes selon la machine » ; le libellé imprimé est dans le script : hors mandat | en-tête, § 9 |

**Autres changements, déclarés.** (1) Les blocs `regles_lecteur_niches`, `jeu_essai_non_vacuite` et `variante_bloc_n4` sont identiques à ceux des brouillons 4 et 5 ; le bloc `parametres_bras_meta` change par une seule chaîne (`definitions_niches.n6_science_evaluation`, CA5-05) : nouvelle empreinte du bloc de paramètres (bloc N4). (2) Aucun chiffre de simulation ne change : le script v5, rejoué sur ce brouillon, redonne les mêmes sections 1 à 7 et 10 à 18 ; les sections 2, 9 et 16 (épreuve par le code v55) passent sur les définitions modifiées (bloc N4, ligne « calcul »). (3) Aucun script nouveau ; le script v5 et sa sortie sur le brouillon 5 sont gardés ; la sortie sur le brouillon 6 est à verser avec compagnon par conv-audit (R6). (4) Le champ `contre_lecture` reste « À REMPLIR » : le code v55 exige que le rapport cité porte sur le brouillon relu, identique au texte scellé hors des deux champs, et le script v5 arrête si ce champ n'est pas « À REMPLIR » ; la contre-lecture 5 est citée en clair dans le bloc N4 (ligne « contre-lecture ») et ici. (5) Je n'ai tranché ni CA1-05, ni CA1-04, ni c(n1, n2), ni la voie (i) ou (ii) de CA5-01 ; la recommandation (b1) × A et sa confiance restent celles des brouillons 3 à 5.

"""

LIGNE_412_ANCIENNE = """- **Calcul joué sur ce fichier** : script `calcul-profil-bras-meta-v1-brouillon5.py` `612e543d16f7b70d10a09a4f07fba28777fcf9815fdc14f176b5ef28da315607` ; sortie `calcul-profil-bras-meta-v1-brouillon5.sortie.txt` `16e5ff7edd4236ae804365a2f1b6258d037d0ce3853e8a40210bfecc91d84ccb` (313 lignes) ; deux rejeux, chacun par `python3 -I` depuis un dossier temporaire vide neuf (resté vide), troisième argument le dossier de la synthèse du tour 1 : le premier sur ce fichier avant que ce bloc reçoive l'empreinte de la sortie et celle du texte hors bloc N4, le second sur ce fichier tel qu'il est écrit ; sorties identiques octet pour octet (heures des rejeux : erratum v2, « Pièces ») : la sortie ne lit, dans ce bloc, que le JSON, ce que l'égalité des deux rejeux éprouve ; un premier jeu, sur un état antérieur du texte qui gardait quatre marqueurs de chiffres en section 2, a été arrêté par la garde de la section 19 (cas artefact de cette garde) et n'est pas versé ; empreinte du bloc de paramètres en JSON canonique sans les deux champs libres (inchangée au remplissage ; **inchangée du brouillon 4 au brouillon 5**, sortie § 19) : `b2cc74e13d19a4ed54c93ed6b27af1c41ea610ed6e106e3e0b2893d62e3abf45` ; **empreinte du texte hors bloc N4** (sortie § 8 ; elle doit être la même au brouillon qui portera l'option choisie, sinon ce brouillon se relit, section 9, étape 3) : `5c01e16fbdbea4f97d10ec644389523b730bf3ee905c1742cf0a68a9cb3c0bd8` (brouillon 4 : `82df8775…`) ; marqueurs entre doubles crochets restants : 0 (sortie § 8) ; marqueurs de rédaction hors bloc N4 : 0 (sortie § 19). Les sections 1 à 17 de la sortie v5 (ses 271 premières lignes) diffèrent de la sortie v4 (`9279d4ad…`, 271 lignes) par trois lignes et par aucun chiffre (vérifié par `diff`) : la ligne de titre (l. 1), l'empreinte du texte hors bloc N4 (l. 95, section 8) et la ligne 271, « fin » en v4, ligne vide en v5 (« fin » y est la dernière ligne, après la section 19) ; les sections 18 et 19 sont nouvelles. Écart du texte hors bloc N4 au brouillon 4 (sortie § 19) : 33 passages, 36 lignes du brouillon 4 remplacées ou retirées, 79 lignes du brouillon 5, empreinte de l'écart `70933ab1122841e2baf4817467c7b8cdf8358d2137d7116f375f2bd982465c07`."""

LIGNE_412_NOUVELLE = ("- **Calcul joué sur ce fichier** : script v5 `calcul-profil-bras-meta-v1-brouillon5.py` "
    "`612e543d16f7b70d10a09a4f07fba28777fcf9815fdc14f176b5ef28da315607` (gardé sans modification, R12 ; aucun script v6), "
    "rejoué deux fois par le rédacteur du brouillon 6 sur ce fichier, chacun par `python3 -I` depuis un dossier temporaire vide "
    "neuf (resté vide), dépôt reconstitué par `git show` (code v55, `src`, question des nœuds v12, relecture Opus ; empreintes "
    "égales à celles attendues par le script), troisième argument le dossier de la synthèse du tour 1 (trois pièces, empreintes "
    "contrôlées par le script) : le premier sur ce fichier avant que ce bloc reçoive l'empreinte de la sortie, le second sur ce "
    "fichier tel qu'il est écrit ; sorties identiques octet pour octet : "
    "`calcul-profil-bras-meta-v1-brouillon5.sur-brouillon6.sortie.txt` `%(empreinte)s` (%(lignes)s lignes ; hors dépôt, à verser "
    "avec compagnon par conv-audit, R6) ; rejeu préalable du même script sur le brouillon 5 : sortie identique à `16e5ff7e…` "
    "octet pour octet ; empreinte du bloc de paramètres en JSON canonique sans les deux champs libres (inchangée au "
    "remplissage) : `%(bloc)s` (**changée** depuis les brouillons 4 et 5, `b2cc74e1…`, par la seule chaîne des indices de "
    "n6, CA5-05) ; **empreinte du texte hors bloc N4** (sortie § 8 ; elle doit être la même au brouillon qui portera l'option "
    "choisie, sinon ce brouillon se relit, section 9, étape 3) : `%(hors)s` (brouillon 5 : `5c01e16f…` ; brouillon 4 : "
    "`82df8775…`) ; marqueurs entre doubles crochets restants : 0 (sortie § 8) ; marqueurs de rédaction hors bloc N4 : 0 "
    "(sortie § 19). La sortie sur le brouillon 6 diffère de la sortie v5 sur le brouillon 5 (`16e5ff7e…`) par %(ecart_v5)s lignes et "
    "par aucun chiffre de simulation (vérifié par `diff`) : empreinte du bloc de paramètres (l. 3), empreinte du texte hors "
    "bloc N4 (§ 8), et les lignes du § 19 qui comparent au brouillon 4 (chemin figé dans le script v5 : le § 19 compare au "
    "brouillon 4, non au brouillon 5 ; l'écart au brouillon 5 est la liste des substitutions de `appliquer-cl5-brouillon6-v1.py`, "
    "même dossier)." )

SUBSTITUTIONS = [
    # Statut (CA3-09, historique des brouillons)
    ("(CA3-09 ; c'est le cas du brouillon 4, qui corrigeait la prose du brouillon 3, et du brouillon 5, qui corrige celle du brouillon 4)",
     "(CA3-09 ; c'est le cas du brouillon 4, qui corrigeait la prose du brouillon 3, du brouillon 5, qui corrige celle du brouillon 4, et du brouillon 6, qui traite la contre-lecture du brouillon 5 : CA5-01 à CA5-12, section 16)"),
    # CA5-04 : boîte « Pour Lazar » et lexique, avant l'explication du code v55
    ("\n\n**Pourquoi le texte est écrit ainsi (code v55).**",
     "\n\n" + POUR_LAZAR + "**Pourquoi le texte est écrit ainsi (code v55).**"),
    # Auteurs
    ("**A9 respecté** par les cinq :",
     "**Brouillon 6** — sous-agent neuf Fable 5.1 (reprise du chantier de conv-audit par une autre session, 1er novembre 2026, après 19:20 UTC, `date -u`), qui n'a écrit ni les brouillons 1 à 5, ni leurs contre-lectures, ni le script v5, ni l'erratum, ni le préenregistrement : il traite la contre-lecture du brouillon 5 (CA5-01 à CA5-12 ; section 16) par le script de substitutions `appliquer-cl5-brouillon6-v1.py` (même dossier), rejoue le script v5 sur les brouillons 5 et 6, reproduit la collision CA5-01 avec le code v55 et vérifie la citation de Bettencourt et Kaiser sur le PDF empreinté. **A9 respecté** par les six :"),
    ("Réserve d'indépendance (inchangée)** : la contre-lecture doit venir d'un modèle autre qu'Opus (Sonnet 5.5 ou Fable 5.1 ; R2).",
     "Réserve d'indépendance** : la contre-lecture doit venir d'un modèle autre que ceux des rédacteurs ; les brouillons 1 à 5 sont d'Opus 5.5 et le brouillon 6 de Fable 5.1 : la contre-lecture du brouillon 6 vient de Sonnet 5.5 ou d'un autre modèle qu'Opus 5.5 et Fable 5.1 (R2)."),
    # Pièces lues au brouillon 6
    ("\n- **Calcul** : `calcul-profil-bras-meta-v1-brouillon4.py`",
     "\n  - lus au brouillon 6 seulement (empreintes recalculées par `sha256sum`) : contre-lecture du brouillon 5 `contre-lecture-annexe-bras-meta-v1-brouillon5.md` `156b9c557f9c5a692374db1f991a7e38846fa2e38214735178f5d5eae0911e2e` (sans compagnon ; CA5-01 à CA5-12, lue en entier) ; brouillon 5 `c04ddf15…` (lu en entier), script v5 `612e543d…` (en-tête, lecture de l'annexe, sections 8, 9, 16, 18, 19) et sortie v5 `16e5ff7e…` (lue en entier), brouillon 4 `397e1cbc…`, script v4 `48e3c57d…` et sortie v4 `9279d4ad…`, tous retrouvés par `git show` sur le commit `e1b603bf` du dépôt de travail (le dossier de conv-audit transmis ne contenait ni le script ni les sorties) ; erratum v2 `b3196687…` (lu en entier ; CA5-09) ; contre-lecture du brouillon 4 `7b467e84…` (en-tête) ; préenregistrement brouillon 10 `ea940d56…` (l. 360, S18 : effectif minimal 6) ; texte I `a7501449…` (l. 36, 52, 57 ; CA5-05) ; consigne de l'aiguilleur `consigne-aiguilleur-v1.md` `c2efa12003bb8ce1a9a636e4610fa9caa9464ae685b0bd628c9c351b64e3271e` (l. 462 : liste A4 avec `N1` à `N4` et `M6b` ; CA5-01) ; code v55 `fiches_v53.py` `7cfcf832…`, `fiches_v54.py` `1ab0796d…`, `outils.py` `966d9553…` (commit `9fb76cd9`, essai de la collision) ; PDF de Bettencourt et Kaiser `arxiv-1504.00319-bettencourt-kaiser-2015.pdf` `2fb9aab049631cdffe59631ce5196b800220dbeb584afd179ce8e6623485a523` et PDF d'Uzzi et coll. `53297098…` (compagnons conformes, extraits par `pdftotext` ; CA5-07) ; synthèse du tour 1 v12 `e4d5a5c9…`, ses critères `22edbf47…`, question du tour 2 `19ff79d9…` (`git show`, commit `9960f154`), question des nœuds v12 `a7fac44b…`, relecture Opus `d1209130…` (pièces exigées par le script v5, empreintes égales). **Non lus au brouillon 6** : synthèse du tour 2, synthèses des questions 4 à 7, `registres/decisions.md`, brouillons 1 à 3 et leurs contre-lectures, archive du code v56 ; rien sous `donnees/`.\n- **Calcul** : `calcul-profil-bras-meta-v1-brouillon4.py`"),
    ("**Renvois « sortie § n » : sections de la sortie v5** (§ 1 à 17 : mêmes chiffres que la sortie v4).",
     "**Renvois « sortie § n » : sections de la sortie v5** (§ 1 à 17 : mêmes chiffres que la sortie v4). **Au brouillon 6** : aucun script nouveau ; le script v5 (gardé sans modification, R12) est rejoué deux fois sur le brouillon 6 (empreintes au bloc N4) ; ses chiffres de simulation sont ceux de la sortie v5 ; son § 19 compare au brouillon 4 (chemin figé dans le script), non au brouillon 5 : l'écart au brouillon 5 est la liste des substitutions de `appliquer-cl5-brouillon6-v1.py` (même dossier), décrite dans `traitement-contre-lecture-5-annexe-bras-meta-v1.md`."),
    # CA5-10 (2) : effectifs 6 et 10, n = 8
    ("deux par axe, texte I, « Déroulé »).",
     "deux par axe, texte I, « Déroulé »). **Effectifs 6 et 10 (CA5-10)** : 10 est ce maximum ; 6 est l'effectif minimal de fiches non aiguillées que le préenregistrement brouillon 10 fixe (S18, l. 360 : « effectif minimal de fiches de Kimi non aiguillées […] 6 ») ; le nombre de fiches qui franchissent l'aiguilleur est lui-même aléatoire, et P14 est donnée conditionnellement à n = 6 et n = 10 ; la sortie imprime aussi n = 8 (P(≥ 1) / P(méta) : (a) 0,42 / 0,41 ; (b1) 0,70 / 0,69 ; (b2) 0,78 / 0,77 ; (d1) 0,75 / 0,74 ; sortie § 3), jamais cité ailleurs dans l'annexe."),
    # CA5-02 : trois issues, table 0.2
    ("6 lectures d'étiquettes × 0,025).",
     "6 lectures d'étiquettes × 0,025).\n\n**Trois issues d'un lot, qui font 1 (CA5-02).** « Aucune paire éligible » est un sous-ensemble de « la paire méta n'est pas dans le profil » : dans ces lots, il n'y a pas de repli, le bras est « non produit ». Les trois issues sont donc, par option : **profil** = P(méta) ; **repli** (compté « hors profil ») = 1 − P(méta) − P(aucune paire éligible) ; **non produit** = P(aucune paire éligible) (0,028 à 6 fiches, 0,001 à 10, 0,000 à 12 et au-delà, sous toutes les options à deux places par axe ; sortie § 3). Le script n'imprime pas le repli : arithmétique sur les chiffres arrondis de la sortie § 3, ± 0,01. Profil / repli / non produit, à 6 puis 10 fiches : (a) 0,25 / 0,72 / 0,03 et 0,55 / 0,45 / 0,00 ; (b1) 0,47 / 0,50 / 0,03 et 0,83 / 0,17 / 0,00 ; (b2) 0,56 / 0,41 / 0,03 et 0,90 / 0,10 / 0,00 ; (d1) 0,53 / 0,44 / 0,03 et 0,87 / 0,13 / 0,00 ; (c1) à 12 puis 15 : 0,66 / 0,34 / 0,00 et 0,79 / 0,21 / 0,00 ; (c2) réunies à 12 puis 20 : 0,66 / 0,34 / 0,00 et 0,91 / 0,09 / 0,00, avec la perte de la passe « tableau » (passe 1 à 6 puis 10) : 0,44 / 0,53 / 0,03 et 0,71 / 0,29 / 0,00. Ce sont les comptes que les quatre espèces du tour 2 demandent avec le verdict (section 0.5) ; leur lecture est en section 6."),
    # CA5-06
    ("n5 (sans partenaire sous (a), (c1), (d1))", "n5 (sans partenaire sous (a), (c1) et (c2) ; sous (d1), n3–n5 est dans le profil)"),
    # CA5-02 en 0.3
    ("à 6 fiches il joue encore avec 0,53.",
     "à 6 fiches il joue encore avec 0,50, et le bras n'est pas produit (aucune paire éligible) avec 0,03 ; les trois issues font 1 (table 0.2, CA5-02)."),
    # CA5-03 renvoi en 0.5
    ("le libellé et la garde sont à écrire au préenregistrement",
     "le libellé et la garde sont proposés en section 6 (CA5-03) et restent à recopier au préenregistrement"),
    # CA5-05 : indices de n6 (table de la section 1 et définition servie)
    ("| banc, famille tenue à l'écart, transfert, universalité, puissance simulée, préenregistrement |",
     "| banc, universalité, puissance simulée, préenregistrement |"),
    ("Indices : banc, famille tenue à l'écart, transfert, universalité, puissance simulée, préenregistrement.",
     "Indices : banc, universalité, puissance simulée, préenregistrement."),
    ("et leur seule présence ne range pas une fiche.",
     "et leur seule présence ne range pas une fiche. **Au brouillon 6 (CA5-05)** : « transfert » et « famille tenue à l'écart » sont retirés des indices de n6 par le même critère : le glossaire du texte I (l. 36) définit « Famille tenue à l'écart », « Transfert » et « Invariance » pour toutes les fiches, et l'axe 1 impose à chaque fiche « (d) l'invariance qui justifie le transfert » (l. 52) ; ces mots restent dans la définition en une ligne de n6, qui nomme l'objet de la niche (ce que le banc mesure), non dans la liste de ce qui range une fiche. « Préenregistrement » est gardé : le texte I ne l'impose qu'à l'axe 4 (et le nomme à l'axe 2 (d), « premier test préenregistrable », l. 57), où la loi par axe range déjà 0,70 des fiches en n6. La sensibilité « l'axe 1 se range en partie en n6 » (la paire n1–n6 porte 0,53 des paires méta du profil sous (a), sortie § 10) n'est pas chiffrée : le script v5 n'est pas modifié ; à ajouter à un script v6 si Lazar la demande. Aucun chiffre de l'annexe ne dépend des mots-indices (la simulation tire les niches, elle ne lit aucun texte) ; l'empreinte du bloc de paramètres change (bloc N4)."),
    # CA5-10 (1) et CA5-11 : S28
    ("erreur-type du kappa de l'ordre de 0,3 à 10 fiches, SUPPOSÉ",
     "erreur-type du kappa de l'ordre de 0,2 à 0,3 à 10 fiches selon les marges, SUPPOSÉ ; ordre de grandeur à la main, **non calculé par le script** : à ajouter à un script v6 ou à retirer, CA5-10"),
    ("Alternative : 0,50 et 0,40 — inconvénient :",
     "Alternative : 0,50 et 0,40 — avantage : accord plus exigeant, moins de paires « loin » fabriquées par une lecture bruitée ; inconvénient :"),
    # CA5-11 : (R3)
    ("(R3) laisser le choix au lecteur (brouillon 1) — inconvénient :",
     "(R3) laisser le choix au lecteur (brouillon 1) — avantage : aucun défaut mécanique, la fiche est rangée selon ce que le lecteur juge central ; inconvénient :"),
    # CA5-01 : section 1
    ("la liste gelée de la configuration reste à éprouver à É0.",
     "la liste gelée de la configuration reste à éprouver à É0 ; **une liste voisine du même pré-pilote contient les étiquettes de classe `N1` à `N4`, que la normalisation trouve dans `n1_…` à `n4_…` : collision reproduite et condition sur la liste gelée en section 8 (CA5-01)**."),
    # CA5-08 : section 4
    ("artefact = fonction de score qui varie avec le désaccord → arrêt.",
     "artefact = fonction de score qui varie avec le désaccord → arrêt. **Où il est joué (CA5-08)** : le script de l'annexe n'appelle `garde_desaccord_v54` que sur le cas sain (sortie § 2 et § 9) ; l'artefact est à jouer à É0 (section 9, étape 9), non par le script."),
    # CA5-11 : poids 0
    ("Alternative : poids 0 (égalités au tirage). Confiance : 0,5.",
     "Alternative : poids 0 (égalités au tirage) — avantage : le choix dans le profil ne favorise pas les paires faciles à fusionner (limite CA1-08) ; inconvénient : entre plusieurs paires du profil, la paire retenue est tirée au sort, sans raison lisible. Confiance : 0,5."),
    # CA5-03 : lecture de l'issue et liste d'arrêt (section 6)
    ("\n\n**Calcul et rejeu.** Script et sortie",
     "\n\n**Lecture de l'issue observée (CA5-03 ; proposée, À GELER par Lazar ; nouvelle au brouillon 6).** Une seule case et une seule paire méta au pré-pilote : **aucune issue observée ne réfute P14** (une probabilité par lot ne se lit pas sur un lot) ; P14 est indicative et sert d'étalonnage, l'issue est rapportée à côté d'elle (sous (b1) à 6 fiches : profil 0,47 / repli 0,50 / non produit 0,03, table 0.2). Le libellé du verdict est le même sous les trois issues, « chaîne éprouvée, profil non éprouvé » (condition des quatre espèces au tour 2, section 0.5), suivi de l'issue et des comptes.\n\n| Issue observée | Libellé du verdict (proposé) | Comptée comme | Audit de symétrie (R4) |\n|---|---|---|---|\n| **profil** : la paire méta retenue est dans le profil | « chaîne éprouvée, profil non éprouvé ; issue : profil (1 paire du profil parmi k éligibles) » | méta : profil | oui si le kappa est dégénéré (deux lecteurs constants) ou si toutes les paires éligibles sont dans le profil : trop propre, audit des lectures |\n| **repli** : des paires éligibles, aucune dans le profil | « chaîne éprouvée, profil non éprouvé ; issue : repli (0 paire du profil parmi k éligibles) » | méta : hors profil | oui si aucune paire éligible ne partage une structure (lecteurs qui ne relèvent rien) : audit des lectures |\n| **non produit** : aucune paire éligible, niches indistinctes, ou moins de 2 fiches étiquetées | « chaîne non éprouvée pour le bras méta ; issue : non produit (cause) » | non lancé, C12 (O15 si grille dégénérée) | oui, toujours : la cause est auditée (lectures rejetées, grille, effectif) |\n\nAlternative : laisser libellé et garde au préenregistrement (brouillon 11, sections de P14 et de M9), l'annexe ne portant que les comptes — avantage : une seule pièce gelée pour les verdicts ; inconvénient : l'annexe scellée renverrait à une section qui n'existe pas encore. Confiance : 0,5.\n\n**Liste d'arrêt propre à l'annexe (CA5-03 ; réunie ici, aucune condition nouvelle).**\n\n| Condition | Action | Où |\n|---|---|---|\n| annexe non conforme (champ vide ou « À REMPLIR », empreinte, brouillon relu différent, clé ou type) | bras méta « non produit (annexe non conforme) », A20 ; jamais un arrêt | § 8 |\n| étiquette interdite dans ce que le lecteur reçoit | arrêt A4, entrée à reconstruire | § 1, § 8, § 9 (étape 4) |\n| lecture hors format (niche hors grille, deux niches, structure hors liste, nom différent de l'identifiant) | lecture rejetée, comptée, jamais corrigée en silence (garde R5 ligne 23) | § 1 |\n| lecture de désaccord horodatée avant le dépôt des paires | arrêt (artefact d'ordre, `verifier_ordre_desaccord`) | § 4 |\n| fonction de score qui varie avec le désaccord | arrêt (garde R5 ligne 24, `garde_desaccord_v54`) | § 4 |\n| consigne figée sans l'un des quatre textes de `regles_lecteur_niches` | arrêt à É0 (contrôle I-15) | § 8, § 9 |\n| sous S28 (kappa < 0,40 ou Jaccard < 0,30) | bras marqué « niches non lisibles », gardé, nœud joint à la demande de GO | § 1 |\n| aucune paire de niches différentes parmi les fiches retenues | « non produit » avec sa cause, C12, O15 | § 1 |\n| deux lecteurs constants sur tout le lot | grille marquée « dégénérée sur ce lot », kappa lu 1 ou 0 | § 1 |\n| jeu d'essai vide ou plein sous le jeu de paramètres | A20 à É0 (`verifier_non_vacuite`) | § 6 |\n\n**Calcul et rejeu.** Script et sortie"),
    # CA5-07 : Bettencourt et Kaiser
    ("rapport de branchement (analogies seulement ; Bettencourt et Kaiser 2015, p. 3, **transcrit de la réponse 3 v2, à vérifier sur PDF empreinté avant tout chiffre opposable**, R7 ; CA3-11) ;",
     "rapport de branchement (analogies seulement ; **vérifié sur PDF empreinté au brouillon 6** : `docs/sources/pdf/bisociation-fertilite-v1/arxiv-1504.00319-bettencourt-kaiser-2015.pdf` `2fb9aab049631cdffe59631ce5196b800220dbeb584afd179ce8e6623485a523`, compagnon conforme, R7 ; CA3-11, CA5-07 : Bettencourt et Kaiser 2015 soutiennent la seule **composante connexe géante** (résumé : « developing a giant connected component containing most authors » ; p. 3 : « one giant connected cluster emerged ») ; les mots « cascade » et « branching » n'apparaissent pas dans le texte extrait du PDF : profondeur de cascade et rapport de branchement restent des grandeurs du journal sans source citée, non attribuées à cette référence ; aucun chiffre n'en est tiré) ;"),
    # CA5-01 : section 8
    ("et un artefact (« fusion » ajouté à une définition) est refusé ;",
     "et un artefact (« fusion » ajouté à une définition) est refusé — **collision relevée par la contre-lecture 5 (CA5-01), reproduite au brouillon 6 avec `fiches_v53.garde_etiquettes` du code v55** : la consigne de l'aiguilleur du même pré-pilote (`consigne-aiguilleur-v1.md` `c2efa120…`, l. 462) éprouve A4 avec une liste qui contient les étiquettes de classe `N1` à `N4` et `M6b` ; la normalisation (`outils.normaliser_texte`) coupe `n1_detection_sequentielle` en mots `n1 detection sequentielle`, et sur ce que le lecteur reçoit (identifiants, `definitions_niches`, `definitions_structures`, types) la garde trouve alors **N1, N2, N3, N4** (arrêt A4) et, sur les quatre règles à recopier, **N1, N2** ; une liste qui contiendrait `D1`, `D2`, `D3` arrêterait aussi sur les définitions des jeux de données. **Conséquence (à geler avec l'annexe, table 11)** : la liste A4 de la configuration servie au lecteur de niches et au lecteur de désaccord (`bisociateur.consigne_lecteur_etiquettes`, `bisociateur.meta.desaccord`) **ne contient ni `N1` à `N4`, ni `D1` à `D3`, ni aucun identifiant de la grille ou de la liste fermée** ; le détenteur de la configuration le confirme avant É0, et le contrôle de l'étape 4 (section 9) rejoue A4 avec la liste réellement gelée. Alternative (voie (i) de la contre-lecture 5) : renommer les niches sans chiffre isolable (`niche_sequentielle`, …) — avantage : plus aucune dépendance à une liste extérieure ; inconvénient : identifiants présents partout (tables, blocs, script, règles servies), nouveau script et relecture entière ; non fait au brouillon 6, mot de Lazar ;"),
    # Bloc N4
    ("brouillon 5 de l'annexe (`annexe-bras-meta-v1-brouillon5.md`), 1er novembre 2026, commencé par le premier rédacteur du brouillon 5 et achevé par le second (en-tête) ;",
     "brouillon 6 de l'annexe (`annexe-bras-meta-v1-brouillon6.md`), 1er novembre 2026, rédacteur neuf Fable 5.1 (en-tête), qui traite la contre-lecture 5 du brouillon 5 (section 16) ;"),
    ("sinon repli, compté « hors profil » (0,53 à 6 fiches, 0,17 à 10), réserve « seul le repli éprouvé » ; aucune paire éligible 0,028 et 0,001 ;",
     "trois issues qui font 1 (CA5-02) : repli, compté « hors profil », 0,50 à 6 fiches et 0,17 à 10 (= 1 − P(méta) − P(aucune paire éligible), arithmétique sur la sortie § 3, ± 0,01 ; le script n'imprime pas le repli), réserve « seul le repli éprouvé » ; bras non produit (aucune paire éligible) 0,028 et 0,001 ;"),
    (LIGNE_412_ANCIENNE, LIGNE_412_NOUVELLE % {"empreinte": SORTIE_B6["empreinte"], "lignes": SORTIE_B6["lignes"],
                                               "ecart_v5": SORTIE_B6["ecart_v5"], "bloc": "%(bloc)s", "hors": "%(hors)s"}),
    ("\n\n```json\n{\"parametres_bras_meta\": {",
     "\n- **Contre-lecture** (champ en clair ; le champ `contre_lecture` du JSON reste « À REMPLIR », voir section 16) : contre-lecture 5 du brouillon 5 (`c04ddf15…`) par un sous-agent neuf Sonnet 5.5, 1er novembre 2026, 16:13 UTC, `contre-lecture-annexe-bras-meta-v1-brouillon5.md` `156b9c557f9c5a692374db1f991a7e38846fa2e38214735178f5d5eae0911e2e` ; verdict « présentable après corrections », 0 bloquant, 1 majeur (CA5-01), 4 moyens (CA5-02 à CA5-05), 7 mineurs (CA5-06 à CA5-12) ; rejeu identique octet pour octet, recalculs indépendants concordants à moins de 0,01, citations d'Uzzi exactes, neuf constats de la contre-lecture 4 traités. Traitement au brouillon 6 : acceptés CA5-01 (voie (ii)), CA5-02, CA5-03, CA5-05, CA5-06, CA5-07, CA5-11 ; acceptés en partie CA5-04 (déplacement des pièces lues non fait), CA5-08, CA5-10, CA5-12 (leur part qui touche le script) ; hors mandat CA5-09 (erratum v2, gardé) ; refusé : aucun. **Ce brouillon 6 n'est pas le brouillon relu par la contre-lecture 5** : il attend sa propre contre-lecture (R2, section 9, étape 3) avant tout scellement.\n\n```json\n{\"parametres_bras_meta\": {"),
    # Section 9
    ("du brouillon 5 par un sous-agent neuf d'un modèle autre qu'Opus, qui n'a écrit aucune pièce lue ici.",
     "du brouillon 6 par un sous-agent neuf d'un modèle autre qu'Opus et que Fable (rédacteurs des brouillons 1 à 6), qui n'a écrit aucune pièce lue ici ; la contre-lecture 5 du brouillon 5 (`156b9c55…`, Sonnet 5.5) est faite et traitée en section 16."),
    ("contre-lecture du brouillon 5 est-elle entière", "contre-lecture du brouillon 6 est-elle entière"),
    ("plus de six minutes par jeu", "de trois à sept minutes par jeu selon la machine, CA5-12"),
    ("liste (écart du texte hors bloc N4 au brouillon 4, empreinte de l'écart donnée)",
     "liste (écart du texte hors bloc N4 au brouillon 4, chemin figé dans le script v5, empreinte de l'écart donnée) et la liste des substitutions de `appliquer-cl5-brouillon6-v1.py` (écart au brouillon 5)"),
    ("aucune relecture du brouillon 5 avant", "aucune relecture du brouillon 6 avant"),
    ("brouillon 5 et son empreinte ; le brouillon 4 ; la contre-lecture du brouillon 4",
     "brouillon 6 et son empreinte ; les brouillons 4 et 5 ; les contre-lectures des brouillons 4 et 5, le traitement de la contre-lecture 5 et le script de substitutions"),
    ("diffère de ce brouillon 5, une vérification courte", "diffère de ce brouillon 6, une vérification courte"),
    ("complète la contre-lecture du brouillon 5 et c'est", "complète la contre-lecture du brouillon 6 et c'est"),
    ("et par la garde A4 avec la liste d'étiquettes gelée ; empreintée (CA3-03).",
     "et par la garde A4 avec la liste d'étiquettes gelée, qui ne contient ni `N1` à `N4`, ni `D1` à `D3`, ni un identifiant de la grille (CA5-01, section 8) ; empreintée (CA3-03)."),
    # Section 10 : v56
    ("(inférence du rédacteur, non éprouvée par le script v5, qui n'importe que la v55).",
     "(inférence du rédacteur, non éprouvée par le script v5, qui n'importe que la v55). **Levée par la contre-lecture 5** : `forme_annexe_v56` rend True sur le brouillon 5 tel quel (archive v56 dépliée par elle dans un dossier neuf). Au brouillon 6, trois blocs sont inchangés et le bloc `parametres_bras_meta` ne change que par une chaîne de `definitions_niches` : même forme ; issue non rejouée par le rédacteur du brouillon 6."),
    # Table 11
    ("| chaque paire candidate (≤ 90 lectures) |",
     "| chaque paire candidate (≤ 90 lectures) — avantage : désaccord connu pour toute paire du classement ; inconvénient : coût et M9 à réécrire |"),
    ("ou si le monde synthétique est étendu aux niches et structures | — |",
     "ou si le monde synthétique est étendu aux niches et structures | — |\n| **Liste A4 du lecteur de niches (CA5-01)** | ne contient ni `N1` à `N4`, ni `D1` à `D3`, ni un identifiant de la grille ou de la liste fermée ; confirmée par le détenteur de la configuration avant É0 (section 8) | renommer les niches sans chiffre isolable (nouveau script, relecture entière) | 0,6 |\n| Lecture de l'issue observée (CA5-03) | libellé unique « chaîne éprouvée, profil non éprouvé » suivi de l'issue et des comptes ; aucune issue ne réfute P14 ; audits R4 par issue (section 6) | libellé et garde au préenregistrement brouillon 11 | 0,5 |\n| Mots-indices de n6 (CA5-05) | « transfert » et « famille tenue à l'écart » retirés (imposés par le texte I) ; « préenregistrement » gardé | les garder et chiffrer « l'axe 1 se range en partie en n6 » (script v6) | 0,5 |"),
    # Section 16
    ("\n\n*Fin. Ce texte ne gèle", "\n\n" + SECTION_16 + "*Fin. Ce texte ne gèle"),
]

MARQ_DEBUT = re.compile(r"<!-- BLOC N4 : DÉBUT.*?-->", re.S)
MARQ_FIN = "<!-- BLOC N4 : FIN -->"
BLOC = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)
CHAMPS_LIBRES = ("contre_lecture", "approbation_lazar")


def canon(o):
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main():
    with open(SRC, "rb") as f:
        brut = f.read()
    sha5 = hashlib.sha256(brut).hexdigest()
    assert sha5 == SHA5_ATTENDUE, f"brouillon 5 : empreinte {sha5}, attendue {SHA5_ATTENDUE}"
    texte = brut.decode("utf-8")
    for n, (ancien, nouveau) in enumerate(SUBSTITUTIONS, 1):
        c = texte.count(ancien)
        assert c == 1, f"substitution {n} : l'ancien texte apparaît {c} fois (attendu 1) : {ancien[:80]!r}"
        texte = texte.replace(ancien, nouveau)
    # Empreintes du brouillon 6, calculées comme le script v5 les calcule (elles ne dépendent pas de la prose du bloc N4).
    assert len(MARQ_DEBUT.findall(texte)) == 1 and texte.count(MARQ_FIN) == 1
    i_debut, i_fin = MARQ_DEBUT.search(texte).end(), texte.index(MARQ_FIN)
    hors = texte[:i_debut] + texte[i_fin:]
    assert "%(bloc)s" not in hors and "%(hors)s" not in hors
    blocs = [json.loads(m.group(1)) for m in BLOC.finditer(texte)]
    p = [b for b in blocs if "parametres_bras_meta" in b][-1]["parametres_bras_meta"]
    e_bloc = hashlib.sha256(canon({k: v for k, v in p.items() if k not in CHAMPS_LIBRES}).encode()).hexdigest()
    e_hors = hashlib.sha256(hors.encode("utf-8")).hexdigest()
    assert texte.count("%(bloc)s") == 1 and texte.count("%(hors)s") == 1
    texte = texte.replace("%(bloc)s", e_bloc).replace("%(hors)s", e_hors)
    for interdit in ("neuf structures", "A-VENIR", "«C12-", "⟦"):
        assert interdit not in texte, f"marqueur interdit par la garde du script v5 : {interdit!r}"
    assert texte.count('"contre_lecture": "À REMPLIR"') == 1 and texte.count('"approbation_lazar": "À REMPLIR"') == 1
    with open(DST, "w", encoding="utf-8", newline="") as f:
        f.write(texte)
    with open(DST, "rb") as f:
        sha6 = hashlib.sha256(f.read()).hexdigest()
    print(f"brouillon 5 {sha5}\nsubstitutions appliquées : {len(SUBSTITUTIONS)}\n"
          f"empreinte du bloc de paramètres (JSON canonique, sans les deux champs libres) : {e_bloc}\n"
          f"empreinte du texte hors bloc N4 : {e_hors}\nbrouillon 6 écrit : {DST}\n{sha6}  {DST}")


if __name__ == "__main__":
    main()
