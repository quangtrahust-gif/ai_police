import os
import shutil
import random

# Đường dẫn
raw_img_dir = "custom_dataset/images/raw"
raw_label_dir = "custom_dataset/labels/raw"

train_img_dir = "custom_dataset/images/train"
val_img_dir = "custom_dataset/images/val"
train_label_dir = "custom_dataset/labels/train"
val_label_dir = "custom_dataset/labels/val"

# Tạo thư mục
for d in [train_img_dir, val_img_dir, train_label_dir, val_label_dir]:
    os.makedirs(d, exist_ok=True)

# Lấy danh sách ảnh
images = [f for f in os.listdir(raw_img_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(images)

# Chia 80/20
split = int(0.8 * len(images))
train_images = images[:split]
val_images = images[split:]

def copy_files(img_list, img_dst, label_dst):
    for img in img_list:
        base = os.path.splitext(img)[0]
        shutil.copy(os.path.join(raw_img_dir, img), os.path.join(img_dst, img))
        label_file = f"{base}.txt"
        src_label = os.path.join(raw_label_dir, label_file)
        if os.path.exists(src_label):
            shutil.copy(src_label, os.path.join(label_dst, label_file))

copy_files(train_images, train_img_dir, train_label_dir)
copy_files(val_images, val_img_dir, val_label_dir)

print(f"Train: {len(train_images)} ảnh")
print(f"Val: {len(val_images)} ảnh")
