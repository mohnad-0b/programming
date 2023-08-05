from Crypto.Util.number import long_to_bytes
from pwn import *

while True:
    try :
        io = remote('34.154.18.2',6951)
        Public = io.recvline().split(b'(')[1].split(b')')[0].split(b',')
        p = int(Public[0])
        g = int(Public[1])
        A = int(Public[2])
        print(p,g,A)
        sign = io.recvline().split(b' ')
        S1 = int(sign[0])
        pow(S1,-1,p-1)
        break
    except :
        continue
while True:
    try :
        sign1 = io.recvline().split(b' ')
        S1 = int(sign1[0])
        S2 = int(sign1[1])
        m = int(sign1[2])
        sign2 = io.recvline().split(b' ')
        S2_ = int(sign2[1])
        m_ = int(sign2[2])
        d = pow(m-m_,-1,p-1)
        k = ((S2-S2_)*d)%(p-1)
        k_inv = pow(k,-1,p-1)
        flag_int = ((((k_inv*S2)%(p-1)*-1 + m%(p-1))%(p-1))*pow(S1,-1,p-1))%(p-1)
        flag = long_to_bytes(flag_int)
        print(flag)
        break

    except :
        continue
#ASCWG{R3uS31n9_G4m4l_NoNc3_S19n1n9_1s_50o_B4d_b4b48c08}
