# Introduction

In this course block and its subsequent chapters we will demonstrate how to build your own YOLO model in practice. 
In the end, you will be able to build a "ready-to-go" model that can detect objects in images, videos, and live streams.

Along the way we will explore the four major steps of building a YOLO model:

``` mermaid
graph LR
  A[Data Acquisition] --> B[Annotation];
  B --> C[Training];
  C --> D[Inference];
  click A "../acquisition" _self
  click B "../annotation" _self
  click C "../training" _self
  click D "../inference" _self
  classDef active fill:#950f42
```


Let's get started! 🚀


---

In addition to the theoretical foundation, we will look at the following chapters using a practical example.  This will enable us to better understand and apply the theoretical concepts.

???+ warning "Training Hardware"
    Training a YOLO model requires a lot of computational resources. The best way to train a computer vision model is to use a GPU. Since a lot of you might work on a laptop without a GPU you can try to train the model on a CPU, but it will take much longer to train the model.
    If your hardware is limited, it is a good idea to use a free online service like [Google Colab](https://colab.research.google.com/) or [Kaggle](https://www.kaggle.com/) to train your model. In the [bonus chapter](colab.md) you will find a guide on how to use Colab to train your model.


## Prerequisites

### 0. :trophy: What's our goal?

We will start with defining a goal for our practical example. 

<div style="text-align: center; margin-top: 1em;">
    <p>
        <i>Build a YOLO model that can detect and classify different types of banknotes (5€ and 10€).</i>
    </p>
</div>

In order to build this kind of model, we will first need to find and generate suitable dataset. 

---

### 1. :file_folder: Project structure

Start with creating a new folder for our project:

```plaintext
📁 yolo_training/
```

### 2. :computer: Virtual environment

Create a [virtual environment](../../python/packages.md#create-a-virtual-environment).
Now, you should have the following structure:

```plaintext
📁 yolo_training/
├── 📁 .venv/
```

Be sure to activate the environment!

### 3. :package: Install packages

Install the necessary packages in this **specific order**: `label-studio`, `ImageEngine`, `opencv-python`, `ultralytics`.
This time, the sequence of installation is important to due some dependencies.


