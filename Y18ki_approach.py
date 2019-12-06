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

img = cv2.imread("result_.png", cv2.IMREAD_COLOR)

corners, ids, rejectedImgPoints = aruco.detectMarkers(img, aruco_dict)

bot_location_x = int(1920/2)
bot_location_y = int(1080/2)

aruco_distance = []
nearest_top = 0
nearest_left = 0
nearest_right = 0
nearest_bottom = 0
corner=corners[1]
# print(corner[0][:,0])
for i, corner in enumerate(corners):
    mid_x = np.sum(corner[0][:,0])/4
    mid_y = np.sum(corner[0][:,1])/4
    distance = ((mid_x-bot_location_x)**2+(mid_y-bot_location_y)**2)
    aruco_distance.append(distance)
    print(mid_x, bot_location_x)
    if mid_x > bot_location_x:
        print('e')
        if aruco_distance[nearest_right] > distance:
            nearest_right = i
            print('updated')

    if mid_x < bot_location_x:
        if aruco_distance[nearest_left] > distance:
            nearest_left = i

    if mid_y > bot_location_y:
        if aruco_distance[nearest_top] > distance:
            nearest_top = i

    if mid_y < bot_location_y:
        if aruco_distance[nearest_bottom] > distance:
            nearest_bottom = i


    
# print(ids)

img = aruco.drawDetectedMarkers(img, [corners[nearest_bottom], corners[nearest_left], corners[nearest_right], corners[nearest_top]], (ids[:4]),  borderColor=(0, 255, 0))
cv2.circle(img, (bot_location_x, bot_location_y), 20, (0, 0, 255), thickness=-1)
cv2.imwrite('y18.png', img)