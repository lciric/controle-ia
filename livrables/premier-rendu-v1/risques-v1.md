# Risques principaux et parades — v1

Rédigé le 2026-10-04.

## Phase 0

1. **Accès bloqués : sources, modèles, recherche.** arxiv.org, huggingface.co et Vast.ai sont refusés par la politique réseau ; le budget de recherche web est épuisé. Sans PDF empreintés, le critère 8 de G0 ne peut pas être rempli, et T0.5 ne sait pas si le code de Terekhov et al. existe.
   *Parade* : ouverture des domaines et budget relevé (ressources 1 et 2) ; à défaut, PDF déposés à la main. Tout le travail GPU se fait sur des instances Vast.ai, qui ont leur propre accès réseau. Le code se développe ici sur un petit modèle à poids aléatoires, sans téléchargement.

2. **Organismes sans effet mesurable ou sans dose-réponse monotone sur 8B.** Le 8B peut être trop faible pour un sabotage subtil sur l'environnement (a), ou la distillation (ii) peut ne pas transférer la politique de sabotage. Cela touche les critères 2 et 3 de G0.
   *Parade* : pilote dès la session 1 avec cibles semées et vérité terrain préenregistrée ; plan B préenregistré (rubrique simplifiée) ; contrôle de la qualité de la distillation (ii) contre (i) avant tout travail de sondes ; aucun changement de modèle sans GO.

3. **Calendrier.** Quatre semaines, neuf tâches, trois sessions GPU suspendues aux GO. Un GO tardif fait glisser G0.
   *Parade* : tout ce qui tourne sur processeur est prêt avant la session 1 (code testé sur petit modèle, scripts de lancement, préenregistrements) ; travail GPU groupé en sessions ; si un critère de G0 ne peut pas être tenu au 1er novembre, nœud de décision avec options (brief, section 7).

## Programme

1. **Érosion de la nouveauté.** Le champ publie plusieurs préprints pertinents par mois. La recherche du 4 octobre montre déjà :
   - le cœur statistique du lemme est classique ;
   - le théorème négatif est occupé en boîte noire ;
   - le déplacement continu des juges par technique de persuasion est mesuré (2508.07805) ;
   - un voisin de H2 sur les activations d'agents est apparu (2607.06503).

   *Parade* : revendications repositionnées sur ce qui reste (boîte blanche × attaquant à budget × indexation agents × temps × compensation) ; veille hebdomadaire ; bascules pré-engagées ; publication rapide de A (vers M3) et de C (vers M4).

2. **Absence de signal interne exploitable (δ ≈ 0) ou échec de G1.** Le sabotage d'organismes 8B peut ne pas déplacer la marginale des scores de sondes. L'attaquant peut aussi compenser (abaisser ses scores ailleurs), ce que la note mathématique montre rédhibitoire sans dommage structuré.
   *Parade* : les deux issues sont publiables (lemme ou théorème négatif ; résultat négatif + H8) ; le coût de la compensation interne est mesuré explicitement (lien avec HC4 et Tr) ; contrôles croisés et plancher apparié.

3. **Validité externe des organismes et budget.** Des organismes à instruction cachée ou distillés ne sont pas de vrais intrigants : les sondes peuvent apprendre un artefact (« j'ai une instruction cachée »). Les postes lourds (apprentissage par renforcement en phase 1, N = 10 en phase 3) peuvent dépasser le budget.
   *Parade* : test de validité (i)/(ii) dès la v0 ; anti-circularité ; famille (iii) sur 70B en contrôle externe optionnel ; devis par phase avec alerte à 80 % ; leviers de réduction préparés (grille N, périmètre de l'apprentissage par renforcement) ; limites explicites dans les papiers.
