import cv2 as cv
import numpy as np

# 模糊操作，本质上就是操作卷积，不同的卷积核会得到不同的模糊效果
# 卷积核大小一般都是奇数的，可以有中心。  中心的值等于卷积核乘上它附近值的平均值


# 均值模糊
def mean_blur(img):
    # kernel (horizontally, vertically)
    res = cv.blur(img, (9, 9))
    cv.imshow("mean blur", res)


# 中值模糊，一般用来去除椒盐噪声，图像上有一颗颗的黑色的点，如果用均值模糊来去除，效果不是特别好
def median_blur(img):
    res = cv.medianBlur(img, 5)
    cv.imshow("median blur", res)


# 自定义模糊
# 卷积也可以进行锐化等操作。
def custom_blur(img):
    # 25 是因为kernel有25个数，取平均
    kernel = np.ones((5,5), np.float32)/25
    res = cv.filter2D(img, -1, kernel)
    cv.imshow("custom_blur", res)


# 高斯模糊，去掉噪声更加实用。
# Gx = 1 / sqrt(2 * pi * sigma) * e ^(- x^2 / 2 * sigma^2)这里的 x 表示的是 距离kernel的距离，
# 比如九宫格中，以中心（1，1）为中心，（0，0）就距离中心-1，-1，所以他的概率则是0.2,0.2
# 为了方便计算，我们会把kernel和近似成整数，例如我们现在的kernel是（1, 3）,那么概率分别是0.2, 0.4, 0.2.我们会把它
# 化成整数 1， 2， 1， 然后再把总和 * 1/4. 相当于我们保证每一个像素点最后最大值还是255， 但是它的权重是根据高斯分布得到的

# 加速方法： 在做3*3的kernel的时候，我们相当于做了9次乘法，对每个格子。如果把其分离成横着的矩阵和竖着的1 * 3矩阵，就可以加速计算？
# 存疑，需要进一步证明

# 因为知道了sigma可以求x，所以kernel和sigmax只需要一个值就可以求出另外一个，另外一个设置为0就好了
# 相比起均值模糊，因为高斯模糊对local点的权重更加的高，所以它更加能保留原图的特征
def gaussian_blur(img):
    res = cv.GaussianBlur(img,(9,9),0)
    cv.imshow("gaussian_blur",res)

# a named window can help enlarge or shirnk our img
cv.namedWindow("custom_blur", cv.WINDOW_NORMAL)
img = cv.imread("Resource/images/lena.jpg")
mean_blur(img)
gaussian_blur(img)
cv.waitKey(0)
cv.destroyAllWindows()
