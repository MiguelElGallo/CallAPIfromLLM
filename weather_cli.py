import openmeteo_requests
import requests_cache
from retry import retry
import numpy as np
import pandas as pd
import os
import argparse
import openai

def get_weather_data(latitude, longitude):
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }
    responses = openmeteo.weather_api(url, params=params)
    return responses[0]

def process_weather_data(response):
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
    
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    
    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m
    
    hourly_dataframe = pd.DataFrame(data=hourly_data)
    print(hourly_dataframe)

def ask_gpt(question):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_base = os.getenv("OPENAI_API_URL")
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=question,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description="Get weather data using Open-Meteo API")
    parser.add_argument("question", type=str, help="Question in English about the weather")
    args = parser.parse_args()
    
    gpt_response = ask_gpt(args.question)
    print(gpt_response)

if __name__ == "__main__":
    main()
