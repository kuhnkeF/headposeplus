# Results on Biwi+

|  Method | MAE | Pitch | Yaw | Roll | Format | Test Set | Num Images | Training Set | Crop | Unsup. Training on Test Set | Calibrated Biwi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  WHENet | 7.25 | 8.00 | 8.05 | 5.72 | pyr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  FSA-Net | 5.75 | 6.43 | 6.27 | 4.55 | pyr | Biwi+ | 15678 | 300W_LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  Hopenet | 5.73 | 7.65 | 5.32 | 4.21 | pyr | Biwi+ | 15678 | 300W_LP | Biwi+ -> Dockerface, Hopenet | ✖ | ✔ |
|  **6DRepNet** |  **4.39** |  **5.19** |  4.62 |  3.37 | pyr | Biwi+ |  15678 | 300W-LP | Biwi+ (DLIB+manual) | ✖ | ✔ |
|  RCRw | 4.55 | 6.34 | **4.55** | **2.74** | pyr | Biwi+ | 15678 | 300W-LP | Biwi+ (DLIB+manual) | ✔ | ✔ |
| | | | | | | | | | | | |
|  PADACO | 4.13 | **4.51** | 4.11 | 3.78 | pyr | Biwi+ | 15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✔ |
|  **RCRw** | **3.86** | 4.73 | **3.95** | **2.89** | pyr | Biwi+ | 15678 | SynHead++ | Biwi+ (DLIB+manual) | ✔ | ✔ |