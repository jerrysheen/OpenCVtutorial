import cv2 as cv
import numpy as np



def empty(a):
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

cap = cv.VideoCapture(0)
while True:
    res, img = cap.read()
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
    cv.imshow("total", mask)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
