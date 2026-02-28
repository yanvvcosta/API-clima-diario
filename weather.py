import requests
from config import WEATHER_API_KEY, CITY

def get_weather_forecast():
    """Retorna dados da previsão para o dia em Guarapari"""
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": CITY,
        "days": 1,
        "lang": "pt"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        forecast = data["forecast"]["forecastday"][0]["day"]
        return {
            "condicao": forecast["condition"]["text"],
            "temp_max": forecast["maxtemp_c"],
            "temp_min": forecast["mintemp_c"],
            "chuva_mm": forecast["totalprecip_mm"],
            "chance_chuva": forecast["daily_chance_of_rain"],
            "umidade": forecast["avghumidity"],
            "vento": forecast["maxwind_kph"]
        }
    except Exception as e:
        print(f"Erro ao obter clima: {e}")
        return None
