# Proposition B — Quel expérimentateur brancher d'abord

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut réel | Commentaire |
|---|---|---|---|
| 1 | Kaimen `cef5bcf` passe le relais Kimi v3 tel quel (appels sans flux, appel de fonctions forcé par nom) | HYPOTHÈSE — la note dit explicitement « non éprouvé : le choix d'outil forcé par nom sur `kimi-k3.1-pro` » (§ 7) | Aucun test n'a été exécuté ; une incompatibilité ici annule tout l'avantage du « relais sans changement ». |
| 2 | Un outil neuf « expérience » branché sur l'exécuteur `bwrap` existant est techniquement réalisable sans modifier le noyau de l'organisme | HYPOTHÈSE — la note décrit un branchement « moyen » mais ne cite aucun prototype ni preuve de faisabilité | Le pont prise Unix ↔ relais local à travers l'isolement réseau est un élément neuf, non trivial. |
| 3 | The Agentic Scientist peut fonctionner enfermé (sans réseau, sans Web, sans Docker réseau `host`) | HYPOTHÈSE — la note dit « branchement jugé lourd », agents à pleins droits, réseau `host` par défaut ; aucune vérification que ces agents fonctionnent sans réseau | Les agents `pi`/`opencode` peuvent échouer silencieusement ou bruyamment dès qu'ils ne résolvent pas d'hôte. |
| 4 | Les agents `pi`, `opencode`, `gemini` lisent en flux | RAPPORTÉ par la note, « non vérifié » (§ 7) — le relais v3 refuse le flux | Si c'est vrai, il faut un relais neuf ; si c'est faux, ce n'est plus un obstacle à (b). Ni l'un ni l'autre n'est établi. |
| 5 | Le témoin « Kimi, meilleur de N » est un comparateur bien défini | HYPOTHÈSE — la note ne spécifie pas la règle mécanique par laquelle le témoin sélectionne ses fiches parmi N tirages, ni comment N est calibré au coût du bras expérimental | Sans règle fixée et préenregistrée, le témoin est sous-spécifié et le test n'est pas réplicable. |
| 6 | L'oracle du monde planté suffit à départager les bras | RAPPORTÉ (N-058) mais suppose que le monde planté présente une difficulté suffisante pour qu'un scientifique puisse faire mieux qu'un proposeur chanceux | Si le monde planté est trop simple, le témoin gagne toujours ; s'il est trop dur, aucun bras ne marque. La difficulté de la course v66 n'est pas encore connue (verdict non rendu). |
| 7 | La comparaison à coût égal est possible | HYPOTHÈSE — le point ouvert de méthode (§ 4) reconnaît que les bras ne soumettent pas le même nombre de fiches ; deux métriques non équivalentes sont proposées sans trancher | La question présuppose « à coût égal » mais ne dit pas quelle des deux règles de multiplicité est retenue. |
| 8 | Co-Scientist sans littérature reste informatif sur Co-Scientist | RAPPORTÉ comme risque par la note : « privé de littérature, ce n'est plus Co-Scientist ; le bras mesurerait 'Co-Scientist sans littérature, avec expériences' » | La fidélité au candidat est compromise ; le résultat ne peut être attribué à l'architecture Co-Scientist elle-même. |
| 9 | Le coût d'un scientifique est de 7 à 500× celui d'un proposeur | ESTIMÉ (§ 4) — « aucune mesure » | Le facteur est très large (≈ 2 ordres de grandeur) ; le devis N-045 repose sur un chiffre qui peut être n'importe où dans cette fourchette. |

---

## (b) Expériences décisives, chacune en duel H_A / H_B

### Expérience 1 — Compatibilité du relais : Kaimen passe-t-il le relais v3 Kimi ?

- **H_A** : L'appel de fonctions forcé par nom et les appels sans flux de Kaimen `cef5bcf` sont correctement traités par le relais Kimi v3 avec `kimi-k3.1-pro` ; une boucle complète (superviseur → outil « expérience » → réponse structurée) aboutit.
- **H_B** : Le relais refuse ou le modèle ne retourne pas l'appel de fonction demandé ; la boucle échoue avant de produire une fiche valide.
- **Métrique** : taux de boucles complètes sur 10 appels indépendants (illustratif : seuil ≥ 8/10 pour déclarer compatible).
- **Contrôle négatif** : même boucle avec un modèle intentionnellement incompatible (par ex. modèle sans appel de fonctions), qui doit échouer 10/10.
- **Falsification** : H_A est falsifiée si < 8/10 ; H_B est falsifiée si ≥ 8/10. Coût : négligeable (quelques appels Kimi, < 0,10 USD illustratif).
- **Conséquence** : si H_B tient, l'option (a) exige une adaptation du relais ou du client, annulant son avantage principal. Le poids relatif de (a) vs (b) change.

