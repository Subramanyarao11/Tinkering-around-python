import requests

response = requests.get('http://api.open-notify.org/astros.json')
# print(type(response))
res_json = response.json()
# print(res_json)

# Priniting Data from  response of API

for people in res_json['people']:
    print(people['name'])
