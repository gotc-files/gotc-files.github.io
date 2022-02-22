#!/bin/bash

protoc --python_out=./process --proto_path=./process process/files/**/*.proto

cd process
python3 process.py
cd ..

BUILD_PATH=docs npm run build
