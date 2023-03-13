import cv2
import torch
import numpy as np
import  os
import C3D_model
import torch

def center_crop(frame):
    frame = frame[8:120, 30:142, :]
    return np.array(frame).astype(np.uint8)


path = r"D:\hdu\InfantMulti\infant\Both_hands"
fliename = r"23_10.10-10.12.mp4"

cap = cv2.VideoCapture(path + "\\" +fliename)

clip = []
while (cap.isOpened()):
    ret, frame = cap.read()

    frame = cv2.resize(frame, dsize=(171, 128))

    cv2.imshow('image', frame)

    print(frame.shape)

    frame = center_crop(frame)

    clip.append(frame)

    cv2.imshow('image1', frame)
    cv2.waitKey(30)
    print(len(clip))



    if len(clip)==16:
        input = np.array(clip).astype(np.float32)
        input = np.expand_dims(input, axis=0)
        input = np.transpose(input, (0, 4, 1, 2, 3))
        input = torch.from_numpy(input)
        net = C3D_model.C3D(num_classes=5, pretrained=False)
        output = net.forward(input)
        print(output)



    print(frame.shape)

     #q键退出
    #if (ord('q')):
    #   break