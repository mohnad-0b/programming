from pwn import *
# nc code.hackerspacejust.com 5623
cor = ["R","P","S"]
c=0
io = remote('code.hackerspacejust.com', 5623)

print(io.recvuntil(b']: '))

while True:
    io.sendline(cor[c%3].encode())
    print(io.recvuntil(b']: '))
    if b"JUST" in x:
        print(x)
        break
    else :
        print(c,end='\r')
        c+=1
# JUST{HunterXHunter_G0n_1s_th3_b3s7_Janken_player}