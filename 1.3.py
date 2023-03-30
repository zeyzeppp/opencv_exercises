import cv2
import numpy

alex_de_souza = cv2.imread("alex.png")
print(alex_de_souza.shape)
alex_de_souza[50:100, 100:200, 0] = 255
alex_de_souza[25:50, 30:60, 1] = 200
alex_de_souza[25:50, 30:60, 2] = 245

cv2.imshow("alex", alex_de_souza)


cv2.waitKey(0)
cv2.destroyAllWindows()