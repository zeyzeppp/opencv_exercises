import cv2
import numpy

fb_2013 = cv2.imread("fb_2013.jpg")
print(fb_2013.shape)

kesit = fb_2013[50:70, 260:300]


cv2.imshow("kesit_alanı", kesit)
cv2.imshow("FB_2013", fb_2013)
cv2.waitKey(0)
cv2.destroyAllWindows()