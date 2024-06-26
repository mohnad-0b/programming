#!/usr/bin/env python3

import os

PASS_LENGTH_BYTES = 128

def encrypt_otp(cleartext, key = os.urandom(PASS_LENGTH_BYTES)):
    # ciphertext = []
    # for i,x in enumerate(cleartext.hex().encode()):
    #     print(i,x,key[i % len(key)])
    #     ciphertext.append(key[i % len(key)] ^ x)
    ciphertext = bytes([key[i % len(key)] ^ x for i,x in enumerate(cleartext.hex().encode())])
    return ciphertext, key


if __name__ == '__main__':
    print('According to Wikipedia:')
    print('"In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a single-use pre-shared key that is not smaller than the message being sent."')
    print('So have fun trying to figure out my password!')
    password = os.urandom(PASS_LENGTH_BYTES)

    enc, key = encrypt_otp(password)
    print(f'Here is my password encrypted with a one-time pad: {enc.hex()}')
    print('Actually, I will give you my password encrypted another time.')
    print('This time you are allowed to permute the password first')
    # permutation = input('Permutation: ')
    permutation = [0 for i in range(128)]
    print(f'first chr in password is {password[0]}\n{password=}\n{key=}\n')
    try:

        # assert set(permutation) == set(range(PASS_LENGTH_BYTES))
        enc, key = encrypt_otp(bytes([password[permutation[i]] for i in range(PASS_LENGTH_BYTES)]))
        print(f'Here is the permuted password encrypted with another one-time pad: {enc.hex()}')
        print(f'\n\n{key=}')
    except:
        print('Something went wrong!')
        exit(1)
    password_guess = input('What is my password: ')
    try:
        password_guess = bytes.fromhex(password_guess)
    except:
        print('Something went wrong!')
        exit(1)
    if password_guess == password:
        with open('flag.txt', 'r') as f:
            flag = f.read()
            print(f'The flag is {flag}')
    else:
        print(password.hex())
        print('Nope.')
