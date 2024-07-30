#!/bin/bash

ROOT_DIR=$(dirname "$(dirname "$(realpath "$0")")")
cd "$ROOT_DIR" || exit

export PYTHONPATH="${ROOT_DIR}/function_package"

python3 -m unittest discover -s tests -p "test.py"
