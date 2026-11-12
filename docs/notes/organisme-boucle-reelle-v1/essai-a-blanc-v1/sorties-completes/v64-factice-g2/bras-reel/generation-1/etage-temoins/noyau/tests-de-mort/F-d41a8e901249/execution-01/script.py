import json, runpy
LOI = '{"biais":[0.075247,-0.392469,0.412312],"poids":[[0.242523,1.207448],[1.335948,2.912101],[-0.820837,-3.664738]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
