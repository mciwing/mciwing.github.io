# YOLO Solutions

<figure markdown="span">
        <img src="https://github.com/ultralytics/docs/releases/download/0/ultralytics-solutions-thumbnail.avif" width="70%" />
        <figcaption style="text-align: center;">Level up your computer vision skills with YOLO solutions! 🔍 (Source: <a href="https://docs.ultralytics.com/solutions/">Ultralytics</a>) </figcaption>
</figure>


???+ info "Ultralytics Solutions"
    
    This chapter introduces [Ultralytics Solutions](https://docs.ultralytics.com/solutions/), a collection of 
    ready-to-use applications built on top of YOLO models. These solutions make it easier to implement 
    common computer vision tasks without extensive customization.

    We'll explore practical applications and create our first object counting system.

## Project Setup

If you've followed the previous chapters, your project structure should look like this:

```plaintext hl_lines="8"
📁 computer_vision/
    ├── 📁 .venv/
    ├── 📁 pics/
    ├── 📄 yolo_detect.ipynb
    ├── 📄 yolo_segment.ipynb
    ├── 📄 yolo_keypoints.ipynb
    ├── 📄 yolo_video.ipynb
    └── 📄 yolo_object_counting.ipynb
```

For this section, we added a new Jupyter notebook named `yolo_object_counting.ipynb` within the project to follow along.

## Object Counting

One of the most practical applications of computer vision is counting objects in specific regions. This could be:

- Counting vehicles in traffic lanes
- Monitoring people in store sections
- Tracking inventory movement
- Analyzing crowd density in areas

Let's implement a basic object counting system using YOLO and explore how to customize it for different scenarios.

### Basic Setup

Before we start counting, we need to define where we want to count objects. Therefore we need to know the frame size of our webcam or video. 

```python
import cv2
from ultralytics import solutions

# Define video source (0 for webcam)
video_source = 0  # Change to video path for file
cap = cv2.VideoCapture(video_source)

# Get video properties
w, h, fps = (int(cap.get(x)) for x in (
    cv2.CAP_PROP_FRAME_WIDTH, 
    cv2.CAP_PROP_FRAME_HEIGHT, 
    cv2.CAP_PROP_FPS
))

print(f"Video properties: {w}x{h} @ {fps}fps")
```

```title=">>> Output"
Video properties: 640x480 @ 30fps
```

### Define Region of Interest

Now that we know the frame size, we can define a 'region of interest'. We start with a generic rectangle which has a distance of 20 pixels to all sides.

```python
# Define counting region (rectangle)
region_points = [
    (20, h-20),     # Bottom left
    (w-20, h-20),   # Bottom right
    (w-20, 20),     # Top right
    (20, 20)        # Top left
]
```

### Initialize Counter

Now we'll set up the YOLO-based counter:

```python
# Initialize RegionCounter
counter = solutions.RegionCounter(
    show=False,            # Show visualization
    region=region_points,  # Our defined region
    model="yolo11n.pt",    # Use nano model for speed
    classes=[0]            # Only count persons (class 0)
)
```

### Process Video

Let's create the main processing loop:

```python
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    # Process frame and count objects
    annotated_frame = counter.count(frame)
    
    # Display results
    cv2.imshow("Object Counting", annotated_frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

???+ info "What Counts to the Region?"
    If you run the code, you will see that YOLO counts the people in the region of interest. Only objects whose center point of the bounding box lies within the region are counted.

### Save Results

To save your counting results for later analysis you need to add the following lines

- Before the Main Loop: 
    ```python
    # Create video writer
    output_path = 'counting_results.mp4'
    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (w, h)
    )
    ```
- In the Main Loop:
    ```python
    writer.write(annotated_frame)
    ```
- After the Main Loop
    ```python
    writer.release()
    ```


???+ question "Experiment with Different Settings"
    Perform an object counting in region with the above code by accessing you webcam. 
    Try these modifications to enhance your counter:

    1. Change the size of the region.

    2. Change the counting region shape:
    ```python
    # Triangle region
    region_points = [
        (w//2, 100),    # Top
        (50, h-100),    # Bottom left
        (w-50, h-100)   # Bottom right
    ]
    ```

    3. Count different objects:
    ```python
    # Count multiple classes
    counter = solutions.RegionCounter(
        classes=[0, 2, 3]  # Person, car, motorcycle
    )
    ```
    4. Save the annotated video with object counts for later analysis.

    What other modifications could make this more useful for your needs?

## Recap

In this chapter, we've learned how to:

- Set up a basic object counting system
- Define custom regions of interest
- Process video streams in real-time
- Save and analyze counting results

Next, we'll explore how we can train our own models. 

<figure markdown="span">
        <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*woCghCV6Lp9gS3f7.jpg" width="70%" />
        <figcaption style="text-align: center;">(Source: <a href="https://medium.com/levana-protocol/dragon-egg-meme-contest-4d27e1ab2f19">Medium</a>) </figcaption>
</figure>