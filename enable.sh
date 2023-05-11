#!/usr/bin/env bash
sudo -i nix-env -q
nix-env -q

home-manager switch --flake ~/.nomos/nix/home-manager#kronos

Create the symbolic link for ZSH from the nix package.
sudo ln -sf "${HOME}/.nix-profile/bin/zsh" /usr/bin/zsh

This is needed to detect all the Nix installed packages.
sudo ln -sf ~/.nix-profile/share/applications/* /usr/share/applications/

gnome-session-quit
