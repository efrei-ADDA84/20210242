import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from uvicorn import run

load_dotenv()
app = FastAPI()

def make_api_call(latitude: float, longitude: float, api_key: str):
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

def extract_weather(data):
    try:
        weather = data['weather']
        return weather
    except (KeyError, TypeError):
        raise HTTPException(status_code=404, detail="Weather data not found")

@app.get("/")
def get_weather(lat: float, lon: float):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="No API key configured")
    data = make_api_call(lat, lon, api_key)
    weather = extract_weather(data)
    return {"latitude": lat, "longitude": lon, "weather": weather}

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8081)
