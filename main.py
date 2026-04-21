import requests
import json

class WeatherBasedClothingAdvisor:
    def __init__(self, city):
        self.city = city
        self.api_key = "API_KEY"  # ICAO kodi yoki API key
        self.weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"

    def get_weather(self):
        response = requests.get(self.weather_api_url)
        return response.json()

    def get_temperature(self, weather_data):
        return weather_data["main"]["temp"]

    def get_humidity(self, weather_data):
        return weather_data["main"]["humidity"]

    def get_weather_description(self, weather_data):
        return weather_data["weather"][0]["description"]

    def get_clothing_recommendation(self, temperature, humidity, weather_description):
        if temperature < 10:
            return "Qorong'i kiyim kiyin"
        elif temperature < 20:
            return "Kurak kiyim kiyin"
        elif temperature < 30:
            return "Issiq kiyim kiyin"
        elif temperature >= 30:
            return "Issiq kiyim kiyin, shuningdek, keng qolgan kiyim kiyin"
        elif humidity > 80:
            return "Issiq kiyim kiyin, shuningdek, keng qolgan kiyim kiyin"
        else:
            return "Issiq kiyim kiyin"

    def get_advisor(self):
        weather_data = self.get_weather()
        temperature = self.get_temperature(weather_data)
        humidity = self.get_humidity(weather_data)
        weather_description = self.get_weather_description(weather_data)
        return self.get_clothing_recommendation(temperature, humidity, weather_description)

city = "Toshkent"
advisor = WeatherBasedClothingAdvisor(city)
print(advisor.get_advisor())
```

Kodda quyidagilar qo'llangan:

1. OpenWeatherMap API dan foydalanish uchun API key yoki ICAO kodi kiritilgan.
2. `WeatherBasedClothingAdvisor` klassi yaratilgan, unda shahar nomi, API key va OpenWeatherMap API dan foydalanish uchun URL kiritilgan.
3. `get_weather` metodida OpenWeatherMap API dan ma'lumotlar olingan.
4. `get_temperature`, `get_humidity` va `get_weather_description` metodlarida ma'lumotlar olingan.
5. `get_clothing_recommendation` metodida kiyim tavsiyasi berilgan.
6. `get_advisor` metodida kiyim tavsiyasi olingan.
