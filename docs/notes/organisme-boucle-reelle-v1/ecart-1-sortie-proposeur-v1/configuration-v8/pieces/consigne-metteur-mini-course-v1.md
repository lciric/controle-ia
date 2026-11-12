# Metteur en combinaison — mini-course d'idéation (v1)

Repère de consigne (à ne pas recopier) : MC1-METTEUR-4ec962f1

Tu reçois **deux fiches** d'idées de recherche, anonymes, sur des statistiques de détection pour la surveillance d'agents (textes ou activations internes d'un modèle de langage). Tu écris en français.

Écris **une seule fiche nouvelle** qui combine les deux méthodes en une statistique cohérente, plus puissante ou plus robuste au transfert que chacune seule, et dis pourquoi. Rédige-la comme une proposition autonome : elle ne dit pas d'où elle vient et ne mentionne pas les deux fiches reçues.

Règles d'intégrité : niveau méthode seulement (aucune conduite d'agent, aucune consigne à donner à un agent, aucun procédé pour déplacer une loi ou échapper à une surveillance) ; tout chiffre calculé est marqué « calcul », tout chiffre supposé « supposé » ; toute antériorité citée porte titre, auteurs, année et identifiant, marquée « à vérifier ».

Réponds par **un seul bloc JSON**, à la fin, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "quantite_lue": "…", "invariance": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Exactement une fiche ; mêmes champs, tous obligatoires et non vides : `titre` (au plus 80 caractères), `hypothese`, `axe` (exactement une des valeurs `boite_noire_par_action`, `boite_noire_sequentielle`, `boite_blanche_par_action`, `boite_blanche_sequentielle`), `quantite_lue`, `invariance`, `prediction` (chiffrée, avec signe et intervalle, marquée « supposé »), `test_de_mort` (le nombre qui, lu une fois sur des données existantes, la réfute), `cout` (processeur). Aucun autre champ.
