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

# Refresh the shell instance.
source ~/.bashrc

# This queries the nix packages, uninstalls them (which is
# no packages) and then runs home-manager process (on the
# daemon) to "install" home-manager at the non-root level.
nix-env -q
nix-env --uninstall "*"
home-manager switch --flake ~/.nomos/nix/home-manager#kronos

# Refresh the shell instance.
source ~/.bashrc
