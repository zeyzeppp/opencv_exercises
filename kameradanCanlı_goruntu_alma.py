import cv2
import numpy


kamera = cv2.VideoCapture(0)

while True :
    ret, goruntu = kamera.read()
    cv2.imshow("zeynep", goruntu)


    if cv2.waitKey(30) & 0xFF == ord("q") :
        break


kamera.release()

cv2.destroyAllWindows()

