# Inference

``` mermaid
graph LR
  A[Data Acquisition]:::active --> B[Annotation];
  B:::active --> C[Training];
  C:::active --> D[Inference]:::active;
  click A "../acquisition" _self
  click B "../annotation" _self
  click C "../training" _self
  click D "../inference" _self
  classDef active fill:#950f42
```

Now that our model is trained and optimized, it’s time to use it for **inference**, meaning we will test the model by running it on new images and evaluating its real-world performance.

Therefore we start by adding a last notebook to our project folder:

```plaintext hl_lines="13"
📁 yolo_training/
├── 📁 .venv/
├── 📁 rawdata/
├── 📁 annotations/
|   ├── 📁 images/
|   |   ├── 📁 train/
|   |   └── 📁 val/
|   └── 📁 labels/
|       ├── 📁 train/
|       └── 📁 val/
├── 📄 config.yaml
├── 📄 data_acquisition.ipynb
├── 📄 inference.ipynb
└── 📄 training.ipynb
```


## Loading the Trained Model
Before making predictions, we need to load the trained YOLO model. The weights for the best-performing model are stored in the `runs/detect/trainX/weights/best.pt` file.

To load the model in Python we simply run:  

```python
model = YOLO("./runs/detect/trainX/weights/best.pt")  # Update with your actual path
```

???+ info "Best vs. Last Model"
    If you want to use the **last trained model** instead of the best-performing one, replace `best.pt` with `last.pt`.

---

## Running Inference on Images
Now that the model is loaded, we can use this model like we did in the [previous chapters](../video/index.md#inference).

<img 
        src="/assets/yolo/cv_inference.gif" alt="inference trained model" 
        style="height: 300px; border-radius:10px;"
    >

As we can see in the gif above, the model is able to detect the 5€ and 10€ bills. Even though it is not perfect (especially when there is a overlap of bills), it is still able to detect the bills in most of the cases.

---

With inference, we can now **test our trained YOLO model** on new images, videos, and live streams. By adjusting settings like confidence thresholds, image resolution, and hardware acceleration, we can further **improve performance and accuracy** for real-world applications. 🚀


## Conclusion

Throughout this guide, we've taken a deep dive into the world of Computer Vision, exploring how YOLO (You Only Look Once) and its related techniques enable fast and accurate object detection. From understanding the fundamentals to training a custom model and deploying it in real-world applications, this journey has equipped you with the knowledge needed to leverage YOLO in various scenarios.




???+ info "🎉"
    
    Congratulations! You've completed the our computer vision journey. You should now be able to build your own custom YOLO models for your own projects and use them to detect objects in images, videos, and live streams.
    
    <figure markdown="span">
      ![Celebration](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif){ width="350" }
    </figure>