import cv2
import numpy

kamera = cv2.VideoCapture(0)

while True :
    ret, goruntu = kamera.read()

    cv2.rectangle(goruntu, (100, 100), (200, 250), (24, 5, 255), 2)
    cv2.line(goruntu, (0, 0), (80, 80), (255, 26, 20), 3)
    cv2.circle(goruntu, (380, 159), 75, (254, 25, 16), 2)
    cv2.putText(goruntu, "zeynep", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 4, (159, 185, 147), 5)



    cv2.imshow("zeynep", goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q") :
        break

kamera.release()

cv2.destroyAllWindows()
