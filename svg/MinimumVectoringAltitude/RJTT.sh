#!/bin/sh

SKYTREE_N='354236N'
SKYTREE_E='1394839E'

cd `dirname $0`

echo 'GEOMETRYCOLLECTION('

echo 'LINESTRING('
python ../../arc.py $SKYTREE_N $SKYTREE_E 3 0 360 10
echo ')'

echo ')'
