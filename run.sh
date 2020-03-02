#/bin/bash

export PATH=/home/minho2/program/anaconda3/bin/python:$PATH

echo "input1 - input2 - output1 - output2 - interleaved"

read input1 input2 output1 output2 interleaved

python reform.py $input1 $output1 &
python reform.py $input2 $output2 &

sleep 100

python interleaved.py $output1 $output2 $interleaved

echo "all jobs finished"
