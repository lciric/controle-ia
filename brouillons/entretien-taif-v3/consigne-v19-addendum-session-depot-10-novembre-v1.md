# Addendum à la consigne de la v19 : ce qui a changé le 10 novembre (session-dépôt) — v1

- **Pour** : la session mère, qui rédige la v19 (`consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md`, `5609fc65…`). Cet
  addendum ne la remplace pas et n'écrit pas la v19 : il donne les faits et les pièces scellées du 10 novembre.
- **Écrit par** : la session-dépôt `session_01QPDgKgcLdggoVJfGC5cBw8`, le 10 novembre 2026, en autonomie (note `…-0927-…`).
  Rien du coffre ; aucun contenu de mode ni de candidat.

## 1. Pièces neuves, scellées

| Pièce | Chemin (branche `claude/upbeat-cray-dmauvv`) | Empreinte |
|---|---|---|
| Règle du jeu du bras d'attaque, après quatre contre-lectures | `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon5.md` | `527a3e7e…` |
| Brief de la session « attaquant informé » | `docs/procedures/brief-session-attaquant-informe-v1.md` | `55108eb8…` |
| Choix de l'attaque publiée (Bailey), après trois contre-lectures | `docs/notes/reproduction-attaque-publiee-v1/choix-et-anteriorite-v1-brouillon3.md` | `e5bab8c3…` |
| Décisions de Lazar du 10 novembre | `registres/passations/2026-11-10-0704`, `-0725`, `-0802`, `-0846`, `-0919`, `-0927` | `bba97a1a`, `081cb8e3`, `06e8f102`, `609e48f6`, `d5739189`, `73857eaf` |

## 2. Bras d'attaque : ce que la v19 peut dire, et ne doit pas dire

1. **L'échelon « avec retour » a un porteur** (décision du 10 novembre, `bba97a1a…`) : l'attaquant peut lire les verdicts
   des moniteurs gelés en nombre compté, avec une procédure d'optimisation publiée et un plafond de requêtes scellé d'avance.
   La v19 peut dire que l'axe « requêtes » de la taxe de déplacement et l'« attaque optimisée » du test d'acceptation ont un
   porteur déclaré. Rien n'a tourné.
2. **Séparation** : une session « attaquant informé » est montée au mandat réduit (`081cb8e3…`). Phrase vraie le jour de
   l'entretien, à préférer tant que le nœud 1 n'est pas tranché : « *The informed attacker is a separate instance from the
   monitor designers, launched only after the monitors are frozen; until then we calibrate on published attacks.* »
3. **Attaque publiée** : Bailey et collègues est choisie et a le feu vert de Lazar, mais **son code n'a aucune licence**
   (`d5739189…`) : la v19 ne dit pas « *we reproduced* ». Au plus, si Lazar a écrit à l'auteur : « *we chose a published
   attack to reproduce; its code has no license yet and we have asked the authors* ».
4. **Revue de sécurité externe** (nœud 3 de la règle du jeu) : ne dire ni « *not yet commissioned* » ni « *done* » avant le mot
   de Lazar ; la phrase sûre sous les deux options : « *the attack arm is mounted and nothing has run* ».
5. **« Hidden mode »** : ne pas dire « *hidden* » tant que le nœud 6 (i) n'est pas tranché : les candidats sont nommés en clair
   dans deux lignes du registre.
6. Inchangé : « bras d'attaque : monté, jamais lancé » au tableau de ce qui n'existe pas encore ; ne dire ni un contenu, ni
   une recette, ni un nombre de refus ; le classifieur seulement sur question.

## 3. La pince : une divergence à faire trancher par Lazar avant d'écrire

La consigne (section 1, point 1) fait dire « *That is a hypothesis we will pre-register* ». La règle du jeu scellée (nœud 8,
recommandation (a), confiance 0,7) lit la pince comme une **mesure jointe** de deux hypothèses déjà au texte envoyé (se
cacher des sondes ; quorum hétérogène), sans revendication neuve : dire « hypothèse » modifierait le programme, ce qui est un
nœud de Lazar. En attendant son mot, une phrase compatible avec les deux options : « *Our defensive bet is a pincer: to fool
an external monitor, an agent has to conceal more, and concealment is itself an internal signal. We will measure it jointly
with our pre-registered hypotheses, on frozen monitors; it is not a result.* »

## 4. La chaîne de prédictions, pour l'ouverture

Théorie → simulation (31 sur 31 ; verdict formel en cours par un lecteur neuf) → activations réelles (mesure unanime, v15 en
cours, une seule course après dépôt chez le tiers ; phrases de chaque issue écrites d'avance :
`docs/notes/entretien-resultats-v1/lectures-possibles-mesure-unanime-v1.md`, brouillon) → littérature (Bailey, suspendue à la
licence). Synthèse d'ensemble, non contre-lue : `livrables/synthese-programme-entretien-2026-11-10-v1.pdf` (`95f6dcc8…`).

## 5. Date

Entretien le 20 ou le 27 novembre, selon l'avancement (Lazar, `d5739189…`).

## 6. Simulation du lemme et du théorème : verdict prononcé, et deux précisions sur le texte envoyé

- **Verdict formel prononcé par un lecteur neuf** : « confirmé avec réserves » (`docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md`,
  `bc53b746…`, à sceller et à soumettre à Lazar). Il remplace, dans la v19, la mention de la v18 « verdict formel R13 non
  prononcé » (v18, l. 185). Réserve principale : 31 sur 31 était attendu par construction ; le résultat valide l'instrument et
  l'arithmétique des preuves en simulation, pas la revendication sur modèles réels.
- **Chiffres du texte envoyé (l. 89-93) : exacts**, avec deux précisions si on les reprend : « 0,21 à 0,35 » ne vaut qu'au plus
  fort effet d'épisode testé (de 0,034 à 0,351 sur les six réglages) ; « 0,17 » est 0,1656, à la corrélation entre agents la
  plus forte testée.
- **Phrase du texte envoyé sur le précurseur boîte noire (arXiv 2606.10456, l. 87-88)** : « *its central statement does not
  hold for its own construction* » n'est établie, dans notre simulation, **que pour la somme** ; pour le maximum, qui reste au
  plus à son taux, la proposition du papier tient (verdict, section des chiffres cités ; non vérifié sur le PDF du papier).
  **Ne pas la répéter telle quelle** à l'entretien ; au plus : « *for sum statistics, its central statement does not hold for
  its own construction in our simulation* ».
