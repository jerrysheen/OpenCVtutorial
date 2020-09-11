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


def get_contours(img_canny, img):
    # we take an **canny image** as input
    contours, hierarchy = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # contour will generate a series of edge cordinate, one set for one graph.
    img_contour = img.copy()
    # contours inside it will have several set of corrdinate represent for edge dot.
    count = 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        # print(area)
        if area > 500:
            cv.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            # peri compute the length of a curve
            peri = cv.arcLength(cnt, True)
            print(peri)
            # approxPloyDp 会回传一个近似的图形，根据原来的点长
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            obj_type = len(approx)
            # according to this series of dot, we can get a external rectangle.
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # decide shape by its numbers of vertics
            obj_name = ""
            if obj_type == 3:
                obj_name = "Tri"
            elif obj_type == 4:
                obj_name = "Rectangle"
            else:
                obj_name = "circle"
            cv.putText(img_contour, obj_name, ((x + w//3),(y + h//2)),cv.FONT_ITALIC, 0.9, (255,255,255),thickness=3)

    print(count)
    return img_contour


img = cv.imread("Resource/images/shape.png")

# convert it to gray scale
# add some gaussion blur


img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_gray, (5, 5), 0.5)
img_canny = cv.Canny(img_blur, 20, 150)
# np. zero_like, copy the array with value img.
img_blank = np.zeros_like(img)
img_contour = get_contours(img_canny, img)

img_stack = stack_images(0.5, ([img, img_gray, img_blur], [img_canny, img_contour, img_blank]))

cv.imshow("shape", img_stack)
cv.waitKey(0)
cv.destroyAllWindows()