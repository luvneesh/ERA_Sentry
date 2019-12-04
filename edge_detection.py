import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('qwerty.png',0)
for i in range(2000):
    edges = cv2.Canny(img,i,200)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    
    plt.show()