#!/bin/sh

cd `dirname $0`

echo 'GEOMETRYCOLLECTION('

echo 'LINESTRING('
python ../../arc.py 354236N 1394839E 3 0 360 10
echo ')'

echo ')'
