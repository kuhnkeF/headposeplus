import dlib
import numpy as np
import cv2 as cv
from PIL import Image

class FaceDetector:

    def __init__(self, force_cnn=0, model_path='models/mmod_human_face_detector.dat'):
        self.model_path = model_path
        if dlib.DLIB_USE_CUDA or force_cnn == 1:
            print('Dlib CNN FaceDetector is using CUDA:', dlib.DLIB_USE_CUDA)
            self.detector = dlib.cnn_face_detection_model_v1(model_path)
            # you can use this on CPU but its too slow for webcam demo
        else:
            print('Dlib FaceDetector CUDA not available. Using lower precision cpu model.')
            self.detector = dlib.get_frontal_face_detector()


    @staticmethod
    def crop(img, box_xywh):
        img = Image.fromarray(img)
        x, y, w, h = box_xywh
        x, y, w, h = (int(x), int(y), int(w), int(h))
        x_min, y_min, x_max, y_max = x, y, x + w - 1, y + h - 1
        return img.crop((x_min, y_min, x_max, y_max))

    def get_faces(self, image_rgb):
        dets = self.detector(image_rgb, 0)
        faces = self.dlib_detection_to_faces(dets)
        return faces

    def draw_bboxes_with_ocv_on_image(self, img, faces, color=(0, 255, 0)):
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x - 1, y - 1), (x + w + 1, y + h + 1), color, 2)

    def dlib_detection_to_faces(self, dets):
        faces = []
        margin = 0.20
        for i, d in enumerate(dets):
            if isinstance(d, dlib.rectangle):
                face = d
            else:
                face = d.rect
            x = face.left()
            y = face.top()
            w = face.right()-face.left()+1
            h = round((face.bottom()-face.top()+1) * 1.18)

            if w > h:
                margin_x = round(w * margin)
                margin_y = round(((w + margin_x * 2) - h) / 2)
            else:  # w < h
                margin_y = round(h * margin)
                margin_x = round(((h + margin_y * 2) - w) / 2)

            x_m = int(round(x - margin_x))
            y_m = int(round(y - margin_y))
            w_m = int(round(w + margin_x * 2))
            #h_m = int(round(h + margin_y * 2))
            h_m = w_m
            faces.append([x_m, y_m, w_m, h_m])

        return faces

    def return_biggest_bbox(self, faces):
        biggest_face = faces[0]
        s_tmp = 0
        for face in faces:
            s = face[2]+face[3]
            if s > s_tmp:
                biggest_face = face
                s_tmp = s
        return biggest_face

