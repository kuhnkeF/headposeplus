# use RCRw trained on 300W-LP to evaluate on Biwi variants

from hpp.RCR import load_model, get_RCR_image_transforms
from hpp import Table, BiwiDataset
from hpp.eval_pytorch import eval_pytorch_model

# paths
result_path = 'results/RCRw300WLP/'
model_path_A = 'models/RCRw_from_300WLP_F.tar'
model_path_B = 'models/RCRw_from_300WLP_T.tar'

# settings
method_name = 'RCRw' # journal variant
training_set = '300W-LP'
transformations = get_RCR_image_transforms() # image augs
model_output_format = 'pyr'  # model will output pyr labels
model_pred_transform = None  # use this to normalize the model output to Euler angles in degree

# variants to evaluate
variants = [('Biwi+', {}),
            ('Biwi+_non_cal', {}),
            ('FSA-Net', {'bbox_transform': 'Biwi+'})]
report_formats = ['pyr', 'ypr']
# kwargs = bbox_transform=None

# eval loop
table = Table(['Method', 'MAE', 'Pitch', 'Yaw', 'Roll', 'Format', 'Test Set', 'Num Images', 'Training Set', 'Crop', 'Unsup. Training on Test Set', 'Calibrated Biwi'])
fixed_infos = {'Method': method_name, 'Training Set': training_set, 'Unsup. Training on Test Set': Table.yes()}

for variant, kwargs in variants:

    dataset = BiwiDataset(transforms=transformations, variant=variant, **kwargs)
    err = eval_pytorch_model(load_model(model_path_A, model_path_B), model_output_format, dataset, model_pred_transform)

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