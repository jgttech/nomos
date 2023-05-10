from sys import argv
from install import install

if __name__ == "__main__":
    # The process to run for setting up the nix
    # package management system
    proc = argv[1]

    # Should be the diretory that the initial "install.sh"
    # script is executing from.
    base_dir = argv[2]

    if proc == "install":
        install(base_dir)
