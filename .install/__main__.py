from os import path
from get_shells import get_shells
from get_shell_path import get_shell_path
from get_unconfigured_shells import get_unconfigured_shells
from env import shells, system_base_dir, system_source_dir

has_bashrc = False
has_zshrc = False

for shell_file in get_unconfigured_shells(get_shells(shells)):
    shell_path = get_shell_path(shell_file)
    shell_source = system_source_dir(shell_file)

    if not has_bashrc and shell_file == ".bashrc":
        has_bashrc = True

    if not has_zshrc and shell_file == ".zshrc":
        has_zshrc = True

    with open(shell_path, "a") as fp:
        fp.write("\n# .nomos configuration\n")
        fp.write(f"{system_base_dir}\n")
        fp.write(f"{shell_source}\n")

# Run post_install operations but these operations
# should only run when the .bashrc file is detected
# as having been registered.
if has_bashrc:
    import post_install
elif has_zshrc:
    print("ZSH registered")
