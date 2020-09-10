import cv2 as cv


def read_img():
    # This function is used for reading img
    img = cv.imread("Resource/images/lena.jpg")
    print(img)
    cv.imshow("image", img)


def read_video():
    cap = cv.VideoCapture("Resource/videos/road_lane.mp4")
    while True:
        res, img = cap.read()
        cv.imshow("video", img)
        # waitKey 0 means one single frame will stuck forever, waitKey 1 means 1 frame last for 1 ms.
        if cv.waitKey(200) & 0xff == ord('q'):
            break


def read_webcam():
    w = 3
    h = 4
    brightness = 10
    cap = cv.VideoCapture(0)
    # cap.set(brightness, 100)
    # dont know how to change the resolution, seems we can only use the original resolution.
    # original resolution 1280, 720
    while True:
        res, img = cap.read()
        flip = cv.flip(img, 1)
        cv.imshow("video", flip)
        # waitKey 0 means one single frame will stuck forever, waitKey 1 means 1 frame last for 1 ms.
        if cv.waitKey(1) & 0xff == ord('q'):
            break


# read_img()
# read_video()
read_webcam()
# meli second or infinite run
cv.waitKey(0)
cv.destroyAllWindows()