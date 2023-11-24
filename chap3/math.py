import cv2
import numpy as np

img1 = cv2.imread("./chap3/1.jpg")
img2 = cv2.imread("./chap3/1.png")

resaize1 =cv2.resize(img1,(1000,720))
resaize2 =cv2.resize(img2,(1000,720))


#s = cv2.add(resaize1, resaize2)
#s = cv2.subtract(resaize2, resaize1)
s = cv2.addWeighted(resaize1, 1, resaize2, 0.4,0)

# name windows & what
cv2.imshow("add", s)

cv2.waitKey(0)
cv2.destroyAllWindows()
