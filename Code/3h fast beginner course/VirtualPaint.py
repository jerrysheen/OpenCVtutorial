import cv2 as cv
import numpy as np


# orange, grren,
my_colors = [[46, 92, 23, 83, 255, 198]]
# record the color.
my_points = []

def findColor(img, my_colors):
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowb = np.array(my_colors[0][0:3])
    upperb = np.array(my_colors[0][3:6])
    mask = cv.inRange(img_hsv,lowerb=lowb, upperb=upperb)
    return mask


def get_contours(mask, color_img):
    # we take an **canny image** as input
    # you dont have to run canny image? only 1 channel image is fine
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # contour will generate a series of edge cordinate, one set for one graph.

    # contours inside it will have several set of corrdinate represent for edge dot.
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        # print(area)
        if area > 500:
            cv.drawContours(color_img, cnt, -1, (0, 255, 0), 3)
            # peri compute the length of a curve
            peri = cv.arcLength(cnt, True)
            #print(peri)
            # approxPloyDp 会回传一个近似的图形，根据原来的点长
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            # according to this series of dot, we can get a external rectangle.
            x, y, w, h = cv.boundingRect(approx)
            # decide shape by its numbers of vertics
    return x + w//2, y


def drawOnCanvas(img, my_points):
    for point in my_points:
        cv.circle(img,(point[0], point[1]),20, (0, 255 ,0), cv.FILLED)


cap = cv.VideoCapture(0)
while True:
    res, img = cap.read()
    flip = cv.flip(img, 1)
    color_img = flip.copy()
    mask = findColor(flip, my_colors)
    x, y = get_contours(mask, color_img)
    if x != 0 and y != 0:
        my_points.append([x,y])
    drawOnCanvas(color_img, my_points)
    # img_color = cv.bitwise_and(flip,flip, mask= img_contour)
    cv.imshow("video", color_img)
    # waitKey 0 means one single frame will stuck forever, waitKey 1 means 1 frame last for 1 ms.
    if cv.waitKey(1) & 0xff == ord('r'):
        my_points.clear()
    if cv.waitKey(1) & 0xff == ord('q'):
        break;

