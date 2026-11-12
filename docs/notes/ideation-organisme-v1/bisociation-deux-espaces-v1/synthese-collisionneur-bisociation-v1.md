# Synthèse du collisionneur — recombinaison bisociative à deux espaces — v1

**Auteur** : sous-agent neuf (Opus 5.5), n'a écrit aucune pièce lue. Rédaction le 2026-10-29 à 23:45 UTC (`date -u`). Aucun commit.
Rien d'autre n'a été ouvert que les pièces ci-dessous, leurs `.sha256` et la synthèse de la question-mère v2 (format).
**Matériau pour un préenregistrement (R1) ; ne tranche rien ; tout chiffre est exploratoire et renvoie à une cellule.**

**Pièces.** Toutes lues par `git show` sur `origin/donnees/collisionneur-bisociation-v1`, dossier `donnees/collisionneur-bisociation-v1/`.
Chaque empreinte recalculée est égale à son compagnon `.sha256`.

| Pièce | Empreinte (début) | Lignes |
|---|---|---|
| `question-bisociation-deux-espaces-v1.md` | `73a30ab727445969` | 64 |
| `faits-bisociation-v1.md` | `0045b0384256a3a3` | 668 |
| `E3-T1-conception-A.md` / `-B` / `-C` | `dcbd2660be70b992` / `717440fe4d51b3d6` / `eae9becf73928141` | 135 / 295 / 219 |
| `E3-T2-redteam-A.md` / `-B` / `-C` | `0b14000d98a25583` / `ed568033a442d356` / `5bb9334d6a3af818` | 118 / 162 / 106 |
| `E3-T3-riposte-A.md` / `-B` / `-C` | `4283d5cec5247511` / `f4659f8f53c3b535` / `d81a8f9d547ccf2d` | 142 / 210 / 141 |
| `argon-a-part/reponse-argon-v1.json` (champ `texte`) | `9b458a7b2601b635` | 165 (texte) |

Cellules sous `run-bisociation-e3-v1/cellules/`, notées T1-A … T3-C ; A = Fable 5.1, B = Opus 5.5, C = Gemini Argon. « l. n » = ligne n
de la cellule ; « Argon l. n » = ligne n du champ `texte`.

**Critères gelés appliqués** (question, l. 57-64) : objectif « commun » seulement si deux modèles au moins donnent la même forme
mathématique (même composition des noyaux, même rôle de la qualité) ; représentation exigeant un juge-modèle dans la boucle de tirage
marquée « juge dans la boucle » ; test auquel manquent ses témoins (stratifié, v6.3, Swanson) **ou** un seuil d'adoption gelé = « non préenregistrable » ;
avis d'Argon et de l'Opus neuf lus à côté, non comptés. Hors objectif, j'applique par analogie « deux modèles au moins, même
définition opérationnelle ». A et B sont de même famille : un accord A + B seul est plus faible.

---

## 1. Verdict

1. **Objectif : divergent au sens gelé.** Les trois s'accordent sur le diagnostic (terme d'éloignement inopérant dans le volume ;
   proximité conceptuelle possible seulement dans le score d'une **paire** ; q retirée), mais pas sur la forme : score par strate sans
   déterminant (A, B) contre déterminant sur les paires (C) ; facteurs de domaine et de concept différents.
2. **Aucun test n'est préenregistrable en l'état** : tous les seuils sont « illustratifs » ; chez C, le témoin v6.3 manque à
   l'expérience décisive du tour 3. A et B le deviennent dès qu'un seuil est gelé.
3. **Dix divergences** ; le signe voulu par Lazar (« minimise ») est relevé par les trois et doit être levé avant écriture.

---

## 2. Ce qui est commun (état final, tour 3)

