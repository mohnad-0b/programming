from itertools import permutations
import random

def encrypt_stage_one(message, key):
    res = ''
    for i in key:
        for j in range(i, len(message), len(key)):
            res += message[j]
    return res

def getFlag(flag_test):
    fake_flag = 'SEKAI{1234567890abcdefghijklmnopqrstuvwxyz}'
    indexs = []
    for i in flag_test:
        indexs.append(fake_flag.index(i))
    enc_flag = '5!K3rn{T_5SA!}0ypC11uu__E__3j5LFI0Esr0m_1!1'
    flag = ''
    for i in range(len(enc_flag)):
        flag += enc_flag[indexs.index(i)]

    return flag

now = ''
flag_enc = open("flag.enc","rb").read()
for i in flag_enc[-18:]:
    now += chr(i^0x42)

now = now.encode('utf-8')
now = now + "".join("0" for _ in range(len(now), 18)).encode('utf-8')

random.seed(now)
flag = ''

for i in flag_enc[:-18]:
    flag += chr(random.randrange(256)^i)
# print(f"flag_enc : {flag}")

for key in list(permutations([0, 1, 2, 3, 4, 5, 6, 7])):
        flag_test = 'SEKAI{1234567890abcdefghijklmnopqrstuvwxyz}'
        key = list(key)
        for _ in range(42):
            flag_test = encrypt_stage_one(flag_test, key)
        if flag_test.index('}') == flag.index('}') and flag_test.index('{') == flag.index('{') and flag_test.index('S') == flag.index('S') and  flag_test.index('K') == flag.index('K') and flag_test.index('A') == flag.index('A') and flag_test.index('I') == flag.index('I'):

            # print(f"key: {key}                                                   ")
            key = list(key)
            print(getFlag(flag_test))
            exit()
        else:
            # print(f"wrong key {key} , {flag_test}",end='\r')
            continue


# key is  [6, 3, 7, 4, 2, 1, 0, 5]
# flag enc is 5!K3rn{T_5SA!}0ypC11uu__E__3j5LFI0Esr0m_1!1
# fake flag enc is  wzK4rl{1s7SAx}no9bc6eqg8k5pamftvIiEh0d3juy2
# flag is SEKAI{T1m3_15_pr3C10u5_s0_Enj0y_ur_L1F5!!!}