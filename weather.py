"""
  tpkit.weather
  ~~~~~~~~~~~~~

This module can be used to get weather data from the Open Meteo API,
"""

from dataclasses import dataclass

@dataclass
class Weather:
  """
  Weather stats for a specific moment in time
  """
  temperature: float # farenheit
  windspeed: float
  winddirection: int
  weathercode: int
  time: str
