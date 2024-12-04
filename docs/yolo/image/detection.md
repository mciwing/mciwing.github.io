#  Detection

## Project Setup
Use the before created project setup
```
📁 computer_vision/
    ├── 📁 .venv/
    ├── 📁 pics/
    └── 📄 yolo_image.ipynb
```

## Performing Detection

Let's detect objects in an image using the base YOLOv11 model:

```python
from ultralytics import YOLO

# Load model
model = YOLO("yolov11n.pt")

# Perform detection
results = model("dog.jpg")
```

???+ question "Task: First Detection" 
    1. Run the code above on your image
    2. Print `results` - what do you see?
    3. What type is the `results` object? 

## Understanding Results

YOLO returns detection results in a structured format. Let's break it down:

```py
# Get the first (and only) image's results
result = results[0]

# Print object count
print(f"Detected {len(result.boxes)} objects")

# Examine each detection
for box in result.boxes:
    # Get class name
    class_id = int(box.cls)
    class_name = model.names[class_id]
    
    # Get confidence
    confidence = float(box.conf)
    
    # Get coordinates (x1, y1, x2, y2 format)
    x1, y1, x2, y2 = box.xyxy[0].tolist()
    
    print(f"\nDetection:")
    print(f"- Class: {class_name}")
    print(f"- Confidence: {confidence:.2f}")
    print(f"- Coordinates: ({x1:.1f}, {y1:.1f}) to ({x2:.1f}, {y2:.1f})")
```

```title=">>> Output"
Detected 2 objects

Detection:
- Class: person
- Confidence: 0.92
- Coordinates: (223.1, 155.3) to (341.8, 592.7)

Detection:
- Class: dog
- Confidence: 0.87
- Coordinates: (82.4, 220.6) to (452.1, 537.9)
```

???+ question "Task: Result Analysis"
    1. What does each coordinate pair represent? 
    2. How confident is YOLO about each detection?
    3. Calculate the width and height of one bounding box

## Visualization

To visualize and save detections:

```python
# Plot results on image
annotated_image = results[0].plot()

# Display using OpenCV
import cv2
cv2.imshow("Detection Results", annotated_image)
cv2.waitKey(0)

# Save the image
cv2.imwrite("detected.jpg", annotated_image)
```

???+ question "Task 4: Visualization"
    1. Run detection with confidence threshold 0.5:
    ```python
    results = model("dog.jpg", conf=0.5)
    ```
    2. Save this image as "high_conf.jpg"
    3. Now try confidence 0.3, save as "low_conf.jpg"
    4. Compare both images - what differences do you notice?

## Model Sizes

YOLOv11 comes in different sizes, trading speed for accuracy:

- nano (n): Fastest, least accurate
- small (s): Good balance
- medium (m): More accurate, slower
- large (l): Most accurate, slowest

```python
# Try different models
models = {
    "nano": YOLO("yolov11n.pt"),
    "small": YOLO("yolov11s.pt"),
    "medium": YOLO("yolov11m.pt"),
    "large": YOLO("yolov11l.pt")
}

# Compare detections
for name, model in models.items():
    print(f"\nUsing {name} model:")
    results = model("dog.jpg")
    boxes = results[0].boxes
    print(f"Found {len(boxes)} objects")
    
    # Save visualization
    results[0].plot()
    cv2.imwrite(f"detected_{name}.jpg", annotated_image)
```

???+ question "Task 5: Model Comparison"
    For each model size:
    1. Time the detection speed
    2. Count detected objects
    3. Compare confidence scores
    4. Create a table with your findings:

    | Model | Detection Time | Objects Found | Avg Confidence |
    |-------|---------------|---------------|----------------|
    | nano  |               |               |                |
    | small |               |               |                |
    | ...   |               |               |                |

Which model provides the best balance for your needs?