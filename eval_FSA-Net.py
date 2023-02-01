# use FSA-Net to evaluate on Biwi variants
# this uses the Tensorflow environment
# check create_tensorflow_env.sh

from hpp.FSANet import load_model, get_FSANet_image_transform
from hpp import Table, BiwiDataset
from hpp.eval_fsa import eval_fsa_model

# paths
result_path = 'results/FSA-Net/'
# FSANet uses three models and averages the results (ensemble)
model_path1 = 'FSANet/pre-trained/300W_LP_models/fsanet_capsule_3_16_2_21_5/fsanet_capsule_3_16_2_21_5.h5'
model_path2 = 'FSANet/pre-trained/300W_LP_models/fsanet_var_capsule_3_16_2_21_5/fsanet_var_capsule_3_16_2_21_5.h5'
model_path3 = 'FSANet/pre-trained/300W_LP_models/fsanet_noS_capsule_3_16_2_192_5/fsanet_noS_capsule_3_16_2_192_5.h5'
model_paths = (model_path1, model_path2, model_path3)

# settings
method_name = 'FSA-Net'
training_set = '300W_LP'
transformations = get_FSANet_image_transform()
model_output_format = 'ypr' # model will output ypr labels
#model_pred_transform = None # fsa outputs Euler angles in degree


variants = [
            ('FSA-Net', {}),
            ('FSA-Net', {'bbox_transform': 'Biwi+'}),
            ('FSA-Net', {'bbox_transform': 'Biwi+->MTCNN'}),
            ('Biwi+_non_cal', {'bbox_transform': 'Biwi+->MTCNN'}),
            ('Biwi+_non_cal', {}),
            ('Biwi+', {'bbox_transform': 'Biwi+->MTCNN'}),
            ('Biwi+', {}),
            ]
# variants to evaluate
report_formats = ['pyr', 'ypr']


table = Table(['Method', 'MAE', 'Pitch', 'Yaw', 'Roll', 'Format', 'Test Set', 'Num Images', 'Training Set', 'Crop', 'Unsup. Training on Test Set', 'Calibrated Biwi'])
fixed_infos = {'Method': method_name, 'Training Set': training_set, 'Unsup. Training on Test Set': Table.no()}

# Reported results from the Paper
res = {'Method': 'FSA-Net (paper)', 'MAE': 4.00, 'Pitch': 4.96, 'Yaw': 4.27, 'Roll': 2.76, 'Test Set': 'Biwi'}
table.add(res)
table.add_horizontal_line()

# eval loop
for variant, kwargs in variants:

    dataset = BiwiDataset(variant=variant, transforms=transformations, **kwargs)
    err = eval_fsa_model(model_paths, model_output_format, dataset)

    for format in report_formats:
        res = {'Test Set': dataset.get_name(), 'Num Images': len(dataset), 'Format': format,
               'Calibrated Biwi': Table.bool(dataset.is_calibrated()), 'Crop': dataset.get_crop()}
        res.update(fixed_infos)
        res.update(err[format])
        table.add(res)

        print('Error on ' + dataset.get_name() + ': (' + str(len(dataset)) + ' images)')
        print(format + ' MAE: %.4f, pitch: %.4f, yaw: %.4f, roll: %.4f' % (err[format]['MAE'], err[format]['Pitch'], err[format]['Yaw'], err[format]['Roll']))

###
table.render()
table.write_file(result_path)
###