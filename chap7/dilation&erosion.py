Поиск точных контуров объекта




from shutil import ExecError
import cv2
import numpy as np


def nothing():
    pass


kernel = np.ones((5, 5), np.uint8)


capt = cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.namedWindow("track")

cv2.createTrackbar("HI", "track", 0, 180, nothing)
cv2.createTrackbar("SL", "track", 0, 255, nothing)
cv2.createTrackbar("VL", "track", 0, 255, nothing)

cv2.createTrackbar("H", "track", 0, 180, nothing)
cv2.createTrackbar("S", "track", 0, 255, nothing)
cv2.createTrackbar("V", "track", 0, 255, nothing)


while True:
    ret, frame = capt.read(0)
    hcv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hi = cv2.getTrackbarPos("HI", "track")
    sl = cv2.getTrackbarPos("SL", "track")
    vl = cv2.getTrackbarPos("VL", "track")

    h = cv2.getTrackbarPos("H", "track")
    s = cv2.getTrackbarPos("S", "track")
    v = cv2.getTrackbarPos("V", "track")

    lower = np.array([hi, sl, vl]) # Минимальный уровень цвета
    upper = np.array([h, s, v]) # Уровень цвета
    frame = cv2.bilateralFilter(frame, 9, 75, 75)  # Размываем изображение
    mask = cv2.inRange(hcv, lower, upper) # Накладываем маску с параметрами цвета
    res = cv2.bitwise_and(frame, frame, mask=mask)

    edge = cv2.Canny(mask, 100, 200)  # фильруем контуры

    countours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # Поиск контуров
    contours = sorted(countours, key=cv2.contourArea, reverse=True) # Сортировка контуров

    try:
        cv2.drawContours(frame, [contours[0]], -1,(255, 0, 0), 5) # Отрисока контуров
    except Exception:
        print()

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    # erosion = cv2.erode(mask,kernel,iterations=1)
    # dilation = cv2.dilate(mask,kernel,iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # closing = cv2.morphologyEx(ope,cv2.MORPH_CLOSE, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # cv2.imshow("er",erosion)
    # cv2.imshow("di",dilation)
    # cv2.imshow("open",opening)
    cv2.imshow("close", closing)

    #cv2.imshow("frame", frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
