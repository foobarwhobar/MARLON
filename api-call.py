import requests

import json_normalize
ourVariable = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast').json_normalize()

print(ourVariable)

