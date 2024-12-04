
# Approaches in CV
To tackle those complex problems, over the years, various approaches have been developed.

## Traditional Approaches in Object Detection

Before the rise of deep learning, object detection relied heavily on handcrafted features and traditional machine learning techniques.

#### Haar Cascades

Introduced by Viola and Jones in 2001, Haar-like features were used for rapid face detection by scanning an image at multiple scales and positions.

???+ example "Example: Haar Cascades"
    
    <figure markdown="span"> ![Image title](../assets/yolo/output_haar_cascade.jpg){width=70% } </figure>

    ??? code "Code"
    
        ``` py
        #Source: https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d

        #-- Load Packages
        import cv2
        from skimage import data

        #-- Load Image and Convert to RGB
        image = data.astronaut()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert to RGB

        #-- Load Haar Cascades
        f_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        e_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        #-- Detect Faces and Eyes
        faces = f_cascade.detectMultiScale(image, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_color = img[y:y+h, x:x+w]
            eyes = e_cascade.detectMultiScale(roi_color)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        #-- Display and Save Image
        cv2.imwrite('output_haar_cascade.jpg',image)
        cv2.imshow('Haar Cascade',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        ```

#### HOG

Proposed for human detection, Histogram of Oriented Gradients (HOG) features capture edge orientations and are combined with Support Vector Machines (SVMs) for classification.

???+ example "Example: HOG"
    
    <figure markdown="span"> ![Image title](../assets/yolo/output_hog.jpg){width=70% } </figure>

    ??? code "Code"
    
        ``` py
        #Source: https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_hog.html

        #-- Load Packages
        import cv2
        from skimage.feature import hog
        from skimage import data, exposure

        #-- Load Image
        image = data.astronaut()

        #-- Compute HOG
        fd, hog_image = hog(
            image,
            orientations=8,
            pixels_per_cell=(16, 16),
            cells_per_block=(1, 1),
            visualize=True,
            channel_axis=-1,
        )
        # Rescale histogram for better display
        hog_image= exposure.rescale_intensity(hog_image, in_range=(0, 10))
        hog_image = cv2.normalize(hog_image, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        #-- Display and Save Image
        cv2.imwrite('output_hog.jpg',hog_image)
        cv2.imshow('HOG',hog_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        ```
    
