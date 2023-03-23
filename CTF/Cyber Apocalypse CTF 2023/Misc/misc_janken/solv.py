from pwn import *
from time import time

proc1 = process('./janken')   
# proc1 = remote('139.59.176.230',32536)
proc1.recv(1024)
proc1.sendline(b'1')
t = int(time())
proc1.recv(1024)

for i in range(99):

    proc2 = process('./out')
    proc2.sendline(str(t).encode())
    rand = proc2.recv(1024).decode()
    # proc2.close()

    if rand == '0':
        print('paper')
        proc1.sendline(b'paper')
        t = int(time())

    elif rand == '1':
        print('rock')
        proc1.sendline(b'rock')
        t = int(time())

    elif rand == '2':
        print('scissors')
        proc1.sendline(b'scissors')
        t = int(time())

    print(i)
    proc1.recv(1024)
    
    sleep(0.5)

print(proc1.recv(1024).decode())
proc1.close()
