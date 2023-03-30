import cv2
import numpy

yukseklik = 40
genislik = 20

ronaldo = cv2.imread("face.jpg")
ronaldo = cv2.resize(ronaldo, (yukseklik, genislik))

cv2.imshow("ronaldo's face", ronaldo)
cv2.imwrite("little_ronaldo.jpg", ronaldo)
cv2.waitKey(0)
cv2.destroyAllWindows()