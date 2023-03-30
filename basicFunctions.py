import cv2
import numpy as np

kernel = (5,5)

img = cv2.imread("resources/ronaldo.webp")
print(img.shape)
img = cv2.resize(img, (400, 400))


#Functions
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7, 7),0) #if you increase it your blurriness will be increased (7, 7) --> (9, 9) and it can be just only odd numbers.
imgCanny = cv2.Canny(imgBlur, 100, 100) #if you decrase it you'll see lots of edges.
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 3)
imgEroded = cv2.erode(imgCanny, kernel, iterations = 1)

cv2.imshow("Ronaldo", img)
cv2.imshow("Ronaldo_gray", imgGray)
cv2.imshow("Ronaldo_blur", imgBlur)
cv2.imshow("Ronaldo_canny", imgCanny)
cv2.imshow("Ronaldo_dilation", imgDilation)
cv2.imshow("Ronaldo_eroded", imgEroded)

cv2.waitKey(0)
if 0xFF == ord("q"):
    cv2.destroyAllWindows()
