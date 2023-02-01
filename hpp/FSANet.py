import cv2

from FSANet.lib.FSANET_model import *
from FSANet.lib.SSRNET_model import *

_IMAGE_SIZE = 64

# model names
# 'FSANet/pre-trained/300W_LP_models/fsanet_capsule_3_16_2_21_5/fsanet_capsule_3_16_2_21_5.h5'
# 'FSANet/pre-trained/300W_LP_models/fsanet_var_capsule_3_16_2_21_5'/fsanet_var_capsule_3_16_2_21_5.h5'
# 'FSANet/pre-trained/300W_LP_models/fsanet_noS_capsule_3_16_2_192_5/fsanet_noS_capsule_3_16_2_192_5.h5'


def load_model(model_path1, model_path2, model_path3):
    # check out https://github.com/shamangary/FSA-Net/blob/master/training_and_testing/FSANET_test.py for more info
    # model_type == 15: # fusion_dim_split_capsule

    S_set = [3, 16, 2, 7 * 3, 5]
    str_S_set = ''.join('_' + str(x) for x in S_set)  # _3_16_2_21_5
    #save_name1 = 'fsanet_capsule' + str_S_set
    model1 = FSA_net_Capsule(_IMAGE_SIZE, 3, [3,3,3], 1, S_set)()

    S_set = [3, 16, 2, 7 * 3, 5]
    str_S_set = ''.join('_' + str(x) for x in S_set)  # _3_16_2_21_5
    #save_name2 = 'fsanet_var_capsule' + str_S_set
    model2 = FSA_net_Var_Capsule(_IMAGE_SIZE, 3, [3,3,3], 1, S_set)()

    S_set = [3, 16, 2, 8 * 8 * 3, 5]
    str_S_set = ''.join('_' + str(x) for x in S_set)  # _3_16_2_192_5
    #save_name3 = 'fsanet_noS_capsule' + str_S_set
    model3 = FSA_net_noS_Capsule(_IMAGE_SIZE, 3, [3,3,3], 1, S_set)()

    try:
        model1.load_weights(model_path1)
        model2.load_weights(model_path2)
        model3.load_weights(model_path3)
    except:
        raise NameError('can not load FSA models, check paths',)

    inputs = Input(shape=(64, 64, 3))
    x1 = model1(inputs)
    x2 = model2(inputs)
    x3 = model3(inputs)
    outputs = Average()([x1, x2, x3])
    model = Model(inputs=inputs, outputs=outputs)
    return model


def get_FSANet_image_transform():
    def fsa_img_transform(img):
        img = cv2.resize(np.array(img), (_IMAGE_SIZE, _IMAGE_SIZE))
        # we load everything in RGB, but FSA net assumes ocv BGR order
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return fsa_img_transform