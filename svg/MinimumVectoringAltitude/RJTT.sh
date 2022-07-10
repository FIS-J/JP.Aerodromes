#!/bin/sh

SKYTREE_N='354236N'
SKYTREE_E='1394839E'

ARC_STEP=('5' '2' '1')

cd `dirname $0`

echo 'GEOMETRYCOLLECTION('


RADIUS='3'
ARC_STEP_LV=0
python ../../arc.py $SKYTREE_N $SKYTREE_E $RADIUS 0 360 ${ARC_STEP[ARC_STEP_LV]}

echo ')'
