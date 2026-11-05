# Listes closes de l'axe 6 (texte II) de la course 2 — v1

Lignée session-depot (instance 2), 30 octobre 2026. Ces listes sont écrites et scellées avant le service, comme l'exige le hors-texte de `axe-6-texte-II-v6.md` (`1b301c15…`). Elles servent :
- au critère de mort (ii) ;
- au classement du lecteur tenu à l'écart ;
- aux effectifs transmis à la défense.

Elles ne reprennent rien de BA-002 ni de la v2 en quarantaine (CA6-V2-07). Leurs seules sources sont :
- les exemples de (b), déjà servis dans le texte II ;
- les classes que la contre-lecture de la v1 a proposées (CA6-12), classiques en théorie des tests.

**Règle de classement** (hors texte de la v6) :
- une classe C est dans une case si elle est incluse dans la famille de la case ;
- une hypothèse porteuse est dans une case si elle lui est équivalente, ou si elle en est un cas particulier ;
- une fiche est classée dans la première case qui convient, dans l'ordre ci-dessous, sinon dans « autre » ;
- le lecteur tenu à l'écart tranche, et son classement est scellé.

Les notations sont celles du texte servi : P_0, Q_T, a_t, h, Π, H_Π, S.

## Liste H — hypothèses porteuses

| Case | Définition |
|---|---|
| H1 stationnarité | La loi conditionnelle P_0(a_t \| a_<t), ou la loi d'une fonction fixée de (a_t, h_t), ne dépend pas de t. |
| H2 indépendance conditionnelle entre actions | Sous P_0, les termes par action que S agrège sont indépendants, ou indépendants conditionnellement à une variable déclarée. |
| H3 exhaustivité de Π | Π est exhaustive pour la classe considérée, au sens de la notation du texte servi. |
| H4 linéarité d'un trait | La quantité séparatrice est un trait linéaire ⟨w, h⟩ + b des activations lues. |
| H5 homogénéité des suites de référence | Les n suites de référence sont tirées d'une seule loi P_0, et non d'un mélange de lois de référence distinctes. |
| H6 étalonnage sur n fini | Le seuil s_α, estimé sur n suites, tient le niveau α à l'erreur d'estimation près, annoncée. |
| H-autre | Toute autre hypothèse. Son contenu ne passe pas à la défense. |

## Liste C — classes de déplacements classiques

| Case | Définition (déplacement diffus au sens du texte servi) |
|---|---|
| C1 déplacement de moyenne | Il existe une fonction fixée f de (a_t, h_t) telle que, sous Q_T, la loi de f est celle de P_0 translatée d'un vecteur m_T, avec ‖m_T‖ ≤ ε_T. Les autres moments sont inchangés. |
| C2 mélange | Par action : Q_T(a_t \| a_<t) = (1 − π_T) P_0(a_t \| a_<t) + π_T R_T(a_t \| a_<t), avec R_T une loi déclarée et π_T tel que la condition de diffusion tienne. La contre-lecture de la v1 (CA6-12) disait « à proportion fixe » ; une proportion fixe n'est pas diffuse si R_T reste à distance de P_0, d'où π_T. |
| C3 changement de variance | Il existe une fonction fixée f de (a_t, h_t) telle que, sous Q_T, la loi de f a la même moyenne que sous P_0, et une covariance multipliée par un facteur scalaire (1 + η_T), avec η_T borné par la condition de diffusion. |
| C-autre | Toute autre classe. Son contenu ne passe pas à la défense. |

**Effectifs transmis** (hors texte de la v6) :
- les effectifs marginaux de la liste H et de la liste C, sur les fiches notables, sans le contenu des cases « autre » ;
- jamais le croisement de H et de C.
