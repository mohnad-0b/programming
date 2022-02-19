#!/bin/bash
read -d "" a

arr=($a)

A="A"
a="a"
for (( i=0; i<=${#arr[@]}; i++ )); do
j="${arr[$i]}"
#echo $j

if [[ "$j" != *"a"* ]] && [[ "$j" != *"a"* ]]
then
echo "$j"
fi
done
