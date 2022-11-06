# Papers

- [ImageNET classification with Deep CNN](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
- YOLO
- SVM

# Motivation / Problem def:

We have a combined interest in self driving cars and we would like to tackle the problem 
of object detection on a specific set of images collected during test-runs of a self-driving car on real-world streets

# Prior Work
- YOLO
- SVM

# Potential Datasets
Email for login: gbhullar@cs.toronto.edu
Password for login: Introtoml@2515

- ImageNET [dataset](https://www.image-net.org/download.php)
- Nuscenes [dataset](https://www.nuscenes.org/nuscenes#download) (#1)
    - Full Dataset (v1.0): 1000 scenes (700 train, 150 val, 150 test)
- Roboflow [dataset](https://public.roboflow.com/object-detection/self-driving-car/3)
    - Obstacle Annotated images
- BDD100k [dataset](https://doc.bdd100k.com/download.html#id1)
    - Weather, scene and timeofday attributes
    

# Project steps / Milestones
- Object Detection
    - ImageNET dataset : Edge detection
        - Train on all 1.2 million (subset: 5k images)
        - Which model: Deep CNN
    - Train the street images using YOLO and Transfer Learning
        - Use weights from the first N-layers of the first model
            - Train another Deep CNN from 4th layer
        - Baselines
            - SVM ??
            - CNN
            - YOLO