#!/usr/bin/bash

# Detect the dir of this script to use as the base
# dir path for invoking the python install script.
SYSTEM_INFERABLE_DIR="$(dirname -- "${BASH_SOURCE[0]}")"

# Setup the system using this Python 3 script.
python3 ${SYSTEM_INFERABLE_DIR}/.install
