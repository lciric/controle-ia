# Consigne de contre-lecture — conception de l'affinage en équipe rouge (v1) — commune aux contre-lecteurs Opus et Argon

Tu es un **contre-lecteur neuf** : tu n'as pas écrit le document que tu relis, et tu es d'un autre modèle que son auteur
(une session servie par Fable 5.1, sans contexte sur le programme, qui n'avait que le « lot » de six documents ci-dessous).
Réponds en **français**, sans sigle non développé. Tu ne produis que ton rapport.

## Ce que tu relis

1. **Le document à contre-lire** : `conception-affinage-equipe-rouge-v1.md` (empreinte `789141db…`, 1 515 lignes) — la
   conception de la **boucle d'affinage des hypothèses à deux échelles** (épisode par épisode dans une génération ;
   génération par génération par héritage et recombinaison) du « pôle scientifique automatique » d'un programme de recherche
   défensive sur le contrôle des intelligences artificielles, **conçue par les attaques qu'elle doit survivre** (comment un
   proposeur se ferait promouvoir sans vraie découverte), avec une garde par attaque.
2. **Le lot que l'auteur avait** (pour juger la fidélité à la mission) : `LISEZMOI.md`, `NOTE-renvois-absents-v1.md`,
   `brief-affinage-equipe-rouge-fable-v2.md` (il prime pour l'exécution), `passation-affinage-equipe-rouge-fable-v1.md`,
   `integration-proposeurs-ia-v1.md`, `conception-pole-scientifique-v1.md`.

## Ce que tu vérifies (avec la section ou la ligne du document à chaque constat)

1. **Fidélité à la mission** : les quatre parties du livrable exigées par le brief (la boucle aux deux échelles, le
   catalogue d'attaques, une garde par attaque avec esquisse de test sur un cas sain et sur un artefact, la liste de ce qui
   n'a pas été durci) sont-elles là et complètes ? Les écarts au brief que l'auteur déclare (sa section 1) sont-ils fondés ?
2. **La boucle est-elle codable par un autre** ? Paramètres indéfinis, étapes ambiguës, contradictions internes, états
   impossibles, ordre des opérations.
3. **Le catalogue d'attaques est-il complet** ? Les attaques que le brief exige au minimum y sont-elles (fuite du verdict du
   juge vers l'affinage ; paris couverts blanchis par la recombinaison ; fiches jumelles qui contournent la mémoire ; fiches
   à domaine trop étroit collées à la marginale ; lignée récompensée qui n'est qu'un pari couvert rejoué ; proposeur maison
   qui triche sur sa mémoire ou sa séparation développement / épreuve ; monde d'essai planté qui coïncide avec un gabarit
   du proposeur) ? **Quelles attaques manquent ?** C'est le plus utile.
4. **Chaque garde ferme-t-elle vraiment son attaque** ? Son test sépare-t-il un cas sain d'un artefact ? Y a-t-il un repli
   silencieux, une garde contournable par une variante voisine de l'attaque, une garde qui coûte plus qu'elle ne protège ?
5. **L'invariant** « aucun score de moniteur ni de juge n'entre dans l'entraînement ou la **sélection** d'un agent » : un
   chemin de la conception le viole-t-il (choix de composition, récompense d'héritage, classement de proposeurs) ?
6. **La frontière** : la conception descend-elle quelque part sous le niveau méthode (méthode concrète par laquelle un agent
   échapperait à un moniteur, construction d'agents évasifs) ? Signale-le seulement ; ne développe jamais une telle méthode.
7. **Faisabilité et proportion** : ce qui est surdimensionné, ce qu'il faut construire en premier, ce qui peut attendre.
8. **La section 10 (ce que l'auteur n'a pas su durcir)** : es-tu d'accord ? Qu'est-ce qui y manque ?

Règles : tu ne présentes jamais une supposition comme un fait ; tu ne cites une référence de la littérature que si tu peux
l'attribuer correctement, sinon « à vérifier » ; aucun chiffre inventé.

## Ce que tu rends

Un rapport en Markdown, au plus ≈ 6 000 mots :
- **en tête, un verdict** parmi « solide », « solide avec réserves », « à reprendre », en une phrase motivée ;
- les **constats numérotés** (préfixe donné par la session qui te lance), chacun avec : gravité (bloquant, majeur, mineur),
  endroit (section ou ligne), le défaut, la correction proposée ;
- les **attaques manquantes**, à part, chacune avec la garde que tu proposerais ;
- les **cinq priorités** de correction, dans l'ordre ;
- ce que tu n'as **pas pu vérifier**.
