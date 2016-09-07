#!/bin/sh
python train.py /preprocessedData
echo "this is some state to return to the user" > /modelState/state.txt
