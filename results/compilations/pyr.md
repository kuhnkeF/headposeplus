## Results for pyr

|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  WHENet |  8.30 |  9.19 |  9.29 |  6.41 | pyr | Biwi (WHENet) |  15636 | 300W-LP | YOLOv3, cleaned, WHENet | ✖ | ✖ |
|  WHENet |  8.02 |  8.89 |  8.73 |  6.42 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✔ |
|  WHENet |  7.82 |  8.45 |  8.66 |  6.37 | pyr | Biwi (WHENet) |  15636 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet |  7.82 |  8.44 |  8.65 |  6.37 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  WHENet |  7.25 |  8.00 |  8.05 |  5.72 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  WHENet |  7.05 |  7.54 |  7.94 |  5.67 | pyr | Biwi (WHENet) |  15636 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet |  7.05 |  7.54 |  7.94 |  5.67 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet |  6.33 |  7.55 |  6.64 |  4.79 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  Hopenet |  6.09 |  7.11 |  6.47 |  4.70 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net |  6.02 |  6.92 |  6.66 |  4.48 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✔ |
|  FSA-Net |  5.75 |  6.43 |  6.27 |  4.55 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  WHENet |  5.75 |  6.41 |  6.66 |  4.19 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ -> YOLOv3, WHENet | ✖ | ✖ |
|  Hopenet |  5.73 |  7.65 |  5.32 |  4.21 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✔ |
|  FSA-Net |  5.65 |  6.15 |  6.46 |  4.34 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  FSA-Net |  5.42 |  5.75 |  6.08 |  4.44 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet |  5.38 |  7.02 |  5.09 |  4.04 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  Hopenet |  5.36 |  7.01 |  5.02 |  4.05 | pyr | Biwi (Hopenet) |  15666 | 300W-LP | Dockerface, cleaned, Hopenet | ✖ | ✖ |
|  WHENet |  5.27 |  5.75 |  6.12 |  3.95 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  WHENet |  5.26 |  5.87 |  5.64 |  4.27 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  Hopenet |  4.91 |  5.28 |  5.54 |  3.90 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet |  4.80 |  5.48 |  5.14 |  3.78 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  RCRw |  4.55 |  6.34 |  4.55 |  2.74 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✔ |
|  6DRepNet |  4.44 |  5.38 |  4.54 |  3.40 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✔ |
|  6DRepNet |  4.39 |  5.19 |  4.62 |  3.37 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  Hopenet |  4.28 |  5.38 |  4.20 |  3.26 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  FSA-Net |  4.25 |  5.24 |  4.61 |  2.89 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  FSA-Net |  4.23 |  5.12 |  4.69 |  2.88 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet |  4.15 |  4.85 |  4.34 |  3.26 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  PADACO |  4.13 |  4.51 |  4.11 |  3.78 | pyr | Biwi+ |  15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✔ |
|  RCRw |  4.13 |  5.49 |  4.34 |  2.56 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  6DRepNet |  4.13 |  4.72 |  4.43 |  3.24 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net |  4.12 |  4.99 |  4.58 |  2.79 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  PADACO |  4.04 |  4.36 |  3.92 |  3.83 | pyr | Biwi+ (non cal) |  15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  RCRw |  3.86 |  4.73 |  3.95 |  2.89 | pyr | Biwi+ |  15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✔ |
|  6DRepNet |  3.70 |  4.43 |  4.06 |  2.61 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  PADACO |  3.68 |  4.14 |  3.55 |  3.34 | pyr | Biwi (FSA-Net) |  13219 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  6DRepNet |  3.64 |  4.29 |  4.05 |  2.58 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  RCRw |  3.63 |  4.43 |  4.21 |  2.26 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  6DRepNet |  3.60 |  4.17 |  4.09 |  2.54 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  RCRw |  3.55 |  4.06 |  3.77 |  2.81 | pyr | Biwi+ (non cal) |  15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  RCRw |  3.38 |  3.92 |  3.67 |  2.56 | pyr | Biwi (FSA-Net) |  13219 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |

