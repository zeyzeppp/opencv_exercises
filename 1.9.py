import cv2
import numpy

resim_1 = cv2.imread("yangin.jpg")

yukseklik_1 = 300
genislik_1 = 168

resim_1 = cv2.resize(resim_1, (yukseklik_1, genislik_1))

cv2.imwrite("new_yangin.jpg", resim_1)


cv2.imshow("new yangın",  resim_1)

resim_2 = cv2.imread("su.jpg")

yukseklik_2 = 300
genislik_2 = 168

resim_2 = cv2.resize(resim_2, (yukseklik_2, genislik_2))

cv2.imwrite("new_su.jpg", resim_2)

cv2.imshow("new su", resim_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
