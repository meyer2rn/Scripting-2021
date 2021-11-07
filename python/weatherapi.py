import json
import requests

print('Please enter your zip code:') 
zip = input() 
 
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=9cfc2464423f22f532d5ea011364f5c1' % zip) 
data=r.json() 
print(data['weather'][0]['description'])