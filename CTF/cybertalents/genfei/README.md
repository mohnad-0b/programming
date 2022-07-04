*Challenge Name: [genfei](https://cybertalents.com/challenges/cryptography/genfei)*                    
*Category: Cryptography*             
*Level: medium*

### Challenge Description
```
We found an encrypted secret and an encrypting machine. It seems to be a complicated cipher, can you break it?
```
you have 

encrypt.py 

```python
import sys
from struct import pack, unpack

def F(w):
	return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32

def encrypt(block):
	a, b, c, d = unpack("<4I", block)
	for rno in xrange(32):
		a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337
		a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337
	return pack("<4I", a, b, c, d)

pt = open(sys.argv[1]).read()
while len(pt) % 16: pt += "#"

ct = "".join(encrypt(pt[i:i+16]) for i in xrange(0, len(pt), 16))
open(sys.argv[1] + ".enc", "w").write(ct)
```

and flag.enc 

```
P
��ي ܮ��hq�>ޒ�b	��M�S\��j
```
to solve error : `NameError: name 'xrange' is not defined`

```python 
xrange=range
```
we need create `dycrbt` function first step extract a,b,c,d use
```python
a, b, c, d = unpack("<4I", block)
```
second step reverse `xor` to each char a,b,c,d use
```python
# a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337

d = d ^1337
a = c ^ (F(d | F(d) ^ d))
b = b ^ (F(d ^ F(a) ^ (d | a)))
c = a ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
# a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337

a = d ^ 31337
d = c ^ (F(a | F(a) ^ a))
c = b ^ (F(a ^ F(d) ^ (a | d)))
b = a ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))
```
but it not work because we need save value of `a` then
```python
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
```
now we have function to decrypt

```python
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

```

*If you want any question, contact me*     
*Discord : mohnad#9100*      
*[LinkedIn](https://www.linkedin.com/in/mohnad-banat/)*   
