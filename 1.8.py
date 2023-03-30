import cv2
import numpy

resim_1 = cv2.imread("yangin.jpg")
resim_2 = cv2.imread("su.jpg")

print(resim_1.shape)
print(resim_2.shape)

cv2.imshow("yangın", resim_1)
cv2.imshow("su", resim_2)

cv2.waitKey(0)
cv2.destroyAllwindows()


