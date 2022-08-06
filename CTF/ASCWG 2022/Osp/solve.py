from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, isPrime
from string import printable, ascii_letters
import os

FLAG = "flag{this_is_the_flag}"

secret = os.urandom(len(FLAG))

# print("Secret:", secret)

def OSP(plain, secret):
    assert len(plain) == len(secret), 'The length has to be idenntical!'
    ct = []
    p = getPrime(256)
    print(p)
    for f, k in zip(FLAG, secret):
        print(f, k)
        ct.append((ord(f) * p + k))
    return ct, p 

# ct, p = OSP(FLAG, secret)
# open('ct.txt', 'w').write(str(ct))

flag_enc = open("output.txt", "r").read().split("\n")
# print(flag_enc[0])

P = []
for i in range(256):
    if  isPrime((int(flag_enc[0])//ord("A") - i )) :
        print(f"P: {int(flag_enc[0])//ord('A') - i}")
        P.append((int(flag_enc[0])//ord("A") - i ))

print(P)
# for i in range(256):
    # if  isPrime((int(flag_enc[1]) - (ord("S") + i ))) :
        # if (int(flag_enc[1]) - (ord("S") + i )) in P : 
            # print(f"S: {int(flag_enc[0]) - (ord('S') + i)}")

# print(8089299319622272404218984323426841677853869833958174960935658787612033517087332//ord("f")-218)


P=83801116101404762217959833436887689169125676463370468685179624854108613659563

for i in flag_enc:
    for j in range(256):
        for k in printable:
            if ord(k) * P + j == int(i):
                print(k, end="")
                break
