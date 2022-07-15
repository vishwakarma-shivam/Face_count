from countFace import countFaces
import cv2
import numpy as np
from urllib.request import urlopen

t1='https://thumbor.forbes.com/thumbor/1500x0/smart/filters:format(jpeg)/https%3A%2F%2Fimages.forbes.com%2FBillies22%2Flanding-1500px.gif'
t2='https://api.time.com/wp-content/uploads/2014/05/166259035.jpg'

req= urlopen(t1)
arr=np.asarray(bytearray(req.read()),dtype=np.uint8)
img=cv2.imdecode(arr,-1)

print(countFaces(img))

