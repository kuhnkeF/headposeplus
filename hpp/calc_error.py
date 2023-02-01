# calculate Euler angle errors for different sequences of rotation axes
# https://github.com/kuhnkeF/headposeplus
import numpy as np
from scipy.spatial.transform import Rotation

def _convert(nx3:np.ndarray, conv_fun):
    converted = []
    for rep in nx3:
        con = conv_fun(rep)
        converted.append(con)
    converted = np.stack(converted, axis=0)
    return converted

def _ypr2pyr(ypr):
    y,p,r = -ypr
    r = Rotation.from_euler('zyx', np.asarray([r, y, p]), degrees=True)
    p, y, r = r.as_euler('xyz', degrees=True)
    return np.asarray([p, y, r])

def _pyr2ypr(pyr):
    r = Rotation.from_euler('xyz', pyr, degrees=True)
    r, y, p = r.as_euler('zyx', degrees=True)
    return -np.asarray([y, p, r])

def _all_formats(arr:np.ndarray, format):
    out = {}
    if format == 'ypr':
        out[format] = arr
        out["pyr"] = _convert(arr, _ypr2pyr)
        #test = _convert(out["pyr"], _pyr2ypr)
    elif format == 'pyr':
        out[format] = arr
        out['ypr'] = _convert(arr, _pyr2ypr)
        #test = _convert(out["yrp"], _ypr2pyr)
    else:
        raise NameError('unknown input format', format)

    return out

def _calc_errors(arr:np.ndarray, gt_arr:np.ndarray, format):
    errs = np.mean(np.abs(arr - gt_arr), axis=0)
    MAE = np.mean(errs)
    if format == 'pyr':
        pitch = errs[0]
        yaw = errs[1]
        roll = errs[2]
    elif format == 'ypr':
        yaw = errs[0]
        pitch = errs[1]
        roll = errs[2]
    else:
        raise NameError('unknown format', format)
    return {'MAE': MAE, 'Pitch': pitch, 'Yaw': yaw, 'Roll': roll}

def calc_error(nx3:np.ndarray, input_format, ground_truth:np.ndarray, gt_format):
    # input is a n x 3 matrix
    # calculate the pyr and the ypr error
    # The format names (pyr, ypr) are not conclusive. They are only given to distinguish the different methods.
    # pyr is our R to pitch yaw roll conversion, similar to the format found in the Biwi files
    # ypr is the conversion used in Hopenet, FSA-Net,...
    # others are possible...

    out = {}
    gt = _all_formats(ground_truth, gt_format)
    prediction = _all_formats(nx3, input_format)

    for format in ['pyr', 'ypr']:
        out[format] = _calc_errors(prediction[format], gt[format], format)

    return out