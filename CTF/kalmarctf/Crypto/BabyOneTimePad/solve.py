from pwn import *
# nc 3.120.132.103 13337
io = remote('3.120.132.103', 13337)

io.recvuntil(b'pad: ')
password = io.recvline().strip().decode()
# print('password :', password)
io.recvuntil(b'Permutation: ')
msg = b'0,'*128 + ','.join([str(x) for x in range(128)]).encode()
# print('msg :', msg)
io.sendline(msg)
io.recvuntil(b'encrypted with another one-time pad: ')
enc = io.recvline().strip().decode()

key = []
a = [ord(x) for x in '0123456789abcdef']

keys = []
for h1 in a:
    for h2 in a:
        KK = []
        c=1
        for x,y,z in zip(bytes.fromhex(password[:256]),bytes.fromhex(enc[:256]),bytes.fromhex(password[256:])):
            for i in range(256):
                if c%2 != 0 :
                    if (i^y) == h1 and i^x in a and i^y in a:
                        KK.append(i)
                else:
                    if (i^y) == h2 and i^x in a and i^y in a:
                        KK.append(i)
            c += 1
        if len(KK) == 128:
            keys.append(KK)

PASSWORD = ''
for i in range(len(bytes.fromhex(password))):
    PASSWORD += chr(keys[0][i%128]^bytes.fromhex(password)[i])
    print(chr(keys[0][i%128]^bytes.fromhex(password)[i]),end='')

io.recvuntil(b'password: ')
io.sendline(PASSWORD.encode())
print(io.recvline())
