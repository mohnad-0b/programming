syslog = open("syslog", "r") # file dumping all the USB events on his Linux host all year
auth = open("auth.json","r") # auth file
auth = auth.read()

for i in  syslog.read().split("\n"):
    if " SerialNumber: " in i : # you can use "Manufacturer" or "Product" 
        if i.split(" ")[-1] not in auth:
            print(f"\033[1;31m{ i.split(' ')[-1] } ===> HACKER\033[0;0m")
            break
        else :
            print(f"\033[1;32m{ i.split(' ')[-1] } ===> OK\033[0;0m")
