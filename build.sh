#!/bin/sh
PWD=$(pwd)
export PYTHONPATH="$PWD:$PWD/Header:$PWD/ID:$PWD/Process"
python -B "Lav/compile.py"
