import cv2
import numpy

resim_1 = cv2.imread("fire.jpg")
cv2.imshow("fire", resim_1)

resim_2 = cv2.imread("fire.jpg", 0)
cv2.imshow("gray_fire", resim_2)

cv2.waitKey(0)
cv2.destroyAllWindows()