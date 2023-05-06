from os import path, mkdir
from env import shells, nix_config_path, nix_config_dir, post_install_instructions
from utils.get_unconfigured_shells import get_unconfigured_shells
from utils.get_scripts import get_scripts
from utils.get_shells import get_shells
from utils.has_str import has_str


def install():
    environments = get_unconfigured_shells(get_shells(shells))
    envs = get_scripts(environments)
    has_bashrc = has_str("bashrc", envs)
    has_zshrc = has_str("zshrc", envs)

    # Create the nix configuration file, if it does not exist.
    if not path.isfile(nix_config_path):
        mkdir(nix_config_dir)

        with open(nix_config_path, "w") as fp:
            fp.write(f"experimental-features = nix-command flakes\n")

    # Write out the environment files data.
    for env_file in envs:
        with open(env_file, "a") as fp:
            for line in envs[env_file]:
                fp.write(line)

    # Messages after the initial install.
    if has_bashrc:
        print("Refresh your shell: \"source ~/.bashrc\"")
    elif has_zshrc:
        print("Refresh your shell: \"source ~/.zshrc\"")

    print(post_install_instructions)
