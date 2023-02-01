import torch
from .calc_error import calc_error
import numpy as np
from tqdm import tqdm

def get_device():
    if torch.cuda.is_available():
        import torch.backends.cudnn as cudnn
        cudnn.enabled = True
        device = torch.device("cuda:0")
        torch.backends.cudnn.benchmark = True
    else:
        device = torch.device("cpu")
    return device

def eval_pytorch_model(model, model_output_format, dataset, denormalizer=None):

    device = get_device()
    model = model.to(device)
    model.eval()

    test_loader = torch.utils.data.DataLoader(
        dataset=dataset,
        batch_size=32,
        num_workers=4,
        drop_last=False)

    total = 0
    predictions = []
    gt = []

    with torch.no_grad():
        for data in tqdm(test_loader):

            labels = data[model_output_format]
            total += labels.size(0)
            images = data['img'].to(device)

            euler = model(images)
            if denormalizer is not None:
                euler = denormalizer(euler)

            predictions.append(euler.cpu().numpy())
            gt.append(labels)

    return calc_error(np.vstack(predictions), model_output_format, np.vstack(gt), model_output_format)
