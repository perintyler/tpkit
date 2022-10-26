"""
  tpkit.tests
  ~~~~~~~~~~~
"""

from .weather import Weather, get_current_weather

from .quotes import Quote, get_random_quote

def test_get_current_weather():
  weather = get_current_weather()
  assert weather is not None and type(weather) is Weather
  weather_description = str(weather)
  assert weather_description is not None and type(weather_description) is str
  assert len(weather_description) > 0

def test_get_random_quote():
  quote = get_random_quote()
  assert quote is not None and type(quote) is Quote
  assert quote.text is not None and type(quote.text) is str
  assert len(quote.text) > 0
  assert quote.author is not None and type(quote.author) is str
  assert len(quote.author) > 0
  formatted_quote = str(quote)
  assert quote.text in formatted_quote and quote.author in formatted_quote
