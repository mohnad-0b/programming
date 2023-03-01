from Crypto.Util.number import isPrime, getPrime
from sympy import *
# reverse of  `M = n%(y-1)`
x,y = getPrime(1024), getPrime(1024)
n = x*y
M = n%(y-1)
if not isPrime(M):

    t = var('t')
    Pol = t**2+t*(M-1)-n
    t=solve(Pol,t)
    print(t[1])
else :
    print(M/n)
