#!/bin/bash
conda create -y --name hpp_tensorflow python=3.6
eval "$(conda shell.bash hook)"
conda activate hpp_tensorflow
pip3 install --no-input tqdm
pip3 install --no-input pillow
# FSA
conda install -y -c anaconda cudatoolkit=9.0 # needed by tensorflow
pip3 install --no-input tensorflow-gpu==1.12.0
pip3 install --no-input Keras==2.1.6
pip3 install --no-input h5py==2.10.0 --force-reinstall
pip3 install --no-input opencv-python # or conda install -c conda-forge opencv
# FSA version is opencv-python==4.1.1.26
# WHENet
pip3 install --no-input efficientnet==0.0.4
pip3 install --no-input scikit-image  #needed by efficientnet preprocessing.py
# everything else should be available from FSA
