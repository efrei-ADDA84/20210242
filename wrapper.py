import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(latitude, longitude, api_key):
    if not api_key:
        raise ValueError("API key not found")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    latitude= float(os.getenv("LOCATION_LATITUDE"))
    longitude= float(os.getenv("LOCATION_LONGITUDE"))
    api_key = os.getenv("OPENWEATHER_API_KEY")

    weather_data= get_weather(latitude, longitude, api_key)
    if weather_data:
        print("Weather data:")
        print(weather_data)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
