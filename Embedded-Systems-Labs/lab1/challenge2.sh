#!/bin/bash

echo "what is your name?"; read name
echo "enter a place"; read place
echo "enter a thing"; read thing
echo "enter a weekday";read weekday

echo "${name} goes to ${place} on ${weekday} to buy ${thing}" >>chall2file.txt


