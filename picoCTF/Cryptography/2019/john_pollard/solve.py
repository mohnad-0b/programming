from Crypto.PublicKey import RSA
from Crypto.Util.number import isPrime


def factors(x):
  for i in range(3, x + 1):
    if x % i == 0 and isPrime(i) :
      return i,x//i

with open("cert") as f:
    crt = f.read()

public_key = RSA.import_key(crt)
p,q= factors(public_key.n)
print("picoCTF{"+str(p)+","+str(q)+"}")
print("picoCTF{"+str(q)+","+str(p)+"}")
