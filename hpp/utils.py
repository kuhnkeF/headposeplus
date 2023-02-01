import numpy as np
import os


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
