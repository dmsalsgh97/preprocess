#/bin/bash

export PATH=/home/minho2/program/anaconda3/bin/python:$PATH
export PATH=//home/minho2/.local/lib/pypy3.6:$PATH

echo "input1 - input2 - output1 - output2 - interleaved"

read input1 input2 output1 output2 interleaved

pypy3 reform.py $input1 $output1 &
pypy3 reform2.py $input2 $output2 &

sleep 3

python interleaved.py $output1 $output2 $interleaved

echo "all jobs finished"

