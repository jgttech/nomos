#!/usr/bin/env bash

# Detect the dir of this script to use as the base
# dir path for invoking the python install script.
BASE_DIR="$(dirname -- "${BASH_SOURCE[0]}")"

# Setup the system using this Python 3 script.
python3 ${BASE_DIR}/.install ${BASE_DIR}
