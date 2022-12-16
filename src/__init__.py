"""
  tpkit
  ~~~~~
"""

from .filelib import \
(
  iterate_paths, 
  get_paths,
  crawl
)

from .functional import map

from .location import get_current_geocoordinate

from .weather import get_current_weather

from .quotes import get_random_quote
