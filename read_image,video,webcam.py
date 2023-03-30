import cv2
import numpy as np
"""
img = cv2.imread("resources/ronaldo.webp")
cv2.imshow("ronaldo", img)
cv2.waitKey(0) #milliseconds, 0 = infinity
"""

"""
cap = cv2.VideoCapture("resources/vtol.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Vtol", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
"""
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Vtol", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break