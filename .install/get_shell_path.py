from os import environ, path

def get_shell_path(shell_file: str):
    return path.join(environ["HOME"], shell_file)
