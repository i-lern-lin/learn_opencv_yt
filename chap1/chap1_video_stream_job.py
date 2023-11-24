import cv2
import numpy as np


# создаём объект с источником видео
capt = cv2.VideoCapture("@dvachannel (8).mp4")
print(f"Состояние камеры: {capt.isOpened()}")

while True:
    # Идёт ли видеопоток(True/False) и картинка
    ret,frame = capt.read()
    cv2.imshow("Video", frame)
    # Ждём нажатие кнопки 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capt.release()
cv2.destroyAllWindows()

