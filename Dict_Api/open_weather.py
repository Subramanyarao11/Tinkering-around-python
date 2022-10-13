import requests

# Feel free to use this API Key
api_key = "b045804ab93431828b3e101e2be26dc1"
city = "Bangalore"
url = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    city+"&appid="+api_key+"&units=metric"

req = requests.get(url)
res = req.json()
# print(res)

description = res.get("weather")[0].get("description")
print("Today's Forecast is", description)
min_temp = res.get("main").get("temp_min")
max_temp = res.get("main").get("temp_max")
print("Today's Minimum Temperature is", min_temp)
print("Today's Maximum Temperature is", max_temp)
