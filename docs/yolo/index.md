# Computer Vision

Computer Vision is a field of artificial intelligence that enables machines to interpret and understand the visual world. By using digital images from cameras and videos and deep learning models, machines can accurately identify and classify objects - and then react to what they "see." This introduction aims to provide an overview of computer vision, its challenges, and its interconnections with other fields.

## What Is Computer Vision?

Befor we take a closer look at computer vision, we need to introduce artificial intelligence (AI). AI is a broad field that aims to create systems capable of performing tasks that typically require human intelligence. As one of the pioneers of AI, described it:

> "An attempt will be made to find how to make machines use language, form abstractions and concepts, solve kinds of problems now reserved for humans, and improve themselves."
>
> -- *John McCarthy*

Artificial Intelligence is a multidiciplinary field that can be divided into several subfields, each contributing to the overarching goal of simulating intelligent behavior in machines. These subfields include:

- **Machine Learning**
- **Natural Language Processing**
- **Robotics**
- **Computer Graphics**
- **Computer Vision**


These subfields are interconnected; advancements in one often benefit the others. For instance, computer vision is essential in robotics for environment perception and in natural language processing for image captioning.

But now we still want to know: **What is computer vision itself?**

At its core, computer vision seeks to automate tasks that the human visual system can do. It involves techniques for acquiring, processing, analyzing, and understanding images to produce numerical or symbolic information.

<figure markdown="span">
    <div style="background-color: white; display: flex; justify-content: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Human_visual_pathway.svg" style="width: 100%;">
    </div>
    <figcaption style="text-align: center;">Biological Vision (Source: Ai	Miquel Perello Nieto on <a href="https://en.wikipedia.org/wiki/File:Human_visual_pathway.svg">Wikipedia</a>) </figcaption>
</figure>

