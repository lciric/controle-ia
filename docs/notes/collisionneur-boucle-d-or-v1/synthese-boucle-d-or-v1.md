# « Boucle d'or » (fenêtre de distance entre parents, allocation des expériences) — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 27 octobre 2026 à partir des neuf cellules du tour (GO-2026-10-27-02 ; branche `donnees/collisionneur-boucle-d-or-v1`, commit `fd91612` ; empreintes compagnon des cellules revérifiées). Matériau de décision, jamais une consigne. **Rien d'opposable** (R7) : aucun chiffre de la littérature n'est vérifié sur PDF empreinté, et les chiffres des modèles sont « illustratifs ».
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Trois tours (conception, équipe rouge croisée, riposte), neuf cellules valides, aucun refus, 8,60 USD.
- **Pièces** : A, P, R1, R2, T et C ont été servies. **P n'a été servie que pour son plan, sans ses résultats** ; aucun modèle n'en invente. Pièce signalée absente par B et C (T1-B, T1-C, T2-B, T3-C) : la réponse d'origine de Gemini et son script (`2784138…`), qui ne sont pas versés.

## Verdict en cinq lignes

1. **Les trois rejettent la fenêtre fixe [0,12 ; 0,26] comme règle.** Elle ne teste jamais hors de sa bande, donc ne peut pas apprendre qu'elle a tort. Sa bande n'est étalonnée sur rien, et la similarité de domaine s est instable et manipulable à coût nul. Au mieux, elle sert d'a priori réversible.
2. **Ils rejettent aussi l'entropie du verdict comme objectif.** Le score « H₂ × 4p(1−p) » classe exactement comme |p − ½|, et il récompense les filles rendues incertaines exprès. Ils proposent à la place l'espérance de découvertes vraies par dollar, avec une exploration apprise.
3. **Première expérience, commune aux trois : éprouver le juge d'abord.** On l'oppose à des tricheurs, dont « parent + loi aveugle ». Processeur seul, 0 USD, quelques minutes. Si un tricheur passe, on arrête tout. C'est le même principe que dans les deux tours précédents.
4. **Le plan P, déjà scellé, a des défauts que les trois trouvent séparément** : grille désalignée, comparateur choisi après coup, aucun plafond. Ses résultats se liront avec ces réserves. B propose de les corriger dans un addendum scellé à part.
5. **Aucune courbe en cloche n'est établie dans la littérature**, citée de mémoire et à vérifier. Ce qui revient, c'est une variance qui croît avec la nouveauté, mesurée sur des citations, jamais sur la vérité. La bonne variable reste ouverte.

## Convergences

- **Le juge passe avant tout.** « C'est le juge qui écarte les triviales » est une propriété de conception, jamais mesurée. La batterie de tricheurs de R1 est « en cours », et P exclut par décret le trou « parent + loi aveugle » (T1-A a2, T1-B a1, T1-C 1.1.2). La fille composite des équipes rouges franchit la fenêtre, les variables et l'entropie ; seul un juge sans trou, sur des tirages non vus, l'arrête (T2-A, T2-B, T2-C ; acceptée par les trois en T3).
- **Uzzi et collègues (2013) ne répondent pas à la question.** L'étude croise conventionnalité et nouveauté dans les références d'*un* article. Elle ne trace pas de courbe sur la distance entre *deux* parents (T1-A a9, T1-B a5, T1-C 1.2).
- **La grille de P favorise la fenêtre.** Ses cases de 0,1 sont à cheval sur la bande ; elles valent 0,41 et 0,32, contre 0,5 dans la fenêtre. Dans le monde « cloche », P mesure donc la grille (T1-B b0.3, T1-C exp. 1). Les trois ajoutent un Thompson à grille alignée, un comparateur fixé d'avance et un oracle continu comme plafond (T2-A c5, B4 ; T3-A, T3-B, T3-C).
- **La perte est asymétrique.** Une fenêtre fausse coûte sans borne et sans correction possible ; écarter une fenêtre juste ne coûte qu'un regret d'exploration (T1-A, T1-B, T1-C, question 5). Ce regret n'est borné que si l'apprentissage converge, ce qu'il faut mesurer avec 40, 80 et 160 tests (T2-A B9, accepté en T3-B).
- **La rétrodiction T ne voit qu'une cooccurrence lexicale.** Son support est tronqué : voisin commun obligatoire, aucune cooccurrence avant. Une relation monotone peut donc y fabriquer un pic (T2-C a5, repris en T3-A et T3-B). Pour mesurer l'impact par les citations, il faut OpenAlex avec une clé, ce qui reste ta décision (pièce A, T1-A, T1-B).

## Divergences et questions ouvertes

