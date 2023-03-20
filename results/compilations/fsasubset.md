# Results on Biwi FSA-Net subset

|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  WHENet | 4.79 | 5.06 | 6.00 | 3.33 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  FSA-Net | 3.91 | 4.78 | 4.29 | 2.66 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✖ |
|  Hopenet | 3.82 | 4.75 | 3.98 | 2.73 | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✖ |
|  **6DRepNet** |  **3.41** |  **3.92** |  **3.70** |  **2.60** | ypr | Biwi (FSA-Net) |  13219 | 300W-LP | Biwi+ -> MTCNN, FSA-Net | ✖ | ✖ |
|  RCRw** | 3.63 | 4.51 | 3.78 | **2.60** | ypr | Biwi (FSA-Net) | 13219 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✖ |
| | | | | | | | | | | | |
|  PADACO | 3.69 | 4.20 | **3.31** | 3.56 | ypr | Biwi (FSA-Net) | 13219 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |
|  **RCRw** | **3.34** | **3.91** | 3.43 | **2.68** | ypr | Biwi (FSA-Net) | 13219 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✖ |