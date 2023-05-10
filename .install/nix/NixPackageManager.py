from subprocess import call
from os import path


class NixPackageManager:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir

    def home_manager_install(self) -> None:
        # Actuall install and activate Nix "home manager".
        hm_nix_dir = path.join(f"{self.base_dir}", "nix", "home-manager")
        hm_profile = "#homeConfigurations.kronos.activationPackage"
        nix_command = "--extra-experimental-features nix-command"
        nix_flakes = "--extra-experimental-features flakes"
        nix_run = ["sudo", "-i", "nix", "run"]
        hm_cmd = [
            f"{hm_nix_dir}{hm_profile}",
            nix_command,
            nix_flakes,
        ]

        # Run the install command, itself.
        call(nix_run + hm_cmd)

        # Create a symbolic link to the .xsessionrc to make
        # sure cursors are the right size.
        xsessionrc_path = path.join(f"{self.base_dir}", "xserver/xsessionrc")

        call(["ln", "-sf", xsessionrc_path, ".xsessionrc"])

    def home_manager_update(self) -> None:
        print(f"home_manager_update {self.base_dir}")

    def node_version_manager_install(self) -> None:
        print(f"node_version_manager_install {self.base_dir}")
