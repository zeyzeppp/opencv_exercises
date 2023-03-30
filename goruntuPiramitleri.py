import cv2
import numpy


resim = cv2.imread("yangin.jpg")
iki_kat_buyuk = cv2.pyrUp(resim) #iki kat buyutme
iki_kat_kucuk = cv2.pyrDown(resim) #iki kat kucultme

print("orijinal resim", resim.shape)
print("iki kat buyuk resim", iki_kat_buyuk.shape)
print("iki kat kucuk", iki_kat_kucuk.shape)
print(resim.shape)
print(iki_kat_buyuk.shape)
print(iki_kat_kucuk.shape)

cv2.imshow("yangın", resim)
cv2.imshow("buyuk yangın", iki_kat_buyuk)
cv2.imshow("kucuk yangın", iki_kat_kucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()

