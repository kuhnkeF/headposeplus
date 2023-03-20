|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  WHENet (paper) | 3.81 | 4.39 | 3.99 | 3.06 | / | Biwi | / | / | / | / | / |
|    |   |   |   |   |   |   |   |   |   |   |   |
|  WHENet | 8.30 | 9.19 | 9.29 | 6.41 | pyr | Biwi (WHENet) | 15636 | 300W-LP | YOLOv3, cleaned, WHENet | ✖ | ✖ |
|  WHENet | 7.62 | 8.77 | 9.80 | 4.30 | ypr | Biwi (WHENet) | 15636 | 300W-LP | YOLOv3, cleaned, WHENet | ✖ | ✖ |
|  WHENet | 7.05 | 7.54 | 7.94 | 5.67 | pyr | Biwi (WHENet) | 15636 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet | 6.41 | 7.22 | 8.17 | 3.84 | ypr | Biwi (WHENet) | 15636 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet | 7.82 | 8.45 | 8.66 | 6.37 | pyr | Biwi (WHENet) | 15636 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet | 7.22 | 8.14 | 9.38 | 4.14 | ypr | Biwi (WHENet) | 15636 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet | 7.82 | 8.44 | 8.65 | 6.37 | pyr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet | 7.22 | 8.14 | 9.38 | 4.14 | ypr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet | 7.05 | 7.54 | 7.94 | 5.67 | pyr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet | 6.41 | 7.21 | 8.16 | 3.84 | ypr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet | 8.02 | 8.89 | 8.73 | 6.42 | pyr | Biwi+ | 15678 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✔ |
|  WHENet | 7.41 | 8.65 | 9.40 | 4.17 | ypr | Biwi+ | 15678 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✔ |
|  WHENet | 7.25 | 8.00 | 8.05 | 5.72 | pyr | Biwi+ | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  WHENet | 6.61 | 7.74 | 8.21 | 3.87 | ypr | Biwi+ | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  WHENet | 5.26 | 5.87 | 5.64 | 4.27 | pyr | Biwi (FSA-Net) | 13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  WHENet | 4.80 | 5.23 | 5.43 | 3.75 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  WHENet | 5.27 | 5.75 | 6.12 | 3.95 | pyr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet | 4.79 | 5.06 | 6.00 | 3.33 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet | 5.75 | 6.41 | 6.66 | 4.19 | pyr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet | 5.32 | 5.87 | 6.60 | 3.50 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |