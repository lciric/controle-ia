import json, runpy
LOI = '{"biais":[0.349725,0.322268,-0.148829],"poids":[[1.107023,-0.300618],[-1.392573,3.383128],[1.837395,-3.160322]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
