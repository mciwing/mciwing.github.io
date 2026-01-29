# Bonus: Training on Google Colab

<figure markdown="span">
  ![Google Colab](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/1280px-Google_Colaboratory_SVG_Logo.svg.png){ width="250" }
</figure>


Training a YOLO model can be computationally demanding, especially when working with large datasets or running multiple training iterations. This bonus chapter explains how to use **Google Colab** as an alternative to local training and why cloud-based solutions can be advantageous.

---

## Why Use Cloud-Based Training?

Training machine learning models locally is not always practical. Most laptops and desktop computers do not have a dedicated GPU suitable for deep learning. Training on a CPU can take **10-50 times longer** than on a GPU. For our Euro note detection model, what takes 5 minutes on a GPU could take over an hour on a CPU.

While local training on GPU is possible, it requires a lot of setup and maintenance. You need to install the CUDA driver, cuDNN libraries, PyTorch with CUDA support, and manage dependency conflicts. Google Colab comes **pre-configured** with all necessary deep learning libraries and GPU drivers. You can start training within minutes without any installation hassle.

Local development still has advantages in some scenarios:

- **Data privacy**: Sensitive data should not be uploaded to cloud services
- **Large datasets**: Uploading/downloading gigabytes of data can be slow
- **Long training runs**: Free Colab sessions have time limits (~12 hours)
- **Production deployment**: Final models often need local testing

After we have already learned how to train a YOLO model locally, we will now use Google Colab to train our model.

---

???+ info "Video Tutorial"
    If you prefer a visual guide, here is a video tutorial on how to train a YOLO model on Google Colab:

    <div style="text-align: center;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/r0RspiLG260?start=465" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>

## Setting up Google Colab

