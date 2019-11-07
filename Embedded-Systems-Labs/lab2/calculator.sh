#!/bin/bash
while true
do
echo "enter the numbers you would like to use"
read -a args 

echo "what operation to preform? (+ - x / % )"
read operation
 
case $operation in 
	+) echo "$((${args[0]} + ${args[1]})" ;;
	-) echo "$((${args[0]} - ${args[1]}))" ;;
	x) echo "$((${args[0]} * $args[1]}))" ;;
	/) echo "$((${args[0]} / ${args[1]}))" ;;
	%) echo "$((${args[0]} % ${args[0]}))" ;;
	*) echo "invalid choice of operator"
esac
echo $total
 
