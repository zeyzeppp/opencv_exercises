import cv2
import numpy

fb_2013 = cv2.imread("fb_2013.jpg")
ronaldo = cv2.imread("little_ronaldo.jpg")

print(ronaldo.shape)
fb_2013[50:70, 260:300] = ronaldo



cv2.imshow("FB_2013", fb_2013)
cv2.imshow("little_ronaldo", ronaldo)

cv2.waitKey(0)
cv2.destroyAllWindows()
