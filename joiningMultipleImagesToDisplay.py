import cv2
import numpy as np
#stack images, horizontal and vertical stacks
kernel = np.ones((5, 5), np.uint8)

image = cv2.imread("resources/ronaldo.webp")
print(image.shape)
image = cv2.resize(image, (400, 500))
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(image, (7, 7), 0)
imageCanny = cv2.Canny(image, 200, 200)
imageDilation = cv2.dilate(imageCanny, kernel, iterations = 1)
imageEroded = cv2.erode(imageDilation, kernel, iterations = 1)



cv2.imshow("image", image)
cv2.imshow("imageGray", imageGray)
cv2.imshow("imageBlur", imageBlur)
cv2.imshow("imageCanny", imageCanny)
cv2.imshow("imageDilation", imageDilation)
cv2.imshow("imageEroded", imageEroded)
cv2.waitKey(0)

if(0xFF == ord("q")):
    cv2.destroyAllWindows()

