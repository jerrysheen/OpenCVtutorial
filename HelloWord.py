import cv2 as cv

img = cv.imread("lena.jpg")
print(img)
cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()