import cv2
import numpy as np
# Создаём изображение библиотекой numpy
# разрешение, каналы, unit8 - 8bit(2^8) цвет

img = np.zeros((300, 300, 3),np.uint8)
# cv2.line(img,(x1,y1),(x2,y2),(B,R,G),T) T - толщина
cv2.line(img, (10,10),(720,640),(140,160,180),5)

# cv2.rectangle(img,(x1,y1), (x2,y2), (B,R,G), T)
cv2.rectangle(img, (10,10),(720,777),(140,160,180),5)

#cv2.circle(img, (x,y), R,(B,R,G), T)
cv2.circle(img, (340,300), 300,(120, 160, 90), -1)

#cv2.putText(img, text, (x,y), font, S, (B,G,R), T, cv2.LINE_AA)
text = "Hello World"
cv2.putText(img, text, (300,300), 2, 1, (16,120,22), 2, cv2.LINE_AA)



# Показать
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()




