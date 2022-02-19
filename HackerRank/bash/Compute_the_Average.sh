#!/bin/bash

read avg
sum=0

for i in $( seq 1 $avg)
do
read a
sum=$(( $sum + $a ))
done

out=$( echo " $sum/$avg" | bc  -l)
printf %.3f\\n "$out"

