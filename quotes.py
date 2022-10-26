"""
  tpkit.quotes
  ~~~~~~~~~~~~

This module generates random quotes.
"""

from dataclasses import dataclass
import requests 
import random

QUOTE_API_URL = 'https://type.fit/api/quotes'

@dataclass
class Quote:
  text: str
  author: str

  def __str__(self):
    return f'{self.text}\n  - {self.author}'

def fetch_quotes():
  request = requests.get(QUOTE_API_URL)
  if request.status_code != requests.codes.ok:
    raise ConnectionError(f'quote API request failed with status code {request.status_code}')
  return [Quote(**json_object) for json_object in request.json()]

def get_random_quote():
  return random.choice(fetch_quotes())

