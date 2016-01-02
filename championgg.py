#3f3a40029c5d36b3ec472b56909f44fd

import requests
import json

r = requests.get('http://api.champion.gg/champion?api_key=3f3a40029c5d36b3ec472b56909f44fd')

# r.json()

# print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))

with open('data.txt', 'w') as outfile:
    json.dump(r.json(), outfile)

#print(r.json())

#print(r.url)

