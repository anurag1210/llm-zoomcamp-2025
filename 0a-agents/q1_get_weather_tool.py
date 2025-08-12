import random

# Known sample data
known_weather_data = {
    'berlin': 20.0
}

# Function that will be used by the agent
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


# Tool description for the agent
get_weather_tool = {
    "type": "function",
    "name": "get_weather",  # TODO1
    "description": "Retrieve the current temperature (°C) for a given city.",  # TODO2
    "parameters": {
        "type": "object",
        "properties": {
            "city": {  # TODO3
                "type": "string",
                "description": "Name of the city to get the temperature for."  # TODO4
            }
        },
        "required": ["city"],  # TODO5
        "additionalProperties": False
    }
}


# Quick test
if __name__ == "__main__":
    print("Tool description:", get_weather_tool)
    print("Weather in Berlin:", get_weather("Berlin"))