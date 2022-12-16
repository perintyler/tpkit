"""
  tpkit.location
  ~~~~~~~~~~~~~~
"""

import json
import subprocess
from typing import Tuple

def get_current_geocoordinate() -> Tuple[float]: # (lattidude, longitude)
  """
  returns the lattitude and longitude of the current IP address
  """
  ip_command = subprocess.run(
    ['curl', 'ipinfo.io'],
    capture_output=True,
  )

  ip_info = json.loads(ip_command.stdout)
  current_coordinate = ip_info['loc']
  lattitude, longitude = current_coordinate.split(',')

  return float(lattitude), float(longitude)
