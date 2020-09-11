import cv2 as cv
import numpy as np

img = cv.imread("Resource/images/cards.jpg")
print(img.shape)

width, height = 250, 350
# 首先先知道原理就是通过目标图和原图之间的一个坐标投影来实现的，具体是怎么样的之后在学
pts1 = np.float32([[124, 234], [305, 198], [170, 500], [370, 460]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv.getPerspectiveTransform(pts1, pts2)
print(matrix)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("cards.jpg", img)
cv.imshow("output", imgOutput)
cv.waitKey(0)
