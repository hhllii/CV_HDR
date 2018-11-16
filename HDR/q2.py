import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

direction = './image/q2/'
imgCount = 3
color = ('b','g','r')
g = [2.098, 1.952, 1.966]

i500 = cv2.imread(direction+'ISO_100_T_500.jpg')
i250 = cv2.imread(direction+'ISO_100_T_250.jpg')
i90 = cv2.imread(direction+'ISO_100_T_90.jpg')
a1 = 2
a2 = 25/3
originalImageArr = [i500, i250, i90]

#sampling a square
imageArr = [0 for n in range(0, imgCount)]

def hist_image_data(img, a):
	yAxis = [[0 for n in range(0, img.shape[0] * img.shape[1])] for n in range(0, 3)]
	pixel_id = 0
	for row in range(0,img.shape[0]):
		for col in range(0,img.shape[1]):
			for idxColor in range(0,3):
				yAxis[idxColor][pixel_id] = img[row,col,idxColor]**g[idxColor] / a
			pixel_id += 1
	return yAxis
	
#image1 plot
yAxis = hist_image_data(i90, a2)
plt.xlabel('B\'g')
plt.ylabel('count')
for idxColor in range(0,3):
	plot_id = 331 + idxColor
	plt.subplot(plot_id)
	plt.hist(yAxis[idxColor], bins=25, range=(0,255**g[idxColor] + 1))
	plt.grid(True)

#image2 plot
yAxis = hist_image_data(i250, a1)
  
plt.xlabel('B\'g')
plt.ylabel('count')
for idxColor in range(0,3):
	plot_id = 334 + idxColor
	plt.subplot(plot_id)
	plt.hist(yAxis[idxColor], bins=25, range=(0,255**g[idxColor] + 1))
	plt.grid(True)

#image3 plot
yAxis = hist_image_data(i500, 1)
  
plt.xlabel('B\'g')
plt.ylabel('count')
for idxColor in range(0,3):
	plot_id = 337 + idxColor
	plt.subplot(plot_id)
	plt.hist(yAxis[idxColor], bins=25, range=(0,255**g[idxColor] + 1))
	plt.grid(True)
	
plt.show()
