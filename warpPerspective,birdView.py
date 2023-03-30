import cv2
import numpy as np

imgButton = cv2.imread("resources/button3.jpg")

width, height = 250, 250
pts1 = np.array([[164, 68], [271, 72], [165, 188], [271, 176]], np.float32)
pts2 = np.array([[0,0], [width, 0], [0, height], [width, height]], np.float32)
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(imgButton, matrix, (width, height))


for x in range(0, 4):
    cv2.circle(imgButton, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 255, 0), cv2.FILLED)

cv2.imshow("button", imgButton)
cv2.imshow("button2", imgOutput)
cv2.waitKey()
if 0xFF == ord("q"):
    cv2.destroyAllWindows()
