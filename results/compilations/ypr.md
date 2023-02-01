## Results for ypr

|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  WHENet  | 7.62 | 8.77 | 9.80 | 4.30 | ypr | Biwi (WHENet) | 15636 | 300W_LP | YOLOv3, cleaned, WHENet | ✖ | ✖ |
|  WHENet  | 7.41 | 8.65 | 9.40 | 4.17 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✔ |
|  WHENet  | 7.22 | 8.14 | 9.38 | 4.14 | ypr | Biwi (WHENet) | 15636 | 300W_LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet  | 7.22 | 8.14 | 9.38 | 4.14 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet  | 6.61 | 7.74 | 8.21 | 3.87 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  WHENet  | 6.41 | 7.22 | 8.17 | 3.84 | ypr | Biwi (WHENet) | 15636 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet  | 6.41 | 7.21 | 8.16 | 3.84 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net | 5.80 | 7.41 | 6.46 | 3.52 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✔ |
|  Hopenet | 5.67 | 6.85 | 6.47 | 3.69 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  FSA-Net | 5.50 | 6.64 | 6.37 | 3.48 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  Hopenet | 5.47 | 6.36 | 6.39 | 3.66 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net | 5.44 | 6.84 | 6.30 | 3.18 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  WHENet  | 5.32 | 5.87 | 6.60 | 3.50 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  FSA-Net | 5.15 | 6.10 | 6.20 | 3.15 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 5.09 | 7.09 | 5.04 | 3.14 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✔ |
|  Hopenet | 4.83 | 6.53 | 4.72 | 3.22 | ypr | Biwi (Hopenet) | 15666 | 300W_LP | Dockerface, cleaned, Hopenet | ✖ | ✖ |
|  Hopenet | 4.83 | 6.49 | 4.89 | 3.13 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  WHENet  | 4.80 | 5.23 | 5.43 | 3.75 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  WHENet  | 4.79 | 5.06 | 6.00 | 3.33 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet| 4.63 | 6.18 | 4.76 | 2.94 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  RCRw    | 4.39 | 6.31 | 3.98 | 2.88 | ypr | Biwi+ | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✔ |
|  6DRepNet| 4.35 | 5.53 | 4.62 | 2.90 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet| 4.34 | 5.46 | 4.65 | 2.91 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 4.32 | 4.39 | 5.45 | 3.12 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 4.21 | 4.64 | 4.96 | 3.02 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  RCRw    | 4.09 | 5.53 | 3.86 | 2.86 | ypr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  FSA-Net | 4.07 | 5.00 | 4.39 | 2.82 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  PADACO  | 4.05 | 4.45 | 3.82 | 3.87 | ypr | Biwi+ | 15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✔ |
|  FSA-Net | 4.00 | 4.96 | 4.26 | 2.76 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  PADACO  | 3.97 | 4.31 | 3.68 | 3.92 | ypr | Biwi+ (non cal) | 15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  FSA-Net | 3.91 | 4.78 | 4.29 | 2.66 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 3.82 | 4.75 | 3.98 | 2.73 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  6DRepNet| 3.73 | 4.67 | 3.98 | 2.54 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  6DRepNet| 3.72 | 4.49 | 4.08 | 2.58 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet| 3.71 | 4.56 | 4.03 | 2.53 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  RCRw    | 3.71 | 4.60 | 3.64 | 2.89 | ypr | Biwi+ | 15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✔ |
|  PADACO  | 3.69 | 4.20 | 3.31 | 3.56 | ypr | Biwi (FSA-Net) | 13219 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  RCRw    | 3.63 | 4.51 | 3.78 | 2.60 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  RCRw    | 3.44 | 3.96 | 3.53 | 2.84 | ypr | Biwi+ (non cal) | 15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  RCRw    | 3.34 | 3.91 | 3.43 | 2.68 | ypr | Biwi (FSA-Net) | 13219 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
