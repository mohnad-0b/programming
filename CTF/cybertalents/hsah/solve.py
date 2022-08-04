import hashlib
from string import printable
flag_enc = open("output", "r").read()
flag={}
res = ""
for i in printable:
    for j in printable:
        chek = (i+j).encode()
        if hashlib.sha512(chek).hexdigest()[31:-31][::-1] in flag_enc :
            flag[flag_enc.find(hashlib.sha512(chek).hexdigest()[31:-31][::-1])] = i+j

for i in sorted(flag.items()) :
    print(i[1],end="")
