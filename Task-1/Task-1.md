# Task 1 - YOLOv8 Segmentation

**Date:** 2025-10-21  
**Task Completed:** Installed Ultralytics and object detection and segmentation done on an image using YOLOv8

**Steps Followed:**
1. Activated virtual environment `(venv)` in a folder.
2. Ran YOLO detection command:
    yolo predict model=yolov8n.pt source="C:\Users\kriti\Documents\IIIT_Research_internship\datasets\images\val\person_val.jpeg"
3. Ran YOLO Segmentation command:
    yolo predict model=yolov8n-seg.pt source="C:\Users\kriti\Documents\IIIT_Research_internship\datasets\images\val\person_val.jpeg"

**Result:** YOLO performed object detection and segmentation on an image successfully