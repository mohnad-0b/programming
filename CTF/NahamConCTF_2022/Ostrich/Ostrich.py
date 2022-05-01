import imageio
from PIL import Image, GifImagePlugin
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
import random
from apng import APNG

im = APNG.open("result.apng")
for i, (png, control) in enumerate(im.frames):
  png.save("{i}.png".format(i=i))


image_name = f'ostrich.jpg'
image_open = Image.open(image_name)
pixels = image_open.load()
images = []
pixels_orgin = image_open.load()

for i in range(38):
    image_name = f'./images/{i}.png'
    image_open = Image.open(image_name)
    pixels = image_open.load()
    width, height = image_open.size
    images = []
    pixels = image_open.load()

    for i in range(width):
        for j in range(height):
            if  pixels[i,j] != pixels_orgin[i,j]:
                print(chr(b2l(l2b(pixels[i,j][0])+l2b(pixels[i,j][1]))//pixels_orgin[i,j][2]),end="")
