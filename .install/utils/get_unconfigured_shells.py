from os import path
from utils.get_shell_path import get_shell_path
from utils.get_system_source_dir import get_system_source_dir
from env import system_base_dir

# This reads through each of the shell configuration files
# and checks for the system base directory and the source
# command that links everything together. If it is not found
# then it gets added to the unconfigured_shells list.


def get_unconfigured_shells(shell_files: list[str]) -> list[str]:
    unconfigured_shells = []

    for shell_file in shell_files:
        shell_path = get_shell_path(shell_file)
        shell_source = get_system_source_dir(shell_file)

        with open(shell_path, "r") as fp:
            system_not_found = True
            source_not_found = True

            for line in fp:
                ln = line.strip()
                is_valid = bool(len(ln)) and ln[0] != "#"

                if is_valid:
                    if system_base_dir in ln:
                        system_not_found = False

                    if shell_source in ln:
                        source_not_found = False

            if system_not_found and source_not_found and shell_file not in unconfigured_shells:
                unconfigured_shells.append(shell_file)

    return unconfigured_shells
