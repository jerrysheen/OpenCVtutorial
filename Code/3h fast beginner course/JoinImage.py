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


img = cv.imread('../../Resource/images/lena.jpg')

# horizontally or vertically combine two images.
imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgStack = stack_images(0.5, ([img, img_gray, img],[img, img, img]))
print(type(img))

array = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]])
zero = np.zeros((1,3))
print(np.hstack(array))
# cv.imshow("result", imgStack)
# cv.waitKey(0)
# cv.destroyAllWindows()