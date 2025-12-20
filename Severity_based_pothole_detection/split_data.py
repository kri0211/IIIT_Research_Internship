import os
import shutil

images_train = r"dataset\Pothole Dataset\Images\train"
images_val   = r"dataset\Pothole Dataset\Images\val"

labels_all   = r"dataset\Pothole Dataset\Labels\all"
labels_train = r"dataset\Pothole Dataset\Labels\train"
labels_val   = r"dataset\Pothole Dataset\Labels\val"

os.makedirs(labels_train, exist_ok=True)
os.makedirs(labels_val, exist_ok=True)

# Train labels
for img in os.listdir(images_train):
    name = os.path.splitext(img)[0] + ".txt"
    src = os.path.join(labels_all, name)
    if os.path.exists(src):
        shutil.copy(src, labels_train)

# Validation labels
for img in os.listdir(images_val):
    name = os.path.splitext(img)[0] + ".txt"
    src = os.path.join(labels_all, name)
    if os.path.exists(src):
        shutil.copy(src, labels_val)

print("Labels copied successfully")