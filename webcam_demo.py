# Demo: Eval RCRw model on webcam

import cv2 as cv
import torch
from demo.FaceDetector import FaceDetector
from hpp.RCR import get_RCR_image_transforms, load_model
from hpp.eval_pytorch import get_device
from hpp.utils import draw_pose_axis
import numpy as np

# Video input
cap = cv.VideoCapture(0) #
# or cap = cv.VideoCapture('my_file.avi')

# Face detector
face_detector = FaceDetector(force_cnn=0)
last_face = None
# Model
model = load_model('models/RCRw_from_SynheadPP_F.tar', 'models/RCRw_from_SynheadPP_T.tar')
img_transform = get_RCR_image_transforms()
device = get_device()
model = model.to(device)
print('Head Pose Detection is using device', device)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("no frame.")
        continue
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_out = img.copy()

    # find face
    faces = face_detector.get_faces(img)
    if len(faces) > 0:
        # draw on image
        face_detector.draw_bboxes_with_ocv_on_image(img_out, faces)
        # we only want to check the biggest
        last_face = face_detector.return_biggest_bbox(faces)
    else:
        if last_face: # draw the face found in one of the previous frames in red
            face_detector.draw_bboxes_with_ocv_on_image(img_out, [last_face], color=(255, 0, 0))

    if last_face is not None:
        crop = face_detector.crop(img, last_face)
        img_input = img_transform(crop)
        with torch.no_grad():
            img_input = img_input.unsqueeze(0).to(device)
            pose = np.squeeze(model(img_input).cpu().numpy())
        draw_pose_axis(img_out, pose, last_face)

    cv.imshow('Pose Estimation', cv.cvtColor(img_out, cv.COLOR_RGB2BGR))

    key = cv.waitKey(1)
    if key != -1:
        break

cap.release()