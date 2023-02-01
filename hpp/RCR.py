# to reproduce results from RCRw model from TBIOM journal
import os
import torch
from torchvision import models
from torchvision import transforms
import torch.nn as nn


class Dummy(nn.Module):
    def __init__(self):
        super(Dummy, self).__init__()

    def forward(self, input):
        return input


class FCNet(nn.Module):

    def __init__(self, input_layer_size=512, output_size=3):
        super(FCNet, self).__init__()
        self.layers = nn.Sequential()
        last_layer_size = input_layer_size
        self.layers.add_module('LastLinear',  nn.Linear(last_layer_size, output_size, bias=True))

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.layers(x)
        return x


def load_model(path_f, path_t):
    model = nn.Sequential()
    model_f = models.resnet18(pretrained=False)
    model_f.fc = Dummy()
    model_t = FCNet()
    model_f = _load_model(model_f, path_f).eval()
    model_t = _load_model(model_t, path_t).eval()
    model.add_module('F', model_f)
    model.add_module('T', model_t)
    return model


def _load_model(model, path):
    if os.path.isfile(path):
        state = torch.load(path)
        t = model.load_state_dict(state['state_dict'], strict=True)
    else:
        raise NameError('can not load '+ path)
    return model


def get_RCR_image_transforms():
    transformations_biwi = transforms.Compose(
        [transforms.Resize(224), #RescaleSquareImage(224),
         transforms.ToTensor(),
         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    return transformations_biwi

