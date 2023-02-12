from pwn import *
from sympy.ntheory.primetest import is_square 

# lac.tf 31190
io = remote('lac.tf', 31190)
io.recvline()
io.recvline()

C = 0

while C != 150:
    c = int((io.recvline().decode()).split(" ")[-1])
    if c%6 == 0 and is_square(c//6):
        io.sendline(b"1")
    else:
        io.sendline(b"0")
    C += 1
    print(C,end="\r")
print(io.recv(1024))
print(io.recv(1024))

# lactf{sm4ll_pla1nt3xt_sp4ac3s_ar3n't_al4ways_e4sy}