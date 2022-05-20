from pwn import *
from string import printable
host = "localhost"
port = 1337
io = remote(host, port)

def find_lenth():

    data =b''
    io.sendlineafter(b'> ', data)
    lenth = (len(io.recv())-1)
    for i in range(20):
        io.sendlineafter(b'> ', b'aa'*i)
        new_lenth = (len(io.recv())-1)
        if new_lenth > lenth :
            print(i,new_lenth)
            break

flag = ""
flagb = b""

def find_4byts(flag=flag,flagb=flagb):
    for j in range(4):
        io.sendlineafter(b'> ', b'aa'*(3-j))
        blook_should_be = io.recv()[:32]
        for i in printable:
            data = ord(i).to_bytes(1, 'big').hex().encode()
            io.sendlineafter(b'> ', b'aa'*(3-j) + flagb + data)
            blook =io.recvline()[:32]
            if blook == blook_should_be:
                flag += i
                flagb += data 
                break
    return flag,flagb

flag,flagb = find_4byts()

def find_16byts(flag=flag,flagb=flagb):
    for j in range(16):
        io.sendlineafter(b'> ', b'aa'*(15-j))
        blook_should_be = io.recv()[32:64]
        for i in printable:
            data = ord(i).to_bytes(1, 'big').hex().encode()
            io.sendlineafter(b'> ', b'aa'*(15-j) + flagb + data)
            blook =io.recvline()[32:64]
            if blook == blook_should_be:
                flag += i
                flagb += data 
                break
    return flag,flagb

flag,flagb = find_16byts()

def find_full_flag(flag=flag,flagb=flagb):
    for j in range(5):

        for i in printable:
            data = ord(i).to_bytes(1, 'big').hex().encode()
            
            io.sendlineafter(b'> ',flagb[:8] + flagb[10+j*2:] + data + b'aa'*(11-j))

            recv = io.recvline()
            blook = recv[32:64]
            blook_should_be = recv[96:128]
            

            if blook == blook_should_be:
                flag += i
                flagb += data
                break
    print(flag)

find_full_flag()