If you want to learn more about Haar Cascades and HOG, look [here](https://medium.com/@goutam0157/haar-cascade-classifier-vs-histogram-of-oriented-gradients-hog-6f4373ca239b)

## Deep Learning Approaches

<figure markdown="span">
  <img src="https://media.geeksforgeeks.org/wp-content/uploads/20231218174301/max.png" width="100%" />
  <figcaption style="text-align: center;">Convolutional Neural Network Architecture (Source: <a href="https://www.geeksforgeeks.org/introduction-convolution-neural-network/">Geeksforgeeks.org</a>)</figcaption>
</figure>

Deep learning has significantly advanced the field of computer vision by enabling models to learn features directly from data. Convolutional Neural Networks (CNNs) automatically learn hierarchical feature representations from images, eliminating the need for manual feature extraction. In this section, we'll explore deep learning approaches to object detection, focusing on both multi-stage and one-stage detectors.

???+ info

    At the time of writing, models like YOLOv11 and SSD are popular choices for object detection tasks. Keep in mind that the field is rapidly evolving, and newer models may offer improved performance in the future.

---

### Multi-Stage Object Detection

Multi-stage detectors involve multiple steps to detect objects within images. They generally consist of generating region proposals and then classifying these proposals.

#### R-CNN 

Regions with Convolutional Neural Networks (R-CNN) was introduced by Girshick et al. in 2014. It was one of the first methods to apply deep learning to object detection.

<figure markdown="span">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20200219161502/RCNN1.png" style="width: 100%;">
    <figcaption style="text-align: center;">R-CNN Architecture (Source: <a href="https://www.geeksforgeeks.org/r-cnn-region-based-cnns/">Geeksforgeeks.org</a>)</figcaption>
</figure>

**Workflow:**

1. **Region Proposal**: Use selective search to generate around 2,000 region proposals.
2. **Feature Extraction**: Warp each region to a fixed size and extract features using a CNN.
3. **Classification**: Use class-specific linear SVMs to classify each region.

**Limitations:**

- **Slow Training and Inference**: Each region proposal is processed individually, leading to high computational costs.
- **Storage Requirements**: Features need to be stored for each region, consuming significant disk space.
- **Complex Pipeline**: Involves multiple training stages.

#### Fast R-CNN

To address the limitations of R-CNN, Girshick proposed Fast R-CNN in 2015.

<figure markdown="span">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20200219160147/fast-RCNN1-1024x416.png" style="width: 100%;">
    <figcaption style="text-align: center;">Fast R-CNN Architecture (Source: <a href="https://www.geeksforgeeks.org/fast-r-cnn-ml/">Geeksforgeeks.org</a>)</figcaption>
</figure>

**Improvements:**

1. **Single-Stage Training**: The entire model is trained end-to-end.
2. **ROI Pooling**: Extracts a fixed-length feature vector from the feature map for each region proposal.
3. **Multi-Task Loss**: Simultaneously predicts class probabilities and bounding box offsets.

**Advantages:**

- **Faster Training and Inference**: Processes the entire image only once.
- **Simplified Pipeline**: Reduces complexity.

#### Faster R-CNN

Ren et al. introduced Faster R-CNN in 2016, integrating the region proposal mechanism into the network itself via the Region Proposal Network (RPN).

<figure markdown="span">
    <img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*tTqg3W165itg-LVRFxHJfA.jpeg" style="width: 100%;">
    <figcaption style="text-align: center;">Faster R-CNN Architecture (Source: <a href="https://towardsdatascience.com/faster-r-cnn-for-object-detection-a-technical-summary-474c5b857b46">Geeksforgeeks.org</a>)</figcaption>
</figure>

**Key Components:**

1. **Region Proposal Network (RPN)**: Generates region proposals directly.
2. **Shared Computation**: Shares convolutional layers with the detection network.
3. **Anchor Boxes**: Uses predefined boxes of various sizes and aspect ratios.

**Benefits:**

- **Improved Speed**: Eliminates the need for external region proposal methods.
- **High Accuracy**: Achieves state-of-the-art results.

???+ example "Example: Object Detection with Faster R-CNN"

    <div class="grid cards" markdown>

    -   __Input__

        ---

        <figure markdown="span"> ![Input](../assets/yolo/dog.jpg){width=100% } </figure>

    -   __Output__

        ---

        <figure markdown="span"> ![Output](../assets/yolo/dog_frcnn.png){width=100% } </figure>

    </div>

    ??? code "Code"

        ```python
        import torch
        from torchvision import models, transforms
        from PIL import Image
        import matplotlib.pyplot as plt

        # Load a pre-trained Faster R-CNN model
        model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
        model.eval()

        # Transform the input image
        transform = transforms.Compose([
            transforms.ToTensor(),
        ])

        # Load and transform the image
        image = Image.open('dog.jpg')
        image_tensor = transform(image)

        # Perform object detection
        with torch.no_grad():
            outputs = model([image_tensor])

        # Visualize the results
        labels = outputs[0]['labels'].numpy()
        scores = outputs[0]['scores'].detach().numpy()
        boxes = outputs[0]['boxes'].detach().numpy()

        # COCO dataset label names (for mapping label IDs to names)
        COCO_INSTANCE_CATEGORY_NAMES = [
            '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
            'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
            'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
            'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A',
            'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
            'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
            'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
            'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
            'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
            'N/A', 'N/A', 'toilet', 'N/A', 'TV', 'laptop', 'mouse', 'remote', 'keyboard',
            'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A',
            'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
        ]

        # Plot the image with bounding boxes and labels
        fig, ax = plt.subplots(1)
        ax.imshow(image)
        ax.axis('off')  # Turn off the axes
        for idx, box in enumerate(boxes):
            if scores[idx] > 0.8:
                xmin, ymin, xmax, ymax = box
                width, height = xmax - xmin, ymax - ymin
                rect = plt.Rectangle((xmin, ymin), width, height, fill=False, color='red', linewidth=2)
                ax.add_patch(rect)
                # Add label with score
                label_text = f"{COCO_INSTANCE_CATEGORY_NAMES[labels[idx]]}: {scores[idx]:.2f}"
                ax.text(xmin, ymin - 5, label_text, color='red', fontsize=10, backgroundcolor='white')
        plt.tight_layout()
        plt.show()

        ```

---

### One-Stage Object Detection

One-stage detectors perform detection in a single, unified network without separate region proposal steps.

#### SSD 

Introduced by Liu et al. in 2016, SSD (Single Shot MultiBox Detector) is a one-stage detector that discretizes the output space of bounding boxes.

<figure markdown="span">
  <img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*51joMGlhxvftTxGtA4lA7Q.png" width="100%" />
  <figcaption style="text-align: center;">SSD Architecture (Source: <a href="https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab">Medium</a>)</figcaption>
</figure>

**Key Features:**

1. **Single-Shot Detection**: Performs object localization and classification in one forward pass.
2. **Multi-Scale Feature Maps**: Uses feature maps at multiple scales.
3. **Default Boxes (Anchors)**: Handles different aspect ratios and scales.

**Advantages:**

- **Real-Time Performance**: Suitable for applications requiring speed.
- **Balance of Speed and Accuracy**: Good trade-off between detection speed and accuracy.

???+ example "Example: Object Detection with SSD"

    <div class="grid cards" markdown>

    -   __Input__

        ---

        <figure markdown="span"> ![Input](../assets/yolo/dog.jpg){width=100% } </figure>

    -   __Output__

        ---

        <figure markdown="span"> ![Output](../assets/yolo/dog_ssd.png){width=100% } </figure>

    </div>

    ??? code "Code"

        ```python
        import torch
        from torchvision import models, transforms
        from PIL import Image
        import matplotlib.pyplot as plt

        # Load a pre-trained SSD model
        model = models.detection.ssd300_vgg16(pretrained=True)
        model.eval()

        # Transform the input image
        transform = transforms.Compose([
            transforms.Resize((300, 300)),
            transforms.ToTensor(),
        ])

        # Load and transform the image
        image = Image.open('dog.jpg')
        original_width, original_height = image.size
        image_tensor = transform(image)

        # Perform object detection
        with torch.no_grad():
            outputs = model([image_tensor])

        # Extract results
        labels = outputs[0]['labels'].numpy()
        scores = outputs[0]['scores'].detach().numpy()
        boxes = outputs[0]['boxes'].detach().numpy()

        # Scale boxes back to original image size
        boxes[:, [0, 2]] *= original_width / 300  # Scale x-coordinates
        boxes[:, [1, 3]] *= original_height / 300  # Scale y-coordinates

        # Plot the image with bounding boxes and labels
        fig, ax = plt.subplots(1)
        ax.imshow(image)
        ax.axis('off')  # Turn off the axes
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove padding/margins
        for idx, box in enumerate(boxes):
            if scores[idx] > 0.5:
                xmin, ymin, xmax, ymax = box
                width, height = xmax - xmin, ymax - ymin
                rect = plt.Rectangle((xmin, ymin), width, height, fill=False, color='red', linewidth=2)
                ax.add_patch(rect)
                # Add label with score
                label_text = f"{COCO_INSTANCE_CATEGORY_NAMES[labels[idx]]}: {scores[idx]:.2f}"
                ax.text(xmin, ymin - 5, label_text, color='red', fontsize=10, backgroundcolor='white')

        # Save the plot to remove additional padding (optional)
        plt.savefig("output_ssd.png", bbox_inches='tight', pad_inches=0, dpi=300)
        plt.show()

        ```

#### YOLO 

YOLO (You Only Look Once), introduced by Redmon et al., is designed for real-time object detection.

<figure markdown="span">
  <img src="https://pjreddie.com/media/image/model2.png" width="100%" />
  <figcaption style="text-align: center;">YOLO Architecture</figcaption>
</figure>

**Key Characteristics:**

1. **Unified Detection Framework**: Treats object detection as a regression problem.
2. **Grid-Based Prediction**: Divides the image into a grid.
3. **Real-Time Speed**: Capable of processing images at high frame rates.

???+ example "Example: Object Detection with YOLOv8"

    <div class="grid cards" markdown>

    -   __Input__

        ---

        <figure markdown="span"> ![Input](../assets/yolo/dog.jpg){width=100% } </figure>

    -   __Output__

        ---

        <figure markdown="span"> ![Output](../assets/yolo/dog_yolo.jpg){width=100% } </figure>

    </div>

    ??? code "Code"

        ```python
        from ultralytics import YOLO

        # Load a pre-trained YOLOv8 model
        model = YOLO("yolov8n.pt")

        # Perform object detection on an image
        results = model("input.jpg", save=True, conf=0.5)

        # Display the results
        results[0].show()
        ```

**Advantages:**

- **Speed**: Processes images quickly.
- **End-to-End Differentiable**: Allows optimization of the entire model during training.

**Limitations:**

- **Lower Accuracy on Small Objects**: May struggle with detecting smaller objects compared to multi-stage detectors.

???+ question "Comparing Detectors"

    - **Which detector is faster, SSD or Faster R-CNN?**
    - **Which detector might be better for detecting small objects?**

    **Answer:**

    - SSD is generally faster than Faster R-CNN because it processes images in a single pass.
    - Faster R-CNN might be better for detecting small objects due to its region proposal mechanism.

---

### Comparison

| Method        | Speed         | Accuracy       | Complexity | Suitable For                     |
|---------------|---------------|----------------|------------|----------------------------------|
| R-CNN         | Slow          | High           | High       | Research, small datasets         |
| Fast R-CNN    | Moderate      | High           | Moderate   | Applications requiring accuracy  |
| Faster R-CNN  | Moderate      | Very High      | Moderate   | Balanced speed and accuracy      |
| SSD           | Fast          | Moderate-High  | Low        | Real-time applications           |
| YOLO          | Very Fast     | High           | Low        | Real-time applications           |

**Key Takeaways**:

- **Multi-Stage Detectors**: Offer higher accuracy but at the cost of speed and computational complexity.
- **One-Stage Detectors**: Provide faster inference suitable for real-time applications, with a trade-off in accuracy.

---

## Conclusion

Object detection has evolved significantly with the development of deep learning methods. Multi-stage detectors like Faster R-CNN provide high accuracy by carefully analyzing region proposals but can be computationally intensive. One-stage detectors like SSD and YOLO offer faster detection suitable for real-time applications, making them ideal for scenarios where speed is crucial.


???+ info "🎉"

    Congratulations, you've gained an understanding of deep learning approaches in object detection!

    <blockquote class="reddit-embed-bq" style="height:500px" data-embed-height="659"><a href="https://www.reddit.com/r/ProgrammerHumor/comments/1g2tv7a/parsertongue/">parserTongue</a><br> by <a href="https://www.reddit.com/user/Ange1ofD4rkness/">u/Ange1ofD4rkness</a> in <a href="https://www.reddit.com/r/ProgrammerHumor/">ProgrammerHumor</a></blockquote><script async src="https://embed.reddit.com/widgets.js" charset="UTF-8"></script>

## What's Next?

In the upcoming sections, we'll delve deeper into YOLO, explore training custom models, and discuss real-world applications.

---

**References**:

- Liu, W. et al. (2016). "SSD: Single Shot MultiBox Detector". *European Conference on Computer Vision (ECCV)*.
- Girshick, R. (2015). "Fast R-CNN". *IEEE International Conference on Computer Vision (ICCV)*.
- Ren, S. et al. (2016). "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks". *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
- Redmon, J. et al. (2016). "You Only Look Once: Unified, Real-Time Object Detection". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*.

**Further Reading**:

- [Understanding SSD MultiBox—Real-Time Object Detection In Deep Learning](https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab)
- [R-CNN, Fast R-CNN, Faster R-CNN, YOLO — Object Detection Algorithms](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)
- [YOLOv8 vs SSD: Choosing the Right Object Detection Model](https://keylabs.ai/blog/yolov8-vs-ssd-choosing-the-right-object-detection-model/)