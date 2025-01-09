# YOLO Solutions

[Solutions](https://docs.ultralytics.com/solutions/)

[Solutions](https://docs.ultralytics.com/reference/solutions/region_counter/)


Ultralytics provides powerful solutions designed to tackle specific computer vision challenges with minimal effort. These solutions integrate YOLO models into ready-to-use applications, making them accessible to developers and businesses without requiring extensive customization. Some examples include:

- Object counting in regions
- People tracking
- Traffic flow monitoring
- Custom workflows for retail or industrial applications

Each solution leverages the YOLO framework's efficiency, allowing seamless deployment in real-world scenarios.

## Object Counting in Regions

One of the most common use cases for YOLO solutions is counting objects in specific regions, such as monitoring the number of vehicles entering a parking lot or people crossing a defined boundary.

### Project Setup
To start, ensure your virtual environment is active, and all necessary packages are installed. Then, create a new Jupyter notebook `yolo_object_counting.ipynb` in the following structure:

```hl_lines="8"
📁 computer_vision/
    ├── 📁 .venv/
    ├── 📁 pics/
    ├── 📄 yolo_detect.ipynb
    ├── 📄 yolo_segment.ipynb
    ├── 📄 yolo_keypoints.ipynb
    ├── 📄 yolo_video.ipynb
    └── 📄 yolo_object_counting.ipynb
```

### Example Code

```python
import cv2
from ultralytics import solutions

# Define the video source (0 for webcam or path to a video file)
video_source = 0  # Use "video.mp4" for a saved video
cap = cv2.VideoCapture(video_source)

# Get video properties
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
print (w, h, fps)

# Define region points
region_points = [(20, h-150), (w-20, h-150), (w-20, 150), (20, 150)]  # For rectangle region counting

# Init RegionCounter
region = solutions.RegionCounter(
    show=False,
    region=region_points,
    model="yolo11n.pt",
    classes=[0]
)

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    annotated_frame = region.count(frame)

    # Display the  frame
    cv2.imshow("Video Analysis", annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
```


### Interactive Task

???+ question "Task: Count Objects in a Region"
    1. Modify the ROI to a custom shape, such as a polygon, and test it on different videos.
    2. Experiment with different YOLO model sizes (nano, small, etc.) to observe the impact on accuracy and speed.
    3. Save the annotated video with object counts for later analysis.
    4. Integrate additional features like tracking IDs or class-specific counts (e.g., count only cars or pedestrians).