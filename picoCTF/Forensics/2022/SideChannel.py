import os
from time import sleep , time
import time
tr = []
P = ""
password="11111111"  
for j in range(8) : 
    print("[+]"+"-"*100+"[+]")
    for i in range(10) :
        password = password[:j] + str(i) + password[j+1:] ; print("password is " + password)
        start_time = time.time()
        os.system("echo "+password+" | ./pin_checker")
        run_time =float(time.time() - start_time)
        tr.append(run_time)
        sleep(0.5)
    password = password[:j] + str(tr.index(max(tr))) + password[j+1:]
    tr = [] 
    print("-"*106)
print(password)
