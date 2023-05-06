from os import environ, path

system_base_name = ".nomos"
system_base_dir = "export __SYSTEM_BASE_DIR"

# A list of the shell files we want to detect.
shells = [
    ".zshrc",
    ".bashrc",
]

nix_config = "nix.conf"
nix_config_dir = path.join(environ["HOME"], ".config", "nix")
nix_config_path = path.join(nix_config_dir, nix_config)

post_install_instructions = """
[NEXT STEPS]

  1. Run: hmi
    - This sets up the home-manager.

  2. Run: hms
    - This installs and activates the
      home-manager packages.

  1. (Optional) Ensure all terminals fonts is set to:
    - "MesloLGS NF" (for Powerlevel10k)

  3. (Optional) Configure Blackbox Terminal:
    - Enable "Remember Window Size"
    - Set "padding" to "6"
    - Enable "Easy Copy & Paste"
    - Theme is 3rd dark theme
    - Enable "Show Header"
    - Enable "Draw Line Under Header Bar"

  4. Run: zsh
    - This will run ZSH and prompt you
      to configure ZSH. Just make sure
      this creates the ".zshrc" file.

  5. Run: ~/.nomos/install.sh
    - This will register this system config
      with the ZSH environment.

  6. Run: ~/.nomos/setup.sh
    - This adds the nix ZSH package to the
      avaiable system shells and logs the
      user out.
"""
