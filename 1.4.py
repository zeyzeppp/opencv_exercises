import cv2
import numpy

ronaldo = cv2.imread("ronaldo.jpg")
print(ronaldo.shape)
face = ronaldo[0:70, 130:200]


ronaldo[50:120, 200:270] = face


cv2.imshow("ronaldo's face", face)
cv2.imshow("ronaldo", ronaldo)


cv2.waitKey(0)
cv2.destroyAllWindows()