import os
import torch
from torchvision import models
from torchvision import transforms
import torch.nn as nn


def _ResNet18_mod():
    model = models.resnet18(pretrained=False)
    num_inputs_fc = model.fc.in_features
    model.fc = nn.Linear(num_inputs_fc, 3)
    model.features = nn.Sequential(model.conv1, model.bn1, model.relu, model.maxpool,
                                             model.layer1, model.layer2, model.layer3, model.layer4, model.avgpool)

    return model


def denormalize_batch_euler_(batch):
    # denormalizes a batch of euler samples
    # TODO use a class
    std = torch.Tensor([23.1782, 30.7491, 10.7432]).to(batch.device)
    mean = torch.Tensor([-4.0955, -2.4469, 0.7590]).to(batch.device)
    return batch.mul_(std).add_(mean)


def load_model(model_file_path):
    model = _ResNet18_mod()
    dict_name = 'state_dict'
    if os.path.isfile(model_file_path) is True:
        state = torch.load(model_file_path)
        if dict_name not in state:
            raise NameError('Can not find ' + dict_name + " in file")
        # clean some stuff
        rem = ['features_layer3.0.weight', 'features_layer3.1.weight', 'features_layer3.1.bias', 'features_layer3.1.running_mean', 'features_layer3.1.running_var', 'features_layer3.1.num_batches_tracked', 'features_layer3.4.0.conv1.weight', 'features_layer3.4.0.bn1.weight', 'features_layer3.4.0.bn1.bias', 'features_layer3.4.0.bn1.running_mean', 'features_layer3.4.0.bn1.running_var', 'features_layer3.4.0.bn1.num_batches_tracked', 'features_layer3.4.0.conv2.weight', 'features_layer3.4.0.bn2.weight', 'features_layer3.4.0.bn2.bias', 'features_layer3.4.0.bn2.running_mean', 'features_layer3.4.0.bn2.running_var', 'features_layer3.4.0.bn2.num_batches_tracked', 'features_layer3.4.1.conv1.weight', 'features_layer3.4.1.bn1.weight', 'features_layer3.4.1.bn1.bias', 'features_layer3.4.1.bn1.running_mean', 'features_layer3.4.1.bn1.running_var', 'features_layer3.4.1.bn1.num_batches_tracked', 'features_layer3.4.1.conv2.weight', 'features_layer3.4.1.bn2.weight', 'features_layer3.4.1.bn2.bias', 'features_layer3.4.1.bn2.running_mean', 'features_layer3.4.1.bn2.running_var', 'features_layer3.4.1.bn2.num_batches_tracked', 'features_layer3.5.0.conv1.weight', 'features_layer3.5.0.bn1.weight', 'features_layer3.5.0.bn1.bias', 'features_layer3.5.0.bn1.running_mean', 'features_layer3.5.0.bn1.running_var', 'features_layer3.5.0.bn1.num_batches_tracked', 'features_layer3.5.0.conv2.weight', 'features_layer3.5.0.bn2.weight', 'features_layer3.5.0.bn2.bias', 'features_layer3.5.0.bn2.running_mean', 'features_layer3.5.0.bn2.running_var', 'features_layer3.5.0.bn2.num_batches_tracked', 'features_layer3.5.0.downsample.0.weight', 'features_layer3.5.0.downsample.1.weight', 'features_layer3.5.0.downsample.1.bias', 'features_layer3.5.0.downsample.1.running_mean', 'features_layer3.5.0.downsample.1.running_var', 'features_layer3.5.0.downsample.1.num_batches_tracked', 'features_layer3.5.1.conv1.weight', 'features_layer3.5.1.bn1.weight', 'features_layer3.5.1.bn1.bias', 'features_layer3.5.1.bn1.running_mean', 'features_layer3.5.1.bn1.running_var', 'features_layer3.5.1.bn1.num_batches_tracked', 'features_layer3.5.1.conv2.weight', 'features_layer3.5.1.bn2.weight', 'features_layer3.5.1.bn2.bias', 'features_layer3.5.1.bn2.running_mean', 'features_layer3.5.1.bn2.running_var', 'features_layer3.5.1.bn2.num_batches_tracked', 'features_layer3.6.0.conv1.weight', 'features_layer3.6.0.bn1.weight', 'features_layer3.6.0.bn1.bias', 'features_layer3.6.0.bn1.running_mean', 'features_layer3.6.0.bn1.running_var', 'features_layer3.6.0.bn1.num_batches_tracked', 'features_layer3.6.0.conv2.weight', 'features_layer3.6.0.bn2.weight', 'features_layer3.6.0.bn2.bias', 'features_layer3.6.0.bn2.running_mean', 'features_layer3.6.0.bn2.running_var', 'features_layer3.6.0.bn2.num_batches_tracked', 'features_layer3.6.0.downsample.0.weight', 'features_layer3.6.0.downsample.1.weight', 'features_layer3.6.0.downsample.1.bias', 'features_layer3.6.0.downsample.1.running_mean', 'features_layer3.6.0.downsample.1.running_var', 'features_layer3.6.0.downsample.1.num_batches_tracked', 'features_layer3.6.1.conv1.weight', 'features_layer3.6.1.bn1.weight', 'features_layer3.6.1.bn1.bias', 'features_layer3.6.1.bn1.running_mean', 'features_layer3.6.1.bn1.running_var', 'features_layer3.6.1.bn1.num_batches_tracked', 'features_layer3.6.1.conv2.weight', 'features_layer3.6.1.bn2.weight', 'features_layer3.6.1.bn2.bias', 'features_layer3.6.1.bn2.running_mean', 'features_layer3.6.1.bn2.running_var', 'features_layer3.6.1.bn2.num_batches_tracked']
        for key in rem:
            if key in state[dict_name]:
                del state[dict_name][key]
        model.load_state_dict(state[dict_name], strict=True)

    return model


def get_PADACO_image_transforms():
    transformations_biwi = transforms.Compose(
        [transforms.Resize(224),
         transforms.ToTensor(),
         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    return transformations_biwi