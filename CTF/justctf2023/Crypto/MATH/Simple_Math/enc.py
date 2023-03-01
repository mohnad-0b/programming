import random
from Crypto.Util.number import *
from  secret import flag,key

######################## Encryption Algorithm ######################## 

x,y = getPrime(128), getPrime(128)
n = x*y
M = n%(y-1)
a = []
for i in range(5):
    a.append(random.randint(1,133333333337))
enc = []
for x in flag:
    enc.append(((a[0]*pow(ord(x),4)+a[1]*pow(ord(x),3)+a[2]*pow(ord(x),2)+a[3]*ord(x)+a[4]))^(y%key))
file = open('flag.enc', 'w')
file.write(str(enc))
file.close()
print(M,n)
print('encryption done\n')

# M = 13296362383043221259836312481327818121
# n = 75610089333048750861240285201209617149804326723066738587197417311512110234929
