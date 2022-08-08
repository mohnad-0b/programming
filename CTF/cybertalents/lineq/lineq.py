import requests
from Crypto.Util.number import inverse

req = requests.get("https://s3-eu-west-1.amazonaws.com/hubchallenges/crypto/lineq.txt")
eq = (req.text).split("\n")


for i in range(25):

# 15345857135052644158 * x[0] mod 15914389274045831441 = 10753153698913165324
# 10753153698913165324 * X = 15345857135052644158 (mod 15914389274045831441)

    print(chr(inverse(inverse(int(eq[i].split(" ")[-1]),int(eq[i].split(" ")[4]))*int(eq[i].split(" ")[0]),int(eq[i].split(" ")[4]))%256),end="")
