import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

direction = './image/q1/'
exampleSize = 200 #even number
imgCount = 8
color = ('b','g','r')

i350 = cv2.imread(direction+'350.jpg')
i250 = cv2.imread(direction+'250.jpg')
i180 = cv2.imread(direction+'180.jpg')
i125 = cv2.imread(direction+'125.jpg')
i90 = cv2.imread(direction+'90.jpg')
i60 = cv2.imread(direction+'60.jpg')
i45 = cv2.imread(direction+'45.jpg')
i30 = cv2.imread(direction+'30.jpg')

originalImageArr = [i350, i250, i180, i125, i90, i60, i45, i30]
#sampling a square
imageArr = [0 for n in range(0, imgCount)]
OutputNameList = ['o350', 'o250', 'o180', 'o125', 'o90', 'o60', 'o45', 'o30']
for i,img in enumerate(originalImageArr):
	imageArr[i] = img[(img.shape[0]//2-exampleSize//2):(img.shape[0]//2+exampleSize//2),(img.shape[1]//2-exampleSize//2):(img.shape[1]//2+exampleSize//2)]
	cv2.imwrite(direction+OutputNameList[i]+'.jpg',imageArr[i])


xAxis = [1/350, 1/250, 1/180, 1/125, 1/90, 1/60, 1/45, 1/30]
xAxisLog = [math.log2(xAxis[n]) for n in range(0, imgCount)]
yAxis = [[0 for n in range(0, imgCount)] for n in range(0, 3)] #seperate row by b,g,r
yAxisLog = [[0 for n in range(0, imgCount)] for n in range(0, 3)] 


for idx,img in enumerate(imageArr):
	for idxColor,clr in enumerate(color):
		singleChannelBrightness = 0
		for row in range(0,exampleSize):
			for col in range(0,exampleSize):
				singleChannelBrightness += img[row,col,idxColor]
		yAxis[idxColor][idx] = singleChannelBrightness/(exampleSize*exampleSize)
		yAxisLog[idxColor][idx] = math.log2(yAxis[idxColor][idx])
			
regressionList = [0,0,0] #b,g,r

print(yAxis)
#ploy B' T
plt.subplot(221)  
plt.xlabel('T(s)')
plt.ylabel('B\'')
for i,col in enumerate(color):
	plt.plot(xAxis,yAxis[i],col+'-o')
plt.grid(True)

#plot log base
plt.subplot(222)  
plt.xlabel('log T(s)')
plt.ylabel('log B\'')
for i,col in enumerate(color):
	plt.plot(xAxisLog,yAxisLog[i],col+'-o')
	z = np.polyfit(xAxisLog, yAxisLog[i], 1)
	regression = np.poly1d(z)
	plt.plot(xAxisLog,regression(xAxisLog),col+'--')
	regressionList[i] = z
	print(col + ':')
	print(regression)

plt.grid(True)
g = [1/(regressionList[n][0]) for n in range(0, 3)]
print(g)

#plot B'g
plt.subplot(223)  
plt.xlabel('T(s)')
plt.ylabel('B = B\'g')
for i,col in enumerate(color):
	plt.plot(xAxis,yAxis[i]**(g[i]), col+'-o')


plt.grid(True)
plt.show()