Navigate to [Google Colab](https://colab.research.google.com/) and sign in (right upper corner) with your Google account. Create a new notebook by clicking **New notebook**.

On the top left you see the name of the current notebook. You can also change the name by clicking on it and typing a new name.

<figure markdown="span"> ![Colab](../../assets/yolo/colab1.png){width=100% }</figure>

By default, Colab uses a CPU to run your code. To enable GPU acceleration - which is the reason we are using Colab in the first place - you need to change the runtime type to a GPU runtime. Therefore:

1. Go to **Runtime > Change runtime type**
2. Select **T4 GPU** (or any available GPU option)
3. Click **Save**

<figure markdown="span"> ![Colab](../../assets/yolo/colab2.png){width=60% }</figure>

You can verify the GPU availability by running the following code in a new code cell in colab:

```python
import torch
print(f"GPU available: {torch.cuda.is_available()}")
print(f"GPU name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'N/A'}")
```

<div class="grid cards" markdown>

-   :white_check_mark: __Correct Setup__

    ---

    ```title=">>> Output"
    GPU available: True
    GPU name: Tesla T4
    ```

-   :x: __Faulty Setup__

    ---

    ```title=">>> Output"
    GPU available: False
    GPU name: N/A
    ```


</div>

The last setup step is to install the YOLO library. There are two ways to do this:

=== "Terminal"

    To install the YOLO library, you can use the terminal (left button of the page) by running the following command:
    
    ```bash
    pip install ultralytics
    ```

    <figure markdown="span"> ![Colab](../../assets/yolo/colab3.png){width=100% }</figure>

=== "Inline Code"

    You can also install the YOLO library by running the following code in a new code cell in colab:
    
    ```python
    !pip install ultralytics
    ```

    Note that the `!` is used to run shell commands in the terminal.

---

## Preparing the files

Before training, you need to upload your dataset and the configuration file to Colab. There are several approaches:

xxxxxxxxxxxxxxx
xxxxxxxxxxxxx


xxxxxxxxxxxxxxxx


### Option A: Google Drive (Recommended)

The most convenient method is to upload your dataset to Google Drive and mount it in Colab.

**Step 1: Upload to Google Drive**

Upload your entire `annotations` folder (containing `images` and `labels` subfolders) to your Google Drive.

```plaintext
📁 My Drive/
└── 📁 yolo_training/
    └── 📁 annotations/
        ├── 📁 images/
        |   ├── 📁 train/
        |   └── 📁 val/
        └── 📁 labels/
            ├── 📁 train/
            └── 📁 val/
```

**Step 2: Mount Google Drive in Colab**

```python
from google.colab import drive
drive.mount('/content/drive')
```

A popup will ask you to authorize access. After mounting, your files are accessible at `/content/drive/MyDrive/`.

### Option B: Direct Upload (Small Datasets)

For small datasets, you can upload directly to the Colab session:

```python
from google.colab import files
uploaded = files.upload()  # Opens file picker
```

???+ warning "Session Storage"
    Files uploaded directly to Colab are **temporary** and will be deleted when the session ends. Use Google Drive for persistent storage.

### Option C: Download from URL

If your dataset is hosted online (e.g., GitHub, cloud storage):

```python
!wget https://example.com/your-dataset.zip
!unzip your-dataset.zip -d /content/dataset
```

---

## Training in Colab

### Install Ultralytics

First, install the YOLO library:

```python
!pip install ultralytics -q
```

The `-q` flag suppresses verbose output.

### Create Configuration File

Create the `config.yaml` file directly in Colab. The paths need to point to your mounted Google Drive location:

```python
config_content = """
# Data
path: /content/drive/MyDrive/yolo_training/annotations
train: images/train
val: images/val

nc: 2

# Classes
names:
  0: 10euro
  1: 5euro
"""

with open('/content/config.yaml', 'w') as f:
    f.write(config_content)
```

### Start Training

Now you can train your model exactly as you would locally:

```python
from ultralytics import YOLO

# Load a pre-trained model
model = YOLO('yolo11n.pt')

# Train the model
results = model.train(
    data='/content/config.yaml',
    epochs=50,
    imgsz=640,
    batch=16,
    device=0  # Use GPU
)
```

???+ tip "Colab Training Settings"
    - **batch size**: Colab's T4 GPU has ~15GB memory. You can often use `batch=32` or higher
    - **device=0**: Explicitly tells YOLO to use the GPU
    - **epochs**: With GPU acceleration, you can afford to train for more epochs

### Monitor Training Progress

Training progress is displayed directly in the notebook output. You can also view the generated plots:

```python
from IPython.display import Image, display

# Display training results
display(Image(filename='/content/runs/detect/train/results.png'))
```

---

## Saving Your Trained Model

After training completes, you need to save your model before the Colab session expires.

### Copy to Google Drive

```python
import shutil

# Copy best model to Google Drive
shutil.copy(
    '/content/runs/detect/train/weights/best.pt',
    '/content/drive/MyDrive/yolo_training/best.pt'
)

# Copy last model as backup
shutil.copy(
    '/content/runs/detect/train/weights/last.pt',
    '/content/drive/MyDrive/yolo_training/last.pt'
)

print("Models saved to Google Drive!")
```

### Download to Local Machine

Alternatively, download the model directly to your computer:

```python
from google.colab import files
files.download('/content/runs/detect/train/weights/best.pt')
```

---

## Complete Colab Notebook

Here is a complete notebook template you can use:

```python
# Cell 1: Setup
from google.colab import drive
drive.mount('/content/drive')

!pip install ultralytics -q

# Cell 2: Configuration
config_content = """
path: /content/drive/MyDrive/yolo_training/annotations
train: images/train
val: images/val
nc: 2
names:
  0: 10euro
  1: 5euro
"""

with open('/content/config.yaml', 'w') as f:
    f.write(config_content)

# Cell 3: Training
from ultralytics import YOLO

model = YOLO('yolo11n.pt')
results = model.train(
    data='/content/config.yaml',
    epochs=50,
    device=0
)

# Cell 4: Save Model
import shutil
shutil.copy(
    '/content/runs/detect/train/weights/best.pt',
    '/content/drive/MyDrive/yolo_training/best.pt'
)
print("Training complete! Model saved to Google Drive.")
```

---

## Tips for Colab Training

???+ tip "Prevent Session Timeout"
    Free Colab sessions disconnect after ~90 minutes of inactivity. Keep the browser tab active during training. For longer runs, consider [Colab Pro](https://colab.research.google.com/signup).

???+ tip "Check GPU Allocation"
    Sometimes Colab assigns a slower GPU or no GPU at all due to high demand. Always verify GPU availability before starting long training runs.

???+ tip "Use Checkpoints"
    If training might exceed session limits, save intermediate checkpoints to Google Drive:
    ```python
    model.train(data='config.yaml', epochs=50, save_period=10)  # Save every 10 epochs
    ```

???+ tip "Resume Training"
    If your session disconnects, you can resume training from the last checkpoint:
    ```python
    model = YOLO('/content/drive/MyDrive/yolo_training/last.pt')
    model.train(data='/content/config.yaml', epochs=50, resume=True)
    ```

---

## Alternative Cloud Platforms

Google Colab is not the only option. Here are some alternatives:

| Platform | Free Tier | GPU Access | Session Limit |
|:---------|:----------|:-----------|:--------------|
| [Google Colab](https://colab.research.google.com/) | Yes | T4/V100 | ~12 hours |
| [Kaggle Notebooks](https://www.kaggle.com/code) | Yes | P100/T4 | 30 hours/week |
| [Lightning AI](https://lightning.ai/) | Yes | T4 | Limited |
| [Paperspace Gradient](https://www.paperspace.com/) | Limited | Various | Varies |

Kaggle is a particularly good alternative with generous GPU quotas and a large community for machine learning.

---

## Summary

Cloud-based training with Google Colab offers a practical solution when local hardware is limited. The key advantages are:

- **Free GPU access** for faster training
- **No setup required** - pre-configured environment
- **Accessible from anywhere** with just a browser

For our Euro note detection project, Colab enables training that would otherwise be impractical on a CPU-only laptop. The trained model can then be downloaded and used locally for inference.

After completing the training (either locally or in Colab), proceed to the [Inference chapter](./inference.md) to test your model on real images and video streams.
