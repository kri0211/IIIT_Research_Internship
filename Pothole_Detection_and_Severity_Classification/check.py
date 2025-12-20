import os

folder = r"dataset\labels\val"
for file in os.listdir(folder):
    path = os.path.join(folder, file)
    with open(path, 'r') as f:
        content = f.read().strip()
        if content == "":
            print("Empty label:", file)