import string
alphabet = string.ascii_uppercase 
c = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + string.digits
users = open("usernames.txt","r").read().split("\n")
password  = open("passwords.txt","r").read().split("\n")
flag = password[users.index("cultiris")] # cvpbPGS{P7e1S_54I35_71Z3}
# ROT 13

for i in flag:
    if (i in c):
        print(i,end="")
    else:
        if (i.isupper()):
            print(alphabet[(alphabet.index(i)+13)%len(alphabet)],end="")
        else:
            print(alphabet[(alphabet.index(i.upper())+13)%len(alphabet)].lower(),end="")
    