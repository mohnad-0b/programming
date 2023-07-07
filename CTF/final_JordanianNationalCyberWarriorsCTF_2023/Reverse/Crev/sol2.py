
from string import *
import os

# def find(enc,index):
#       for c1 in ascii_letters+digits+'{}_':
#         for c2 in ascii_letters+digits:
#             os.system('echo -n '+c1+c2+' > flag.txt')
#             enc = [int(i) for i in os.popen('./Rev2.bin').read().split(' ')[:-1]]
#             if enc == flagenc[index:index+4]:
#                 return c1+c2

flagenc = [5, 11, 15, 1, 8, 1 ,1 ,12 , 15 , 9 , 12 , 5 , 5 , 0 , 4 , 3 , 8 , 6 , 15 , 8 , 15 , 11 , 6 , 1 , 2 , 6 , 12 , 1 , 14 , 11 , 15 , 6 , 0 , 5 , 0 , 12 , 7 , 1 , 3 , 1 , 5 , 0 , 4 , 3 , 3 , 2 , 1 , 0 , 7 , 0 , 10 , 3 , 5 , 5 , 8 , 13 , 0 , 0 , 0 , 14 , 11 , 5 , 10 , 14 , 6 , 4 , 8 , 7 , 5 , 14 , 14 , 12]
#         #   [5, 11, 15, 1, 8, 1, 1, 12, 3, 2, 12, 0]
#         # [5, 11, 15, 1, 8, 1, 1, 12]

# print(len(flagenc)/8)
# key = {}



# for c1 in ascii_letters+digits+'{}_' :
#         for c2 in ascii_letters+digits+'{}_' :
#             print(c1+c2)
#             os.system('echo -n '+c1+c2+' > flag.txt')
#             enc = [int(i) for i in os.popen('./Rev2.bin').read().split(' ')[:-1]]
#             key[tuple(enc)] = c1+c2

# print(key)

# open('key.txt','w').write(str(key))

key = eval(open('key.txt','r').read())
flag =''

for i in range(0,len(flagenc),4):
    print(i)
    flag += key[tuple(flagenc[i:i+4])]
print(flag)
