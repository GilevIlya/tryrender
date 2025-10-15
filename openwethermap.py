import aiohttp
import asyncio

API_KEY = "7b406eb976d5843c00840557759dc6b2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cities = [
    "London","Paris","Berlin","Madrid","Rome","Vienna","Amsterdam","Prague",
    "Budapest","Warsaw","Lisbon","Dublin","Copenhagen","Oslo","Stockholm",
    "Helsinki","Athens","Moscow","Kyiv","Istanbul"
]

async def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as resp:
            data = await resp.json()
            if resp.status == 200:
                print(data)
            else:
                print(f"{city}: ошибка {data.get('message')}")

asyncio.run(get_weather('Одесса'))


# import requests
# import time

# BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
# API_KEY = '7b406eb976d5843c00840557759dc6b2'

# def weather(city):
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": "ru"
#     }
#     response = requests.get(BASE_URL, params=params)
#     data = response.json()

#     if response.status_code == 200:
#         city_name = data["name"]
#         temp = data["main"]["temp"]
#         feels = data["main"]["feels_like"]
#         desc = data["weather"][0]["description"]
#         wind = data["wind"]["speed"]

#         print(f"🌍 Город: {city_name}")
#         print(f"🌡 Температура: {temp}°C (ощущается как {feels}°C)")
#         print(f"☁ Погода: {desc}")
#         print(f"💨 Ветер: {wind} м/с")
#     else:
#         print("Ошибка:", data)

# cities = [
#     "London",
#     "Paris",
#     "Berlin",
#     "Madrid",
#     "Rome",
#     "Vienna",
#     "Amsterdam",
#     "Prague",
#     "Budapest",
#     "Warsaw",
#     "Lisbon",
#     "Dublin",
#     "Copenhagen",
#     "Oslo",
#     "Stockholm",
#     "Helsinki",
#     "Athens",
#     "Moscow",
#     "Kyiv",
#     "Istanbul"
# ]
# start = time.time()
# for city in cities:
#     weather(city)
# print(round(time.time()-start, 2))