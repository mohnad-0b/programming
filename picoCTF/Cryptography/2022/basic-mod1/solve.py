"""
Take each number mod 37 and map it to the following character set: 0-25 is the
alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
"""
import string
alphabet = string.ascii_uppercase + string.digits + "_"
f = open("./msg","r").read().split(" ")

print("picoCTF{",end="")
for i in f:
    print(alphabet[int(i)%37],end="")
print("}")