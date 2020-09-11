import cv2 as cv

# what is face cascade
# It is a machine learning based approach where a cascade function is trained from a lot
# of positive and negative images. It is then used to detect objects in other images.
# Here we will work with face detection.

face_cascade = cv.CascadeClassifier("Resource/cascades/haarcascade_frontalface_default.xml")
img = cv.imread('Resource/images/face.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# it will derectly contains a rectangle face region
faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

img_resize = cv.resize(img,(0,0),None, 0.4, 0.4)
cv.imshow("gray", img_gray)
cv.imshow("Result", img_resize)
cv.waitKey(0)