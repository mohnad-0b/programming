#! /usr/bin/env python3
from Crypto.Util.number import bytes_to_long, long_to_bytes , getPrime
msg = b'flag'
p = getPrime(1024)
q = getPrime(1024)
e = 3
n = p*q
m = bytes_to_long(msg)
print("e = ", e)
print("n = ",n)
c = pow(m, e, n)
print("c = " , c)
