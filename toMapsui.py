#!/usr/bin/env python3

from math import log, pi, radians, tan
from sys import argv
from typing import Tuple
from toDEG import toDEG

EARTH_RADIUS_M = 6378137

def FromLonLat(lon: float, lat: float) -> Tuple[float, float]:
  return (EARTH_RADIUS_M * radians(lon), EARTH_RADIUS_M * log(tan((pi * 0.25) + (radians(lat) * 0.5))))

def FromDMSLonLat(lon: str | float, lat: str | float) -> Tuple[float, float]:
  return FromLonLat(toDEG(lon), toDEG(lat))

def main():
  result = FromDMSLonLat(
    argv[1],
    argv[2]
  )

  print(result[0], result[1], end="")

if __name__ == "__main__":
    main()
