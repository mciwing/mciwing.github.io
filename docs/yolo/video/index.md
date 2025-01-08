# Analysing Videos

Moving from static images to videos, YOLO demonstrates its real power. With its high-speed analysis, YOLO can process each video frame individually and provide real-time insights. Whether detecting objects, segmenting images, or estimating poses, the procedure mirrors that used for static images but adds the dimension of handling sequential frames.

## Project Setup
To start working with video analysis, we'll extend our previous project structure and create a new Jupyter notebook `yolo_video.ipynb`:
```hl_lines="7"
📁 computer_vision/
    ├── 📁 .venv/
    ├── 📁 pics/
    ├── 📄 yolo_detect.ipynb
    ├── 📄 yolo_segment.ipynb
    ├── 📄 yolo_keypoints.ipynb
    └── 📄 yolo_video.ipynb
```
Ensure your virtual environment (`.venv`) is active and that all necessary packages, including `ultralytics` and `opencv-python`, are installed.

## Inference :material-run:

To analyze video data, whether from a webcam or a saved file, we leverage the Python package OpenCV (`cv2`).

### Accessing Video Sources

YOLO can handle various video sources, such as live webcam feeds or pre-recorded video files. Here's an example of how to set up your video source:

```python
import cv2

# Define the video source (0 for webcam or provide a file path)
video_source = 0  # Example: "video.mp4" for a saved video
cap = cv2.VideoCapture(video_source)

# Check if the video source is accessible
if not cap.isOpened():
    print("Error: Cannot access the video source.")
    exit()

# Release the video capture once done
cap.release()
```

### Real-Time Video Analysis

For video analysis, YOLO processes each frame independently, applying detection, segmentation, or keypoint extraction models. Below is an example demonstrating real-time video detection.

### Example: Video Detection

```python
import cv2
from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolov8n.pt")

# Define the video source (0 for webcam or path to a video file)
video_source = 0  # Use "video.mp4" for a saved video
cap = cv2.VideoCapture(video_source)

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the current frame
    results = model(frame)

    # Annotate the frame with detection results
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("Video Analysis", annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
```

???+ question "Task: Analyze a Video"
    1. Try to access the webcam and display the live video [:octicons-link-external-16:](https://www.studytonight.com/post/capture-videos-and-images-with-python-part2)
    2. Use the YOLOv8 Nano model to perform a:
        - Detection
        - Segmentation
        - Pose Estimation
        - Tracking [:octicons-link-external-16:](https://docs.ultralytics.com/modes/track/#tracking)
    3. Compare results across detection, segmentation, and keypoint extraction.
    4. Visualize and save results for further analysis.
