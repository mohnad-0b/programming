host = 1
time_unit = 0
input1 = input().split(" ")
n = int(input1[0]) 
m = int(input1[1]) 

input2 = input().split(" ")
tasks = []
for i in range(m):
    tasks.append(int(input2[i]))

while (True):
    if tasks[0] == host:
        while (True):
            if (len(tasks) > 1 and tasks[0] == tasks[1]):
                tasks.remove(host)
            tasks.remove(host)
            break
        if len(tasks) == 0:
            break
    if host == n:
        i = 1
        host = 0
    host += 1
    time_unit += 1

print(time_unit)
