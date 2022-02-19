from itertools import count
from re import M


count = int(input())
mark = []
res = {}
for i in range(count) :
    mark.append(input().split(" "))
    res[mark[i][0]] = ("{:.2f}".format((float(mark[i][1]) + float(mark[i][2]) + float(mark[i][3]))/3))
name = input()

print(res[name])