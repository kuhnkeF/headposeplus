#!/bin/bash
conda create -y --name hpp_pytorch python=3.9
eval "$(conda shell.bash hook)"
conda activate hpp_pytorch
pip3 install --no-input tqdm
pip3 install --no-input SixDRepNet==0.1.2
# SixDRepNet will install pytorch, I used
#SixDRepNet==0.1.2
#torch==1.13.1
#torchvision==0.14.1
