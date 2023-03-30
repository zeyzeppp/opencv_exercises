import cv2
import numpy as np
circles = np.zeros((4, 2))
counter = 0

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        print(x, y)
        counter = counter + 1

imgButton = cv2.imread("resources/button3.jpg")


cv2.imshow("button", imgButton)
cv2.setMouseCallback("button", mousePoints)
cv2.waitKey(0)
