

import cv2

image1 = cv2.imread("aruco_approach.png")  
img = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

img = img[:,:,1]
img = 255 - img

cv2.imwrite("result_.png",img)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 