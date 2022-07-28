import requests
from Crypto.Util.number import inverse

req = requests.get("https://s3-eu-west-1.amazonaws.com/hubchallenges/crypto/lineq.txt")
eq = (req.text).split("\n")

for i in range(25):
    
    print(chr(int(inverse(inverse(int(eq[i].split(" ")[-1]),int(eq[i].split(" ")[4]))*int(eq[i].split(" ")[0]),int(eq[i].split(" ")[4])))%256),end="")               
