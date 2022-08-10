flat_enc =  "1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}".split(",")
for i in flat_enc:
    if "-" in i:
        
        flat_enc[flat_enc.index(i)] = flat_enc[flat_enc.index(i)].split("-")

from string import ascii_lowercase
key5x5=[]

for i in range(5):
    key=[]
    for j in range(5):
        if ascii_lowercase[i*5+j] != "k" :
            key.append(ascii_lowercase[i*5+j])
        else:
            ascii_lowercase = ascii_lowercase.replace("k", "")
            key.append(ascii_lowercase[i*5+j])

    key5x5.append(key)

for i in flat_enc :
    if type(i) == list:
        print(key5x5[int(i[0])-1][int(i[1])-1],end="")
    else:
        print(i,end="")
