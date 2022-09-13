flag_enc = open('cipher.enc' , 'rb').read()

key = b'perfecto'
flag = ""
for i in range(len(flag_enc)):
    
    flag += (chr(flag_enc[i] ^ key[i%len(key)]))
    if key[i%len(key)] == ord('U') : 
        print(chr(flag_enc[i] ^ key[i%len(key)]))

print(flag)

# yuctf{X0r_15_r3v3rsible}