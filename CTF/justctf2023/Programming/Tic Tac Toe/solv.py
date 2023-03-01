from pwn import *
# nc code.hackerspacejust.com 8423
io = remote('code.hackerspacejust.com', 8423)

for _ in range(20):
    io.recvline()
print(io.recvline())
while True:
    print("+------------------+")
    
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    
    print("+------------------+")

    io.sendline(b'2,2')
    io.recvline()
    lineone = io.recvline().replace(b'\n', b'')
    linetwo = io.recvline().replace(b'\n', b'')
    linethre = io.recvline().replace(b'\n', b'')

    print(f'lineone: {lineone}')
    print(f'linetwo: {linetwo}')
    print(f'linethre: {linethre}')

    if (lineone.decode()).split(' | ')[0].strip() == 'X':
        print("13")

        io.sendline(b'1,3')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        io.sendline(b'3,1')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
#  solve message
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())

    elif (lineone.decode()).split(' | ')[-1].strip() == 'X':
        print("11")

        io.sendline(b'1,1')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        io.sendline(b'3,3')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
#  solve message
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())


    elif (linethre.decode()).split(' | ')[0].strip() == 'X' :
        print("33")
        io.sendline(b'3,3')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        io.sendline(b'1,1')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
#  solve message
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())

    elif (linethre.decode()).split(' | ')[-1].strip() == 'X' :
        print("31")
        io.sendline(b'3,1')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        io.sendline(b'1,3')
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
#  solve message
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())
        print(io.recvline())

    else :
        print("lol")
        print(f"{lineone.decode().split(' | ')[0].strip()}")
        print(f"{lineone.decode().split(' | ')[-1].strip()}")
        print(f"{linethre.decode().split(' | ')[0].strip()}")
        print(f"{linethre.decode().split(' | ')[-1].strip()}")