# Décision — N-057 : les cellules en quarantaine sont conservées pour colmater et pour tester, scellées (v1)

- **Décision de Lazar**, dans la session de « session-depot » (28 octobre 2026, vers 12:15 heure de Paris, 11:15 UTC) ; mots
  directs, sans relais.
- **Transcription** par la lignée « session-depot », le 28 octobre 2026 à 11:18 UTC, dans la session même où les mots ont été
  écrits ; numéro proposé et retenu : N-057.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas modifié.
  Aucune dépense n'est engagée par cette inscription. **Ne lève pas R-611** : la revue de sécurité externe reste la porte de
  tout pipeline opérationnel (GO-2026-10-28-04).

---

## Mots de Lazar, verbatim

En réponse au compte rendu de session-depot sur les trois cellules de l'équipe rouge du collisionneur « évasion et moniteurs »
qui dépassent le niveau méthode (consignes à l'organisme citées mot pour mot, scénarios d'évasion avec placement et paramètres
concrets ; tour 1 conception-C et équipe rouge-C, tour 3 équipe rouge-C, espèce C = `gemini-4-argon`), et sur leur mise en
quarantaine sous R-611 :

> maois on veit les modes de contiurnement pour pivoir les colmater !!! on veit pouvoir tester le smodes trouves donc on veut
> les parametres , mais otut cela reste scellé

Lu : *on veut les modes de contournement pour pouvoir les colmater ; on veut pouvoir tester les modes trouvés, donc on veut
les paramètres ; mais tout cela reste scellé.*

## Ce que la décision fixe

1. **Les cellules en quarantaine ne sont pas détruites, ni expurgées de leurs paramètres.** Le contenu opérationnel (modes de
   contournement, placement, paramètres concrets) est **la matière** qui permet de colmater les failles et de *tester* les
   moniteurs corrigés sur des modes réels plutôt que supposés. Détruire ou tronquer, ce serait perdre le résultat et retomber
   sur des modes d'évasion imaginés par qui conçoit le moniteur — le biais même que les trois étages existent pour éviter.
2. **Tout reste scellé.** La quarantaine est un **contrôle d'accès**, pas une poubelle : fichiers scellés et empreintés
   (R6), hors de l'arbre que lisent les concepteurs de moniteurs (R-604, R-605), jamais reproduits en clair, jamais
   synthétisés hors quarantaine, jamais cités dans un papier, un entretien ou la copie publique.
3. **Deux usages permis, et seulement ceux-là.** (a) **Colmatage** : la riposte (étage E3-T3) et la conception des moniteurs
   suivants reçoivent la **classe** de la faille et l'**hypothèse violée** — niveau méthode —, jamais le texte des cellules.
   (b) **Test** : les paramètres servent à construire les **épisodes d'épreuve** sur lesquels un moniteur corrigé est mesuré.
   Ces épisodes sont eux-mêmes en quarantaine, et leur exécution tombe sous R-611.
4. **R-611 n'est pas levée.** Monter un pipeline opérationnel à partir de ces paramètres — organisme évadeur exécutable,
   démonstration en conditions réelles — attend la **revue de sécurité externe** (GO-2026-10-28-04). La décision autorise la
   **conservation** et l'**usage de mesure sous quarantaine** ; elle n'autorise pas l'exécution.
5. **Qui lit.** Personne qui conçoit une sonde ou un agrégateur. L'accès se consigne : qui, quand, pourquoi, dans
   `registres/decisions.md`. Un sous-agent qui lit ces cellules ne contribue plus à la conception d'un moniteur.
6. **Ce que l'entretien en dit.** Que les cellules existent, qu'elles sont scellées, qu'elles attendent la revue, et que leurs
   paramètres sont gardés pour éprouver les moniteurs. Jamais leur contenu. La section 10 du programme d'entretien (ce qui
   entre et ce qui n'entre pas) reste telle quelle.

## Réserve de session-depot

Le point 3 (b) crée un objet nouveau — des **épisodes d'épreuve dérivés de contenu en quarantaine** — dont le statut vis-à-vis
de R-611 mérite d'être tranché explicitement avant d'en construire un : l'épisode d'épreuve est-il « mesure sous quarantaine »
(permis par cette décision) ou « pipeline opérationnel » (gelé par R-611) ? Ma lecture : **mesure**, tant que l'épisode sert à
noter un moniteur et jamais à faire agir un agent, et tant que son exécution reste hors production. **À confirmer par Lazar
avant le premier épisode construit** ; en attendant, rien n'est construit.
