import cv2
import numpy as np


# создаём объект с порядковым номером камеры
capt = cv2.VideoCapture(0)

print(f"Состояние камеры: {capt.isOpened()}")

while True:
    # Идёт ли видеопоток(True/False) и картинка
    ret,frame = capt.read(0)
    cv2.imshow("Video", frame) # Выводит видео поток

    # Размываем изображение
    blur = cv2.blur(frame, (21,21)) #ядро не чётное 
    gblur = cv2.GaussianBlur(frame,(21,21), 0) # Гаус размытие
    bblur = cv2.bilateralFilter(frame, 21, 75, 75) #Билетеральное размытие

    cv2.imshow("bblur", bblur)
    cv2.imshow("blur", blur)
    cv2.imshow("gblur", gblur)
    # Ждём нажатие кнопки 
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

capt.release()
cv2.destroyAllWindows()
