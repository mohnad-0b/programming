#!/bin/bash
read n1
read n2
read n3
if [ $n1 -eq $n2 ] || [ $n2 -eq $n3 ]
then 
if [ $n2 -eq $n3 ] && [ $n1 -eq $n2 ]
then
echo "EQUILATERAL"
else
echo "ISOSCELES"
fi
else
echo "SCALENE"
fi
