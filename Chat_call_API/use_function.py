import json
from typing import Annotated

import openmeteo_requests
import requests_cache
from promptflow import tool
from pydantic import Field
from retry_requests import retry


def get_current_weather(
    latitude: Annotated[
        float, Field(ge=-90, le=90, description="Latitude between -90 and +90 degrees")
    ],
    longitude: Annotated[
        float,
        Field(ge=-180, le=180, description="Longitude between -180 and +180 degrees"),
    ],
) -> float:
    """
    Fetches the current weather for a given location using the Open-Meteo API.

    Args:
        latitude (float): Latitude between -90 and +90 degrees
        longitude (float): Longitude between -180 and +180 degrees

    Returns:
        float: The current temperature in Celsius at 2m above ground
    """
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": latitude, "longitude": longitude, "hourly": "temperature_2m"}
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    return float(hourly_temperature_2m[0])


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def temperature_tool(response_message: dict) -> str:
    function_call = response_message.get("function_call", None)
    if function_call and "name" in function_call and "arguments" in function_call:
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])
        print(function_args)
        result = globals()[function_name](**function_args)
    else:
        print("No function call")
        if isinstance(response_message, dict):
            result = response_message.get("content", "")
        else:
            result = response_message
    return result
