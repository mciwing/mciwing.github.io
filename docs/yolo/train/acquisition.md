# Data Acquisition

After learning about different computer vision tasks with YOLO, you might want to train your own model for specific use cases. The first step in training a custom YOLO model is acquiring a suitable dataset. A well-curated and diverse dataset is key to achieving high performance and generalization in computer vision tasks.This chapter will guide you through various methods of collecting training data.

## Project Setup
We'll start a new project for training our custom YOLO model:
```
📁 yolo_training/
    ├── 📁 .venv/
    ├── 📁 data/
    │   ├── 📁 images/
    │   └── 📁 videos/
    └── 📄 data_acquisition.ipynb
```

## The Need for Data :material-database:

Training an effective YOLO model requires a substantial amount of data. Here's why:

- **Better Generalization**: A diverse dataset helps the model learn features that generalize to new, unseen data.
- **Handling Variability**: Capturing different lighting conditions, perspectives, and object appearances ensures robust performance.
- **Avoiding Overfitting**: A small dataset can cause the model to memorize specific examples rather than learning general patterns, leading to overfitting.

The amount of data needed depends on several factors like **Task Complexity**, **Required Accuracy**, **Object Variation** and **Background Variation**

| Task Complexity | Recommended Images |
|-----------------:|:-------------------|
| Simple (e.g., logo detection) | 500 - 2,000 |
| Moderate (e.g., car types) | 2,000 - 10,000 |
| Complex (e.g., defect detection) | 5,000 - 20,000+ |

Building a large dataset can be a challenging task, but there are several strategies to gather the required data efficiently.

## Automatic Image Collection

