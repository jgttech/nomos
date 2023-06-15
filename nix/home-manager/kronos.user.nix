{ config, pkgs, ... }: {
  programs = {
    home-manager.enable = true;
  };

  nixpkgs.config = {
    allowUnfree = true;
    allowUnfreePredicate = _: true;
  };

  home = {
    username = "kronos";
    homeDirectory = "/home/kronos";
    stateVersion = "22.11";

    # [PACKAGES.START]
    packages = with pkgs; [
      vim
      vscodium
      brave
      librewolf
      postman
      insomnia
      zsh
      gh
      htop
      btop
      keychain
      ngrok
      blackbox-terminal
      fira-code
      meslo-lgs-nf
      zsh-powerlevel10k
      oh-my-zsh
      pdm
      go
      rustup
      zig
      keepassxc
      filezilla
      xclip
      oh-my-zsh
      signal-desktop
      tidal-hifi
      vlc
      onlyoffice-bin
      vimPlugins.vim-plug
    ];
    # [PACKAGES.END]
  };
}
