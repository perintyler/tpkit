"""
  tpkit.functional
  ~~~~~~~~~~~~~~~~

This module contains functions that can be used for functional programming.
"""

from typing import List, Iterator, Callable

builtin_map = map

def map(function: Callable, iterable: Iterator, *args, **kwargs) -> List:
  map_iterator = builtin_map(function, iterable, *args, **kwargs)
  return list(map_iterator)
