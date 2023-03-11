from Crypto.Cipher import AES
import random

for s in range(256) :
    keytest = bytearray(bytes.fromhex("000102030405060708090a0b0c0d0e0f"))
    random.seed(s)
    random.shuffle(keytest)
    KEY = {}
    for i in bytearray(bytes.fromhex("000102030405060708090a0b0c0d0e0f")) :
        KEY[i] = keytest.index(i)
    keyenc = bytes.fromhex("ce1443a779a2c9a41caf2ce9fff59114")
    key = ''
    for i in bytearray(bytes.fromhex("000102030405060708090a0b0c0d0e0f")):
        key += hex(keyenc[KEY[i]])[2:].zfill(2)
    key = bytes.fromhex(key)

    cipher = AES.new(key, AES.MODE_CBC, key)
    if b"JUST{" in (cipher.decrypt(bytes.fromhex("ad97b306418ff145ea037c2e611155f99e0542d93023c03f0b99f1887ec2a398ac1063519b7e7ffd1aba158899322d14"))) :
        print(s,key.hex(),cipher.decrypt(bytes.fromhex("ad97b306418ff145ea037c2e611155f99e0542d93023c03f0b99f1887ec2a398ac1063519b7e7ffd1aba158899322d14")))
    # if this not work, try https://gchq.github.io/CyberChef/
