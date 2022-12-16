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

