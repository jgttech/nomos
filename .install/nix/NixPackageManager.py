from subprocess import call
from os import path


class NixPackageManager:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir

    def home_manager_install(self) -> None:
        # Actuall install and activate Nix "home manager".
        home_manager_path = "home-manager#homeConfigurations.kronos.activationPackage"
        home_manager_profile = path.join(f"{self.base_dir}", home_manager_path)

        call(["sudo", "-i", "nix", "run", home_manager_profile])

        # Create a symbolic link to the .xsessionrc to make
        # sure cursors are the right size.
        xsessionrc_path = path.join(f"{self.base_dir}", "xserver/xsessionrc")

        call(["ln", "-sf", xsessionrc_path, ".xsessionrc"])

    def home_manager_update(self) -> None:
        print(f"home_manager_update {self.base_dir}")

    def node_version_manager_install(self) -> None:
        print(f"node_version_manager_install {self.base_dir}")
