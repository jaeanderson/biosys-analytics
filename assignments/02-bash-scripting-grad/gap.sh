#!/bin/bash

DATADIR="/rsgrps/bh_class/jaea/biosys-analytics/data/gapminder"

ARG1=$1
TMP=$(mktemp)

if [[ $# -eq 0 ]]; then
    find "$DATADIR" -type f -name *.cc.txt -printf "%f\n" | sort > "$TMP"
fi

if [[ $# -eq 1 ]]; then
    find "$DATADIR" -type f -iname "$ARG1*" -printf "%f\n" | sort > "$TMP"
    NUM_FILES=$(wc -l "$TMP" | awk '{print $1}')

    if [[ $NUM_FILES -lt 1 ]]; then
        echo "There are no countries starting with" \"$ARG1\"
    fi
fi

i=0
while read -r FILENAME; do
    let i++
    BASENAME=$(basename "$FILENAME" .cc.txt)
    printf "%3d %s\n" $i "$BASENAME"
done < "$TMP"
        


