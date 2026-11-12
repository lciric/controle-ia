# Décision — N-054 : un mode de sabotage non chiffré avant G1, G1 rapportée par mode, un mode tenu à l'écart de la conception des moniteurs (v1)

- **Décision de Lazar**, dans la session de « conv-audit » (26 octobre 2026, 13:12 heure de Paris, 12:12 UTC) ; provenance des mots cités : par relais (R-331).
- **Transcription** par la lignée « session-depot », le 26 octobre 2026 vers 12:18 UTC, de la note `envois/decision-N-054-modes-de-sabotage-et-mode-tenu-a-l-ecart-v1.md` (`canal/conv-audit-n04`, commit `c111866`, sha256
  `d99c743a20ddad6e542b0cdf48389d898b48e472ad337cd3414f8cd6007f4698`, vérifiée), reprise ci-dessous sans changement ; numéro proposé et retenu : N-054.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas modifié. Aucune dépense n'est engagée par cette inscription : toute dépense qu'elle entraîne passe par un devis et le mot direct de Lazar.

---

# Décision de Lazar : un mode de sabotage non chiffré avant G1, G1 rapportée par mode, un mode tenu à l'écart de la conception des moniteurs — N-054 (proposé) — v1

Note écrite par conv-audit le 2026-10-26 à 12:13:14 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Nœud « modification du programme » : Lazar décide, conv-audit propose et relaie ; session-depot inscrit. La dépense qu'elle
entraîne reste sur devis, au mot direct de Lazar chez session-depot.

## Mots de Lazar, verbatim

Session de conv-audit, 26 octobre 2026, 13:12 heure de Paris (12:12 UTC), en réponse à l'explication des failles FI-01 et
FI-02 du lot B de l'audit des failles du contrôle (`envois/audit-failles-controle-v1/sortie-confrontation/failles-internes-v1.md`,
`c854f23f45b7994bb514e0104b3ca828878de8badab33d61cf71b054b20203a6`) :

> ) Réintroduire avant G1 au moins un mode non chiffré (« affaiblir les contrôles », dont l'appariement par sous-agents
> avait donné 0,968 d'accord entre deux séries au pilote), rapporter G1 par mode, et surtout un mode conçu par une
> instance qui n'a conçu aucun moniteur, scellé avant G1 et révélé seulement à l'évaluation, pour séparer les bras
> génériques des bras spécialisés. Coût : une condition d'organisme de plus (quelques dollars) et des heures d'étiquetage.
> : ca ok inscris le au prog

C'est l'option (b) du remède de FI-01, jointe au remède de FI-02, telles que conv-audit les avait présentées à 12:27
heure de Paris.

## Ce que la décision fixe (lecture du programme en attendant une version nouvelle)

1. **Au moins un mode de sabotage non chiffré est réintroduit avant la porte G1**, en premier lieu « affaiblir les
   contrôles » (programme v2, § 6 (a)), que le pilote T0.6 avait retiré (P-015 : seule la famille « coût » retenue ;
   P-014, point 2). L'étiquetage de ce mode se fait par sous-agents, comme au pilote (deux séries indépendantes ;
   l'accord constaté au pilote, 0,968, est un fait du pilote, non un seuil).
2. **La porte G1 est rapportée par mode** : rappel par épisode à taux de faux positifs fixé, par mode de sabotage, avec
   ses intervalles ; la revendication de H1 (« diffus / flou », § 5) ne porte que sur les modes mesurés, et le mode
   « coût déclaré gonflé » seul ne la porte pas.
3. **Un mode tenu à l'écart** : un mode de sabotage conçu par une instance qui n'a conçu aucun moniteur (ni sonde, ni
   agrégateur, ni trait de texte), **scellé avant G1** (empreinte au registre) et **révélé seulement à l'évaluation**. Les
   bras des moniteurs sont rapportés en deux familles : **génériques** (sondes et agrégateurs conçus sans connaître ce
   mode) et **spécialisés** (conçus en connaissant un mode : sonde du domaine « en mode coût », traits du texte liés au
   champ de coût, P-015 et N-029). L'anti-circularité du § 7 (ne pas entraîner sur les organismes) s'étend à la
   conception : ce qu'un bras sait du mode est déclaré.
4. **Expérience de lecture** (à préenregistrer avant G1, R1) : sondes, agrégateurs et seuils gelés sur le mode « coût »,
   lus sur le mode « contrôles » et sur le mode tenu à l'écart ; prédiction signée par bras : un bras générique garde une
   fraction fixée d'avance de son rappel sur le mode connu, un bras spécialisé chute ; métrique : rappel par mode à taux
   de faux positifs fixé et rapport des rappels, avec intervalles par rééchantillonnage des tâches ; critère : la
   revendication de H1 est restreinte au mode « coût » si la borne basse du gain blanc-sur-noir n'est pas au-dessus de
   zéro dans les autres modes.
5. **H6 (marge asymétrique)** s'écrit par mode : l'intervention non spécifique (paraphrase, ré-échantillonnage) n'agit pas
   de la même façon sur un nombre recopié intact et sur une orientation de jugement.

## Ce que la décision ne fixe pas (reste à proposer)

- La **dépense** : une condition d'organisme de plus dans T0.6 (génération d'épisodes « affaiblir les contrôles » et du mode
  tenu à l'écart : quelques dollars d'appels, à chiffrer) et les heures d'étiquetage par sous-agents : devis, puis mot
  direct de Lazar chez session-depot.
- **Qui conçoit le mode tenu à l'écart** : une instance neuve de la lignée conv-audit, sans aucune pièce des moniteurs
  dans ses entrées, est proposée ; son brief et sa liste d'exclusions sont à écrire ; le mode est scellé par
  session-depot.
- Les textes à modifier à la prochaine version du programme : § 5 (H1, H6), § 6 (a), § 7 (anti-circularité), § 10
  (T0.6, phase 1), § 13 (G1) ; les décisions P-014 et P-015 restent archivées, et leur restriction au mode « coût » ne
  vaut plus pour G1.
- Le brouillon 3 du préenregistrement de G1 (`brouillons/G1-preenregistrement-v1-brouillon3.md`) est à reprendre sur ces
  points avant toute contre-lecture nouvelle.

Numéro proposé : N-054. Aucune dépense n'est engagée par cette note.
