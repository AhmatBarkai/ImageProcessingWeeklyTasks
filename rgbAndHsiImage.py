import cv2
import numpy as np

#Converting a rgb image to hsv

image = cv2.imread("image.jpg")
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("RGB Image ",image)
cv2.imshow("hsi",hsvImage)

#Converting from hsv to rgb
mask = cv2.inRange(hsvImage, (7, 25, 25), (70, 255,255))

## slicing the green
imask = mask>0
green = np.zeros_like(image, np.uint8)
green[imask] = image[imask]

## saving
cv2.imwrite("image.png", green)
cv2.waitKey(0)
cv2.destroyAllWindows()
