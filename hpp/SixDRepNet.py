import torch
from torchvision import transforms
import numpy as np
from SixDRepNet.model import SixDRepNet
from SixDRepNet.utils import compute_euler_angles_from_rotation_matrices


def _load_filtered_state_dict(model, snapshot):
    model_dict = model.state_dict()
    snapshot = {k: v for k, v in snapshot.items() if k in model_dict}
    model_dict.update(snapshot)
    model.load_state_dict(model_dict)


def load_model(model_path):
    model = SixDRepNet(backbone_name='RepVGG-B1g2',
                       backbone_file='',
                       deploy=True,
                       pretrained=False)

    saved_state_dict = torch.load(model_path, map_location='cpu')

    if 'model_state_dict' in saved_state_dict:
        model.load_state_dict(saved_state_dict['model_state_dict'])
    else:
        model.load_state_dict(saved_state_dict)

    return model


def get_SixDRepNet_Image_Transforms():
    transformations = transforms.Compose([transforms.Resize(256),
                                          transforms.CenterCrop(224),
                                          transforms.ToTensor(),
                                          transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                               std=[0.229, 0.224, 0.225])])
    return transformations


def SixDRepNet_predictions_to_ypr_eulers(R_pred):
    pyr_but_like_ypr = compute_euler_angles_from_rotation_matrices(R_pred) * 180 / np.pi
    # convert to ypr
    return pyr_but_like_ypr[:, [1, 0, 2]]
