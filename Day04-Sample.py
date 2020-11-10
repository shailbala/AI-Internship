import cv2
import imutils

img = cv2.imread("sample2.jpg")

#resizeImg = imutils.resize(img, width=20)
# with extension
#cv2.imwrite("resizedImage.jpg", resizeImg)

## Gaussian Blur
#gbImg = cv2.GaussianBlur(img, (21, 21), 0)
#cv2.imwrite("GaussianBlurredImage.jpg", gbImg)


## Grayscale
## dst = cv2.threshold(src, threshold, maxValueForThreshold, binary.type)

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("ThresholdImage.jpg", thresImg)


## Draw a rectangle
#cv2.rectangle(src, startpoint, endpoint, color, thickness)
#cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
