#!/usr/bin/bash
alias sn="sudo -i nix"
alias hm="home-manager"

# home-manager install
function hmi() {
    source "${HOME}/.bashrc"

    # This does the initial setup and activation of nix home-manager.
    # This does NOT install the packages, this is just an initial setup step.
    sudo -i nix run ${HOME}/${__SYSTEM_BASE_DIR}/nix/home-manager#homeConfigurations.kronos.activationPackage

    # This symbolic link is needed to set the cursor size correctly.
    ln -sf "${HOME}/${__SYSTEM_BASE_DIR}/xserver/xsessionrc" .xsessionrc

    # Install NVM (Node Version Manager)
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    source "${HOME}/.bashrc"

    # Install the LTS version of NodeJS and set it as the default.
    nvm install --lts
    nvm use --lts --default
    source "${HOME}/.bashrc"
}

# home-manager switch
function hms() {
    # Switches to the user flake and applies its configuration which DOES install all the packages.
    home-manager switch --flake ${HOME}/${__SYSTEM_BASE_DIR}/nix/home-manager#kronos

    # This symbolic link is needed to link the "zsh" location in the expected area
    sudo ln -sf "${HOME}/.nix-profile/bin/zsh" /usr/bin/zsh

    # This is needed to detect all the Nix installed packages.
    sudo ln -sf ~/.nix-profile/share/applications/* /usr/share/applications/
}

# home-manager update
function hmu() {
    sudo -i nix flake update ${HOME}/${__SYSTEM_BASE_DIR}/nix/home-manager
    hms;
}

# home-manager directory
function hmd() {
    # Change into the directory that the nix home-manager configuration are kept.
    cd ${HOME}/${__SYSTEM_BASE_DIR}/nix/home-manager;
}
