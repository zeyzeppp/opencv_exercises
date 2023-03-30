import cv2
import numpy

alex_de_souza = cv2.imread("alex.png")
alex_de_souza[ : , : , 0] = 255 #Blue
alex_de_souza[ : , : , 1] = 50 #Green

#BGR = 012

cv2.imshow("alex", alex_de_souza)


cv2.waitKey(0)
cv2.destroyAllWindows()
