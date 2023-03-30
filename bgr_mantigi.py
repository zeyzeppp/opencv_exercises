import cv2
import numpy

resim = cv2.imread("fire.jpg")
cv2.imshow("fire", resim)

print(resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
