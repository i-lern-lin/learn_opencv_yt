import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    # Проверяем идет ли поток ret == True - изображение есть, frame - поток
    ret, frame = cap.read(0)
    # Переводим видео поток в серый цвет
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Создаём фильтры - пороги
    #Фильр размытия: Что хотим сделать, поток, границы, метод размытия
    ret, t1 = cv2.threshold(frame, 127,255, cv2.THRESH_BINARY)
    ret, t2 = cv2.threshold(frame, 127,255, cv2.THRESH_BINARY_INV)
    ret, t3 = cv2.threshold(frame, 127,255, cv2.THRESH_TRUNC)
    ret, t4 = cv2.threshold(frame, 127,255, cv2.THRESH_TOZERO)
    ret, t5 = cv2.threshold(frame, 127,255, cv2.THRESH_TOZERO_INV)

# Окна фильтров  
    cv2.imshow("t1", t1)
    cv2.imshow("t2", t2)
    cv2.imshow("t3", t3)
    cv2.imshow("t4", t4)
    cv2.imshow("t5", t5)

    cv2.imshow("frame", frame) #Рисуем окно


    key = cv2.waitKey(1) & 0xFF # ждём нажатия и отпущенной клавиши
    if key == 27: # Проверяем клавиша Esc нажата и отпущена
        break # Выходим из цикла

cv2.destroyAllWindows() # Закрываем все окна какие есть.