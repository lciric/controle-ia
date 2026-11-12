# Vérification sur PDF de ce que la note d'antériorité P-041 (flux v2) attribue à Bailey et collègues, arXiv:2412.09565v2 — v1

31 octobre 2026. Lecteur neuf (Claude Opus 5.5, sous-agent), qui n'a écrit ni P-041 ni la note vérifiée. Aucune dépense, aucun appel payant, aucun commit. Rien de procédural sur la manière de déjouer un moniteur n'est reproduit ici : on reste aux affirmations, aux chiffres de résultat et à leur portée.

- **PDF lu** : `docs/sources/pdf/anteriorite-P-041-v2/c3/bailey-2025-obfuscated-activations-2412.09565.pdf`, empreinte `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9`, conforme à son compagnon `.sha256` (contrôlé). En-tête p. 1 : « arXiv:2412.09565v2 [cs.LG] 8 Feb 2025 », 51 pages. Les copies `c1/2412.09565v2.pdf` et `docs/sources/pdf/2412.09565v2.pdf` ont la même empreinte (contrôlé).
- **Note vérifiée** : `docs/notes/anteriorite-P-041-v1/note-anteriorite-P-041-workflow-v2.md`, empreinte `900db290bfc51dbf45678cd14f399a4e9e8dd5246f970aa4dbcf193552cfb089` (conforme à son compagnon).
- **Méthode** : `pdftotext -layout`, texte découpé par saut de page ; le numéro imprimé en pied de page coïncide avec le numéro de page du fichier pour les 51 pages. Les pages 12 (figure 8) et 45 (figure 20) ont en outre été relues sur l'image (`pdftoppm`, 80 points par pouce) ; tout chiffre lu sur une courbe est marqué « lu sur la figure ».

## Verdict

**Les attributions de la note à Bailey et collègues sont exactes sur les faits, à deux surévaluations près.** Toutes les citations et pages vérifiées tiennent (« over 70 epochs » p. 11 ; « do not easily lead to robust monitors » p. 13 ; rappel parfait sur les attaques passées p. 11 ; ensemble incrémental p. 42 ; coût en performance p. 23 ; durcissement du modèle sans moniteur robuste p. 25–26 ; échec à l'orthogonalité p. 26–27 ; aucune mention de certificat, de contrôle ni d'ICLR dans le PDF).

Les deux surévaluations :

1. **« Réfutée dans le cadre même de P-041 par Bailey (p. 13) »** (note, §1.1) est trop fort. Le cadre de Bailey n'est pas celui de P-041 : l'attaque y est un suffixe de plongement continu optimisé en boîte blanche à travers un vrai modèle (Llama-3-8B-Instruct), pas une famille de lois sur activations synthétiques ; la défense n'y connaît que des instances, jamais des paramètres de famille — ce que la note dit elle-même en (e). Et les auteurs bornent leur conclusion : « We can't rule out that this training process would eventually converge » (p. 13). Bailey **contraint** la prémisse d'avantage du terrain dans un cadre voisin ; il ne la réfute pas dans celui de P-041.
2. **« Le cœur technique de P-041 […] est publié »** (note, §1 en tête) vaut pour la **boucle** (alternance, archive des attaques passées, rappel à 1 % de fausses alertes), pas pour les traits que la note elle-même retient comme critères au sens fort (lois synthétiques à plages déclarées, défense informée des paramètres, pire cas sur une boîte).

Une nuance de plus, mineure : chez Bailey l'attaque n'opère pas « dans l'espace des activations » ni « par gradient sur les activations » ; elle opère sur l'entrée (plongements continus) et les activations sont induites ; seul le moniteur lit les activations. Et un « tournoi contre l'histoire » rudimentaire existe chez Bailey (figure 9, p. 13 : sonde finale évaluée contre les attaques de toutes les époques), ce qui nuance l'absence de « tournoi maître » en (d).

## Les quatre questions

### (1) Ce que mesure le réentraînement itéré de la défense, et son résultat

