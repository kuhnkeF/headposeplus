|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  6DRepNet (paper) |  3.47 |  4.48 |  3.24 |  2.68 | / | Biwi | / | / | / | / | / |
|    |   |   |   |   |   |   |   |   |   |   |   |
|  6DRepNet |  4.39 |  5.19 |  4.62 |  3.37 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  6DRepNet |  4.04 |  4.78 |  4.30 |  3.03 | ypr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  6DRepNet |  4.44 |  5.38 |  4.54 |  3.40 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✔ |
|  6DRepNet |  4.04 |  4.89 |  4.23 |  3.01 | ypr | Biwi+ |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✔ |
|  6DRepNet |  4.13 |  4.72 |  4.43 |  3.24 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet |  3.84 |  4.32 |  4.18 |  3.01 | ypr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet |  4.15 |  4.85 |  4.34 |  3.26 | pyr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet |  3.81 |  4.37 |  4.09 |  2.98 | ypr | Biwi+ (non cal) |  15678 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet |  3.70 |  4.43 |  4.06 |  2.61 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  6DRepNet |  3.48 |  4.12 |  3.71 |  2.61 | ypr | Biwi (FSA-Net) |  13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  6DRepNet |  3.64 |  4.29 |  4.05 |  2.58 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet |  3.41 |  3.92 |  3.70 |  2.60 | ypr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  6DRepNet |  3.60 |  4.17 |  4.09 |  2.54 | pyr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  6DRepNet |  3.41 |  3.86 |  3.73 |  2.64 | ypr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
