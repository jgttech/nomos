{ config, pkgs, ... }: {
  programs = {
    home-manager.enable = true;
    bash.enable = true;
    zsh.enable = true;
  };

  nixpkgs.config = {
    allowUnfree = true;
    allowUnfreePredicate = _: true;
  };

  home = {
    username = "kronos";
    homeDirectory = "/home/kronos";
    stateVersion = "22.11";

    packages = with pkgs; [
      vim
      vscodium
      brave
      librewolf
      postman
      insomnia
      zsh
      docker
      docker-compose
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
    ];
  };
}
