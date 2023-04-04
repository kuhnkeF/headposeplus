# Webcam demo

https://user-images.githubusercontent.com/35331054/228528516-77e746af-2563-4a38-97b6-df08862cab52.mp4


## Setup

- Install Dlib and download face detection model (optional)
  
        conda activate hpp_pytorch
        pip install Dlib
  
- (optional step) You can use a better (CNN based) face detector
  - build Dlib with CUDA support (optional, but otherwise very slow)
  - Download face detection model from https://github.com/davisking/dlib-models
    - you need to download and extract https://github.com/davisking/dlib-models/blob/master/mmod_human_face_detector.dat.bz2
      to the models folder
    - if you did not build Dlib with CUDA support you need to change force_cnn=1 in  webcam_demo.py 
  
- run demo from main folder
        
        conda activate hpp_pytorch
        python webcam_demo.py

## Notes
 - Dlib is not good at detecting non-frontal faces. Using another face detector will give better results.
