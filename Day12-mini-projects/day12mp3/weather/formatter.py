def format_weather(data: dict) -> str:
    """Format weather data into human-readable output"""
    if "error" in data:
        return f"❌ Error: {data['error']}"
    
    return (
        f"\n🌍 Weather Report for {data['city']}, {data['country']}\n"
        f"📅 Time: {data['time']}\n"
        f"🌡 Temperature: {data['temp']}°C (Feels like {data['feels_like']}°C)\n"
        f"💧 Humidity: {data['humidity']}%\n"
        f"☁ Condition: {data['weather'].title()}\n"
    )
