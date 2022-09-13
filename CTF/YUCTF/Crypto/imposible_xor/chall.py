import os

flag = b"yuctf{}"#the flag just contains letters , digits , _ , {}

key=list(b'*******')
enc = b''
for i in range(len(flag)):

	# eedede
	# eededd
	enc+=  chr(flag[i] ^ key[i%len(key)]).encode()
	if i%len(key)==0:
		r = key[0]
		del key[0]
		key.append(r)


with open('secret.enc' , 'wb') as a:
	a.write(enc)
