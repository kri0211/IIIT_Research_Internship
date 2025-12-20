# Pothole Detection and Severity Classification using YOLOv8

## Overview
This project implements a computer vision system to detect potholes from road images and classify their severity using YOLOv8. The model categorizes potholes into three severity levels: minor, moderate, and severe.

## Dataset
- Source: Kaggle pothole dataset
- Total images: 1243
- Training images: 995
- Validation images: 248

The original dataset provided only pothole annotations without severity labels.

## Severity Label Generation
Since severity information was unavailable, severity approximation was made using the bounding box area of each pothole with a python script:
- Small area → Minor pothole
- Medium area → Moderate pothole
- Large area → Severe pothole


## Model Used
- YOLOv8 Nano (yolov8n)

## Training Details
- Image size: 512 × 512
- Epochs: 5
- Hardware: CPU-only
- Optimizer: Default YOLOv8 settings

Training was limited to 5 epochs due to computational constraints.

## Evaluation
The model was evaluated on the validation dataset using:
- Precision
- Recall
- mAP@0.5
- mAP@0.5:0.95

yolo val model=runs/detect/train/weights/best.pt data=data.yaml imgsz=512

Despite limited epochs, the model demonstrates reasonable pothole detection and severity classification performance.

## Result
The model was able to detect potholes and reasonably differentiate severity levels. Performance is limited by dataset size and visual similarity between severity classes, but results are promising for real-world road monitoring applications.

## Limitations
- Severity is inferred using bounding box size, not actual depth
- Limited training epochs due to CPU constraints
- Class imbalance between severity levels

## Future Improvements
- Real-time pothole detection and classification
- Manual severity annotation
- Depth-based severity estimation
- Training with more epochs and GPU acceleration

## How to Run
### Train the model
```bash
yolo train model=yolov8n.pt data=data.yaml imgsz=512 epochs=5