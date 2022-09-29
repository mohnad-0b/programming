f1 = open("file2.txt", "r").read()
f2 = open("file3.txt", "r").read()

flag1 = ""
flag2 = ""

for i in range(0, len(f1)):
    if f1[i] != f2[i] :
        # print(f1[i], f2[i])
        flag1 += f1[i]
        flag2 += f2[i]
# print(flag1)
print(flag2[::-1])
