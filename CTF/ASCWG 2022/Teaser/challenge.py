from Crypto.Util.number import bytes_to_long, long_to_bytes, getStrongPrime, getRandomNBitInteger
from time import time_ns
from secret import p, q, FLAG

BITS = 512

N = p * q

a, b, x = [getRandomNBitInteger(64) for _ in range(3)]
s = x*(a * x + b) + 1
inf = -x*(a * x + b)
FLAG = bytes_to_long(FLAG)

c1 = pow(FLAG, s, N)
c2 = pow(FLAG, inf, N)

q1 = (x*a*c1 + b*c2 + a*b) % N
q2 = (a*c2 - x*b*c1 + a*b) % N

print(f"{N=}\n{q1=}\n{q2=}")
hint = x**5 + a*b*x**4 + b*x**3 - (a*b**2)*x**2 + (b*a**2)*x - (b**2)*(a**2)
print(f"{hint=}\n{a=}\n{b=}")

'''
N=136172654412975696672277699911326568930906766030832704596331587851913580572236893811129555165206299271122442434714570487317929463308920741438574074555215146250641537240478488340634101606111041980010829107689359885402204793049862837890400636654700457420935273510878322624221066308139237364134968330182982837219
q1=129700851577911833951546779649879386781363652757273181746564105468579589496221524015498600435486574591787516500081344266887101103166695795763627773287485087193020550446476318981445160008866376604043109183290785818082565090275386881955913967486969291033661943236500735834562836343585517551647242966723167449078
q2=106187520824836916140530981655653639328217502775479926753617707156322730832324365295797538549177802527036773048825921792473140235119964421139149577764124882650810667324422218800463880704315570077101568050089773823894917651766606738325184195516375067069083002909431495903494276122403106230525955048238146574777
hint=6573544964235663795110387821358621068738264530355319754834598296204350028845729399053875214556575503920004379593112
a=12011053116152205388
b=11423234452039057359
'''