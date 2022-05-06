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
copy all msg and past [here](https://www.soscisurvey.de/tools/view-chars.php) and save in `lol.txt`
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

> you can show source page and use `zwnj` & `zwj` instead of `u200C` & `u200D`

![image](https://user-images.githubusercontent.com/75941340/167118146-f1111f2c-8b69-40d6-9911-cee4c1e93a0a.png)