- **Ce qui remplace la fenêtre.** A : un a priori informé, sous une règle d'admission (n'entre dans l'allocation qu'une grandeur calculée hors des agents ou observée après paiement, T3-A). B : un a priori réversible fort, avec espérance et gradient de connaissance (T3-B). C : un Thompson structuré à trois paramètres ou à grille alignée (T3-C).
- **La bonne variable.** A : la synergie des parents, sur les tirages déjà payés de leurs propres tests (T3-A). B : quatre variables des parents gelés, testées sur un lot uniforme réservé, dans le pôle réel (T3-B E4′). C : ancrage d'opérateur pondéré par la rareté × orthogonalité des erreurs des parents (T3-C) ; A et B tiennent ces étiquettes pour manipulables (T2-A, T2-B). Désaccord sur ce qu'une simulation peut trancher : pour B, la variable que le monde encode gagne ; pour A, elle ne mesure que l'instrument.
- **Quel juge éprouver ?** C teste un juge durci : mélange « parent + bruit » dans le nul, strates fixes, correction de Holm (T3-C exp. 0). A et B éprouvent le juge v1 tel quel. Durcir le juge en fait une nouvelle version : il faudra la sceller, et ce n'est pas valider v1.
- **Le coût d'une fenêtre fausse** : −74 % contre le hasard dans le monde « bords » pour C ; de 0,26 à 0,56 fois le hasard pour B. Pour A, le coût dominant est ailleurs : une entrée écrite par les agents laisse un tricheur capter tout le budget (T3-A, T3-B, T3-C).

## Ce que l'équipe rouge a abattu ou fait corriger

- **Validation du juge.** La règle de B était inatteignable pour un juge exactement au niveau α (T2-A B1, T2-C a6) ; elle passe à une marge d'équivalence, avec correction de Holm et témoin « nul exact » (T3-B). Une liste figée de tricheurs ne valide qu'une liste : les trois ajoutent une famille adaptative et une garde « juge fuyant » (T2-A B2). A avait oublié « parent + loi aveugle » (T2-B A8).
- **Fuite par les tirages de calibrage du juge**, où A, B et C calculaient la synergie (T2-A B7, T2-B A4, T2-C a1). Les trois l'acceptent : tirages disjoints et facturés.
- **Résultats acquis par construction**, que chacun corrige : le duel 1 de A suivait la loi choisie pour le centre de la bande (T2-B A1, T2-C 2) ; l'a priori faible de B dominait par définition (T2-A B3) ; le criblage de C était un mini-test du juge, sans coût de fusion (T2-B C5).
- **Courbe en cloche.** La régression quadratique de B voyait une cloche dans toute courbe monotone qui sature (T2-A B6, T2-C a3). On compare désormais une régression unimodale à une isotone, et l'on injecte une courbe monotone comme témoin. La distance qui recopie le voisinage du score d'allocation de ressources est écartée (T2-A B5, T2-B A5).
- **C** confondait vérité et probabilité de promotion (T2-A C5, T2-B C1) : il ajoute deux régimes de puissance et une fenêtre gloutonne, et retire « prouve », « contient exactement », « non détectable ». **A** retire son objectif de sévérité comme parade : une force déclarée gonflée le trompe (T2-C b1, T2-B A7).
- **Intégrité.** A étiquetait « VÉRIFIÉ » des références citées de mémoire, et C les donnait pour « RAPPORTÉ ». Les deux corrigent en « référence à vérifier » (T2-B ; T3-A §0, T3-C).
- **Attaques rejetées, avec raison** : « la fille mémorise les tirages » (non, la fiche est gelée avant, T3-B) ; « l'orthogonalité est acquise par construction » (non, la loi neuve appartient à la fille, T3-C).

## Première action recommandée (les trois)

**Éprouver le juge contre des tricheurs, avant tout allocateur** (T3-A duel 0, T3-B E0′, T3-C exp. 0).
- Batterie : les tricheurs de R1, « parent + loi aveugle », un mélange dilué et une famille adaptative.
- Contrôles : un nul exact, une garde « juge fuyant » et la puissance sur les filles vraies. Sans puissance, un juge frileux passe sans rien prouver.
- Coût : processeur seul, 0 USD, de 30 secondes à moins d'une heure (1 700 à 2 000 mondes par forme, illustratif).
- **Critère d'arrêt** : un tricheur au-dessus de α plus la marge (0,01 à 0,015, illustratif). On n'évalue alors aucun allocateur, et le juge est à refaire.

Ensuite, l'addendum à P, scellé à part (T3-B b0′). Puis la rétrodiction sur les fichiers de T, sans réseau.

## Réserves

- Toute la littérature est citée de mémoire (Fleming, Wang, Foster, Bromham, Frazier, Simonsohn, entre autres). Les chiffres d'Uzzi ne sont connus que par transcription. Rien n'est utilisable avant vérification sur PDF empreinté.
- Seuils, tailles et gains sont illustratifs. Ils sont à fixer dans un préenregistrement scellé et contre-lu (R1, R2).
- Même corrigées, les simulations encodent leurs hypothèses (T2-B A3). La rétrodiction ne porte que sur des mots et sur deux couples de champs : math et physique, informatique et physique.
- Modifier le juge figé se décide et se scelle ; le collisionneur ne le décide pas.
