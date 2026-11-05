# Pilote d'essai — quatre règles de mise à jour de la défense, témoin R0 et mesure X̄ — v2 (racines d'essai 20266501 / 20266502 ; À NE PAS LIRE COMME UN RÉSULTAT)

- Fichier : `pilote-essai-regles-defense-v2.json` — sha256 `9295fa1f6be3fcd2fd73b65d3d8722863c833467ed3dfa15880d85591119a572`
- Code : `9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3` ; arène v4 `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` ; gel `9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3` ; configuration `3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098` ; numpy 2.4.6, scipy 1.17.1, Python 3.13.18
- Commande : `arene_regles_defense_v2.py essai --instances 0:2 --sortie pilote-essai-regles-defense-v2.json --processus 2 --pids pids-pilote-essai-regles-defense-v2.txt --regles R0,R1,R2,R3,R4 --lambdas 0.3 --references moyenne`
- Tâches : 4 (instances × δ), T = 8, variantes : R0, R1, R2, R3, R4[moyenne,λ=0.3] ; λ ∈ [0.3], références ['moyenne'] ; finale légère.

## 1. Temps et extrapolation

- Processeur, somme des tâches : 69 s ; mur : 36 s sur 2 processus ; efficacité (processeur / (mur × processus)) : 0.96.
- Par tâche (5 variantes) : moyenne 17.3 s, min 15.8 s, max 18.7 s (plafond interne 600 s).

| Variante | processeur trajectoire (s, moyenne) | processeur finale (s) | appels optimiseur | programmes linéaires | entraînements | départs attaquant |
|---|---|---|---|---|---|---|
| R0 | 0.75 | 1.27 | 127 | 0 | 0 | 127 |
| R1 | 1.33 | 1.28 | 167 | 0 | 8 | 127 |
| R2 | 1.55 | 1.22 | 198 | 0 | 8 | 127 |
| R3 | 2.44 | 4.16 | 192 | 35 | 8 | 127 |
| R4[moyenne,λ=0.3] | 1.76 | 1.41 | 198 | 0 | 8 | 127 |

- Hors variantes (contexte, M0, lois tenues) : ≈ 0.1 s par tâche.
- **Extrapolation à N = 100 par δ (200 tâches)** :
  - décision à 5 variantes (R0, R1, R2, R3, R4 à λ*) : 17.3 s par tâche → 58 min de processeur ; mur sur 2 processus : 29 min à efficacité 1, 30 min à l'efficacité mesurée 0.96 ; sur 4 processus à efficacité 1 : 14 min.
  - toutes les variantes présentes dans ce pilote : 17.3 s par tâche → 58 min de processeur ; mur sur 2 processus : 29 min à efficacité 1, 30 min à l'efficacité mesurée 0.96 ; sur 4 processus à efficacité 1 : 14 min.

## 2. X̄ et R0 sortent-ils ? Les mesures bougent-elles ? (moyennes sur 2 instances par δ ; bruit non opposable)

### δ = 1.4 (code 1, n = 2)

| Variante | V final (iii) | X = 1 − V | **X̄ (moyenne des tours)** | (ii) tenues final | (i) vus | fausses alertes | I1 | I3 − nul | cos consécutif | valeur jeu restreint | poids purs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R0 | 0.1024 | 0.8976 | 0.8955 | 0.5154 | 0.1045 | 0.0106 | +0.0004 | -0.068 | 1.000 | — | — |
| R1 | 0.1057 | 0.8943 | 0.9147 | 0.5038 | 0.3299 | 0.0093 | +0.0059 | +0.265 | -0.250 | — | — |
| R2 | 0.0731 | 0.9269 | 0.9015 | 0.3989 | 0.2928 | 0.0092 | +0.0082 | +0.265 | 0.351 | — | — |
| R3 | 0.2126 | 0.7874 | 0.8470 | 0.3720 | 0.2534 | 0.0096 | +0.0562 | +0.099 | 0.188 | 0.232 | 0.00 |
| R4[moyenne,λ=0.3] | 0.1134 | 0.8866 | 0.8895 | 0.5014 | 0.1534 | 0.0101 | +0.0043 | +0.015 | 0.954 | — | — |

