import cv2
import numpy


#mean_filter
image = cv2.imread("manzara.png")
mainFilter = cv2.blur(image, (3, 3))
mainFilter_2 = cv2.blur(image, (5, 5))
mainFilter_3 = cv2.blur(image, (7, 7))



cv2.imshow("orijinal_manzara", image)
cv2.imshow("manzara(meanF)-3*3", mainFilter)
cv2.imshow("manzara(meanF)-5*5", mainFilter_2)
cv2.imshow("manzara(meanF)-7*7", mainFilter_3)


#median_filter
image_2 = cv2.imread("village.jpeg")
medianFilter = cv2.medianBlur(image_2, (3))


cv2.imshow("orijinal_village", image_2)
cv2.imshow("village(medianF)-3", medianFilter)



cv2.waitKey(0)

if 0xFF == ord("q"):
    cv2.destroyAllWindows()

"""imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
    cv2.destroyAllWindows()"""