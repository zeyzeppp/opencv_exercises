import cv2
import numpy as np


resim = cv2.imread("alex.png")
print(resim.shape)

aynalanan_resim = cv2.copyMakeBorder(resim, 75, 75, 100, 100, cv2.BORDER_REFLECT)
uzatilan_resim = cv2.copyMakeBorder(resim, 50, 50, 30, 30, cv2.BORDER_REPLICATE)
tekrarlanan_resim = cv2.copyMakeBorder(resim, 200, 200, 200, 200, cv2.BORDER_WRAP)
sarilan_resim = cv2.copyMakeBorder(resim, 40, 40, 50, 50, cv2.BORDER_CONSTANT, value = (227, 191, 157) ) #çerçeve


cv2.imshow("alex_de_souza", resim)
cv2.imshow("alex_de_souza", aynalanan_resim)
cv2.imshow("alex_de_souza", uzatilan_resim)
cv2.imshow("alex_de_souza", tekrarlanan_resim)
cv2.imshow("alex_de_souza",sarilan_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()



