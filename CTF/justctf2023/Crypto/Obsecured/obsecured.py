import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random

def obfuscate(key):
    key = bytearray(key)
    print(random.randint(*sorted(key[:2])))
    random.seed(random.randint(*sorted(key[:2])))
    random.shuffle(key)
    return key

flag = b""
flag = pad(flag, AES.block_size)

key = os.urandom(16)

cipher = AES.new(key, AES.MODE_CBC, key)

# print(f"encrypted_flag = {cipher.encrypt(flag).hex()}")
print(f"obfuscated_key = {obfuscate(key).hex()}")