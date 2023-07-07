import cv2
from PIL import Image

vidcap = cv2.VideoCapture('case.mp4')
success,image = vidcap.read()
count = 0
success = True
flag = ''
while success:
    cv2.imwrite("frames/frame%d.png" % count, image)     # save frame as png file      
    success,image = vidcap.read()
    Img = Image.open("frames/frame%d.png" % count)
    print(Img.getpixel(xy=(320,240)))
    if Img.getpixel(xy=(320,240)) == (252, 0, 0) :
        flag += '0'
    else:
        flag += '1'

    count += 1
print(flag)
print(bytes.fromhex(hex(int(flag,2))[2:]))


'''
b'Well, this is some exfiltration technique. This is just a demo, but in real world, it would be better implemented and better use case.\r\nWith a lot of other techniques, we can follow some here:\r\nhttps://thesecmaster.com/14-popular-air-gapped-data-exfiltration-techniques-used-to-steal-the-data/#What_Is_Air_Gapping\r\n\r\nFor this challenge, the FLAG is: FLAG{LED_DATA_EXFILTRATION}\r\n\r\n'
'''