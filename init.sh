#!/usr/bin/env bash

# Writes the current shell instance into the system registers shells
# this way we can switch to ZSH without any problems.
sudo echo $(which zsh) >> /etc/shells

# Actually switch which shell we use.
chsh -s $(which zsh)

# Log out and log back in to apply changes.
gnome-session-quit
