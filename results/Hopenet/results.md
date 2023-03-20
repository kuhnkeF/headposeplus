|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  Hopenet (paper) | 4.89 | 6.61 | 4.81 | 3.27 | / | Biwi | / | / | / | / | / |
|    |   |   |   |   |   |   |   |   |   |   |   |
|  Hopenet | 5.36 | 7.01 | 5.02 | 4.05 | pyr | Biwi (Hopenet) | 15666 | 300W-LP | Dockerface, cleaned, Hopenet | ✖ | ✖ |
|  Hopenet | 4.83 | 6.53 | 4.72 | 3.22 | ypr | Biwi (Hopenet) | 15666 | 300W-LP | Dockerface, cleaned, Hopenet | ✖ | ✖ |
|  Hopenet | 6.33 | 7.55 | 6.64 | 4.79 | pyr | Biwi+ | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  Hopenet | 5.67 | 6.85 | 6.47 | 3.69 | ypr | Biwi+ | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  Hopenet | 5.73 | 7.65 | 5.32 | 4.21 | pyr | Biwi+ | 15678 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✔ |
|  Hopenet | 5.09 | 7.09 | 5.04 | 3.14 | ypr | Biwi+ | 15678 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✔ |
|  Hopenet | 6.09 | 7.11 | 6.47 | 4.70 | pyr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 5.47 | 6.36 | 6.39 | 3.66 | ypr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 5.38 | 7.02 | 5.09 | 4.04 | pyr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  Hopenet | 4.83 | 6.49 | 4.89 | 3.13 | ypr | Biwi+ (non cal) | 15678 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  Hopenet | 4.80 | 5.48 | 5.14 | 3.78 | pyr | Biwi (FSA-Net) | 13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  Hopenet | 4.21 | 4.64 | 4.96 | 3.02 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | MTCNN, cleaned, FSA-Net | ✖ | ✖ |
|  Hopenet | 4.91 | 5.28 | 5.54 | 3.90 | pyr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 4.32 | 4.39 | 5.45 | 3.12 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 4.28 | 5.38 | 4.20 | 3.26 | pyr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  Hopenet | 3.82 | 4.75 | 3.98 | 2.73 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
