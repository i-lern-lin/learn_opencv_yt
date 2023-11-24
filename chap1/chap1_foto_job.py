import cv2
import numpy as np

#Обьект класса cv2, с функцией прочитать 
img = cv2.imread("logocv.png", 1)
# размер окна
cv2.namedWindow("logocv.png", cv2.WINDOW_NORMAL)

# Показываем картинку
cv2.imshow("logocv.png", img)
# Ждем нажатия клавиши.
cv2.waitKey(0)
cv2.destroyAllWindows()


