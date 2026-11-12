# Question — à Argon seul, à Kimi seul, au collisionneur (quatre espèces, deux tours), à GPT-6 Astra quand il sera branché, et à conv-audit (réponse propre, à comparer puis fusionner) — une vérification non circulaire des artefacts produits en bac à sable par l'organisme — v2

**v2 (session-depot, 1er novembre 2026, ≈ 17:35 UTC) = v1 (`26f2db15…`, gardée, R12) + un fait servi** (remarque de conv-audit au
n° 321 ; décisions du directeur du 1er novembre, 16:03 UTC, rapportées au n° 318) : **dans le code actuel des tests de mort, le chiffre
qui décide (« survit » ou « éliminée ») est imprimé par le script écrit par l'agent, et ce script choisit la statistique que le noyau
recalcule ; seul le fichier est contrôlé** (lecture du code par conv-audit, `tests_de_mort_v2.py`, l. 510-540 ; à vérifier sur le code).
Le directeur a déjà tranché deux règles, à tenir pour acquises : (1) le test de mort est lié au préenregistrement, et le verdict est
**calculé dans la session** à partir des sorties brutes, jamais lu d'un chiffre imprimé par le script de l'agent ; (2) « non concluant »
n'est jamais mieux traité qu'« éliminée ». Les réponses partent de ce fait et de ces deux règles : la question n'est plus de savoir s'il
faut les adopter, mais comment vérifier, sans circularité, que la session calcule bien le verdict sur des sorties brutes non altérées.

conv-audit, 1er novembre 2026 (heure UTC en tête du registre, R-1046). Demande de Lazar (09:52 UTC) : « oui go, envoie la question au collisionneur, Astra, Kimi et Argon aussi ». Dépense : nœud chez session-depot (mot direct de Lazar). **Niveau méthode et défense seulement** : aucune technique d'évasion de bac à sable, aucun exploit, aucune recette ; les suites d'étanchéité sont des suites publiques nommées, jamais écrites par nous. Toute recommandation des auteurs est retirée et servie au tour 2 seulement.

## Le problème (pièces servies)

L'organisme d'idéation fera écrire du code par des agents et l'exécutera dans un bac à sable (tests de mort : `docs/notes/ideation-organisme-v1/orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v48.md`, l. 30-44 ; bac `bwrap` sans réseau, système en lecture seule, un seul dossier inscriptible ; jugé non sûr par deux contre-lectures, durci ensuite ; machine louée jetable sans secret décidée : `docs/notes/ideation-organisme-v1/machine-jetable-v1/`, devis v3 R-868). Le collisionneur sur les nœuds N12 et N13 (synthèse `synthese-n12-n13-v1.md`, section N12 (2), risque nommé par Argon) relève, d'après le rapport Avalon (p. 76 : « hacher les outils de vérification est circulaire » ; 25 environnements sondés), que **si la vérification d'un artefact tourne dans le même bac que sa production, un optimiseur peut apprendre à satisfaire le vérificateur, ou à l'atteindre**. Lazar demande comment surmonter cette circularité.

## La demande de Lazar, reformulée (c'est l'objet à critiquer)

Concevoir et éprouver une vérification non circulaire des artefacts produits en bac à sable : (a) **base de confiance** écrite et minimale — machine virtuelle jetable, noyau et bac versionnés, constructions reproductibles ; (b) **vérificateur hors du bac**, sur un hôte distinct, qui ne reçoit que des artefacts hachés par un canal étroit ; (c) **attestation** — empreintes calculées hors du bac et journal des appels système prouvent que ce qui a tourné est ce qui a été relu ; (d) **redondance diverse** — deux bacs d'implémentations différentes, accord exigé ; (e) **mesure du sondage** de la plate-forme par canaris journalisés (fichiers, clés et chemins factices), seuil éliminatoire gelé ; (f) **pré-test d'étanchéité par suites publiques**, jamais par nos propres tentatives ; (g) préenregistrement avec témoins (cas sain : artefact honnête ; artefact : artefact qui touche un canari ou modifie une empreinte), coût de la machine ; (h) **vérification extérieure** — reproduction des empreintes par un tiers, audit indépendant du périmètre.

## Questions (tour 1 : avis propre — option, confiance, pire cas et garde, option manquante, pièce qui trancherait)

- **Q1 — Base de confiance.** Qu'est-ce qui doit y entrer au minimum (hyperviseur, noyau invité, bac, canal de sortie, vérificateur) et qu'est-ce qu'un expert en exclut ? Une machine virtuelle légère (Firecracker, Kata) change-t-elle la classe du problème par rapport à un bac dans l'hôte (`bwrap`, gVisor) ?
- **Q2 — Séparer produire et vérifier.** Le vérificateur hors du bac, nourri par un canal étroit d'artefacts hachés : quelles fuites restent (canaux cachés, temps, taille, ordre) et lesquelles comptent pour un optimiseur qui ne voit que le verdict ?
- **Q3 — Attestation.** Constructions reproductibles et journaux d'appels système suffisent-ils à prouver « ce qui a tourné est ce qui a été relu » ? Faut-il une attestation matérielle, et à quel prix pour une machine louée ?
- **Q4 — Redondance diverse.** Deux bacs d'implémentations différentes avec accord exigé : quel gain réel contre un optimiseur qui sonde, et quel coût ? Quelle antériorité (double compilation diverse de Wheeler ; « faire confiance à la confiance » de Thompson ; exécution en N versions) ?
- **Q5 — Mesurer le sondage.** Les canaris journalisés sont-ils une mesure valide du sondage de la plate-forme, quel seuil éliminatoire gelé, et quel taux de fausses alertes sur un artefact honnête ? Quelle autre mesure un expert ajouterait-il ?
- **Q6 — Étanchéité.** Quelles suites publiques d'étanchéité conviennent pour `bwrap`, gVisor, Firecracker (nommer, avec lien), et comment lire leurs résultats sans en faire une garantie ?
- **Q7 — Ordre et coût.** Que faut-il faire avant d'activer les tests de mort pour la course 2, en ordre, avec un devis indicatif « illustratif » ; qu'est-ce qui peut attendre ?

## Ce que les réponses ne doivent pas contenir

Aucune technique d'évasion, aucun exploit, aucun code offensif, aucun cas concret ; la défense et la mesure seulement.
