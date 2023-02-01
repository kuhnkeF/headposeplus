# use Hopenet to evaluate on Biwi variants

from hpp.Hopenet import load_model, hopenet_pred_to_ypr, get_Hopenet_image_transforms_center_crop, get_Hopenet_image_transforms_no_crop
from hpp import Table, BiwiDataset
from hpp.eval_pytorch import eval_pytorch_model

# paths
result_path = 'results/Hopenet/'
model_path = 'models/hopenet_alpha1.pkl'

# settings
method_name = 'Hopenet'
training_set = '300W_LP'
#transformations = different augs to avoid some problems with non-square bboxes
model_output_format = 'ypr' # model will output ypr labels
model_pred_transform = hopenet_pred_to_ypr # use this to normalize the model output to Euler angles in degree

variants = [
            ('Hopenet', {'transforms': get_Hopenet_image_transforms_center_crop()}),
            ('Biwi+', {'transforms': get_Hopenet_image_transforms_no_crop()}),
            ('Biwi+', {'bbox_transform': 'Biwi+->Dockerface',
                       'transforms': get_Hopenet_image_transforms_center_crop()}),
            ('Biwi+_non_cal', {'transforms': get_Hopenet_image_transforms_no_crop()}),
            ('Biwi+_non_cal', {'bbox_transform': 'Biwi+->Dockerface',
                               'transforms': get_Hopenet_image_transforms_center_crop()}),
            ('FSA-Net', {'transforms': get_Hopenet_image_transforms_center_crop()}),
            ('FSA-Net', {'bbox_transform': 'Biwi+',
                         'transforms': get_Hopenet_image_transforms_no_crop()}),
            ('FSA-Net', {'bbox_transform': 'Biwi+->Dockerface',
                         'transforms': get_Hopenet_image_transforms_center_crop()})
            ]
# variants to evaluate
report_formats = ['pyr', 'ypr']
# kwargs = bbox_transform=None


table = Table(['Method', 'MAE', 'Pitch', 'Yaw', 'Roll', 'Format', 'Test Set', 'Num Images', 'Training Set', 'Crop', 'Unsup. Training on Test Set', 'Calibrated Biwi'])
fixed_infos = {'Method': method_name, 'Training Set': training_set, 'Unsup. Training on Test Set': Table.no()}

# Reported results from the Paper
res = {'Method': 'Hopenet (paper)', 'MAE': 4.895, 'Pitch': 6.606, 'Yaw': 4.810, 'Roll': 3.269, 'Test Set': 'Biwi'}
table.add(res)
table.add_horizontal_line()

# eval loop
for variant, kwargs in variants:

    dataset = BiwiDataset(variant=variant, **kwargs)
    err = eval_pytorch_model(load_model(model_path), model_output_format, dataset, model_pred_transform)

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