| # | Élément | A | B | C |
|---|---|---|---|---|
| 1 | « Minimiser le produit scalaire » est contenu dans « maximiser le volume » en signe, inopérant en force aux cosinus mesurés (pénalité 0,6 % à cos 0,28) : terme à part nécessaire | T1-A l. 29, 39 ; T3-A l. 128 | T1-B l. 66-72 ; T3-B l. 188 | T1-C l. 26-29 ; T3-C l. 125 |
| 2 | Hors diagonale, une similarité est une répulsion ; la proximité conceptuelle n'entre que dans le score d'une paire ; ensemble de base = paires valides | T1-A l. 29-39 | T1-B l. 84 ; T3-B l. 186 | T1-C l. 13, 29 ; T3-C l. 127 |
| 3 | q exclue des tests synthétiques (q indépendante de la vérité) | T3-A l. 16, 53 | T3-B l. 17, 62 | T3-C l. 24 |
| 4 | Un bras « meilleure paire par strate, score produit, sans déterminant » | T3-A l. 17, 57 | T3-B l. 66 (forme retenue) | T3-C l. 112, 140 |
| 5 | Placebo de concepts par permutation conservant fréquences et paires valides | T3-A l. 66 | T3-B l. 30, 75 | T3-C l. 59, 99 |
| 6 | Séparabilité mesurée sur les **paires**, en excès sur l'oracle latent, loi nulle par permutation | T3-A l. 105-106 | T3-B l. 119-120 | T3-C l. 16 |
| 7 | Contrôle de queue (part de même domaine ou champ parmi les plus forts C_ij) et jumelles à vocabulaire de domaine substitué | T3-A l. 107-108 | T3-B l. 119, 127 | T2-C l. 102-105 |
| 8 | Réglages jamais sur les mondes de décision | T3-A l. 69 (graines de calibrage) | T3-B l. 69-70 (a priori, sans pilote) | T3-C l. 53 |
| 9 | b_eloigne (ou sa version observée) et Swanson ajoutés aux témoins | T3-A l. 21, 68 | T3-B l. 75 | T3-C l. 91, 139 |
| 10 | Course 2 non jugeable au budget d'une course ; lecture descriptive ou pilote | T3-A l. 112-114 | T3-B l. 169-170 | T3-C l. 30 |
| 11 | Le juge K1-K5 de la pièce C n'est pas un oracle de promotion | T2-A l. 85 | T2-B l. 101-103 | T3-C l. 28 |
| 12 | Le signe du mot de Lazar contredit l'hypothèse de travail | T1-A l. 17 ; T3-A l. 43 | T1-B l. 18-22 ; T3-B l. 195 | T3-C l. 32 |
| 13 | Homonymes rares (rareté indépendante du statut de pont) | T3-A l. 64 | mondes « compte »/« rareté », T3-B l. 84-85 (autre forme) | T3-C l. 49, 105 |
| 14 | Plan factoriel distance × concept × sélection, à même forme fonctionnelle | T3-A l. 87 | proposé en T2-B l. 91, non repris en T3 | T3-C l. 44-47 |
| 15 | Expérience préalable « le terme de distance est-il opérant ? » (V1) | T3-A l. 73-77, 141 | proposée en T2-B l. 149-153 ; remplacée par β a priori | T3-C l. 78-84 (E0) |

Les éléments 13 à 15 sont communs à A et C (familles différentes) ; B les a inspirés sans les garder sous la même forme.

---

## 3. Divergences

**D1 — Rôle du déterminant.**
- A : à λ = 0, le glouton **est** l'argmax par strate ; la machinerie n'est plus qu'un bras du factoriel (T3-A l. 57, 92, 135).
- B : formalisme déterminantal retiré ; stratification dure, une paire par strate (T3-B l. 66-68).
- C : garde un déterminant sur les paires, S^paire = produit de Schur domaines au carré × concepts, contre « stratifié pondéré » (T3-C l. 72-74, 112-115).

**D2 — Facteur conceptuel.**
- A : cosinus pondéré par une rareté lissée, calculée sur un corpus de calibrage hors vivier (T3-A l. 53).
- B : (ε + C_ij)^α, cosinus pondéré par la rareté, ε = 0,05 (T3-B l. 62-71).
- C : rareté de l'étiquette partagée la plus rare, ou moyenne géométrique des deux plus rares (T3-C l. 71) ; variante « ancrée » à deux marqueurs liés (T3-C l. 106).

