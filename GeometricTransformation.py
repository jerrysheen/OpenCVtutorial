import numpy as np
import cv2 as cv
import math

img = cv.imread("Resource/images/lena.jpg")


# 平移，利用到了矩阵的平移，它是从现在的图像到原图的一种映射。][
def shifted_img(img, shift_x, shift_y):
    M = np.array([[1, 0, shift_x], [0, 1, shift_y]], np.float32)
    res = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return res


# rotation :
# first we try forward mapping, to see what's the problem here
# matrix multiply using numpy.dot
# source ： https://blog.csdn.net/lkj345/article/details/50555870
def forward_rotate(degree, img):
    # shape 里面是height最开始。
    h, w, o = img.shape
    print(img.shape)
    new_w = math.ceil(abs(w * math.cos(degree) + h * math.sin(degree)))
    new_h = math.ceil(abs(w * math.sin(degree) + h * math.cos(degree)))
    m1 = np.array([[1, 0, 0], [0, -1, 0], [-0.5 * w, 0.5 * h, 1]], np.float32)
    m2 = np.array([[math.cos(degree), - math.sin(degree), 0], [math.sin(degree), math.cos(degree), 0], [0, 0, 1]], np.float32)
    m3 = np.array([[1, 0, 0], [0, -1, 0], [0.5 * new_w, 0.5 * new_h, 1]], np.float32)
    # new 的时候是width 先开始
    new_img = np.zeros((new_w, new_h, o), np.uint8)
    #print(new_img.shape)
    for i in range(w):
        for j in range(h):
            new_coordinate = np.array([i, j, 1], np.float32).dot(m1).dot(m2).dot(m3)
            col = math.ceil(new_coordinate[0])
            row = math.ceil(new_coordinate[1])
            #print(new_coordinate)
            new_img[row, col, 0] = img[i, j, 0]
            new_img[row, col, 1] = img[i, j, 1]
            new_img[row, col, 2] = img[i, j, 2]
    #可以看到我们刚才说的映射问题就出现了
    cv.imshow("res", new_img)



def backward_rotate(degree, img):
    # shape 里面是height最开始。
    h, w, o = img.shape
    print(img.shape)
    new_w = math.ceil(abs(w * math.cos(degree) + h * math.sin(degree)))
    new_h = math.ceil(abs(w * math.sin(degree) + h * math.cos(degree)))
    m1 = np.array([[1, 0, 0], [0, -1, 0], [-0.5 * new_w, 0.5 * new_h, 1]], np.float32)
    m2 = np.array([[math.cos(degree), math.sin(degree), 0], [-math.sin(degree), math.cos(degree), 0], [0, 0, 1]],
                  np.float32)
    m3 = np.array([[1, 0, 0], [0, -1, 0], [0.5 * w, 0.5 * h, 1]], np.float32)
    new_img = np.zeros((new_w, new_h, o), np.uint8)
    # print(new_img.shape)
    for i in range(new_w):
        for j in range(new_h):
            old_coordinate = np.array([i, j, 1], np.float32).dot(m1).dot(m2).dot(m3)
            col = math.ceil(old_coordinate[0])
            row = math.ceil(old_coordinate[1])
            if col < 0 or col >= h or row < 0 or row >= w :
                new_img[i, j] = 0
            else:
                new_img[i, j, 0] = img[row, col,0]
                new_img[i, j, 1] = img[row, col, 1]
                new_img[i, j, 2] = img[row, col, 2]
    cv.imshow("backword_ rotate", new_img)

# 原理就相当于进行了一系列的旋转，平移，拉伸
def warp_affine(img):
    rows, cols, ch = img.shape
    print(img.shape)
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv.getAffineTransform(pts1, pts2)

    res = cv.warpAffine(img, M, (cols, rows))
    cv.imshow("warp", res)


#print(img.shape)
#res = shifted_img(img, 100, 5)

#forward_rotate(math.pi/6, img)
img2 = cv.imread("Resource/images/drawing.png")
warp_affine(img2)
cv.imshow("origin", img2)
backward_rotate(math.pi/3, img)
cv.waitKey(0)
cv.destroyAllWindows()