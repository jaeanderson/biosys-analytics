
#!/bin/bash


if [[ $# -ne 1 ]]; then
    printf "Usage: %s FILE\n" "$(basename "$0")"
    exit 1
fi

FILE=$1

if [[ ! -f $FILE ]]; then
    echo "$FILE is not a file"
    exit 1
fi

while read -r LINE; do
    let i++
    echo "$i" "$LINE"
done < "$FILE"

#FILE=$1
#i=0
#for LINE in $(cat "$FILE"); do
#    let i++
#    printf "%3d: %s\n" $i "$LINE"
#done
