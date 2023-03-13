

import os





folder = r'D:\hdu\InfantMulti\infant'



foldernames, videonames = [],[]


for foldername in os.listdir(folder):
    for videoname in os.listdir(os.path.join(folder,foldername)):
        videonames.append(os.path.join(folder,foldername,videoname))
    foldernames.append(os.path.join(folder,foldername))
    print(foldernames)
    print('\n')











fnames, labels = [], []

for label in sorted(os.listdir(folder)):
    for fname in os.listdir(os.path.join(folder, label)):
        #print(fname)
        fnames.append(os.path.join(folder, label, fname))
        labels.append(label)


assert len(labels) == len(fnames)
#print('Number of {} videos: {:d}'.format('train', len(fnames)))

#print(folder)



#s_labels = set(labels)
#ss_labls = sorted(set(labels))
#e_labels = enumerate(sorted(set(labels)))

#label2index = {label: index for index, label in enumerate(sorted(set(labels)))}

#print(label2index)
#print(labels)
#print("\n")
#print(s_labels)
#print("\r\n")
#print(ss_labls)
#print("\r\n")
#print(e_labels)

#print(labels)
#print(fnames)