import os
from dotenv import load_dotenv
import requests

def get_data():
    api_key = os.getenv('OPEN_WEATHER_API_KEY')
    print(api_key)
    lat = 45.5476
    lon = -87.3956
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    response = requests.get(url)

    data = response.json()

    print(data)


if __name__ == "__main__":
    load_dotenv()
    get_data()
