import cv2
import numpy as np


def nothing():
    pass

capt = cv2.VideoCapture(0)
cv2.namedWindow("frame")

cv2.createTrackbar("HI", "frame", 0, 180, nothing)
cv2.createTrackbar("SL", "frame", 0, 255, nothing)
cv2.createTrackbar("VL", "frame", 0, 255, nothing)

cv2.createTrackbar("H", "frame", 0, 180, nothing)
cv2.createTrackbar("S", "frame", 0, 255, nothing)
cv2.createTrackbar("V", "frame", 0, 255, nothing)


while True:
    ret, frame = capt.read()
    hcv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hi = cv2.getTrackbarPos("HI","frame")
    sl = cv2.getTrackbarPos("SL","frame")
    vl = cv2.getTrackbarPos("VL","frame")

    h = cv2.getTrackbarPos("H","frame")
    s = cv2.getTrackbarPos("S","frame")
    v = cv2.getTrackbarPos("V","frame")

    lower = np.array([hi,sl,vl])
    upper = np.array([h,s,v])
    mask = cv2.inRange(hcv, lower,upper)

    res = cv2.bitwise_and(frame,frame,mask=mask)



    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
