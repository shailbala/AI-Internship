import cv2
import os

## python3 -m pip install opencv-contrib-python
dataset = "dataset"
name = "champ"
##i = 0

path = os.path.join(dataset, name)
if not os.path.isdir(path):
    os.makedirs(path)
    
(width, height) = (130, 100)
alg = "haarcascade_frontalface_default.xml"

#haar_cascade = cv2.CascadeClassifier(alg)
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + alg)

## -1 on linux, 0 on windows
cam = cv2.VideoCapture(-1)

count = 1
while count < 31:
    print(count)
    _,img = cam.read()
    
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        ## find out the rectangle containing face only image
        faceOnly = grayImg[y:y+h, x:x+w]
        cv2.imwrite("%s/%s.jpg" %(path, count), faceOnly)
        resizeImg = cv2.resize(faceOnly, (width, height))
        cv2.imwrite("%s/%s.jpg" %(path, count), resizeImg)
        count += 1

    cv2.imshow("Face Detection", img)
    key = cv2.waitKey(10)
    #esc key
    if key == 27:
        break
print("Image captured succesfully")
cam.release()
cv2.desroyAllWindows()
