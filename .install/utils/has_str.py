def has_str(shell_env: str, envs: list[str]) -> bool:
    return bool(len(list(filter(lambda env: shell_env in env, envs))))
