import cv2
import numpy as np

img = cv2.imread("resources/ronaldo.webp")
print(img.shape)
imgResize = cv2.resize(img, (500, 350))
imgCropped = img[ : , 350: ]

cv2.imshow("ronaldo", img)
cv2.imshow("ronaldoResize", imgResize)
cv2.imshow("ronaldoCropped", imgCropped)
cv2.waitKey(0)