#!/bin/bash

URL="https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Leaked-Databases/Ashley-Madison.txt"
if [ ! -f "Ashley-Madison.txt" ]; then
    wget $URL
fi

NUM_TRIES=0
while IFS= read -r line; do
    case $line in
    im*)
        if gpg  --batch --yes --passphrase "$line" --decrypt $1 2>/dev/null; then
            echo "$line"
            exit 0
        fi
    esac
    NUM_TRIES=$((NUM_TRIES + 1))
    if expr $NUM_TRIES % 100 = 0 > /dev/null; then
        echo "Tried $NUM_TRIES passwords..."
    fi
done < "$(basename "$URL")"
