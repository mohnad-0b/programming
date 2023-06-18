import random

OUT = open('output2.txt', 'w')
# FLAG = open('flag.txt', 'r').read().strip()
FLAG = 'flag{8b76b85e7f450c39502e71c215f6f1fe}'
N = 64

l = len(FLAG)
arr = [random.randint(1,pow(2, N)) for _ in range(l)]
OUT.write(f'{arr}\n')

s_arr = []
out_msg =[]
for i in range(len(FLAG)-1):
    out_msg.append([f'{str(arr[j])}*ord(FLAG[{j}])' for j in range(l)])
    s_i = sum([arr[j]*ord(FLAG[j]) for j in range(l)])
    s_arr.append(s_i)
    arr = [arr[-1]] + arr[:-1]
    print(f"{'+'.join(out_msg[i])}={s_arr[i]}")
    OUT.write(f"{'+'.join(out_msg[i])}={s_arr[i]}\n")
    # break
# print(out_msg[0][0])



# OUT.write(f'{s_arr}\n')

