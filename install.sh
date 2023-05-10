#!/usr/bin/env bash
# Detect the dir of this script to use as the base
# dir path for invoking the python install script.
BASE_DIR="$(dirname -- "${BASH_SOURCE[0]}")"

# Install Nix package manager
sh <(curl -L https://nixos.org/nix/install) --daemon

# Refresh the shell instance.
source ~/.bashrc

# Setup the system using this Python 3 script.
python3 ${BASE_DIR}/.cli install ${BASE_DIR}

# Refresh and enable
gnome-terminal -- /bin/bash -c "${BASE_DIR}/enable.sh; exec bash" && exit
