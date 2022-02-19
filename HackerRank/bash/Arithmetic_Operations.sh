read e

a=`echo "scale=4; $e" | bc -l`

if [ ${a[@]: -1} == 5 ]
then
        echo "scale=3; $e + 0.001" | bc -l 
 else
         echo "scale=3; $e"| bc -l
 fi