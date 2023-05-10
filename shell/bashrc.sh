#!/usr/bin/env bash
# home-manager switch
function hms() {
    # Switches to the user flake and applies its configuration which DOES install all the packages.
    home-manager switch --flake ${HOME}/${__SYSTEM_BASE_DIR}/nix/home-manager#kronos

    # This is needed to detect all the Nix installed packages.
    sudo ln -sf ~/.nix-profile/share/applications/* /usr/share/applications/

    # This symbolic link is needed to link the "zsh" location in the expected area
    sudo ln -sf "${HOME}/.nix-profile/bin/zsh" /usr/bin/zsh
}

# home-manager update
function hmu() {
    sudo -i nix flake update ${HOME}/${__SYSTEM_BASE_DIR}/nix/home-manager \
        --extra-experimental-features nix-command \
        --extra-experimental-features flakes

    hms;
}

# home-manager directory
function hmd() {
    # Change into the directory that the nix home-manager configuration are kept.
    cd ${HOME}/${__SYSTEM_BASE_DIR}/nix/home-manager;
}
