import os
import sys
from typing import List, Tuple

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from arc import arc as _arc
from point import point
from toMapsui import FromLonLat
from toDEG import toDEG

g_DEFAULT_N = 0
g_DEFAULT_E = 0
g_MAG_VAR = 0
def SetValue(Default_N: float, Default_E: float, Mag_VAR: float):
  global g_DEFAULT_N
  global g_DEFAULT_E
  global g_MAG_VAR
  g_DEFAULT_N = Default_N
  g_DEFAULT_E = Default_E
  g_MAG_VAR = Mag_VAR

g_RADIUS = 0
def SetRadius(Radius: float):
  global g_RADIUS
  g_RADIUS = Radius

g_ARC_STEP = 1
def SetArcStep(Step: float):
  global g_ARC_STEP
  g_ARC_STEP = Step

def arc(ArcFrom: float, ArcTo: float, N: float | None = None, E: float | None = None) -> List[Tuple[float, float]]:
  ARC_FROM = ArcFrom + g_MAG_VAR
  ARC_TO = ArcTo + g_MAG_VAR

  if N is None:
    N = g_DEFAULT_N
  if E is None:
    E = g_DEFAULT_E

  return _arc(N, E, g_RADIUS, ARC_FROM, ARC_TO, g_ARC_STEP)

def arc_pt(Radius: float | None, _Angle: float, N: float | None = None, E: float | None = None) -> Tuple[float, float]:
  Angle = _Angle + g_MAG_VAR

  if N is None:
    N = g_DEFAULT_N
  if E is None:
    E = g_DEFAULT_E
  if Radius is None:
    Radius = g_RADIUS

  return point(N, E, Radius, Angle)

def arc_bridge(BridgeFrom: float, BridgeTo: float, _Angle: float, N: float | None = None, E: float | None = None) -> List[Tuple[float, float]]:
  return [arc_pt(BridgeFrom, _Angle, N, E), arc_pt(BridgeTo, _Angle, N, E)]

def dms(E: float, N: float) -> Tuple[float, float]:
  return (toDEG(E), toDEG(N))


def _print_xy(lonlat: Tuple[float, float], _is_first_row: List[bool]):
  xy = FromLonLat(lonlat[0], lonlat[1])

  if _is_first_row[0] != True:
    print(',')
  _is_first_row[0] = False

  print(xy[0], xy[1], end='')

g_IS_FIRST = True
def LINESTRING(*args: Tuple[float, float] | List[Tuple[float, float]]):
  global g_IS_FIRST

  _is_first_row = [True]

  if g_IS_FIRST != True:
    print(",")
  g_IS_FIRST = False

  print("LINESTRING(")
  for arg in args:
    if type(arg) is tuple:
      _print_xy(arg, _is_first_row)
    else:
      for lonlat in arg:
        _print_xy(lonlat, _is_first_row)
  
  print(")")