**D3 — Facteur de domaine et réglage.**
- A : (1 − s)^β, β fixé sur graines de calibrage (T3-A l. 16, 53).
- B : (1 − D²)^(β/2), β ≈ 17 fixé a priori par la règle « une paire proche pèse la moitié » (T3-B l. 70).
- C : (1 − d²)^(α_D/2), α_D ≈ 17 « a priori par géométrie » (T3-C l. 42), puis dit « calibré sur graines de validation » (T3-C l. 79).

**D4 — Source du vecteur de concepts tiré.**
- A : déclaration sur liste fermée, chaque entrée ancrée à un passage vérifié par programme ; l'étiqueteur tiers ne sert qu'à mesurer (T1-A l. 74 ; T3-A l. 34).
- B : étiqueteur-modèle tiers hors boucle, scellé avant tirage, texte non caviardé ; déclaration en audit seulement (T1-B l. 115-118 ; T3-B l. 42).
- C : déclaration sur liste fermée validée par au moins deux marqueurs formels (expressions régulières) ; plafond de trois retiré (T1-C l. 70, 85 ; T3-C l. 26).

**D5 — Traitement du signe.**
- A : trancher par Lazar avant tout préenregistrement (T3-A l. 43).
- B : idem, première action (T3-B l. 199).
- C : deux branches d'un test symétrique (T3-C l. 32).

**D6 — Contraste décisif et seuil.**
- A : effet principal « concept » ≥ +4, intervalle au-dessus de +1, plus contrôle inversé et homonymes rares ≥ +2 ; adoption ×1,3 sur le stratifié et ≥ b_eloigne-observé − 2, illustratif (T3-A l. 89-93).
- B : Z − Z₀ ≥ δ = 2 dans le monde « compte », équivalence dans le monde « plat », Z_perm nul ; adoption à geler à part (T3-B l. 92-99, 163).
- C : F11 bat F10 et F01, borne inférieure > +1, et F00 de +10 / +5, illustratif (T3-C l. 94) ; règle immédiate : battre b_eloigne et d1_inv de +2,5 (T3-C l. 139).

**D7 — Mondes étendus et contrôle inversé.**
- A : multi-opérateurs, homonymes rares, concepts inversés (étiquette de surface commune) ; vérité par opérateur latent ; témoins reproduits (T3-A l. 59-69).
- B : mondes plat / compte / rareté, condition de jugeabilité Z_oracle − Z₀ ≥ δ ; contrôle inversé par monde « import » à étage relâché (T3-B l. 82-114).
- C : trois niveaux d'observation, homonymes rares à couple d'opérateurs ; concepts inversés = ponts plantés sur les moyeux, chute ≤ −8 (T3-C l. 14, 100, 105).

**D8 — Nombre de mondes.**
- A : 400 de décision et 100 de calibrage ; test sur mondes non nuls si π < 0,5 (T3-A l. 69-71).
- B : 1 200 par condition, sans pilote (T3-B l. 147).
- C : 400 par condition (T3-C l. 65).

**D9 — Première expérience.**
- A : V1, puis V2, E4′, E1′, E3′ (T3-A l. 118, 141).
- B : signe, puis E1′ (T3-B l. 198-202).
- C : E0 + E1 factoriel sur le banc existant (T3-C l. 136-140).

**D10 — Course 2, taille requise.**
- A : environ 300 fusions par bras pour +10 points (T3-A l. 114).
- B : environ 160 par bras (T3-B l. 169).
- C : au moins 128 par bras (T3-C l. 30).

---

## 4. Ce que le tour 2 a abattu ; ce que le tour 3 a sauvé ou concédé

