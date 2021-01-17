import requests
from bs4 import BeautifulSoup

url = "https://pogoda.interia.pl/prognoza-szczegolowa-krakow,cId,4970"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

informations = []

weather_box= soup.select("div.weather-currently-middle").pop(0)


selectors = ["div.weather-currently-temp-strict", "li.weather-currently-icon-description", "li.feelTemperature > .weather-currently-details-value", "li.pressure > .weather-currently-details-value", "li.wind span.weather-currently-details-value", "div.kind > .value", "div.pm25 > .value", "div.pm10 > .value"]

# selectors = {
#     "strict_temp": "div.weather-currently-temp-strict",
#     "weath_description": "li.weather-currently-icon-description",
#     "weath_feel": "li.feelTemperature > .weather-currently-details-value",
#     "pressure": "li.pressure > .weather-currently-details-value",
#     "wind_speed": "li.wind span.weather-currently-details-value",
#     "air_qual": "div.kind > .value",
#     "pm25": "div.pm25 > .value" ,
#     "pm10": "div.pm10 > .value"
# }

# weather = dict.fromkeys(selectors,"")

# for key,value in selectors.items():
#     weather[key] = " ".join(weather_box.selet(value).pop(0).text.strip().split())

for selector in selectors:
    informations.append(" ".join(weather_box.select(selector).pop(0).text.strip().split()))



print(f"Temperatura: {informations[0]}\nOpis: {informations[1]}\nTemperatura odczuwalna: {informations[2]}\nCiśnienie: {informations[3]}\nPrędkość wiatru: {informations[4]}\nJakość powietrza: {informations[5]}\nPM 2.5: {informations[6]}\nPM 10: {informations[7]}")
