#!/usr/bin/env python3

from toDEG import toDEG
from sys import argv
from typing import Tuple
from arc import toDEG
from geopy.distance import distance
from toMapsui import FromLonLat

def point_deg(CENTER_LAT: float, CENTER_LNG: float, RADIUS_NM: float, ANGLE_DEG: float) -> Tuple[float, float]:
  RADIUS_KM = float(RADIUS_NM) * 1.852

  CENTER = (CENTER_LAT, CENTER_LNG)

  destination = distance(kilometers=RADIUS_KM).destination(CENTER, bearing=ANGLE_DEG)

  return destination.longitude, destination.latitude

def point(CENTER_LAT_DMS: str | float, CENTER_LNG_DMS: str | float, RADIUS_NM: float, ANGLE_DEG: float) -> Tuple[float, float]:
  return point_deg(toDEG(CENTER_LAT_DMS), toDEG(CENTER_LNG_DMS), RADIUS_NM, ANGLE_DEG)

def main():
  result = point(
    argv[1],
    argv[2],
    float(argv[3]),
    float(argv[4])
  )

  if argv[-1] == "DEG":
    print(result)
  else:
    (n_lng, n_lat) = FromLonLat(result[0], result[1])
    print(n_lng, n_lat, end="")

if __name__ == "__main__":
    main()
