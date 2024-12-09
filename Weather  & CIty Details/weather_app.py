import requests
import json
print('*'*30,'Welcome to Weather App ','*'*30)
city = input('Enter city name: ')

url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=sUnRezxbU3VB8USMRp07SQ9Sqhy3pIgm"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

# Converting data to dict
dic = json.loads(response.text)
# Fetching temperature
temperature  = dic['data']['values']['temperature']

# Fetching details about humidirty and wind_speed
humidity = dic['data']['values']['humidity']
wind_speed = dic['data']['values']['windSpeed']

print('Weather Details are given below !')
print(f"Temperature in {city} is {temperature}°C")
print(f"Humidity in {city} is {humidity}%")
print(f"Wind_Speed in {city} is {wind_speed}")
print('Thank you for using..!')
