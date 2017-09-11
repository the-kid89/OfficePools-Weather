import os


OPEN_WEATHER_MAP_KEY = os.environ.get('OPEN_WEATHER_MAP_KEY', 'N/A')
OPEN_WEATHER_MAP_URI = 'http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&units=metric&appid=' + OPEN_WEATHER_MAP_KEY
