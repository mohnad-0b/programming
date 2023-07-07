
from string import ascii_letters, digits 
import os



flagenc = [5, 11, 15, 1, 8, 1 ,1 ,12 , 15 , 9 , 12 , 5 , 5 , 0 , 4 , 3 , 8 , 6 , 15 , 8 , 15 , 11 , 6 , 1 , 2 , 6 , 12 , 1 , 14 , 11 , 15 , 6 , 0 , 5 , 0 , 12 , 7 , 1 , 3 , 1 , 5 , 0 , 4 , 3 , 3 , 2 , 1 , 0 , 7 , 0 , 10 , 3 , 5 , 5 , 8 , 13 , 0 , 0 , 0 , 14 , 11 , 5 , 10 , 14 , 6 , 4 , 8 , 7 , 5 , 14 , 14 , 12]
        #   [5, 11, 15, 1, 8, 1, 1, 12, 3, 2, 12, 0]
        # [5, 11, 15, 1, 8, 1, 1, 12]

print(len(flagenc)/8)
key = {}
for c1 in ascii_letters+digits+'{}_':
    for c2 in ascii_letters+digits+'{}_':
        for c3 in ascii_letters+digits+'{}_':
            for c4 in ascii_letters+digits+'{}_':
                os.system('echo -n '+c1+c2+c3+c4+' > flag.txt')
                enc = [int(i) for i in os.popen('./Rev2.bin').read().split(' ')[:-1]]
                print(c1+c2+c3+c4)
                # key[c1+c2+c3+c4] = enc
                
                key[tuple(enc)] = c1+c2+c3+c4
print(key)

# 

flag=''
for i in range(0,len(flagenc),8):
    flag += key[tuple(flagenc[i:i+8])][0]
print(flag)