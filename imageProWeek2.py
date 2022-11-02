import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("myImage.jpg")

cv2.imshow("nature",image1)
print(image1.size)
cv2.waitKey(0)

row = 256
col = 256

img = np.zeros((row,col))

img[100:105, : ] = 1
img[ : ,100:105 ]=0.5 #these two are for colors
plt.figure(figsize=(15,4))#This is for the printing table size only
plt.imshow(img) #ploting process
plt.show()


height = 512
width = 512

img = np.random.randint(255,size=(height,width,1),dtype=np.uint8)

cv2.imshow('Binary',img)
plt.imshow(img)
plt.show()

# Matrices
A=[[1,4,5],
   [-5,8,9],
   [6,8,10],
   [0,2,38]
   ]
print("A =",A)
print("A[1] = ",A[1])
print("A[1][2] = ", A[1][2])
print("A[0][-1] = ", A[0][-1])


c = np.array([[1,1,2],[3,5,3],[5,6,9]])
print(c[:2]) #The 2 first elements of the matrix are printed
s = sum(sum(c[:]))
print("The Sum of all matrix elements : " , s)






