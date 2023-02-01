|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  FSA-Net (paper) | 4.00 | 4.96 | 4.27 | 2.76 | / | Biwi | / | / | / | / | / |
|    |   |   |   |   |   |   |   |   |   |   |   |
|  FSA-Net | 4.25 | 5.24 | 4.61 | 2.89 | pyr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  FSA-Net | 4.00 | 4.96 | 4.26 | 2.76 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  FSA-Net | 4.12 | 4.99 | 4.58 | 2.79 | pyr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net | 3.91 | 4.78 | 4.29 | 2.66 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net | 4.23 | 5.12 | 4.69 | 2.88 | pyr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  FSA-Net | 4.07 | 5.00 | 4.39 | 2.82 | ypr | Biwi (FSA-Net) | 13219 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  FSA-Net | 5.65 | 6.15 | 6.46 | 4.34 | pyr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  FSA-Net | 5.50 | 6.64 | 6.37 | 3.48 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  FSA-Net | 5.42 | 5.75 | 6.08 | 4.44 | pyr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net | 5.15 | 6.10 | 6.20 | 3.15 | ypr | Biwi+ (non cal) | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net | 6.02 | 6.92 | 6.66 | 4.48 | pyr | Biwi+ | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✔ |
|  FSA-Net | 5.80 | 7.41 | 6.46 | 3.52 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✔ |
|  FSA-Net | 5.75 | 6.43 | 6.27 | 4.55 | pyr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  FSA-Net | 5.44 | 6.84 | 6.30 | 3.18 | ypr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
