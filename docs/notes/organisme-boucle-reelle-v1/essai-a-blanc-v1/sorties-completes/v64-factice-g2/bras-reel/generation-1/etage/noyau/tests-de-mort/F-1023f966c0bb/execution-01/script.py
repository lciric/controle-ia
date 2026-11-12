import json, runpy
LOI = '{"biais":[-0.282582,-0.012768,-0.391703],"poids":[[0.190151,0.21294],[-1.566284,1.674372],[0.4718,-3.170206]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
