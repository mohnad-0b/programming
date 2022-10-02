def getFlag(key,enc_flag):
    fake_flag = '1234567890abcdefghijklmnopqrstuvwxyz}'
    indexs = []
    for i in key:
        indexs.append(fake_flag.index(i))
    flag = ''
    for i in range(len(enc_flag)):
        flag += enc_flag[indexs.index(i)]

    return flag

enc_flag = ''
for i in b"oz]{R]3l]]B#" :
    enc_flag += chr(i^2)

for  i in b"50es6O4tL23E":
    enc_flag += chr(i^1)

for i in b"tr3c10_F4TD2":
    enc_flag += chr(i^0)

# print(enc_flag) mx_yP_1n__@!41dr7N5uM32Dtr3c10_F4TD2
print("SEKAI{" + getFlag('167bchinotuz258adgjmpsvy3490efklqrwx',enc_flag) + "}")
# SEKAI{m4tr1x_d3cryP710N_15_Fun_M4T3_@2D2D!}