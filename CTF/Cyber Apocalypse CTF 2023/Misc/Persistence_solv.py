from pwn import *
# 165.232.98.21 32031

c = 0
while True:
    io = remote('165.232.98.21',32031)
    io.sendline(b'GET /flag\n')
    out = io.recv(1024)
    print(out,c)
    if b'HTB' in out :
        print(out)
        break
    # print(c,end='\n\n')
    c += 1
# HTB{y0u_h4v3_p0w3rfuL_sCr1pt1ng_ab1lit13S!}