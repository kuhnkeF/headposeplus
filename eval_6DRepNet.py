# use 6DRepNet to evaluate on Biwi variants

from hpp.SixDRepNet import load_model, get_SixDRepNet_Image_Transforms, SixDRepNet_predictions_to_ypr_eulers
from hpp import Table, BiwiDataset
from hpp.eval_pytorch import eval_pytorch_model

# paths
result_path = 'results/6DRepNet/'
model_path = 'models/6DRepNet_300W_LP_BIWI.pth'

# settings
method_name = '6DRepNet'
training_set = '300W-LP'
transformations = get_SixDRepNet_Image_Transforms() # image augs
model_output_format = 'ypr' # model will output ypr labels
model_pred_transform = SixDRepNet_predictions_to_ypr_eulers # use this to normalize the model output to Euler angles in degree

# variants to evaluate
variants = [('Biwi+', {}),
            ('Biwi+', {'bbox_transform': 'Biwi+->MTCNN'}),
            ('Biwi+_non_cal', {}),
            ('Biwi+_non_cal', {'bbox_transform':'Biwi+->MTCNN'}),
            ('FSA-Net', {}),
            ('FSA-Net', {'bbox_transform': 'Biwi+->MTCNN'}),
            ('FSA-Net', {'bbox_transform': 'Biwi+'})]
report_formats = ['pyr', 'ypr']
# kwargs = bbox_transform=None


table = Table(['Method', 'MAE', 'Pitch', 'Yaw', 'Roll', 'Format', 'Test Set', 'Num Images', 'Training Set', 'Crop', 'Unsup. Training on Test Set', 'Calibrated Biwi'])
fixed_infos = {'Method': method_name, 'Training Set': training_set, 'Unsup. Training on Test Set': Table.no()}

# Reported results from the Paper
res = {'Method': '6DRepNet (paper)', 'MAE': 3.47, 'Pitch': 4.48, 'Yaw': 3.24, 'Roll': 2.68, 'Test Set': 'Biwi'}
table.add(res)
table.add_horizontal_line()

# eval loop
for variant, kwargs in variants:

    dataset = BiwiDataset(transforms=transformations, variant=variant, **kwargs)
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