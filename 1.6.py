import cv2
import numpy

bloom = cv2.imread("bloom.jpg")
bloom_gray = cv2.imread("bloom.jpg", 0)
mainFilter = cv2.blur(bloom, (3,3))
mainFilter_2 = cv2.blur(bloom, (7, 7))

cv2.imshow("ejderha", bloom)
cv2.imshow("ejderha_3*3", mainFilter)
cv2.imshow("ejderha_7*7", mainFilter_2)
cv2.imshow("ejderha_gray", bloom_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
