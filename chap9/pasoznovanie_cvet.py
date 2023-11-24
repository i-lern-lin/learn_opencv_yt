from collections import Counter
import cv2
import numpy as np
import time

def nothing(x):
    pass

kernel = np.ones((5,5),np.uint8)

cap = cv2.VideoCapture(0)

cv2.namedWindow("track", cv2.WINDOW_NORMAL)

cv2.createTrackbar("HI", "track", 0, 180, nothing)
cv2.createTrackbar("SL", "track", 0, 255, nothing)
cv2.createTrackbar("VL", "track", 0, 255, nothing)

cv2.createTrackbar("H", "track", 0, 180, nothing)
cv2.createTrackbar("S", "track", 0, 255, nothing)
cv2.createTrackbar("V", "track", 0, 255, nothing)


while True:
    ret, frame = cap.read(0)

    # Фильтрация в кадре
    frame = cv2.bilateralFilter(frame, 9, 75, 75)



    hcv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    h = cv2.getTrackbarPos("H", "track")
    s = cv2.getTrackbarPos("S", "track")
    v = cv2.getTrackbarPos("V", "track")

    hi = cv2.getTrackbarPos("HI", "track")
    sl = cv2.getTrackbarPos("SL", "track")
    vl = cv2.getTrackbarPos("VL", "track")



    lower = np.array([hi, sl, vl]) # Минимальный уровень цвета
    upper = np.array([h, s, v]) # Уровень цвета
    # frame = cv2.bilateralFilter(frame, 9, 75, 75)  # Размываем изображение
    mask = cv2.inRange(hcv, lower, upper) # Накладываем маску с параметрами цвета
    res = cv2.bitwise_and(frame, frame, mask=mask)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # Рисуем контуры, берем слой closing, он наиболее чистый, и исщем контуры на нём
    contours, h = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Сортировка контуров от ошибок, берем только большие контуры
    contours = sorted(contours, key = cv2.contourArea, reverse=True)

    for x in range(len(contours)):
        area = cv2.contourArea(contours[x])
        if area > 300:
            x,y,w,h = cv2.boundingRect(contours[x])
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0),) # Выделяем квадратом обнаруженную область
            frame = cv2.rectangle(frame, (x,y), (x+60, y-25),(0,0,0), -1) # Квадарат для текста 
            frame = cv2.circle(frame,(x + (w//2), y + (h//2)), 20,(0,255,0), -1) # Рисуем круг по центру объекта
            print(f"x: {x + (w//2)}; y: {y + (h//2)};") # пишем в stdout координаты выделенных цветов. 
            frame = cv2.putText(frame, "yellow",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255),2) # Текст

    cv2.imshow("mask", mask)
    cv2.imshow("close", closing)
    cv2.imshow("frame", frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
