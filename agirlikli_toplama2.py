import cv2
import numpy

resim_1 = cv2.imread("new_yangin.jpg")
resim_2 = cv2.imread("new_su.jpg")

toplam = cv2.add(resim_1, resim_2)
agirlikli_toplam = cv2.addWeighted(resim_1, 0.6, resim_2, 0.4, 0)


cv2.imshow("new yangın", resim_1)
cv2.imshow("new su", resim_2)
cv2.imshow("su+yangın_toplama", toplam)
cv2.imshow("su+yangın_agırlıklı-toplam", agirlikli_toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()