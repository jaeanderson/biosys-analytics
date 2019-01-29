 #!/bin/bash

if [[ $# -eq 0 ]] || [[ $# -gt 2 ]] ; then
    printf "Usage: %s FILE NUMBER\n" "$(basename "$0")"
    exit 1
fi

INPUT_FILE=$1
NUM=${2:-3}

if [[ ! -f  "$INPUT_FILE" ]]; then
     echo "$INPUT_FILE is not a file"
     exit 1
fi

IFS=''
for (( i=1; i <= NUM; i++ )); do
     echo "$(sed "${i}q;d" "$INPUT_FILE")"
done