### Expérience 2 — Enfermement de The Agentic Scientist : fonctionne-t-il sans réseau ?

- **H_A** : L'agent `pi` (ou `opencode`) sur Kimi, lancé dans un conteneur Docker sans route réseau sortante sauf le pont vers le relais local, termine sa phase d'investigation et produit au moins une fiche convertible au gabarit `{enonce, loi_predictive}`.
- **H_B** : L'agent échoue (erreur réseau, blocage, sortie vide, ou tentative d'accès Web non interceptée) avant de produire une fiche.
- **Métrique** : nombre de fiches valides produites / nombre de tentatives, sur 5 essais (illustratif : seuil ≥ 3/5).
- **Contrôle négatif** : même agent, même tâche, pont vers le relais *coupé* — doit échouer 5/5 (preuve que le test d'isolement mord réellement).
- **Falsification** : H_A falsifiée si < 3/5 ; H_B falsifiée si ≥ 3/5.
- **Conséquence** : si H_B tient, (b) est hors de portée sans réécriture profonde ; l'option « passer à (b) si (a) bat le témoin » perd son sens parce que (b) n'existe pas encore.

### Expérience 3 — Pilote A/A : la métrique est-elle stable ?

- **H_A** : Deux runs identiques du même bras (par ex. Kimi proposeur seul, mêmes mondes, même graine fixée pour l'orchestrateur) produisent des scores oracle (vraies et fausses découvertes par dollar) dont la différence absolue est inférieure à un seuil préenregistré δ.
- **H_B** : La variance inter-runs est ≥ δ ; la métrique ne stabilise pas sur un seul monde planté et le test A/B subséquent n'a pas de puissance.
- **Métrique** : |score_run1 − score_run2| ; δ fixé avant le run (par ex. illustratif : 20 % du score moyen).
- **Contrôle négatif** : deux bras *intentionnellement différents* (un proposeur et un proposeur avec consigne dégradée) doivent différer de plus de δ, sinon la métrique ne discrimine rien.
- **Falsification** : H_A falsifiée si différence ≥ δ ; H_B falsifiée si différence < δ et le contrôle négatif différencie bien.
- **Conséquence** : si H_B tient, aucun test de (a) vs témoin n'est interprétable ; il faut plus de mondes ou plus de runs, donc un budget plus élevé. L'expérience 3 **précède** obligatoirement les expériences 4 et 5 (conformément à N-045 : pilote A/A d'abord).

### Expérience 4 — Kaimen scientifique vs témoin « meilleur de N »

- **H_A** : Sur les mondes plantés préenregistrés, le bras Kaimen-scientifique produit un taux de vraies découvertes (lois promues dont l'oracle confirme la vérité) par dollar strictement supérieur au témoin « Kimi, meilleur de N à coût apparié », à un niveau préenregistré (illustratif : valeur p < 0,05 unilatérale, ou valeur e > 20, selon la méthode du juge statistique O2).
- **H_B** : Le témoin fait aussi bien ou mieux ; le scientifique ne justifie pas son surcoût.
- **Métrique** : (vraies découvertes − α × fausses promotions) / coût_USD, où α est préenregistré (pénalité pour faux positifs).
- **Contrôle négatif** : inclus via le pilote A/A (exp. 3). De plus, le bras « Kimi proposeur seul sans surcoût » sert de borne inférieure.
- **Falsification** : H_A falsifiée si la métrique du scientifique ≤ celle du témoin (ou si la différence n'atteint pas le seuil) ; H_B falsifiée si le scientifique dépasse le seuil.
- **Conséquence** : si H_B tient, on ne passe **pas** à (b) — on reste au proposeur simple. Le directeur a alors la réponse à « pourquoi pas lui ? » : parce qu'un proposeur chanceux fait aussi bien pour moins cher.

### Expérience 5 — Fausses découvertes du scientifique vs témoin

- **H_A** : Le scientifique ne produit pas un taux de fausses promotions (lois promues dont l'oracle dit qu'elles sont fausses) significativement supérieur au témoin.
- **H_B** : Le scientifique amplifie les fausses promotions (Goodhart via la boucle expérimentale : il optimise ce que le juge accepte, pas ce qui est vrai).
- **Métrique** : taux de fausses promotions = fausses promotions / total de promotions, comparé entre bras.
- **Contrôle négatif** : bras « proposeur dégradé » (consigne volontairement biaisée) qui doit produire un taux de fausses promotions élevé.
- **Falsification** : H_A falsifiée si le taux du scientifique est significativement supérieur ; H_B falsifiée si pas de différence significative.
- **Conséquence** : si H_B tient, le scientifique est non seulement inutile (exp. 4) mais activement nuisible. On ne branche aucun scientifique.

---

## (c) Mesure minimale de chaque instrument nommé

### Instrument 1 — Relais Kimi v3 (barrière modèle)

- **Fonction** : ne laisser passer que `kimi-k3.1-pro`, bloquer tout autre modèle.
- **Taux de détection minimal** : 100 % de blocage sur 5 requêtes portant un modèle interdit (Claude, GPT-4, etc.).
- **Taux de fausses alertes maximal** : 0 % sur 10 requêtes portant `kimi-k3.1-pro` (aucun blocage indu).
- **Cas honnêtes appariés** : 10 requêtes légitimes (modèle correct, format correct) et 5 requêtes forgées (modèle incorrect mais format correct).
- **Vérification mécanique à battre** : `grep` sur le champ `model` du JSON de la requête. Le relais doit être au moins aussi strict que ce `grep`.

### Instrument 2 — Exécuteur isolé `bwrap`

- **Fonction** : exécuter le code du scientifique sans accès réseau, sans accès aux fichiers de l'orchestrateur hors de la vue servie.
- **Taux de détection** : le code `curl http://example.com` doit échouer 10/10 ; le code `cat /chemin/vers/oracle` doit échouer 10/10.
- **Taux de fausses alertes** : un script légitime (lire un fichier de la vue, écrire un résultat, terminer) doit aboutir 10/10.
- **Vérification mécanique à battre** : un `strace` filtré sur les appels `connect()` et `open()` hors du répertoire autorisé. L'exécuteur doit bloquer tout ce que le `strace` détecte.

### Instrument 3 — Pont prise Unix ↔ relais local (élément neuf)

- **Fonction** : permettre au code dans `bwrap` d'atteindre le relais Kimi via une prise Unix, sans route réseau.
- **Taux de détection** : une requête API vers le relais depuis l'intérieur du bac doit aboutir 10/10 quand la prise est montée.
- **Taux de fausses alertes** : une requête vers toute autre destination (IP, nom d'hôte) doit échouer 10/10.
- **Vérification mécanique** : `ss -xlp` dans le bac ne doit lister que la prise du pont ; `ip route` vide.

### Instrument 4 — Garde « loi plantée dans les journaux »

- **Fonction** : détecter si le scientifique a eu accès à la loi plantée.
- **Taux de détection** : un journal forgé contenant la loi plantée en clair doit être détecté 10/10 (détection par correspondance exacte de la chaîne).
- **Taux de fausses alertes** : 10 journaux d'un run honnête (sans fuite) doivent passer 10/10.
- **Vérification mécanique à battre** : `grep -F "$LOI_PLANTEE"` sur les fichiers du bac. La garde doit couvrir au moins ce que le `grep` trouve (et idéalement les paraphrases, mais c'est un second temps — le `grep` strict est le plancher).

### Instrument 5 — Témoin « Kimi, meilleur de N »

- **Fonction** : servir de comparateur calibré.
- **Mesure minimale** : sur un monde planté de difficulté connue, vérifier que le score du témoin croît avec N de manière monotone (sinon la règle de sélection mécanique est défectueuse) et sature (sinon le coût apparié n'a pas de sens). Courbe score(N) sur N ∈ {1, 5, 10, 20, 50} (illustratif), 3 réplications par point.
- **Vérification mécanique** : le témoin avec N=1 doit donner le même score que le proposeur seul (sinon la règle mécanique altère le signal).

---

## (d) Ancrage matériel

### Modèles

- **`kimi-k3.1-pro`** : seul modèle autorisé (contrainte vérifiée du texte scellé v66). Aucun modèle Claude, aucun modèle OpenAI.
- Pas de modèle ouvert local requis pour les expériences 1-5 ; tout passe par le relais existant. Si le relais v3 échoue (exp. 1, H_B), un relais neuf serait nécessaire — coût de développement non estimé ici.

### Calcul

- **Machine** : l'exécuteur `bwrap` et le conteneur Docker (pour les tests de The Agentic Scientist) tournent sur la machine de l'orchestrateur. Pas de GPU requis (inférence distante via Kimi API). Machine minimale : un poste Linux avec `bwrap`, Docker, ≈ 4 Go RAM (illustratif).
- **Réseau** : sortant uniquement vers l'API Kimi (via le relais). Aucun autre accès.

### Coûts (tous illustratifs, fondés sur les estimations § 4 des faits)

| Étape | Appels API estimés | Coût illustratif |
|---|---|---|
| Exp. 1 — compatibilité relais | ~10 appels Kimi | < 0,10 USD |
| Exp. 2 — enfermement Agentic Scientist | ~5 runs investigation | ~1–5 USD |
| Exp. 3 — pilote A/A (2 runs × 1 monde) | 2 courses complètes | ~3–4 USD |
| Exp. 4 — Kaimen vs témoin (3 mondes × 2 bras) | 6 courses | ~10–30 USD |
| Exp. 5 — fausses découvertes | même donnée qu'exp. 4 | 0 (même runs) |
| **Total illustratif** | | **~14–39 USD** |

Le budget « go collisionneur ≤ 15 USD » (R-2380) couvre les expériences 1-3 ; les expériences 4-5 dépassent ce budget et nécessitent un GO de dépense séparé (conformément aux règles). Je note que les expériences 1-3 sont précisément celles qui conditionnent la faisabilité de 4-5 ; les faire d'abord est cohérent avec N-045.

---

## Réponse à la question du directeur

### Choix : (a) Kaimen d'abord, **mais seulement après avoir vérifié les prérequis techniques** (exp. 1, 2, 3)

**Raisons :**

1. **Le bon marché d'abord (N-045)** : Kaimen sur le relais v3 existant est le bras le moins cher à tester. The Agentic Scientist exige un relais neuf (si le flux est confirmé), un conteneur durci, un pont réseau — chacun de ces éléments est un risque d'ingénierie et un coût non estimé. Tester (a) d'abord consomme moins de budget irréversible.

2. **Surface d'attaque** : The Agentic Scientist exécute des agents à pleins droits. Même enfermé, le risque résiduel est supérieur (clés lisibles, modification du protocole — incident rapporté par les auteurs eux-mêmes). Kaimen n'exécute rien hors de l'outil « expérience » acheminé vers `bwrap`. La contrainte « aucun Web » est plus facile à garantir quand le candidat n'a pas d'agents de code autonomes.

3. **Falsifiabilité propre** : le plan séquentiel (a) puis éventuellement (b) falsifie quelque chose à chaque étape. Si (a) ne bat pas le témoin, on sait que l'architecture « tournoi + outil d'expérience » ne vaut pas ses jetons sur ce monde planté. Si (a) bat le témoin, on sait que l'exécution d'expériences ajoute de la valeur, et on peut alors justifier le surcoût d'enfermement de (b). Si on commence par (b), un échec ne distingue pas « l'exécution d'expériences est inutile » de « l'enfermement a cassé l'agent ».

4. **Fidélité dégradée, mais mesurable** : oui, Co-Scientist sans littérature n'est plus Co-Scientist. Mais le bras ne prétend pas mesurer Co-Scientist — il mesure « un proposeur structuré avec outil d'expérience isolé ». C'est le bon bras pour la question posée (le rôle d'expérimentateur aide-t-il ?), pas pour une revue de l'architecture Co-Scientist.

### Risques :

- **Exp. 1 échoue** (relais incompatible) : le plan (a) est bloqué. On doit soit adapter le client Kaimen (coût non estimé), soit tester directement (b) — ce qui change l'ordre et le budget.
- **Exp. 3 échoue** (variance trop haute) : aucun test n'est interprétable avec un seul monde planté. Il faut plus de mondes (et le verdict de v66 peut informer sur la difficulté disponible).
- **Règle de multiplicité non tranchée** : si le scientifique soumet 3 fiches et le témoin en a 30 à coût égal, la comparaison est dominée par la multiplicité, pas par la qualité. La règle doit être fixée *dans le préenregistrement*, avant le run.

### Ce qui ferait changer d'avis :

1. Si l'exp. 1 montre que Kaimen ne passe pas le relais v3, et qu'un correctif coûte plus cher que le relais neuf pour The Agentic Scientist → inverser l'ordre.
2. Si le verdict de la course v66 montre que les mondes plantés sont si simples que le proposeur seul les résout → aucun scientifique n'est utile ; la question est prématurée.
3. Si quelqu'un vérifie que les agents de The Agentic Scientist fonctionnent *sans flux* et *sans réseau* (contrairement à l'hypothèse actuelle) → l'obstacle technique de (b) disparaît et la comparaison (a) vs (b) peut se faire en parallèle plutôt qu'en séquence.
4. Si le pilote A/A (exp. 3) montre que la métrique est trop bruitée pour un seul monde → on ne peut rien trancher à 15 USD, et il faut un budget plus large ou un protocole adaptatif.

---

### Ordonnancement recommandé (séquentiel, chaque étape conditionne la suivante)

```
Exp. 1 (compat. relais)  ──pass──▶  Exp. 2 (enfermement, en parallèle si budget)  
         │                                     │
         ▼ fail                                ▼ résultat gardé pour (b) éventuel
   Adapter client ou                     
   tester (b) directement          Exp. 3 (pilote A/A)
                                          │
                                          ▼ pass
                                   Exp. 4+5 (Kaimen vs témoin, fausses découvertes)
                                          │
                                   ▼ H_A tient           ▼ H_B tient
                              Brancher (a) en v67    Pas de scientifique ;
                              puis tester (b)        rester au proposeur simple
```

FIN-DE-CELLULE