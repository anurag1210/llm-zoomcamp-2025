import random

# Sample in-memory database
known_weather_data = {
    'berlin': 20.0
}

# Q1 function
def get_weather(city: str) -> float:
    """
    Retrieve the current temperature (°C) for a given city.

    Parameters:
        city (str): The name of the city to get the temperature for.

    Returns:
        float: The temperature in °C.
    """
    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]

    return round(random.uniform(-5, 35), 1)

get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Retrieve the current temperature (°C) for a given city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "Name of the city to get the temperature for."
            }
        },
        "required": ["city"],
        "additionalProperties": False
    }
}

# Q2 function
def set_weather(city: str, temp: float) -> None:
    """
    Set the temperature (°C) for a specified city.

    Parameters:
        city (str): The name of the city to set the temperature for.
        temp (float): The temperature value in °C to associate with the city.

    Returns:
        str: "OK" after updating the temperature.
    """
    city = city.strip().lower()
    known_weather_data[city] = temp
    return 'OK'

set_weather_tool = {
    "type": "function",
    "name": "set_weather",
    "description": "Set the temperature (°C) for a given city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "Name of the city to set the temperature for."
            },
            "temp": {
                "type": "number",
                "description": "Temperature value in °C to set for the city."
            }
        },
        "required": ["city", "temp"],
        "additionalProperties": False
    }
}

# Quick test
if __name__ == "__main__":
    print("Initial weather data:", known_weather_data)
    print("Setting Paris temp to 25.5°C ->", set_weather("Paris", 25.5))
    print("Weather in Paris:", get_weather("Paris"))
    print("Updated weather data:", known_weather_data)