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
