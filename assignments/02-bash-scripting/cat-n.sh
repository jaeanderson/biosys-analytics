
#!/bin/bash


if [[ $# -ne 1 ]]; then
    printf "Usage: %s FILE\n" "$(basename "$0")"
    exit 1
fi

FILE=$1

if [[ -f $FILE ]]; then
    NUM_LINES=$(wc -l "$FILE" | awk '{print $1}')
else    
    echo "$FILE is not a file"
    exit 1
fi

for (( i=1; i <= NUM_LINES; i++ )); do
    #printf "%3d: %s\n" $i "$LINE"
    echo ""$i "$(sed "${i}q;d" "$FILE")"
done
