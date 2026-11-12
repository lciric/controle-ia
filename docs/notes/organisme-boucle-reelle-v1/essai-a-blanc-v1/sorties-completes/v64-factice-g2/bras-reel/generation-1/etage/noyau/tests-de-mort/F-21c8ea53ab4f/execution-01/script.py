import json, runpy
LOI = '{"biais":[0.104196,0.489026,-0.527475],"poids":[[0.927044,0.390796],[-1.268495,3.405885],[0.972325,-3.375372]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
