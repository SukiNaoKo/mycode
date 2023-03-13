import cv2
import torch
import numpy as np
import  os
import C3D_model
import torch

def center_crop(frame):
    frame = frame[8:120, 30:142, :]
    return np.array(frame).astype(np.uint8)

clip=[]
path = r"D:\hdu\InfantMulti\video2pic\test\Both_hands\26_12.59.mp4"
pic_name = r'\00000.jpg'
pic_name_2 = r'\00001.jpg'


for img_name in os.listdir(path):
    img = cv2.imread(path+'\\'+img_name)
    img = center_crop(img)
    clip.append(img)
    if len(clip)==16:
        break




#img_1 = cv2.imread(path+pic_name)
#img_2 = cv2.imread(path+pic_name_2)
#print(img_1.shape)
#img_1 = center_crop(img_1)
#img_2 = center_crop(img_2)
#clip.append(img_1)
#clip.append(img_2)
#inputs = np.expand_dims(img, axis=0)

print(len(clip))

clip = np.array(clip).astype(np.float32)
print(clip.shape)
clip = np.expand_dims(clip, axis=0)
print(clip.shape)
clip = np.transpose(clip, (0, 4, 1, 2, 3))
print(clip.shape)
clip = torch.from_numpy(clip)


net = C3D_model.C3D(num_classes=5, pretrained=False)
output = net.forward(clip)

print(output)

print(np.amax(output.detach().numpy()))