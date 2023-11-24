import cv2
import numpy as np

capt = cv2.VideoCapture(0)
cv2.namedWindow("frame")

while True:
    ret, frame = capt.read()
    # Переводим изображение в чёрнобелый формат
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Градиент
    # framex = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    # framey = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    edge = cv2.Canny(gray, 40, 150) # фильтр 

    contours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # Ищем контуры
    contours = sorted(contours, key = cv2.contourArea, reverse=True) #Сортировка контуров
    cv2.drawContours(frame, [contours[0]], -1, (0,0,255), 5) # Рсиуем контуры



    # Показываем окна
    cv2.imshow("frame", frame)  
    # cv2.imshow("x", framex)  
    # cv2.imshow("y", framey)  
    cv2.imshow("edge", edge)
   
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
