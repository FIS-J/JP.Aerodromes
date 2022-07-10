#!/usr/bin/env python3

from toDEG import toDEG
from sys import argv
from typing import List, Tuple
from geopy.distance import distance
from toMapsui import FromLonLat

# $1: Center lat (**N) (in dms)
# $2: Center lng (**E) (in dms)
# $3: Radius (in nm)
# $4: begin (in deg, point included)
# $5: end (in deg, point included)
# $6: step (in deg) = splits every...

# Output: lng lat(in deg) every line

def arc_deg(CENTER_LAT: float, CENTER_LNG: float, RADIUS_NM: float, ARC_BEGIN_DEG: float, ARC_END_DEG: float, STEP_DEG: float = 1) -> List[Tuple[float, float]]:
  RADIUS_KM = float(RADIUS_NM) * 1.852

  deg = ARC_BEGIN_DEG
  calculator = distance(kilometers=RADIUS_KM)
  CENTER = (CENTER_LAT, CENTER_LNG)

  ret = []
  while deg <= ARC_END_DEG:
    destination = calculator.destination(CENTER, bearing=deg)
    ret.append((destination.longitude, destination.latitude))
    deg += STEP_DEG
  
  return ret

def arc(CENTER_LAT_DMS: str | float, CENTER_LNG_DMS: str | float, RADIUS_NM: float, ARC_BEGIN_DEG: float, ARC_END_DEG: float, STEP_DEG: float = 1) -> List[Tuple[float, float]]:
  return arc_deg(toDEG(CENTER_LAT_DMS), toDEG(CENTER_LNG_DMS), RADIUS_NM, ARC_BEGIN_DEG, ARC_END_DEG, STEP_DEG)


def main():
  result = arc(
    argv[1],
    argv[2],
    float(argv[3]),
    float(argv[4]),
    float(argv[5]),
    float(argv[6])
  )

  if len(argv) == 8 and argv[7] == "DEG":
    for (lng, lat) in result:
      print(lng, lat)
  else:
    for (lng, lat) in result[:-1]:
      (n_lng, n_lat) = FromLonLat(lng, lat)
      print(n_lng, n_lat, end=",\n")

    (lng, lat) = result[-1]
    (n_lng, n_lat) = FromLonLat(lng, lat)
    print(n_lng, n_lat)

if __name__ == "__main__":
    main()
