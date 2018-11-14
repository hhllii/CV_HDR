import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

direction = './image/q2/'
imgCount = 3
color = ('b','g','r')
g = [2.0984317435303166, 1.952438298782427, 1.9665891131222188]

i250 = cv2.imread(direction+'ISO_100_T_250.jpg')
i125 = cv2.imread(direction+'ISO_100_T_125.jpg')
i30 = cv2.imread(direction+'ISO_100_T_30.jpg')
a1 = 2.0
a2 = 25/3
originalImageArr = [i250, i125, i30]

#sampling a square
imageArr = [0 for n in range(0, imgCount)]

def hdr1_data(img_1, img_2, img_3, a1, a2):
	yAxis = [[0 for n in range(0, img_1.shape[0] * img_1.shape[1])] for n in range(0, 3)]
	pixel_id = 0
	for row in range(0,img_1.shape[0]):
		for col in range(0,img_1.shape[1]):
			if(img_3[row,col,0] < 255 and img_3[row,col,1] < 255 and img_3[row,col,2] < 255):#use img3
				for idxColor in range(0,3):
					yAxis[idxColor][pixel_id] = img_3[row,col,idxColor]**g[idxColor] / a2
			elif(img_2[row,col,0] < 255 and img_2[row,col,1] < 255 and img_2[row,col,2] < 255):#use img2
				for idxColor in range(0,3):
					yAxis[idxColor][pixel_id] = img_2[row,col,idxColor]**g[idxColor] / a1
			else:
				for idxColor in range(0,3):
					yAxis[idxColor][pixel_id] = img_1[row,col,idxColor]**g[idxColor]
			pixel_id += 1
	return yAxis

def hdr2_data(img_1, img_2, img_3, a1, a2):
	yAxis = [[0 for n in range(0, img_1.shape[0] * img_1.shape[1])] for n in range(0, 3)]
	pixel_id = 0
	for row in range(0,img_1.shape[0]):
		for col in range(0,img_1.shape[1]):
			if (img_3[row,col,0] < 255 and img_3[row,col,1] < 255 and img_3[row,col,2] < 255):#use img3
				for idxColor in range(0,3):
					yAxis[idxColor][pixel_id] = (img_3[row,col,idxColor]**g[idxColor] / a2 + img_2[row,col,idxColor]**g[idxColor] / a1 + img_1[row,col,idxColor]**g[idxColor]) / 3
			elif (img_2[row,col,0] < 255 and img_2[row,col,1] < 255 and img_2[row,col,2] < 255):#use img2
				for idxColor in range(0,3):
					yAxis[idxColor][pixel_id] = (img_2[row,col,idxColor]**g[idxColor] / a1 + img_1[row,col,idxColor]**g[idxColor]) / 2
			else:
				for idxColor in range(0,3):
					yAxis[idxColor][pixel_id] = img_1[row,col,idxColor]**g[idxColor]
			pixel_id += 1
	return yAxis


#hdr_a1 plot
yAxis_a1 = hdr1_data(originalImageArr[0], originalImageArr[1], originalImageArr[2], a1, a2)
plt.xlabel('B\'g')
plt.ylabel('count')
for idxColor in range(0,3):
	plot_id = 231 + idxColor
	plt.subplot(plot_id)
	plt.hist(yAxis_a1[idxColor], bins=25, range=(0,255**g[idxColor] + 1))
	plt.grid(True)

#hdr_a2 plot
yAxis_a2 = hdr2_data(originalImageArr[0], originalImageArr[1], originalImageArr[2], a1, a2)
plt.xlabel('B\'g')
plt.ylabel('count')
for idxColor in range(0,3):
	plot_id = 234 + idxColor
	plt.subplot(plot_id)
	plt.hist(yAxis_a2[idxColor], bins=25, range=(0,255**g[idxColor] + 1))
	plt.grid(True)

plt.show()
