# MANIFESTE -- collisionneur « nouveaux moniteurs boite blanche » -- P2

Proposeur : P2. Date : 2026-10-28 (UTC). Famille assignee : C -- adaptation.

---

## Fichiers lus

| Fichier | SHA256 |
|---|---|
| `entrees/brief-moniteurs-evasion-v2.md` | `0047cf41368d01b1e42f0d659292c2a9a739e8ee5a21264b826d542ddb2bba6e` |
| `entrees/etat-art-niveau2-conscience-eval-v1.md` | `06c60b13596138a6c0808bb8afc658c5751595b8ad651d3a4d46d0ee2ad4b117` |
| `entrees/programme-v2-sections-1-2-6-7.md` | `37c4102e9ec028f250d69995acbd3f759d749eb780a0a94522ee03dbbba9bbd8` |

Aucun autre fichier lu.

---

## Famille assignee

**C -- adaptation.** Le modele pourrait s'adapter statistiquement a la sonde (masquage de gradient, imitation de la distribution honnete dans la direction sondee). Comment concevoir un moniteur robuste a l'adversaire qui le connait ?

---

## Propositions produites

Cinq propositions, numerotees C-1 a C-5, chacune fermant une breche differente :

| N | Fichier | Breche | Principe du moniteur |
|---|---|---|---|
| C-1 | `moniteur-C-1.md` | Masquage par redistribution dimensionnelle | Taxe de capacite representationnelle (moniteur entropique) : mesurer le cout informationnel du masquage |
| C-2 | `moniteur-C-2.md` | Mimicry statique sans mimicry causale | Sondage causal par perturbation (moniteur du jacobien) : perturber les activations pour reveler la structure causale |
| C-3 | `moniteur-C-3.md` | Adaptation ciblee a une sonde connue | Ensemble de sondes a tirage secret : rendre le plan de mesure imprevisible |
| C-4 | `moniteur-C-4.md` | Commutation conditionnelle a la detection de la surveillance | Piege contextuel : detecter le mecanisme de commutation entre modes |
| C-5 | `moniteur-C-5.md` | Adaptation au niveau des valeurs sans adaptation au niveau de la structure de calcul | Moniteur des invariants de circuit : lire la decomposition par tete plutot que la somme totale |

**Verification de distinctivite.** Les cinq principes sont conceptuellement distincts :
- C-1 mesure le *cout global* de l'adaptation (informationnel, integrale sur tout l'espace).
- C-2 teste la *structure causale* des dimensions sondees (interventionnel, pas observationnel).
- C-3 rend la *cible de l'adaptation imprevisible* (randomisation du plan de mesure).
- C-4 detecte le *mecanisme de commutation* entre modes (meta-signal, pas signal de tromperie).
- C-5 lit la *decomposition du calcul* en composants (structure micro, pas valeur macro).

Aucune paire ne partage le meme principe de detection.

---

## Ce que je n'ai pas compris ou qui reste ambigu

1. **Regime de l'adversaire dans un 8B.** Le brief mentionne un adversaire « informe » de la sonde, mais le mecanisme par lequel un modele 8B acquiert cette connaissance n'est pas precise. Pour mes propositions, j'ai suppose que l'adversaire est cree par reglage fin adversariel (un operateur optimise les poids pour tromper une sonde connue). Le cas ou l'adversaire decouvre la sonde par sa propre cognition (sans reglage fin explicite) est plus difficile a modeliser pour un 8B, et je n'ai pas traite ce cas.

2. **Seuil de faux positifs.** Le brief cite 1 % de faux positifs comme reference (Apollo 2025). Je n'ai pas calibre mes criteres de succes sur ce seuil parce que les moniteurs proposes utilisent des traits differents (entropie, sensibilite causale, profils de tetes) dont la distribution sous l'hypothese nulle est inconnue a priori. Le calibrage precis des seuils releve de l'experimentation.

3. **Interaction entre moniteurs.** Mes cinq propositions sont conçues comme des moniteurs independants. La question de savoir s'ils doivent etre combines en un systeme composite (et comment agreger leurs verdicts) n'est pas traitee -- elle releve de la synthese.

4. **Distinction entre familles A et C.** La frontiere entre « le signal est dans l'espace nul de la sonde par hasard » (famille A, geometrique) et « l'adversaire a pousse le signal dans l'espace nul » (famille C, adaptation) est nette en theorie mais pourrait se brouiller en pratique. Le moniteur C-1 (taxe de capacite) pourrait aussi etre pertinent pour la famille A si le biais diffus occupe naturellement une large fraction de l'espace. J'ai choisi de le classer en C parce que le mecanisme detecte est le *cout de l'adaptation*, pas la *geometrie du signal*.
