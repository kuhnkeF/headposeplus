#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate hpp_tensorflow
python eval_FSA-Net.py
python eval_WHENet.py

conda activate hpp_pytorch
python eval_6DRepNet.py
python eval_Hopenet.py
python eval_PADACO.py
python eval_RCRw_from_300W-LP.py
python eval_RCRw_from_SynHeadPP.py
