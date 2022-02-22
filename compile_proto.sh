#!/bin/bash

protoc --python_out=./process --proto_path=./process process/files/**/*.proto
