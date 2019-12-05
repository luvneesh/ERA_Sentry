import cv2
import numpy as np
img = cv2.imread("trafnformed_w:o_hoe.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 26 , 96)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 15, maxLineGap=100)
print(lines[1])
for line in lines:


   x1, y1, x2, y2 = line[0]
   cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)

cv2.imwrite("hoelines.png",img)   
cv2.imshow("linesEdges", edges)
cv2.imshow("linesDetected", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
