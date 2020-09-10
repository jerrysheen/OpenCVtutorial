import cv2 as cv
import numpy as np

img = cv.imread("Resource/images/cars.jpg")

print(img.shape)

# resize
img2 = cv.resize(img, (100, 50))
cv.imshow("original", img)
cv.imshow("modified", img2)

cv.waitKey(0)
cv.destroyAllWindows()