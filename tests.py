"""tpkit tests"""

import time
import tpkit

def test_get_random_quote():
  for _ in range(3):
    quote = tpkit.get_random_quote()
    assert type(quote.text) is str 
    assert len(quote.text) > 0
    assert type(quote.author) is str 
    assert len(quote.author) > 0
    formatted_quote = str(quote)
    assert type(formatted_quote) is str
    assert len(formatted_quote) > 0
    assert quote.author == formatted_quote.split(' - ')[1]
    time.sleep(0.1)

def test_get_current_geocordinates():
  coordinates = tpkit.get_current_geocoordinate()
  assert type(coordinates) is tuple
  assert len(coordinates) == 2
  lattitude, longitude = coordinates
  assert lattitude
  assert type(lattitude) is float
  assert -90 <= lattitude <= 90
  assert longitude
  assert type(lattitude) is float
  assert -180 <= lattitude <= 180

def test_get_current_weather():
  weather = tpkit.get_current_weather()
  assert weather.temperature and type(weather.temperature) is float
  assert weather.windspeed and type(weather.windspeed) is float
  assert weather.winddirection and type(weather.winddirection) is float
  assert weather.weathercode and type(weather.weathercode) is int
  assert weather.time and type(weather.time) is str

def test_map_function():
  multiples_of_2 = tpkit.map(lambda x: 2*x, [1,2,3])
  assert type(multiples_of_2) is list
  assert multiples_of_2 == [2,4,6]
