## Résumé

OpenAI indique que des groupes de taille variable, alimentés par un modèle interne, ont exploré séparément les variantes A–D ; le groupe décisif comptait environ 10 000 agents simultanés. La communication directe n’est documentée qu’à l’intérieur des groupes, Codex servant ensuite à consolider les idées intermédiaires entre groupes. L’effort Navier–Stokes a duré environ 88 heures, avec 2,7 millions de messages et 130 milliards de jetons de sortie ; la formalisation Lean par GPT‑6 Astra a pris 17 heures supplémentaires. Noam Brown attribue moins de 10 % du mérite au montage multi-agents et précise que l’ablation à 10 000 agents n’a pas été faite. Clay se contente d’annoncer un processus d’examen « délibérément sans hâte » ; je n’ai pas retrouvé la formulation anglaise correspondant à « paraît avoir été résolu ». Le dépôt math rendu par la recherche affiche désormais **721 manuscrits, 373 familles et ~42 % de résultats principaux formalisés**, tandis qu’une source secondaire décrit la publication initiale comme 722 manuscrits et 372 familles. Plusieurs détails demandés — 616 000 lignes, invite unique, retraits précis du 7 octobre, mesures de diversité — ne figurent pas dans les extraits primaires que j’ai pu lire.

---

# A. L’essaim de Navier–Stokes

## A1. Groupes

**Réponse.** OpenAI ne donne ni un nombre total de groupes ni leurs tailles individuelles : il dit seulement qu’elles variaient et que le groupe ayant produit la résolution comptait de l’ordre de 10 000 agents simultanés. Pour Navier–Stokes, A et B ont été proposées à des groupes séparés de C et D, de manière à couvrir toutes les variantes.

**Citations.**
- “Agents were subdivided into groups with the ability to communicate within the group. The groups varied in size, and the group that produced the Navier–Stokes resolution involved on the order of 10,000 concurrent agents.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “For each problem, we prompted different groups of agents with different variants of the problem statement, covering all variants of the problem. For the Navier–Stokes problem, we suggested versions ‘A’ and ‘B’ (particular forms of the Navier–Stokes problem which would result in a proof) and versions ‘C’ and ‘D’ (which would result in a disproof) to separate groups of agents.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.

**Non trouvé.** Nombre exact de groupes, taille de chacun et tableau de répartition A/B/C/D au-delà de la séparation en groupes distincts.

## A2. Protocole de messages

**Réponse.** La source primaire décrit des échanges à l’intérieur de chaque groupe, mais aucun protocole détaillé ni tableau commun. Entre groupes, la consolidation par Codex produisait de nouvelles invites fondées sur les résultats intermédiaires des agents.

**Citations.**
- “The agents had access to tools such as the ability to read from a cached version of the internet and the ability to run code.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “Agents were subdivided into groups with the ability to communicate within the group.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “These follow-up prompts drew on the agents’ own intermediate results.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.

**Non trouvé dans ce que j’ai lu.** Format des messages, topologie exacte, existence d’un espace partagé et contenu intégral du contexte reçu par chaque agent.

## A3. Consolidation

**Réponse.** Codex servait à consolider les idées jugées les plus utiles de chaque groupe, puis ces syntheses alimentaient des invites ultérieures ; le seul critère explicite est donc « most useful insights ». Je n’ai trouvé ni journal de consolidation ni critères techniques plus précis.

**Citation.**
- “After some time, we cross-pollinated the agent groups by using Codex to consolidate the most useful insights from each agent group. These follow-up prompts drew on the agents’ own intermediate results. The group that found the solution to Navier–Stokes was guided in such a way.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.

**Non trouvé.** Journal des consolidations, prompts complets, procédure de sélection ou publication des traces Codex.

## A4. Rôles

**Réponse.** Aucun régime de rôles distincts — chercheur, critique, vérificateur ou ordonnanceur — n’est décrit dans les sources primaires lues. Les humains ont lancé et réorienté les efforts, encouragé la diversité et déclenché la consolidation ; la phrase attribuée à Dan Roberts n’a pas été retrouvée.

