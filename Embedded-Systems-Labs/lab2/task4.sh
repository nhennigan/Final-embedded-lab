#!/bin/bash

for f in $( ls ); do
    echo $f
done > output.txt
