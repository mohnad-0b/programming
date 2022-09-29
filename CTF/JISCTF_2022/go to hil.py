#  go to hil 300 point
import numpy as np
import string

letters = string.ascii_uppercase

def to_num(arr):
    l = []
    for i in arr:
        l.append(letters.index(i))
    return l


flags = []
cipher = "DCIEUXFJPTTLFJZOXJBQMLML"
for c in range(0,len(cipher),4):
    for i1 in letters:
        for i2 in letters:
            for i3 in letters:
                for i4 in letters:
                    flag = i1 + i2 + i3 + i4
                    flags.append(flag)

    for flag in flags:
        k = (letters[5], letters[6], letters[11], letters[13])

        key = np.array(to_num(k)).reshape(2, 2)
        ciphertext = ''
        for i in range(0, len(flag), 4):
                    enc = np.array(to_num(flag[i:i + 4])).reshape(2, 2)
                    ciphertext += ''.join([letters[i] for i in enc.dot(key).reshape(4) % len(letters)])

        if ciphertext == cipher[c:c+4]:
            print(flag, end="")
            break

# JISCTFILOVEHILLCIPHERRRR
