from typing import List
from sympy import content

list=[]
list2=[]
method=["insert","print","remove","append","sort","pop","reverse"]
counter= int(input()) 

for i in range(counter) :

    select= input().split()

    if select[0] == method[0] :
        
        list.insert(int(select[1]),int(select[2]))
    elif select[0] == method[1] :
        list2.append(list.copy()) # to use end input step
    elif select[0] == method[2] :
        list.remove(int(select[1]))
    elif select[0] == method[3] :
        list.append(int(select[1]))
    elif select[0] == method[4] :
        list.sort()
    elif select[0] == method[5] :
        list.pop()
    elif select[0] == method[6] :
        list.reverse()

for i in range(len(list2)) : # print waith finsh input 
    print(list2[i])
