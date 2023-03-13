import cv2 as cv
import torch
import numpy as np
import  os
import C3D_model
import torch




cap = cv.VideoCapture(700)

while (cap.isOpened()):                      #检测摄像头是否开启
    ret, frame = cap.read()                  #读取每一针的数据
    farme =cv.resize(frame, dsize=(1080, 1080))                      #171, 128
    cv.imshow("2", farme)
    k = cv.waitKey(20)
    # q键退出
    if (k & 0xff == ord('q')):
        break