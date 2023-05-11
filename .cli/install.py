from os import path, mkdir
from env import shells, nix_config_path, nix_config_dir
from utils.get_unconfigured_shells import get_unconfigured_shells
from utils.get_scripts import get_scripts
from utils.get_shells import get_shells
from nix.NixPackageManager import NixPackageManager


def install(base_dir: str):
    environments = get_unconfigured_shells(get_shells(shells))
    envs = get_scripts(environments)

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

    nix = NixPackageManager(base_dir)

    nix.system_config_install()
    nix.home_manager_install()
    nix.home_manager_update()
