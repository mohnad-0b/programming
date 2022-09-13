
flag_enc = open('secret.enc' , 'rb').read()
key=list(b'eededeeddedeedeedeededdeededeeedededededededededeeededeeddedee') # USE function to generate this key and alot of guesses :)

for i in range(0,len(flag_enc)):

    print(chr(flag_enc[i] ^ key[i%len(key)]), end='')
    if i%len(key)==0 and i!=0:
        r = key[0]
        del key[0]
        key.append(r)

# yuctf{4_c0mpl3x_X0r_1mpl3m3ntat10n_w1ll_n0t_s0lve_Th3_pr0blem}