

import requests
longitude = input("enter longitude")
latitude = input("enter latitude")
url = "https://api.open-meteo.com/v1/forecast"

parameater = {"longitude" : longitude,
               "latitude" :latitude,
            "current_weather":True}

response = requests.get(url,parameater)
data = response.json()
#print(data.keys())
#print(data.values())
Windspeed = data ["current_weather_units"]
print(Windspeed)






