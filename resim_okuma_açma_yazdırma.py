import cv2
import numpy as np

resim = cv2.imread("fire.jpg", 0)
cv2.imshow("fire", resim)
cv2.imwrite("gray_fire.jpg", resim)


cv2.waitKey(0)
cv2.destroyAllWindows()





