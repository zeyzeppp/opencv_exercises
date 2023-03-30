import cv2
import numpy as np

resim = np.zeros((300, 500, 3), dtype = "uint8")
print(resim)

#line --- cv2.line(img, pt1, pt2, color, thickness)
cv2.line(resim, (50, 50), (80, 100), (0, 255, 0), 3)

#circle --- cv2.line(img, center, radious, color, thickness)
cv2.circle(resim, (100, 100), 30, (0, 0, 255), 2)

#text --- cv2.putText(img, text, org(baslangic noktasi), fontFace, fontScale, color, thickness)
cv2.putText(resim, "Zeynep Alperen", (150, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)


cv2.imshow("deneme", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()