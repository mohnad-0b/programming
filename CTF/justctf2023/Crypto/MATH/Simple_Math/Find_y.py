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

''' 
How To find y in M = n%(y-1) ? 
n = x*y .... (1) eq1
M = n % (y-1)
M = x*y % (y-1)
M = [x%(y-1)*y%(y-1)]  ---> y%(y-1) = 1 
M = x%(y-1)
x = k(y-1) + M .... (2) eq2 # Note :  k = 1
####### Solve equ ###########
n = x*y
n = y*[(y-1) + M]  from eq1 in eq2 
y**2 + y*(M - 1 ) - n = 0 ; we have M and n :)
'''
