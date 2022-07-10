#!/bin/sh

SKYTREE_N='354236N'
SKYTREE_E='1394839E'

DEFAULT_N='353312N'
DEFAULT_E='1394652E'

ARC_STEP=('5' '2' '1')

cd `dirname $0`

echo 'GEOMETRYCOLLECTION('


# $1: arc from [deg]
# $2: arc to [deg]
# $3: lat [dms] (opt)
# $4: lng [dms] (opt)
IS_FIRST=1
arc() {
  if [ $IS_FIRST != 1 ]; then
    echo ','
  fi

  python -u ../../arc.py ${3:-$DEFAULT_N} ${4:-$DEFAULT_E} $RADIUS $1 $2 ${ARC_STEP[ARC_STEP_LV]}

  IS_FIRST=0
}

# $1: radius [nm]
# $2: angle [deg]
# $3: lat [dms] (opt)
# $4: lng [dms] (opt)
arc_pt() {
  python -u ../../point.py ${3:-$DEFAULT_N} ${4:-$DEFAULT_E} $1 $2
}
# $1: bridge from [nm]
# $2: bridge to [nm]
# $3: angle [deg]
# $4: lat [dms] (opt)
# $5: lng [dms] (opt)
arc_bridge() {
  if [ $IS_FIRST != 1 ]; then
    echo ','
  fi

  echo 'LINESTRING('
  arc_pt $1 $3 $4 $5
  echo ','
  arc_pt $2 $3 $4 $5
  echo ')'
  IS_FIRST=0
}

# $1: lng [dms] (opt)
# $2: lat [dms] (opt)
dms() {
  python -u ../../toMapsui.py $1 $2
}

ARC_STEP_LV=0

RADIUS='3'
arc 0 360 $SKYTREE_N $SKYTREE_E


RADIUS='2'
arc 200 260


RADIUS='3'
arc 260 410


RADIUS='6'
arc 90 150
arc 220 260


RADIUS='7'
arc 150 220
arc 260 320


RADIUS='10'
arc 20 90
arc 130 150
arc 210 220


ARC_STEP_LV=1


RADIUS='15'
arc 90 190
arc 220 380


RADIUS='20'
arc 0 120
arc 250 330


RADIUS='30'
arc 0 220
arc 280 330


RADIUS='35'
arc 230 250


RADIUS='39'
arc 20 40


RADIUS='40'
arc -30 20


RADIUS='45'
arc 200 230
arc 250 330


ARC_STEP_LV=2


RADIUS='50'
arc -80 250


RADIUS='60'
arc -80 40


RADIUS='65'
arc 40 180
arc 220 250


RADIUS='70'
arc 20 40


RADIUS='80'
arc 20 150
arc 280 350 # TODO: crossing-check
arc -40 70 354555N 1402308E # TODO: crossing-check

RADIUS='105'
arc 30 165 # TODO: crossing-check

# Arc Bridges
# from[nm] to[nm] angle[deg]

arc_bridge 2 7 200
arc_bridge 2 3 260


arc_bridge 3 15 20
arc_bridge 3 10 50
arc_bridge 3 15 320


arc_bridge 6 10 90
arc_bridge 6 10 150
arc_bridge 6 7 220
arc_bridge 6 7 260


arc_bridge 7 10 210
arc_bridge 7 15 280


arc_bridge 10 15 130
arc_bridge 10 30 220


arc_bridge 15 30 0
arc_bridge 15 20 90
arc_bridge 15 30 120
arc_bridge 15 30 190


arc_bridge 20 100 250 # TODO: crossing-check
arc_bridge 20 80 280
arc_bridge 20 80 330
arc_bridge 20 80 330


arc_bridge 35 45 230


arc_bridge 39 100 20 # TODO: crossing-check
arc_bridge 39 65 40


arc_bridge 45 50 200
arc_bridge 45 65 220 # Specified point available

echo ','
echo 'LINESTRING('
arc_pt 65 220
echo ','
dms '1390018.59' '343347.25'
echo ','
dms '1390102.43' '340254.60'
echo ')'


arc_bridge 65 80 150
arc_bridge 65 100 180 # TODO: crossing-check


arc_bridge 70 80 40


echo ','
echo 'LINESTRING('
arc_pt 80 280
echo ','
dms '1380852.00' '353127.02'
echo ','
dms '1381154.70' '340227.95'
echo ','
dms '1390102.43' '340254.60'
echo ','
dms '1405156.08' '340242.55'
echo ','
dms '1410615.06' '340233.70'
echo ','
dms '1411152.44' '340431.65'
echo ','
dms '1415945.12' '342101.78'
echo ','
dms '1420054.39' '350322.38'
echo ','
dms '1420306.55' '362118.07'
echo ','
dms '1415132.38' '362134.18'
echo ')'

echo ','
echo 'LINESTRING('
dms '1411152.44' '340431.65'
echo ','
dms '1412629.06' '341417.40'
echo ','
dms '1420054.39' '350322.38'
echo ')'

echo ','
echo 'LINESTRING('
dms '1410437.57' '362228.03'
echo ','
dms '1414137.62' '362147.09'
echo ')'


echo ')'
