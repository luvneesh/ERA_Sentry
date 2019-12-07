import cv2 as cv
cdst = cv.imread("hell1.png", cv.IMREAD_COLOR)
cv.imshow("image", cdst)
cv.waitKey(0)