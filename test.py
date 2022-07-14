from countFace import countFaces
import cv2
img= cv2.imread('example3.jpg')
print(countFaces(img))