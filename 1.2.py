import cv2
import numpy

resim = cv2.imread("gray_fire.jpg")

for x in range(301) :
    resim[30, x] = [250, 157, 77]


cv2.imshow("gray_fire", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()