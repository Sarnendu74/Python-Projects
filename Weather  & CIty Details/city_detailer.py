import requests
import json
print('Welcome to City-Detailer')
city = 'kolkata'
url = f"https://Weather-API.proxy-production.allthingsdev.co/weather/citySearch?search_term={city}"

payload = {}
headers = {
   'accept': '*/*',
   'accept-language': 'en-US,en;q=0.9',
   'origin': 'https://edition.cnn.com',
   'priority': 'u=1, i',
   'referer': 'https://edition.cnn.com/',
   'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
   'sec-ch-ua-mobile': '?0',
   'sec-ch-ua-platform': '"Windows"',
   'sec-fetch-dest': 'empty',
   'sec-fetch-mode': 'cors',
   'sec-fetch-site': 'cross-site',
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
   'x-apihub-key': 'v5y-gPrCXnj7Wr5WrKPHLEiIm-iM5vomj1Ppfh0rvcyoKl3bqb',
   'x-apihub-host': 'Weather-API.allthingsdev.co',
   'x-apihub-endpoint': '175f72ec-0ec4-4986-bbc6-b098d29b8200'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(f'Your {city} details are given below:--')
city_details = json.loads(response.text)
# print(len(city_details))
for x in city_details.values():
    print(x) 
    break
