from os import path
from get_shell_path import get_shell_path

# Detects if the given shell file exists or not.
# If the file exists it is added to a list of files
# that exist and returned.
def get_shells(shell_files: [str]) -> [str]:
    existing_shells = []

    for shell_file in shell_files:
        shell_path = get_shell_path(shell_file)
        is_dotfile = shell_file[0] == "."
        is_file = path.isfile(shell_path)

        if is_dotfile and is_file:
            existing_shells.append(shell_file)

    return existing_shells
