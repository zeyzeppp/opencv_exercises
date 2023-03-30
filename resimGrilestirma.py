import cv2
import numpy

resim = cv2.imread("yangin.jpg")
resimGri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# resim = cv2.imread("yangin.jpg", 0) buda resmi grileştirir.
# yukseklik, genislik, kanal sayisi



cv2.imshow("orijinal_resim", resim)
cv2.imshow("gri_resim", resimGri)

cv2.waitKey(0)
cv2.destroyAllWindows()