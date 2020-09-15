import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# change the color
# it means the first layer BGR B all be 255, and
# img[:] equals img[ : , : ]
img[:] = 255, 0, 0

# line:
cv.line(img, (0, 0), (240, 300), (0, 255, 255), thickness=5)
cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), thickness=5)

# rectangle
cv.rectangle(img, (0, 0), (100, 100), (0, 0, 255), thickness=5)
cv.rectangle(img, (480, 480), (img.shape[1], img.shape[0]), (0, 0, 255), cv.FILLED)


# circle
cv.circle(img, (350, 350), 30, (255, 255, 0), cv.FILLED)

# text
# thickness just like bold effect on the font.
cv.putText(img, "Hello World", (250, 60), cv.FONT_ITALIC, fontScale=1, color=(255, 0, 255), thickness=5)

cv.imshow("img", img)
cv.waitKey(0)


