"""
  tpkit.weather
  ~~~~~~~~~~~~~

This module can be used to get weather data from the Open Meteo API,
"""

from dataclasses import dataclass

WEATHER_INTERPRETATION_CODES = {
  0: 'clear skies',
  1: 'partly cloudy skies and overcast',
  2: 'partly cloudy skies and overcast',
  3: 'partly cloudy skies and overcast',
  45: 'fog and depositing rime fog',
  48: 'fog and depositing rime fog',
  51: 'drizzle: light, moderate, and dense intensity',
  53: 'drizzle: light, moderate, and dense intensity',
  55: 'drizzle: light, moderate, and dense intensity',
  56: 'freezing drizzle: Light and dense intensity',
  57: 'freezing drizzle: Light and dense intensity',
  61: 'rain: slight, moderate and heavy intensity',
  63: 'rain: slight, moderate and heavy intensity',
  65: 'rain: slight, moderate and heavy intensity',
  66: 'freezing rain: light and heavy intensity',
  67: 'freezing rain: light and heavy intensity',
  71: 'snow fall: slight, moderate, and heavy intensity',
  73: 'snow fall: slight, moderate, and heavy intensity',
  75: 'snow fall: slight, moderate, and heavy intensity',
  77: 'snow grains',
  80: 'rain showers: slight, moderate, and violent',
  81: 'rain showers: slight, moderate, and violent',
  82: 'rain showers: slight, moderate, and violent',
  85: 'snow showers slight and heavy',
  86: 'snow showers slight and heavy',
  95: 'thunderstorm: slight or moderate',
  96: 'thunderstorm with slight and heavy hail',
  99: 'thunderstorm with slight and heavy hail'
}

@dataclass
class Weather:
  """
  Weather stats for a specific moment in time
  """
  temperature: float # farenheit
  windspeed: float
  winddirection: int
  weathercode: int
  time: str

  def __str__(self):
    weather_description = f'It is currently {self.temperature} degrees with a windspeed of {self.windspeed}. '
    if self.weathercode in WEATHER_INTERPRETATION_CODES:
      weather_description += f'Expect {WEATHER_INTERPRETATION_CODES[self.weathercode]}.'
    return weather_description

