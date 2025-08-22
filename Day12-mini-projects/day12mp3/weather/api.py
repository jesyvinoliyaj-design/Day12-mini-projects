import requests as rq
import json
from datetime import datetime as dt

API_KEY = "your_api_key_here"  # get free key from openweathermap.org
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    """Fetch weather data from API for a given city"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = rq.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code != 200:
            return {"error": data.get("message", "Unknown error")}
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "time": dt.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": str(e)}
from datetime import datetime as dt

def get_weather(city: str):
    """Mock weather data for offline testing"""
    sample_data = {
        "city": city.title(),
        "country": "IN",
        "temp": 32,
        "feels_like": 34,
        "humidity": 60,
        "weather": "haze",
        "time": dt.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return sample_data
