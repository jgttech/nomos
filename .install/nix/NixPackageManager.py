from subprocess import call
from os import path


class NixPackageManager:
    # The format of these variables is designed to be used
    # as shell commands, so they are pre-formatted for the
    # subprocess.call command.
    nix_run = ["sudo", "-i", "nix", "run"]
    hm_profile = "#homeConfigurations.kronos.activationPackage"
    nix_features = [
        "--extra-experimental-features", "flakes",
        "--extra-experimental-features", "nix-command"
    ]

    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir
        self.hm_nix_dir = path.join(f"{base_dir}", "nix", "home-manager")

    def home_manager_install(self) -> None:
        # Actuall install and activate Nix "home manager".
        hm_profile = f"{self.hm_nix_dir}{self.hm_profile}"
        nix_hm = self.nix_run + [hm_profile] + self.nix_features

        # Run the install command, itself.
        call(nix_hm)

        # Create a symbolic link to the .xsessionrc to make
        # sure cursors are the right size.
        xsessionrc_path = path.join(f"{self.base_dir}", "xserver/xsessionrc")

        call(["ln", "-sf", xsessionrc_path, ".xsessionrc"])

    # home-manager switch --flake ~/.nomos/nix/home-manager#kronos
    def home_manager_update(self) -> None:
        pass

    def node_version_manager_install(self) -> None:
        # INSTALL: Node Version Manager
        # call(["wget", "-qO-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh", "|", "bash"])
        pass