???+ tip "Interesting Fact"   
    Did you know, that over 50% of the processing in the human brain is devoted directly or indirectly to visual information (Source: [MIT News](https://news.mit.edu/1996/visualprocessing))

So in other words, computer vision transforms visual data into meaningful information. 


### Applications

Computer vision has a wide range of applications across various industries.

???+ example "Possible Applications for Computer Vision"
    <div class="grid cards" markdown>

    -   __Robotics__

        ---

        <figure markdown="span"> ![Image title](../assets/yolo/robot.jpg){width=100% } </figure>

    -   __Autonomous Vehicles__

        ---

        <figure markdown="span"> ![Image title](../assets/yolo/auto.jpg){width=100% } </figure>


    -   __Medical Applications__

        ---

        <figure markdown="span">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Model_of_a_segmented_femur_-_journal.pone.0079004.g005.png" style="width: 50%;">
        <figcaption style="text-align: center;">(Source: Newe A, Ganslandt T on <a href="https://de.wikipedia.org/wiki/Datei:Model_of_a_segmented_femur_-_journal.pone.0079004.g005.png">Wikipedia</a>) </figcaption>
        </figure>

    -   __Quality Control__

        ---

        <figure markdown="span">
            <img src="https://www.elunic.com/de/wp-content/uploads/2020/07/Crack-Bounding-Box-2-450x450.png" style="width: 90%;">
        <figcaption style="text-align: center;">(Source: <a href="https://www.elunic.com/de/showcase/automatisierte-risserkennung/">elunic</a>) </figcaption>
        </figure>

    -   __Retail__

        ---

        <figure markdown="span">
            <img src="https://imageio.forbes.com/specials-images/imageserve/60a53427c26131a1df84b6ef/snapchat-ar/960x0.png" style="width: 100%;">
        <figcaption style="text-align: center;">(Source: SNAP INC via <a href="https://www.forbes.com/sites/lelalondon/2021/05/20/virtual-try-on-is-more-than-a-pandemic-trendand-these-brands-are-reaping-the-rewards/">Forbes</a>) </figcaption>
        </figure>

    -   __Facial Recognition__

        ---

        <figure markdown="span">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/ef/Face_detection.jpg" style="width: 100%;">
        <figcaption style="text-align: center;">(Source: Sylenius on <a href="https://commons.wikimedia.org/wiki/File:Face_detection.jpg">Wikipedia</a>) </figcaption>
        </figure>

    </div>

### How can Machines "See"?

When we look at the world, our eyes receive light reflected from objects. Similarly, cameras capture light to create images. 

<figure markdown="span">
    <img src="https://www.neg.co.jp/en/assets/img/rd/topics/cover-glass_03.png" style="width: 100%;">
    <figcaption style="text-align: center;">
        Camera sensor prinicpal (Source: <a href="https://www.neg.co.jp/en/rd/topics/product-cover-glass/">Neg</a>) 
    </figcaption>
</figure>

However, interpreting these images to understand the scene involves complex algorithms that can discern patterns, shapes, and colors. This process involves several steps:

1. **Image Acquisition**: Capturing the visual data using cameras or sensors.
2. **Preprocessing**: Enhancing image quality and correcting distortions.
3. **Feature Extraction**: Identifying edges, textures, and other significant parts of the image.
4. **High-Level Processing**: Recognizing objects, understanding scenes, and making decisions.


### Challenges in Computer Vision

<div class="grid cards" markdown>

-   __Inverse Problem__ 

    --- 
    One of the fundamental challenges in computer vision is the inverse problem: reconstructing a 3D scene from a 2D image. Since multiple 3D scenes can produce the same 2D projection, the problem is ill-posed.

-   <figure markdown="span">
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/11/Ames_room_forced_perspective.jpg" style="width: 100%;">
    <figcaption style="text-align: center;">(Source: mosso on <a href="https://commons.wikimedia.org/wiki/File:Ames_room_forced_perspective.jpg">Wikipedia</a>) </figcaption>
    </figure>

-   <figure markdown="span">
        <img src="https://csdl-images.ieeecomputer.org/trans/tp/2022/04/figures/palaz7-3030701.gif" style="width: 100%;">
    <figcaption style="text-align: center;">(Source: Palazzi et al at <a href="https://www.computer.org/csdl/journal/tp/2022/04/09222285/1nTpT7bj1qU">Computer.org</a>) </figcaption>
    </figure>

-   __Variability Due to Viewpoint__ 

    --- 
    An object can look vastly different from various angles. For example, a car viewed from the front, side, or top presents different shapes and features, complicating recognition tasks.

-   __Deformation__ 

    --- 
    Non-rigid objects, like clothing or human bodies, can change shape, making it challenging to maintain consistent recognition.

-   <figure markdown="span"> ![Image title](../assets/yolo/Pferd.jpg){width=100% } </figure>

-   <figure markdown="span"> ![Image title](../assets/yolo/kid.jpg){width=100% } </figure>

-   __Occlusion__ 

    --- 
    Objects in images often block parts of other objects. Detecting partially visible objects requires algorithms to infer the hidden parts.

-   __Illumination__ 

    --- 
    Lighting conditions can alter the appearance of objects. An apple under bright sunlight looks different from one under indoor lighting.

-   <figure markdown="span">
        <img src="https://www.flocutus.de/wordpress/wp-content/uploads/unter_ueberbelichtet_rahmen.jpg" style="width: 100%;">
    <figcaption style="text-align: center;">(Source: <a href="https://www.flocutus.de/besser-fotografieren-belichtungbetter-photography-exposure/">Flocutus</a>) </figcaption>
    </figure>

-   <figure markdown="span">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/09/Radsport.jpg" style="width: 100%;">
    <figcaption style="text-align: center;">(Source: Osi on <a href="https://commons.wikimedia.org/wiki/File:Radsport.jpg">Wikipedia</a>) </figcaption>
    </figure>

-   __Motion Blur__ 

    --- 
    Movement during image capture can blur images, obscuring details necessary for recognition.

-   __Optical Illusions__ 

    --- 
    Our perception can be deceived by optical illusions, where our brain interprets images differently from the actual measurements.

-   <figure markdown="span">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Grey_square_optical_illusion_proof2.svg" style="width: 100%;">
    </figure>

-   <figure markdown="span">
        <img src="https://www.researchgate.net/profile/Nizar-Massouh/publication/325311506/figure/fig1/AS:651550879932418@1532353243401/shows-an-example-of-Intra-Class-variation-on-the-Chair-class-But-how-will-a-machine.png" style="width: 100%;">
    <figcaption style="text-align: center;">(Source: Nizar Massouh on <a href="https://www.researchgate.net/figure/shows-an-example-of-Intra-Class-variation-on-the-Chair-class-But-how-will-a-machine_fig1_325311506">ResearchGate</a>) </figcaption>
    </figure>

-   __Intra Class Variation__ 

    --- 
    Objects within the same category can look very different.Chairs come in numerous designs—armchairs, stools, recliners—but they all serve the same function. Recognizing all variations as "chairs" is challenging for computer vision systems.


-   __Number of Categories__ 

    --- 
    There are thousands of object categories, each with its own variations. Building systems that can recognize all of them requires extensive data and sophisticated algorithms.

-   <figure markdown="span">
        <img src="https://www.researchgate.net/profile/Cees-Snoek/publication/224577638/figure/fig1/AS:340731802734626@1458248200818/Object-categories-of-the-PASCAL-Visual-Object-Challenge-2007-5-used-in-the-image.png" style="width: 100%;">
    <figcaption style="text-align: center;">(Source: Cees Snoek on <a href="https://www.researchgate.net/figure/Object-categories-of-the-PASCAL-Visual-Object-Challenge-2007-5-used-in-the-image_fig1_224577638">ResearchGate</a>) </figcaption>
    </figure>

</div>


## Approaches in Computer Vision

Over the years, various approaches have been developed to tackle this complex problem.

### Traditional Approaches in Object Detection

Before the rise of deep learning, object detection relied heavily on handcrafted features and traditional machine learning techniques.

- **Haar Cascades**: Introduced by Viola and Jones in 2001, Haar-like features were used for rapid face detection by scanning an image at multiple scales and positions.
    https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d
- **Histogram of Oriented Gradients (HOG)**: Proposed for human detection, HOG features capture edge orientations and are combined with Support Vector Machines (SVMs) for classification.
    https://de.wikipedia.org/wiki/Histogram_of_oriented_gradients

comparison: https://medium.com/@goutam0157/haar-cascade-classifier-vs-histogram-of-oriented-gradients-hog-6f4373ca239b


--<> https://medium.com/@rajshekhar_k/introduction-to-computer-vision-7cfdacfc3f2e

### Deep Learning Approaches
The advent of deep learning revolutionized computer vision by enabling models to learn features directly from data. Convolutional Neural Networks (CNNs) can automatically learn hierarchical feature representations from images, eliminating the need for manual feature extraction.

**ImageNet Challenge**: In 2012, AlexNet significantly reduced error rates in image classification, demonstrating the power of CNNs.

Extending CNNs to object detection led to the development of region-based methods that combine localization and classification.

#### Multi-Stage Object Detection

- R-CNN (Regions with CNN Features)
- Fast R-CNN
- Faster R-CNN

#### One-Stage Object Detection
- SSD (Single Shot MultiBox Detector)
- YOLO

xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxx
yolo vs ssd
https://keylabs.ai/blog/yolov8-vs-ssd-choosing-the-right-object-detection-model/

ssd
https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab
https://developers.arcgis.com/python/latest/guide/how-ssd-works/

rcnn vs fast-rcnn vs faster-rcnn vs yolo
https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e

faster-rcnn vs yolo vs ssd
https://medium.com/ibm-data-ai/faster-r-cnn-vs-yolo-vs-ssd-object-detection-algorithms-18badb0e02dc
https://pro.arcgis.com/en/pro-app/latest/tool-reference/image-analyst/object-detection.htm



### Limitations of Previous Methods

Despite advancements, these methods faced challenges:

- **Complex Pipelines**: Multiple stages increased system complexity and potential error points.
- **Speed vs. Accuracy Trade-off**: Achieving real-time performance often meant sacrificing detection accuracy.
- **Resource Demands**: High computational and memory requirements limited deployment on devices with constrained resources.

### Introduction to YOLO

YOLO, proposed by Joseph Redmon et al. in 2016, redefined object detection by treating it as a single regression problem.

#### How YOLO Differs

- **Unified Architecture**: Processes the entire image with a single neural network, predicting bounding boxes and class probabilities simultaneously.
- **Grid-Based Prediction**: Divides the image into an \( S \times S \) grid, where each cell predicts a fixed number of bounding boxes and confidence scores.
- **Real-Time Performance**: Capable of processing images at high frame rates suitable for real-time applications.

*Example*: A drone using YOLO to detect and avoid obstacles while flying autonomously.

#### Advantages of YOLO

- **Speed**: Processes images quickly, achieving up to 45 frames per second with YOLOv1.
- **Global Context**: Considers the entire image during training and inference, reducing false positives in background regions.
- **Simplified Pipeline**: Eliminates the need for complex region proposal algorithms and multiple processing stages.

*Example*: A wearable device for visually impaired individuals that recognizes and announces nearby objects in real-time.

conclution
The evolution of object detection methods reflects the ongoing pursuit of balancing accuracy and efficiency. From traditional feature-based techniques to deep learning models, each approach has contributed to our understanding and capabilities in computer vision. YOLO stands out by offering a fast and accurate solution, simplifying the detection pipeline and enabling practical real-world applications.

## Different Tasks in Object Recognition

Within the Object Recognition there are different tasks that can be performed.

BILD

1. Classification
    - Purpose: The goal is to categorize an entire image into a specific class or category. For example, determining whether an image is of a cat, a dog, a car, etc.
    - Use Case: Sorting images into categories, like identifying the breed of a dog in a photo.
2. Detection
    - Purpose: Object detection not only categorizes objects within an image but also locates them using bounding boxes. It can detect multiple objects and their types in a single image.
    - Use Case: Identifying and locating different objects in a street scene, like cars, pedestrians, and traffic signs.
3. Segmentation
    - Purpose: Image segmentation is used to understand and analyze the shape and location of objects at a pixel level.
    - Use Case: Medical imaging to delineate different tissue types, autonomous vehicles for understanding the road environment.
4. Pose Estimation
    - Purpose: Pose estimation is about determining the position and orientation of objects or beings (usually humans). In human pose estimation, it involves identifying the position of body joints.
    - Use Case: Analyzing human activities in sports, monitoring exercises for physiotherapy, or in gaming for motion capture.




<div class="annotate" markdown>

- **Machine Learning** (1) 
- **Natural Language Processing**
- **Robotics**
- **Computer Graphics**
- **Computer Vision**

</div>

1.  <figure markdown="span"> ![Image title](../assets/yolo/robot.jpg){width=100% } </figure>