- **Question posée** : « How many different ways can a model represent harmfulness and what does this mean for adversarial training of probes? (§3.5) » (p. 6).
- **Protocole** : « in each epoch, the attacker trains an embedding attack to jailbreak the model and fool the current monitor, then the defender retrains a monitor against the obfuscated activations from the current and all previous attacks. We focus our attention to input based probes. » (p. 11).
- **Modèle surveillé** : Llama-3-8B-Instruct par défaut (« Unless stated otherwise, we use Llama-3-8B-Instruct as our model being monitored », p. 6–7 ; §3.5 ne dit pas autrement).
- **Moniteur** : sondes « à l'entrée », qui lisent l'activation du dernier jeton de l'invite (« Input-based monitors use only the activations on the final prompt token », p. 5) ; deux sondes retenues pour leur capacité : « the MLP probe, as well as a new probe that consists of an ensemble of mean difference probes » (p. 11). La sonde MLP a une couche cachée de taille 64 (p. 41). L'ensemble ajoute à chaque tour une direction « moyenne des activations bénignes contre moyenne des activations camouflées de la dernière attaque » et prend le maximum (« they simple take the max prediction from each probe », p. 42). Les couches agrégées en §3.5 ne sont pas précisées ; la figure 8c montre la couche 22 (p. 12).
- **Métrique** : rappel à 1 % de fausses alertes (« we use recall at a 1% false positive rate (FPR) », p. 6), calculé **sur la dernière attaque seulement** (« Recall is calculated on the most recent obfuscation attack », légende figure 8a, p. 12) ; plus le taux d'évasion du refus (« jailbreaking rate ») jugé par StrongREJECT (p. 6).
- **Nombre d'itérations** : sonde MLP « even after over 70 epochs » (p. 11), axe de la figure 8a jusqu'à environ 72 (lu sur la figure, p. 12) ; ensemble : axe de la figure 20 jusqu'à environ 91 (lu sur la figure, p. 45). Le texte dit aussi « the 70 epochs we train for » (p. 13), en léger désaccord avec la figure 20 : on retient « plus de 70 époques pour la sonde MLP, environ 90 pour l'ensemble ».
- **Résultat chiffré** :
  - sur l'archive : « the defender can always achieve perfect recall against all previous attack suffixes » (p. 11) ; figure 9 : « Both probes perform well against all previous attacks simultaneously » (p. 13) ;
  - sur la nouvelle attaque : « the attacker can still find a new suffix that fools the latest probe » (p. 11–13) ; « the final suffix still produces a score as low as that of benign data » (figure 9, p. 13). Sur la figure 8a, le rappel sur la dernière attaque oscille à chaque tour entre 100 % (après la défense) et 0 % (après l'attaque) jusqu'à la fin (lu sur la figure, p. 12 ; aucun chiffre dans le texte) ;
  - taux d'évasion du refus : « stays high for MLP » ; ensemble « seem to plateau at an average of around 50% » (p. 12) ; pour la MLP, environ 85 à 90 % lu sur la figure 8b ;
  - conclusion : « obfuscated activations are abundant in the latent space, and thus adversarial training techniques do not easily lead to robust monitors » ; réserve des auteurs : « running this process for much longer could mean that the attacker would "run out" of obfuscated activations, resulting in a robust probe » (p. 13) ; et « We can't rule out that this training process would eventually converge, but we do not see clear signs of any improvement for the defender » (p. 13).

### (2) Nature des « familles » : lois synthétiques ou entrées d'un vrai modèle ?

**Entrées d'un vrai modèle de langage, optimisées contre le moniteur courant ; aucune loi de probabilité synthétique.** L'attaque de §3.5 est un suffixe de plongement universel (« embedding suffixes (a matrix of values appended to the end of a token sequence embedding) », p. 7 ; « we optimize a single universal suffix against a set of inputs, and test it on held-out inputs », p. 7), optimisé avec accès boîte blanche (« we assume the attacker has white-box access to the model », p. 9), avec un objectif double, comportement et camouflage (équation 1, p. 5). Les activations camouflées sont **induites** à travers le réseau, pas tirées d'une loi. Il n'y a d'ailleurs pas de « familles » au sens de P-041 : une seule procédure d'attaque, relancée à chaque époque contre la sonde courante ; chaque époque produit une instance. Ni plages déclarées, ni paramètres de loi.

### (3) La défense connaît-elle les paramètres des familles ou seulement leurs instances ?

**Seulement les instances** : les activations induites par les attaques passées. MLP : « retrains a monitor against the obfuscated activations from the current and all previous attacks » (p. 11) ; ensemble : « calculate the mean difference between the set of benign activations and harmful obfuscated activations induced by the most recent attack embedding » (p. 42). Rien dans le texte ne donne au défenseur la procédure, l'objectif ou un paramètre de l'attaque. Réserve de lecture : c'est une absence dans la description du protocole, pas un contraste énoncé par les auteurs ; et il n'existe pas de paramètres de famille à connaître. Asymétrie à noter : l'attaquant joue en second et vise la sonde courante (« fool the current monitor », p. 11).

### (4) Ce qui distingue P-041 du dispositif de Bailey, et ce qui ne le distingue pas

Ne distingue pas (déjà publié chez Bailey) :
- alternance attaquant–défenseur où chacun s'adapte au dernier état de l'autre, moniteur boîte blanche sur activations réentraîné à chaque tour (p. 11) ;
- défense entraînée sur l'archive de toutes les attaques passées, y compris sous forme d'ensemble incrémental de sondes (p. 11, 42) ;
- métrique : rappel à 1 % de fausses alertes (p. 6, 12) ;
- attaquant informé du moniteur courant (p. 11) ;
- évaluation de la sonde finale contre toute l'histoire des attaques (figure 9, p. 13) ;
- résultat attendu possible : rappel parfait sur l'archive, nul sur l'attaque suivante, sans convergence visible au budget testé (p. 11–13).

Distingue (absent du PDF, ou différent) :
- **objet de l'attaque** : familles déclarées de lois sur activations synthétiques à plages déclarées, au lieu d'un suffixe de plongement optimisé à travers un vrai réseau (p. 7, 9). C'est la différence décisive, dans les deux sens : le mécanisme invoqué par Bailey pour son résultat négatif — la malléabilité d'un vrai réseau, « obfuscated activations are abundant in the latent space » (p. 13) — n'existe pas dans un espace de lois à paramètres bornés ; inversement, un résultat positif de P-041 sur lois synthétiques ne contredirait pas Bailey et ne dirait rien, seul, des vrais modèles ;
- **information de la défense** : paramètres de famille plutôt qu'instances (voir (3)) ;
- **critère** : pire cas sur toute une boîte de paramètres, avec certificat, au lieu d'un rappel empirique sur la dernière attaque (aucune occurrence de « certif » dans le PDF) ;
- **cadre** : contrôle (agent non fiable, budget d'audit) au lieu de défenses contre l'évasion du refus et les portes dérobées (aucune occurrence de « audit », « untrusted », « AI control ») ;
- **dynamique** : générations avec héritage, population, diagnostics de cyclage, au lieu d'une procédure unique relancée ;
- **évaluation** : familles tenues à l'écart conçues par des tiers de plusieurs fournisseurs, lues une fois (absent : Bailey teste la transposition entre sondes et sur entrées tenues à l'écart, p. 7, pas sur des familles de tiers) ;
- **mesure de la boucle** (juge figé, témoins plantés, fausses promotions) : absente.

## Tableau des affirmations de la note

Lignes de la note citées par numéro (fichier d'empreinte `900db290…`).

| Ligne | Affirmation de la note | Page et phrase du PDF | Sort |
|---|---|---|---|
| 32 | Le cœur technique de P-041 (défense réentraînée contre les attaques passées, dans les activations, rappel à 1 % de fausses alertes) est publié avec un résultat négatif, §3.5 p. 11–13 | p. 11 « the defender retrains a monitor against the obfuscated activations from the current and all previous attacks » ; p. 12 axe « Recall at 1% FPR » | **nuancée** : vrai pour la boucle, pas pour les traits forts de P-041 (lois synthétiques, paramètres connus, pire cas sur boîte) |
| 32, 454 | Citation p. 13 « adversarial training techniques do not easily lead to robust monitors » | p. 13, mot pour mot | **confirmée** |
| 34 | Le résultat négatif de Bailey décourage d'y investir | p. 13 (même phrase) ; mais aussi p. 13 « could mean that the attacker would "run out" » | **nuancée** : jugement du rédacteur ; les auteurs laissent la convergence ouverte |
| 44 | Prémisse d'avantage du terrain « réfutée dans le cadre même de P-041 par Bailey (p. 13) » | p. 13 « We can't rule out that this training process would eventually converge » ; p. 7, 9 (attaque sur plongements d'un vrai modèle) ; p. 11, 42 (défense sur instances) | **nuancée, surévaluée** : cadre voisin, pas celui de P-041 ; « contrainte » et non « réfutée » |
| 52 | 1+2 : la défense connaît les instances passées, pas les paramètres (p. 11–13, 42) | p. 11 et p. 42 (citations en (3)) | **confirmée** (au sens faible de la composante 2 : entraînement adverse) ; aucun paramètre n'existe à connaître |
| 53, 83 | 1+3 et 1+2+3 : §3.5–3.6 p. 11–14, plus de 70 époques, résultat négatif | p. 11 « even after over 70 epochs » ; p. 14 « Even when a monitor is adversarially trained against previous attacks, an attacker can find new obfuscated activations » | **confirmée** ; préciser : plus de 70 époques pour la MLP, environ 90 pour l'ensemble (figure 20, p. 45, lu sur la figure) ; « the 70 epochs we train for » (p. 13) |
| 65, 84 | 3+4 et 1+2+3+4 : archive en ensemble de sondes (p. 42), composante 4 rudimentaire | p. 42 « add it to the running ensemble » ; p. 11 « the probes need to have enough capacity to guard against all previous attacks » | **nuancée** : l'archive existe, mais motivée par la capacité de la sonde, pas comme remède à une pathologie de coévolution ; aucun diagnostic de cyclage ou d'oubli |
| 102 | Chez Bailey l'attaquant procède par gradient ; pas de générateur modèle de langage | p. 9 « we assume the attacker has white-box access to the model » ; aucun proposeur de langage dans §3.5 (PAIR et GPT-4 n'apparaissent que comme jeu de données d'évasions standard, p. 42) | **confirmée** ; préciser : gradient sur les plongements d'entrée, pas sur les activations |
| 103, 116 (c) | Contournement, pas contrôle ; cadre du contrôle absent | p. 1 « Recent latent-space monitoring techniques have shown promise as defenses against LLM attacks » ; aucune occurrence de « audit », « untrusted », « AI control » | **confirmée** (par recherche plein texte) |
| 112 | Auteurs, titre, arXiv:2412.09565v2, empreinte, même fichier en trois copies ; venue ICLR 2026 non lue sur le PDF | p. 1 (auteurs, « arXiv:2412.09565v2 [cs.LG] 8 Feb 2025 ») ; aucune occurrence de « ICLR » | **confirmée** (empreintes recalculées) |
| 114 | Boucle attaquant contre moniteur dans l'espace des activations | p. 11 ; p. 5 « Input-based monitors use only the activations on the final prompt token » ; p. 7 « embedding suffixes » | **nuancée** : le moniteur lit les activations ; l'attaque agit sur l'entrée |
| 114 | Défense réentraînée contre l'archive de toutes les attaques passées, y compris ensemble incrémental | p. 11 ; p. 42 | **confirmée** |
| 114 | Métrique de P-041 : rappel à 1 % de fausses alertes | p. 6 « we use recall at a 1% false positive rate (FPR) » ; p. 12 « Recall is calculated on the most recent obfuscation attack » | **confirmée** pour l'unité ; **nuancée** pour l'agrégation (dernière attaque, pas pire cas sur une boîte) |
| 114 | Rappel parfait sur toutes les attaques passées ; après plus de 70 époques l'attaquant trouve encore une activation camouflée (p. 11–13) | p. 11 « the defender can always achieve perfect recall against all previous attack suffixes » ; p. 11–13 « even after over 70 epochs, the attacker can still find a new suffix that fools the latest probe » | **confirmée** |
| 114 | Durcissement du modèle sans moniteur robuste (p. 25–26) | p. 26 « OAT significantly increases the computational cost of finding a successful attack, but does not ultimately result in a robust monitor » ; chiffres p. 26 : 35 % d'évasion et rappel nul à 1 % de fausses alertes après 16 384 pas contre 95 % et 256 pas sans durcissement | **confirmée** |
| 114 | Coût en performance sur tâche difficile (p. 23) | p. 23 « There is a trade-off between obfuscation and model performance » ; 34,8 % de requêtes SQL correctes sans camouflage (figure 15) | **confirmée** (modèle Gemma-2-2b, p. 23 et 48) |
| 114 | Échec à l'orthogonalité (p. 26–27) | p. 26 « We are unable to achieve near-orthogonality while preserving behavior » ; « this is a tentative negative result » | **confirmée** (résultat déclaré provisoire par les auteurs) |
| 114 | Les auteurs notent qu'une boucle bien plus longue pourrait épuiser les régions disponibles (p. 13) | p. 13 « running this process for much longer could mean that the attacker would "run out" of obfuscated activations, resulting in a robust probe » | **confirmée** |
| 116 (a) | Familles au niveau des lois sur activations synthétiques, au lieu d'« attaques par gradient sur les activations d'un vrai modèle » | p. 7, 9 | **nuancée** : la différence tient, mais l'attaque de Bailey porte sur les plongements d'entrée, pas sur les activations |
| 116 (b) | Certificat absent chez Bailey | aucune occurrence de « certif » | **confirmée** (par recherche plein texte) |
| 116 (d) | Générations avec héritage, diagnostics de cyclage, tournoi maître absents ; archive rudimentaire | p. 13, figure 9 « the final probe […] against attack suffixes from all epochs » | **nuancée** : générations et diagnostics absents ; mais une évaluation finale contre toute l'histoire existe (une fois, sans rôle de sélection) |
| 116 (e) | Défense informée des paramètres et non des seules instances | p. 11, 42 | **confirmée** |
| 116 (f), (g) | Familles de tiers lues une fois ; mesure de la boucle : absentes | §3.5 entier (p. 11–14) ; p. 7 (entrées tenues à l'écart seulement) | **confirmée** |
| 442 | Bailey réunit 1+2+3 si l'on admet la composante 2 au sens faible (instances, pas paramètres) | p. 11, 42 | **confirmée** |
| 473 | Bailey, Casper, Sheshadri appartiennent à un même réseau d'auteurs | p. 1 : Casper et Sheshadri sont coauteurs de Bailey | **confirmée** pour ces deux noms ; le reste du réseau (Che, Neural Chameleons, RL-Obfuscation) n'est pas vérifiable sur ce PDF |

Aucune affirmation **contredite** ; aucune **non trouvée**.

## Réserves

- Les chiffres lus sur figure (oscillation 100 % / 0 %, environ 72 et 91 époques, environ 85 à 90 % d'évasion pour la MLP) sont des lectures d'image à basse résolution, pas des chiffres du texte ; ils ne sont pas opposables en l'état (R7).
- Le lecteur est de la même famille de modèle que le rédacteur de la note et que les lecteurs c1 à c8 ; sa concordance ne vaut pas confirmation indépendante (R2).
- Le désaccord interne du PDF (« over 70 epochs », p. 11 ; « the 70 epochs we train for », p. 13 ; axe jusqu'à environ 90 pour l'ensemble, p. 45) est signalé, non résolu.

## Correction proposée à la note (pour une v3, la v2 restant intacte, R12)

- §1.1 : remplacer « réfutée dans le cadre même de P-041 par Bailey (p. 13) » par « contrainte, dans un cadre voisin (attaque sur les plongements d'entrée d'un vrai modèle, défense informée des seules instances), par Bailey (p. 13), qui laisse la convergence ouverte ».
- §1 en tête et §2 : écrire « la boucle de P-041 » plutôt que « le cœur technique de P-041 » ; « attaques par gradient sur les plongements d'entrée d'un vrai modèle » plutôt que « sur les activations ».
- §2 (d) : mentionner l'évaluation finale contre toutes les époques (figure 9, p. 13).
- Ajouter en §2 la portée dans les deux sens : un résultat positif de P-041 sur lois synthétiques ne contredirait pas Bailey et ne transposerait pas seul aux vrais modèles.
