import sys
from PIL import Image, ImageDraw, ImageFont
payload = sys.argv[1].replace("\\n","\n")
out = Image.new("RGB", (2500, 900), (255, 255, 255))
d = ImageDraw.Draw(out)
fnt = ImageFont.truetype("arialbd.ttf", 100) # if you use windos is good 
# fnt = ImageFont.truetype("Pillow/Tests//FreeMonoBold.ttf", 30) # if you use linux is good 
d.multiline_text((50,50 ),f"{payload}",fill=(0, 0, 0),font=fnt)
# out.show() # if you need show imag remov comment :)
out.save("imag.png","PNG")
