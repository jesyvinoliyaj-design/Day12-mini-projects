from . import api as weather_api
from . import formatter as fmt

def run_cli():
    print("=== Weather Report Console App ===")
    city = input("Enter city name: ")
    data = weather_api.get_weather(city)
    report = fmt.format_weather(data)
    print(report)
