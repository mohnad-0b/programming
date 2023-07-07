import cv2
import numpy as np
import time

width, height = 640, 480
fps = 5
output_filename = 'case.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
light_radius = 50
light_color_on = (0, 255, 0)
light_color_off = (0, 0, 255)
file = open('flag.txt','rb').read()
binary_input = ''.join(format(i, '08b') for i in file)

for bit in binary_input:
	frame = np.zeros((height, width, 3), dtype=np.uint8)
	if bit == '1':
		center_x = int(width / 2)
		center_y = int(height / 2)
		cv2.circle(frame, (center_x, center_y), light_radius, light_color_on, -1)
	else:
		center_x = int(width / 2)
		center_y = int(height / 2)
		cv2.circle(frame, (center_x, center_y), light_radius, light_color_off, -1)
	out.write(frame)
	

out.release()


# extract frames from a video and save to directory as 'x.png'br

