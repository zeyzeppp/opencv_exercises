import cv2
import numpy

resim = cv2.imread("fire.jpg")

cv2.rectangle(resim, (100, 130), (200,20), [0, 0, 255], 3)


print(resim.shape)
cv2.imshow("fire", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()