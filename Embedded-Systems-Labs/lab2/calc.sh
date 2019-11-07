#!/bin/bash
while true
do

total=0
echo "enter 2 numbers"
read -a args

echo "what operation to perform ? ( + - x / % )"
read operation 

for i in "${args[@]}"; do
	echo $i
done 

case $operation in 
+) echo "$((${args[0]}+${args[1]}))";;
-) echo "$((${args[0]}-${args[1]}))";;
x) echo "$((${args[0]}*${args[1]}))";;
/) echo "$((${args[0]}/${args[1]}))";;
%) echo "$((${args[0]}%${args[1]}))";;
*) echo "invalid choice of operator"
esac
done
