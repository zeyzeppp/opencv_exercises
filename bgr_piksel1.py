import cv2
import numpy

resim = cv2.imread("fire.jpg")
cv2.imshow("fire", resim)

print(resim.shape)
print(resim[(70, 95)])

print("resmin boyutu : " + str(resim.size))
print("resmin özellikleri : " + str(resim.shape))
print("resmin veri tipi : " + str(resim.dtype))






cv2.waitKey(0)
cv2.destroyAllWindows()
