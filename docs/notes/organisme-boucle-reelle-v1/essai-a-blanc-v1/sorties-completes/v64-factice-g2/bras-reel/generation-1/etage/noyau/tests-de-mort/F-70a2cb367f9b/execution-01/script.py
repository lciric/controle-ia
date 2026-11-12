import json, runpy
LOI = '{"biais":[0.120625,0.263705,-0.384331],"poids":[[0.574151,-0.373317],[-1.522319,3.230412],[0.948168,-2.857095]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
