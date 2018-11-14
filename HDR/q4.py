import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

direction = './image/q2/'
imgCount = 3
color = ('b','g','r')
g = [2.518, 2.518, 2.518]

# i250 = cv2.imread(direction+'ISO_100_T_250.jpg')
# i125 = cv2.imread(direction+'ISO_100_T_125.jpg')
# i30 = cv2.imread(direction+'ISO_100_T_30.jpg')
# a1 = 2.0
# a2 = 8.3

i250 = cv2.imread(direction+'1.jpg')
i125 = cv2.imread(direction+'2.jpg')
i30 = cv2.imread(direction+'3.jpg')
a1 = 4425./1000
a2 = 4425./350

originalImageArr = [i250, i125, i30]
img_row = originalImageArr[0].shape[0]
img_col = originalImageArr[0].shape[1]

def hdr1_img(img_1, img_2, img_3, a1, a2):
	new_img = np.zeros((img_1.shape[0], img_1.shape[1], 3), dtype='float32')
	for row in range(0,img_1.shape[0]):
		for col in range(0,img_1.shape[1]):
			if(img_3[row,col,0] < 255 and img_3[row,col,1] < 255 and img_3[row,col,2] < 255):#use img3
				for idxColor in range(0,3):
					new_img[row,col,idxColor] = img_3[row,col,idxColor]**g[idxColor] / a2 
			elif(img_2[row,col,0] < 255 and img_2[row,col,1] < 255 and img_2[row,col,2] < 255):#use img2
				for idxColor in range(0,3):
					new_img[row,col,idxColor] = img_2[row,col,idxColor]**g[idxColor] / a1
			else:
				for idxColor in range(0,3):
					new_img[row,col,idxColor] = img_1[row,col,idxColor]**g[idxColor]
	return new_img

def hdr2_img(img_1, img_2, img_3, a1, a2):
	new_img = np.zeros((img_1.shape[0], img_1.shape[1], 3), dtype='float32')
	for row in range(0,img_1.shape[0]):
		for col in range(0,img_1.shape[1]):
			if(img_3[row,col,0] < 255 and img_3[row,col,1] < 255 and img_3[row,col,2] < 255):#use img3
				for idxColor in range(0,3):
					new_img[row,col,idxColor] = (img_3[row,col,idxColor]**g[idxColor] / a2 + img_2[row,col,idxColor]**g[idxColor] / a1 + img_1[row,col,idxColor]**g[idxColor]) / 3
			elif(img_2[row,col,0] < 255 and img_2[row,col,1] < 255 and img_2[row,col,2] < 255):#use img2
				for idxColor in range(0,3):
					new_img[row,col,idxColor] = (img_2[row,col,idxColor]**g[idxColor] / a1 + img_1[row,col,idxColor]**g[idxColor]) / 2
			else:
				for idxColor in range(0,3):
					new_img[row,col,idxColor] = img_1[row,col,idxColor]**g[idxColor]
	return new_img
new_img1 = np.zeros((img_row, img_col, 3), dtype='float32')
new_img1 = hdr1_img(originalImageArr[0], originalImageArr[1], originalImageArr[2], a1, a2)

new_img2 = np.zeros((img_row, img_col, 3), dtype='float32')
new_img2 = hdr2_img(originalImageArr[0], originalImageArr[1], originalImageArr[2], a1, a2)

def tonemap(hdr, alg):
    tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
    ldrDrago = tonemapDrago.process(hdr)
    ldrDrago = 3 * ldrDrago
    cv2.imwrite(direction+'hdr'+ alg + '_img'+'.jpg', ldrDrago * 255)

tonemap(new_img1, '1') 
tonemap(new_img2, '2') 