"""
  tpkit.tests
  ~~~~~~~~~~~
"""

from .weather import Weather, get_current_weather

def test_get_current_weather():
  weather = get_current_weather()
  assert weather is not None and type(weather) is Weather
  weather_description = str(weather)
  assert weather_description is not None and type(weather_description) is str
  assert len(weather_description) > 0

