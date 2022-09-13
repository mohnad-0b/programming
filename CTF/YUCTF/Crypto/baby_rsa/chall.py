from Crypto.Util.number import getPrime , bytes_to_long
flag = bytes_to_long(b'flag')
p = getPrime(128)
q= getPrime(128)
n = p*q
e= 0x10001

print('N' , n )
print('e' , e )
print('c' , pow(flag,e,n))

