import cv2
import numpy as np
import sys
sys.path.append('WHENet/')  # to fix WHENet code imports
from WHENet.whenet import WHENet


def load_model(model_path):
    model = WHENet(snapshot=model_path) # "WHENet/WHENet.h5"
    return model


def get_WHENet_image_transform():
    def whenet_img_transform(img):
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (224, 224))
        img = np.expand_dims(img, axis=0)
        return img

    return whenet_img_transform