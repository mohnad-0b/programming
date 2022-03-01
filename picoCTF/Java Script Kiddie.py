a="" #Here, type your bytes
a=a.split()
h=[]
m=['0x89','0x50','0x4e','0x47','0xd','0xa','0x1a','0xa','0x0','0x0','0x0','0xd','0x49','0x48','0x44','0x52']
k=[]
k1=[]
 
for i in range(len(a)):
    h.append(hex(int(a[i])))
 
for i in range(10):
    for j in range(16):
        k.append(h[j+(i*16)])
    k1.append(k)
    k=[]
 
# print(len(k1[0]))
# print(len(k1))
 
 
for i in range(16):
    for j in range(10):
        if (m[i] == k1[j][i]):
            print(j,end=" ")
    print()
 
