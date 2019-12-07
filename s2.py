import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img0 = cv2.imread("p_t.png")
img0=cv2.resize(img0,None,fx=0.35,fy=0.35,interpolation=cv2.INTER_CUBIC)
# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
print(gray.shape)
# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
#sobelx=cv2.threshold(sobelx,50,255,type=cv2.THRESH_BINARY)
ret,sobelx = cv2.threshold(sobelx,200,255,cv2.THRESH_BINARY)
ret,sobely = cv2.threshold(sobely,200,255,cv2.THRESH_BINARY)

#print(sobelx)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)

cv2.waitKey(0)