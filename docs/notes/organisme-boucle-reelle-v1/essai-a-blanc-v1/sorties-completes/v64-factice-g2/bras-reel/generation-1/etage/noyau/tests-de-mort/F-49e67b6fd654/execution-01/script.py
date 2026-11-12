import json, runpy
LOI = '{"biais":[0.105645,0.310307,-0.402978],"poids":[[0.020837,-1.204996],[-2.541291,3.046929],[0.51264,-3.745715]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
