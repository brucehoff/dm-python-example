#!/bin/sh
python train.py /trainingData
echo "this is some state to return to the user" > /modelState/state.txt
