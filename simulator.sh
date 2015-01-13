#!/bin/sh

BASE="EjercicioC"

INPUT_DIR="${BASE}/data01"
MAP="${BASE}/Amap.py"
REDUCE="${BASE}/Areduce.py"

OUTPUT_DIR="${BASE}"
MAP_OUT="${OUTPUT_DIR}/map.txt"
REDUCE_OUT="${OUTPUT_DIR}/reduce.txt"

############
############
### Work ###
############
############

if [ -f ${MAP_OUT} ]; then
    rm ${MAP_OUT}
fi
if [ -f ${REDUCE_OUT} ]; then
    rm ${REDUCE_OUT}
fi

echo "Map ..."

for i in `ls "${INPUT_DIR}"`
do
    tmp=${INPUT_DIR}/${i}

    python "${MAP}" <  "${tmp}" >> "${MAP_OUT}"
done

echo "Reduce ..."

python "${REDUCE}" < "${MAP_OUT}" > "${REDUCE_OUT}"

echo "Done!!!"
echo "See ${REDUCE_OUT}"
