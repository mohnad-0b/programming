"""
Take each number mod 41 and find the modular inverse for the result. Then map to the following
character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
"""
import string
from Crypto.Util.number import inverse

alphabet = string.ascii_uppercase + string.digits + "_"
f = open("./msg","r").read().split(" ")

print("picoCTF{",end="")
for i in f:
    print(alphabet[inverse(int(i),41)-1],end="")

print("}")