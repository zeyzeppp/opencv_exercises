import cv2
import numpy

resim_1 = cv2.imread("yangin.jpg")
resim_2 = cv2.imread("su.jpg")

cv2.imshow("yangın", resim_1)
cv2.imshow("su", resim_2)
print(resim_1.shape)
print(resim_2.shape)

print(resim_1[110, 200])
print(resim_2[105, 120])

cv2.waitKey()
cv2.destroyAllWindows()

