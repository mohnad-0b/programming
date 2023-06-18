import os
from pwn import *


while True:
    # nc challenge.nahamcon.com 31837
    io = remote('challenge.nahamcon.com', 31837,level='warn')
    io.recvline()
    first_part = io.recvline().decode().split(':')[-1].strip()
    print(first_part)
    io.recvuntil(b'Choice:')
    io.sendline(b'1')
    io.recvuntil(b'msg (hex):')
    io.sendline(b'moh'.hex().encode())

    sha1 = io.recvline().decode().split(':')[-1].strip()
    print(f'hash: {sha1}')

    coll = os.popen(f'./hashpump -s {sha1} -d "moh" -k 64 -a "{first_part}"').read().strip()
    tag = coll[:40]
    msg = b'moh'.hex() + ''.join(coll[41+len('moh'):-len(first_part)].split('\\x')) + first_part.encode().hex()
    print(f'msg: {msg}')
    print(f'tag: {tag}')

    io.recvuntil(b'Choice:')
    io.sendline(b'3')
    io.recvuntil(b'msg (hex):')
    io.sendline(msg.encode())
    io.recvuntil(b'tag (hex):')
    io.sendline(tag.encode())
    rev = io.recv(1024).decode()
    if 'flag' in rev:
        print(rev)
        break
    print(rev,'failed :(')
    io.close()