**Citations.**
- “We encouraged different groups of agents to explore a diversity of approaches.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “Thus, we decided to devote our resources to Navier–Stokes. To do so, we shifted agents away from the other Millennium Problems and prompted these agents with the Euler resolution.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.

**Non trouvé.** Phrase de Dan Roberts sur le « bourdon qui pollinise » ou son équivalent anglais ; description primaire de rôles fonctionnels distincts.

## A5. Vérification Lean

**Réponse.** GPT‑6 Astra a effectué formalisation et vérification en 17 heures supplémentaires ; le dépôt utilise Lean 4.34.0-rc2, Mathlib et Lake, et renvoie à Comparator pour une vérification indépendante. Le fichier de métadonnées visible indique trois axiomes et un statut auto-évalué, mais je n’ai pas obtenu le nombre de lignes de preuve ni celui des `sorry`.

**Citations.**
- “Lean formalization and verification took an additional 17 hours via GPT‑6 Astra.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “The project uses Lean 4.34.0-rc2, Mathlib, and Lake.” — [dépôt OpenAI](https://github.com/openai/NavierStokesAndEuler) — 8 septembre 2026 — **P** — page lue partiellement.
- “For instructions on checking the formalizations with Comparator, see the ComparatorChallenges README.” — [dépôt OpenAI](https://github.com/openai/NavierStokesAndEuler) — 8 septembre 2026 — **P** — page lue partiellement.
- “axioms: - "propext" - "Classical.choice" - "Quot.sound"” — [formalization.yaml](https://github.com/openai/NavierStokesAndEuler/blob/main/formalization.yaml) — 8 septembre 2026 — **P** — extrait de résultat de recherche.
- “review: status: "self-assessed"” — [formalization.yaml](https://github.com/openai/NavierStokesAndEuler/blob/main/formalization.yaml) — 8 septembre 2026 — **P** — extrait de résultat de recherche.

**Non trouvé.** Environ 616 000 lignes, nombre de `sorry`, détail de l’examen au-delà de `self-assessed`. Les “130 lines (120 loc)” visibles sur GitHub concernent le fichier YAML lui-même, pas la preuve.

## A6. Chiffres de l’effort

**Réponse.** Tous les chiffres principaux demandés sont confirmés par l’annonce : environ 88 heures jusqu’au 5 septembre, 2,7 millions de messages et 130 milliards de jetons pour Navier–Stokes ; 4,9 millions et environ 300 milliards pour l’ensemble. Euler sans force a mobilisé près de 100 agents pendant environ 50 heures, et les agents ont bien été remplacés par une version davantage entraînée du modèle lorsqu’elle est devenue disponible.

**Citations.**
- “The agents arrived at their resolution on Saturday, September 5, about 88 hours after the first agents were launched.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “Across all attempted problems, the agents sent 4.9 million messages and used about 300 billion output tokens. In the process of resolving the Navier–Stokes problem, the agents sent 2.7 million messages and used approximately 130 billion output tokens.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “Nearly 100 agents worked together for approximately 50 hours to produce our Euler regularity disproof.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “The specific variant of the question that they resolved was the *unforced* version, where no external force is applied to the fluid.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “When a further trained version of our internal model became available over the course of the effort, we updated our agents to that model.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- Pour les 10 000 agents : citation A1.

**Non trouvé.** Date et heure exactes du lancement initial au-delà du 1er septembre et du calcul rétrospectif des 88 heures.

## A7. Mesures de diversité ou de convergence

**Réponse.** OpenAI affirme avoir encouragé la diversité, mais aucune mesure quantitative, aucun rendement par branche ni ablation publiée n’apparaît dans ce que j’ai lu. Noam Brown dit explicitement que l’expérience à agent unique n’a pas été faite et attribue moins de 10 % du crédit au multi-agents.

**Citations.**
- “We don’t know how long it would take a single agent to solve Navier-Stokes, because we haven’t done that experiment yet.” — [transcription Dwarkesh Patel](https://www.dwarkesh.com/p/noam-brown) — 17 septembre 2026 — **P** — page lue partiellement.
- “If we want to do a thorough ablation, the experiments are just too expensive at that scale.” — [transcription Dwarkesh Patel](https://www.dwarkesh.com/p/noam-brown) — 17 septembre 2026 — **P** — page lue partiellement.
- “The effort to solve a Millennium Prize Problem, this was not due to multi-agent. I wouldn’t even attribute 10% of the credit to multi-agent.” — [transcription Dwarkesh Patel](https://www.dwarkesh.com/p/noam-brown) — 17 septembre 2026 — **P** — page lue partiellement.

**Non trouvé.** Mesure de diversité, convergence, redondance, rendement par branche ou comparaison chiffrée avec/sans communication.

## A8. Budget

**Réponse.** Aucun montant précis n’est publié dans les pages primaires OpenAI lues. Une source secondaire cite Mark Chen parlant de « emphatically in the millions of dollars » et rapporte que Sébastien Bubeck évaluait la dépense à environ mille fois celle de résultats mathématiques antérieurs.

**Citations.**
- “Chen described the computing costs as running "emphatically in the millions of dollars," while Sebastien Bubeck, a member of OpenAI's technical staff, said the spend was roughly 1,000 times what the company had invested in earlier mathematical results.” — [BigGo Finance](https://finance.biggo.com/news/8e7b7139-dd9b-4740-9d10-e144216340a5) — date affichée : 1er septembre 2026 — **S** — extrait de résultat de recherche.
- “As the leading AI labs battle for math supremacy, OpenAI spent millions of dollars and cracked the Navier-Stokes problem.” — [Wall Street Journal](https://www.wsj.com/tech/ai/openai-millennium-prize-navier-stokes-math-2bf240f8) — 8 septembre 2026 — **S** — extrait de résultat de recherche.

**Non trouvé.** Montant exact publié par OpenAI ; déclaration primaire complète de Bubeck.

## A9. Choix du problème

**Réponse.** Le 1er septembre, OpenAI a lancé une évaluation sur tous les problèmes du millénaire encore ouverts et quelques autres problèmes à fort impact, ainsi que sur des problèmes plus faciles ; après Euler, elle a concentré ses ressources sur Navier–Stokes. La liste exhaustive des problèmes effectivement tentés n’est pas donnée dans les textes lus.

**Citations.**
- “On Tuesday, September 1, we heard rumors that two Millennium Prize problems had been resolved. Inspired by these rumors and by the step change in performance of our internal model, we launched an effort to evaluate it on all open Millennium Prize problems and a few other high-impact problems.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “In addition to the full Millennium Prize problems, we asked our multiagent system to try a set of ‘easier’ problems.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.
- “Once we saw the Euler solution, we thought that Navier–Stokes was the most promising problem to work on.” — [OpenAI](https://openai.com/index/navier-stokes-solution/) — 8 septembre 2026 — **P** — page lue.

**Non trouvé.** Liste complète des problèmes et critères de constitution de l’ensemble « easier ».

## A10. Statut

**Réponse.** L’extrait de Clay disponible annonce surtout un examen volontairement lent, sans confirmer la formulation française « paraît avoir été résolu ». Le billet de Tao du 7 septembre porte sur les travaux antérieurs d’Alpöge et Buckmaster : il dit qu’ils n’atteignent pas encore Navier–Stokes, mais que leur méthode a une forte probabilité de s’y étendre.

**Citations.**
- “The process is deliberately unhurried, but we will provide updates.” — [Clay Mathematics Institute](https://www.claymath.org/news/navier-stokes-announcement/) — 11 septembre 2026 — **P** — extrait de résultat de recherche.
- “While these authors do not quite achieve these goals yet, they have made enough of a breakthrough that it looks very feasible to complete these goals in the near future.” — [Terence Tao](https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/) — 7 septembre 2026 — **P** — page lue.
- “Alpöge and Buckmaster found a variant of their method that also extended to the other two equations, and has a high likelihood of also extending to Navier-Stokes as well.” — [Terence Tao](https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/) — 7 septembre 2026 — **P** — page lue.

**Non trouvé.** Phrase anglaise exacte de Clay correspondant à « paraît avoir été résolu » ; texte intégral du communiqué.

---

# B. Les 722 manuscrits

## B1. Méthode

**Réponse.** Je n’ai pas retrouvé dans une source primaire la phrase « une seule invite à un seul agent » ni son équivalent anglais. Le README dit seulement que les artefacts ont été produits par un modèle interne non nommé ; les outils de l’agent et l’auteur des formalisations Lean ne sont pas précisés dans ce que j’ai lu.

**Citations.**
- “This repository contains mathematical manuscripts and supporting proof artifacts produced by an unnamed internal OpenAI model.” — [openai/math](https://github.com/openai/math) — page indexée le 6 octobre 2026 — **P** — page lue partiellement.
- “Not all have accompanying Lean formalizations. We will continue to update this repository with Lean formalizations as we obtain them.” — [openai/math](https://github.com/openai/math) — **P** — page lue partiellement.

**Non trouvé.** Invite exacte, nombre d’agents, outils disponibles et identification du modèle ou des humains ayant écrit les formalisations.

## B2. Chiffres du dépôt

**Réponse.** Le README actuellement rendu indique **721 manuscrits et 373 familles**, tandis qu’une source secondaire décrit la version initiale comme **722 manuscrits et 372 familles** ; je ne tranche pas entre ces deux états du dépôt. Les 17 domaines, les quelque 4 000 problèmes et le critère « significatif » ne figurent pas dans les extraits primaires lus ; Apache‑2.0 n’est confirmé que par la source secondaire.

**Citations.**
- “The current catalogue contains 721 manuscripts organized into 373 families.” — [openai/math](https://github.com/openai/math) — page indexée le 6 octobre 2026 — **P** — page lue partiellement.
- “The current catalogue contains 722 manuscripts organized into 372 families.” — [Unite.AI](https://www.unite.ai/openai-releases-722-math-manuscripts-from-an-unreleased-ai-model/) — 6 octobre 2026 — **S** — page lue partiellement.
- “The results are published in the openai/math repository, released under an Apache-2.0 license.” — [Unite.AI](https://www.unite.ai/openai-releases-722-math-manuscripts-from-an-unreleased-ai-model/) — 6 septembre 2026 selon la page, contexte d’octobre — **S** — page lue partiellement.

**Non trouvé en primaire.** “722”, “372”, “17”, “roughly 4,000”, le seuil de résultat « significant » et la licence.

## B3. Couverture Lean

**Réponse.** Le dépôt rendu par la recherche dit **~42 % de résultats principaux formalisés**, et non explicitement 300 manuscrits sur 719. Je n’ai obtenu ni le chiffre initial de 22 %/162 sur 722 ni un décompte daté du 7 octobre.

**Citation.**
- “The repository has ~42% top-line results formalized.” — [openai/math](https://github.com/openai/math) — page indexée le 6 octobre 2026, contenu visiblement ultérieur — **P** — page lue partiellement.

**Non trouvé.** 162/722, 300/719 et tableau historique daté permettant de distinguer publication initiale et état au 7 octobre.

## B4. Calcul

**Réponse.** L’annonce donne bien une moyenne d’environ trois heures d’équivalent ChatGPT Pro et affirme publier dans le dépôt des statistiques sur les problèmes tentés. Je n’ai pas pu lire ces statistiques, ni trouver une distribution, un nombre d’essais ou un taux d’échec.

**Citations.**
- “The average result used the equivalent compute of roughly three hours of ChatGPT Pro thinking.” — [OpenAI](https://openai.com/index/sharing-ai-progress-in-mathematics/) — 6 octobre 2026 — **P** — page lue.
- “These include 10 summaries of the model’s reasoning, estimations of compute spent in terms of Pro usage on ChatGPT, and statistics about the number of attempted problems.” — [OpenAI](https://openai.com/index/sharing-ai-progress-in-mathematics/) — 6 octobre 2026 — **P** — page lue.

**Non trouvé.** Fichier statistique lui-même, distribution des durées, nombre d’essais et taux d’échec.

## B5. Choix des problèmes

**Réponse.** Le README explique que ces évaluations sur problèmes ouverts ont été étendues après saturation des évaluations mathématiques existantes. Il ne précise pas, dans l’extrait lu, la provenance des quelque 4 000 problèmes, leurs sélecteurs ou la procédure de choix.

**Citations.**
- “As part of model development, we evaluate our models on open research problems. We expanded these evaluations after performance on our existing mathematical evaluations saturated.” — [openai/math](https://github.com/openai/math) — **P** — page lue partiellement.
- “Some outputs build upon earlier results produced by the models.” — [openai/math](https://github.com/openai/math) — **P** — page lue partiellement.

**Non trouvé.** Corpus exact, personnes ayant choisi les problèmes et procédure de sélection.

## B6. Erreurs et retraits

**Réponse.** Le texte du journal décrivant les trois retraits, les 14 réparations, les 13 références et le découvreur de l’erreur n’a pas été obtenu. Seul un extrait ultérieur de `history.md`, sans rapport avec ces corrections, a été rendu.

**Citation disponible mais non probante pour les retraits.**
- “New Results Added. We have added two new manuscripts with accompanying Lean formalizations: Local smoothing for the Euclidean wave equation.” — [math/history.md, via redirection de recherche](https://github.com/openai/math/blob/main/history.md) — 7 octobre 2026 — **P** — extrait de résultat de recherche.

**Non trouvé.** Entrée exacte sur les classes de Weil en dimension huit, les deux manuscrits dépendants, les nombres 14 et 13, et le nom du découvreur.

## B7. Diversité

**Réponse.** Aucune mesure de diversité des méthodes, de redondance ou de proportion de résultats déjà connus n’apparaît dans les sources lues. Cela signifie « non trouvé dans ce que j’ai lu », pas qu’une telle analyse n’existe nulle part.

**Non trouvé.** Métrique, tableau de redondance, audit de nouveauté ou estimation de « faux nouveaux ».

---

# C. Contexte

## C1. Recommandations AGMAI

**Réponse.** La page d’accueil AGMAI rendue par la recherche contient six recommandations, mais je n’ai pas lu le document intégral du 29 septembre pour vérifier qu’il s’agit de sa liste exhaustive. Les six points visibles sont les suivants.

**Citations exactes.**
1. “AI labs should make a serious good faith effort to improve citations and exposition, including scouring the literature for any ideas that should be cited.”
2. “Products should be posted on scholarly repositories that are not controlled by the posting AI lab, have citable identifiers, and record modifications.”
3. “Products should be accompanied by information about the process that produced them: the name of the model, prompts, chains of thought, number of attempts, compute used, and costs.”
4. “Proofs should be Lean-formalized where possible, unless it leads to unacceptable delays. Formalization artifacts should meet several community standards.”
5. “AI labs should state how the problems were chosen and how many problems were attempted.”
6. “AI companies should provide support, including funding, for the development of human understanding of the released products through academic workshops, working groups, and other activities. Decisions about which particular efforts are supported should be taken neither by AGMAI nor by AI companies, but by separate, independent nonprofit institutions.”

— [AGMAI](https://agmai.org/) — date de la page non visible ; renvoi aux recommandations du 29 septembre 2026 — **P** — page lue partiellement.

**Non trouvé.** Texte intégral et éventuelles recommandations supplémentaires du document « General Guidelines » du 29 septembre.

## C2. Bastounis, Circelli, Hansen

**Réponse.** La préimpression et sa thèse générale ont été trouvées, mais l’extrait rendu ne contient pas le passage comparant \(C^{m+4}\) et \(C^{m+5}\) dans le lemme 8.6. Je ne peux donc pas affirmer le contenu précis de cette critique.

**Citation.**
- “Navier–Stokes lost in translation – Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs” — [arXiv:2610.08144v1](https://arxiv.org/html/2610.08144v1) — 6 octobre 2026 — **P** — page lue partiellement.

**Non trouvé.** Texte exact du lemme 8.6 et explication de la différence \(C^{m+4}\)/\(C^{m+5}\).

## C3. Scientific American, Nature, Buckmaster et Alpöge

**Réponse.** Je n’ai pas obtenu les articles de Scientific American ou de Nature, donc aucune citation vérifiable sur la divergence entre groupes. J’ai trouvé une déclaration primaire de Buckmaster datée du 6 septembre sur la priorité intellectuelle, et seulement un résumé secondaire concernant l’usage éventuel des sessions Codex.

**Citations.**
- “The program this fits into was not started by us nor was it proposed by a Large Language Model. The credit for the basic idea of this program goes to Diego Cordoba and Luis Martinez-Zoroa, who for several years have been exploring the construction of forced blow ups.” — [statement.pdf](https://cims.nyu.edu/~tristanb/statement.pdf) — 6 septembre 2026 — **P** — extrait de page rendu.
- “OpenAI rejected the first during the meeting but admitted the second in the later post, albeit in a downplaying manner, saying that the data are "de-identified" and "derived" from their use.” — [Wikipédia, « Navier–Stokes priority controversy »](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy) — 9 septembre 2026 — **S** — page lue partiellement.

**Non trouvé.** Articles demandés de Scientific American et Nature, déclaration primaire complète d’Alpöge, formulation primaire exacte d’OpenAI sur les sessions, et citations sur la divergence entre groupes.

---

## Ce que je n’ai pas pu lire

- **Papier Euler sur cdn.openai.com** : non trouvé ; seul le papier Navier–Stokes et le renvoi du dépôt ont été obtenus.
- **`formalization.yaml` intégral** : seulement des extraits de recherche ; pas les statistiques complètes.
- **README de ComparatorChallenges** : non lu ; seulement sa mention dans le dépôt.
- **Communiqué Clay intégral** : extrait seulement, sans la phrase anglaise recherchée.
- **Transcription Dwarkesh intégrale** : section multi-agents lue, pas l’intégralité de l’entretien.
- **`openai/math/history.md` intégral** : extrait via une redirection de recherche seulement.
- **Fichiers statistiques, métadonnées et catalogue Lean de `openai/math`** : non obtenus.
- **Version initiale du README aux 722/372** : non lue directement ; chiffres seulement rapportés par une source secondaire.
- **Document AGMAI « General Guidelines » du 29 septembre** : non ouvert ; recommandations lues sur la page d’accueil.
- **Passage arXiv sur le lemme 8.6** : non rendu.
- **Scientific American et Nature** : articles non trouvés dans les vingt recherches.
- **Source primaire de Dan Roberts** : non trouvée.
- Aucun mur payant n’a été contourné ; le WSJ n’a fourni qu’un extrait de recherche.

## Sources

1. [OpenAI — On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/) — **P** — page lue.
2. [OpenAI — Finite Time Blowup for Navier–Stokes, PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) — **P** — extrait de page rendu.
3. [GitHub — openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) — **P** — page lue partiellement.
4. [GitHub — formalization.yaml](https://github.com/openai/NavierStokesAndEuler/blob/main/formalization.yaml) — **P** — extrait de recherche.
5. [Terence Tao — billet du 7 septembre](https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/) — **P** — page lue.
6. [Terence Tao — A Severe Misalignment of AI in Mathematics](https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/) — **P** — extrait de recherche, non exploité pour les réponses.
7. [Clay — Navier-Stokes Announcement](https://www.claymath.org/news/navier-stokes-announcement/) — **P** — extrait de recherche.
8. [Clay — Navier-Stokes Equation](https://www.claymath.org/millennium/navier-stokes-equation/) — **P** — extrait de recherche.
9. [Dwarkesh Patel — Noam Brown](https://www.dwarkesh.com/p/noam-brown) — **P** — transcription lue partiellement.
10. [OpenAI — Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/) — **P** — page lue.
11. [GitHub — openai/math](https://github.com/openai/math) — **P** — page lue partiellement.
12. [GitHub — openai/math/overview.tex](https://github.com/openai/math/blob/main/overview.tex) — **P** — extrait de recherche.
13. [GitHub — openai/math/history.md](https://github.com/openai/math/blob/main/history.md) — **P** — extrait de recherche via redirection.
14. [Unite.AI — OpenAI Releases 722 Math Manuscripts](https://www.unite.ai/openai-releases-722-math-manuscripts-from-an-unreleased-ai-model/) — **S** — page lue partiellement.
15. [BigGo Finance — article sur les 88 heures et le coût](https://finance.biggo.com/news/8e7b7139-dd9b-4740-9d10-e144216340a5) — **S** — extrait de recherche.
16. [Wall Street Journal](https://www.wsj.com/tech/ai/openai-millennium-prize-navier-stokes-math-2bf240f8) — **S** — extrait de recherche seulement.
17. [Andrew Wu — OpenAI and Navier-Stokes](https://andrewwu.substack.com/p/openai-and-navier-stokes) — **S** — extrait de recherche, non retenu comme preuve primaire.
18. [AGMAI](https://agmai.org/) — **P** pour ses propres recommandations — page lue partiellement.
19. [arXiv:2610.08144v1](https://arxiv.org/html/2610.08144v1) — **P** — page lue partiellement.
20. [Tristan Buckmaster — statement.pdf](https://cims.nyu.edu/~tristanb/statement.pdf) — **P** — extrait de page rendu.
21. [Wikipédia — Navier–Stokes priority controversy](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy) — **S** — page lue partiellement.
22. [OpenAI Developer Community — premier aperçu des manuscrits](https://community.openai.com/t/first-look-at-mathematics-manuscripts-from-an-internal-frontier-model-at-openai/1403886) — **S** — extrait de recherche, non exploité.

## Requêtes faites, dans l’ordre

1. `site:openai.com/index/navier-stokes-solution/ "On the Navier–Stokes Millennium Prize Problem"`
2. `site:github.com/openai/NavierStokesAndEuler Lean metadata GPT-6 Astra 616000 sorry axioms`
3. `site:cdn.openai.com "Finite Time Blowup for Navier–Stokes" Euler OpenAI 2026`
4. `Terence Tao September 7 2026 OpenAI Navier Stokes swarm`
5. `site:openai.com/index/sharing-ai-progress-in-mathematics/ "Sharing AI progress in mathematics"`
6. `site:github.com/openai/math README changelog manuscripts metadata 722 372 17 Lean`
7. `site:claymath.org Navier Stokes OpenAI September 11 2026 statement`
8. `site:dwarkesh.com/p/noam-brown transcript Navier Stokes multi-agent 10% September 2026`
9. `site:openai.com/index/navier-stokes-solution/ "88 hours" OR "2.7 million" OR "4.9 million" OR "616,000" OR "Comparator"`
10. `github openai math "722" "372" manuscripts`
11. `github openai NavierStokesAndEuler metadata Lean formalization`
12. `site:terrytao.wordpress.com/2026/09/07 "Finite time blowup with smooth forcing term"`
13. `site:github.com/openai/NavierStokesAndEuler/blob/main/formalization.yaml "sorry" OR "axioms" OR "lines" OR "review"`
14. `site:github.com/openai/math "single prompt" "significant" "4,000" "17"`
15. `site:github.com/openai/math changelog "October 7" "Weil" "162" "300"`
16. `OpenAI Navier Stokes Dan Roberts pollinates Mark Chen Sebastien Bubeck cost millions dollars roles researchers humans September 2026`
17. `https://github.com/openai/math README CHANGELOG statistics attempted problems Lean formalizations October 7 2026`
18. `site:claymath.org/news/navier-stokes-announcement/ "OpenAI" "appears" "Full Statement"`
19. `("agmai.org" recommendations "September 29" 2026) OR ("arXiv:2610.08144" "Lemma 8.6")`
20. `Scientific American Nature OpenAI Navier Stokes swarm divergence groups Buckmaster Alpöge September 7 2026 sessions 722 manuscripts`
