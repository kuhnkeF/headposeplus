# bbox transformations

# the conversion will not only include the face detector bbox, but also the postprocessing of the method
# (e.g. adding a margin to original detections, e.g., Biwi+ uses margins of ~20%)

# transformation uses a simple shift (pixels) and scale (percent) of the original box
# however, as shifting by pixels is not invariant to image/box size, we first determine the box size
# to choose from a list of possible transformations (=add_scale_mean)
# -add_scale_mean and bin_edges was computed from the boxes found by the detectors + method post processing


import numpy as np

def _box_scale_xywh(xywh):
    return np.sqrt(xywh[2]**2+xywh[3]**2)

def _box_apply_xywh_pixel_add_scale(xywh, add_scale):
    xy = xywh[0:2] + add_scale[0:2]
    wh = xywh[2:4] * add_scale[2:4]
    return np.asarray([xy[0], xy[1], wh[0], wh[1]])

def _transform_boxes(boxes, add_scale, bins):
    new_boxes = np.zeros(boxes.shape)
    for i, box in enumerate(boxes):
        box[2] = box[2] - 1
        box[3] = box[3] - 1
        scale = _box_scale_xywh(box)
        for bin_id in range(len(bins) - 1):  # first one is not needed
            if scale < bins[bin_id + 1]:
                new_boxes[i] = _box_apply_xywh_pixel_add_scale(box, add_scale[bin_id])
                break
    return new_boxes

def transform_to_MTCNN_FSANet(biwiplus_bboxes):
    bin_edges = [0., 175.36248173, 185.26197667, 189.50461736, 220.61731573, 267.28636329, 999.]
    add_scale_mean = [np.asarray([-4.25, -8.,  0.94533548,  1.13440258]),
                      np.asarray([-5.33333333, -7.33333333,  0.80436552,  1.02775292]),
                      np.asarray([3.84469987, -21.348659,   0.9567313,   1.22674583]),
                      np.asarray([6.82067248, -24.5765878,   0.93728201,   1.21181858]),
                      np.asarray([6.60401189, -23.43808816,   0.93433694,   1.21281797]),
                      np.asarray([17.97407407, -20.54814815,   0.85944542,   1.12404468])]

    return _transform_boxes(biwiplus_bboxes, add_scale_mean, bin_edges)

def transform_to_Dockerface_Hopenet(biwiplus_bboxes):
    bin_edges = [130., 150., 170., 190., 220., 999.]
    add_scale_mean = [np.asarray([11.82026786, 1.20267857, 0.82874542, 0.82874542]),
                      np.asarray([18.21395391, 3.76094957, 0.7473356, 0.7473356]),
                      np.asarray([18.84964794, 2.99583283, 0.78673647, 0.78673647]),
                      np.asarray([24.68544601, 3.89646735, 0.76937699, 0.76937699]),
                      np.asarray([25.18093421, 5.47032309, 0.76385549, 0.76385549])]

    return _transform_boxes(biwiplus_bboxes, add_scale_mean, bin_edges)

def transform_to_YOLOv3_WHENet(biwiplus_bboxes):
    bin_edges = [0, 149.90663761, 165.4629868, 175.36248173, 185.26197667, 189.50461736, 220.61731573, 267.28636329, 999]
    add_scale_mean = [np.asarray([-0.8,  7.,  1.09381099,  1.08786006]),
                      np.asarray([1.125, 6.825, 1.07122652, 1.04251575]),
                      np.asarray([1.0483871, 6.48387097, 1.06651621, 0.98710734]),
                      np.asarray([0.78947368, 5.18421053, 1.05087768, 0.94138944]),
                      np.asarray([-0.58639934, -23.05766846,   1.12337523,   1.14646623]),
                      np.asarray([0.08343126, -29.65452409,   1.07643559,   1.12654346]),
                      np.asarray([0.2690818, -31.70175439, 1.078591,   1.13337394]),
                      np.asarray([10.43649374, -31.96064401, 0.99616662,   1.05441501])]

    return _transform_boxes(biwiplus_bboxes, add_scale_mean, bin_edges)


def box_ltrb2xywh(ltrb):
    x_min, y_min, x_max, y_max = ltrb
    return x_min, y_min, x_max-x_min+1, y_max-y_min+1

def hopenet_box_processing(bboxes):
    new_bboxes = np.zeros(bboxes.shape)
    for i, box in enumerate(bboxes):
        x_min, y_min, x_max, y_max = (box[0], box[1], box[0]+box[2]-1, box[1]+box[3]-1)

        # found in the BIWI dataset class from Ruiz et al.
        # https://github.com/natanielruiz/deep-head-pose/blob/master/code/datasets.py
        # so it should be used for dockerface biwi detections
        # Loosely crop face
        k = 0.35
        x_min -= 0.6 * k * abs(x_max - x_min)
        y_min -= k * abs(y_max - y_min)
        x_max += 0.6 * k * abs(x_max - x_min)
        y_max += 0.6 * k * abs(y_max - y_min)
        x_min, y_min, x_max, y_max = np.asarray([int(x_min), int(y_min), int(x_max), int(y_max)])

        new_bboxes[i] = np.asarray([x_min, y_min, x_max-x_min+1, y_max-y_min+1])

    return new_bboxes