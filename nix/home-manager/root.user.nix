{ config, pkgs, ... }: {
  programs.home-manager.enable = true;

  nixpkgs.config = {
    allowUnfree = true;
    allowUnfreePredicate = _: true;
  };

  home = {
    username = "root";
    homeDirectory = "/root";
    stateVersion = "22.11";

    packages = with pkgs; [
      vim
      zsh
      htop
      btop
      meslo-lgs-nf
      zsh-powerlevel10k
      oh-my-zsh
    ];
  };
}
