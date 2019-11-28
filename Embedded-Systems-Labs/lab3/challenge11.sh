#!/bin/bash

echo "Please enter a password"

read userpass

if [ ${#userpass} -lt 10]; then 
    echo "password must be at least 10 chars long"
exit

elif [ ${userpass:0:4} == "pass" ] then 
    echo "pass can't start with pass"
exit

else 
    echo "$userpass" > passFile.txt

fi

