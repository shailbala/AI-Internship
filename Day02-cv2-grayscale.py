import cv2

img = cv2.imread("sample1.png")
img2 = cv2.imread("sample2.jpg")

cv2.imshow("sample1",img)
cv2.imwrite("sample1Copy.png",img)

grayImg=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",grayImg)

cv2.imwrite("GrayImage.jpg",grayImg)

cv2.imshow("Orig",img2)
cv2.imshow("Gray",grayImg)


cv2.waitKey(0)
cv2.destroyAllWindows()
