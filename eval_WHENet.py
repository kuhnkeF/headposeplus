# use WHENet to evaluate on Biwi variants
# this uses the Tensorflow environment
# check create_tensorflow_env.sh

from hpp.WHENet import load_model, get_WHENet_image_transform
from hpp import Table, BiwiDataset
from hpp.eval_whenet import eval_whenet_model

# paths
result_path = 'results/WHENet/'
# FSANet uses three models and averages the results (ensemble)
model_path = 'WHENet/WHENet.h5'

# settings
method_name = 'WHENet'
training_set = '300W_LP'
transformations = get_WHENet_image_transform()
model_output_format = 'ypr' # model will output ypr labels
#model_pred_transform = None # WHENet outputs Euler angles in degree

variants = [
            ('WHENet', {}),
            ('WHENet', {'bbox_transform': 'Biwi+'}),
            ('WHENet', {'bbox_transform': 'Biwi+->YOLOv3'}),
            ('Biwi+_non_cal', {'bbox_transform': 'Biwi+->YOLOv3'}),
            ('Biwi+_non_cal', {}),
            ('Biwi+', {'bbox_transform': 'Biwi+->YOLOv3'}),
            ('Biwi+', {}),
            ('FSA-Net', {}),
            ('FSA-Net', {'bbox_transform': 'Biwi+'}),
            ('FSA-Net', {'bbox_transform': 'Biwi+->YOLOv3'})
            ]
# variants to evaluate
report_formats = ['pyr', 'ypr']


table = Table(['Method', 'MAE', 'Pitch', 'Yaw', 'Roll', 'Format', 'Test Set', 'Num Images', 'Training Set', 'Crop', 'Unsup. Training on Test Set', 'Calibrated Biwi'])
fixed_infos = {'Method': method_name, 'Training Set': training_set, 'Unsup. Training on Test Set': Table.no()}

# Reported results from the Paper
res = {'Method': 'WHENet (paper)', 'MAE': 3.81, 'Pitch': 4.39, 'Yaw': 3.99, 'Roll': 3.06, 'Test Set': 'Biwi'}
table.add(res)
table.add_horizontal_line()

# eval loop
for variant, kwargs in variants:

    dataset = BiwiDataset(variant=variant, transforms=transformations, **kwargs)
    err = eval_whenet_model(load_model(model_path), model_output_format, dataset)

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