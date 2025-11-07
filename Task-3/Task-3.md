# Object Detection for Video using YOLO and FFMPEG

This task demonstrates extractracting frames from videos and applying 'object detection' using YOLO and FFmpeg.

These are the steps used for completing this task
### 1. Download video

Downloaded a simpel traffic video using 'yt-dlp'
yt-dlp https://www.youtube.com/watch?v=MNn9qKG2UFI -o traffic_video.mp4

### 2. Trimmed video from 5 min to 30 sec

ffmpeg -i traffic_video.mp4 -t 30 -c copy short_video.mp4

### 3. Extracted Frames from video at 24fps

mkdir frames30
ffmpeg -i short_video.mp4 -vf fps=24 frames30/frame_%04d.png


### 4. Run YOLO object detection on all frames

yolo detect predict model=yolov8n.pt source=frames30 save=True project=processed_frames30

### 5. Converted the processed frames back into a video

ffmpeg -framerate 24 -i processed_frames30/predict/frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p output30.mp4

## Output: 

Successfully extracted the frames from the video, detected objects and converted the processed frames back into a video