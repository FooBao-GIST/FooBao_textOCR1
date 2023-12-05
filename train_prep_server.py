import os
import json
import glob
from tqdm import tqdm

root_dir = "/home/user/ocr2/yolov5/custom_dataset"

img_dir = os.path.join(root_dir, "images")
#label_dir = os.path.join(root_dir,"labels")

train_img_dir = "/home/user/ocr2/Train Source_"
val_img_dir = "/home/user/ocr2/Val Source_"

train_imgs_name = os.listdir(train_img_dir)
val_imgs_name = os.listdir(val_img_dir)

#data = glob.glob(os.path.join(img_dir,"*.jpg"))

#디렉토리 경로 바꿔주기
train_imgs = []
for name in train_imgs_name:
    train_img = img_dir + "/" + name
    train_imgs.append(train_img)

val_imgs = []
for name in val_imgs_name:
    val_img = img_dir + "/" + name
    val_imgs.append(val_img)

# train.txt 만들기
with open(os.path.join(root_dir, "train.txt"), 'w') as f:
	f.write('\n'.join(train_imgs) + '\n')

# valid.txt 만들기
with open(os.path.join(root_dir, "valid.txt"), 'w') as f:
	f.write('\n'.join(val_imgs) + '\n')