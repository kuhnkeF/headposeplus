from .calc_error import calc_error
from tqdm import tqdm
import numpy as np

def eval_whenet_model(model, model_output_format, dataset):
    if model_output_format == 'pyr':
        raise NameError('WHENet output is ypr')

    preds = []
    gt = []

    for data in tqdm(dataset):
        out = model.get_angle(data['img'])
        gt.append(data[model_output_format])
        preds.append(np.array(out))

    return calc_error(np.array(preds).squeeze(), model_output_format, np.array(gt), model_output_format)


