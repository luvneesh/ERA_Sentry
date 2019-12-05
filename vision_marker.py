import numpy as np
import cv2
import cv2.aruco as aruco

# we will not use a built-in dictionary, but we could
# aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# define an empty custom dictionary with 
aruco_dict = aruco.custom_dictionary(44, 5, 1)
# add empty bytesList array to fill with 3 markers later
aruco_dict.bytesList = np.empty(shape = (44, 4, 4), dtype = np.uint8)

# add new marker(s)
mybits = np.array([[0,1,1,0,0],[1,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[0] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[1] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[0,0,1,1,0],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[2] = aruco.Dictionary_getByteListFromBits(mybits)

mybits = np.array([[0,0,0,1,0],[0,0,1,1,0],[0,1,0,1,0],[1,1,1,1,1],[0,0,0,1,0]], dtype = np.uint8)
aruco_dict.bytesList[3] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,1],[1,0,0,0,0],[0,1,1,1,0],[0,0,0,0,1],[1,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[4] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,1],[1,0,0,0,0],[1,1,1,1,0],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[5] = aruco.Dictionary_getByteListFromBits(mybits)

mybits = np.array([[1,1,1,1,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0]], dtype = np.uint8)
aruco_dict.bytesList[6] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[0,1,1,1,0],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[7] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[0,1,1,1,1],[0,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[8] = aruco.Dictionary_getByteListFromBits(mybits)#9

mybits = np.array([[0,1,1,1,0],[1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[9] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,0,1,0,0],[0,1,0,1,0],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]], dtype = np.uint8)
aruco_dict.bytesList[10] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,0],[1,0,0,0,1],[1,1,1,1,0],[1,0,0,0,1],[1,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[11] = aruco.Dictionary_getByteListFromBits(mybits)#b

mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,0],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[12] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[13] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[14] = aruco.Dictionary_getByteListFromBits(mybits)#e

mybits = np.array([[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,0,0,0,0]], dtype = np.uint8)
aruco_dict.bytesList[15] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,0],[1,0,0,0,0],[1,0,1,1,1],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[16] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]], dtype = np.uint8)
aruco_dict.bytesList[17] = aruco.Dictionary_getByteListFromBits(mybits)#h

mybits = np.array([[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[18] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,0,0,0,1],[0,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[19] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,0,0,0,1],[1,0,0,1,0],[1,1,1,0,0],[1,0,0,1,0],[1,0,0,0,1]], dtype = np.uint8)
aruco_dict.bytesList[20] = aruco.Dictionary_getByteListFromBits(mybits)#k

mybits = np.array([[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[21] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,0,0,0,1],[1,1,0,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1]], dtype = np.uint8)
aruco_dict.bytesList[22] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,0,0,0,1],[1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1],[1,0,0,0,1]], dtype = np.uint8)
aruco_dict.bytesList[23] = aruco.Dictionary_getByteListFromBits(mybits)#n

mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[24] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,0],[1,0,0,0,1],[1,1,1,1,0],[1,0,0,0,0],[1,0,0,0,0]], dtype = np.uint8)
aruco_dict.bytesList[25] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,1,0],[0,1,1,0,1]], dtype = np.uint8)
aruco_dict.bytesList[26] = aruco.Dictionary_getByteListFromBits(mybits)#q

mybits = np.array([[1,1,1,1,0],[1,0,0,0,1],[1,1,1,1,0],[1,0,0,1,0],[1,0,0,0,1]], dtype = np.uint8)
aruco_dict.bytesList[27] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1,1],[1,0,0,0,0],[0,1,1,1,0],[0,0,0,0,1],[1,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[28] = aruco.Dictionary_getByteListFromBits(mybits)#s
mybits = np.array([[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]], dtype = np.uint8)
aruco_dict.bytesList[29] = aruco.Dictionary_getByteListFromBits(mybits)#t

mybits = np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[30] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0]], dtype = np.uint8)
aruco_dict.bytesList[31] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[0,1,0,1,0]], dtype = np.uint8)
aruco_dict.bytesList[32] = aruco.Dictionary_getByteListFromBits(mybits)#w

mybits = np.array([[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]], dtype = np.uint8)
aruco_dict.bytesList[33] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]], dtype = np.uint8)
aruco_dict.bytesList[34] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[35] = aruco.Dictionary_getByteListFromBits(mybits)#z

mybits = np.array([[0,1,1,1,0],[1,0,0,0,1],[0,0,1,1,0],[0,0,0,0,0],[0,0,1,0,0]], dtype = np.uint8)
aruco_dict.bytesList[36] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,0,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]], dtype = np.uint8)
aruco_dict.bytesList[37] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,1,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[38] = aruco.Dictionary_getByteListFromBits(mybits)

mybits = np.array([[0,0,1,0,0],[0,1,1,1,1],[1,1,1,1,1],[0,0,0,1,1],[0,0,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[39] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,0,1,0,0],[1,1,1,1,0],[1,1,1,1,1],[1,1,0,0,0],[1,1,0,0,0]], dtype = np.uint8)
aruco_dict.bytesList[40] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[41] = aruco.Dictionary_getByteListFromBits(mybits)

mybits = np.array([[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]], dtype = np.uint8)
aruco_dict.bytesList[42] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[43] = aruco.Dictionary_getByteListFromBits(mybits)

# # save marker images
# for i in range(len(aruco_dict.bytesList)):
#     cv2.imwrite("custom_aruco_" + str(i) + ".png", aruco.drawMarker(aruco_dict, i, 128))

# open video capture from (first) webcam
# cap = cv2.VideoCapture("dcim.mp4")

# img = cv2.imread('s1 vision markers_page-0002.jpg')
while(True ):
    # Capture img-by-img
    # ret,img=cap.read()
    # img  = cv2.imread('asdfgh.png',0)
    img = cv2.imread("result.png", cv2.IMREAD_COLOR)
    # lYellow = np.array([20,100,100])
    # uYellow = np.array([40,255,255])
    # # th, im_th = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # mask = cv2.inRange(hsv, lYellow, uYellow)
    # img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # _, img = cv2.threshold(img, 75, 255, cv2.THRESH_BINARY)
    #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, aruco_dict)
    # draw markers on farme
    img = aruco.drawDetectedMarkers(img, corners, (ids),  borderColor=(0, 255, 0))
    print(ids)

#     # resize img to show ecven on smaller screens
#     img = cv2.resize(img, None, fx = 0.6, fy = .6)
#     # Display the resulting img
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imwrite("plk.png",img)

# # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()