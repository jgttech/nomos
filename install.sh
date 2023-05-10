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

# Re-run the nix command because, for whatever reason
# the home-manager instance does not quite exist and
# re-running this, somehow, makes it work again...
sudo -i nix run \
    ~/.nomos/nix/home-manager#homeConfigurations.kronos.activationPackage \
    --extra-experimental-features nix-command \
    --extra-experimental-features flakes

# Refresh the shell instance.
source ~/.bashrc
