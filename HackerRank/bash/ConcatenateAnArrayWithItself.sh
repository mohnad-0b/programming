a="Namibia
Nauru
Nepal
Netherlands
NewZealand
Nicaragua
Niger
Nigeria
NorthKorea
Norway"


arr=($a)
n=""
j=${#arr[@]}

#echo $j
for (( i=0 ; i<3*${#arr[@]}; i++ ))
do

n[$i]=$(echo ${arr[$i%$j]})

done

echo ${n[@]}
