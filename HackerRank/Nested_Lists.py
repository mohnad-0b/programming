cont = input()
records = []
min = 0
min2 = 0

for i in range(int(cont)) :
    name = input()
    grade = float(input())
    records.append([name,grade])

records.sort(key=lambda x:float(x[1])) # sort use "grade"

min2=records[1][1]
min = records[0][1]

for i in range(len(records)-2) : # if min2 not secand valio in list
    if min == min2 : 
        min2=records[i+2][1]
    else:
        break

records.sort()

for i in range(len(records)) : # print all
    if records[i][1] == min2 :
        print(records[i][0])   

