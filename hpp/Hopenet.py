import torch
import torchvision
from torchvision import transforms
from Hopenet.code.hopenet import Hopenet
#from Hopenet.code.utils import softmax_temperature


def softmax_temperature(tensor, temperature):
    result = torch.exp(tensor / temperature)
    result = torch.div(result, torch.sum(result, 1).unsqueeze(1).expand_as(result))
    return result


def load_model(model_path):
    model = Hopenet(torchvision.models.resnet.Bottleneck, [3, 4, 6, 3], 66)
    saved_state_dict = torch.load(model_path)
    model.load_state_dict(saved_state_dict)
    return model


def get_Hopenet_image_transforms_center_crop():
    # similar to original code
    transformations = transforms.Compose([transforms.Resize(224),
                      transforms.CenterCrop(224),
                      transforms.ToTensor(),
                      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    return transformations


def get_Hopenet_image_transforms_no_crop():
    transformations = transforms.Compose([transforms.Resize(224),
                      #transforms.CenterCrop(224), # center crop is not needed if boxes are square
                      # if image is square this should not have an effect but collate fun will throw an error if not
                      transforms.ToTensor(),
                      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    return transformations


def hopenet_pred_to_ypr(preds):
    yaw, pitch, roll = preds

    # Binned predictions
    _, yaw_bpred = torch.max(yaw.data, 1)
    _, pitch_bpred = torch.max(pitch.data, 1)
    _, roll_bpred = torch.max(roll.data, 1)

    # Continuous predictions
    yaw_predicted = softmax_temperature(yaw.data, 1)
    pitch_predicted = softmax_temperature(pitch.data, 1)
    roll_predicted = softmax_temperature(roll.data, 1)

    idx_tensor = [idx for idx in range(66)]
    idx_tensor = torch.FloatTensor(idx_tensor).to(yaw.device)

    yaw_predicted = torch.sum(yaw_predicted * idx_tensor, 1).cpu() * 3 - 99
    pitch_predicted = torch.sum(pitch_predicted * idx_tensor, 1).cpu() * 3 - 99
    roll_predicted = torch.sum(roll_predicted * idx_tensor, 1).cpu() * 3 - 99

    return torch.stack([yaw_predicted, pitch_predicted, roll_predicted], dim=1)