from pwn import *
from sage.all import *

io = remote('34.154.18.2',6952,)
data = io.recvline().split(b'(')[1].split(b')')[0].split(b',')
# q, g, h, c1, c2
q = int(data[0])
g = int(data[1])
h = int(data[2])
c1 = int(data[3])
c2 = int(data[4])

R = IntegerModRing(q)
y = discrete_log(R(c1), R(g))
assert pow(g,y,q) == c1
s = pow(h,y,q)
print(bytes.fromhex(hex((c2*pow(s,-1,q))%q)[2:]))
#ASCWG{H0w_5m0o0zy_E1G4m4l_c@n_B3_964dc75a}