| Cible | Critique (tour 2) | Réponse (tour 3) |
|---|---|---|
| A, vérité plantée par le score (E1 vrai par construction) | T2-B l. 17-21 ; T2-C l. 11-13 | Concédée : vérité par opérateur latent, V2 de B reprise (T3-A l. 15, 79-83) |
| A, (1 − s)^β écrasé par q | T2-B l. 23-28 | Concédée : η = 0 (T3-A l. 16) |
| A, O-paires = argmax par strate ; coupure à 25 % = fuite | T2-B l. 30-32 ; T2-C l. 15-17, 29-31 | Concédées : DPP réduit à un bras, coupure supprimée (T3-A l. 17, 32, 57) |
| A, séparabilité linéaire aveugle ou rejetant l'honnête | T2-B l. 40-44 ; T2-C l. 37-39 | Transformée : E4′ (T3-A l. 19, 37, 101-110) |
| A, ancrage par chaîne | T2-C l. 23-25 | **Rejetée pour moitié** : R3 vérifie un passage, non une chaîne (T3-A l. 34) |
| A, E5 confondue et sous-puissante | T2-B l. 46-49, 65 ; T2-C l. 41-43 | Concédée : pilote de calibrage (T3-A l. 112-114) |
| B, q confondante | T2-A l. 13-14 | Concédée : q retirée (T3-B l. 17) |
| B, noyau K inerte (8,5 %) | T2-A l. 28-29 ; T2-C l. 60-66, 82-85 | Concédée sur le fond ; « inversion de signe » **rejetée** ; DPP retiré (T3-B l. 40, 68) |
| B, E2 vide sans moyeu ; E3 trivial | T2-A l. 16-20 | Concédée : mondes croisés, étage relâché (T3-B l. 18-19) |
| B, TOST mal dimensionné | T2-C l. 94-96 | Concédée : 1 200 mondes (T3-B l. 46, 147) |
| B, E5 sur le mauvais canal ; fuite de domaine dans R2 | T2-A l. 25-26 ; T2-C l. 72-74 | Transformées : manipulation textuelle, jumelles ; caviardage **refusé** (T3-B l. 21, 42) |
| C, mondes vrais par construction ; Mantel sans base | T2-A l. 62-66 | Concédées (T3-C l. 13-16) |
| C, volume √(1 − cos²) plat | T2-B l. 82-87 | Concédée : exposant ≈ 17 (T3-C l. 40-42) |
| C, noyau de sommets ; m = 1 ; statuts ; puissance « > 0,99 » ; log W ; homonymes rares ; division par zéro | T2-A l. 69-85 ; T2-B l. 93-131 | Toutes concédées : puissance ramenée à 0,86, ou 0,74 à 0,82 ; log W abandonné (T3-C l. 18-28, 49, 55-59) |

**Reste ouvert, non répondu.** Le noyau S^paire de C (T3-C l. 73) porte la partie domaine en cosinus **au carré** ; l'argument
d'inertie que C opposait au Kronecker linéaire de B (T2-C l. 82-85) s'y applique a fortiori — mon inférence, non testée. Les
« concepts inversés » de C plantent les ponts sur les moyeux (T3-C l. 100) : ce contrôle confond concept et rareté, défaut que B
reprochait aux faux ponts fréquents (T2-B l. 93) — mon inférence. B et C, par deux règles différentes, aboutissent au même exposant
≈ 17 et à la même forme (1 − d²)^(·/2) (T3-B l. 70 ; T3-C l. 42) : convergence non relevée par eux.

---

## 5. L'avis d'Argon à part, lu à côté (non compté)

- **Il n'a pas reçu les pièces** : « le contenu exact des Pièces A, B, C, D n'étant pas joint » (Argon l. 3). Ses chiffres viennent
  du résumé de la question. Il attribue à la pièce D une « mémoire qui refuse les redites » (Argon l. 26, 39) que les trois cellules
  disent absente (T1-A l. 5 ; T1-B l. 5 ; T1-C l. 3).
- **Objectif** : déterminant sur les paires, w_e = √(q_i q_j)·⟨c_i,c_j⟩^α·(1 − ⟨d_i,d_j⟩²)^β, α = β = 1, empreinte croisée
  domaine-de-l'un ⊗ concept-de-l'autre (Argon l. 19-25). Il **garde q** et β = 1 : exactement ce que le tour 2 a abattu (T2-A l. 13-14 ;
  T2-B l. 82-87). Il lit « (a) puis (b) » de Lazar comme ses options 1A et 1C (Argon l. 44) : lecture non vérifiable dans mes pièces.
