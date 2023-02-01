# Biwi variant dataset
# includes Biwi+ Dataset as proposed in
# "Deep head pose estimation using synthetic images and partial adversarial domain adaption for continuous label spaces"
# extension of the original Biwi Kinect Head Pose Database by Fanelli et al.
# "Random Forests for Real Time 3D Face Analysis"
# https://github.com/kuhnkeF/headposeplus

# ---> Change to your path
path_biwi = "/data/face/BiwiKinectHeadPose/tmp/kinect_head_pose_db/"
# size of kinect_head_pose_db 7,1 GiB


import pickle
import os
from PIL import Image
import numpy as np
from tqdm import tqdm
from .bbox import transform_to_Dockerface_Hopenet, transform_to_MTCNN_FSANet, transform_to_YOLOv3_WHENet,\
    hopenet_box_processing
from .utils import load_dict_from_npz_file


class BiwiDataset():

    def __init__(self, transforms=None, variant='Biwi+', bbox_transform=None):
        if not os.path.isdir(path_biwi):
            raise NameError('Please set path_biwi')
        self.root = path_biwi
        # check if root dir has a slash at the end, only works on linux
        if self.root.endswith('/') == False:
            self.root = self.root + '/'

        self.transforms = transforms
        self.bbox_transform = bbox_transform

        # choose npz file based on Biwi variant
        if variant not in ['Biwi+', 'Biwi+_non_cal', 'FSA-Net', 'WHENet', 'Hopenet']:
            raise NameError('unknown Biwi variant', variant)

        if variant == 'Biwi+':
            self.name = 'Biwi+'
            self.calibrated = True
            npz_file = os.path.join('data', 'Biwi_plus.npz')
            d = load_dict_from_npz_file(npz_file)
            self.images = d['images']
            self.pyr = d['pyr']
            self.ypr = d['ypr']
            self.Rs = None
            self.biwi_plus_box_selection(bbox_transform, d)
        elif variant == 'Biwi+_non_cal':  # use non calibrated labels
            self.name = 'Biwi+ (non cal)'
            self.calibrated = False
            npz_file = os.path.join('data', 'Biwi_plus_non_cal.npz')
            d = load_dict_from_npz_file(npz_file)
            self.images = d['images']
            self.pyr = d['pyr']
            self.ypr = d['ypr']
            self.Rs = None
            self.biwi_plus_box_selection(bbox_transform, d)
        elif variant == 'FSA-Net':  # aka MTCNN subset
            self.name = 'Biwi (FSA-Net)'
            self.calibrated = False
            npz_file = os.path.join('data', 'Biwi_FSA-Net.npz')
            d = load_dict_from_npz_file(npz_file)
            self.images = d['images']
            self.pyr = d['pyr']
            self.ypr = d['ypr']
            self.Rs = None
            self.bbox_crop = self.xywh_pil_crop
            if bbox_transform == 'Biwi+':
                self.bbox = d['bbox_from_BiwiPlus']
                self.bbox_name = 'Biwi+ (DLIB+manual)'
            elif bbox_transform == 'Biwi+->MTCNN':
                self.bbox = transform_to_MTCNN_FSANet(d['bbox_from_BiwiPlus'])
                self.bbox_name = 'Biwi+ -> MTCNN, FSA-Net'
            elif bbox_transform == 'Biwi+->Dockerface':
                self.bbox = transform_to_Dockerface_Hopenet(d['bbox_from_BiwiPlus'])
                self.bbox_name = 'Biwi+ -> Dockerface, Hopenet'
            elif bbox_transform == 'Biwi+->YOLOv3':
                self.bbox = transform_to_YOLOv3_WHENet(d['bbox_from_BiwiPlus'])
                self.bbox_name = 'Biwi+ -> YOLOv3, WHENet'
            elif bbox_transform is None:  # default MTCNN with FSA-Net post processing
                self.bbox = d['bbox']
                self.bbox_name = 'MTCNN, cleaned, FSA-Net'
            else:
                raise NameError('unknown bbox_transform for FSA-Net variant', bbox_transform)
        elif variant == 'WHENet':  # aka YOLOv3 subset
            self.name = 'Biwi (WHENet)'
            self.calibrated = False
            npz_file = os.path.join('data', 'Biwi_WHENet.npz')
            d = load_dict_from_npz_file(npz_file)
            self.images = d['images']
            self.pyr = d['pyr']
            self.ypr = d['ypr']
            self.Rs = None
            self.bbox_crop = self.xywh_pil_crop
            if bbox_transform == 'Biwi+':
                self.bbox = d['bbox_from_BiwiPlus']
                self.bbox_name = 'Biwi+ (DLIB+manual)'
            elif bbox_transform == 'Biwi+->YOLOv3':
                self.bbox = transform_to_YOLOv3_WHENet(d['bbox_from_BiwiPlus'])
                self.bbox_name = 'Biwi+ -> YOLOv3, WHENet'
            elif bbox_transform is None:  # default: YOLOv3, cleaned, with WHENet post processing
                self.bbox = d['bbox']
                self.bbox_name = 'YOLOv3, cleaned, WHENet'
            else:
                raise NameError('unknown bbox_transform for WHENet variant', bbox_transform)
        elif variant == 'Hopenet':
            # Use only for Hopenet because this has only bboxes that match Hopenet processing
            self.name = 'Biwi (Hopenet)'
            self.calibrated = False
            npz_file = os.path.join('data', 'Biwi_Dockerface.npz')
            d = load_dict_from_npz_file(npz_file)
            self.images = d['images']
            self.pyr = d['pyr']
            self.ypr = d['ypr']
            self.Rs = None
            if bbox_transform is None:  # default dockerface (cleaned)
                # xywh dockerface boxes
                bbox = d['bbox']
                # dockerface Hopenet post processing
                self.bbox = hopenet_box_processing(bbox)
                self.bbox_crop = self.xywh_pil_crop
                self.bbox_name = 'Dockerface, cleaned, Hopenet'  # results of Dockerface were corrected manually
            elif bbox_transform == 'Biwi+':
                self.bbox = d['bbox_from_BiwiPlus']
                self.bbox_name = 'Biwi+ (DLIB+manual)'
            else:
                raise NameError('unknown bbox_transform for Biwi (Hopenet/Dockerface) variant', bbox_transform)

    def biwi_plus_box_selection(self, bbox_transform, d):
        if bbox_transform == 'Biwi+->MTCNN':
            self.bbox = transform_to_MTCNN_FSANet(d['bbox'])
            self.bbox_name = 'Biwi+ -> MTCNN, FSA-Net'

        elif bbox_transform == 'Biwi+->Dockerface':
            self.bbox = transform_to_Dockerface_Hopenet(d['bbox'])
            self.bbox_name = 'Biwi+ -> Dockerface, Hopenet'

        elif bbox_transform == 'Biwi+->YOLOv3':
            self.bbox = transform_to_YOLOv3_WHENet(d['bbox'])
            self.bbox_name = 'Biwi+ -> YOLOv3, WHENet'

        elif bbox_transform is None:  # default based on manual labels and dlib cnn face detector +20% margin
            self.bbox = d['bbox']
            self.bbox_name = 'Biwi+ (DLIB+manual)'
        else:
            raise NameError('unknown bbox_transform for BiwiPlus dataset', bbox_transform)
        self.bbox_crop = self.xywh_pil_crop

    def get_name(self):
        return self.name

    def is_calibrated(self):
        return self.calibrated

    def get_crop(self):
        return self.bbox_name

    @staticmethod
    def xywh_pil_crop(img, box_xywh):
        x, y, w, h = box_xywh
        x, y, w, h = (int(x), int(y), int(w), int(h))
        x_min, y_min, x_max, y_max = x, y, x + w - 1, y + h - 1
        img = img.crop((x_min, y_min, x_max, y_max))  # crops x_min to x_max-1
        return img

    @staticmethod
    def xywh_ocv_crop(img, box_xywh):  # same result as xywh_pil_crop
        x, y, w, h = box_xywh
        x, y, w, h = (int(x), int(y), int(w), int(h))
        img = np.array(img)
        img = img[y:y+h, x:x+w, :]
        return Image.fromarray(img)

    @staticmethod
    def x1y1x2y2_pil_crop_direct(img, box_x1y1x2y2):
        x_min, y_min, x_max, y_max = box_x1y1x2y2
        img = img.crop((int(x_min), int(y_min), int(x_max), int(y_max)))
        return img

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        data = {}
        if self.pyr is not None:
            data['pyr'] = self.pyr[index]
        if self.ypr is not None:
            data['ypr'] = self.ypr[index]
        if self.Rs is not None:
            data['R'] = self.Rs[index]

        img_path = os.path.join(self.root, self.images[index])
        img = Image.open(img_path)
        img = img.convert('RGB')
        data['img'] = img
        bbox = self.bbox[index]
        img = self.bbox_crop(img, bbox)

        if self.transforms is not None:
            img = self.transforms(img)
        data['img'] = img

        return data

    def get_all_items(self, saveload=False):
        # 64x64 Biwi files are only about 150 mb
        if saveload:  # store to disk and load if available
            # Warning: this will also store the image transforms, -> might cause errors/wrong results
            if self.bbox_transform is not None:
                path = 'data/' + self.name.replace(' ', '_') + '_' + self.bbox_transform.replace(' ', '_') + '.pkl'
            else:
                path = 'data/' + self.name.replace(' ', '_') + '.pkl'
            print(path)
            if os.path.isfile(path):
                with open(path, 'rb') as file:
                    images, pyr, ypr = pickle.load(file)
                return images, pyr, ypr
        # used for fsa eval
        images = []
        labels_pyr = []
        labels_ypr = []
        print('loading complete dataset', self.get_name())
        for data in tqdm(self):
            images.append(np.array(data['img']))
            labels_pyr.append(data['pyr'])
            labels_ypr.append(data['ypr'])
        if saveload:
            with open(path, "wb") as output_file:
                pickle.dump([np.array(images), np.array(labels_pyr), np.array(labels_ypr)], output_file)
        return np.array(images), np.array(labels_pyr), np.array(labels_ypr)





