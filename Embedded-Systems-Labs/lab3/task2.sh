#!/bin/bash 

string=onetwothreefour

echo ${string:6:5}

echo ${string#one}

echo ${string%four}

echo ${string/four/seven}

