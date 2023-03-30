import cv2
import numpy as np

circles = np.zeros((4, 2))
counter = 0


def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        print(x, y)
        counter = counter + 1




kitap = cv2.imread("resources//kitap.jpeg")
print(kitap.shape)
kitap = cv2.resize(kitap, (450, 800))


while True:


    if counter == 4:
        width, height = 450, 800
        pts1 = np.array([circles[0], circles[1], circles[2], circles[3]], np.float32)
        pts2 = np.array([[0, 0], [width, 0], [0, height], [width, height]], np.float32)
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(kitap, matrix, (width, height))
        cv2.imshow("kitap", imgOutput)

        for x in range(0, 4):
            cv2.circle(kitap, (int(pts1[x][0]), int(pts1[x][1])), 3, (0, 0, 255), cv2.FILLED)

    cv2.imshow("kitap", kitap)
    cv2.setMouseCallback("kitap", mousePoints)
    cv2.waitKey(1)

    if 0xFF == ord('q'):
        cv2.destroyAllWindows()