import cv2
import numpy

resim = cv2.imread("fire.jpg")

resim[50, 30] = [0, 0, 255] #pixel

for i in range(100) : #çizgi şekli oluşturur
    resim[30, i] = [255, 255, 255]

cv2.imshow("fire", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()









