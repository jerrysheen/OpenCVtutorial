import cv2 as cv
import numpy as np


def stack_images(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    # if the input is a single img ? the instance compare will result false;
    rows_avaliable = isinstance(imgArray[0], list)
    # be careful here, height is the first parameter
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    # if it has multiple rows
    if rows_avaliable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[0][0].shape[:2] == imgArray[x][y].shape[:2]:
                    # if two image is same size, then we don't need to resize,(0, 0) ,
                    # we only need to care about scale.
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale, None)
                else:
                    # first resize then scale.
                    imgArray[x][y] = cv.resize(imgArray[x][y], imgArray[0][0].shape[:2], None, scale, scale, None)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        # what will happen here?
        imageBlank = np.zeros((height, width, 3), np.uint8)
        #print(imageBlank.shape)
        # this step, array become an list, thins like {imageBlank, imageBlank, imageBlank....}
        hor = [imageBlank]*rows
        #print(hor)
        for x in range(0, rows):
            # 这里就只是把原来的位置赋值给处理完成后的array
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2] :
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale, None)
            else:
                # first resize then scale.
                imgArray[x] = cv.resize(imgArray[x], imgArray[0].shape[:2], None, scale, scale, None)
            if len(imgArray[x].shape == 2):
                imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def empty(a):
    #print(a)
    pass


# how to use trackbar and hsv mask

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)
# the first one stands for initial value
cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv.imread("Resource/images/lambo2.jpg")
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lowb = np.array([h_min, s_min, v_min])
    upperb = np.array([h_max, s_max, v_max])
    mask = cv.inRange(img_hsv,lowerb=lowb, upperb=upperb)
    img_color = cv.bitwise_and(img, img, mask=mask)
    total = stack_images(1, ([img, img_hsv], [mask, img_color]))
    cv.imshow("total", total)
    cv.waitKey(1000)
