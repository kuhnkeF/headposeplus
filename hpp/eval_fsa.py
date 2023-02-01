from .calc_error import calc_error
from keras import backend as K
from .FSANet import load_model


def eval_fsa_model(models_paths, model_output_format, dataset, save_data_and_load_if_available=False):
    if model_output_format == 'pyr':
        raise NameError('FSA-Net output is ypr')

    images, labels_pyr, labels_ypr = dataset.get_all_items(saveload=save_data_and_load_if_available)

    # call this before loading the model
    K.clear_session()
    K.set_learning_phase(0)

    # load the models (~ 10800MiB on GPU)
    model = load_model(*models_paths)
    print('evaluating FSA-Net...')
    preds = model.predict(images)

    # errors
    return calc_error(preds, model_output_format, labels_ypr, model_output_format)
