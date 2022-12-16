# WildRSA.py

from Crypto.Util.number import getRandomNBitInteger, bytes_to_long, long_to_bytes, getStrongPrime, isPrime

BITS = 512
SEED = 1
while SEED & 1:
SEED = getRandomNBitInteger(BITS//2)

class WildRSA:
def __init__(self, seed=getRandomNBitInteger(BITS//2)):
self.P = getStrongPrime(BITS)
self.seed = seed

    def __get_q(self, s):
        Q = s
        while not isPrime(Q+1):
            Q = s
            for _ in range(8):
                Q *= getRandomNBitInteger(32)
        return Q + 1

    def pub(self):
        N = self.P * self.__get_q(self.seed)
        return N, 0x10001

from secret import APT
obj = WildRSA(SEED)

for _, user in APT.items():
    N, E = obj.pub()
    key = N
    msg = pow(bytes_to_long(user["msg"]),E, N)
    print(key, msg)
