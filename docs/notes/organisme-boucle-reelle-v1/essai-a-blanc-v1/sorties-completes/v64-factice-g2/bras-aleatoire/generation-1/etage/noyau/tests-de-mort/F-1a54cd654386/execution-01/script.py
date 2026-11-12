import json, runpy
LOI = '{"biais":[0.0,0.0,0.0],"poids":[[-0.216072,-0.326696],[-1.464201,1.567505],[-0.5152,-1.560019]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
