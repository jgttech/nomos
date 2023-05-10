from utils.get_system_source_dir import get_system_source_dir
from utils.get_shell_path import get_shell_path
from env import system_base_dir, system_base_name


def get_scripts(envs: list[str]):
    scripts = {}

    for env in envs:
        scripts[get_shell_path(env)] = [
            "\n# .nomos configuration\n",
            f"{system_base_dir}={system_base_name}\n",
            f"{get_system_source_dir(env)}\n"
        ]

    return scripts
