#!/bin/bash
read -d '' t
for i in $(echo $t)
do
echo -n ".${i:1} "
done
