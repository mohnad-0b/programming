flag = b'yuctf{}'
key = b'********'
cipher = b''

for i in range(len(flag)):
	cipher+= chr(flag[i] ^ key[i%len(key)]).encode()
with open('cipher.enc' , 'wb') as f :
	f.write(cipher)
