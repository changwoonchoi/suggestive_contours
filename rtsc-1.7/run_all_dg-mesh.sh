#!/bin/bash

for i in {0..99}
do
    echo ./rtsc ../data/dystroke/robin/dynamic_mesh/frame_$(printf "%d" $i).ply ../data/dystroke/robin/predict/$(printf "%d" $i).txt ../output/dystroke/robin/predict/$(printf "%d" $i).ppm
done