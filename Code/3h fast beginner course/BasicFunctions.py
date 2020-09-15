import cv2 as cv
import numpy as np
img = cv.imread("../../Resource/images/lena.jpg")

# convert to gray scale


def to_gary():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    cv.waitKey(0)
    cv.destroyWindow()


# odd number, sigma 0,
def blur_img():
    blur = cv.GaussianBlur(img, (7, 7), 0)
    cv.imshow("blur", blur)
    cv.imshow("compare", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# canny
def canny_img():
    # 　high value stands for less edge
    canny = cv.Canny(img, 100, 100)
    cv.imshow("canny", canny)
    cv.waitKey(0)
    cv.destroyAllWindows()

# dialation : let the canny edge become more wild and big


def dilation():
    kernal = np.ones((3, 3), np.uint8)
    canny = cv.Canny(img, 200, 200)
    img_dialation = cv.dilate(canny, kernal, iterations=1)
    # erosion destroty 
    img_eroded = cv.erode(img_dialation, kernal, iterations=1)
    cv.imshow("canny", canny)
    cv.imshow("dialation image", img_dialation)
    cv.imshow("eroded image", img_eroded)
    cv.waitKey(0)
    cv.destroyAllWindows()




# to_gary()
# blur_img()
# canny_img()
dilation()