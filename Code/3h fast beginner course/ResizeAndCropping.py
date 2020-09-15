import cv2 as cv
import numpy as np

img = cv.imread("../../Resource/images/cars.jpg")

print(img.shape)

# resize
img2 = cv.resize(img, (0, 0), None, 1, 1    , None)
cv.imshow("original", img)
cv.imshow("modified", img2)

# crop image.
# or you can write as img3 = img[40:150, 0: 200]
# note, it starts with height then width.
img3 = img[40:150, 0: 200, :]
cv.imshow("cropping", img3)

cv.waitKey(0)
cv.destroyAllWindows()