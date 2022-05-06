to send msg `story0 to story37`
```python
import  pyautogui as pg
import time

time.sleep(5)
for i in range(38):
    msg = f"story {i}"
    pg.write(msg)
    pg.press('Enter')
    time.sleep(2)
```
copy all msg to `lol.txt`
find all `u200C` to `0` & `u200D` to `1`
```python
f = open("lol.txt", "r")
flag = ""
c = 0
for i in f.read().split() :

    if c == 8 :
        # print(" ",end="")
        flag = flag + " "

        c = 0        
    if "u200C" in i :
        # print("0",end="")
        flag = flag + "0"

        c = c + 1
    elif "u200D" in i :
        # print("1",end="")
        flag = flag + "1"
        c = c + 1
flag = flag.split(" ")
for i in flag:
    if i != "":
        print(chr(int(i,2)),end="")
```
`lag{e4e5ad33eb16426d52b94e398e593466}`
