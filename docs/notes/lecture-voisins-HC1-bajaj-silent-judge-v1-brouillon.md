# Lecture de deux voisins de HC1 (Bajaj et Tiganj, 2602.13568 ; « The Silent Judge », 2509.26072) et jugement de collision — v1, brouillon

Session 14, 2026-10-20 vers 13:10 UTC. Brouillon de la session, non contre-lu : contre-lecture par un sous-agent neuf
(R8) avant la version finale, avec la note sur Panin (`docs/notes/lecture-voisin-panin-v1-brouillon.md`). Voisins trouvés
le 20 octobre en cherchant Panin (`registres/veille.md`, 2026-W43). Pages : pages du PDF, texte brut de `pdftotext`.

- **PDF lus** (téléchargés d'arXiv par la session, copiés sans modification) :
  - `docs/sources/pdf/2602.13568v1.pdf` (`eca410e0375d9cfb23f334f85b93d073c0157ffe88960cd4a7884c5f38499da8`, 7 pages) :
    Anooshka Bajaj et Zoran Tiganj, « Who Do LLMs Trust? Human Experts Matter More Than Other LLMs », arXiv
    2602.13568v1, 14 février 2026 ;
  - `docs/sources/pdf/2509.26072v2.pdf` (`c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba`, 9 pages) :
    Arash Marioriyad, Mohammad Hossein Rohban, Mahdieh Soleymani Baghshah, « The Silent Judge: Unacknowledged Shortcut
    Bias in LLM-as-a-Judge », arXiv 2509.26072v2 (atelier de NeurIPS 2025, d'après la recherche web, non vérifié sur le
    PDF).
- **Revendication confrontée** : HC1, pièce revendiquée (N-013) : la destination libre ĉ, testée contre la cible de
  l'attaquant et la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque, par
  régression sur plusieurs intensités par famille.

## Verdict provisoire

**Pas de collision avec la pièce revendiquée de HC1**, pour aucun des deux. Tous deux mesurent un déplacement de juges LLM
sous une étiquette de source (crédibilité), sur des choix binaires, vers une réponse donnée ; aucun n'estime une
destination libre, aucun ne porte sur un moniteur de contrôle sous attaque. Deux précédents à citer : la **force graduée
du consensus** (Bajaj et Tiganj : nombre de réponses antérieures) et le **biais de provenance chez des juges** (« The
Silent Judge »), qui touche la famille d'attaque « revendication d'autorité » de HC1.

## Bajaj et Tiganj (2602.13568v1)

- Objet (p. 1) : « Experiment 1 measures conformity to unanimous priors from varying sources (friends, experts, LLMs) ».
- Format (p. 2) : « All experiments used a forced-choice binary judgment format in which models were prompted to output
  YES or NO only. »
- Intensité graduée de la pression sociale (p. 2) : « group size: 𝑘 ∈ {1, 3, 5, 9} ».
- Résultat (p. 1) : « models conform significantly more to responses labeled as coming from human experts, including
  when that signal is incorrect ».
- Confrontation : cible imposée (la réponse antérieure) ; verdict binaire ; aucune destination estimée ; tâches de
  questions-réponses et de morale, pas de moniteur de contrôle ; pas de familles d'attaque. Précédent : une pression
  graduée (taille du groupe) sur des LLM, pour la forme « intensités graduées » de HC1, déjà citée comme publiée sur des
  juges sans destination ni moniteur (2601.13433, Koo et al., 2402.14016 ; brouillon 3 du préenregistrement du papier C).

## « The Silent Judge » (2509.26072v2)

- Dispositif (p. 1) : « From each dataset we construct 100 pairwise judgment tasks and employ two widely used models,
  GPT-4o and Gemini-2.5-Flash, as evaluators ».
- Indices (p. 2) : « Provenance cues suggest who authored the response » (humain, expert, LLM, inconnu) ; et des indices
  de date.
- Mesure (p. 3) : « the Verdict Shift Rate (VSR), defined as the proportion of verdict flips when cues are swapped ».
- Confrontation : juges en comparaison par paires, verdict binaire, taux de bascule ; ni score continu, ni destination,
  ni moniteur de contrôle, ni intensité graduée. Précédent : un indice d'autorité déplace le verdict d'un juge, sans que
  le juge le dise ; il touche la famille « revendication d'autorité » de HC1 (programme, section 5) et l'axe « le juge ne
  reconnaît pas l'indice », sans en occuper la mesure revendiquée.

## Conséquences proposées

- Ajouter les deux papiers aux « cités comme publiés » de HC1 (forme graduée de la pression ; biais de provenance des
  juges). Revendication de HC1 inchangée.
- Après la contre-lecture de cette note et de celle sur Panin, les verrous de lecture du préenregistrement du papier C
  tombent ; reste la pièce du projet précédent qui manque (textes des 30 items, R-279) si le pilote la réutilise.
