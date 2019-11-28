#!/bin/bash



while true; do

read line
echo "${line}" >> chall2.txt

if [ "$line" == "quit"]; then 
echo "quit now"    
break
fi

done
