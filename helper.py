import base64
import numpy
import cv2

def img64_to_cvImg(img64):
    img64=img64.replace('data:image/jpeg;base64,','')
    img=base64.b64decode(img64)
    img=numpy.fromstring(img,numpy.uint8)
    img=cv2.imdecode(img,cv2.IMREAD_COLOR)
    return img