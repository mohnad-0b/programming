# tshark -2 -r swaal.pcap  -T fields -e data > file.hex
f = open('file.hex','r').read()

data = f.replace('\n','').split('0a')
flag = ['']*(len(data[0]))

for i in data:
    for j in range(0,len(i),2):
        if  int(i[j:j+2],16):
            flag[(j//2)] = chr(int(i[j:j+2],16))
print(''.join(flag))

# kalmar{if_4t_first_you_d0nt_succeed_maybe_youre_us1ng_udp}
