from struct import pack, unpack
xrange=range

def F(w):
	return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32

def decrypt(block):

	a, b, c, d = unpack("<4I", block)
	for i in xrange(32):
		# a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337
		old_a = a
		d = d ^1337
		a = c ^ (F(d | F(d) ^ d))
		b = b ^ (F(d ^ F(a) ^ (d | a)))
		c = old_a ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
		# a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337
		old_a = a
		a = d ^ 31337
		d = c ^ (F(a | F(a) ^ a))
		c = b ^ (F(a ^ F(d) ^ (a | d)))
		b = old_a ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))

	return pack("<4I", a, b, c, d)


flagenc = open("flag.enc","rb").read()
flag = b""
for i in range(0,32,16):
	flag += decrypt(flagenc[i:i+16])
print(flag)

open( "flag", "wb").write(flag)
