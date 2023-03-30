import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[ : ] = 255, 50, 75

cv2.line(img, (0, 0), (100, 65), (25, 255, 125), 2)
cv2.rectangle(img, (70, 70), (40, 40), (100, 28, 19), cv2.FILLED)
cv2.circle(img, (200, 200), 85, (158, 147, 152), 3)
cv2.putText(img, "Zeynep", (130, 130), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 245, 10))
cv2.imshow("black image", img)

cv2.waitKey(0)
