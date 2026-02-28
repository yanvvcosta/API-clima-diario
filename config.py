import os
from dotenv import load_dotenv

load_dotenv()

# WeatherAPI
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Guarapari"

# WhatsApp
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
WHATSAPP_TO = os.getenv("WHATSAPP_TO")  # formato: 5511999999999
