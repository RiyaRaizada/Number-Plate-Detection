import cv2
import numpy as np
frameWidth=640
frameHeight=480
widthImg=640
heightImg=480
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
def preProcessing(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,200,200)
    kernel=np.ones((5,5))
    imgDial=cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres=cv2.erode(imgDial,kernel,iterations=1)
    return imgThres


while True:
    success, img=cap.read()
    cv2.resize(img,(widthImg,heightImg))
    imgThres=preProcessing(img)
    cv2.imshow("Result",imgThres)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        break