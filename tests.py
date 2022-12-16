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
