flagenc = open("flag", "rb").read()
FLAG = []
for i in range(0, len(flagenc), 2):
    FLAG.append(hex(flagenc[i])[2:].zfill(2))

open("flag.png", "wb").write(bytes.fromhex("".join(FLAG)))