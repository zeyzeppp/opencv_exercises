import cv2
import numpy as np
width = 400
height = 500
cap = cv2.VideoCapture("resources/vtol.mp4")

while True:
    success, img = cap.read()
    img = cv2.resize(img, (width, height))
    cv2.imshow("Vtol", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break