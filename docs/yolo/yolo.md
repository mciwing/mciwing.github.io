# YOLO

Ultralytics YOLO is a state-of-the-art, real-time object detection system that is part of the YOLO family of models. Developed and maintained by Ultralytics, this implementation of YOLO is widely recognized for its speed and accuracy in detecting objects in images and videos. Here are some key aspects of Ultralytics YOLO:

- Real-Time Detection: YOLO is known for its ability to perform object detection in real-time. This makes it highly suitable for applications that require immediate detection, such as in video surveillance, autonomous vehicles, and various real-time monitoring systems.
- Single Neural Network: Unlike other detection systems that use separate networks or stages for object localization and classification, YOLO applies a single neural network to the entire image. This network divides the image into regions and predicts bounding boxes and probabilities for each region. These bounding boxes are then weighted by the predicted probabilities.
- Ease of Use: Ultralytics provides a user-friendly platform for using YOLO. Their implementations are often accompanied by detailed documentation, pre-trained models, and example code, making it accessible for both beginners and experienced machine learning practitioners.
- Customization and Training: While pre-trained models are available, users can also train the YOLO model on their own datasets. This allows for customization and adaptation to specific use cases that may not be covered by the standard pre-trained models.
- Wide Range of Applications: YOLO’s efficiency and accuracy have made it popular for a wide range of applications, including pedestrian detection, robot navigation, vehicle detection in traffic, and many more.

## YOLO Approach

YOLO, on the other hand, simplifies this process by using a single neural network that does everything
in one pass. Here’s how it works:

1. Single Neural Network: YOLO applies a single convolutional neural network (CNN) to the full image. This network divides the image into a grid (e.g., 13x13).
2. Grid Cells Predictions: Each cell in the grid is responsible for predicting objects centered in that cell. Each cell predicts a certain number of bounding boxes and confidence scores for those boxes. A confidence score reflects how confident the model is that the box contains an object and also how accurate it thinks the box is.
3. Bounding Box Parameters: Each bounding box has five predictions: x, y, w, h, and a confidence score. (x, y) coordinates represent the center of the box relative to the bounds of the grid cell. Width (w) and height (h) are predicted relative to the whole image. Finally, the confidence score represents the likelihood that the box contains an object and how accurate the box is.
4. Class Predictions: In addition to predicting bounding boxes, each cell also predicts class probabilities. These probabilities are conditioned on the grid cell containing an object.
5. Combining Predictions: The bounding box predictions and class predictions are combined to create a complete detection. If a grid cell is confident that it contains an object, and if the predicted class score is high, then it’s a strong detection.
6. Non-Max Suppression: Since YOLO predicts multiple boxes for each grid cell, it uses a technique called non-max suppression to eliminate overlapping boxes, keeping only the ones with the highest confidence scores.

BILD

Video What is YOLO algorithm? (Codebasics/Youtube) https://www.youtube.com/watch?v=ag3DLKsl2vk

## Advantages and Limitations of YOLO

Advantages of YOLO

- Speed: By processing an image in a single pass, YOLO can perform object detection in real-time. This is a significant advantage over traditional two-step detectors.
- Generalization: Since YOLO sees the entire image during training and testing, it implicitly encodes contextual information about classes and their appearance.
- Versatility: YOLO can be adapted to various object detection tasks and has been extended in many ways since its initial introduction.

Limitations

- Struggles with Small Objects: YOLO can struggle with detecting small objects, especially if they appear in groups, as it tends to predict large bounding boxes.
- Less Precision: While YOLO is fast, it may not be as precise in terms

## Installation & Setup