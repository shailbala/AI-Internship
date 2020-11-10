## Convert image to grayscale

import cv2

img = cv2.imread("krishna.jpg")
# convert to GrayScale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# save it
cv2.imwrite("GrayImage.jpg", grayImg)

## show both images
cv2.imshow("Original", img)
cv2.imshow("GrayImage", grayImg)


cv2.waitKey(0)
cv2.destroyAllWindows()
