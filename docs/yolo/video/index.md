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

### Capture Video Stream

Let's begin with a program to access your web camera and display its live feed.

#### Step 1: Import the Library
To use OpenCV, start by importing the library:

```python
import cv2
```
This statement includes the OpenCV library in our program, giving us access to its methods and properties.

#### Step 2: Create a VideoCapture Object
In OpenCV, the `VideoCapture()` method allows us to capture the video stream from our webcam:

```python
videoStreamObject = cv2.VideoCapture(0)
```
The argument `0` refers to the first camera connected to the device. If additional cameras are connected, you can use `1`, `2`, etc.

#### Step 3: Read Frames
The `read()` method of the `VideoCapture` object retrieves each frame from the video stream:

```python
ret, frame = videoStreamObject.read()
```
- `ret`: Boolean indicating if the frame was captured successfully.
- `frame`: The captured frame as a NumPy array.

#### Step 4: Display Frames
To display the captured frames in a window, use the `imshow()` method:

```python
cv2.imshow('Capturing Video', frame)
```
The first argument is the window title, and the second argument is the frame to display.

#### Step 5: Loop and Exit
To continuously capture frames, use a `while` loop and break it based on user input. Use `cv2.waitKey()` to listen for key presses:

```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```
This stops the loop when the `q` key is pressed.

#### Step 6: Release Resources
Release the video stream and close any OpenCV windows:

```python
videoStreamObject.release()
cv2.destroyAllWindows()
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