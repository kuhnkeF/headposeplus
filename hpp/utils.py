import numpy as np
import os
import cv2 as cv
from scipy.spatial.transform import Rotation

def load_dict_from_npz_file(file):
    if os.path.isfile(file) is False:
        raise NameError("ERROR: .npz file not found " + file)
    else:
        npz = np.load(file, allow_pickle=False)
    out = {}
    for key, value in npz.items():
        if value.dtype.type is np.str_:
            if value.size > 1:
                value = value.tolist()
            else:
                value = np.array_str(value)
        out[key] = value
    return out

def rint(x):
    return int(round(x))

def draw_pose_axis(img, pyr, bbox):
    x = bbox[0]
    y = bbox[1]
    size = bbox[2]/2
    ep, ey, er = pyr
    R = Rotation.from_euler('xyz', np.array([-ep, ey, -er]), degrees=True).as_matrix()
    x = rint(x+size)
    y = rint(y+size)
    # X-Axis red
    # Y-Axis green
    # Z-Axis blue
    cv.line(img, (x, y), (rint(x+R[0,0]*size), rint(y+R[1,0]*size)), (255, 0, 0), 4)
    cv.line(img, (x, y), (rint(x+R[0,1]*size), rint(y+R[1,1]*size)), (0, 255, 0), 4)
    cv.line(img, (x, y), (rint(x+R[0,2]*size), rint(y+R[1,2]*size)), (0, 0, 255), 4)
