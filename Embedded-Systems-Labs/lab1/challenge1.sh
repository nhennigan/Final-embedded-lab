#!/bin/bash
echo "please enter names"
args=("$@")

var="Hello ${args[0]} and ${args[1]}"

echo $var 
echo $var>>file.txt