(iii) par tour, moyenne :

- R0 : 0.104, 0.106, 0.102, 0.105, 0.103, 0.106, 0.104, 0.106
- R1 : 0.108, 0.056, 0.103, 0.062, 0.112, 0.066, 0.110, 0.064
- R2 : 0.103, 0.103, 0.105, 0.067, 0.100, 0.108, 0.116, 0.087
- R3 : 0.104, 0.055, 0.196, 0.144, 0.208, 0.143, 0.212, 0.162
- R4[moyenne,λ=0.3] : 0.106, 0.105, 0.103, 0.118, 0.117, 0.109, 0.109, 0.116

(ii) par tour, moyenne :

- R0 : 0.515, 0.515, 0.515, 0.515, 0.515, 0.515, 0.515, 0.515
- R1 : 0.515, 0.387, 0.503, 0.396, 0.503, 0.400, 0.504, 0.398
- R2 : 0.515, 0.506, 0.492, 0.402, 0.487, 0.497, 0.498, 0.482
- R3 : 0.515, 0.387, 0.421, 0.407, 0.431, 0.345, 0.395, 0.367
- R4[moyenne,λ=0.3] : 0.515, 0.513, 0.513, 0.508, 0.510, 0.512, 0.509, 0.509

R3′ (valeur du jeu restreint par tour, les deux joueurs à l'équilibre) : 0.104, 0.235, 0.219, 0.226, 0.221, 0.236, 0.230, 0.232

Contrastes appariés contre R2 (moyenne [B2 = q0,00625 ; q0,99375], 20 000 rééchantillonnages, n = 6 : intervalles larges, non opposables) :

| Contraste | V (iii) | (ii) | X̄ | écart standard seul − renforcé seul (sur V) |
|---|---|---|---|---|
| R0 − R2 | +0.0294 [-0.0208 ; +0.0795] | +0.1164 [+0.0127 ; +0.2202] | -0.0060 [-0.0149 ; +0.0029] | +0.0011 |
| R1 − R2 | +0.0326 [-0.0186 ; +0.0838] | +0.1049 [-0.0095 ; +0.2193] | +0.0131 [+0.0037 ; +0.0226] | +0.0017 |
| R3 − R2 | +0.1395 [+0.1078 ; +0.1712] | -0.0269 [-0.1092 ; +0.0553] | -0.0546 [-0.0618 ; -0.0474] | -0.0003 |
| R4[moyenne,λ=0.3] − R2 | +0.0403 [-0.0041 ; +0.0847] | +0.1025 [-0.0133 ; +0.2182] | -0.0120 [-0.0174 ; -0.0066] | -0.0006 |

Contrôles : entraînements 68, non convergés 0 ; départs de l'attaquant 1270, non finis 0, réponses à la limite 0 ; processeur par tâche moyenne 16.2 s, max 16.6 s.

### δ = 1.6 (code 2, n = 2)

| Variante | V final (iii) | X = 1 − V | **X̄ (moyenne des tours)** | (ii) tenues final | (i) vus | fausses alertes | I1 | I3 − nul | cos consécutif | valeur jeu restreint | poids purs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R0 | 0.0451 | 0.9549 | 0.9542 | 0.5279 | 0.0458 | 0.0092 | -0.0005 | +0.099 | 1.000 | — | — |
| R1 | 0.0404 | 0.9596 | 0.9646 | 0.5123 | 0.2998 | 0.0088 | +0.0028 | +0.265 | -0.284 | — | — |
| R2 | 0.0471 | 0.9529 | 0.9606 | 0.5178 | 0.2580 | 0.0092 | -0.0070 | +0.182 | 0.185 | — | — |
| R3 | 0.1439 | 0.8561 | 0.8826 | 0.3443 | 0.2266 | 0.0091 | +0.0819 | +0.182 | 0.343 | 0.201 | 0.00 |
| R4[moyenne,λ=0.3] | 0.0512 | 0.9488 | 0.9509 | 0.4964 | 0.1273 | 0.0080 | +0.0024 | -0.235 | 0.937 | — | — |

(iii) par tour, moyenne :

- R0 : 0.049, 0.046, 0.045, 0.045, 0.045, 0.045, 0.046, 0.046
- R1 : 0.046, 0.017, 0.044, 0.029, 0.046, 0.030, 0.042, 0.030
- R2 : 0.048, 0.052, 0.024, 0.048, 0.033, 0.046, 0.035, 0.030
- R3 : 0.046, 0.018, 0.144, 0.098, 0.144, 0.156, 0.154, 0.180
- R4[moyenne,λ=0.3] : 0.045, 0.051, 0.050, 0.045, 0.051, 0.050, 0.053, 0.048

(ii) par tour, moyenne :

- R0 : 0.528, 0.528, 0.528, 0.528, 0.528, 0.528, 0.528, 0.528
- R1 : 0.528, 0.362, 0.518, 0.386, 0.513, 0.388, 0.508, 0.387
- R2 : 0.528, 0.501, 0.397, 0.496, 0.471, 0.467, 0.479, 0.389
- R3 : 0.528, 0.367, 0.400, 0.320, 0.402, 0.381, 0.403, 0.389
- R4[moyenne,λ=0.3] : 0.528, 0.511, 0.505, 0.514, 0.519, 0.493, 0.496, 0.516

R3′ (valeur du jeu restreint par tour, les deux joueurs à l'équilibre) : 0.046, 0.208, 0.195, 0.214, 0.204, 0.199, 0.198, 0.189

Contrastes appariés contre R2 (moyenne [B2 = q0,00625 ; q0,99375], 20 000 rééchantillonnages, n = 6 : intervalles larges, non opposables) :

| Contraste | V (iii) | (ii) | X̄ | écart standard seul − renforcé seul (sur V) |
|---|---|---|---|---|
| R0 − R2 | -0.0020 [-0.0044 ; +0.0004] | +0.0101 [-0.0006 ; +0.0208] | -0.0064 [-0.0194 ; +0.0065] | -0.0009 |
| R1 − R2 | -0.0068 [-0.0099 ; -0.0037] | -0.0055 [-0.0094 ; -0.0015] | +0.0040 [+0.0021 ; +0.0059] | -0.0022 |
| R3 − R2 | +0.0968 [+0.0762 ; +0.1174] | -0.1735 [-0.1811 ; -0.1659] | -0.0780 [-0.0925 ; -0.0636] | -0.0016 |
| R4[moyenne,λ=0.3] − R2 | +0.0041 [-0.0123 ; +0.0205] | -0.0214 [-0.0230 ; -0.0199] | -0.0097 [-0.0168 ; -0.0027] | -0.0002 |

Contrôles : entraînements 68, non convergés 0 ; départs de l'attaquant 1270, non finis 0, réponses à la limite 0 ; processeur par tâche moyenne 18.3 s, max 18.7 s.

## 3. Variante de R4 présente (λ* et référence NON rechoisis en v2 : gel v2 § 3, valeurs du pilote v1)

- Règle : max de la moyenne de V sur toutes les tâches ; égalité à la tolérance près → plus petite λ, puis « dernier » ; tolérance 0.005.
- Moyenne de V(R4) par variante : R4[moyenne,λ=0.3] 0.0823
- **Retenu : R4[moyenne,λ=0.3]** (λ = 0.3, référence « moyenne »). Cosinus consécutif moyen de la variante retenue : 0.954, 0.937 (δ 1 ; δ 2).

## 4. Réserves de lecture

- Racine d'essai v2, 2 instances par δ : rien ici n'est opposable ; aucune prédiction du préenregistrement n'en est tirée ; ce pilote vérifie seulement que X̄ et R0 sortent (zéro entraînement, 7 paramètres), qu'aucune garde ne se déclenche, et mesure le temps à 5 variantes.
- R0 : cosinus consécutif 1 et I2 = 0 par construction (M0 jamais réentraîné) ; hors S12.
- Cosinus consécutif moyen par tâche de la variante de R4 (lu par le lecteur R13 pour S12) : δ 1.4 : [0.998, 0.911] ; δ 1.6 : [0.976, 0.899]
