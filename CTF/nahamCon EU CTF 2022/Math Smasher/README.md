## **Math Smasher**

*346 points - Scripting - 46 Solves -* `medium`



```py
from PIL import Image
from pytesseract import pytesseract
import requests


url = 'http://challenge.nahamcon.com:32560' # u port 
conter = 0

def ORC(image):
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    return text

while True:
    try:

        # download the image
        r = requests.get(url+'/static/eqn.png', allow_redirects=True) 
        open('eqn.png', 'wb').write(r.content)
        orc = ORC('eqn.png')
        
        if chr(176) in orc:
            orc = orc.replace(chr(176), '*')
        orc = orc.replace(' ',"")  
        orc = orc.replace("\n","")  
        
        eqn_ans= round(eval(orc), 4)
        print(f"[{conter}] {orc} = {eqn_ans}")
        conter += 1
        
        # send the answer
        data = {'eqn_ans': eqn_ans}
        r = requests.post(url, data=data)

        # download the flag image
        r = requests.get(url+'/static/flag.png', allow_redirects=True)
        if r.status_code == 200:
            open('flag.png', 'wb').write(r.content)
            flag = ORC('flag.png')
            print(f"FLAG = {flag}")
            break
    except :
        print(ORC('eqn.png').replace(' ',''))
        print(eval(ORC('eqn.png').replace(' ','')))
        break
```
**FLAG**: `flag{7058813988514da4070026045010887}`
