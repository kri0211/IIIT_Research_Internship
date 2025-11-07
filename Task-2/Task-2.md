# Task 2: Object Detection and Evaluation of Performance Metrics on Multiple Images

**Date:** 06-11-2025

---

## Objective

Perform object detection on multiple images using YOLO’s pretrained models, and evaluate performance metrics such as precision, recall, F1 score, and mAP.

---

## Theory

- **Bounding Boxes:** Represented as `(x_center, y_center, width, height)` relative to image size (normalized coordinates).  
- **Performance Metrics:**  
  - **Precision:** Fraction of predicted boxes that are correct.  
  - **Recall:** Fraction of actual objects detected.  
  - **F1 Score:** Harmonic mean of Precision and Recall.  
  - **mAP@0.5:** Mean Average Precision at IoU threshold 0.5.  
  - **mAP@0.5:0.95:** Mean AP across IoU thresholds 0.5 to 0.95.  

---

## Features

- **Multi-Object Detection:** Detects multiple objects in a single image with bounding boxes.  
- **Custom Classes Support:** Supports user-defined classes in `my_data.yaml` (e.g., person, dog, bicycle, car).  
- **Performance Metrics:** Computes Precision, Recall, F1 Score, mAP@0.5, and mAP@0.5:0.95.  
- **Batch Processing:** Processes multiple images at once and saves annotated results automatically.  
- **Per-Class & Overall Evaluation:** Provides detailed metrics for each class and the overall dataset.  
- **Pretrained YOLOv8 Model:** Uses pretrained weights, no additional training required.  

---

## Running the program

1. Place test images in the `images/` folder.  
2. Run detection and evaluation:  
   ```bash
python multiple_images.py


## Results

Successfully performed object detection on multiple images and generated performance metrics including Precision, Recall, F1 Score, and mAP.