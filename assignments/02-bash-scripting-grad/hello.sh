 #!/bin/bash

if [[ $# -eq 0 ]] || [[ $# -gt 2 ]] ; then
    printf "Usage: %s GREETING [NAME]\n" "$(basename "$0")"
    exit 1
fi

GREETING=$1
NAME=${2:-"Human"}

printf "%s, %s!\n" "$GREETING" "$NAME"
