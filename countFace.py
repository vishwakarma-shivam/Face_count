import cv2
classifier= cv2.CascadeClassifier('data2.xml')

def countFaces(img):
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    count=0
    faces= classifier.detectMultiScale(grayImg,1.1,4)
    for x,y,w,h in faces:count+=1
    return count