#!/bin/bash
while true
do

total=0

echo "enter 3 numbers"
read -a args

echo "what operation to perform ? ( + - x / % )";read operation 

case $operation in 
+)total=$((${args[0]}+${args[1]}+${args[2]}))
    #running = $((${total}+${running}))
    running=$((${running}+${total}))
    echo "Ans: ${total}"
    echo "Total: ${running}";;
-) echo "$((${args[0]}-${args[1]}-${args[2]}))";;
x) echo "$((${args[0]}*${args[1]}*${args[2]}))";;
/) echo "$((${args[0]}/${args[1]}/${args[2]}))";;
%) echo "$((${args[0]}%${args[1]}%${args[2]}))";;
*) echo "invalid choice of operator"
esac
done
