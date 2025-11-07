from ultralytics import YOLO

model = YOLO("yolov8m.pt") 

yaml_path = "datasets/my_data.yaml"

metrics = model.val(data=yaml_path)

results = model.predict(source="datasets/images", conf=0.1, save=True)  

class_names = ["person", "dog", "bicycle", "car"]  

print("\n=== OVERALL PERFORMANCE METRICS ===")
print("Mean Precision (mp):", metrics.mp)
print("Mean Recall (mr):", metrics.mr)
print("mAP@0.5:", metrics.map50)
print("mAP@0.5:0.95:", metrics.map)
class_names = ["person", "dog", "bicycle", "car"]

print("\n=== PER-CLASS METRICS ===")
for i, name in enumerate(class_names):
    p, r, ap50, ap = metrics.class_result(i)
    print(f"\nClass: {name}")
    print(" Precision:", p)
    print(" Recall   :", r)
    print(" AP@0.5   :", ap50)
    print(" AP@0.5:0.95:", ap)

print("\nAll detection images and plots saved in:", results[0].save_dir)