- **Représentation** : déclaration sur liste fermée validée par extraction syntaxique (Argon l. 74, 88), même famille que A et C ;
  aucun juge dans la boucle. Séparabilité par alignement de noyaux < 0,15 et sonde linéaire ≤ hasard + 10 % (Argon l. 79-85) : les
  deux critères tombent sous les critiques du tour 2 (sans base latente, T2-A l. 65-66 ; aveugle à l'ordre 2, T2-C l. 37-39).
- **Test** : témoins stratifié, v6.3, Swanson et seuil gelé +12 (Argon l. 104-114) : **formellement préenregistrable** au sens du
  critère gelé. Mais la vérité plantée est définie par seuils sur ⟨c_i,c_j⟩ (Argon l. 99) — vrai par construction (T2-B l. 17-21) ;
  b_eloigne, qui fait déjà +11,9 / +6,6 (T2-B l. 124), manque ; aucun placebo de concepts ; puissance « > 99,9 % » (Argon l. 117) du
  type corrigé chez C (T3-C l. 57).
- **Antériorité** : apporte Chan et al. (2018), « SOLVENT » (Argon l. 148), qu'il donne comme la plus proche (but contre mécanisme),
  et Sebastian et al. (2017) (Argon l. 144). À vérifier sur PDF (R7) ; candidat sérieux d'occupation partielle.

**Avis de l'Opus neuf** : non servi ; non lu.

---

## 6. Les quatre points de la question

**1. Objectif.**
- *Établi par les cellules* : terme d'éloignement à part et pondéré (§ 2, él. 1) ; proximité conceptuelle seulement dans un score de
  paire (él. 2) ; q exclue (él. 3) ; un bras « par strate » chez les trois (él. 4). Forme : divergente (D1-D3).
- *Inférence* : socle = « score produit, meilleure paire par strate » ; le déterminant de C n'est qu'un niveau du facteur
  « sélection », à terme de domaine probablement inerte (§ 4).
- *Confiance* : 0,8 sur le socle ; 0,4 sur toute forme particulière.

**2. Représentation des concepts.**
- *Établi* : aucune cellule ne met de juge-modèle dans la boucle ; B emploie un étiqueteur-modèle **hors boucle, scellé avant tirage**
  (T1-B l. 112), admis comme étiquetage au sens gelé, non comme juge ; A et C convergent sur une déclaration fermée ancrée et vérifiée
  par programme (D4). Mesure de séparabilité commune aux trois (él. 6-7).
- *Inférence* : en pôle réel, l'étiquetage de B se rescelle à chaque génération ; appel de modèle, donc devis.
- *Confiance* : 0,65 sur la mesure ; 0,5 sur le choix de source.

**3. Test préenregistré.**
- *Établi* : témoins élargis (él. 9), placebo de concepts (él. 5), q ≡ 1, réglages hors décision (él. 8), homonymes rares (A, C),
  course 2 descriptive (él. 10).
- *Non établi* : seuil gelé (aucun), nombre de mondes (D8), forme du contrôle inversé (D7). Au sens gelé : **non préenregistrable en
  l'état** chez A, B et C ; C n'a plus v6.3 dans son expérience décisive (T3-C l. 89-93).
- *Confiance* : 0,7 sur les contrôles ; 0,4 sur les seuils.

**4. Antériorités.**
- *Établi* : rien. Les trois donnent la forme à deux espaces sur paires comme « question, pas trou » (T1-A l. 118 ; T1-B l. 247, 266 ;
  T3-C l. 34). Toutes les références sont « à vérifier ».
- *Candidats à vérifier d'abord* : Gentner (1983) (T1-A l. 121 ; T1-B l. 249) ; Hope, Chan, Kittur et Shahaf (2017) (T1-B l. 250) ;
  Chan et al. (2018) (Argon l. 148) ; Berthold (dir.) (2012), *Bisociative Knowledge Discovery* (T1-B l. 257) — titre littéralement
  sur la zone revendiquée.
- *Confiance que la zone soit vierge* : 0,3. Zone séduisante, donc à vérifier plus durement (R8).

---

## 7. Recommandation pour le préenregistrement v2

1. **Avant d'écrire** : signe tranché par Lazar (Q1) ; lecture de `monde_v1.py` et `methodes_v1.py` (absents des pièces) pour
   savoir si b_eloigne lit la vérité (T3-A l. 21, 134 ; T3-B l. 32).
2. **Étape 0, gratuite** : V1 sur les mondes existants, q ≡ 1 (T3-A l. 141 ; T3-C l. 78-84).
3. **Étape 1** : factoriel distance × concept × sélection (par strate contre déterminant sur paires), même forme pour chaque terme ;
   mondes plat, multi-opérateurs ou « compte », homonymes rares, concepts inversés de A ; placebos de concepts et de domaine ;
   condition de jugeabilité Z_oracle de B ; témoins stratifié, v6.3, (a′) à budget égal, d1, b_eloigne-observé, O4.
4. **Séparer détection et adoption** : contraste « concept » à forme de domaine fixée (Z − Z₀ de B, avec équivalence) ; adoption
   relative au stratifié et à b_eloigne-observé (A). Seuils gelés avant toute exécution ; nombre de mondes : prendre le plus prudent
   des cellules (1 200, T3-B l. 147) sauf devis contraire.
5. **E4′ avant toute fiche réelle** ; course 2 descriptive seulement ; recherche d'antériorité avant toute revendication.

---

## 8. Questions pour Lazar (défaut sous 48 heures)

**Q1 — Signe de la proximité conceptuelle.** Décision : les parents doivent-ils être proches ou éloignés en concepts ?
- Enjeu : le signe de α et la moitié des contrôles en dépendent (T3-A l. 43 ; T3-B l. 209).
- Options : (a) proches, hypothèse de travail — cohérente avec les conceptions, contredit le mot cité ; (b) éloignés — tout à
  réécrire ; (c) test symétrique (C) — ne présume rien, double les bras.
- Recommandation : (a) confirmé en un mot ; confiance 0,6. Défaut : (c), sur processeur seul.

**Q2 — Forme à tester en tête.**
- Enjeu : le déterminant n'apporte rien par construction à λ = 0 (T3-A l. 57) ; C le garde (T3-C l. 112).
- Options : (a) par strate sans déterminant (B) — simple, répulsion non testée ; (b) déterminant sur paires (C) — terme de domaine
  probablement inerte ; (c) les deux, niveaux d'un factoriel (A, C) — plus de bras, coût négligeable.
- Recommandation : (c) ; confiance 0,7. Défaut : (c).

**Q3 — Seuil d'adoption.**
- Enjeu : +12 absolu est critiqué par les trois (T1-A l. 19 ; T1-B l. 56 ; T1-C l. 108) et quasi hors d'atteinte (T2-B l. 124).
- Options : (a) +12 absolu (question, Argon) ; (b) relatif ×1,3 et ≥ b_eloigne-observé − 2 (A) ; (c) détection Z − Z₀ ≥ δ, adoption
  gelée à part (B).
- Recommandation : (c) pour la détection, (b) pour l'adoption ; confiance 0,55. Défaut : idem.

**Q4 — Source des concepts sur vraies fiches.**
- Enjeu : manipulation et fuite de domaine.
- Options : (a) déclaration ancrée vérifiée par programme (A, C) — gratuite, manipulable par le texte ; (b) étiqueteur-modèle hors
  boucle scellé (B) — appel de modèle par génération, dépense.
- Recommandation : (a) comme mécanisme, (b) comme mesure seulement ; confiance 0,6. Défaut : (a) ; toute part de (b) sur devis.

**Q5 — Course 2.**
- Enjeu : 9 à 12 fusions par bras ne tranchent rien (T2-A l. 87 ; T2-C l. 43).
- Options : (a) lecture descriptive ; (b) budget de 128 à 300 fusions par bras (T3-C l. 30 ; T3-A l. 114) sur devis.
- Recommandation : (a) jusqu'au verdict du banc ; confiance 0,75. Défaut : (a).

---

**Anomalies.** Argon à part sans les pièces (Argon l. 3) ; avis de l'Opus neuf absent ; `methodes_v1.py` et `monde_v1.py` non servis
(T3-A l. 5) ; α_D de C à la fois « a priori » et « calibré » (T3-C l. 42, 79).
