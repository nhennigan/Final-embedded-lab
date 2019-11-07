#!/bin/bash

echo "enter a password"

read userpass

if [ ${#userpass} -le 10 ]
then 
echo "password must be longer than 10 chaaracters"
exit 

elif [ ${userpass:0:4} == "pass" ]
then 
echo "password cannot start with the letters pass"
exit 

else 
echo "$userpass" > saved_password.txt
chmod 600 saved_password.txt
fi