Web scraping can be used to download large amounts of images for training datasets. Python libraries like `requests` and `BeautifulSoup` are common tools for this purpose. An even more comfortable way is to use an API of a search engine like [Bing :material-microsoft-bing:](https://pypi.org/project/bing-image-downloader/), [Google :material-google:](https://pypi.org/project/google_images_download/) or [DuckDuckGo :simple-duckduckgo:](https://pypi.org/project/duckduckgo-search/).

=== "Bing Image Downloader"
    ???+ info "Package Installation"

        ```commandline
        pip install bing-image-downloader
        ```

    ```python
    from bing_image_downloader import downloader

    # Define Search Term
    query_string = "Homer Simpson"

    # Download Images
    downloader.download(
        query_string,           # Use the search term
        limit=10,               # Number of images
        output_dir='dataset',   # Output folder
        adult_filter_off=False, # Enable/Disable adult filter
        force_replace=False,    # Delete folder if present and start fresh
        verbose=True            # Show/Hide Download message
    )
    ```

=== "Google Image Download"

    ???+ info "Package Installation"

        ```commandline
        pip install google_images_download
        ```

    ```python
    from google_images_download import google_images_download 

    # Class Instantiation
    response = google_images_download.googleimagesdownload()   

    # Define Search Term
    query = [
        'Homer Simpson',
        'Marge Simpson',
        'Bart Simpson',
    ]

    # Creating List of Arguments
    arguments = {"keywords": query,         # Use the search term
                 "format": "jpg",           # Search for jpg files
                 "limit":10,                # Number of images
                 "print_urls":True,         # Show the image URLs
                 "size": "medium",          # Image size ("large, medium, icon")
                 "aspect_ratio":"panoramic" # Aspect ratio ("tall, square, wide, panoramic")
    }
                 
    # Download Images                
    response.download(arguments)   #passing the arguments to the function
    ```

=== "DuckDuckGo Search"

    ???+ info "Package Installation"

        ```commandline
        pip install duckduckgo-search
        ```

    ```python
    from duckduckgo_search import DDGS 

    # Class Instantiation
    response = google_images_download.googleimagesdownload()   

    # Define Search Term
    query_string = "Homer Simpson"

    results = DDGS().images(
        keywords=query_string,
        region="wt-wt",
        safesearch="off",
        size=None,
        color="Monochrome",
        type_image=None,
        layout=None,
        license_image=None,
        max_results=100,
    )
    ```
### Data Cleaning Tips

After downloading, it's important to clean your dataset:

???+ tip "Dataset Cleaning Checklist"
    - [ ] Remove corrupted images
    - [ ] Remove duplicates
    - [ ] Verify image quality
    - [ ] Check image relevance
    - [ ] Ensure consistent format

Here's a script to help with basic cleaning:

```python
import os
from PIL import Image
import hashlib

def clean_dataset(directory):
    """
    Clean a directory of images by removing corrupted files and duplicates
    
    Args:
        directory (str): Path to image directory
    """
    # Store image hashes to detect duplicates
    hash_dict = {}
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            # Try to open the image
            with Image.open(filepath) as img:
                # Calculate image hash
                img_hash = hashlib.md5(img.tobytes()).hexdigest()
                
                # Check for duplicates
                if img_hash in hash_dict:
                    print(f"Removing duplicate: {filename}")
                    os.remove(filepath)
                else:
                    hash_dict[img_hash] = filepath
                    
        except Exception as e:
            print(f"Removing corrupted file {filename}: {str(e)}")
            os.remove(filepath)

# Clean the downloaded images
clean_dataset('data/images')
```

## Video Frame Extraction

Another effective way to collect data is by recording video and extracting frames.

### Recording Guidelines

When recording video for training data:

- Capture different angles
- Vary lighting conditions
- Include different backgrounds
- Move around the object
- Vary object positions

### Frame Extraction

Here's how to extract frames from a video file:

```python
import cv2
import os

def extract_frames(video_path, output_dir, sample_rate=1):
    """
    Extract frames from a video file
    
    Args:
        video_path (str): Path to video file
        output_dir (str): Directory to save frames
        sample_rate (int): Extract every nth frame
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Video FPS: {fps}")
    print(f"Total frames: {frame_count}")
    
    # Initialize frame counter
    frame_number = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Save every nth frame
        if frame_number % sample_rate == 0:
            frame_path = os.path.join(output_dir, f'frame_{saved_count:05d}.jpg')
            cv2.imwrite(frame_path, frame)
            saved_count += 1
            
        frame_number += 1
        
    cap.release()
    print(f"Saved {saved_count} frames to {output_dir}")

# Example usage
extract_frames(
    'data/videos/object_video.mp4',
    'data/images/extracted_frames',
    sample_rate=30  # Extract one frame per second for 30fps video
)
```

### Frame Selection Tips

Not all frames are equally valuable for training:

???+ tip "Frame Selection Guidelines"
    - Remove blurry frames
    - Ensure good object visibility
    - Maintain diversity in selection
    - Consider temporal spacing
    - Check for redundancy

Here's a simple blur detection function:

```python
def detect_blur(image_path, threshold=100):
    """
    Detect if an image is blurry
    
    Args:
        image_path (str): Path to image
        threshold (int): Blur threshold (lower means stricter)
        
    Returns:
        bool: True if image is blurry
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    return laplacian < threshold

# Example usage
for frame in os.listdir('data/images/extracted_frames'):
    frame_path = os.path.join('data/images/extracted_frames', frame)
    if detect_blur(frame_path):
        os.remove(frame_path)
        print(f"Removed blurry frame: {frame}")
```

## Best Practices

When collecting your dataset:

1. **Diversity**
   - Vary lighting conditions
   - Include different backgrounds
   - Capture different angles
   - Include different times of day

2. **Quality Control**
   - Check image resolution
   - Remove blurry images
   - Ensure correct labeling
   - Verify class balance

3. **Organization**
   - Use clear folder structure
   - Maintain consistent naming
   - Document your process
   - Back up your data

???+ question "Task: Data Collection"
    Practice data collection with these exercises:

    1. Image Download
        - Download 100 images for a custom object
        - Clean the downloaded dataset
        - Document the success rate
    
    2. Video Recording
        - Record a 1-minute video of an object
        - Extract frames at different rates
        - Compare the quality of extracted frames
    
    3. Dataset Analysis
        - Count images per category
        - Check image resolutions
        - Verify image quality
        - Report on dataset statistics

???+ info "🎉 Congratulations"
    You've learned how to collect and prepare data for training your YOLO model! In the next chapter, we'll cover how to annotate your collected images.

---

???+ info "Further Reading"
    - [YOLO Dataset Format](https://docs.ultralytics.com/datasets/detect/)
    - [Data Collection Best Practices](https://docs.ultralytics.com/datasets/)
    - [Image Augmentation Techniques](https://docs.ultralytics.com/datasets/augment/)





xxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx

# Train a Model

## Data Acquisition

Data acquisition is the first and most critical step when training a model. A well-curated and diverse dataset is key to achieving high performance and generalization in computer vision tasks.

### Why Do We Need a Lot of Data?

Training deep learning models requires a large amount of labeled data for several reasons:

- **Better Generalization**: A diverse dataset helps the model learn features that generalize to new, unseen data.
- **Handling Variability**: Capturing different lighting conditions, perspectives, and object appearances ensures robust performance.
- **Avoiding Overfitting**: A small dataset can cause the model to memorize specific examples rather than learning general patterns, leading to overfitting.

Building a large dataset can be a challenging task, but there are several strategies to gather the required data efficiently.

### Automatic Downloading of Images from the Web

Web scraping can be used to download large amounts of images for training datasets. Python libraries like `requests` and `BeautifulSoup` are common tools for this purpose.

#### Example: Downloading Images Using Bing Search API

```python
import os
import requests

# Set up search parameters
API_KEY = "your_bing_api_key"
SEARCH_TERM = "cats"
DOWNLOAD_DIR = "images"
NUM_IMAGES = 50

headers = {"Ocp-Apim-Subscription-Key": API_KEY}
params = {"q": SEARCH_TERM, "count": NUM_IMAGES}
url = "https://api.bing.microsoft.com/v7.0/images/search"

# Create download directory
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

response = requests.get(url, headers=headers, params=params)
data = response.json()

# Download images
for idx, img in enumerate(data["value"]):
    try:
        img_url = img["contentUrl"]
        img_data = requests.get(img_url).content
        with open(os.path.join(DOWNLOAD_DIR, f"{SEARCH_TERM}_{idx}.jpg"), "wb") as img_file:
            img_file.write(img_data)
        print(f"Downloaded {idx + 1}/{NUM_IMAGES}")
    except Exception as e:
        print(f"Failed to download image {idx + 1}: {e}")
```

#### Tips for Web Downloading

- Always check copyright restrictions and ensure compliance with legal regulations.
- Use APIs like Bing or Google Custom Search to streamline image scraping.
- Filter images to avoid irrelevant or low-quality data.

### Record a Video and Split it into Frames

Another way to collect data is by recording videos and extracting frames for annotation and training.

#### Example: Splitting Video into Frames

```python
import cv2
import os

# Define the video source and output directory
video_source = "input_video.mp4"
output_dir = "video_frames"
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_source)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Save each frame as an image
    frame_path = os.path.join(output_dir, f"frame_{frame_count:05d}.jpg")
    cv2.imwrite(frame_path, frame)
    print(f"Saved {frame_path}")
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames from {video_source}")
```

#### Benefits of Using Video Data

- **Efficiency**: Videos can capture many frames in one recording session, saving time compared to capturing individual photos.
- **Diverse Scenarios**: Recording videos in various environments ensures that frames capture different conditions and perspectives.

### What's Next?

After collecting the data, the next step is to annotate it with labels or bounding boxes for training the model. Continue to the next section, [Image Annotation](./image_annotation.md), to learn how to prepare your dataset for training!
