from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

import os 


    

key = os.urandom(8)
flag = b'flag'

des = DES.new(key, DES.MODE_ECB)

padded_text = pad(flag,8)
encrypted_text = des.encrypt(padded_text)

print(encrypted_text.hex())

