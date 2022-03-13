#!/bin/bash

protoc --python_out=./process --proto_path=./process process/files/**/*.proto

if [[ ! -z $1 ]]; then
    cd process
    rm ./raw/*
    cp $1/*.json ./raw/
    cp $1/*.txt ./raw/
    for f in $1/*.pb; do
        protoc --decode_raw < $f > ${f}txt
    done
    cp $1/*.pbtxt ./raw/
    python3 process.py $1
    cd ..
fi

BUILD_PATH=docs npm run build
