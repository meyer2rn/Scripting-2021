import requests
import json

r = requests.get('http://localhost:3000')
data = r.json()

for name in data:
    x = name.get('name')
    y = name.get('color')
    print(x, y)