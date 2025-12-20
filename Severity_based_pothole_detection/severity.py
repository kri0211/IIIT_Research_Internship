import os

labels_train = r"dataset\Pothole Dataset\Labels\train"
labels_val   = r"dataset\Pothole Dataset\Labels\val"

output_train = r"dataset\Pothole Dataset\Severity_labels\train"
output_val   = r"dataset\Pothole Dataset\Severity_labels\val"

os.makedirs(output_train, exist_ok=True)
os.makedirs(output_val, exist_ok=True)

def get_severity(area):
    if area < 0.01:
        return 0  
    elif area < 0.03:
        return 1 
    else:
        return 2  

def process_labels(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            with open(os.path.join(input_folder, file_name), "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                cls, x, y, w, h = parts
                w, h = float(w), float(h)
                area = w * h
                severity_class = get_severity(area)
                new_line = f"{severity_class} {x} {y} {w} {h}\n"
                new_lines.append(new_line)

            with open(os.path.join(output_folder, file_name), "w") as f:
                f.writelines(new_lines)

process_labels(labels_train, output_train)
process_labels(labels_val, output_val)

print("All labels updated with severity classes!")