import cv2
import numpy

resim_1 = cv2.imread("fire.jpg")
cv2.imshow("fire", resim_1)

print(resim_1.size)
print(resim_1.dtype)
print(resim_1.shape)


resim_2 = cv2.imread("fire.jpg", 0)
cv2.imshow("gray_fire", resim_2)

print(resim_2.size)
print(resim_2.dtype)
print(resim_2.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()