#!/bin/bash
source /etc/profile.d/modules.sh
module load boost/1.58.0
module load gcc/5.3.0

# Switching from a tensorflow version to another
# GPU version
module load cuda/8.0
module load cudnn/5.1-cuda-8.0


export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.1-cp35-cp35m-linux_x86_64.whl
pip3 install --upgrade --user $TF_BINARY_URL

# CPU version
# pip3 uninstall -y tensorflow
# export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp35-cp35m-linux_x86_64.whl
# pip3 install --user $TF_BINARY_URL

cd /home/gdebard/tests
export PYTHONPATH=.
python3 ae_test.py
