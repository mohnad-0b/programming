from math import ceil
from math import floor


STDOUTH = "H"
STDOUTH_new = STDOUTH
num = int(input())
for i in range(num) :
    width = num*2 - 1
    print(STDOUTH_new.center(width," "))
    STDOUTH_new = STDOUTH_new + STDOUTH*2

for i in range(num + 1 ) :
    print(" "*int(floor(num/2)) + (" "*(num*5 -num*2)).center((5*num),STDOUTH))

for i in range(ceil(num/2)) : 
    print(" "*int(floor(num/2)) + STDOUTH*(5*num))

for i in range(num + 1) :
    print(" "*int(floor(num/2)) + (" "*(num*5 -num*2)).center((5*num),STDOUTH))

STDOUTH_new = STDOUTH_new[:len(STDOUTH_new)-2]
for i in range(num) :
    width = num*2 + 1
    print((" "*(num*5 - num - 1) ) + STDOUTH_new.center(width," "))
    STDOUTH_new = STDOUTH_new[:len(STDOUTH_new)-2]


