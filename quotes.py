"""
  tpkit.quotes
  ~~~~~~~~~~~~

This module generates random quotes.
"""

from dataclasses import dataclass

@dataclass
class Quote:
  text: str
  author: str

  def __str__(self):
    return f'{self.text}\n  - {self.author}'

