|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  6DRepNet (paper) | 3.47 | 4.48 | 3.24 | 2.68 | / | Biwi | / | / | / | / | / |
|    |   |   |   |   |   |   |   |   |   |   |   |
|  6DRepNet | 5.09 | 6.55 | 5.21 | 3.50 | pyr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  6DRepNet | 4.63 | 6.18 | 4.76 | 2.94 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  6DRepNet | 4.70 | 5.80 | 5.02 | 3.28 | pyr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet | 4.34 | 5.46 | 4.65 | 2.91 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet | 4.71 | 5.88 | 4.99 | 3.26 | pyr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet | 4.35 | 5.53 | 4.62 | 2.90 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet | 4.01 | 4.99 | 4.37 | 2.66 | pyr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  6DRepNet | 3.73 | 4.67 | 3.98 | 2.54 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  6DRepNet | 3.98 | 4.88 | 4.42 | 2.64 | pyr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet | 3.71 | 4.56 | 4.03 | 2.53 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet | 3.97 | 4.76 | 4.48 | 2.67 | pyr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet | 3.72 | 4.49 | 4.08 | 2.58 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
