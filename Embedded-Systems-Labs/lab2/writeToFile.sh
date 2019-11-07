#!/bin/bash
boop=true
while ${boop};
do

echo "Type some text which will be saved to the writeToText_output.txt "
echo "type 'quit' on a new line to quit"

read user_input 
echo $user_input >> writeToText_Output.txt

if [ $user_input == "quit" ] ;
then 
exit 
fi 

done
