#!/usr/bin/env bash
sudo -i nix-env -q
nix-env -q

home-manager switch --flake ~/.nomos/nix/home-manager#kronos
