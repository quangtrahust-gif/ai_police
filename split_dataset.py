import os
import shutil
import random

# Đường dẫn đến dataset bạn vừa giải nén
base_dir = 'make_sense_dataset'   # hoặc tên thư mục thực tế
src_img = os.path.join(base_dir, 'images')
src_label = os.path.join(base_dir, 'labels')

# Thư mục đích train/val
train_img = 'custom_dataset/images/train'
val_img = 'custom_dataset/images/val'
train_label = 'custom_dataset/labels/train'
val_label = 'custom_dataset/labels/val'

for d in [train_img, val_img, train_label, val_label]:
    os.makedirs(d, exist_ok=True)

# Lấy danh sách ảnh
images = [f for f in os.listdir(src_img) if f.endswith(('.jpg', '.png'))]
random.shuffle(images)

split = int(0.8 * len(images))
train = images[:split]
val = images[split:]

def copy_files(file_list, img_dst, label_dst):
    for f in file_list:
        base = os.path.splitext(f)[0]
        shutil.copy(os.path.join(src_img, f), os.path.join(img_dst, f))
        label_file = base + '.txt'
        if os.path.exists(os.path.join(src_label, label_file)):
            shutil.copy(os.path.join(src_label, label_file), os.path.join(label_dst, label_file))

copy_files(train, train_img, train_label)
copy_files(val, val_img, val_label)

print(f"Train: {len(train)} ảnh")
print(f"Val: {len(val)} ảnh")