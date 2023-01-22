from Crypto.Util.number import getPrime, bytes_to_long
import random

flag1 = b"kctf{*****"
flag2 = b"******}"

p, q = getPrime(512), getPrime(512)
n = p * q
e = 0x10001
phi = (p - 1) * (q - 1) 
m = bytes_to_long(flag1)
ct = pow(m, e, n)

primes = [p, q]

for _ in range(98):
    primes.append(getPrime(512))

random.shuffle(primes)



primes2 = []

while True:
    if len(primes2) == 16:
        break
    p = getPrime(128)
    if p not in primes2:
        primes2.append(p)

while True:
    n2 = 1
    for p in primes2:
        r = random.randint(0, 1)
        if r:
            n2 *= p
    if n2.bit_length() > 1024:
        break

m2 = bytes_to_long(flag2)
ct2 = pow(m2, e, n2)

with open("infos.txt", 'w') as f:
    f.write('{}\n'.format(ct))
    f.write('{}\n'.format(ct2))

    for p in primes:
        f.write(str(p) + " ")
    f.write("\n")
    
    for p in primes2:
        f.write(str(p) + " ")
