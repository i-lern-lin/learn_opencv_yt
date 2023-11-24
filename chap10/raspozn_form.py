import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("track") # Создаём окно для трекбара
cv2.createTrackbar("T1","track", 0,255, nothing)
cv2.createTrackbar("T2","track", 0,255, nothing) #создаём трекбар

kernel = np.ones((5,5))

while True:
    ret, frame = cap.read()

    frame = cv2.bilateralFilter(frame, 9, 75,75) # Сглаживание
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # ЧБ

    threshold1 = cv2.getTrackbarPos("T1","track")
    threshold2 = cv2.getTrackbarPos("T2","track")

    canny = cv2.Canny(gray,threshold1,threshold2) # Canny фильтр
    dil = cv2.dilate(canny, kernel, iterations= 1)

    contours, h = cv2.findContours(dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 10000:
            cv2.drawContours(frame, contour, -1,(200,200,0), 3)
            p = cv2.arcLength(contour,True)
            num = cv2.approxPolyDP(contour, 0.02*p, True) #вершины фигуры
            # print(num) вершины обводки
            x,y,w,h = cv2.boundingRect(num) # Получаем координаты 
            print(len(num))
            cv2.rectangle(frame, (x,y, x+w,y+h), (0,0,255), 4) #рисуем квадрат вокру обводки

    cv2.imshow("frame", frame)
    cv2.imshow("dil", dil)
    cv2.imshow("canny", canny)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows
