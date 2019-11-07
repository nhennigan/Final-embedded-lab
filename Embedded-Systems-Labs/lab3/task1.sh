#!/bin/bash
string=hello
echo "string: $string"
echo "string length = ${#string}"

echo "alternative method: string length = `expr length $string` "

num1=9
num2=999
echo "length of $num1 = ${#num1}"
echo "length of $num2 = ${#num2}"

