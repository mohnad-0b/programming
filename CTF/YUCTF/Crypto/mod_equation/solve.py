from string import printable

key = {}
for i in printable : 
    key[((ord(i)<<1 * 23244 )>>3)%435262] = i

# print(key)

flag_enc = open('output' , 'r').read()
for i in (flag_enc[1:-2].split(",")):
    print(key[int(i)],end="")