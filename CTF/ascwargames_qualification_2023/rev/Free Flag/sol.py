from Crypto.Util.number import *

def dec(arg1,arg2):
    return arg1 >> 5 | arg1 << 3

flagenc =long_to_bytes(2767022067221555752)[::-1]+long_to_bytes(12603582931989325414)[::-1]+long_to_bytes(16980236692028812902)[::-1]+long_to_bytes(44965)[::-1]
for i in flagenc:
    print(chr(dec(i, 3)%256),end='')
