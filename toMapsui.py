from math import log, pi, radians, tan
from typing import Tuple

EARTH_RADIUS_M = 6378137

def FromLonLat(lon: float, lat: float) -> Tuple[float, float]:
  return (EARTH_RADIUS_M * radians(lon), EARTH_RADIUS_M * log(tan((pi * 0.25) + (radians(lat) * 0.5))))
