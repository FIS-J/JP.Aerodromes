#!/usr/bin/env python3

from func import *

SKYTREE_N = 354236
SKYTREE_E = 1394839

DEFAULT_N = 353312
DEFAULT_E = 1394652

RJAA_ARP_N = 354555
RJAA_ARP_E = 1402308

MAG_VAR = -8

ARC_STEP = [2, 1, 0.5]


print("GEOMETRYCOLLECTION(")

SetValue(DEFAULT_N, DEFAULT_E, MAG_VAR)
SetArcStep(ARC_STEP[0])

SetRadius(3)


LINESTRING(
  arc_pt(None, 30, SKYTREE_N, SKYTREE_E),
  arc_pt(None, 30.221, SKYTREE_N, SKYTREE_E),
  arc(35, 105, SKYTREE_N, SKYTREE_E),
  arc_pt(None, 106.015, SKYTREE_N, SKYTREE_E),
  arc(110, 186, SKYTREE_N, SKYTREE_E),
  arc_pt(None, 189.81, SKYTREE_N, SKYTREE_E),
  arc(190, 390, SKYTREE_N, SKYTREE_E)
)


SetRadius(2)
LINESTRING(arc(200, 260))


SetRadius(3)
LINESTRING(arc(260, 410))


SetRadius(6)
LINESTRING(arc(90, 150))
LINESTRING(arc(220, 260))


SetRadius(7)
LINESTRING(arc(150, 220))
LINESTRING(arc(260, 320))


SetRadius(10)
LINESTRING(
  arc_pt(None, 34.2516),
  arc(35, 90)
)
LINESTRING(arc(130, 150))
LINESTRING(arc(210, 220))


SetArcStep(ARC_STEP[1])


SetRadius(15)
LINESTRING(arc(90, 190))
LINESTRING(arc(220, 380))


SetRadius(20)
LINESTRING(arc(0, 120))
LINESTRING(arc(250, 330))


SetRadius(30)
LINESTRING(arc(0, 220))
LINESTRING(arc(280, 330))


SetRadius(35)
LINESTRING(arc(230, 250))


SetRadius(39)
LINESTRING(arc(20, 40))


SetRadius(40)
LINESTRING(arc(-30, 20))


SetRadius(45)
LINESTRING(arc(200, 230))
LINESTRING(arc(250, 330))


SetArcStep(ARC_STEP[2])


SetRadius(50)
LINESTRING(arc(-80, 250))


SetRadius(60)
LINESTRING(arc(-80, 40))


SetRadius(65)
LINESTRING(arc(40, 180))
LINESTRING(arc(220, 250))


SetRadius(70)
LINESTRING(arc(20, 40))


SetRadius(80)
LINESTRING(
  arc(20, 59),
  dms(1410437.57, 362228.03),
  arc(60, 150)
)
LINESTRING(
  arc(280, 356),
  arc_pt(None, 356.1735),
  arc(-26, 29, RJAA_ARP_N, RJAA_ARP_E),
  arc_pt(None, 29.1653, RJAA_ARP_N, RJAA_ARP_E),
  arc(30, 71, RJAA_ARP_N, RJAA_ARP_E),
  dms(1415132.38, 362134.18)
)


SetRadius(105)

LINESTRING(
  arc_pt(80, 29.1653, RJAA_ARP_N, RJAA_ARP_E),
  arc_pt(None, 41.488),
  arc(42, 69.5),
  dms(1414137.62, 362147.09),
  arc(70.5, 156),
  dms(1405156.08, 340242.55)
)


LINESTRING(arc_bridge(2, 7, 200))
LINESTRING(arc_bridge(2, 3, 260))


LINESTRING(
  arc_pt(3, 20),
  arc_pt(6.5, 20),
  arc_pt(3, 189.81, SKYTREE_N, SKYTREE_E)
)


LINESTRING(
  arc_pt(15, 20),
  arc_pt(12.5, 20),
  arc_pt(3, 30.221, SKYTREE_N, SKYTREE_E)
)

LINESTRING(arc_bridge(3, 10, 50))
LINESTRING(arc_bridge(3, 15, 320))


LINESTRING(arc_bridge(6, 10, 90))
LINESTRING(arc_bridge(6, 10, 150))
LINESTRING(arc_bridge(6, 7, 220))
LINESTRING(arc_bridge(6, 7, 260))


LINESTRING(arc_bridge(7, 10, 210))
LINESTRING(arc_bridge(7, 15, 280))


LINESTRING(arc_bridge(10, 15, 130))
LINESTRING(arc_bridge(10, 30, 220))


LINESTRING(arc_bridge(15, 30, 0))
LINESTRING(arc_bridge(15, 20, 90))
LINESTRING(arc_bridge(15, 30, 120))
LINESTRING(arc_bridge(15, 30, 190))


LINESTRING(arc_bridge(20, 90.04, 250))
LINESTRING(arc_bridge(20, 80, 280))
LINESTRING(arc_bridge(20, 80, 330))


LINESTRING(arc_bridge(35, 45, 230))


LINESTRING(arc_bridge(39, 94.2285, 20))
LINESTRING(arc_bridge(39, 65, 40))


LINESTRING(arc_bridge(45, 50, 200))
LINESTRING(
  arc_bridge(45, 65, 220),
  dms(1390018.59, 343347.25),
  dms(1390102.43, 340254.60)
)


LINESTRING(arc_bridge(65, 80, 150))
LINESTRING(arc_bridge(65, 91.1224, 180))


LINESTRING(arc_bridge(70, 80, 40))



LINESTRING(
  arc_pt(80, 280),
  dms(1380852.00, 353127.02),
  dms(1381154.70, 340227.95),
  dms(1390102.43, 340254.60),
  dms(1405156.08, 340242.55),
  dms(1410615.06, 340233.70),
  dms(1411152.44, 340431.65),
  dms(1415945.12, 342101.78),
  dms(1420054.39, 350322.38),
  dms(1420306.55, 362118.07),
  dms(1415132.38, 362134.18)
)


LINESTRING(
  dms(1411152.44, 340431.65),
  dms(1412629.06, 341417.40),
  dms(1420054.39, 350322.38)
)


LINESTRING(
dms(1410437.57, 362228.03),
dms(1414137.62, 362147.09)
)

print(")")
